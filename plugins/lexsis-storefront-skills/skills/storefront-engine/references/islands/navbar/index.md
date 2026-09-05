# Navbar — Island Directory

Primary site navigation. Always first section (position 0). Max 1 per page.

## Files

| File | Purpose |
|------|---------|
| `layouts/minimal.json` | Clean nav: logo left, links center, cart right. Transparent bg. |
| `layouts/mega-menu.json` | Full mega-menu with dropdown panels on hover |
| `layouts/transparent-overlay.json` | Transparent nav overlaying hero (absolute positioned) |

## Quick Reference

- **Variants**: none (single default)
- **Props**: logo (object), links (array), style (object), cta (object) — 11 total
- **Schema**: `vibe://schema/island/Navbar`
- **Layouts**: `vibe://islands/navbar/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- ALWAYS position 0 (first section on page)
- Max 1 per page
- Pair with: MobileMenu (hidden section, hamburger trigger)
- AnnouncementBar goes ABOVE navbar (position 0 shifts navbar to 1)
- Transparent variant requires dark/image hero directly below
- Container: `w-full` outer, `max-w-7xl mx-auto` inner content
