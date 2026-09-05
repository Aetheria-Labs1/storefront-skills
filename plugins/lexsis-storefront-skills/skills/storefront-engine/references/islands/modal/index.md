# Modal — Island Directory

Container island for overlay content. Holds other islands/content inside.

## Files

| File | Purpose |
|------|---------|
| `layouts/center.json` | Centered overlay with backdrop blur, standard dialog |
| `layouts/side-panel.json` | Slide-in from right, full height drawer |
| `layouts/bottom-sheet.json` | Slides up from bottom, mobile-friendly with drag handle |

## Quick Reference

- **Category**: engagement
- **Props**: trigger, size, position, showClose, backdrop, animation, title, description, primaryAction, secondaryAction, preventClose, fullscreen, scrollable, id, children
- **Required prop**: `trigger` (button text or element that opens modal)
- **Schema**: `vibe://schema/island/Modal`
- **Layouts**: `vibe://islands/modal/layouts/{name}`
- **Contract**: follows `_contract.md` rules (engagement: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`)

## Composition

- Can contain: any island (SizeGuide, OptionResolver, forms, quick-view product)
- Max 1 instance of same modal `id` per page
- Trigger renders as a styled button/link in the page flow
- Gallery shows modal in "open" state for preview purposes
- Pair with: BuyBox (size guide trigger), ProductGallery (quick view), forms (email capture)
