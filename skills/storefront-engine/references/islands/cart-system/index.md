# Cart System — Island Directory

Composed cart drawer using DrawerShell + CartLines + CartCheckoutButton + CartProgressBar + CartSummary + CartCrossSell (Cart V2).

## Files

| File | Purpose |
|------|---------|
| `layouts/drawer-right.json` | Standard right-side slide-out drawer |
| `layouts/bottom-sheet.json` | Mobile bottom sheet pattern |
| `layouts/mini-cart.json` | Dropdown mini-cart (compact, no full drawer) |

## Quick Reference

- **Variants**: DrawerShell (none), CartLines (compact, full), CartCheckoutButton (filled, outline), CartProgressBar (none), CartSummary (none), CartCrossSell (horizontal, grid, stack)
- **Required prop**: `DrawerShell.trigger` (event name, default `"cart:open"`)
- **Schema**: `vibe://schema/island/DrawerShell`, `vibe://schema/island/CartLines`, `vibe://schema/island/CartCheckoutButton`, `vibe://schema/island/CartProgressBar`, `vibe://schema/island/CartSummary`, `vibe://schema/island/CartCrossSell`
- **Layouts**: `vibe://islands/cart-system/layouts/{name}`
- **Contract**: follows `_contract.md`

## Config-Driven Architecture

Cart V2 islands subscribe to store-level `commerce_config` (exposed as `$cartConfig` at runtime):
- **CartProgressBar** reads `free_shipping_threshold` and `currency` from config — pass empty props or override with explicit values
- **CartCrossSell** reads `upsells[]` from config — self-manages visibility based on cart contents matching `trigger_product_ids`
- **DrawerShell** reads `cart_style.mode` and `cart_style.responsive` from config

Islands self-manage visibility. No rules needed for basic show/hide of CartProgressBar (hides when threshold=0 or cart empty) or CartCrossSell (hides when no triggers match).

## Composition

- Max 1 DrawerShell per page
- Cart V2 pages set `head.use_cart_v2: true` — no cart section in page sections array
- CartProgressBar sits at top (shows free shipping threshold)
- CartCrossSell sits after CartLines (shows upsell recommendations)
- CartLines fills the scrollable middle area
- CartSummary + CartCheckoutButton anchor to the bottom
- DrawerShell is triggered by BuyBox or Navbar cart icon — ensure trigger event matches
- Product IDs in commerce_config must be Shopify GIDs (gid://shopify/Product/...)
