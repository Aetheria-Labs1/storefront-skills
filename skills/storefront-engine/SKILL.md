---
name: storefront-engine
description: Orchestrator for Lexsis AI storefront page generation. Routes broad or multi-step requests to the right workflow (generate, optimize, remix, experiment, cart, publish), sequences MCP tools, and loads reference knowledge on demand. Prefer a focused workflow skill when one clearly matches.
---

# Storefront Engine — Workflow Orchestration

The routing and orchestration layer for Lexsis AI storefront operations. Use it for broad requests that span several workflows or when no focused skill is a clear match.

## How This Works

1. **Focused skills** handle generate, optimize, remix, experiments, Cart V2, publishing, CRO analysis, and page building. Select one when its scope matches.
2. **Reference files** in `references/` contain deep knowledge — load ONLY what the selected workflow needs, never all at once.
3. **Island schemas** in `references/islands/{name}/schema.json` — full prop types, parts, examples, anti-patterns.
4. For URL analysis, use a browser tool when available (see `browser-analyze`); otherwise use Lexsis server-side design extraction.

All page work follows one contiguous sequence: **Phase 1 Plan → Phase 2 Context → Phase 3 Assets → Phase 4 Build → Phase 5 Ship.**

---

## Phase 1: Page Planning (MANDATORY)

> Do NOT skip this phase. Do NOT proceed to Flow Selection until a plan is approved.
> Skip ONLY if: user is editing an existing page, a CRO_BLUEPRINT is already provided, or user explicitly says "skip planning" / "just build it".

### Step 1 — Assess What's Known

Score the user's input:

| Signal | Check |
|--------|-------|
| Page type (landing, PDP, homepage, collection, editorial, listicle, bundle) | stated? |
| Target audience / persona | described? |
| Products or collection to feature | named? |
| Traffic source (Meta, Google, TikTok, email, organic) | mentioned? |
| Conversion goal (purchase, signup, browse) | clear? |
| Reference URL or ad creative | provided? |
| Tone/style preference | specified? |

- **4+ signals present** → proceed to Step 3 (auto-plan)
- **< 4 signals** → proceed to Step 2 (ask questions)

### Step 2 — Adaptive Discovery

Ask ONLY questions whose answers are missing. Never ask more than 4 at once.

**Tier 1 (always ask if missing):**
1. "What type of page?" (landing / PDP / homepage / collection / editorial)
2. "Who is this for?" (audience: demographics + pain point)
3. "What should visitors do?" (single conversion goal)

**Tier 2 (ask if Tier 1 reveals complexity):**
4. "Where does traffic come from?" (impacts visual density + social proof weight)
5. "Any sections you specifically want?" (hero style, FAQ, comparison table, etc.)
6. "Should this feel bold/energetic or minimal/premium?" (visual approach)
7. "Any animations or scroll effects?" (parallax, reveal-on-scroll, sticky elements)

**Follow-up triggers:**
- Multiple products mentioned → "Which is the hero product? Are others cross-sells or equals?"
- Health/beauty vertical → "Do you have clinical data or certifications to feature?"
- Ad creative provided → "Should the page match the ad's exact style, or just the message?"

### Step 3 — Generate Page Plan

Produce a structured plan covering:

**A. Section Sequence** (ordered list) — for each section: section ID + type, purpose, key content, island requirement, animation.

**B. Visual Rhythm** — spacing pattern, color temperature flow, typography hierarchy.

**C. Inter-Section Communication** — narrative thread, CTA placement strategy, social proof distribution, scroll incentives.

**D. Technical Requirements** — islands needed (exact list), custom animations, asset requirements.

### Step 4 — Present Plan for Approval

```
📋 Page Plan: [Page Type] for [Audience]

Goal: [Conversion goal]
Sections: [N] | Islands: [list] | Style: [visual approach]

Section Layout:
1. [hero-split] — Hook headline + product image + primary CTA
   Animation: fade-up on load
2. [trust-bar] — Star rating + press logos + "X customers served"
   Animation: none (instant credibility)
...

Visual Flow: [spacing + color temperature description]
CTA Strategy: [where + how many]

Proceed with this plan? (Or tell me what to change)
```

Wait for user confirmation. If the user suggests changes, update the plan and re-present.

### Step 5 — Hand Off

Once approved, the plan is the binding blueprint: Phase 2 context gathering targets its requirements, Phase 3 assets follow its imagery needs, Phase 4 HTML follows its section sequence EXACTLY.

---

## Flow Selection

```
What did the user provide?
│
├─ Ad creative (image URLs / screenshot)
│  → AD-TO-PAGE FLOW (analyze creative → extract style → generate matched page)
│
├─ Reference URL (competitor / inspiration)
│  → DESIGN-FIRST FLOW (browser screenshots URL → extract tokens → use as theme → generate)
│
├─ Brand brief only (name, industry, tone)
│  → STANDARD FLOW (Phases 1-5)
│
├─ Existing page (wants edits)
│  → EDIT FLOW (read page → modify sections → validate → write)
│
├─ Product focus (PDP, collection)
│  → PRODUCT FLOW (list_products first → build around real product data)
│
└─ Multiple inputs (ad + products + brand)
   → STANDARD FLOW with enriched context
```

---

## Standard Flow

### Phase 2: Context Gathering ✅ ALL PARALLEL

Fire simultaneously — no dependencies:

```
┌─ get_storefront_skills({ brief, page_type })    → system prompt + island catalog + schema
├─ get_design_md()                                 → brand voice/guidelines
├─ list_products(limit: 10)                        → product catalog (names, images, prices)
├─ search_design_library({ query: "hero" })        → existing brand assets
├─ get_navigation()                                → nav links (check `status` — if not_synced/empty, ask the user)
└─ get_connected_stores()                          → store_id (for publish later)
```

### Phase 3: Asset Preparation ✅ PARALLEL PER SECTION

Full multi-source strategy (library → generate → import → external MCPs): see the `asset-prep` skill or `references/asset-prep.md`.

Decision tree per image:
1. `search_design_library` first — if the brand has relevant assets, USE THEM
2. No match → `generate_asset` (write your own descriptive prompt)
3. Product-on-background → `edit_asset` with product image + background
4. Transparent overlay → `generate_asset` with `transparent: true`
5. User has their own file → `import_asset` with no arguments (opens an upload picker)

Collect all image URLs before Phase 4.

### Phase 4: Build (Agent writes VibePage)

1. Set `theme_css` from brand tokens (map flat columns → CSS vars)
2. Write each section's HTML using Tailwind classes + CSS vars
3. Place island markers where interactive commerce is needed
4. Embed asset URLs directly in `<img src="...">` and `background-image`
5. Add section `css` only for custom keyframes/animations
6. Add section `js` only for scroll-triggered reveals (IntersectionObserver)

Sub-steps when writing HTML (see `references/generation-protocol.md`): **4a — raw HTML + Tailwind** (structure and copy first), then **4b — island mapping** (swap interactive placeholders for `data-island` markers with schema-valid `data-props`).

### Phase 5: Validate + Ship ❌ SEQUENTIAL

```
validate_vibe_page({ page })                → { valid, errors, warnings }; fix and re-validate
publish_vibe_page({ slug, page, publish: false })  → draft + preview URL
```

Report the preview URL. Call `publish_page` ONLY after the user explicitly says to go live.

---

## Ad-to-Page Flow

```
Phase 2: analyze_ad_creative({ image_urls }) + get_storefront_skills + list_products
Phase 3: use ad creative images directly; generate_asset / edit_asset for the rest
Phase 4-5: Standard Flow
```

## Design-First Flow (Reference URL)

```
Phase 2: browser screenshots URL → extracted palette/fonts/spacing + get_storefront_skills + list_products
Phase 3-5: Standard Flow, with extracted tokens as the theme_css base
```

## Edit Flow (Safe Iteration)

```
1. find_page({ query })                                   → locate page
2. get_page_content({ page_id })                          → read sections + head
3. preview_section_update({ page_id, section_id, html })  → dry-run (repeat per section)
4. update_page_section({ page_id, section_id, html })     → commit (bumps version)
5. check_page_integrity({ page_id, archetype })           → structural QA
6. [Optional] diff_page_versions / rollback_page_version
```

**Key rules:** always preview before update; run integrity after all edits; rollback creates a forward version, preserving history.

---

## Reference Files

Load with `Read references/{name}.md` when you need specific knowledge. Do NOT load all at once.

### Knowledge (domain expertise)
- **generation-protocol.md** — Page generation rules, constraints, quality gates, Phase 4a/4b detail
- **cro-research.md** — Conversion rate optimization research and data (2026)
- **storefront-craft.md** — Load FIRST on any page generation task. Core craft principles.
- **workflow-orchestration.md** — Tool sequences, parallelization, flow selection
- **conversion-psychology.md** — AIDA framework → section order mapping
- **visual-craft.md** — Premium visual techniques. Load when polishing quality.
- **island-patterns.md** — How to embed, wrap, and combine React islands
- **premium-patterns.md** — Copy-and-adapt HTML+Tailwind patterns for high-converting sections
- **animation-system.md** — CSS-only + IntersectionObserver animations. No framer-motion.
- **design-enrichment.md** — generate_asset, edit_asset, view_asset prompt patterns
- **asset-prep.md** — Multi-source asset strategy (library, generation, import, external MCPs)
- **qa-recipe.md** — Validation, integrity checks, screenshot QA workflow
- **reference-pdp-remix.md** — PDP reference site patterns and adaptation

### Verticals
vertical-beauty, vertical-supplements, vertical-fashion, vertical-food, vertical-home, vertical-luxury

### Traffic Sources
traffic-source-meta, traffic-source-google, traffic-source-tiktok

### Island Reference
- **islands/_contract.md** — Rules ALL island wrappers must follow
- **islands/{name}/schema.json** — Full props, variants, examples, anti-patterns (one per island)
- **islands/{name}/layouts/*.json** — Pre-built renderer-compatible section templates

### Operational (workflow procedures)
page-generation, design-assets, publishing, page-editing, analytics, generate-pdp, generate-landing-page, generate-homepage, generate-collection, generate-listicle, generate-bundle-page, generate-editorial, ad-to-page, page-redesign, competitor-remix, personalization-variant, ab-test-variant, section-library, cart-composition, cart-v2-management
