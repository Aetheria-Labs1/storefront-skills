# Competitor Remix (Rebuild from Reference URL)

Capture a competitor page, decompose its structure, and rebuild it using the user's own brand identity, copy, and products. NEVER copy content -- only structural inspiration.

## Prerequisites

- User provides a reference URL
- Store connected and brand kit configured
- User's own product/content available to replace competitor's

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Capture Reference Design

```
capture_design_source({ url })
```

Screenshots the page and extracts structural layout data.

The agent should analyze the screenshot to extract the competitor's design DNA: color palette, typography, spacing rhythm, border radius, shadow depth, image treatment style, overall aesthetic (minimal, bold, editorial, etc.).

### Step 3 — Decompose into Section Map

Analyze captured page into numbered section breakdown:
```
1. Full-bleed hero — product centered, headline overlay, gradient wash
2. Trust badge row — 4 icons with micro-labels, centered
3. Split feature section — image left, text right, 50/50
4. Testimonial carousel — 3 cards, star ratings, photos
5. Product grid — 3 columns, hover zoom
6. FAQ accordion — 6 items, expandable
7. Final CTA — full-width, contrasting background
```

For each: note layout pattern, content type, approximate proportions, interactive elements.

### Step 4 — Map to Lexsis Capabilities

For each competitor section:
- Island available? Use `get_island_schema(island_name)` for prop shapes
- Static HTML+Tailwind section? (most common)
- Requires custom interactivity? Flag for JS sandbox

### Step 5 — Match Existing Templates + Source Assets

```
search_section_templates({ query: "<competitor section description>", section: "<type>", industry: "<vertical>" })
search_design_library({ query: "<relevant product/category>" })
list_products({ limit: 10 })
```

For each competitor section, check if a pre-built template matches the pattern. Templates give you proven HTML/CSS/JS — just swap content.

Replace ALL competitor imagery with user's own assets. Generate new if needed:
```
generate_asset({ prompt: "...", style_reference: "brand_kit" })
```

CRITICAL: NEVER reference, hotlink, or reuse competitor images/copy/logos.

### Step 6 — Two-Phase Generation

**Phase A — Raw HTML + Tailwind (no islands)**

For each section from the decomposition:
- **Structure**: Keep competitor's layout pattern (grid, split, stacked)
- **Brand**: Replace ALL colors/fonts/spacing with user's `--lx-*` variables
- **Content**: Write original copy serving user's value proposition
- **Images**: User's own assets exclusively
- **CTAs**: Aligned with user's conversion goals

Set all brand tokens in `theme_css`:
```css
:root { --lx-accent-color: #...; --lx-font-heading: '...', serif; }
```

Mark interactive placeholders: `<div data-placeholder="BuyBox" class="..."></div>`

**Phase B — Island Mapping**

Replace placeholders with hydrated islands:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
<div data-island="FAQ" data-props='{"items":[{"question":"...","answer":"..."}]}'></div>
```

### Step 7 — Validate and Publish Draft

```
validate_vibe_page(page_data)
publish_vibe_page(page_data, { publish: false })
```

Returns `preview_url`.

### Step 8 — Visual Verification

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open preview_url.

**Other IDEs:** Provide URL: "Preview: {url} -- open to verify alongside reference."

Checklist:
- [ ] ZERO competitor content carried over (no copy, images, logos)
- [ ] All colors from user's `--lx-*` variables (not competitor palette)
- [ ] Structural similarity recognizable but not pixel-perfect
- [ ] User's brand fonts loading (not system fallback)
- [ ] Mobile layout works independently
- [ ] Islands hydrated with user's own product data
- [ ] Original copy serves user's value proposition

If issues found: `update_page_section` to fix, then re-verify.

## Decision Points

| Question | Decision |
|----------|----------|
| Keep exact structure or adapt? | Adapt: remove irrelevant sections, add where user has more to say |
| Which sections to skip? | Competitor-specific (their awards, team), navigation that does not fit |
| How close to follow? | Structural only -- proportions, flow, section types |
| Interactive elements? | Map to available islands; static equivalent if no island exists |

## Quality Gates

- ZERO competitor content (copy, images, logos, brand marks)
- Page uses exclusively user's `--lx-*` CSS variables
- All images are user's own or freshly generated
- All product references from user's own catalog
- Copy is original, serving user's value proposition
- Mobile layout independent (do not assume competitor's responsive approach)
- Page passes `validate_vibe_page` with zero errors
