# VariantSwatches — Island Directory

Variant selection UI. Color circles, size buttons, or image-based swatches.

## Quick Reference

- **Component**: VariantSwatches
- **Category**: commerce
- **Props**: 8 (variants, values, selectedVariant, onChange, layout, size, showLabel, showStock)
- **Required props**: `variants` (array), `values` (array)
- **Schema**: `vibe://schema/island/VariantSwatches`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: BuyBox (embedded inside), ProductCard (inline below image)
- Always place above the Add to Cart CTA
- When used standalone, wrap in a labeled fieldset for accessibility
- Cross-out unavailable variants (strikethrough + reduced opacity)
