# FAQ — Island Directory

Collapsible question-and-answer island for addressing objections and improving SEO.

## Files

| File | Purpose |
|------|---------|
| `layouts/accordion.json` | Full-width centered accordion, section wrapper |
| `layouts/two-column.json` | 2-column grid, questions split left/right |
| `layouts/compact.json` | No section wrapper, inline for embedding in PDP |

## Quick Reference

- **Variants**: default, compact
- **Schema**: `vibe://schema/island/FAQ`
- **Layouts**: `vibe://islands/faq/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place mid-to-lower page (after product details, before footer)
- Pair with: EmailCapture (below FAQ), TrustBadgeBar
- Never place above the fold or before primary CTA
- Compact variant embeds within other sections (no own wrapper)
- Max 8-10 items for readability; group by category if >6
