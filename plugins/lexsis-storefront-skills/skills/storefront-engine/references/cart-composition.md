# Cart Profile Composition

A cart profile is a renderer-managed surface backed by a published profile.

## Page contract

A commerce page declares:

```json
{
  "head": {
    "title": "...",
    "use_cart_v2": true
  }
}
```

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

Custom page code can open the resolved cart with:

```js
document.dispatchEvent(new CustomEvent("cart:open"))
```

No trigger should carry or infer a profile ID.

## Styling

Page `theme_css` provides brand defaults. Cart profile design values and
`custom_css` apply only under the cart profile root.

Custom CSS is sanitized and scoped at render time. Do not put profile CSS in
page sections or page metadata.

## Anti-patterns

| Anti-pattern | Correct behavior |
|---|---|
| Inline `DrawerShell` on a cart-profile page | Set `use_cart_v2` and configure a profile |
| Cart selected through title or SEO metadata | Use a page assignment |
| Agent publishes a draft automatically | Merchant reviews and publishes in the app |
| Fabricated products or selling plans | Use real store catalog data |
| Page-wide selectors in cart CSS | Use profile-scoped CSS |
