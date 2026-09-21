# Cart Profile Composition

A cart profile is a renderer-managed surface backed by a published profile.
Custom cart interactions, batch add flows, and controls selecting multiple
products use the documented `lx:cart:add-items` renderer command.

## Page contract

Cart V2 is enabled by default for every storefront. New source omits the
deprecated `use_cart_v2` compatibility field. Existing `true` values remain
valid; `false` fails validation because Cart V2 cannot be disabled.

The page must not contain `CartDrawer`, `DrawerShell`, or cart child islands.
The renderer resolves and injects the cart after the page sections.

Resolution order:

```text
page assignment > campaign assignment > store default > legacy fallback
```

Page metadata does not select a profile.

## Profile modules

The profile snapshot owns:

- Cart mode and responsive behavior
- Ordered layout modules
- Cart sections and rules
- Free-shipping progress
- Shopify selling-plan presentation
- Manual and Shopify-powered offers
- Checkout behavior
- Cart design settings and scoped CSS

Cart lines, order summary, and checkout are required. Optional modules include
shipping progress, purchase options, payment methods, and product offers.

## Offers and subscriptions

Offer placements:

- `header`
- `after_line`
- `after_lines`
- `before_checkout`

Manual offers use Shopify product GIDs. Recommendation offers use Shopify
`RELATED` or `COMPLEMENTARY` intent.

Selling-plan options are line-item capabilities. A profile can choose cards or
a select menu, but it cannot make an ineligible product subscribable.

## Trigger protocol

Add-to-cart controls and the site header emit `cart:open`. The hydrator bridges
DOM events into the cart event bus. The injected `DrawerShell` listens for the
event and lazily hydrates its children on first open.

Use the selected island's supported cart trigger for normal product controls.
For a custom interaction that owns a dynamic product selection, use the
renderer-managed `lx:cart:add-items` command instead of hidden BuyBoxes,
programmatic clicks, or a parallel Shopify/cart mutation. This is the custom
cart and batch add contract for controls that select multiple products.

```js
const addButton = lifecycle.query('[data-lx-control="add-selection"]');

addButton.addEventListener("click", () => {
  section.dispatchEvent(
    new CustomEvent("lx:cart:add-items", {
      bubbles: true,
      detail: {
        requestId: crypto.randomUUID(),
        items: selectedProducts.map((product) => ({
          variantId: product.variantId,
          quantity: product.quantity,
        })),
        openCart: true,
      },
    }),
  );
});
```

The control must use `data-lx-control` and a registered lifecycle handler.
Responses return to the originating section as
`lx:cart:add-items:pending`, `lx:cart:add-items:success`, or
`lx:cart:add-items:error`. Every response includes `requestId`.

No trigger should carry or infer a profile ID.

## Styling

Page `theme_css` provides brand defaults. Cart profile design values and
`custom_css` apply only under the cart profile root.

Custom CSS is sanitized and scoped at render time. Do not put profile CSS in
page sections or page metadata.

## Anti-patterns

| Anti-pattern | Correct behavior |
|---|---|
| Inline `DrawerShell` on a storefront page | Remove it and configure the effective profile |
| Cart selected through title or SEO metadata | Use a page assignment |
| Agent publishes a draft automatically | Merchant reviews and publishes in the app |
| Fabricated products or selling plans | Use real store catalog data |
| Page-wide selectors in cart CSS | Use profile-scoped CSS |
| Hidden BuyBox plus `.click()` for a custom selection | Dispatch `lx:cart:add-items` from the registered section control |
| Direct `/cart/add.js` or Storefront API request | Let the renderer perform the managed GraphQL cart mutation |
