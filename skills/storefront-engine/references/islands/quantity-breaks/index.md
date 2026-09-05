# QuantityBreaks — Island Directory

Volume discount tiers. Shows savings for buying more units.

## Quick Reference

- **Component**: QuantityBreaks
- **Category**: commerce
- **Props**: 3 (tiers, selectedTier, highlightBest)
- **Required prop**: `tiers` (array of {quantity, price, savings, label})
- **Schema**: `vibe://schema/island/QuantityBreaks`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: BuyBox (below variant selection), SubscriptionToggle (combine volume + frequency)
- Place directly above or below quantity selector in BuyBox
- "Most popular" or "Best value" badge on recommended tier
- Never show more than 4 tiers (cognitive overload)
