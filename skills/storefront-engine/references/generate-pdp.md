# Product Detail Page (PDP) Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`
> **Workflow:** See `generation-protocol.md` for Phases 1-5 execution (context gathering, HTML generation, validation, publishing). This doc covers page-type-specific patterns only.

Generate high-converting product detail pages. BuyBox island is REQUIRED. Sticky CTA adds +12% CVR. Reviews placement adds +22% CVR. Variant swatches reduce bounce 15%.

## Triggers

"product page", "PDP", "product detail", "product landing", "product showcase"

## CRO-Backed Section Ordering

```
1. Hero (Split)         — product visual + benefit headline + CTA above fold
2. Product Gallery      — swipeable images, zoom on desktop
3. BuyBox + Variants    — price visible without scrolling (CRITICAL)
4. Benefits Grid        — 3-5 benefit cards with icons
5. Ingredients/Specs    — transparency builds trust (63% research ingredients before buying)
6. Reviews              — +22% CVR with real names/photos (place after claims)
7. Related Products     — cross-sell grid (Magnolia Bakery pattern)
8. FAQ                  — objection handling immediately before final CTA
9. Sticky CTA (mobile)  — +12% CVR, appears after scrolling past BuyBox
```

## Page-Specific Context Calls

After the standard 4 context calls, also fetch:
```
get_product(product_id) → title, variants, images, price, metafields
get_navigation          → navbar/footer links
list_products           → related products for cross-sell
```

## Required Islands

| Island | Placement | Props Source |
|--------|-----------|-------------|
| **BuyBox** (REQUIRED) | Section 3 | `get_product` → variants, price, images |
| ProductGallery | Section 2 | `get_product` → images array |
| VariantSwatches | Section 3 | `get_product` → variant options |
| StickyCart | Section 9 | product title + price |
| ReviewCarousel | Section 6 | provider + productId |
| FAQ | Section 8 | items[{question, answer}] |

```html
<!-- BuyBox (REQUIRED) -->
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[{"id":"v1","title":"30ml","price":"$29.99"},{"id":"v2","title":"60ml","price":"$49.99"}],"images":["url1","url2"]}}'></div>

<!-- StickyCart -->
<div data-island="StickyCart" data-props='{"product":{"title":"...","price":"$29.99"},"threshold":600}'></div>
```

## Page-Specific Rules

- Price MUST be visible without scrolling
- Single h1 (product title), h2 per section
- Hero height: 420-550px (Seton.de data: -11% bounce, +19% engagement)

## Niche Variants

### Beauty PDP
- Hero: dewy product shot with soft lighting, split-layout
- Ingredients section: hero actives with source/science, EWG/cruelty-free badges
- Before/after UGC gallery (+54% purchase intent — Nosto)
- Routine builder: "Your AM/PM ritual" (increases AOV via bundling)
- Texture close-ups reduce returns by setting sensory expectations

### Supplement PDP
- Clinical data section: study results with specific numbers ("23% improvement in 8 weeks")
- Dosage/serving info prominently displayed
- Third-party testing badges (NSF, USP, ConsumerLab) — significant trust lift
- Transformation timeline: "Week 1... Week 4... Week 12..."
- Subscribe & save with 15-25% discount anchoring
- NO aggressive countdown timers on health products (erodes trust)

### Fashion PDP
- Size guide section with model measurements + fabric details (reduces returns 20-30%)
- Two-image product cards (front + hover alternate view)
- "Complete the look" cross-sell section
- Color variant swatches visible on first viewport
- Free returns messaging prominent (82% say returns influence purchase)

## Verification Checklist

- [ ] BuyBox island hydrates (shows product, not empty div)
- [ ] Price visible without scrolling on mobile
- [ ] Variant selector works (swatches clickable)
- [ ] Sticky CTA appears after scrolling past BuyBox
- [ ] Product images render (not broken placeholders)
- [ ] Brand colors applied via `--lx-accent-color` (not default purple)
- [ ] Mobile: no horizontal scroll, single column stack
- [ ] CTA contrast ratio >= 4.5:1 (WCAG AA)

## Section CSS Pattern

```html
<section id="pdp-hero" class="py-16 md:py-24 px-4" style="background: var(--lx-bg-color);">
  <div class="max-w-7xl mx-auto">
    <!-- Content with --lx-* variables -->
  </div>
</section>
```

## Conversion Data Reference

| Tactic | Impact | Source |
|--------|--------|--------|
| Sticky CTA + above-fold CTA | +12% CVR | Digital Applied 2026 |
| Real testimonials with names/photos | +22% CVR | Digital Applied 2026 |
| Variant swatches (vs dropdown) | -15% bounce | CXL |
| Size guide presence | -20-30% returns | Baymard |
| Before/after UGC | +54% purchase intent | Nosto |
| Subscribe & save option | +30-50% AOV | Supplement industry avg |
| FAQ before final CTA | Objection handling at decision point | NNGroup |
| Price visible without scroll | Table stakes (abandonment if hidden) | Baymard |
