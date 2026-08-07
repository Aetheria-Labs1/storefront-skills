# CountdownTimer — Island Directory

Urgency-driving countdown for flash sales, launches, and limited offers.

## Files

| File | Purpose |
|------|---------|
| `layouts/flip-clock.json` | Retro flip-clock digits, dark bg, centered section |
| `layouts/simple-inline.json` | Inline text countdown, no wrapper, embeds in hero/CTA |
| `layouts/circular.json` | Circular progress rings, centered max-w-md |

## Quick Reference

- **Variants**: flip, simple, circular
- **Schema**: `vibe://schema/island/CountdownTimer`
- **Layouts**: `vibe://islands/countdown-timer/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place near primary CTA or within hero section for maximum urgency
- Pair with: BuyBox (above or beside), EmailCapture (deadline-gated offer)
- Flip-clock variant needs dark bg for contrast (use section wrapper)
- Simple-inline embeds directly in other sections (no own wrapper)
- Never use more than 1 countdown per page (dilutes urgency)
- END_DATE must be ISO 8601 format; island handles timezone display
