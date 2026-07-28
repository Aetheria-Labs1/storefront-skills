# Storefront Page Generation

Generate high-quality Shopify storefront pages using the Lexsis AI MCP tools.

> **Prerequisites**: Read `vibe://docs/generation-guide` and `vibe://skills/generation-protocol` first — they define the VibePage schema, CSS variable system, island integration, and visual verification step.

## Generation Flow (Two-Phase)

### Phase 0 — Context Gathering (run ALL in parallel)

```
get_workspace_details    → workspace ID
get_connected_stores     → store domain
get_brand_kit            → logo, fonts, colors, voice, border radius
get_design_md            → brand brief + design philosophy + don'ts
list_products            → product catalog (for commerce islands)
get_navigation           → navbar/footer links
search_design_library    → existing brand assets (hero images, lifestyle shots)
search_section_templates → pre-built section templates matching the brief
```

All 8 calls can run in parallel. Wait for all before proceeding.

> **Template-first rule:** Always search `search_section_templates` before generating sections from scratch. Matching templates are faster, conversion-proven, and pixel-perfect. Only generate custom HTML when no template fits the brief.

### Phase 1 — Template Selection + Asset Preparation

**Step 1: Search templates for each section in the page plan:**
```
search_section_templates({ query: "hero with video background for fashion", section: "hero", industry: "fashion", mood: "editorial" })
```
- If a matching template is found (score > 0.7): USE IT. Swap placeholder content for brand-specific copy/images.
- If no match: generate from scratch in Phase 2.

**Step 2: Asset preparation (for both template-based and custom sections):**
1. `search_design_library` — check existing assets FIRST (always)
2. `generate_asset` — only if library has nothing suitable
3. `edit_asset` — composite/modify if needed
4. `view_asset` — verify result before using in page

Budget: 3-5 generated assets per page max. Existing assets = free.

### Phase 2A — Raw HTML Generation (No Islands)

Generate complete VibePage JSON with pure HTML + Tailwind CSS:
- Place `data-placeholder="IslandName"` divs where islands will go
- Focus entirely on visual design: layout, typography, color, spacing, imagery
- Apply brand CSS variables in `theme_css`
- Use Google Fonts URLs in `head.fonts`
- Write real copy (never Lorem Ipsum)
- Use asset URLs from Phase 1 in `<img>` tags

This renders instantly in any browser — iterate on design here.

### Phase 2B — Island Mapping

Replace placeholders with actual islands:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[{"id":"v1","title":"Default","available":true}]}}'></div>
```

Use `vibe://schema/island/{name}` resource to get exact prop shapes for each island.

### Phase 3 — Validation

```
validate_vibe_page(page_json)
```

Fix any errors. Common issues: duplicate section IDs, invalid island names, missing required props, inline `<style>`/`<script>` tags.

### Phase 4 — Publish + Visual Verify

```
publish_vibe_page(slug, page, archetype, publish=false)  → preview_url
```

**Visual verification is REQUIRED before marking complete:**

| Agent | How to Verify |
|-------|--------------|
| Claude Code | `browser_navigate(preview_url)` → `browser_take_screenshot({fullPage: true})` → review screenshot |
| Codex | Use built-in browser to open preview_url |
| Cursor | Open preview_url in browser, take screenshot with available tool |
| No browser | Provide preview_url to user: "Open this to verify the page" |

**Checklist:**
- [ ] Hero visible above fold (headline + CTA without scrolling)
- [ ] Brand colors applied (not default purple)
- [ ] Fonts loaded (not system fallback)
- [ ] Images rendering (not broken/placeholder)
- [ ] Mobile layout correct (375px viewport, no horizontal scroll)
- [ ] Islands hydrated (BuyBox shows product data, not empty div)
- [ ] CTA contrast ≥ 4.5:1

If issues → `update_page_section` → re-screenshot.
When satisfied → `publish_page(page_id)` to go live.

## Page Type Templates

**Product Landing (PDP)** — 8-10 sections:
Hero (split) → Gallery → BuyBox → Benefits → Ingredients/Specs → Reviews → Related Products → FAQ → Sticky CTA → Footer

**Campaign Landing** — 10 sections:
Hero → Problem/Pain → Solution → Key Benefits → Social Proof → How It Works → Comparison → Offer/Pricing → FAQ → CTA

**Homepage** — 7-8 sections:
Hero → Featured Products → Brand Story → Categories → Testimonials → Newsletter → Trust Bar → Footer

**Collection** — 6 sections:
Hero Banner → Filter/Sort → Product Grid → Promo Card → Social Proof → Footer

## Quality Bar

- Mobile-first (375px viewport — test this)
- All brand colors via `--lx-*` CSS variables (never hardcoded hex in HTML)
- Proper heading hierarchy (single h1 in hero, h2 per section, h3 for sub-items)
- Islands for ALL commerce interactions (add-to-cart, checkout, cart drawer)
- All images from asset tools (never external URLs unless Shopify CDN)
- No fetch/XHR, eval, localStorage, @import, duplicate IDs
- Hero headline ≤ 8 words, visible without scrolling
- Use shared keyframes (fadeUp, fadeIn, scaleIn) — don't define new @keyframes unless truly unique

## Ad-to-Page Flow

When converting an ad creative to a landing page:
1. `get_ad_creatives` — get creative metadata
2. `analyze_ad_creative` — extract headline, claims, colors, tone, CTA
3. `match_persona_to_ad` — identify target audience
4. Continue with Phase 0-4 using extracted context
5. Ensure "scent continuity" — ad headline ≈ page hero headline
