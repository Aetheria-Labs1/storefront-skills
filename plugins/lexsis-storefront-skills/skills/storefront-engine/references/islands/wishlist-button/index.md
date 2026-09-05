# WishlistButton — Island Directory

Commerce wishlist/save action island. Lightweight toggle for product save state.

## Files

| File | Purpose |
|------|---------|
| `layouts/icon-heart.json` | Heart icon button, toggles filled/outline on click |
| `layouts/text-button.json` | "Save for Later" text link with heart icon prefix |
| `layouts/card-overlay.json` | Heart icon positioned top-right of a product card |

## Quick Reference

- **Variants**: default, compact, overlay
- **Required prop**: `productId` (Shopify GID)
- **Schema**: `vibe://schema/island/WishlistButton`
- **Layouts**: `vibe://islands/wishlist-button/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: BuyBox, ProductCard, ProductGrid, StickyBar
- Place adjacent to Add to Cart actions
- Card overlay variant used inside grid items (ProductGrid, CollectionGrid)
- Icon variant works standalone in toolbars or nav
