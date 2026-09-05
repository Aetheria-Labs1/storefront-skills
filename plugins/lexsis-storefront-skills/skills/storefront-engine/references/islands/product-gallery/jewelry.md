# ProductGallery — Jewelry/Accessories

## Tone

- Close-up detail shots essential (gemstones, clasps, engravings)
- Show scale: on hand/wrist/neck + beside reference object
- Sparkle/light play in photography — clean white bg or soft gradient

## Layout Selection

- Default: `grid-2x2.json` for rings/earrings (square images, detail-heavy)
- For necklaces/watches: `hero-thumbnails.json` (large main for full piece)
- Editorial: `editorial-asymmetric.json` for collection pages

## Image Requirements

- Min 5 images: full piece, worn (on body), detail/gemstone, clasp/back, scale reference
- Aspect ratio: 1/1 (square — jewelry is compact, doesn't need portrait)
- Background: pure white or soft gradient (never busy)
- Lighting: highlight brilliance without blown-out reflections

## Prop Overrides

| Prop | Value | Why |
|------|-------|-----|
| layout | "grid" | Square tiles for detail views |
| enableZoom | true | CRITICAL — customers inspect quality |
| aspectRatio | "1/1" | Compact items, square works |
| backgroundColor | "#fafafa" | Subtle bg for transparent/white products |
| maxImages | 6 | Jewelry needs more angles than apparel |

## Companion Context

- Size reference text: "Band width: 4mm" or "Chain length: 18 inches"
- Material callout: "18K Gold Vermeil over Sterling Silver"
- Care instructions link near gallery
