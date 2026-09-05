# ProductHero — Island Directory

Full-viewport product launch hero with image, headline, and primary CTA.

## Quick Reference

- **Variants**: stacked, splitLeft, splitRight, fullHeight
- **Required prop**: `productId` (Shopify GID)
- **Schema**: `vibe://schema/island/ProductHero`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: StickyBar (triggers when hero scrolls out), TrustBadgeBar, BuyBox (below)
- Hero always uses `--lx-bg-color` or image (never surface-alt)
- Only one h1 per page — ProductHero owns it
- Place TrustBadgeBar or social-proof within 1 scroll of the hero CTA
