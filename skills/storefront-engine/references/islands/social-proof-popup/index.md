# SocialProofPopup — Island Directory

Displays real-time purchase notifications or activity counts as toast popups or banners.

## Files

| File | Purpose |
|------|---------|
| `layouts/bottom-left.json` | Fixed toast notification, bottom-left corner |
| `layouts/bottom-right.json` | Fixed toast notification, bottom-right corner |
| `layouts/top-banner.json` | Full-width slim banner showing live activity |

## Quick Reference

- **Variants**: none (position-controlled)
- **Required props**: `position`, `delayMs`, `durationMs`
- **Schema**: `vibe://schema/island/SocialProofPopup`
- **Layouts**: `vibe://islands/social-proof-popup/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Always placed in a hidden/utility section (`class="hidden"`)
- Island renders its own fixed-position overlay — section is just a mount point
- Max 1 SocialProofPopup per page
- Do not pair with StickyBar on same edge (visual collision)
- `top-banner` conflicts with sticky Navbar — use bottom variants when Navbar is sticky
- Default timing: 5000ms delay, 4000ms display duration
