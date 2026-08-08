---
name: generate
description: Generate a complete Shopify storefront page — auto-detects page type (landing, PDP, collection, homepage, editorial, listicle, bundle) and applies conversion-optimized patterns
---

# Generate Storefront Page

Generate a complete Shopify storefront page — auto-detects page type (landing, PDP, collection, homepage, editorial, listicle, bundle) and applies conversion-optimized patterns

## Context

- **storefront-craft**: Load this skill first on any storefront page generation task.
- **workflow-orchestration**: Load after `craft-guide`. Defines optimal tool sequences, parallelization rules, and flow selection.
- **conversion-psychology**: > When to load: ALWAYS. Read before generating any ecommerce page.
- **island-patterns**: How to properly embed, wrap, and combine React islands in vibe-code HTML sections. Load when using commerce or engagement islands.

## Workflow

> **STOP — Planning Required First**
> Before running any generation phase, execute the Page Planning workflow (Phase 1 from storefront-engine).
> Assess what the user has told you, ask clarifying questions if < 4 signals are present, generate a section plan, and get user approval.
> Do NOT proceed to Phase 2 until a page plan is confirmed by the user.
> Exception: If user explicitly says "skip planning" or "just build it".

# Storefront Page Generation

Generate high-quality Shopify storefront pages using the Lexsis AI MCP tools.

> **Prerequisites**: Read `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`, and `vibe://skills/source-format` first — they define the source authoring format, CSS variable system, island integration, and visual verification step.

## Generation Flow (Two-Phase)

### Phase 2 — Context Gathering (run ALL in parallel)

```
get_workspace_details    → workspace ID
get_connected_stores     → store domain
get_brand_kit            → logo, fonts, colors, voice, border radius
get_design_md            → brand brief + design philosophy + don'ts
list_products            → product catalog (for commerce islands)
get_navigation           → navbar/footer links
search_design_library    → existing brand assets (hero images, lifestyle shots)
```

All 7 calls can run in parallel. Wait for all before proceeding.

### Phase 3 — Asset Preparation

Decision tree per section:
1. `search_design_library` — check existing assets FIRST (always)
2. `generate_asset` — only if library has nothing suitable
3. `edit_asset` — composite/modify if needed
4. `view_asset` — verify result before using in page

Budget: 3-5 generated assets per page max. Existing assets = free.

### Phase 4a — Draft Source HTML

Author the page in **source format** (see `vibe://skills/source-format`) — plain HTML, never JSON-escaped:
- Sections delimited by `<!-- section: id -->` comments
- Islands as `<lx-island name="BuyBox"><script type="application/json">{...props}</script></lx-island>` — use `vibe://schema/island/{name}` for exact prop shapes
- Section CSS in a `<style>` block, section JS in a `<script>` block per section
- Generate `theme_css` with `compile_theme` (WCAG-checked, from brand kit colors)
- Focus on visual design: layout, typography, color, spacing, imagery; animations via `data-behavior="gsap-*"` presets or shared keyframes
- Write real copy naturally (apostrophes/quotes are fine — never escape anything; never Lorem Ipsum)
- Use asset URLs from Phase 3 in `<img>` tags

### Phase 4b — Compile & Fix

```
compile_page_source(source, head, theme_css, scripts)   → compiled page + issues
```

Fix reported issues in the source and re-compile. Common issues: duplicate section IDs, invalid island names, malformed props JSON, missing headless hooks, external scripts in section HTML.

### Phase 5 — Publish + Visual Verify

```
create_page_from_source(source, head, theme_css, scripts, slug, archetype, publish=false)  → preview_url
```

**Visual verification is REQUIRED before marking complete:**

| Environment | How to Verify |
|-------------|--------------|
| Codex Browser | Open `preview_url`, capture desktop and mobile screenshots, then review them |
| No Browser | Provide `preview_url` and state that visual verification remains manual |

**Checklist:**
- [ ] Hero visible above fold (headline + CTA without scrolling)
- [ ] Brand colors applied (not default purple)
- [ ] Fonts loaded (not system fallback)
- [ ] Images rendering (not broken/placeholder)
- [ ] Mobile layout correct (375px viewport, no horizontal scroll)
- [ ] Islands hydrated (BuyBox shows product data, not empty div)
- [ ] CTA contrast ≥ 4.5:1

If issues → `update_section_from_source` (one section per call) → re-screenshot.
When satisfied, return the draft preview. Call `publish_page(page_id)` only after the user explicitly approves a live publish.

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
4. Continue with Phases 1-5 using extracted context
5. Ensure "scent continuity" — ad headline ≈ page hero headline
