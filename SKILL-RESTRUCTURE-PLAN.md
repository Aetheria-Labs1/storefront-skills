# Storefront Skills Restructure Plan

> Audit date: 2026-07-28
> Goal: Eliminate redundancy, create distinct non-overlapping workflows publishable as lead magnets, add external MCP integration guidance.

---

## Problem Statement

1. **Context bloat**: The same 5-phase generation workflow is copy-pasted across 8+ files (~5,000-7,000 duplicate lines). This inflates the AI agent's context window and causes confused/inconsistent behavior.
2. **No external MCP guidance**: Zero mentions of Exa, OpenArt, HiggsField, Replicate, or any external image/video generation MCPs. The only asset workflow documented is the built-in `generate_asset`/`edit_asset`/`view_asset`.
3. **Skills don't tell distinct stories**: `/generate`, `workflow-orchestration`, `page-builder` agent, and `storefront-engine` SKILL.md all say roughly the same thing. A user installing the plugin gets the same instructions loaded 3-4x.
4. **Page-type docs are 60% boilerplate**: Each `generate-*.md` repeats Phase 0-4, quality bar, and visual verification — only the CRO section ordering is unique.

---



## Phase 1: Delete Pure Duplicates (30 min)

**No content decisions needed — these are exact copies.**

### 1.1 Delete `cursor/rules/reference/` (26 files)

These are byte-for-byte copies of root `reference/` files. Cursor should reference root directly.

Files to delete:

```
cursor/rules/reference/ab-test-variant.md
cursor/rules/reference/ad-to-page.md
cursor/rules/reference/analytics.md
cursor/rules/reference/cart-composition.md
cursor/rules/reference/cart-v2-management.md
cursor/rules/reference/competitor-remix.md
cursor/rules/reference/conversion-psychology.md
cursor/rules/reference/cro-research.md
cursor/rules/reference/design-assets.md
cursor/rules/reference/generate-bundle-page.md
cursor/rules/reference/generate-collection.md
cursor/rules/reference/generate-editorial.md
cursor/rules/reference/generate-homepage.md
cursor/rules/reference/generate-landing-page.md
cursor/rules/reference/generate-listicle.md
cursor/rules/reference/generate-pdp.md
cursor/rules/reference/generation-protocol.md
cursor/rules/reference/page-editing.md
cursor/rules/reference/page-generation.md
cursor/rules/reference/page-redesign.md
cursor/rules/reference/personalization-variant.md
cursor/rules/reference/publishing.md
cursor/rules/reference/qa-recipe.md
cursor/rules/reference/section-library.md
cursor/rules/reference/storefront-craft.md
cursor/rules/reference/visual-craft.md
```

Update `cursor/rules/lexsis-storefront.mdc` to point at `../reference/` instead.

### 1.2 Delete duplicate island reference in plugin

```
plugins/lexsis-storefront-skills/skills/storefront-engine/reference/blob-shapes.md
```

(duplicate of `reference/blob-shapes.md`)

### 1.3 Verify codex duplicates

Check if `codex/skills/storefront-engine/reference/` duplicates root. If yes, delete and symlink or reference.

---



## Phase 2: Slim Plugin Commands to Thin Wrappers (1 hour)

**Principle:** Each `commands/*.md` file should be <30 lines. It states what the command does, what skill it invokes, and any command-specific notes. All workflow content lives in `reference/` (single source of truth).

### Files to slim:


| File                                 | Current                            | Target                                                                 |
| ------------------------------------ | ---------------------------------- | ---------------------------------------------------------------------- |
| `plugins/.../commands/generate.md`   | 148 lines (full workflow)          | ~25 lines (triggers storefront-engine, references generation-protocol) |
| `plugins/.../commands/plan-page.md`  | ~130 lines                         | ~20 lines (references plan-page.md)                                    |
| `plugins/.../commands/optimize.md`   | 218 lines (full redesign workflow) | ~25 lines (references page-redesign.md + page-editing.md)              |
| `plugins/.../commands/remix.md`      | TBD                                | ~20 lines                                                              |
| `plugins/.../commands/experiment.md` | TBD                                | ~20 lines                                                              |




### Template for slim command:

```markdown
---
description: [One line]
allowed-tools: mcp__lexsis-ai__*
---

# /[command]

[One-sentence description]

## What This Does

Invokes the **storefront-engine** skill with [specific context]. 

## Workflow Reference

See `reference/[canonical-doc].md` for the full execution protocol.

## Command-Specific Notes

- [Anything unique to this command vs the generic workflow]
```



### Same treatment for `mcp-skills/_operational/*.md`:


| File                             | Status                                                                |
| -------------------------------- | --------------------------------------------------------------------- |
| `_operational/generate.md`       | 95% identical to `commands/generate.md` — merge or delete one         |
| `_operational/plan-page.md`      | 98% identical to `reference/plan-page.md` — replace with thin wrapper |
| `_operational/optimize.md`       | Mix of page-editing + page-redesign — slim to references              |
| `_operational/analyze-page.md`   | Unique (Playwright workflow) — KEEP as-is                             |
| `_operational/publish.md`        | Likely thin already — verify                                          |
| `_operational/remix.md`          | Check overlap with `reference/competitor-remix.md`                    |
| `_operational/cart.md`           | Likely unique — verify                                                |
| `_operational/experiment.md`     | Check overlap with `reference/ab-test-variant.md`                     |
| `_operational/extract-island.md` | Likely unique — verify                                                |
| `_operational/search-docs.md`    | Likely unique — verify                                                |


---



## Phase 3: Consolidate Reference Docs — Single Source of Truth (2 hours)



### 3.1 Designate canonical docs


| Concept                        | Canonical File                        | Contains                                                                                      |
| ------------------------------ | ------------------------------------- | --------------------------------------------------------------------------------------------- |
| Architecture + quality bar     | `reference/storefront-craft.md`       | VibePage schema, CSS vars, quality bar, anti-patterns, island rules, Tailwind usage           |
| Full generation workflow       | `reference/generation-protocol.md`    | Phase 0-4 execution, VibePage JSON, visual verification, island integration, deprecated tools |
| Flow routing + parallelization | `reference/workflow-orchestration.md` | Flow selection tree, standard/ad-to-page/design-first/edit/duplication flows, cost control    |
| Page planning                  | `reference/plan-page.md`              | Section templates by page type, animation vocab, visual rhythm, narrative structures          |
| Asset generation               | `reference/design-enrichment.md`      | generate_asset/edit_asset/view_asset pipeline, style guide, compositing, cost control         |
| Quick asset reference          | `reference/design-assets.md`          | Condensed version of design-enrichment (brand kit, theme management)                          |




### 3.2 Strip workflow from page-type docs

Each `generate-*.md` keeps ONLY:

1. Triggers (when to use this page type)
2. CRO-backed section ordering (the unique value)
3. Niche variants (beauty PDP vs supplement PDP etc.)
4. Traffic source calibration (if applicable)
5. Conversion data table

**Remove from each:**

- Phase 0 context gathering (→ reference `generation-protocol.md`)
- Phase 2A/2B HTML generation instructions
- Phase 3 validation
- Phase 4 visual verification checklist
- Quality bar
- Ad-to-page flow snippet

Files affected:

```
reference/generate-landing-page.md
reference/generate-pdp.md
reference/generate-editorial.md
reference/generate-listicle.md
reference/generate-bundle-page.md
reference/generate-collection.md
reference/generate-homepage.md (if exists)
```



### 3.3 Remove from `reference/page-generation.md`

This file is now 100% redundant with `generation-protocol.md`. Either:

- Delete it entirely, OR
- Convert to a 10-line pointer: "See generation-protocol.md"



### 3.4 Slim `page-builder.md` agent

The agent currently embeds the full workflow (280 lines). After Phase 3:

- Remove VibePage schema (→ `storefront-craft.md`)
- Remove CSS variables table (→ `storefront-craft.md`)  
- Remove page type section sequences (→ `plan-page.md`)
- Remove quality bar + anti-patterns (→ `storefront-craft.md`)
- Remove Playwright verification details (→ `generation-protocol.md`)
- Keep: blueprint ingestion, flow selection table, cost control, draft-first rule

Target: ~80 lines (from 280).

### 3.5 Slim `storefront-engine/SKILL.md`

Currently 263+ lines embedding full workflow-orchestration. After Phase 3:

- Keep: routing logic (how commands → workflows), reference loading instructions
- Remove: Phase -1 planning (→ `plan-page.md`), Phase 0-4 (→ `generation-protocol.md`)

Target: ~60 lines.

---



## Phase 4: Create Distinct Workflow Packs (2 hours)

**The lead magnet structure.** Each workflow is a self-contained sequence that feeds into the next. No overlap.

### Workflow 1: `/plan-page` — Discovery & Blueprint

**File:** `reference/plan-page.md` (already mostly correct)
**Story:** "From vague idea to approved plan in 60 seconds"
**Unique to this workflow:**

- 7-signal assessment
- Adaptive questioning (max 4 questions)
- Section sequence with purpose + island + animation
- Visual rhythm patterns
- Narrative structures (AIDA, Problem→Solution→Proof→Action)
- CTA placement strategy
- Template search (`search_section_templates`)

**Inputs:** User brief (text, URL, ad creative, or combination)
**Outputs:** Approved page plan (section sequence + asset requirements + islands needed)
**Does NOT contain:** Asset generation, HTML generation, validation, publishing, CRO audit

---



### Workflow 2: `/asset-prep` — Visual Asset Pipeline (NEW)

**File:** `reference/asset-pipeline.md` (TO CREATE)
**Story:** "Multi-source asset strategy — built-in tools + external MCPs"
**Unique to this workflow:**

- Decision tree: when to use each source
- Built-in: `search_design_library` → `generate_asset` → `edit_asset` → `view_asset`
- External MCPs: Exa (reference research), OpenArt/Replicate/XFILD (video), import_asset
- Asset manifest output format
- Per-section asset requirements (from plan)
- Cost control and budgeting

**Inputs:** Approved page plan (from Workflow 1)
**Outputs:** Asset manifest (URLs + purposes + section mapping)
**Does NOT contain:** Planning, HTML generation, publishing, CRO

**External MCP integration table:**


| Need                  | Built-in                                | External MCP               | Notes                                               |
| --------------------- | --------------------------------------- | -------------------------- | --------------------------------------------------- |
| Lifestyle photography | `generate_asset(style: "photography")`  | —                          | Best for hero backgrounds, section bgs              |
| Product composite     | `edit_asset(mode: "composite")`         | —                          | Product on generated/library background             |
| Product shots         | `list_products` (real images)           | —                          | NEVER generate fake product images                  |
| Video hero            | —                                       | XFILD / Runway / Kling MCP | For TikTok traffic, fashion, luxury                 |
| Video frames from ad  | `extract_video_frames`                  | —                          | Pull stills from existing creative                  |
| Reference imagery     | —                                       | Exa (`web_search_exa`)     | Mood board, competitor screenshots                  |
| Stock photography     | —                                       | Unsplash/Pexels MCP        | When brand has no assets and generation isn't right |
| AI illustration       | `generate_asset(style: "illustration")` | OpenArt MCP (more control) | Brand illustrations, icons, patterns                |
| Texture/patterns      | `generate_asset(style: "texture")`      | —                          | Section backgrounds, overlays                       |
| Transparent overlays  | `generate_asset(transparent: true)`     | —                          | Decorative elements                                 |


**Feeding external assets into pages:**

```
1. Find/generate asset via external MCP → get URL
2. import_asset({ url, purpose, tags }) → stores in Lexsis design library
3. Use returned asset_id/URL in page HTML (same as built-in assets)
```

---



### Workflow 3: `/generate` — HTML Generation Engine

**File:** `reference/generation-protocol.md` (refactored)
**Story:** "Plan + assets in, published draft out"
**Unique to this workflow:**

- Two-phase HTML generation (2A: raw HTML + Tailwind, 2B: island mapping)
- VibePage JSON schema
- CSS variable system
- Section JS sandboxing rules
- `validate_vibe_page` error fixing
- `publish_vibe_page(draft: true)` → preview URL
- Visual verification (Playwright / manual)

**Inputs:** Page plan + asset manifest
**Outputs:** Published draft with preview URL
**Does NOT contain:** Planning, asset generation, CRO analysis, page-type-specific CRO ordering

---



### Workflow 4: `/audit-cro` — Conversion Rate Audit

**File:** `mcp-skills/agents/cro-analyzer.md` (already well-structured)
**Story:** "12-point scoring with data-backed benchmarks"
**Unique to this workflow:**

- Full page capture (Playwright desktop + mobile)
- 12-dimension scoring (0-10 each)
- Priority ranking (critical/high/medium/low)
- Conversion benchmark data
- `CRO_BLUEPRINT` JSON output
- Hero pattern identification (5 types)
- Section ordering rules

**Inputs:** Page URL (existing page)
**Outputs:** `CRO_BLUEPRINT` JSON
**Does NOT contain:** Page generation, asset creation, publishing, section editing

---



### Workflow 5: `/optimize` — Apply CRO Fixes

**File:** `reference/page-redesign.md` + `reference/page-editing.md` (merge into one)
**Story:** "Data-informed section-by-section improvement"
**Unique to this workflow:**

- Ingest CRO_BLUEPRINT or manual instructions
- Analytics-informed decisions (KEEP / REDESIGN / REPLACE / REMOVE)
- Section-level edit operations (`update_page_section`, `move_page_section`, `remove_page_section`)
- `preview_section_update` (dry-run before commit)
- `diff_page_versions` (before/after comparison)
- `rollback_page_version` (safety net)
- Version preservation

**Inputs:** Existing page + CRO_BLUEPRINT (from Workflow 4) or edit instructions
**Outputs:** Updated page (published after user approval)
**Does NOT contain:** New page generation, planning from scratch, asset generation

---



### Page-Type Reference Docs (NOT workflows — loaded on demand)

After restructuring, each `generate-*.md` becomes a pure **CRO reference card**:


| Doc                        | Unique content (KEEP)                                                                                                                                               | Remove                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `generate-landing-page.md` | Zero-nav rule, CRO section ordering (cold traffic), traffic source calibration (Meta/Google/TikTok), urgency tactics, hero patterns by niche, conversion data table | Phase 0-4, quality bar, visual verification, tool calls |
| `generate-pdp.md`          | PDP section ordering, required islands, niche variants (beauty/supplement/fashion PDP), conversion data                                                             | Same                                                    |
| `generate-editorial.md`    | Magazine patterns, shoppable moment placement, award-winning references (Serotoninn, Lemaire, Vero), editorial CRO evidence                                         | Same                                                    |
| `generate-listicle.md`     | Numbered item structure, comparison tables, verdict CTA, SEO structure                                                                                              | Same                                                    |
| `generate-bundle-page.md`  | Bundle builder island usage, savings calculator, included-items layout                                                                                              | Same                                                    |
| `generate-collection.md`   | Product grid patterns, filter bar, mid-grid promos, collection-specific islands                                                                                     | Same                                                    |
| `generate-homepage.md`     | Multi-CTA strategy, collections grid, brand story, multi-audience homepage                                                                                          | Same                                                    |


These get loaded by the generation workflow when it needs page-type-specific guidance (via the plan's `page_type` field). They never execute tool calls themselves.

---



## Phase 5: Add External MCP Docs (1 hour)



### 5.1 Create `reference/external-mcps.md`

Full guide for using external MCPs alongside built-in Lexsis tools. Content outlined in Workflow 2 above.

### 5.2 Create `reference/video-assets.md`

Specific guidance for video generation/extraction:

- When video heroes convert better (TikTok traffic, fashion, luxury)
- `extract_video_frames` from existing ad creatives
- External video MCPs (XFILD, Runway, Kling)
- Video placement patterns (click-to-play ONLY, never autoplay)
- Thumbnail generation for video heroes
- Integration: video URL → page HTML (`<video>` tag or HeroMedia island)



### 5.3 Update `reference/design-enrichment.md`

Add section: "When Built-In Isn't Enough" with pointer to `external-mcps.md`.

### 5.4 Update `storefront-craft.md` Image Strategy section

Add bullet: "For video assets, reference imagery, or specialized generation → see `external-mcps.md`"

---



## Phase 6: Update Plugin Packaging (30 min)



### 6.1 Update `plugin.json` version

Bump to 4.0.0 (breaking: restructured skills, removed duplicates).

### 6.2 Update [README.md](http://README.md)

- Add workflow sequence diagram
- Update "How It Works" to show the 5-workflow pipeline
- Add "External MCPs" section listing compatible third-party tools



### 6.3 Update `.mcp.json` if needed

Ensure MCP server config reflects any new tools or resources.

---



## Execution Order & Dependencies

```
Phase 1 (delete dupes)
  ↓ no dependencies
Phase 2 (slim commands)
  ↓ needs Phase 1 done (cursor refs fixed)
Phase 3 (consolidate reference)
  ↓ needs Phase 2 done (commands point at reference)
Phase 4 (distinct workflows)
  ↓ needs Phase 3 done (canonical docs established)
Phase 5 (external MCPs)
  ↓ can run in parallel with Phase 4
Phase 6 (packaging)
  ↓ needs Phase 4 + 5 done
```

---



## Success Criteria

- [ ] No file contains the Phase 0 tool list more than once (canonical: `generation-protocol.md`)
- [ ] No file contains the visual verification checklist more than once (canonical: `generation-protocol.md`)
- [ ] No file contains the quality bar more than once (canonical: `storefront-craft.md`)
- [ ] No file contains page type section templates more than once (canonical: `plan-page.md`)
- [ ] Each of the 5 workflows has ZERO overlap with the others
- [ ] External MCP integration is documented with decision tree
- [ ] `cursor/rules/reference/` directory no longer exists
- [ ] Each command/skill file is <30 lines (thin wrapper)
- [ ] Page-type docs contain only CRO reference (no workflow instructions)
- [ ] Total line count reduced by ~40-50%

---



## Token Impact Estimate


| State            | Approx tokens loaded per generation task                       |
| ---------------- | -------------------------------------------------------------- |
| Before (current) | ~15,000-20,000 (redundant workflow × 3-4 sources)              |
| After            | ~6,000-8,000 (one canonical workflow + one page-type CRO card) |


That's a **60% reduction** in context consumption per task.