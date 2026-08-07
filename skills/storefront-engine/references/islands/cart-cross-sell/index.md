# CartCrossSell — Island Knowledge

Self-contained cross-sell/upsell inside the cart drawer. Reads config from `commerce_config.upsells`, evaluates triggers against cart contents, fetches recommended products from Shopify Storefront API, and self-hides when no triggers match.

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `heading` | string | From config `label` | Section heading text |
| `max` | number | 3 | Maximum products to show |
| `layout` | "horizontal" \| "grid" \| "stack" | "horizontal" | Display layout |
| `showQuickAdd` | boolean | true | Show "Add" button on each product |

## Config Source

Reads from `commerce_config.upsells` (array):

```json
{
  "upsells": [
    {
      "trigger_product_ids": ["gid://shopify/Product/123"],
      "recommend_product_ids": ["gid://shopify/Product/789", "gid://shopify/Product/456"],
      "label": "Complete your routine"
    }
  ]
}
```

- `trigger_product_ids` — when ANY of these are in cart, this upsell activates
- `recommend_product_ids` — products to show (fetched from Shopify Storefront API)
- `label` — used as heading (overridden by `heading` prop if set)

## Self-Managing Behavior

- Shows when: cart contains a product matching any `trigger_product_ids`
- Hides when: no trigger matches OR no products to recommend
- No rules needed for visibility control

## Product ID Format

All IDs must be Shopify GIDs: `gid://shopify/Product/1234567890`

## Anti-Patterns

- Passing product data via data-props — use `commerce_config.upsells` instead
- Using hidden class + rules for visibility — the island self-manages
- Placing outside DrawerShell — needs cart state subscription
- Using non-GID product IDs — will fail to fetch from Storefront API

## Example HTML

```html
<!-- Default — reads everything from commerce_config -->
<div data-island="CartCrossSell" data-props='{}'></div>

<!-- With display overrides -->
<div data-island="CartCrossSell" data-props='{"heading":"You might also like","layout":"grid","max":4}'></div>
```

## data-part Attributes

| Part | Element | Purpose |
|------|---------|---------|
| `root` | Outer container | CSS targeting root |
| `heading` | Heading text | Section title |
| `item` | Product card | Individual recommendation |
| `item-image` | Product image | Product thumbnail |
| `item-info` | Info container | Title + price |
| `item-title` | Title text | Product name |
| `item-price` | Price text | Product price |
| `add-button` | Quick add button | Add to cart CTA |
