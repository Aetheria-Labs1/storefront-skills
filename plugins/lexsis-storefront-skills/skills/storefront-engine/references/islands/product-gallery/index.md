# ProductGallery — Island Directory

Mixed image/video PDP gallery with thumbnail viewers, editorial grids, collages,
masonry, stacked media, mobile swipe, and an accessible lightbox.

## Files

| File | Purpose |
|------|---------|
| `fashion.md` | Fashion: model angles, fabric zoom, 3/4 aspect |
| `jewelry.md` | Jewelry: close-up detail, 1/1 aspect, scale reference |

## Quick Reference

- **Canonical media prop**: `media: MediaItem[]`
- **Mobile modes**: swipe, stacked
- **Lightbox**: defaults on for grid-family layouts
- **Schema**: `vibe://schema/island/ProductGallery`
- **Contract**: follows `_contract.md` rules

## Composition

- Always occupies wider column in split layouts (1.2fr+)
- On mobile: stacks ABOVE BuyBox (images first)
- Pair with: BuyBox and VariantSwatches
- Use `collageLeft` for a large lead image with two stacked supporting views
- Use `mobileLayout:"stacked"` only when the PDP can absorb the added page height
- Customize tiles with `--lx-product-gallery-*` variables and stable `data-part` hooks
