# Quick Section Insert

Insert common section patterns into existing pages — one section at a time, matched to the page's existing brand style. NOT full page generation.

## When to Use

- Adding a single section to an existing page (NOT building a full page from scratch)
- User requests a specific section type by name (hero, FAQ, testimonials, etc.)
- Filling a gap in page structure (e.g., "add social proof between hero and product")
- Quick iteration on page layout without regenerating the whole page

## Template Search (do this FIRST)

Before building any section from scratch, search the template library:

```
search_section_templates({ query: "video testimonial carousel with stars", section: "social-proof", mood: "warm" })
```

If a match is found → use the template's HTML/CSS/JS directly, swap placeholder content with brand-specific copy/images. Only generate custom HTML when no template matches.

## Prerequisites

- Target page must already exist (use `page-generation` skill for new pages)
- Brand kit should be configured (read it to match styles)
- Know the desired position (before/after which section, or index)

## Flow

### 1. Identify target page

```
find_page({ query: "page name or slug" })
```

Or user specifies page by name/ID directly.

### 2. Read current page structure + brand context

```
get_page({ page_id })
```

```
inspect_page_sections({ page_id })
```

- Note existing section IDs, order, and style patterns
- Identify where new section fits in the narrative flow

### 3. Read brand kit for style matching

```
get_brand_kit
```

- Extract colors, fonts, spacing to match new section to existing page
- All generated CSS must use `--lx-*` variables, never hardcoded hex values

### 4. Select section type from reference table (below)

If the section uses an island component, read its schema:

```
vibe://schema/island/{IslandName}
```

- Get required props, variants, and configuration options
- Ensure props match the island's expected shape exactly

### 5. Generate section HTML (single section, not full page)

- Match existing page's color usage, font sizes, spacing
- Use `--lx-*` CSS custom properties from brand kit (not hardcoded values)
- Include responsive breakpoints (mobile-first: 320px, 768px, 1024px, 1440px)
- For islands: use `data-island="Name" data-props='JSON'` pattern
- For plain HTML: use Tailwind classes + inline style with CSS variables

### 6. Preview the section update (dry-run)

```
preview_section_update({ page_id, section_id: null, html, css, position })
```

- Dry-run to verify it won't break page layout
- Check for conflicts with existing sections

### 7. Insert section into page

```
update_page_section({ page_id, section_id: null, html, css, position })
```

- `null` section_id = "add new" (not update existing)
- Position formats: `"before:{section_id}"`, `"after:{section_id}"`, or numeric index

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
| Hero (deck slider) | none (JS) | first | nth-child positioned cards. Active=full bg, 3-5=thumbnails. JS rotates DOM order on click |
| Hero (organic blob) | none (SVG) | first | SVG `<clipPath clipPathUnits="objectBoundingBox">` organic shape mask. See `reference/blob-shapes.md` |
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
<section class="py-16 md:py-24 px-4" style="background-color: var(--lx-bg-color)">
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
<section class="py-16 md:py-24 px-4" style="background-color: var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <div data-island="ReviewCarousel" data-props='{"provider":"shopify","productId":"gid://shopify/Product/123","layout":"cards","columns":3}'></div>
  </div>
</section>
```

Key rules for islands:
- Always use `data-island="Name"` attribute (exact casing from catalog)
- Always use `data-props='JSON'` with single quotes wrapping valid JSON
- Read `vibe://schema/island/{name}` before generating to get correct prop shape
- Never nest islands inside each other

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
| `get_theme_json` | `get_brand_kit` (includes theme data) |
| `provision_store` | Handle via Shopify OAuth onboarding, not MCP |
