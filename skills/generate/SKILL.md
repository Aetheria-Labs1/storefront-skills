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

When invoked by `visual-page`, use its approved plan, final asset manifest, and
layout brief as the binding inputs. Recreate the approved composition with
source-format HTML and valid islands; never embed the visual layout reference as
page media.

# Storefront Page Generation

Generate high-quality Shopify storefront pages using the Lexsis AI MCP tools.

> **Prerequisites**: Read `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`, and `vibe://skills/source-format` first — they define the source authoring format, CSS variable system, island integration, and visual verification step.

## Generation Flow (Two-Phase)

### Phase 2 — Context Gathering (run ALL in parallel)

```
lexsis_workspace → get       → workspace context
lexsis_workspace → stores    → store ID and domain
lexsis_brand → brand_kit     → logo, fonts, colors, voice, border radius
lexsis_brand → list_themes   → available themes
lexsis_brand → get_theme     → complete selected theme + theme_css
lexsis_design → guide        → design philosophy + don'ts
lexsis_catalog → list        → product catalog
lexsis_asset_library → search → existing brand assets
```

Run independent reads in parallel. If more than one workspace or store is
available, select explicitly. If no valid theme exists in the selected
workspace, stop and report the configuration error—never borrow another
workspace's theme.

### Phase 3 — Asset Preparation

Decision tree per section:
1. `lexsis_asset_library` action `search` — check existing assets first
2. `lexsis_drafts` action `asset_generate` — only if no suitable match exists
3. Add `reference_images` to edit or composite
4. `lexsis_assets` action `view` — verify before page use

Budget: 3-5 generated assets per page max. Existing assets = free.

### Phase 4a — Draft Source HTML

Author the page in **source format** (see `vibe://skills/source-format`) — plain HTML, never JSON-escaped:
- Sections delimited by `<!-- section: id -->` comments
- Islands as `<lx-island name="BuyBox"><script type="application/json">{...props}</script></lx-island>` — use `vibe://schema/island/{name}` for exact prop shapes
- Section CSS in a `<style>` block, section JS in a `<script>` block per section
- Use `theme_css` returned by `lexsis_brand` action `get_theme`, or generate it
  with action `compile_theme` when intentionally authoring a new palette
- Focus on visual design: layout, typography, color, spacing, imagery; animations via `data-behavior="gsap-*"` presets or shared keyframes
- Write real copy naturally (apostrophes/quotes are fine — never escape anything; never Lorem Ipsum)
- Use asset URLs from Phase 3 in `<img>` tags

### Phase 4b — Compile & Fix

```
lexsis_pages({
  action: "compile",
  args: { source, head, theme_css, scripts }
}) → compiled page + issues + compiled_page_css
```

Fix reported issues and recompile. `missing_candidates` must be empty: Tailwind
is compiled once into `compiled_page_css`; do not add a runtime Tailwind CDN or
separate page stylesheet.

### Phase 5 — Publish + Visual Verify

```
lexsis_page_create({
  action: "create",
  args: {
    source, head, theme_css, scripts, slug, archetype,
    workspace_id, store_id, theme_id,
    inherit_header: true, inherit_footer: true,
    publish: false
  }
}) → preview_url
```

**Visual verification is REQUIRED before marking complete:**

Use the host agent's own browser capability. The Lexsis MCP does not create or
pool Playwright sessions. Verify 390px, 768px, and 1280px; use screenshots when
available and computed styles/DOM geometry when they are not.

**Checklist:**
- [ ] Hero visible above fold (headline + CTA without scrolling)
- [ ] Brand colors applied (not default purple)
- [ ] Fonts loaded (not system fallback)
- [ ] Images rendering (not broken/placeholder)
- [ ] Layout correct at 390px, 768px, and 1280px with no horizontal scroll
- [ ] Islands hydrated (BuyBox shows product data, not empty div)
- [ ] CTA contrast ≥ 4.5:1

If issues, use `lexsis_drafts` action `page_update_section` or `page_patch`,
then repeat QA. Return the draft preview. Call `lexsis_live_ops` action
`publish` only after explicit approval.

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

- Mobile-first (test 390px, 768px, and 1280px)
- All brand colors via `--lx-*` CSS variables (never hardcoded hex in HTML)
- Proper heading hierarchy (single h1 in hero, h2 per section, h3 for sub-items)
- Islands for ALL commerce interactions (add-to-cart, checkout, cart drawer)
- All images from asset tools (never external URLs unless Shopify CDN)
- No fetch/XHR, eval, localStorage, @import, duplicate IDs
- Hero headline ≤ 8 words, visible without scrolling
- Use shared keyframes (fadeUp, fadeIn, scaleIn) — don't define new @keyframes unless truly unique

## Scope Boundary

Do not analyze ads, screenshots, competitor URLs, or reference pages here.
`browser-analyze`, `analyze-page`, and `remix` create the safe source brief;
`visual-page` owns the resulting layout concept and approval.

## Optional Follow-Up

This skill can end after source compilation, draft creation, and visual QA
produce `DRAFT_READY`. `publish` is available only when the user explicitly
asks to make that draft live.
