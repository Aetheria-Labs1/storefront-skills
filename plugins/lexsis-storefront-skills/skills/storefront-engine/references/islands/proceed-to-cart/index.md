# ProceedToCart — Island Directory

"View Cart" button that navigates to cart page or opens cart drawer.

## Files

| File | Purpose |
|------|---------|
| `layouts/primary.json` | Full-width accent button "View Cart (3 items)" |
| `layouts/outline.json` | Outlined button style |
| `layouts/minimal.json` | Text link "View cart →" |

## Quick Reference

- **Variants**: outline, primary, minimal
- **Required prop**: none (reads cart state)
- **Schema**: `vibe://schema/island/ProceedToCart`
- **Layouts**: `vibe://islands/proceed-to-cart/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place after add-to-cart confirmation
- Or as secondary CTA below BuyBox
- Primary: standalone section or below product grid
- Minimal: inline text link in navbar or after quick-add
- Shows item count badge automatically
