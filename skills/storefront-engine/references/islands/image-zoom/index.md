# ImageZoom — Island Directory

Product image magnification island. Enables close-up inspection of product details.

## Files

| File | Purpose |
|------|---------|
| `layouts/hover-zoom.json` | Zoom lens follows cursor on hover |
| `layouts/click-lightbox.json` | Full-screen lightbox on click |
| `layouts/inline-magnifier.json` | Magnified view in adjacent panel |

## Quick Reference

- **Variants**: hover, lightbox, magnifier
- **Required prop**: `src` (image URL)
- **Schema**: `vibe://schema/island/ImageZoom`
- **Layouts**: `vibe://islands/image-zoom/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: ProductGallery, BuyBox, BeforeAfter
- Use for product detail close-ups (texture, stitching, ingredients label)
- Place within or adjacent to gallery area
- Never stack multiple ImageZoom islands for the same product — use gallery carousel instead
