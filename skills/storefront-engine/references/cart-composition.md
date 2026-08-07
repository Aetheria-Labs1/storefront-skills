# Cart V2 Composition — DrawerShell + Atomic Islands

Compose a Cart V2 drawer using atomic islands inside a DrawerShell container. Use when store has `cart_v2` enabled.

---

## Overview

Cart V2 replaces the monolithic CartDrawer with composable islands that each handle one responsibility. The drawer HTML lives in store-level config (`cart_sections` array), shared across all pages. Islands read runtime data from the store's `commerce_config` at hydration time.

---

## Required Structure

Cart V2 pages set `head.use_cart_v2: true` ONLY. No cart section appears in the page sections array.

```jsonc
{
  "head": {
    "title": "...",
    "use_cart_v2": true
  }
}
```

The renderer injects the cart HTML (from store config) after page sections at render time. Manage via `get_cart_config` and `update_cart_config` MCP tools.

**Minimum required islands inside DrawerShell:**
1. `CartLines` — line items
2. `CartCheckoutButton` — checkout CTA

Validation fails without both.

---

## Island Catalog

| Island | Purpose | Key Props |
|---|---|---|
| `DrawerShell` | Container / drawer chrome | `trigger` (event name, default `"cart:open"`) |
| `CartLines` | Line items with qty controls | — |
| `CartCheckoutButton` | Checkout CTA | `text?` |
| `CartSummary` | Subtotal / taxes / total | — |
| `CartProgressBar` | Free shipping / tiered progress | `threshold?`, `message?`, `completedMessage?`, `tiers?`, `currency?` |
| `CartDiscountInput` | Promo code field | `placeholder?` |
| `CartCrossSell` | Upsell recommendations | `heading?`, `max?`, `layout?`, `showQuickAdd?` |

**DO NOT use** `CartAnnouncement`, `CartOrderNote`, or `CartCountdown` — these are unimplemented.

---

## CartCrossSell Config

CartCrossSell is self-managing. It reads product recommendations from `commerce_config.upsells` at the store level. There is NO `source` prop.

Props (all optional):
- `heading` — section heading text (e.g. `"Complete Your Routine"`)
- `max` — maximum products to show (default determined by config)
- `layout` — `"horizontal"` | `"grid"` | `"stack"`
- `showQuickAdd` — boolean, show inline add-to-cart

Product IDs in `commerce_config.upsells` must be Shopify GIDs: `gid://shopify/Product/...`

For config-driven defaults, use empty props:
```html
<div data-island="CartCrossSell" data-props='{}'></div>
```

For display overrides:
```html
<div data-island="CartCrossSell" data-props='{"heading":"You May Also Like","max":3,"layout":"horizontal","showQuickAdd":true}'></div>
```

---

## CartProgressBar Config

CartProgressBar self-manages visibility. It falls back to `$cartConfig.free_shipping_threshold` when no `threshold` prop is passed.

Props (all optional):
- `threshold` — target amount in cents (overrides store config)
- `message` — template string, use `{remaining}` placeholder
- `completedMessage` — shown when threshold met
- `tiers` — array of `{ threshold, label }` for multi-tier progress
- `currency` — currency code (falls back to store currency)

Config-driven (reads threshold from store config):
```html
<div data-island="CartProgressBar" data-props='{}'></div>
```

Explicit threshold:
```html
<div data-island="CartProgressBar" data-props='{"threshold":7500,"message":"Add {remaining} for free shipping!","completedMessage":"Free shipping unlocked!"}'></div>
```

Multi-tier:
```html
<div data-island="CartProgressBar" data-props='{"tiers":[{"threshold":5000,"label":"Free shipping"},{"threshold":10000,"label":"10% off"},{"threshold":15000,"label":"Free gift"}]}'></div>
```

---

## Composition Rules

1. DrawerShell must have `data-island-container` attribute — prevents children from hydrating on page load.
2. DrawerShell `trigger` prop is an event name (default `"cart:open"`). It is NOT `triggerId`.
3. Only pass display props (heading, layout, text). Config-driven behavior uses empty `data-props='{}'`.
4. CartCrossSell and CartProgressBar self-manage visibility — no conditional rules needed for basic show/hide.
5. Max 6-7 islands inside DrawerShell to avoid clutter and hydration overhead.
6. One cart config per store — applies to ALL pages. Pages only set the `head.use_cart_v2: true` flag.
7. Never mix CartDrawer (V1) and DrawerShell (V2) — validation error.

---

## Example

Complete DrawerShell HTML for a store config:

```html
<div data-island="DrawerShell" data-island-container data-props='{"trigger":"cart:open"}'>
  <div class="p-4 border-b">
    <div data-island="CartProgressBar" data-props='{"threshold":7500,"message":"Add {remaining} for free shipping!","completedMessage":"Free shipping unlocked!"}'></div>
  </div>
  <div class="flex-1 overflow-y-auto p-4">
    <div data-island="CartLines" data-props='{}'></div>
  </div>
  <div class="p-4 border-t">
    <div data-island="CartCrossSell" data-props='{"heading":"Complete Your Routine","max":2,"layout":"horizontal","showQuickAdd":true}'></div>
  </div>
  <div class="p-4 border-t">
    <div data-island="CartDiscountInput" data-props='{"placeholder":"Promo code"}'></div>
  </div>
  <div class="p-4 border-t bg-gray-50">
    <div data-island="CartSummary" data-props='{}'></div>
    <div data-island="CartCheckoutButton" data-props='{"text":"Checkout"}'></div>
  </div>
</div>
```

---

## Anti-Patterns

| Anti-Pattern | Why It Breaks |
|---|---|
| Using `triggerId` on DrawerShell | Prop is `trigger` (event name string), not `triggerId` |
| Passing `source` to CartCrossSell | No `source` prop exists — reads from `commerce_config.upsells` |
| Using CartAnnouncement / CartOrderNote / CartCountdown | Unimplemented islands — will not render |
| Missing `data-island-container` on DrawerShell | Children hydrate immediately on page load (perf hit) |
| Putting cart section in page sections array | Cart V2 lives in store config only; page sets `head.use_cart_v2: true` |
| CartDrawer + DrawerShell on same page | Validation error — pick one |
| No CartLines or CartCheckoutButton | Validation blocks publish |
