# IngredientExplorer — Island Directory

Interactive ingredient/material showcase island. Displays product ingredients with details and benefits.

## Files

| File | Purpose |
|------|---------|
| `layouts/grid.json` | Card grid with icon + name + benefit per ingredient |
| `layouts/list.json` | Vertical scrollable list with expandable details |
| `layouts/editorial.json` | Magazine-style: large images + text blocks, one at a time |

## Quick Reference

- **Variants**: grid, list, editorial
- **Required prop**: `ingredients` (array of ingredient objects)
- **Schema**: `vibe://schema/island/IngredientExplorer`
- **Layouts**: `vibe://islands/ingredient-explorer/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: BuyBox (below), TrustBadgeBar, BeforeAfter
- Place in product details section for beauty/supplements/food
- Works well between hero and social proof sections
- Max 1 per page
