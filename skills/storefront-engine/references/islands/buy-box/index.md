# BuyBox — Island Directory

Primary purchase action island. One per page max.

## Files

| File | Purpose |
|------|---------|
| `beauty.md` | Beauty/skincare copy, tone, companion islands |
| `supplements.md` | Supplements copy, subscription-first, clinical trust |
| `fashion.md` | Fashion copy, size guide, "Add to Bag" convention |

## Quick Reference

- **Variants**: default, compact, expanded
- **Required prop**: `productId` (Shopify GID)
- **Schema**: `vibe://schema/island/BuyBox`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: ProductGallery, TrustBadgeBar, StickyBar
- Place TrustBadgeBar within 200px below
- StickyBar triggers when BuyBox scrolls out of viewport
- Set matching `syncKey` on BuyBox and StickyBar, with the same complete variant catalog, to synchronize both directions. This works in rendered and headless mode.
- For a linked group using external selectors, enable `listenForEvents` and set the selectors' `data-scope` wrapper to that key. Tier-priced options stay controlled by the main tier selector.
- Never duplicate title/price outside island (it renders its own)
