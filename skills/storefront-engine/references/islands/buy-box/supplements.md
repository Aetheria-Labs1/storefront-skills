# BuyBox — Supplements/Wellness

## Tone Modifiers

- ctaText: "Start Your Supply" or "Subscribe & Save 20%"
- Lead with subscription option (supplements = monthly reorder)
- Clinical, evidence-based language — no miracle claims
- Show serving count: "60 capsules • 30-day supply"

## Layout Selection

- Default: `sticky-sidebar.json` (long PDP with clinical details beside)
- Left column: gallery + ingredient breakdown + clinical studies
- Right sidebar: sticky BuyBox with subscription toggle

## Prop Overrides

| Prop | Value | Why |
|------|-------|-----|
| ctaText | "Subscribe & Save 20%" | Subscription-first framing |
| showSubscription | true | Always — supplements = repeat |
| variant | "expanded" | Show stock level + delivery estimate |
| showQuantity | true | Users buy 2-3 months at once |

## Copy Patterns (wrapper text)

| Position | Copy | Purpose |
|----------|------|---------|
| Below price | "60 capsules • 30-day supply" | Serving context |
| Below price | "$0.83/serving" | Per-serving cost reduction framing |
| Above CTA | "Subscribe: Free shipping + 20% off every order" | Subscription incentive |
| Below CTA | "Cancel anytime • No commitment" | Risk reducer |
| Trust badges | "Third-Party Tested", "GMP Certified", "Made in USA" | Supplement-specific trust |

## Companion Islands

- `SubscriptionToggle` — always include (one-time vs subscribe)
- `TrustBadgeBar` with cert badges (NSF, GMP, third-party tested)
- `PDPInfoCards` with dosage instructions, timing, stacking advice
- `QuantityBreaks` — "Buy 2, Save 10%" tier pricing
- `ReviewCarousel` filtered to "results after X weeks" reviews

## Urgency Elements

- `InventoryIndicator` with variant "badge" — "Only 12 left in stock"
- Avoid fake urgency — supplement buyers are research-heavy, distrust pressure
