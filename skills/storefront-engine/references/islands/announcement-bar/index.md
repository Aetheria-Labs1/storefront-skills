# AnnouncementBar — Island Directory

Top-of-page promotional banner for sales, shipping info, or urgency messaging. Dismissible.

## Files

| File | Purpose |
|------|---------|
| `layouts/single-message.json` | Simple single-line announcement with dismiss button |
| `layouts/rotating.json` | Multiple messages auto-rotating with arrows |
| `layouts/countdown.json` | Announcement with inline countdown timer for urgency |

## Quick Reference

- **Variants**: none (single default)
- **Props**: messages (array of {text, link?}) — 7 total
- **Schema**: `vibe://schema/island/AnnouncementBar`
- **Layouts**: `vibe://islands/announcement-bar/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- ALWAYS position 0 (before Navbar) — pushes Navbar to position 1
- Max 1 per page
- Dismissible via X button (stores dismiss state in localStorage)
- Full-width, accent bg by default (exception to `_contract.md` accent-as-bg rule — banners are allowed)
- py-2 height (compact, never more than ~40px)
- Pair with: Navbar (directly below)
