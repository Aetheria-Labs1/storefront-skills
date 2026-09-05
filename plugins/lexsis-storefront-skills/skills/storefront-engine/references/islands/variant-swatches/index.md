# VariantSwatches — Island Directory

Variant selection UI. Color circles, size buttons, or image-based swatches.

## Files

| File | Purpose |
|------|---------|
| `layouts/color-circles.json` | Circular color swatches |
| `layouts/size-buttons.json` | Rectangular size buttons (S/M/L/XL) |
| `layouts/image-swatches.json` | Thumbnail images per variant |

## Quick Reference

- **Component**: VariantSwatches
- **Category**: commerce
- **Props**: 8 (variants, values, selectedVariant, onChange, layout, size, showLabel, showStock)
- **Required props**: `variants` (array), `values` (array)
- **Schema**: `vibe://schema/island/VariantSwatches`
- **Layouts**: `vibe://islands/variant-swatches/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: BuyBox (embedded inside), ProductCard (inline below image)
- Always place above the Add to Cart CTA
- When used standalone, wrap in a labeled fieldset for accessibility
- Cross-out unavailable variants (strikethrough + reduced opacity)
