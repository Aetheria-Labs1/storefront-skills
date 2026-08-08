# Ad Creative to Landing Page

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then run `compile_page_source`.

Generate a high-converting landing page from an ad creative with full scent continuity (headline, palette, CTA, tone match from click to page).

## Prerequisites

- At least one ad creative synced (Meta/Google/TikTok)
- Store connected and brand kit configured

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Identify and Analyze the Ad

```
get_ad_creatives({ store_id, status: "active" })
```

Present available creatives (thumbnail + headline + spend). User picks one, or use highest-spend active creative.

```
analyze_ad_creative({ creative_id })
```

Extracts: headline, subheadline, claims, color_palette, tone, cta_text, target_audience, urgency_signals, imagery_style.

### Step 3 — Match Persona and Source Assets

```
match_persona_to_ad({ creative_id })
```

Maps to persona: demographics, pain points, motivations, objections, buying stage. Determines page tone.

```
search_design_library({ query: "<product/topic from ad>" })
```

Find product shots and lifestyle images matching the ad aesthetic. Use `generate_asset` if library insufficient.

### Step 4 — Two-Phase Page Generation

**Phase 4a — Raw HTML + Tailwind (no islands)**

Generate full page as HTML + Tailwind. Scent continuity rules:
- Hero headline = ad headline (semantic match, max 2-word variation)
- `--lx-accent-color` set to ad's dominant color
- CTA text matches or escalates the ad CTA
- First fold answers the same promise the ad made
- Zero navigation links (single CTA focus)

Structure: Hero > Problem/Agitation > Solution > Social Proof > Features > CTA repeat > FAQ

Mark interactive placeholders: `<div data-placeholder="BuyBox" class="..."></div>`

Use `--lx-*` CSS variables in `theme_css` for all brand colors and fonts.

**Phase 4b — Island Mapping**

Replace placeholders with hydrated islands:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
```

Use `get_island_schema` for exact prop shapes.

### Step 5 — Validate and Publish Draft

```
compile_page_source({ source, head, theme_css, scripts })
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
```

Always publish as draft first. Returns `preview_url`.

### Step 6 — Visual Verification

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open preview_url.

**Other IDEs:** Provide URL: "Preview: {url} -- open to verify."

Checklist:
- [ ] Hero headline matches ad headline (scent continuity)
- [ ] Brand colors applied via `--lx-*` variables (not defaults)
- [ ] Single CTA focus (no nav leakage)
- [ ] Mobile layout not broken (stack, readable text)
- [ ] Islands hydrated (BuyBox shows product data)
- [ ] Social proof section present

If issues found: `update_section_from_source` to fix, then re-verify.

## Decision Points

| Question | Decision |
|----------|----------|
| Which ad? | Ask user, or highest-spend active creative |
| Which product? | Extract from ad analysis (primary product) |
| Draft or live? | Always draft first -- user confirms |
| Long or short? | Video ad = longer storytelling; static = concise |
| Include pricing? | Only if ad mentions price/discount explicitly |

## Quality Gates

- Hero headline >=80% semantic similarity to ad headline
- Color palette matches ad dominant colors (set via `--lx-accent-color`)
- Single primary CTA throughout (no competing actions)
- Mobile-first layout (most ad traffic is mobile)
- No navigation links that leak traffic from conversion
- Ad urgency signals carried through (countdown, limited stock, etc.)
- Page passes `compile_page_source` with zero errors
