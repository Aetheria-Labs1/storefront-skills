# QuantityBreaks — Island Directory

Volume discount tiers. Shows savings for buying more units.

## Files

| File | Purpose |
|------|---------|
| `layouts/horizontal-tiers.json` | 3 tier cards side by side (1x, 2x, 3x) |
| `layouts/vertical-list.json` | Stacked list with radio buttons |
| `layouts/badge-overlay.json` | Subtle badge on BuyBox: "Buy 2+ save 10%" |

## Quick Reference

- **Component**: QuantityBreaks
- **Category**: commerce
- **Props**: 3 (tiers, selectedTier, highlightBest)
- **Required prop**: `tiers` (array of {quantity, price, savings, label})
- **Schema**: `vibe://schema/island/QuantityBreaks`
- **Layouts**: `vibe://islands/quantity-breaks/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: BuyBox (below variant selection), SubscriptionToggle (combine volume + frequency)
- Place directly above or below quantity selector in BuyBox
- "Most popular" or "Best value" badge on recommended tier
- Never show more than 4 tiers (cognitive overload)
