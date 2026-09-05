# BuyBox — Beauty/Skincare

## Tone Modifiers

- ctaText: "Add to My Routine" (not generic "Add to Cart")
- Show "per-use cost" for premium products: "$1.20/application"
- Reviews badge: "Verified Purchase" with photo count
- Emphasize routine integration, not one-time purchase

## Layout Selection

- Default: `split-pdp.json` for hero products
- Add `IngredientExplorer` island below BuyBox (after trust badges)
- If product has shade/color variants: configure `VariantSwatches` with `type: "color"` in BuyBox props area

## Prop Overrides

| Prop | Value | Why |
|------|-------|-----|
| ctaText | "Add to My Routine" | Routine language = repeat purchase framing |
| showSubscription | true | Beauty = high repeat purchase rate |
| showPaymentIcons | true | Reduces checkout anxiety |

## Copy Patterns (wrapper text, NOT inside island)

| Position | Copy | Purpose |
|----------|------|---------|
| Below price | "Enough for X weeks" | Volume context reduces sticker shock |
| Above CTA | "Free returns within 30 days" | Anxiety reducer |
| Below CTA | "X people have this in their routine" | Social proof |
| Trust badges | "Dermatologist Tested", "Cruelty Free", "Clean Ingredients" | Category-specific trust |

## Companion Islands

- `IngredientExplorer` below BuyBox (variant: "editorial")
- `TrustBadgeBar` with beauty-specific badges (cruelty-free, dermatologist-tested)
- `ReviewCarousel` filtered to photo reviews
- `BeforeAfter` for treatment products (serums, retinol)
