# Custom Cart Module Authoring

Use one complete Lexsis source section in `composition_ops` with
`operation:"upsert"`, a stable `module_id`, and `source`. An upsert with source
replaces the whole source, including HTML, CSS and script. Omitting source
preserves it when changing placement, enabled state or `visible_when`.
Renderer-owned cart islands must not be embedded in a custom module.

## Lifecycle and state

`root` and `lifecycle.root` are the renderer's
`[data-cart-custom-module="<module_id>"]` wrapper, not the authored inner
`<section>`. `lifecycle.query(selector)` returns the first matching descendant
or null; `queryAll` returns an array. Both exclude island internals.
Use `lifecycle.on(target,event,handler)` for managed listeners. Timers, frames,
observers and `addCleanup` are managed too; unmount stops them.
`section` remains a deprecated alias of `root`. `lifecycle.setVisible(boolean)`
controls the wrapper and authored top-level section; an authored hidden root
section produces a compile warning.

The compiler rejects `window` and `document` access. Do not reach outside the
wrapper, fetch Shopify directly, write cart storage or dispatch fake response
events. Use the cart commands below.

Variant availability is owned by the runtime. Put `data-lx-variant="<variant gid>"`
on every element that sells one variant (set it from JS when the variant follows
other choices); the runtime disables and slashes sold-out variants, labels them
for screen readers and refuses their adds. Never keep your own sold-out state or
learn it from an add error. `lifecycle.catalog.variants(ids)` returns live
availability keyed by gid for logic only (default selection, pack eligibility);
it resolves to `{}` without a store token and after unmount. A module that
dispatches `lx:cart:add-items` without `data-lx-variant` fails publish
(`variant_availability`).

`lifecycle.cart` is a deeply frozen CartSnapshot. Subscribe with
`lifecycle.onCart((snapshot,previous) => {...})` during initialization: the
getter throws before the store currency and prices are available. The first
callback receives `previous:null`; later callbacks run after mutation/reward
settlement, at most once per frame. The returned unsubscribe function stops
the listener early; unmount cleans it up automatically. During a mutation,
the getter reports pending status with confirmed merchandise amounts.

Read `lexsis_cart.capabilities` for `snapshot_schema`, `module_lifecycle`,
`commands`, and `conditions`. Snapshot fields:

- `status`, `itemCount`, `currency`, `subtotal`, `total`, `compareAtSubtotal`, `savings`
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

Dispatch a bubbling `CustomEvent` from `root` with a unique `requestId` in
`detail`. Responses arrive on that same **wrapper** and bubble. Listen on
`root`, not only on an authored inner element. Every command emits
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

Presentation commands have no request lifecycle (nothing is written, so no
`:pending` or `:success` responses):

| Event | Detail fields |
| --- | --- |
| `lx:cart:open-sheet` | `sheetId` (a `region: "sheet"` module id), optional `context` object |
| `lx:cart:close-sheet` | optional `sheetId` |

A `region: "sheet"` module renders hidden inside the cart and slides up over the
cart content when opened. Any element inside the cart with
`data-lx-open-sheet="<module id>"` (plus optional `data-lx-sheet-context` JSON)
opens it on click; `data-lx-close-sheet` closes it. An offer slot with
`presentation.detail_sheet: "<module id>"` makes each recommendation card a
trigger with `{product_id, variant_id, handle, title, price, image}` as context.
The sheet module's `root` receives `lx:cart:sheet-opened` `{sheetId, context}`
and `lx:cart:sheet-closed`, and carries the context as `data-lx-sheet-context`
JSON. Escape, the backdrop, swipe-down and closing the cart all close the sheet.
Sheet opens and closes are tracked automatically (`lx_cart_sheet_open` /
`lx_cart_sheet_close` in cart analytics); a module emits nothing for that.

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
<section class="upsell">
  <h3>Add a matching item</h3>
  <p data-remaining hidden></p>
  <button type="button" data-lx-control="add-upsell" data-lx-variant="gid://shopify/ProductVariant/123" disabled>Add item</button>
  <p data-result role="status" aria-live="polite"></p>
  <style>
    .upsell { padding: 16px; border: 1px solid var(--lx-border-color); }
    .upsell button { min-height: 44px; padding: 8px 16px; }
    .upsell button:disabled { opacity: 0.6; }
  </style>
  <script>
    const button = lifecycle.query('[data-lx-control="add-upsell"]');
    const remaining = lifecycle.query('[data-remaining]');
    const result = lifecycle.query('[data-result]');
    const variantId = button.dataset.lxVariant;
    let requestId = null;
    let sequence = 0;
    let present = false;
    const refreshButton = () => {
      button.disabled = Boolean(requestId) || present || button.dataset.lxAvailable === 'false';
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
      root.dispatchEvent(new CustomEvent('lx:cart:add-items', {
        bubbles: true,
        detail: { requestId, items: [{ variantId, quantity: 1 }], openCart: true }
      }));
    });
    lifecycle.on(root, 'lx:cart:add-items:pending', (event) => {
      if (event.detail.requestId === requestId) result.textContent = 'Adding item...';
    });
    lifecycle.on(root, 'lx:cart:add-items:success', (event) => {
      if (event.detail.requestId !== requestId) return;
      requestId = null;
      present = lifecycle.cart.lines.some((line) => line.variantId === variantId);
      result.textContent = 'Added to your cart';
      refreshButton();
    });
    lifecycle.on(root, 'lx:cart:add-items:error', (event) => {
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

## Product detail sheet opened from a recommendation card

A `region: "sheet"` module. Set `presentation.detail_sheet: "product-detail"`
on the offer slot (`cart_promotions_edit`) so each card opens it with the tapped
product as context. The sheet reads the context on `lx:cart:sheet-opened`, adds
the variant with the managed command and closes itself with `data-lx-close-sheet`.

```html lexsis-cart-example
<!-- section: product-detail -->
<section class="detail">
  <img data-detail-image alt="" hidden>
  <h3 data-detail-title>Product</h3>
  <p data-detail-price></p>
  <p class="detail-copy">Free returns within 30 days. Ships in 1-2 business days.</p>
  <button type="button" data-lx-control="add-from-sheet" disabled>Add to cart</button>
  <button type="button" data-lx-close-sheet class="detail-close">Keep shopping</button>
  <p data-result role="status" aria-live="polite"></p>
  <style>
    .detail { padding: 20px; display: grid; gap: 12px; }
    .detail img { width: 100%; max-height: 240px; object-fit: cover; border-radius: 12px; }
    .detail button { min-height: 44px; padding: 8px 16px; }
    .detail-copy { color: var(--lx-muted-color, #6b7280); }
    .detail-close { background: transparent; border: 1px solid var(--lx-border-color); }
  </style>
  <script>
    const image = lifecycle.query('[data-detail-image]');
    const title = lifecycle.query('[data-detail-title]');
    const price = lifecycle.query('[data-detail-price]');
    const button = lifecycle.query('[data-lx-control="add-from-sheet"]');
    const result = lifecycle.query('[data-result]');
    let variantId = null;
    let requestId = null;
    lifecycle.on(root, 'lx:cart:sheet-opened', (event) => {
      const context = event.detail.context || {};
      variantId = context.variant_id || null;
      if (variantId) button.setAttribute('data-lx-variant', variantId);
      else button.removeAttribute('data-lx-variant');
      title.textContent = context.title || 'Product';
      price.textContent = context.price || '';
      image.hidden = !context.image;
      if (context.image) image.src = context.image;
      result.textContent = '';
      button.disabled = !variantId;
    });
    lifecycle.on(button, 'click', () => {
      if (!variantId || requestId) return;
      requestId = 'detail-' + Date.now();
      button.disabled = true;
      root.dispatchEvent(new CustomEvent('lx:cart:add-items', {
        bubbles: true,
        detail: { requestId, items: [{ variantId, quantity: 1 }] }
      }));
    });
    lifecycle.on(root, 'lx:cart:add-items:success', (event) => {
      if (event.detail.requestId !== requestId) return;
      requestId = null;
      result.textContent = 'Added to your cart';
      root.dispatchEvent(new CustomEvent('lx:cart:close-sheet', { bubbles: true, detail: {} }));
    });
    lifecycle.on(root, 'lx:cart:add-items:error', (event) => {
      if (event.detail.requestId !== requestId) return;
      requestId = null;
      button.disabled = false;
      result.textContent = event.detail.message;
    });
  </script>
</section>
```

Any element inside the cart can open a sheet declaratively:
`<button type="button" data-lx-open-sheet="product-detail" data-lx-sheet-context='{"title":"Gift wrap"}'>Details</button>`.

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
