# InventoryIndicator — Island Directory

Shows stock level urgency (low stock warnings, progress bars).

## Files

| File | Purpose |
|------|---------|
| `layouts/badge.json` | Colored badge "Only 3 left!" |
| `layouts/bar.json` | Progress bar showing stock depletion |
| `layouts/text.json` | Subtle text "Low stock — order soon" |

## Quick Reference

- **Variants**: badge, bar, text
- **Required prop**: `productId`
- **Schema**: `vibe://schema/island/InventoryIndicator`
- **Layouts**: `vibe://islands/inventory-indicator/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place near BuyBox (above CTA or below price)
- Badge: inline next to price
- Bar: below variant selector, above CTA
- Text: subtle, below CTA
- Only show when stock < threshold (island handles logic)
