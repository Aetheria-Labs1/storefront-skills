# QuickAdd — Island Directory

Fast add-to-cart action. Minimal UI for rapid purchase without navigating to PDP.

## Files

| File | Purpose |
|------|---------|
| `layouts/button-overlay.json` | + button overlaying product card on hover |
| `layouts/inline-button.json` | Always-visible "Add" button below card |

## Quick Reference

- **Component**: QuickAdd
- **Category**: commerce
- **Props**: 2 (product, onAdd)
- **Required prop**: `product` (object with id, title, availableForSale)
- **Schema**: `vibe://schema/island/QuickAdd`
- **Layouts**: `vibe://islands/quick-add/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: ProductCard (overlay or below), ProductCarousel (inside each card)
- Overlay variant: appears on hover/focus, absolute positioned over card image
- Inline variant: always visible, below card content
- Must check availableForSale before rendering — hide if out of stock
- Triggers cart drawer open on success (pairs with DrawerShell)
