# Brand Homepage Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`
> **Workflow:** See `generation-protocol.md` for Phase 0-4 execution (context gathering, HTML generation, validation, publishing). This doc covers page-type-specific patterns only.

Generate brand-first homepages. Navigation-driven, multi-CTA, storytelling-focused. Category grid adds +18% engagement. Featured products carousel drives discovery. Navbar + Footer islands REQUIRED.

## Triggers

"homepage", "home page", "main page", "front page", "store home"

## CRO-Backed Section Ordering

```
1. Navbar/SiteHeader   — full navigation (REQUIRED island)
2. Hero                — brand lifestyle visual + value prop CTA
3. Categories Grid     — +18% engagement vs flat product list
4. Bestsellers         — featured products carousel (social proof via "popular")
5. Brand Story         — editorial mid-page (founder, mission, craft)
6. Testimonials        — 3 reviews with real names/photos (+22% CVR)
7. Trust Bar           — press logos + certifications (3-5 max)
8. Newsletter          — email capture with incentive ("10% off first order")
9. Footer              — full nav columns + legal + social (REQUIRED island)
```

## Page-Specific Context Calls

After the standard 4 context calls, also fetch:
```
get_navigation          → header nav links, footer columns, collection hierarchy
list_products           → identify bestsellers, new arrivals, featured items
```

`get_navigation` is CRITICAL for homepages — it provides the full site structure.

## Page-Specific Rules

- Multiple CTAs to DIFFERENT destinations (explore, shop, learn — not all same link)
- Full-width hero (lifestyle imagery, not product-only)
- Max-width 7xl for content sections
- Mobile: hamburger nav, single column, touch-friendly targets (48px min)

## Required Islands

| Island | Placement | Props Source |
|--------|-----------|-------------|
| **Navbar / SiteHeader** (REQUIRED) | Section 1 | `get_navigation` → links[], logo |
| **Footer** (REQUIRED) | Section 9 | `get_navigation` → footer links, social |
| EditorialProductGrid | Section 4 | `list_products` → bestsellers array |
| EmailCapture | Section 8 | provider, listId, incentive |

```html
<!-- SiteHeader -->
<div data-island="SiteHeader" data-props='{"logo":{"src":"...","alt":"Brand"},"links":[{"label":"Shop","href":"/collections/all"},{"label":"About","href":"/pages/about"}],"cartEnabled":true}'></div>

<!-- Footer -->
<div data-island="Footer" data-props='{"logo":{"src":"..."},"columns":[{"title":"Shop","links":[...]},{"title":"About","links":[...]}],"social":[{"platform":"instagram","url":"..."}],"newsletter":true}'></div>
```

Use `vibe://schema/island/SiteHeader` and `vibe://schema/island/Footer` for exact props.

## Award-Winning Homepage Patterns

### Marine Layer Style (Editorial + Transactional Hybrid)
- Dual-path hero segmentation: "New for Him" / "New for Her"
- "This Just In" horizontal scroll carousel between editorial sections
- Quick-add from grid: hover reveals size selector (reduces clicks to purchase)
- Curated "shops within the shop" (Espresso Edit, Hemp Shop)
- 365-day return policy in announcement bar
- Color swatch visibility on grid cards
- Free shipping threshold in cart drawer

### Orbea Style (Full-Bleed Cinematic)
- Full-viewport video hero with brand manifesto overlay
- Category grid with dramatic overlay text
- Progressive product disclosure through scroll
- Minimal text: 2-5 words per section headline
- Dark background, product provides color
- Geographic identity embedded in narrative

### DTC Wellness (Clean + Trustworthy)
- Soft, warm hero with lifestyle imagery
- Category pills for quick filtering
- Ingredient/process transparency section
- Doctor/expert endorsement mid-page
- Subscription CTA prominent
- Clean whitespace signaling premium positioning

## Homepage-Specific CRO Data

| Tactic | Impact | Source |
|--------|--------|--------|
| Category grid (vs flat list) | +18% engagement | Shopify 2026 |
| Featured products carousel | Discovery path creation | Marine Layer pattern |
| Social proof below fold | Acceptable (not critical above fold on homepages) | NNGroup |
| Multiple CTAs (different goals) | Expected on homepages (unlike LPs) | Conversion Rate Experts |
| Announcement bar (shipping/returns) | Reduces cart abandonment anxiety | Route 2026 |
| Newsletter with incentive | 10-15% signup rates | Industry avg |
| Editorial mid-page (brand story) | Increases time-on-site, reduces bounce | Awwwards analysis |

## Verification Checklist

- [ ] SiteHeader island renders with navigation links from `get_navigation`
- [ ] Hero communicates brand value prop in 3 seconds (not product-specific)
- [ ] Multiple CTAs go to DIFFERENT destinations (shop, about, collections)
- [ ] Category/collection grid links are functional
- [ ] Featured products show real data (real prices, real titles)
- [ ] Footer renders with all nav columns + social + payment icons
- [ ] Mobile: hamburger nav works, single column, touch-friendly
- [ ] Brand colors applied via `--lx-*` variables (not defaults)
- [ ] Fonts loading (not system fallback)
- [ ] Heading hierarchy: single h1 in hero, h2 per section

## Page Feels Editorial, Not Catalog

The homepage is a BRAND experience. It should feel like a magazine cover, not a product spreadsheet:
- Generous whitespace between sections (py-16 md:py-24 minimum)
- Lifestyle photography > product-on-white
- Copy speaks to identity/values, not just features
- Collections named creatively (not just "Shirts" — "The Weekend Edit")
- Visual rhythm: alternate full-bleed and contained sections
- First and last impressions matter most (Serial Position Effect)
