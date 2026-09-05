# PaymentOptions — Island Directory

Displays accepted payment methods (Visa, MC, Apple Pay, Shop Pay, etc.).

## Files

| File | Purpose |
|------|---------|
| `layouts/inline.json` | Horizontal row of payment icons |
| `layouts/expandable.json` | Collapsible "Payment options" with details |
| `layouts/icons-only.json` | Just icons, no text, ultra-compact |

## Quick Reference

- **Variants**: inline, expandable, icons_only
- **Required prop**: none (auto-detects from store)
- **Schema**: `vibe://schema/island/PaymentOptions`
- **Layouts**: `vibe://islands/payment-options/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place below BuyBox CTA button
- Or in footer trust section
- Inline: single row, centered or left-aligned
- Never above the CTA (distracts from purchase action)
