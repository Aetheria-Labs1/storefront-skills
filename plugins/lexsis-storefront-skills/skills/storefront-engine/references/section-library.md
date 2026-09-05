# Quick Section Insert

Insert common section patterns into existing pages — one section at a time, matched to the page's existing brand style. NOT full page generation.

Read `source-artifact-workflow.md` and `page-editing.md`. Every insertion begins
in canonical local source.

## When to Use

- Adding a single section to an existing page (NOT building a full page from scratch)
- User requests a specific section type by name (hero, FAQ, testimonials, etc.)
- Filling a gap in page structure (e.g., "add social proof between hero and product")
- Quick iteration on page layout without regenerating the whole page

## Template Search (do this FIRST)

Before building any section from scratch, search the template library. Search
returns metadata only; fetch authoring source for selected IDs:

```
lexsis_template_library({ action: "search_sections", args: { query, section, mood } })
lexsis_design({ action: "get_section", args: { ids, format: "authoring_source" } })
```

If a match is found → fetch it with `lexsis_design` action `get_section`, use
the returned `source`, swap placeholder content with brand-specific
copy/images, then compile it. Only generate custom HTML when no template
matches.

`format: "compiled_reference"` is renderer-only output. Use it for inspection, never as
input to `lexsis_pages` action `compile` or `lexsis_drafts.page_update_section`.

For a whole page instead of one section, check `lexsis_template_library.search_page_kits` first — it returns curated groupings of existing templates (hero + buy-box + reviews + faq, etc.) that already share one palette/vertical, avoiding the mismatched-brand-imagery problem of hand-picking sections one at a time.

## Prerequisites

- Target page must already exist
- Local page files must exist or be adopted before editing
- The page's store/theme pair must exist in the one-time setup
- Know the desired position (before/after which section, or index)

## Flow

### 1. Identify target page

```
lexsis_pages({ action: "find", args: { query: "page name or slug" } })
```

Or user specifies page by name/ID directly.

### 2. Read current page structure + brand context

```
lexsis_pages({ action: "edit_context", args: { page_id } })
lexsis_pages({ action: "inspect", args: { page_id } })
```

- Note existing section IDs, order, and style patterns
- Identify where new section fits in the narrative flow

### 3. Read saved style context

Read `setupPath`, then resolve the selected store's brand design and selected
theme CSS from the setup index. Confirm the manifest theme ID
matches the remote page. Use the saved colors, fonts, spacing, and `--lx-*`
variables; never silently use another saved theme.

### 4. Select section type from reference table (below)

If the section uses an island component, read its schema:

```
lexsis_design({ action: "island_schema", args: { name: IslandName } })
```

- Confirm lifecycle status, current version, required props, and native variants
- Ensure props match the island's expected shape exactly

### 5. Generate section HTML (single section, not full page)

- Match existing page's color usage, font sizes, spacing
- Use `--lx-*` CSS custom properties from brand kit (not hardcoded values)
- Include responsive breakpoints (mobile-first: 320px, 768px, 1024px, 1440px)
- Include `<!-- section: id -->` and one matching `<section id="id">`
- For islands: use `<lx-island>` with an `application/json` script child
- For plain HTML: use Tailwind classes + inline style with CSS variables

### 6. Change local source and compile

Insert the section in `lexsis-source.html`, update manifest order and island
records, run the shared validator, and compile the complete local page. Compare
the current remote version with the manifest before writing.

### 7. Insert section remotely

```
lexsis_drafts({
  action: "page_update_section",
  args: { page_id, source, position: { "after": "hero" }, expected_version }
})
```

Use `{ "before": "section-id" }`, `{ "after": "section-id" }`, or a numeric
index. Update the manifest's remote version, hashes, and
`lastChangedSections` only after success.

### 8. Visual verify updated page

Navigate to the page preview URL and verify:
- New section renders correctly
- No layout breakage in surrounding sections
- Mobile responsive (no horizontal scroll)
- Islands hydrated (interactive elements working)
- Colors and fonts match the rest of the page

## Section Reference Table

| Section Type | Island | Position Hint | Key Pattern |
|---|---|---|---|
| Hero (full-bleed) | none (HTML) | first | bg-image + overlay text + CTA button |
| Hero (split) | none (HTML) | first | 2-col: image + text/CTA |
| Hero (scrolling images) | none (CSS anim) | first | infinite horizontal scroll bg images + overlay text. CSS `translateX(-50%)` on duplicated slides |
| Hero (before/after) | BeforeAfter | first | centered text top + card with 2× BeforeAfter sliders + numbered features list |
| Hero (curved ribbon) | none (SVG) | first | SVG `<textPath>` on Bezier curves + `<animate>` for flowing text ribbons at bottom |
| Hero (deck slider) | MediaCarousel | first | Use a supported island variant; do not add custom slider JavaScript |
| Hero (organic blob) | none (SVG) | first | SVG `<clipPath clipPathUnits="objectBoundingBox">` organic shape mask. See `blob-shapes.md` |
| Hero (wavy edge) | none (SVG) | first | full-bleed bg + SVG wave top/bottom dividers. `preserveAspectRatio="none"` |
| Product Showcase | ProductGallery + BuyBox | after hero | split layout, gallery left, buy right |
| Testimonials/Reviews | ReviewCarousel | mid-page | card carousel, star ratings |
| FAQ Accordion | FAQ | before footer | collapsible Q&A, schema.org markup |
| Trust Badge Row | TrustBadgeBar | after hero or before CTA | 3-5 icons with short labels |
| Newsletter Signup | EmailCapture | before footer | centered, single input + button |
| Feature Grid | none (HTML) | mid-page | 3-col, icon + heading + description |
| Comparison Table | none (HTML) | mid-page | responsive table, checkmarks |
| CTA Banner | none (HTML) | near bottom | full-width colored band, button |
| Product Carousel | EditorialProductGrid | mid-page | horizontal scroll, 3-4 visible |
| Video Embed | none (HTML) | mid-page | 16:9 aspect ratio container |
| Stats/Counter Row | none (HTML) | after hero | 3-4 big numbers + labels |
| Logo/Press Bar | none (HTML) | after hero | "As seen in" horizontal logos |
| Announcement Bar | AnnouncementBar | very first (position 0) | dismissible top banner |

## Position Guidelines

| Position Rule | Rationale |
|---|---|
| Trust/social proof: within 1 scroll of primary CTA | Reduces friction at decision point |
| FAQ: always before footer | Captures "almost convinced" visitors with objection handling |
| Newsletter: before footer, after main content | Low-commitment conversion for non-buyers |
| Announcement: always position 0 (top of page) | Urgency/promo visibility before scroll |
| Product grid: mid-page for discovery, below fold for cross-sell | Context-dependent placement |

## HTML Template Pattern (for non-island sections)

```html
<!-- section: feature-grid -->
<section id="feature-grid" class="py-16 md:py-24 px-4" style="background-color: var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="font-family: var(--lx-font-heading); color: var(--lx-text-color)">
      Section Title
    </h2>
    <!-- Content here -->
  </div>
</section>
```

## Island Section Pattern

```html
<!-- section: reviews -->
<section id="reviews" class="py-16 md:py-24 px-4" style="background-color: var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <lx-island name="ReviewCarousel" hydrate="visible">
      <script type="application/json">
        {
          "productIds": ["gid://shopify/Product/123"],
          "variant": "grid",
          "pageSize": 6
        }
      </script>
    </lx-island>
  </div>
</section>
```

Key rules for islands:
- Use exact catalog casing and the current active schema
- Keep JSON valid and readable
- Supply every required prop with real IDs
- Prefer native variants over custom headless markup
- Never replace a commerce island with a plain button

## Quality Bar

- Section matches existing page typography (same heading sizes, body font)
- Colors use `--lx-*` CSS custom properties from brand kit (not hardcoded hex)
- Responsive: works at 320px, 768px, 1024px, 1440px breakpoints
- Proper spacing: consistent with adjacent sections (no jarring gaps)
- Islands have valid props matching their schema exactly
- Page still valid after insertion (no layout breaks)
- Section has a unique, kebab-case ID
- No horizontal scroll introduced on mobile
- Images use proper aspect ratios and lazy loading
- CTA buttons meet WCAG AA contrast (4.5:1 min)

## Deprecated Tools (DO NOT USE)

| Removed | Replacement |
|---------|-------------|
| `get_theme_json` | `lexsis_brand` action `brand_kit` (includes theme data) |
| `provision_store` | Handle via Shopify OAuth onboarding, not MCP |
| `extract_brand_design` / `capture_design_source` / `list_design_sources` | No replacement — design DNA extraction from a reference URL is not currently an MCP tool |
| `lexsis_template_library.search_sections` returning `html`/`css`/`js` inline | Search is metadata-only now; call `lexsis_design.get_section({ ids, format: "authoring_source" })` for editable source |
