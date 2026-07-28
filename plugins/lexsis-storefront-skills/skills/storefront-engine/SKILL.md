---
name: storefront-engine
description: Core orchestrator for Lexsis AI storefront page generation. Routes requests to the correct workflow, manages tool sequencing, and loads reference knowledge on demand. Auto-invoked by commands and agents.
allowed-tools: mcp__lexsis-ai__*
---

# Storefront Engine — Core Orchestrator

This is the routing and orchestration layer for all Lexsis AI storefront operations. It determines the correct workflow based on user input and coordinates tool calls in the optimal sequence.

## How This Works

1. **Commands** (generate, optimize, remix, experiment, cart, publish, analyze-page, extract-island, search-docs) invoke this skill automatically
2. **Agents** (cro-analyzer, page-builder) have their own orchestration logic
3. **Reference files** in `reference/` contain deep knowledge — load ONLY what you need
4. **Island schemas** in `reference/islands/{name}/schema.json` — full prop types, parts, examples, anti-patterns

---

# Workflow Orchestration — Execution Engine

Load after `craft-guide`. Defines optimal tool sequences, parallelization rules, and flow selection.

---

## Phase -1: Page Planning (MANDATORY)

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

**A. Section Sequence** (ordered list)
For each section:
- Section ID + type (e.g. `hero-split`, `social-proof-bar`, `features-grid`)
- Purpose (what it communicates / why it's here in this position)
- Key content (headline direction, imagery type, specific products)
- Island requirement (if interactive: BuyBox, FAQ, ReviewCarousel, etc.)
- Animation (fade-up, parallax, sticky, reveal, none)

**B. Visual Rhythm**
- Spacing pattern (tight-loose-tight, progressive relaxation, etc.)
- Color temperature flow (hero warm → middle neutral → CTA warm)
- Typography hierarchy (display → heading → body sizes)

**C. Inter-Section Communication**
- Narrative thread (how sections connect logically)
- CTA placement strategy (where and how many)
- Social proof distribution (where trust signals appear and why)
- Scroll incentives (what makes user keep scrolling)

**D. Technical Requirements**
- Islands needed (exact list)
- Custom animations (scroll-triggered reveals, parallax, sticky)
- Asset requirements (hero image, lifestyle shots, textures, icons)

### Step 4 — Present Plan for Approval

Show the plan to the user in this format:

```
📋 Page Plan: [Page Type] for [Audience]

Goal: [Conversion goal]
Sections: [N] | Islands: [list] | Style: [visual approach]

Section Layout:
1. [hero-split] — Hook headline + product image + primary CTA
   Animation: fade-up on load
2. [trust-bar] — Star rating + press logos + "X customers served"
   Animation: none (instant credibility)
3. [problem-solution] — Pain → product as answer (emotional)
   Animation: reveal on scroll
...

Visual Flow: [spacing + color temperature description]
CTA Strategy: [where + how many]

Proceed with this plan? (Or tell me what to change)
```

Wait for user confirmation. If user suggests changes, update plan and re-present.

### Step 5 — Hand Off to Generation

Once approved, the plan becomes the binding blueprint for all subsequent phases:
- Phase 0 context gathering targets the plan's requirements
- Phase 1 asset generation follows the plan's imagery needs
- Phase 2 HTML generation follows the plan's section sequence EXACTLY
- Section purposes from the plan guide the copywriting
- Animation choices from the plan guide the JS/CSS

---

## Flow Selection & Execution

Determine which flow to run based on user input, then execute it.

See `reference/workflow-orchestration.md` for:
- Flow Selection tree (ad creative → Ad-to-Page, reference URL → Design-First, brand brief → Standard, existing page → Edit, product focus → Product)
- Standard Flow (Phase 0-4)
- Ad-to-Page, Design-First, Edit, and Duplication flows
- Parallelization rules
- Cost control and credit costs

See `reference/generation-protocol.md` for:
- VibePage JSON schema
- Two-phase HTML generation (Phase A: raw HTML, Phase B: island mapping)
- Visual verification protocol
- Island integration reference

---

## Reference Files

Load these with `Read reference/{name}.md` when you need specific knowledge. Do NOT load all at once.

### Knowledge (domain expertise)
- **generation-protocol.md** — Page generation rules, constraints, and quality gates
- **cro-research.md** — Conversion rate optimization research and data (2026)
- **storefront-craft.md** — Load FIRST on any page generation task. Core craft principles.
- **workflow-orchestration.md** — Tool sequences, parallelization, flow selection
- **conversion-psychology.md** — AIDA framework → section order mapping
- **visual-craft.md** — Premium visual techniques. Load when polishing quality.
- **island-patterns.md** — How to embed, wrap, and combine React islands in vibe-code HTML
- **premium-patterns.md** — Copy-and-adapt HTML+Tailwind patterns for high-converting sections
- **animation-system.md** — CSS-only + IntersectionObserver animations. No framer-motion.
- **design-enrichment.md** — Using generate_asset, edit_asset, view_asset for custom imagery
- **qa-recipe.md** — Validation, integrity checks, screenshot QA workflow
- **reference-pdp-remix.md** — PDP reference site patterns and adaptation techniques

### Verticals (industry-specific knowledge)
- **vertical-beauty.md** — Beauty/skincare patterns, ingredient displays, routine builders
- **vertical-supplements.md** — Supplements: clinical data, dosage, subscription-first
- **vertical-fashion.md** — Fashion: size guides, lookbooks, "Add to Bag" conventions
- **vertical-food.md** — Food/beverage DTC: flavor profiles, subscription boxes
- **vertical-home.md** — Home goods: room scenes, measurement guides, material specs
- **vertical-luxury.md** — Luxury: editorial restraint, heritage storytelling, exclusivity

### Traffic Sources
- **traffic-source-meta.md** — Meta/Facebook/Instagram ad optimization patterns
- **traffic-source-google.md** — Google Search/Shopping ad optimization
- **traffic-source-tiktok.md** — TikTok ad creative adaptation

### Island Reference
- **islands/_contract.md** — Rules ALL island wrappers must follow (spacing, colors, responsive, data-parts)
- **islands/{name}/schema.json** — Full props, types, variants, examples, parts, anti-patterns (47 islands)
- **islands/{name}/index.md** — Composition rules, file index, quick reference
- **islands/{name}/layouts/*.json** — Pre-built section templates (renderer-compatible)

### Operational (workflow procedures)
- **page-generation.md** — Generate pages using MCP tools
- **design-assets.md** — Manage visual assets and brand identity
- **publishing.md** — Page publishing, previews, lifecycle
- **page-editing.md** — Edit existing pages via section-level operations
- **analytics.md** — Page performance data and A/B experiments
- **generate-pdp.md** — Product detail pages (BuyBox required, sticky CTA +12% CVR)
- **generate-landing-page.md** — Post-click landing pages (zero nav, +30% CVR)
- **generate-homepage.md** — Brand homepages (nav, collections, story)
- **generate-collection.md** — Product grids with EditorialProductGrid + QuickAdd
- **generate-listicle.md** — SEO long-form comparison pages (>2000 words)
- **generate-bundle-page.md** — Bundle builders with BundleBuilder island
- **generate-editorial.md** — Magazine-style shoppable editorial content
- **ad-to-page.md** — Ad creative → message-matched landing page
- **page-redesign.md** — Refresh existing pages preserving what works
- **competitor-remix.md** — Rebuild competitor page with your brand
- **personalization-variant.md** — Per-persona page variants
- **ab-test-variant.md** — Hypothesis-driven A/B test setup
- **section-library.md** — Insert section patterns into existing pages
- **cart-composition.md** — Cart V2 drawer composition (DrawerShell + atomic islands)
- **cart-v2-management.md** — Read/modify/validate cart configuration via MCP
