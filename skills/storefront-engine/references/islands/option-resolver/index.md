# OptionResolver — Island Directory

Product variant/option selector island. Resolves user selections to a specific product variant.

## Files

| File | Purpose |
|------|---------|
| `layouts/dropdown.json` | Select dropdowns for each option group (Size, Color, Material) |
| `layouts/buttons.json` | Button group per option: Size [S] [M] [L], Color swatches |
| `layouts/visual.json` | Image tiles for visual options (pattern, material, color) |

## Quick Reference

- **Variants**: dropdown, buttons, visual
- **Required prop**: `options` (array of option groups)
- **Schema**: `vibe://schema/island/OptionResolver`
- **Layouts**: `vibe://islands/option-resolver/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: BuyBox (inside or adjacent), SizeGuide, WishlistButton
- Resolves user selections to a specific variant before add-to-cart
- Usually embedded within BuyBox section or directly above CTA
- Place SizeGuide trigger link near size option group
