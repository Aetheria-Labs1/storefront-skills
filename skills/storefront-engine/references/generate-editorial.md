# Editorial / Magazine-Style Page Generation

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

> References: `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`
> **Workflow:** See `generation-protocol.md` for Phases 1-5 execution (context gathering, HTML generation, validation, publishing). This doc covers page-type-specific patterns only.

Generate long-form editorial pages with cinematic visuals, magazine layout patterns, and restrained shoppable product moments (max 2-3 commerce touchpoints per 1000 words).

## When to Use

- "Create a brand story page"
- "Build a lookbook for our new collection"
- "Magazine-style editorial with shoppable products"
- "Content page that tells our brand story"
- "Journal/blog landing with embedded commerce"
- Any page where narrative and visual storytelling take priority, with commerce woven in after emotional peaks

## CRO Evidence (from CRO-RESEARCH-2026)

- Commerce touchpoints placed **after emotional peaks** (story resolution, reveal moment) convert higher than those interrupting narrative flow
- Aesthetic-Usability Effect: beautiful interfaces perceived as more usable — users forgive more from aesthetically pleasing pages
- Editorial architecture (like Lemaire, Delvaux) signals premium positioning — fewer products per viewport = higher perceived value
- 85% of Awwwards luxury winners use 85%+ viewport as photography or whitespace
- Generous section spacing (80-120px vertical) signals luxury/quality brand (all award winners: 100-200px between sections)
- Full-bleed photography dominates award-winning e-commerce (10/10 Awwwards SOTD winners)
- Drop cap + large body text (text-xl+) with generous line-height creates comfortable magazine reading
- Peak-End Rule: experiences judged by peak moment + ending — invest in final section delight
- Invitation language ("Discover", "Explore") outperforms command language ("Buy Now", "Shop") for editorial/luxury
- UGC photos/videos drive **54% purchase intent** after seeing (Nosto) — embed in gallery sections

## Design Patterns (Award-Winning References)

**Serotoninn style:** High-contrast B&W + single color accent, vertical typography, numbered editorial sections, massive editorial photos, bracket-notation CTAs `[ DISCOVER ]`

**Lemaire style:** Ultra-minimal, lowercase navigation, zero persuasion mechanics, 85%+ viewport is photography/whitespace, radical omission as luxury signal, single product spotlight

**Vero Studio style:** Typography IS the visual (no hero image), italic word emphasis, near-monochrome palette, poetry as transitions, coffee-table-book spacing

**Radian style:** Cinematic scroll-snap, pagination indicators (01/09), progressive disclosure through chapters, geographic coordinates as design elements

## Page-Specific Context Calls

After the standard 4 context calls, also fetch:
```
lexsis_catalog.list            → products to weave into narrative (select 2-5)
lexsis_brand.navigation           → navbar/footer links
```

Heavy use of design library (editorial = existing brand photography, not AI-generated):
```
lexsis_asset_library(action: "search", args: { query: "editorial lifestyle brand" })
lexsis_asset_library(action: "search", args: { query: "behind the scenes studio process" })
lexsis_asset_library(action: "search", args: { query: "texture detail closeup material" })
lexsis_asset_library(action: "search", args: { query: "portrait founder team" })
```

Determine from user input:
- Narrative angle (brand origin, collection story, seasonal mood, day-in-the-life)
- Products to feature (2-5 max shoppable moments)
- Visual mood (minimal/luxe/raw/warm/cool)
- Tone of voice (aspirational, intimate, bold, poetic)

## Asset Discovery (Heavy — Editorial Is Image-Driven)

Editorial pages require 6-10 high-quality images. ALWAYS prioritize existing brand photography over generation:

1. `lexsis_asset_library` action `search` — run 4-6 queries covering hero, lifestyle, texture, behind-scenes, portraits
2. `lexsis_drafts` action `asset_generate` — ONLY for gaps after exhausting library:
   - Hero: style `editorial`, purpose `hero_bg`, aspect `landscape`, quality `high`
   - Look images: style `photography`, purpose `product_lifestyle`, aspect `portrait`, quality `high`
   - Interlude textures: style `photography`, purpose `section_bg`, aspect `landscape`
3. `lexsis_assets.view` — verify EVERY image (editorial quality demands visual review)

Budget: up to 6-8 assets for editorial. Always prefer library over generation.

## Section Architecture (8-10 sections)

Write with generous whitespace (section padding 80-120px vertical). Total narrative content MUST exceed 800 words.

**Section 1: Full-Bleed Cinematic Hero**
- Full-viewport image (min-height: 80vh or 100vh)
- Minimal text: editorial title + category/date label (2-5 words max overlay)
- Text positioned bottom-left with dark gradient overlay
- No navigation clutter — image breathes
- CRO: Radian/Lemaire pattern — photography dominates 85%+ viewport

```html
<section id="hero" class="relative min-h-screen flex items-end overflow-hidden">
  <div class="absolute inset-0">
    <img src="{hero_asset_url}" alt="{contextual alt}" class="w-full h-full object-cover" />
    <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
  </div>
  <div class="relative z-10 max-w-4xl mx-auto px-8 pb-20 md:pb-28">
    <p class="font-[--lx-font-body] text-sm uppercase tracking-[0.2em] text-white/60 mb-4">{Category} · {Season Year}</p>
    <h1 class="font-[--lx-font-heading] text-4xl md:text-6xl lg:text-7xl font-bold text-white leading-[1.1]">
      {Editorial Title}
    </h1>
    <p class="font-[--lx-font-body] text-lg text-white/75 mt-6 max-w-2xl">{Opening hook — one evocative sentence}</p>
  </div>
</section>
```

**Section 2: Opening Narrative (Drop Cap)**
- 200-300 words of storytelling prose
- Wide reading column (max-w-3xl centered)
- Large body text (text-xl) with generous line-height (leading-relaxed)
- Drop cap on first letter (CSS `first-letter:` pseudo-element)
- Set the scene — NO products yet, pure narrative
- Vertical padding: py-20 md:py-32 (80-128px)

```html
<section id="opening" class="py-20 md:py-32 px-6">
  <div class="max-w-3xl mx-auto">
    <p class="font-[--lx-font-body] text-xl md:text-2xl leading-relaxed text-[--lx-text-color]/85 first-letter:text-6xl first-letter:font-[--lx-font-heading] first-letter:font-bold first-letter:float-left first-letter:mr-4 first-letter:mt-1 first-letter:text-[--lx-accent-color]">
      {Opening narrative — 200-300 words setting the scene, introducing the story...}
    </p>
    <p class="font-[--lx-font-body] text-lg leading-relaxed text-[--lx-text-color]/70 mt-8">
      {Second paragraph deepening the story...}
    </p>
    <p class="font-[--lx-font-body] text-lg leading-relaxed text-[--lx-text-color]/70 mt-6">
      {Third paragraph...}
    </p>
  </div>
</section>
```

**Section 3: Shoppable Look #1 (After Emotional Peak)**
- Asymmetric grid: image 60% + product details 40%
- Image: hero-quality lifestyle shot with product in context
- Product details: name, one-line narrative description, price
- `data-placeholder="EditorialProductGrid"` for commerce
- CRO: place commerce AFTER emotional peak (story resolution), not interrupting flow
- Invitation language: "Discover" or "Explore" (not "Buy Now")

```html
<section id="look-1" class="py-20 md:py-28">
  <div class="grid md:grid-cols-5 gap-0 items-stretch">
    <div class="md:col-span-3">
      <img src="{look_1_asset}" alt="{contextual alt}" class="w-full h-full object-cover min-h-[500px]" />
    </div>
    <div class="md:col-span-2 flex flex-col justify-center px-8 md:px-14 py-12 bg-[--lx-bg-color]">
      <p class="font-[--lx-font-body] text-xs uppercase tracking-[0.15em] text-[--lx-accent-color] mb-4">The Look</p>
      <h2 class="font-[--lx-font-heading] text-2xl md:text-3xl font-bold text-[--lx-text-color]">{Look Title}</h2>
      <p class="font-[--lx-font-body] text-[--lx-text-color]/70 mt-4 leading-relaxed">{Narrative description — why this piece matters in the story}</p>
      <div data-placeholder="EditorialProductGrid" class="mt-8 p-4 border border-dashed border-[--lx-border-color] rounded">Product island</div>
    </div>
  </div>
</section>
```

**Section 4: Pull Quote / Interlude**
- Full-width with texture or tinted background
- Large pull quote (text-3xl to text-5xl) centered, italic
- Attribution (founder, designer, brand voice)
- Visual break between shoppable moments
- Generous padding: py-24 md:py-32 (96-128px)
- Optional: Vero Studio style — poetry as transitional section

```html
<section id="interlude" class="py-24 md:py-32 px-6 bg-[--lx-surface-alt]">
  <div class="max-w-4xl mx-auto text-center">
    <blockquote class="font-[--lx-font-heading] text-3xl md:text-4xl lg:text-5xl font-light text-[--lx-text-color] leading-snug italic">
      "{Evocative brand statement or founder quote}"
    </blockquote>
    <cite class="font-[--lx-font-body] text-sm text-[--lx-text-muted] mt-8 block not-italic uppercase tracking-[0.15em]">
      — {Name}, {Title}
    </cite>
  </div>
</section>
```

**Section 5: Mid-Narrative (Continue Story)**
- 150-200 words continuing the narrative arc
- Same reading column (max-w-3xl)
- Text-lg with relaxed line-height
- Build toward the next emotional peak before Look #2
- Internal cross-reference or anecdote

**Section 6: Shoppable Look #2 (Reversed Layout)**
- Mirror layout of Look #1 (image right, text left on desktop)
- Different product(s) featured in new context
- CRO: commerce placed after second emotional peak (reveal moment)
- Same `data-placeholder="EditorialProductGrid"` pattern

**Section 7: Asymmetric Image Grid (Behind the Scenes)**
- 2-3 images in CSS grid with varying spans (not uniform)
- 100-150 words about craft/process/people
- Humanizes the brand — studio shots, raw materials, hands at work
- NO commerce in this section — pure storytelling
- CRO: Aesthetic-Usability Effect — visual polish increases trust

```html
<section id="behind-scenes" class="py-20 md:py-28 px-6">
  <div class="max-w-6xl mx-auto">
    <h2 class="font-[--lx-font-heading] text-2xl font-bold text-[--lx-text-color] mb-12 text-center">Behind the Scenes</h2>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-4">
      <div class="col-span-2 row-span-2">
        <img src="{bts_1}" alt="{alt}" class="w-full h-full object-cover rounded-lg" />
      </div>
      <div class="col-span-1">
        <img src="{bts_2}" alt="{alt}" class="w-full h-full object-cover rounded-lg aspect-square" />
      </div>
      <div class="col-span-1">
        <img src="{bts_3}" alt="{alt}" class="w-full h-full object-cover rounded-lg aspect-square" />
      </div>
    </div>
    <p class="font-[--lx-font-body] text-lg text-[--lx-text-color]/70 mt-10 max-w-2xl mx-auto text-center leading-relaxed">
      {Behind the scenes narrative — craft, process, people, materials}
    </p>
  </div>
</section>
```

**Section 8: Shoppable Collection Grid (Optional, Max 2-3 items)**
- h2: "Explore the Collection" (invitation language, not "Shop Now")
- `data-placeholder="EditorialProductGrid"` with editorial variant
- Clean, minimal cards preserving editorial feel
- 3-4 column grid maximum
- CRO: Peak-End Rule — this is near the end, make it rewarding

**Section 9: Closing Narrative**
- 100-150 words wrapping the story
- Callback to the opening (narrative closure)
- Subtle CTA: "Discover more" linking to collection

**Section 10: Footer**
- Standard brand footer via `lexsis_brand.navigation`

## Required Islands

Replace `data-placeholder="EditorialProductGrid"` with hydrated islands. Maximum 2-3 commerce islands total (editorial restraint):

```html
<div data-island="EditorialProductGrid" data-props='{
  "products": [{"id":"gid://shopify/Product/1","title":"...","price":"$89.00","image":"..."}],
  "columns": {"mobile": 1, "desktop": 2},
  "variant": "editorial",
  "showPrice": true,
  "showQuickAdd": true,
  "ctaText": "Discover"
}'></div>
```

Use `lexsis_design.island_schema("EditorialProductGrid")` to confirm exact prop shape.

## Verification Checklist

- [ ] Cinematic hero: full-bleed, high-quality image, text legible via gradient
- [ ] Drop cap rendering on opening paragraph
- [ ] Generous whitespace between sections (80-120px)
- [ ] Pull quote visually distinct (large italic font, centered, padded)
- [ ] Asymmetric image grid not broken on mobile (single column)
- [ ] Commerce islands only appear after narrative peaks (not interrupting)
- [ ] Maximum 2-3 shoppable moments total
- [ ] Brand colors applied via `--lx-*` variables
- [ ] Fonts loading (heading + body distinct)
- [ ] Total narrative > 800 words (read through for quality)
- [ ] No horizontal scroll on mobile
- [ ] Editorial feel preserved — not a product catalog

## Quality Bar (Editorial-Specific)

- Cinematic full-bleed hero (min-height: 80vh, gradient overlay for text contrast)
- Magazine layout patterns: drop cap, pull quotes, asymmetric grids, full-bleed images
- Maximum 2-3 commerce touchpoints per 1000 words (editorial restraint over conversion pressure)
- Commerce placed AFTER emotional peaks (story resolution, reveal moment)
- Invitation language ("Discover", "Explore") not command language ("Buy Now")
- >800 words total narrative content
- Generous whitespace: section padding 80-120px vertical
- Large body text (text-xl+) with relaxed line-height for comfortable reading
- All images via `lexsis_asset_library` action `search` first (editorial = real photography, not AI)
- Asymmetric/editorial grid layouts (not uniform boxes)
- Pull quotes: large italic font, generous padding, visual separation
- Contextual alt text on all images (narrative, not just product names)
