# Footer — Island Directory

Site-wide footer with links, branding, and social. Always last section on page. Max 1 per page.

## Files

| File | Purpose |
|------|---------|
| `layouts/editorial-grid.json` | Multi-column: logo + tagline left, 3 link columns right, social row |
| `layouts/compact.json` | Single-row inline: logo + links + social. Minimal height. |
| `layouts/multi-column.json` | 4-column grid with newsletter signup below |

## Quick Reference

- **Variants**: none (single default)
- **Props**: links, columns, logo, socialLinks, style, newsletter — 10 total
- **Schema**: `vibe://schema/island/Footer`
- **Layouts**: `vibe://islands/footer/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- ALWAYS last section on page
- Max 1 per page
- Typically uses `--lx-surface-alt` or inverted (dark) background
- Pair with: AnnouncementBar (top), Navbar (first) — footer anchors the bottom
- Container: `w-full` outer, `max-w-7xl mx-auto` inner content
- py-16 standard vertical padding (more generous than body sections)
