# SiteHeader — Island Directory

Compound navigation island combining AnnouncementBar + Navbar. Max 1 per page, must be first section.

## Quick Reference

- **Variants**: none (single default)
- **Props**: announcement (object), navbar (object), sticky (boolean) — 3 total
- **Schema**: `vibe://schema/island/SiteHeader`
- **Contract**: follows `_contract.md` rules

## Composition

- MUST be first section (position 0)
- Max 1 per page
- Wraps AnnouncementBar + Navbar as a compound island
- Alternative to using separate AnnouncementBar and Navbar islands
- Rule: max 1 SiteHeader OR (1 AnnouncementBar + 1 Navbar) per page — never both patterns
- Container: `w-full` outer, `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8` inner content
