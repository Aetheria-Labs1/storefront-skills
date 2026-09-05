# ProductGallery — Island Directory

Mixed image/video PDP gallery with thumbnail viewers, editorial grids, collages,
masonry, stacked media, mobile swipe, and an accessible lightbox.

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

- **Layouts**: horizontal, vertical, grid, collageLeft, collageRight, twoColumn, masonry, stacked
- **Canonical media prop**: `media: MediaItem[]`
- **Mobile modes**: swipe, stacked
- **Lightbox**: defaults on for grid-family layouts
- **Schema**: `vibe://schema/island/ProductGallery`
- **Layouts**: `vibe://islands/product-gallery/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Always occupies wider column in split layouts (1.2fr+)
- On mobile: stacks ABOVE BuyBox (images first)
- Pair with: BuyBox and VariantSwatches
- Use `collageLeft` for a large lead image with two stacked supporting views
- Use `mobileLayout:"stacked"` only when the PDP can absorb the added page height
- Customize tiles with `--lx-product-gallery-*` variables and stable `data-part` hooks
