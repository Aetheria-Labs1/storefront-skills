# InventoryIndicator — Island Directory

Shows stock level urgency (low stock warnings, progress bars).

## Quick Reference

- **Variants**: badge, bar, text
- **Required prop**: `productId`
- **Schema**: `vibe://schema/island/InventoryIndicator`
- **Contract**: follows `_contract.md` rules

## Composition

- Place near BuyBox (above CTA or below price)
- Badge: inline next to price
- Bar: below variant selector, above CTA
- Text: subtle, below CTA
- Only show when stock < threshold (island handles logic)
