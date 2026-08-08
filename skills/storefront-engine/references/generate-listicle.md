# SEO Listicle / Comparison Page Generation

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then run `compile_page_source`.

> References: `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`
> **Workflow:** See `generation-protocol.md` for Phases 1-5 execution (context gathering, HTML generation, validation, publishing). This doc covers page-type-specific patterns only.

Generate SEO-optimized long-form listicle and comparison pages (>2000 words) with proper heading hierarchy, anchor navigation, and embedded commerce islands.

## When to Use

- "Top 10 best [products] for [use case]"
- "[Brand A] vs [Brand B]" comparison pages
- "Best alternatives to [product]"
- "Product roundup" or "buyer's guide"
- Any search-intent page designed to rank and convert

## CRO Evidence (from CRO-RESEARCH-2026)

- Anchor nav (sticky TOC on desktop) increases time-on-page **+40%** — users jump between entries, reducing bounce
- Comparison table placed at page bottom captures "ready to buy" readers — they scroll past entries → land on table → decide
- Winner badge on recommended product drives **+25% CTR** over unbadged entries
- FAQ before final CTA handles objections at decision point (Serial Position Effect: last items best remembered)
- Real testimonials with names increase trust **+22% CVR** (Digital Applied 2026)
- E-E-A-T signals (author byline, last-updated date, methodology) correlate with higher search placement and user trust

## Page-Specific Context Calls

After the standard 4 context calls, also fetch:
```
list_products            → full product catalog (select featured items)
get_navigation           → navbar/footer links for internal linking
```

Determine from user input:
- Primary keyword (h1 target)
- Product list (3-10 products to feature)
- Comparison criteria (price, features, use case, rating)
- Author name for E-E-A-T byline

## Asset Discovery

For each product in the listicle:
1. `search_design_library` — find existing product/lifestyle imagery
2. `get_product(product_id)` — pull product images, price, description
3. `generate_asset` — only if no suitable imagery exists (style: `photography`, purpose: `product_lifestyle`)
4. `view_asset` — verify before embedding

Generate one hero asset for the page header (style: `editorial`, purpose: `hero_bg`, aspect: `landscape`).

## Section Architecture

Write 8-12 sections:

**Section 1: Hero + E-E-A-T Signals**
- h1 matching primary keyword exactly
- Subtitle with freshness signal: "Updated [Month] [Year] — [N] products tested"
- Author byline with name, role, and avatar
- Last-updated date + methodology disclosure link
- Full-bleed background or gradient

```html
<section id="hero" class="relative py-20 md:py-28 px-6 bg-[--lx-bg-color]">
  <div class="max-w-4xl mx-auto text-center">
    <h1 class="font-[--lx-font-heading] text-4xl md:text-5xl font-bold text-[--lx-text-color] leading-tight">{Keyword-Matched Title}</h1>
    <p class="font-[--lx-font-body] text-lg text-[--lx-text-muted] mt-4">Updated July 2026 — {N} products tested over {X} weeks</p>
    <div class="flex items-center justify-center gap-3 mt-6">
      <img src="{author_avatar}" alt="{Author Name}" class="w-10 h-10 rounded-full" />
      <div class="text-left">
        <p class="font-[--lx-font-body] text-sm font-medium text-[--lx-text-color]">{Author Name}</p>
        <p class="font-[--lx-font-body] text-xs text-[--lx-text-muted]">{Role} · {X} years in {category}</p>
      </div>
    </div>
  </div>
</section>
```

**Section 2: Sticky Table of Contents (Anchor Nav)**
- Desktop: sticky sidebar or horizontal sticky bar below header
- Ordered list linking to each `#product-N` section ID
- "Jump to verdict" shortcut at end
- CRO: anchor nav increases time-on-page +40%

```html
<nav id="toc" class="sticky top-0 z-40 bg-[--lx-bg-color]/95 backdrop-blur border-b border-[--lx-border-color] py-3 px-6 overflow-x-auto">
  <ol class="flex gap-6 max-w-5xl mx-auto text-sm font-[--lx-font-body] whitespace-nowrap">
    <li><a href="#product-1" class="text-[--lx-text-muted] hover:text-[--lx-accent-color] transition-colors">1. {Name}</a></li>
    <li><a href="#product-2" class="text-[--lx-text-muted] hover:text-[--lx-accent-color] transition-colors">2. {Name}</a></li>
    <!-- ... -->
    <li><a href="#verdict" class="font-semibold text-[--lx-accent-color]">Verdict</a></li>
  </ol>
</nav>
```

**Section 3: Introduction + Methodology**
- h2: "How We Chose the Best [Category]"
- 150-200 words: selection criteria, testing methodology
- Internal links to related pages via `get_navigation`
- Methodology disclosure builds E-E-A-T trust

**Sections 4-N: Product Entries (one per product)**
- h2: "[Product Name] — Best for [Use Case]"
- Product image (alternating left/right layout per entry)
- 150-250 word mini-review
- h3 sub-sections for features where needed
- Pros/Cons as structured lists
- Key specs mini-table
- Star rating visual (CSS-only using `--lx-accent-color`)
- `data-placeholder="BuyBox"` where commerce island goes
- Winner badge (CRO: +25% CTR on recommended product):

```html
<section id="product-1" class="py-16 px-6 border-b border-[--lx-border-color]">
  <div class="max-w-4xl mx-auto">
    <div class="grid md:grid-cols-2 gap-8 items-start">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-[--lx-accent-color]/10 text-[--lx-accent-color] rounded-full text-xs font-semibold mb-3">
          <span>★</span> Editor's Choice
        </div>
        <span class="text-sm font-semibold text-[--lx-accent-color] uppercase tracking-wide">#1 Pick</span>
        <h2 class="font-[--lx-font-heading] text-3xl font-bold text-[--lx-text-color] mt-2">{Product Name}</h2>
        <p class="text-sm text-[--lx-text-muted] mt-1">Best for: {use case}</p>
        <p class="mt-4 font-[--lx-font-body] text-[--lx-text-color]/80 leading-relaxed">{Review paragraph}</p>
        <div class="mt-4 grid grid-cols-2 gap-4">
          <div>
            <h3 class="font-semibold text-green-600 text-sm">Pros</h3>
            <ul class="mt-1 space-y-1 text-sm text-[--lx-text-color]/70"><li>+ {pro}</li></ul>
          </div>
          <div>
            <h3 class="font-semibold text-red-500 text-sm">Cons</h3>
            <ul class="mt-1 space-y-1 text-sm text-[--lx-text-color]/70"><li>- {con}</li></ul>
          </div>
        </div>
        <div data-placeholder="BuyBox" class="mt-6 p-4 border border-dashed border-[--lx-border-color] rounded">Add to cart island</div>
      </div>
      <div>
        <img src="{asset_url}" alt="{product name}" class="rounded-lg shadow-md w-full" />
      </div>
    </div>
  </div>
</section>
```

**Section N+1: Comparison Table**
- Full-width responsive table with feature matrix
- Highlight "Best Overall" / "Best Value" / "Best Premium" rows
- Mobile: horizontal scroll with sticky first column
- CRO: captures ready-to-buy readers who scrolled through all entries

**Section N+2: Verdict (Winner)**
- h2: "Our Top Pick"
- `data-placeholder="BuyBox"` for winning product
- Runner-up mention linking back to its anchor

**Section N+3: FAQ with Schema.org JSON-LD**
- h2: "Frequently Asked Questions"
- 5-8 questions targeting "People Also Ask" queries
- Embedded FAQPage structured data:

```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"...","acceptedAnswer":{"@type":"Answer","text":"..."}}]}
</script>
```

**Section N+4: Related Content (Internal Linking)**
- 3-4 card grid linking to related listicles/collections
- Anchor text optimized for adjacent keywords

## Required Islands

Each product entry gets its own BuyBox island:

```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[{"id":"...","title":"Default"}]}}'></div>
```

Use `get_island_schema("BuyBox")` to confirm exact prop shape.

## SEO Validation Checks

- Exactly one h1 tag (hero)
- h2 for each product entry, h3 for sub-features
- All anchor nav links resolve to section IDs
- FAQ schema JSON-LD is valid
- Total word count > 2000
- No duplicate section IDs

## Verification Checklist

- [ ] Sticky TOC visible and functional on desktop
- [ ] All anchor links scroll to correct sections
- [ ] Product images rendering (not broken placeholders)
- [ ] Winner badge visible on recommended product
- [ ] Comparison table scrollable on mobile (no overflow)
- [ ] BuyBox islands hydrated with real product data
- [ ] Brand colors applied via `--lx-*` variables
- [ ] FAQ accordion functional
- [ ] No horizontal scroll on mobile

## Quality Bar (Listicle-Specific)

- Total word count > 2000 across all sections
- Proper heading hierarchy: h1 (hero) → h2 (entries) → h3 (features)
- Sticky anchor nav with valid section ID targets
- Comparison table responsive (horizontal scroll on mobile, sticky first column)
- Each product entry has a working BuyBox island
- FAQ includes valid Schema.org FAQPage JSON-LD
- Winner badge on recommended product (+25% CTR)
- Author byline + last-updated date (E-E-A-T)
- Internal linking structure via `get_navigation`
