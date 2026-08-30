# Bundle Builder Page Generation

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

> References: `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`
> **Workflow:** See `generation-protocol.md` for Phases 1-5 execution (context gathering, HTML generation, validation, publishing). This doc covers page-type-specific patterns only.

Generate interactive bundle-builder pages with step-based UX, discount tier visualization, live price calculation, and progress indicators via the BundleBuilder island.

## When to Use

- "Create a build-your-own bundle page"
- "Box builder where customers pick 3-5 products"
- "Mix and match page with volume discounts"
- "Bundle deal landing page"
- Any page where customers assemble a multi-product bundle with tiered pricing

## CRO Evidence (from CRO-RESEARCH-2026)

- Progress bar toward next discount tier increases AOV **+18%** (Goal-Gradient Effect: motivation increases with proximity to goal)
- Showing savings as dollar amount (not just %) improves completion **+12%** ("You're saving $14.70" > "Save 15%")
- Pre-selected starter bundle for decision-fatigued users reduces choice paralysis (Hick's Law: decision time increases with options)
- "X bundles sold today" urgency counter leverages social proof without fake scarcity
- Sticky CTA + above-fold CTA combined = **+12% CVR** (Digital Applied 2026)
- Stack/bundle builders increase AOV **30-50%** (CRO-RESEARCH supplements data)
- Mobile sticky summary at bottom leverages Fitts' Law (infinite-width targets at screen edge)
- Free shipping threshold indicators in cart: "Add $15 more for free shipping" activates Goal-Gradient Effect

## Page-Specific Context Calls

After the standard 4 context calls, also fetch:
```
lexsis_catalog.list            → bundleable products catalog
lexsis_brand.navigation           → navbar/footer links
lexsis_design.island_schema("BundleBuilder") → props shape, config, slots
```

Determine from user input:
- Product pool (which products can be bundled)
- Minimum/maximum items per bundle (default: min 2, max 6)
- Discount tiers (default: 2 items = 10%, 3 = 15%, 4+ = 20%)
- Bundle theme/name (e.g., "Build Your Skincare Routine")

## Asset Discovery

1. `lexsis_asset_library` action `search` — hero imagery, lifestyle shots showing bundles/boxes
2. `lexsis_drafts` action `asset_generate` — hero background if none found (style: `photography`, purpose: `hero_bg`, aspect: `landscape`)
3. Product images come from `lexsis_catalog.get(id)` for each bundleable item
4. `lexsis_assets.view` — verify hero asset quality

## Section Architecture (7 sections)

**Section 1: Hero (Savings Hook)**
- h1: "Build Your [Category] Bundle & Save Up to [max]%"
- Subtitle emphasizing mix-and-match + escalating savings
- Visual showing example bundle (3-4 product thumbnails fanned)
- Primary CTA: "Start Building" (anchor to product grid)
- CRO: savings amount in hero headline not just percentage (+12% completion)

```html
<section id="hero" class="relative min-h-[60vh] flex items-center justify-center px-6 overflow-hidden">
  <div class="absolute inset-0 bg-gradient-to-br from-[--lx-accent-color]/10 via-[--lx-bg-color] to-[--lx-lavender]/10"></div>
  <div class="relative z-10 text-center max-w-3xl mx-auto">
    <p class="text-sm font-semibold text-[--lx-accent-color] uppercase tracking-wide font-[--lx-font-body] mb-4">Build Your Box</p>
    <h1 class="font-[--lx-font-heading] text-4xl md:text-6xl font-bold text-[--lx-text-color] leading-tight">
      Build Your Bundle<br/>
      <span class="text-[--lx-accent-color]">Save Up to 20%</span>
    </h1>
    <p class="font-[--lx-font-body] text-lg text-[--lx-text-muted] mt-4 max-w-xl mx-auto">
      Mix and match your favorites. The more you add, the more you save.
    </p>
    <a href="#products" class="inline-block mt-8 px-8 py-4 bg-[--lx-accent-color] text-white font-semibold rounded-lg hover:bg-[--lx-accent-color-hover] transition-colors text-lg">
      Start Building
    </a>
  </div>
</section>
```

**Section 2: Step Progress Indicator**
- 3-step visual: Choose (active) → Review → Checkout
- Sticky on scroll (`position: sticky; top: 0; z-index: 30`)
- Current step uses `--lx-accent-color`, inactive uses `--lx-text-muted`
- Connecting lines between steps

```html
<nav id="progress" class="sticky top-0 z-30 bg-[--lx-bg-color]/95 backdrop-blur border-b border-[--lx-border-color] py-4">
  <div class="max-w-4xl mx-auto flex items-center justify-center gap-4">
    <div class="flex items-center gap-2">
      <span class="w-8 h-8 rounded-full bg-[--lx-accent-color] text-white flex items-center justify-center text-sm font-bold">1</span>
      <span class="font-[--lx-font-body] text-sm font-medium text-[--lx-text-color]">Choose</span>
    </div>
    <div class="w-12 h-px bg-[--lx-border-color]"></div>
    <div class="flex items-center gap-2">
      <span class="w-8 h-8 rounded-full bg-[--lx-surface-alt] text-[--lx-text-muted] flex items-center justify-center text-sm font-bold">2</span>
      <span class="font-[--lx-font-body] text-sm text-[--lx-text-muted]">Review</span>
    </div>
    <div class="w-12 h-px bg-[--lx-border-color]"></div>
    <div class="flex items-center gap-2">
      <span class="w-8 h-8 rounded-full bg-[--lx-surface-alt] text-[--lx-text-muted] flex items-center justify-center text-sm font-bold">3</span>
      <span class="font-[--lx-font-body] text-sm text-[--lx-text-muted]">Checkout</span>
    </div>
  </div>
</nav>
```

**Section 3: Discount Tier Visualization**
- Visual tier ladder: 3 cards showing escalating savings
- Current tier highlighted with accent border + background tint
- "Add X more for next tier" nudge text
- Show dollar savings (not just %): CRO +12% completion
- CRO: progress bar toward next tier +18% AOV

```html
<section id="tiers" class="py-12 px-6 bg-[--lx-surface-alt]">
  <div class="max-w-3xl mx-auto">
    <h2 class="font-[--lx-font-heading] text-2xl font-bold text-center text-[--lx-text-color] mb-8">The More You Add, The More You Save</h2>
    <div class="grid grid-cols-3 gap-4">
      <div class="text-center p-6 rounded-xl border-2 border-[--lx-accent-color] bg-[--lx-accent-color]/5">
        <p class="text-3xl font-bold text-[--lx-accent-color]">10%</p>
        <p class="text-sm text-[--lx-text-muted] mt-1">2 items</p>
        <p class="text-xs text-[--lx-accent-color] mt-2 font-medium">Save ~$7</p>
      </div>
      <div class="text-center p-6 rounded-xl border-2 border-[--lx-border-color]">
        <p class="text-3xl font-bold text-[--lx-text-color]">15%</p>
        <p class="text-sm text-[--lx-text-muted] mt-1">3 items</p>
        <p class="text-xs text-[--lx-text-muted] mt-2">Save ~$14</p>
      </div>
      <div class="text-center p-6 rounded-xl border-2 border-[--lx-border-color]">
        <p class="text-3xl font-bold text-[--lx-text-color]">20%</p>
        <p class="text-sm text-[--lx-text-muted] mt-1">4+ items</p>
        <p class="text-xs text-[--lx-text-muted] mt-2">Save ~$24+</p>
      </div>
    </div>
  </div>
</section>
```

**Section 4: Product Selection Grid (BundleBuilder zone)**
- h2: "Choose Your Products"
- Responsive grid: 2 cols mobile, 3-4 cols desktop
- Each product card: image, name, individual price, "Add to Bundle" button
- Optional category filter tabs above grid
- `data-placeholder="BundleBuilder"` wrapping the grid
- CRO: pre-select a "starter bundle" for decision-fatigued users (Hick's Law)

```html
<section id="products" class="py-16 px-6">
  <div class="max-w-6xl mx-auto">
    <h2 class="font-[--lx-font-heading] text-2xl md:text-3xl font-bold text-[--lx-text-color] text-center mb-8">Choose Your Products</h2>
    <p class="text-center text-[--lx-text-muted] font-[--lx-font-body] mb-8">Select 2 or more items to unlock bundle savings</p>
    <div data-placeholder="BundleBuilder" class="border-2 border-dashed border-[--lx-border-color] rounded-xl p-8 min-h-[400px] flex items-center justify-center">
      <p class="text-[--lx-text-muted]">BundleBuilder island: product grid + live cart + tier progress</p>
    </div>
  </div>
</section>
```

**Section 5: Social Proof**
- "X bundles sold today" urgency counter (real data, not fake)
- 2-3 customer testimonials specific to bundles/value
- Star ratings with review excerpts
- UGC images of received bundles
- CRO: social proof after claims that raise skepticism (+22% with real names)

```html
<section id="social-proof" class="py-16 px-6 bg-[--lx-surface-alt]">
  <div class="max-w-4xl mx-auto text-center">
    <p class="font-[--lx-font-body] text-sm font-semibold text-[--lx-accent-color] uppercase tracking-wide">Trusted by Bundlers</p>
    <p class="font-[--lx-font-heading] text-3xl font-bold text-[--lx-text-color] mt-2">1,247 bundles built this week</p>
    <div class="grid md:grid-cols-3 gap-6 mt-12">
      <!-- Testimonial cards with real names, photos, star ratings -->
    </div>
  </div>
</section>
```

**Section 6: FAQ**
- h2: "Bundle FAQs"
- 4-6 questions: pricing, changes, minimums, shipping
- Schema.org FAQPage JSON-LD embedded
- CRO: FAQ before final CTA handles objections (Serial Position Effect)

**Section 7: Mobile Sticky Summary**
- Fixed bottom bar on mobile (hidden on desktop)
- Shows: item count, current savings, "View Bundle" button
- Leverages Fitts' Law: infinite-width target at screen edge

```html
<div class="fixed bottom-0 left-0 right-0 z-50 md:hidden bg-[--lx-bg-color] border-t border-[--lx-border-color] p-4 shadow-lg">
  <div class="flex items-center justify-between">
    <div>
      <p class="font-[--lx-font-body] text-sm font-medium text-[--lx-text-color]">0 items selected</p>
      <p class="font-[--lx-font-body] text-xs text-[--lx-accent-color]">Add 2+ to save</p>
    </div>
    <button class="px-6 py-3 bg-[--lx-accent-color] text-white rounded-lg font-semibold text-sm">View Bundle</button>
  </div>
</div>
```

## Required Islands

Replace `data-placeholder="BundleBuilder"` with the hydrated island:

```html
<div data-island="BundleBuilder" data-props='{
  "products": [{"id":"gid://shopify/Product/1","title":"...","price":"$34.00","image":"..."}],
  "minItems": 2,
  "maxItems": 6,
  "discountTiers": [
    {"minQuantity": 2, "discountPercent": 10, "label": "Save 10%"},
    {"minQuantity": 3, "discountPercent": 15, "label": "Save 15%"},
    {"minQuantity": 4, "discountPercent": 20, "label": "Save 20%"}
  ],
  "layout": "grid",
  "columns": {"mobile": 2, "tablet": 3, "desktop": 4},
  "showProgress": true,
  "preselected": []
}'></div>
```

Use `lexsis_design.island_schema("BundleBuilder")` to confirm exact prop shape before mapping.

## Bundle-Specific Validation Checks

- BundleBuilder island has valid product IDs from the store
- Discount tiers are logically sequential (higher qty = higher discount)
- Sticky elements (progress bar, mobile summary) don't overlap
- Price displays use consistent currency formatting
- Island props match schema from `lexsis_design.island_schema`

## Verification Checklist

- [ ] Hero CTA scrolls to product grid
- [ ] Step progress indicator sticky and visible
- [ ] Discount tier cards rendering with correct percentages
- [ ] BundleBuilder island hydrated (products visible, add buttons work)
- [ ] Mobile sticky summary bar visible on small viewports
- [ ] Brand colors applied via `--lx-*` variables
- [ ] No horizontal scroll on mobile
- [ ] Progress bar updates as items added (island handles this)
- [ ] Dollar savings shown alongside percentage

## Quality Bar (Bundle-Specific)

- BundleBuilder island correctly configured with valid product IDs and discount tiers
- Discount tier visualization shows both percentage AND dollar savings (+12% completion)
- Progress bar toward next tier visible (+18% AOV)
- Pre-selected starter bundle option for choice-paralyzed users
- Step progress indicator sticky and functional
- Mobile: sticky bottom summary bar, swipeable product grid (2-col)
- "X bundles sold today" social proof (real, not fabricated)
- Proper heading hierarchy (h1 hero, h2 per section)
- FAQ includes Schema.org FAQPage JSON-LD
- Minimum 2 items required before checkout CTA enables
- Currency formatting consistent throughout
