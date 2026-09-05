# Page Planning — Templates & Vocabulary

> House rules in `storefront-engine/references/design-rules.md` override every example below.
> Examples show structure and copy intent; their styling (gradients, hover transforms,
> uppercase labels, pills, emoji, section fills) is illustrative and must not be copied.
> Where an example conflicts with a house rule, the rule wins.

Reference material for Phase 1 planning. Load when generating a page plan.

---

## Template Search (ask first, then browse)

Ask the user whether they want to pick a page kit or sections themselves before
searching. The catalog is small (about 30 page kits, about 200 section
templates), so browsing beats ranking. An empty `query` browses the catalog and
opens the Template Gallery in hosts with inline UI; wait for the
`Design template selection:` message before choosing yourself. Search returns
metadata only (no markup); fetch source separately for the ids you pick:

```
lexsis_template_library.search_page_kits({ query: "", page_type: "<page_type>", industry: "<vertical>", mood: "<mood>", limit: 20 })
lexsis_template_library.search_sections({ query: "", section: "<type>", industry: "<vertical>", mood: "<mood>", page_type: "<page_type>" })
lexsis_template_library.get_kit({ kit: "<slug or pasted https://storefront.trylexsis.com/templates/kits/<slug>>" })
lexsis_design.get_section({ ids: ["<chosen id from results>"], format: "authoring_source" })
```

When the user declines to pick, search with a description instead and present
at most three candidates for confirmation. Page kits are coherent
multi-section groupings (hero + buy-box + reviews + faq) that already share one
palette and vertical; a kit is a list of section-template slugs, hydrated one
to three at a time.

Templates are a starting point: swap copy, images, and colors to match the
brand kit, and keep the house rules above every example.

**Available filters** (mirrors `storefront-renderer/public/templates/registry.json`):
section (hero, buy-box, social-proof, trust, reviews, faq, product-info,
interactive, navigation, countdown, guarantee, comparison); industry (beauty,
fashion, fashion-accessories, jewelry, sportswear, supplements, food, home,
tech); mood (bold, clean, warm, editorial, soft, minimal, clinical, rugged,
dramatic, neutral, luxurious, calm, modern, playful, cinematic, energetic);
page_type (pdp, landing, homepage, guided-commerce, campaign, editorial,
collection, article); archetype (for kits, e.g. conversion_optimized_pdp,
ingredient_led_pdp, ugc_pdp, concern_landing, listicle_landing, advertorial,
bundle_landing, offer_landing, quiz_funnel, gifting, seasonal); islands
(filter by islands_used).

---

## Section Templates by Page Type

### Landing Page (8-10 sections)

| # | Section Type | Purpose | Typical Island |
|---|---|---|---|
| 1 | `hero-split` or `hero-full` | Hook + primary CTA above fold | BuyBox (if PDP-hybrid) |
| 2 | `trust-bar` | Instant credibility (logos, ratings, stats) | TrustBadgeBar |
| 3 | `problem-solution` | Emotional pain → product as answer | — |
| 4 | `features-grid` or `benefits-stack` | Key differentiators (3-4 items) | — |
| 5 | `social-proof` | Reviews, testimonials, UGC | ReviewCarousel |
| 6 | `how-it-works` | 3-step process / usage flow | — |
| 7 | `comparison-table` | vs competitors or before/after | ComparisonTable |
| 8 | `faq` | Objection handling | FAQ |
| 9 | `final-cta` | Urgency + repeat offer | BuyBox or StickyBar |
| 10 | `footer` | Navigation + legal | — |

### PDP (6-8 sections)

| # | Section Type | Purpose | Typical Island |
|---|---|---|---|
| 1 | `hero-product` | Gallery + BuyBox side-by-side | BuyBox |
| 2 | `trust-bar` | Shipping, returns, guarantees | TrustBadgeBar |
| 3 | `benefits-icons` | Key product benefits with icons | — |
| 4 | `ingredients` or `specs` | What's inside / technical details | — |
| 5 | `reviews` | Social proof (filterable) | ReviewCarousel |
| 6 | `faq` | Product-specific questions | FAQ |
| 7 | `related-products` | Cross-sell grid | ProductGrid |
| 8 | `sticky-cta` | Persistent add-to-cart on scroll | StickyBar |

### Homepage (7-8 sections)

| # | Section Type | Purpose | Typical Island |
|---|---|---|---|
| 1 | `hero-full` | Brand statement + seasonal push | — |
| 2 | `featured-products` | Best sellers / new arrivals | ProductGrid |
| 3 | `brand-story` | Mission, values, origin | — |
| 4 | `categories` | Collection navigation tiles | — |
| 5 | `testimonials` | Customer stories | ReviewCarousel |
| 6 | `press-logos` | As seen in... | — |
| 7 | `newsletter` | Email capture | NewsletterSignup |
| 8 | `footer` | Full navigation | — |

### Collection (5-6 sections)

| # | Section Type | Purpose | Typical Island |
|---|---|---|---|
| 1 | `collection-hero` | Category intro + lifestyle image | — |
| 2 | `filter-bar` | Sort/filter controls | FilterBar |
| 3 | `product-grid` | Main product listing | ProductGrid |
| 4 | `promo-card` | Mid-grid promotional insert | — |
| 5 | `trust-bar` | Shipping + returns guarantee | TrustBadgeBar |
| 6 | `newsletter` | Email capture | NewsletterSignup |

### Editorial (6-8 sections)

| # | Section Type | Purpose | Typical Island |
|---|---|---|---|
| 1 | `editorial-hero` | Magazine-style header + byline | — |
| 2 | `intro-copy` | Hook paragraph + context | — |
| 3 | `shoppable-gallery` | Products in lifestyle context | ProductGrid |
| 4 | `content-block` | Long-form with pull quotes | — |
| 5 | `expert-quote` | Authority / credibility | — |
| 6 | `product-spotlight` | Featured product deep-dive | BuyBox |
| 7 | `related-reads` | Content cross-links | — |
| 8 | `footer` | Navigation | — |

---

## Animation Vocabulary

| Effect | CSS/JS | When to Use |
|--------|--------|-------------|
| `fade-up` | `@keyframes fadeUp` + IntersectionObserver | Never by default; the one plan-named moment |
| `fade-in` | `opacity 0→1` | Subtle element appearance |
| `scale-in` | `transform: scale(0.95)→1` | Cards, images on scroll |
| `slide-left` / `slide-right` | `translateX` | Before/after, comparison |
| `parallax` | `transform: translateY(calc(...))` on scroll | Only a plan-named full-bleed image |
| `sticky` | `position: sticky` | CTA bars, navigation |
| `reveal-on-scroll` | IntersectionObserver + class toggle | Never by default; one plan-named moment at most |
| `stagger` | `animation-delay: calc(index * 100ms)` | Never by default; only inside the one plan-named moment |
| `counter` | JS number animation | Stats, social proof numbers |
| `none` | — | The default for every section |

**Rules:**
- Default is `none`. Animate nothing unless the plan names one moment
- Hero: `fade-up` on load only if the plan names the hero as that moment
- Trust bar: NO animation (instant credibility, never delayed)
- Content sections: `none` by default (never reveal-on-scroll per section)
- Grids: `none` by default (never stagger children)
- Final CTA: NO animation (urgency = instant)
- Max 1 orchestrated moment per page; hover/focus/open-close feedback is always fine

---

## Visual Rhythm Patterns

### Progressive Relaxation (recommended for landing pages)
```
Hero: TIGHT spacing, HIGH density
  ↓
Middle: MEDIUM spacing, balanced density
  ↓
End: GENEROUS spacing, LOW density
```

### Density Rhythm (good for long pages)
```
Dense section → Spacious section → Dense → Spacious
(content-heavy) → (breathing room) → (content) → (breathe)
```

### One Background
- One page background from navbar to footer; vary density and spacing, not colour.
- Section separation is spacing, type scale and a 1px hairline.

### Spacing Scale
- Between sections: `py-16` (mobile) / `py-24` (desktop) default
- Dense sections: `py-12` / `py-16`
- Spacious sections: `py-20` / `py-32`
- Hero: full viewport height or `min-h-[80vh]`

---

## Inter-Section Communication Patterns

### Narrative Structures

**Problem → Solution → Proof → Action** (classic landing page)
- Hero: State the desired outcome
- Section 2-3: Identify the pain, introduce the solution
- Section 4-6: Prove it works (reviews, data, before/after)
- Section 7+: Ask for the action

**Story Arc** (editorial, brand pages)
- Hook → Context → Rising tension → Climax (product) → Resolution (CTA)

**AIDA** (ad-driven traffic)
- Attention (hero) → Interest (benefits) → Desire (social proof) → Action (CTA)

### CTA Placement Strategy

| Page Type | CTA Count | Placement |
|-----------|-----------|-----------|
| Landing | 3 | Hero, mid-page (after social proof), final section |
| PDP | 2 | BuyBox (hero), Sticky bar (scroll) |
| Homepage | 2-3 | Hero, featured products, newsletter |
| Collection | 1 | Each product card (implicit) |

**Rules:**
- First CTA: always above fold (hero)
- Never 2 CTAs visible simultaneously (except sticky + in-content)
- CTA copy escalates: "Learn More" → "See Results" → "Get Started" → "Buy Now"
- Final CTA: strongest urgency (scarcity, guarantee, bonus)

### Social Proof Distribution

- **Early** (section 2-3): Lightweight (star rating bar, "10,000+ customers", press logos)
- **Middle** (section 5-6): Heavy (full testimonials, before/after, video reviews)
- **Late** (before final CTA): Reinforcement (single powerful quote, guarantee badge)

Never cluster all social proof in one place — distribute it to answer doubts as they arise.

---

## Scroll Incentive Patterns

What makes users keep scrolling:
1. **Visual hooks** — partially visible next section (cut off image, peeking headline)
2. **Curiosity gaps** — "Here's what 10,000 customers discovered..."
3. **Progressive disclosure** — numbered steps (1/3 visible = "where's 2 and 3?")
4. **Type-scale breaks** — a larger heading or a hairline after dense copy = "something new is starting"
5. **Micro-rewards** — a numbered step or a revealed answer (not scroll animation)
