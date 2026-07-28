# Campaign / Ad Landing Page Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`
> **Workflow:** See `generation-protocol.md` for Phase 0-4 execution (context gathering, HTML generation, validation, publishing). This doc covers page-type-specific patterns only.

Generate high-converting post-click landing pages. ZERO navigation (+30% CVR from reduced distraction). Single CTA repeated 3x minimum. Message-match from ad creative is non-negotiable.

## Triggers

"landing page", "campaign page", "ad landing", "post-click", "LP", "convert ad to page"

## Core Principles (CRO-Backed)

- **ZERO navigation** — every link is an exit. Remove header nav entirely. +30% CVR (EmailVendorSelection)
- **Single CTA repeated 3x** — hero, mid-page offer, bottom (minimum)
- **Message-match** — headline must echo ad within 2 words (mismatch = bounce spike)
- **One page, one goal** — no wishlists, comparisons, social shares alongside primary CTA
- **Hero height: 420-550px** — Seton.de cut 850→420px: -11% bounce, +19% form fills

## CRO Section Ordering (Cold Traffic DTC)

```
1. Hero               — message-match headline + product visual + CTA (above fold)
2. Social Proof Bar   — star rating + review count + press logos (3-5 max)
3. Problem/Solution   — pain points → product as answer (2-3 bullets)
4. Product Demo       — video (click-to-play ONLY, never autoplay: -7% CVR) or carousel
5. Benefits Grid      — 3-6 differentiators with icons, mapped from ad claims
6. Detailed Proof     — 2-3 full testimonials with photos + real names (+22% CVR)
7. Ingredients/How    — transparency section or 3-step "How It Works"
8. Comparison         — vs competitors or vs doing nothing (subtle)
9. FAQ                — 4-6 objection-handling Qs immediately before CTA
10. Final CTA         — restate offer + guarantee + urgency
```

## Page-Specific Context Calls

After the standard 4 context calls, also fetch:
```
analyze_ad_creative(url)    → extract headline, claims, colors, CTA, tone, product
match_persona_to_ad(...)    → target persona (demographics, pain points, motivations)
get_product(product_id)     → product data for BuyBox island
list_products               → catalog context
```

## Traffic Source Calibration

### Meta (Facebook/Instagram) — Warm, Social Proof Heavy
- Hero matches ad visual exactly (same product angle, lighting, model)
- Shorter copy, more visual storytelling
- Social proof dominant: reviews, UGC, influencer mentions (+63% trust vs brand content)
- Urgency elements: limited stock, time-bound offer
- Before/after transformations (54% purchase after visual UGC — Nosto)

### Google (Search/Shopping) — Intent-Driven, Feature-First
- Hero directly answers search query intent
- Detailed specs, comparison tables, feature lists
- Credibility: certifications, expert endorsements, clinical data
- Structured information layout (scannable, F-pattern aware)
- FAQ section more prominent (searchers have specific questions)

### TikTok — Scroll-Stopping, Video-Native
- Bold visual hero with energy/movement
- Short punchy copy (1-2 lines per section max)
- Creator-style social proof (not corporate testimonials)
- Before/after transformations front and center
- Price reveal after desire built (younger demo more price-sensitive)

## Required Islands

Only ONE commerce island needed (BuyBox). Minimal islands = fast page load.

```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$39.99","compareAtPrice":"$59.99","variants":[...],"images":["..."]},"offer":{"discount":"33%","badge":"Limited Time"}}'></div>
```

Use `vibe://schema/island/BuyBox` for exact prop shape.

## Page-Specific Rules

- NO `<nav>` elements, NO anchor links in header/footer — logo only, non-clickable
- CTA buttons: min 48px height, full-width on mobile, `--lx-accent-color`
- Max-width: 5xl (narrower than PDP — focused reading lane)
- Mobile sticky CTA bar at bottom

## Hero Patterns by Niche

### Supplements — Product-in-Action Hero
- Full-bleed product on nightstand/kitchen counter (usage context)
- Benefit headline matching ad: "Finally Sleep Through the Night"
- Single CTA + one trust signal (star rating or "Free shipping")

### Beauty — Split-Hero (Product + Copy)
- 50/50 split: product left (dewy macro shot), copy + CTA right
- "As seen in" press logos beneath hero
- Price anchoring visible without scroll

### Fashion — Video Hero (Click-to-Play)
- Compelling thumbnail (NOT autoplay — saves 7% CVR loss)
- Creator-style try-on video
- Bold 2-5 word headline overlay

## Urgency Tactics: What Works vs. What Backfires

**Works (data-backed):**
- Limited-time offer with real end date (not resetting timer)
- Low stock indicator on genuinely scarce items
- "Free shipping ends tonight" with actual deadline
- Seasonal/launch window messaging

**Backfires (trust-destroying):**
- Countdown timers that reset on refresh — destroys ALL trust permanently
- "Only 2 left!" on always-available products
- Fake "live viewer" counts
- Urgency on health/wellness products (erodes trust in category)

## Verification Checklist

- [ ] ZERO navigation links (no header nav, no footer nav, logo not clickable)
- [ ] Headline matches ad creative within 2-word difference
- [ ] CTA button appears minimum 3 times (hero, offer, final)
- [ ] All CTA buttons perform same action (single goal)
- [ ] No competing actions (no wishlist, share, compare buttons)
- [ ] Hero above fold with product visual + CTA visible (no scroll needed)
- [ ] Mobile: sticky bottom CTA bar present
- [ ] Brand colors applied via `--lx-accent-color`
- [ ] No autoplay video (click-to-play only)

## Conversion Data Reference

| Tactic | Impact | Source |
|--------|--------|--------|
| Remove navigation | +30% CVR | EmailVendorSelection |
| Sticky CTA + above-fold CTA | +12% CVR | Digital Applied 2026 |
| Real testimonials (names + photos) | +22% CVR | Digital Applied 2026 |
| Personalized CTAs | +202% vs default | HubSpot |
| Autoplay video | -7% CVR (AVOID) | Digital Applied 2026 |
| Message mismatch (ad vs page) | Bounce spikes | Nik Sharma |
| Single CTA focus | +10% CVR | EmailVendorSelection |
| Hero 420-550px height | -11% bounce, +19% fills | Seton.de case study |
| FAQ before final CTA | Objection handling | NNGroup serial position |
