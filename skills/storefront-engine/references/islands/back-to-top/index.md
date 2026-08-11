# BackToTop — Island Directory

Scroll-to-top utility island. One per page max.

## Files

| File | Purpose |
|------|---------|
| `layouts/circle-button.json` | Fixed bottom-right circular button, appears after scroll threshold |
| `layouts/text-link.json` | "Back to top" text link at end of page content (not fixed) |

## Quick Reference

- **Variants**: none (single default)
- **Props**: threshold (number), smooth (boolean), label (string) — 3 total
- **Schema**: `vibe://schema/island/BackToTop`
- **Layouts**: `vibe://islands/back-to-top/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place once per page (max 1)
- Fixed variant (circle-button) is invisible until user scrolls past threshold
- Text-link variant goes at end of long content sections, before footer
- Never pair both layouts on the same page — pick one
- Container: navigation category = `w-full` outer (fixed variant has its own positioning)
