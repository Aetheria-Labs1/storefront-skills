---
name: cart
description: Inspect, assign, design, compose, or preview Lexsis cart profiles. Supports responsive design, scoped CSS, custom source-format modules, and read-only promotion diagnostics.
---

# Configure a Cart

Cart profiles are managed separately from page section HTML.

Use `lexsis_cart.get`, `lexsis_cart.capabilities`,
`lexsis_cart.promotions`, and `lexsis_cart.preview`. When requested, use
`lexsis_drafts.cart_set` and `lexsis_drafts.cart_edit`. Resolve unfamiliar
argument schemas with exact router/action discovery. An empty discovery result
is not a cart outage; the actual cart call determines availability. Do not
infer the effective cart profile from page HTML.

Resolve the target store from a page binding, an explicit saved choice, or the
unambiguous default in `work/storefront/setup/setup.json`. If it is not saved,
stop and ask the user to run `/setup`; never invoke setup automatically.

## Rules

- A page enables the cart through its supported page configuration; do not add
  DrawerShell or cart-line markup to page sections.
- Effective profile order is page assignment, campaign assignment, store
  default, then legacy fallback.
- Draft profile edits are not live until published in the Lexsis app.
- Do not invent products, prices, currencies, offers, or selling plans.
- Promotion, discount, offer, shipping-threshold, and cart-rule configuration
  is read-only through MCP. Never try to recreate those writes through another
  tool.
- Custom modules use the same Lexsis source format as normal pages: HTML,
  `<style>`, section `<script>`, managed motion, and registered `<lx-island>`
  components. Cart lines, order summary, checkout, and DrawerShell remain
  renderer-owned.

## Workflow

1. Call `lexsis_cart.get`.
   - Use `page_id` to inspect the effective profile and resolution source.
   - Use `cart_profile_id` to inspect an editable profile.
   - Use `store_id` to list profiles.
2. Call `lexsis_cart.capabilities` before the first design or composition edit
   in a task. Resolve island props through `lexsis_design.island_schema`.
3. For discounts or offers, call `lexsis_cart.promotions` and report the
   configured profile values, active Shopify discounts, and readiness or
   conflict diagnostics without changing them.
4. When requested, assign a published profile with
   `lexsis_drafts` action `cart_set`. Passing a null profile removes the page
   assignment.
5. Edit a draft with `lexsis_drafts` action `cart_edit` and a partial patch.
   Supported areas are cart mode, typed design settings, responsive
   presentation, scoped custom CSS, and composition operations.
   - `upsert` adds or replaces one custom module from one source section.
     Omit source to change `visible_when` on an existing custom or optional
     built-in module; pass `visible_when: null` to clear the rule.
   - `move` reorders a module within its header, body, or footer region.
   - `set_enabled` toggles custom or optional modules.
   - `remove` deletes only custom modules.
   - Use `before_module_id: "checkout"` and `region: "footer"` for a block
     immediately above checkout.
6. Re-read the profile with `lexsis_cart.get`.
7. Call `lexsis_cart.preview`.
   - Pass `page_id` to render the immutable cart draft version on the existing
     storefront page. The returned URL includes `preview=1`,
     `cart_profile_id`, and `cart_version`; it does not publish or synchronize
     Shopify discounts.
   - Omit `page_id` only when an isolated signed cart fixture preview is more
     useful.
   Verify desktop and mobile. Test both populated and empty cart states when
   the design changes structure.

Use real catalog and review data in custom modules. For example, a rotating
review strip above checkout should use `ReviewCarousel` with an active review
collection or merchant-confirmed reviews; never fabricate quotes or ratings.
Cart triggers dispatch `cart:open`; they do not need a profile ID.

Custom CSS must remain scoped to the cart. External imports, remote URLs,
script escapes, and unbalanced rules are not allowed.

## Custom module examples

Read `capabilities.snapshot_schema`, `commands`, and `conditions` first.
Money has decimal `amount`, `currencyCode`, and integer `minor`. Never supply
a fallback currency. Snapshot amounts share CartSummary's confirmed selectors.
`lifecycle.cart` is deeply frozen. Use `onCart` during initialization: it waits
for currency/prices and settlement, calls at most once per frame, and cleans up
on unmount. The getter reports pending status with confirmed merchandise values
while a mutation runs.

### Read live gift remaining

Use this single section as `composition_ops[].source`. Its reward comes from
the existing profile, not a hardcoded threshold or invented gift.

```html
<!-- section: gift-remaining -->
<section>
  <p data-gift-message hidden>Only <strong data-remaining></strong> to go for your gift.</p>
  <script>
    lifecycle.onCart((cart, previous) => {
      const next = cart.rewards.next;
      lifecycle.query('[data-gift-message]').hidden = !next;
      lifecycle.query('[data-remaining]').textContent = next
        ? new Intl.NumberFormat(cart.context.locale || undefined, {
            style: 'currency', currency: next.remaining.currencyCode
          }).format(Number(next.remaining.amount))
        : '';
    });
  </script>
</section>
```

### Send a managed command

Every command uses a unique request ID and bubbles from `section`; responses
return to this module. Replaying the identical request returns its terminal
response without another write. The eight additional commands are
`update-line`, `remove-line`, `apply-code`, `remove-code`, `set-attributes`,
`set-note`, `choose-gift`, and `swap-variant`, all prefixed `lx:cart:`.
Read their exact limits and payloads in capabilities.

```html
<!-- section: cart-note -->
<section>
  <label>Order note <textarea data-note maxlength="5000"></textarea></label>
  <button type="button" data-lx-control="save-note">Save note</button>
  <span data-result role="status"></span>
  <script>
    let sequence = 0;
    lifecycle.on(lifecycle.query('[data-lx-control="save-note"]'), 'click', () => {
      section.dispatchEvent(new CustomEvent('lx:cart:set-note', {
        bubbles: true,
        detail: {
          requestId: 'note-' + Date.now() + '-' + (++sequence),
          note: lifecycle.query('[data-note]').value
        }
      }));
    });
    lifecycle.on(section, 'lx:cart:set-note:success', () => {
      lifecycle.query('[data-result]').textContent = 'Note saved';
    });
    lifecycle.on(section, 'lx:cart:set-note:error', (event) => {
      lifecycle.query('[data-result]').textContent = event.detail.message;
    });
  </script>
</section>
```

Success waits for settlement; pending/accepted/confirmed are intermediate
phases. Shopper code application and gift selection do not change promotion
configuration. Gift IDs and variants must come from the configured profile.
An AJAX variant swap can return `partial_swap` if only the replacement add
succeeded; show the error and current cart, never blindly replay a new add.

### Hide a module on an empty cart

Use the actual module ID from `cart.get`. This example updates an existing
payment module without replacing its renderer-owned source:

```json
{
  "operation": "upsert",
  "module_id": "payment-options",
  "visible_when": {
    "op": "AND",
    "clauses": [{"field": "cart.item_count", "op": "gt", "value": 0}]
  }
}
```

The same `visible_when` works on custom modules and offers. To hide an upsell
after its variant is added, use `cart.has_variant_id`, `op: "neq"`, and the
real ProductVariant GID as `value`. Hidden content leaves the accessibility
tree; it updates without a reload. Required cart modules cannot be hidden.
Money conditions use minor units. Customer flags default false without a host
session provider; tags/collections depend on available Shopify metadata.

### Bind simple content without JavaScript

```html
<!-- section: gift-binding -->
<section>
  <p data-lx-if="rewards.next.remaining.minor &gt; 0">
    Only <strong data-lx-text="rewards.next.remaining"></strong> to go.
  </p>
</section>
```

Conditions also accept comparisons, `!`, `&&`, `||`, parentheses and predicates
such as `!reward.unlocked('REAL_REWARD_ID')`. Unknown paths/functions are rejected
by the compiler. Money text uses the real snapshot currency. No `window` or
`document` access is needed.

## Return

Report the effective profile, resolution source, composition and design
changes, promotion diagnostics, preview URL/evidence, page assignment, and
which actions still require review or publication in Lexsis.
