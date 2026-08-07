# Page Planning — Templates & Vocabulary

Reference material for Phase 1 planning. Load when generating a page plan.

---

## Template Search (ALWAYS do this first)

Before planning custom sections, search the template library for pre-built sections. Search returns metadata only (no markup) — fetch it separately for the ids you pick:

```
search_section_templates({ query: "<describe what you need>", section: "<type>", industry: "<vertical>", mood: "<mood>", page_type: "<page_type>" })
get_section_template({ ids: ["<chosen id from results>"] })
```

For a whole page instead of one section at a time, search curated page-kits first — coherent multi-section groupings (hero + buy-box + reviews + faq, etc.) that already share one palette/vertical:

```
search_page_kits({ query: "<describe the page you need>", page_type: "<pdp|landing|homepage|collection>", industry: "<vertical>", mood: "<mood>" })
```

Templates are conversion-proven, pixel-perfect, and faster than generating from scratch. Use them as the starting point — swap copy, images, and colors to match the brand kit.

**Available filters:** section (hero, social-proof, trust, faq, etc.), industry (beauty, fashion, supplements, food, home, tech), mood (bold, clean, warm, editorial, soft, minimal, clinical, rugged, dramatic, neutral, luxurious, calm, modern), page_type (pdp, landing, homepage, collection), islands (filter by islands_used).

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
| `fade-up` | `@keyframes fadeUp` + IntersectionObserver | Default reveal — works everywhere |
| `fade-in` | `opacity 0→1` | Subtle element appearance |
| `scale-in` | `transform: scale(0.95)→1` | Cards, images on scroll |
| `slide-left` / `slide-right` | `translateX` | Before/after, comparison |
| `parallax` | `transform: translateY(calc(...))` on scroll | Hero backgrounds, lifestyle images |
| `sticky` | `position: sticky` | CTA bars, navigation |
| `reveal-on-scroll` | IntersectionObserver + class toggle | Any content section |
| `stagger` | `animation-delay: calc(index * 100ms)` | Grid items, feature lists |
| `counter` | JS number animation | Stats, social proof numbers |
| `none` | — | Trust bars, CTAs (instant credibility) |

**Rules:**
- Hero: `fade-up` on load (no scroll trigger — it's above fold)
- Trust bar: NO animation (instant credibility, never delayed)
- Content sections: `reveal-on-scroll` with `fade-up`
- Grids: `stagger` children
- Final CTA: NO animation (urgency = instant)
- Max 3 different animation types per page (visual coherence)

---

## Visual Rhythm Patterns

### Progressive Relaxation (recommended for landing pages)
```
Hero: TIGHT spacing, HIGH density, WARM colors
  ↓
Middle: MEDIUM spacing, balanced density, NEUTRAL colors
  ↓
End: GENEROUS spacing, LOW density, WARM colors (return to brand)
```

### Alternating Density (good for long pages)
```
Dense section → Spacious section → Dense → Spacious
(content-heavy) → (breathing room) → (content) → (breathe)
```

### Color Temperature Flow
- **Warm open** (brand primary in hero) → **Cool middle** (neutral backgrounds) → **Warm close** (brand primary in final CTA)
- Never put two warm-colored sections adjacent (visual fatigue)
- White/light sections between colored ones = "breathing room"

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
4. **Contrast breaks** — dark section after light = "something new is starting"
5. **Micro-rewards** — animation triggers on scroll = dopamine
