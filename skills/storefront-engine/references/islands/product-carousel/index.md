# ProductCarousel — Island Directory

Horizontal product showcase. Scrollable row of product cards with navigation.

## Files

| File | Purpose |
|------|---------|
| `layouts/default.json` | Horizontal scroll, 4 visible cards |
| `layouts/compact.json` | 3 visible, smaller cards |
| `layouts/full-width.json` | Edge-to-edge, peek from sides |

## Quick Reference

- **Component**: ProductCarousel
- **Category**: commerce
- **Props**: 11 (products, visibleCount, autoScroll, gap, showArrows, showDots, cardVariant, aspectRatio, speed, loop, pauseOnHover)
- **Required prop**: `products` (array of product objects)
- **Schema**: `vibe://schema/island/ProductCarousel`
- **Layouts**: `vibe://islands/product-carousel/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: SectionHeading, QuickAdd (inside cards), TrustBadgeBar
- Place mid-page or below hero for "Shop our bestsellers" sections
- Never place inside a grid column — needs full container width
- Cards inside can embed QuickAdd overlays on hover
