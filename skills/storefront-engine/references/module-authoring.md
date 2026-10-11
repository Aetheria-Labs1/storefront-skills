# Custom Cart Module Authoring

Use one complete Lexsis source section in `composition_ops` with
`operation:"upsert"`, a stable `module_id`, and `source`. An upsert with source
replaces the whole source, including HTML, CSS and script. Omitting source
preserves it when changing placement, enabled state or `visible_when`.
Renderer-owned cart islands must not be embedded in a custom module.

## Lifecycle and state

`section` and `lifecycle.root` are the renderer's
`[data-cart-custom-module="<module_id>"]` wrapper, not the authored inner
`<section>`. `lifecycle.query(selector)` returns the first matching descendant
or null; `queryAll` returns an array. Both exclude island internals.
Use `lifecycle.on(target,event,handler)` for managed listeners. Timers, frames,
observers and `addCleanup` are managed too; unmount stops them.

The compiler rejects `window` and `document` access. Do not reach outside the
wrapper, fetch Shopify directly, write cart storage or dispatch fake response
events. Use the cart commands below.

`lifecycle.cart` is a deeply frozen CartSnapshot. Subscribe with
`lifecycle.onCart((snapshot,previous) => {...})` during initialization: the
getter throws before the store currency and prices are available. The first
callback receives `previous:null`; later callbacks run after mutation/reward
settlement, at most once per frame. The returned unsubscribe function stops
the listener early; unmount cleans it up automatically. During a mutation,
the getter reports pending status with confirmed merchandise amounts.

Read `lexsis_cart.capabilities` for `snapshot_schema`, `module_lifecycle`,
`commands`, and `conditions`. Snapshot fields:

- `status`, `itemCount`, `currency`, `subtotal`, `compareAtSubtotal`, `savings`
- `discountCodes`: code and applicability
- `lines`: identity, variant/product IDs, handle, titles, quantity, prices,
  line total, selling plan, attributes, tags, collections and reward-gift flag
- `rewards.next`: id, type, title, threshold and remaining Money, or null
- `rewards.unlocked`: id/type/title; `chosenGiftVariantId`: variant ID or null
- `context`: market, locale, pageHandle, pageType, UTM fields and customer flags

Money is `{amount:"552.00",currencyCode:"INR",minor:55200}`. Use the snapshot's
currency, never an invented default. Summary and modules use the same confirmed
selectors: subtotal is after line discounts, before shipping/tax and remaining
order discounts; savings includes those order discounts without counting line
discounts twice. Reward remaining uses paid-price eligibility, excluding gifts
from qualifying spend. Eligibility is not proof of Shopify discount application.
Tags/collections depend on available metadata; customer flags default false
without a host session provider.

## Commands and responses

Dispatch a bubbling `CustomEvent` from `section` with a unique `requestId` in
`detail`. Responses arrive on that same **wrapper** and bubble. Listen on
`section`, not only on an authored inner element. Every command emits
`:pending`, `:accepted`, `:confirmed`, then terminal `:success` or `:error`.
Errors can arrive before any intermediate phase. Filter responses by requestId.

| Event | Additional detail fields |
| --- | --- |
| `lx:cart:add-items` | `items:[{variantId,quantity,sellingPlanId?,attributes?}]`, `openCart?` |
| `lx:cart:update-line` | `lineId`, `quantity` |
| `lx:cart:remove-line` | `lineId` |
| `lx:cart:apply-code` | `code` |
| `lx:cart:remove-code` | `code` |
| `lx:cart:set-attributes` | `attributes` |
| `lx:cart:set-note` | `note` |
| `lx:cart:choose-gift` | `rewardId`, `variantId` |
| `lx:cart:swap-variant` | `lineId`, `variantId`, optional `quantity` |

Use the live capabilities for exact payload types, limits and error codes.
Reuse the same requestId only to replay the identical request; a changed payload
fails with `request_id_conflict`. A terminal replay returns the recorded outcome
without a second mutation. `partial_add`/`partial_swap` require inspecting the
current cart; do not blindly retry with a new ID. Success means settled, not
just accepted. A sample preview handles commands in memory and blocks checkout.

## Complete upsell with live state

This is a compiler-tested template. Replace the example variant GID and item
label with a verified, available catalog variant before saving. The template
does not invent a price or discount. It displays the profile's next reward,
updates after cart changes, and disables adding when the variant is present.

```html lexsis-cart-example
<!-- section: matching-item -->
<section class="upsell" data-variant-id="gid://shopify/ProductVariant/123">
  <h3>Add a matching item</h3>
  <p data-remaining hidden></p>
  <button type="button" data-lx-control="add-upsell" disabled>Add item</button>
  <p data-result role="status" aria-live="polite"></p>
  <style>
    .upsell { padding: 16px; border: 1px solid var(--lx-border-color); }
    .upsell button { min-height: 44px; padding: 8px 16px; }
    .upsell button:disabled { opacity: 0.6; }
  </style>
  <script>
    const content = lifecycle.query('[data-variant-id]');
    const button = lifecycle.query('[data-lx-control="add-upsell"]');
    const remaining = lifecycle.query('[data-remaining]');
    const result = lifecycle.query('[data-result]');
    const variantId = content.dataset.variantId;
    let requestId = null;
    let sequence = 0;
    let present = false;
    const refreshButton = () => {
      button.disabled = Boolean(requestId) || present;
      button.textContent = requestId ? 'Adding...' : present ? 'Already in cart' : 'Add item';
    };
    lifecycle.onCart((cart) => {
      present = cart.lines.some((line) => line.variantId === variantId);
      const next = cart.rewards.next;
      remaining.hidden = !next;
      remaining.textContent = next
        ? new Intl.NumberFormat(cart.context.locale || undefined, {
            style: 'currency', currency: next.remaining.currencyCode
          }).format(Number(next.remaining.amount)) + ' to go for ' + next.title
        : '';
      refreshButton();
    });
    lifecycle.on(button, 'click', () => {
      if (requestId || present) return;
      requestId = 'upsell-' + Date.now() + '-' + (++sequence);
      refreshButton();
      result.textContent = '';
      section.dispatchEvent(new CustomEvent('lx:cart:add-items', {
        bubbles: true,
        detail: { requestId, items: [{ variantId, quantity: 1 }], openCart: true }
      }));
    });
    lifecycle.on(section, 'lx:cart:add-items:pending', (event) => {
      if (event.detail.requestId === requestId) result.textContent = 'Adding item...';
    });
    lifecycle.on(section, 'lx:cart:add-items:success', (event) => {
      if (event.detail.requestId !== requestId) return;
      requestId = null;
      present = lifecycle.cart.lines.some((line) => line.variantId === variantId);
      result.textContent = 'Added to your cart';
      refreshButton();
    });
    lifecycle.on(section, 'lx:cart:add-items:error', (event) => {
      if (event.detail.requestId !== requestId) return;
      requestId = null;
      result.textContent = event.detail.message;
      refreshButton();
    });
  </script>
</section>
```

To hide this whole upsell once added, include this sibling of `source` in the
upsert, using the same verified variant GID:

```json
{
  "visible_when": {
    "op": "AND",
    "clauses": [{"field": "cart.has_variant_id", "op": "neq", "value": "gid://shopify/ProductVariant/123"}]
  }
}
```

For a trust row on nonempty carts, use `cart.item_count`, `op:"gt"`, `value:0`.
Rules apply to optional built-ins as well. Required cart lines, summary and
checkout cannot be hidden. Hidden modules use `hidden` and leave the
accessibility tree; they remain in the DOM for live visibility changes.
Disabled modules (`set_enabled:false`) are omitted from generated sections.

## Bind text and conditions without JavaScript

```html lexsis-cart-example
<!-- section: next-reward -->
<section>
  <p data-lx-if="rewards.next.remaining.minor &gt; 0">
    Only <strong data-lx-text="rewards.next.remaining"></strong> to go for
    <span data-lx-text="rewards.next.title"></span>.
  </p>
</section>
```

Money bindings format the store currency. Expressions support comparisons,
`!`, `&&`, `||`, parentheses and the documented predicates, including
`reward.unlocked('reward-id')`. They are parsed, never evaluated as JavaScript.
Unknown paths/functions fail compilation. Read the complete field/operator
inventory from capabilities; money comparisons use minor units.

## CSS scope

Compiled module CSS is wrapped in
`@scope ([data-cart-custom-module="<module_id>"])`. Author ordinary selectors;
do not add a global page selector or a second manual cart wrapper. Compiler
`:root`/`:host` token selectors are adapted to the module scope.
Scoped module CSS belongs to cart design; profile `custom_css` has precedence.
Do not depend on page CSS reaching the cart. Use `references/styling-hooks.md`
for profile-wide seams and inline-style exceptions.
