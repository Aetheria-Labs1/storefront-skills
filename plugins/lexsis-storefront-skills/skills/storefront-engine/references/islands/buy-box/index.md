# BuyBox — Island Directory

Primary purchase action island. One per page max.

## Files

| File | Purpose |
|------|---------|
| `layouts/split-pdp.json` | Gallery left, BuyBox right (standard PDP) |
| `layouts/stacked-mobile.json` | Mobile-first vertical stack |
| `layouts/sticky-sidebar.json` | Long PDP with sticky buy panel |
| `layouts/minimal-compact.json` | Compact for bundles/upsells |
| `beauty.md` | Beauty/skincare copy, tone, companion islands |
| `supplements.md` | Supplements copy, subscription-first, clinical trust |
| `fashion.md` | Fashion copy, size guide, "Add to Bag" convention |

## Quick Reference

- **Variants**: default, compact, expanded
- **Required prop**: `productId` (Shopify GID)
- **Schema**: `vibe://schema/island/BuyBox`
- **Layouts**: `vibe://islands/buy-box/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: ProductGallery, TrustBadgeBar, StickyBar
- Place TrustBadgeBar within 200px below
- StickyBar triggers when BuyBox scrolls out of viewport
- Never duplicate title/price outside island (it renders its own)
