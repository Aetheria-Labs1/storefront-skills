# MobileMenu — Island Directory

Off-canvas or overlay navigation for mobile viewports. Triggered by hamburger icon in Navbar.

## Quick Reference

- **Variants**: none (single default)
- **Props**: links (array), socials (array), logo (object) — 3 total
- **Schema**: `vibe://schema/island/MobileMenu`
- **Contract**: follows `_contract.md` rules

## Composition

- Placed in a hidden section (only visible when triggered by hamburger icon in Navbar)
- Pair with: Navbar (always — hamburger button triggers this)
- Never visible on desktop (hidden behind interaction trigger)
- Touch targets must be min 48px height for accessibility
- Close button or tap-outside must dismiss
