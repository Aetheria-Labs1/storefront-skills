# StickyBar — Island Directory

Fixed-bottom purchase bar that appears when the primary BuyBox or Hero CTA scrolls out of viewport.

## Files

| File | Purpose |
|------|---------|
| `layouts/default.json` | Product name + price + CTA button, fixed bottom |
| `layouts/with-image.json` | Small product thumbnail + name + price + CTA |
| `layouts/minimal.json` | Just CTA button, compact accent-colored bar |

## Quick Reference

- **Variants**: (single default)
- **Required prop**: `productId` (Shopify GID)
- **Schema**: `vibe://schema/island/StickyBar`
- **Layouts**: `vibe://islands/sticky-bar/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Triggers when BuyBox or ProductHero scrolls out of viewport
- Place in section AFTER the primary purchase island (BuyBox or ProductHero)
- Max 1 StickyBar per page
- Touch target: min 44px height on mobile
- Uses `position: fixed; bottom: 0` — account for mobile browser chrome
- z-index: 50 (above content, below modals/drawers)
