# SizeGuide — Island Directory

Size/measurement reference island. Displays sizing tables, unit conversion, and body diagrams.

## Files

| File | Purpose |
|------|---------|
| `layouts/modal-table.json` | Opens as modal with measurement table + unit toggle |
| `layouts/inline-table.json` | Embedded table within PDP section, directly visible |
| `layouts/visual.json` | Body diagram with measurements highlighted |

## Quick Reference

- **Variants**: modal, inline, visual
- **Required prop**: `headers` (array of column headers)
- **Schema**: `vibe://schema/island/SizeGuide`
- **Layouts**: `vibe://islands/size-guide/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: BuyBox, OptionResolver, Modal (as container)
- Trigger from "Size Guide" link near size selector in BuyBox
- Place within 1 scroll of size options
- Modal variant uses Modal island as container
