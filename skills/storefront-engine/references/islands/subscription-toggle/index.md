# SubscriptionToggle — Island Directory

One-time vs. subscription purchase toggle with savings display.

## Quick Reference

- **Component**: SubscriptionToggle
- **Category**: commerce
- **Props**: 5 (plans, benefits, selectedPlan, savingsPercent, frequency)
- **Required props**: `plans` (array), `benefits` (array)
- **Schema**: `vibe://schema/island/SubscriptionToggle`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: BuyBox (embedded above CTA), QuantityBreaks (below for volume + frequency combos)
- Place between variant selection and Add to Cart button
- Savings badge should use --lx-accent-color background
- Never duplicate price display — toggle updates BuyBox price
