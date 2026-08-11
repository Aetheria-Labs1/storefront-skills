# BuyBox — Fashion/Apparel

## Tone Modifiers

- ctaText: "Add to Bag" (fashion convention, not "Add to Cart")
- Show size availability inline: "S M L XL" with struck-through for OOS
- Emphasize fit: "Model is 5'9" wearing size M"
- Returns copy prominent: "Free returns within 14 days"

## Layout Selection

- Default: `split-pdp.json` (gallery dominates — 1.2fr ratio)
- Gallery needs multiple angles: front, back, detail, model full-length
- BuyBox column: size selector + color swatches + fit guide link

## Prop Overrides

| Prop | Value | Why |
|------|-------|-----|
| ctaText | "Add to Bag" | Fashion industry convention |
| showQuantity | false | Apparel = usually qty 1 |
| variant | "default" | Need full variant picker for size/color |
| showPaymentIcons | true | Apple Pay = faster mobile checkout |

## Copy Patterns (wrapper text)

| Position | Copy | Purpose |
|----------|------|---------|
| Above variant selector | "Select Size" with linked "Size Guide" | Size confidence |
| Below size selector | "Model is 5'9\" / 175cm, wearing size M" | Fit reference |
| Below CTA | "Free shipping over $100 • Free returns" | Fashion standard |
| Below CTA | "Usually ships within 1-2 business days" | Delivery expectation |

## Companion Islands

- `VariantSwatches` — for color selection (type: "color", swatchSize: "lg")
- `SizeGuide` — modal triggered by "Size Guide" link near size selector
- `TrustBadgeBar` — "Free Shipping", "Easy Returns", "Secure Checkout"
- `ProductGallery` with variant: "vertical" — thumbnail strip for outfit angles
- `WishlistButton` — fashion shoppers save-for-later before buying

## Mobile Considerations

- Size selector: full-width buttons (not tiny dropdown)
- Color swatches: horizontally scrollable if >6 options
- "Add to Bag" button: full-width, min-height 48px (thumb-friendly)
- Gallery: horizontal swipe, dots indicator
