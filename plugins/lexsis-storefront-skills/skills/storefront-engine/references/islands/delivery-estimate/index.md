# DeliveryEstimate — Island Directory

Shows estimated delivery date/time for current product.

## Files

| File | Purpose |
|------|---------|
| `layouts/inline.json` | Single line with truck icon + date |
| `layouts/card.json` | Bordered card with shipping method details |
| `layouts/banner.json` | Full-width slim banner above BuyBox |

## Quick Reference

- **Variants**: inline, card, banner
- **Required prop**: `productId`
- **Schema**: `vibe://schema/island/DeliveryEstimate`
- **Layouts**: `vibe://islands/delivery-estimate/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place directly below or inside BuyBox section
- Inline variant: within BuyBox wrapper, below price
- Card variant: standalone below BuyBox
- Banner variant: full-width above BuyBox section
