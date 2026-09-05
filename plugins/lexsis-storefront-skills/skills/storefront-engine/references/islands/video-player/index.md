# VideoPlayer — Island Directory

Content video playback island. Supports inline, hero, and background loop modes.

## Files

| File | Purpose |
|------|---------|
| `layouts/hero-fullwidth.json` | Full-width 16:9 video with centered play button overlay |
| `layouts/inline-card.json` | Video in bordered card, content-flow width (max-w-3xl) |
| `layouts/background-loop.json` | Autoplay muted loop as section background with text overlay |

## Quick Reference

- **Variants**: default, autoplay, background
- **Required prop**: `src` (video URL)
- **Schema**: `vibe://schema/island/VideoPlayer`
- **Layouts**: `vibe://islands/video-player/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Hero usage: pair with headline overlay text, CTA buttons
- Inline: pair with product details, testimonials, feature descriptions
- Background: replaces static hero image, overlay with Hero or Headline island
- Pair with: Hero, BuyBox, TestimonialCarousel, FeatureGrid
