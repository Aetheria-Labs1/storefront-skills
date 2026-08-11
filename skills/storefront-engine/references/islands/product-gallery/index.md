# ProductGallery — Island Directory

Product image display with zoom, thumbnails, and swipe.

## Files

| File | Purpose |
|------|---------|
| `layouts/grid-2x2.json` | 2x2 image grid (4+ images, desktop PDP) |
| `layouts/horizontal-scroll.json` | Swipeable carousel (mobile-first) |
| `layouts/hero-thumbnails.json` | Large main + vertical thumbnail strip |
| `layouts/editorial-asymmetric.json` | Varied sizes, luxury/editorial feel |
| `fashion.md` | Fashion: model angles, fabric zoom, 3/4 aspect |
| `jewelry.md` | Jewelry: close-up detail, 1/1 aspect, scale reference |

## Quick Reference

- **Variants**: grid, horizontal, vertical
- **Required prop**: `productId` (Shopify GID)
- **Schema**: `vibe://schema/island/ProductGallery`
- **Layouts**: `vibe://islands/product-gallery/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Always occupies wider column in split layouts (1.2fr+)
- On mobile: stacks ABOVE BuyBox (images first)
- Pair with: BuyBox (always), ImageZoom (optional for detail)
- Transparent product images: add `backgroundColor` prop or `--lx-surface-alt`
