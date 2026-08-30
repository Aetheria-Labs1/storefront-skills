# Workflow Orchestration — Execution Engine

Load after `craft-guide`. Defines optimal tool sequences, parallelization rules, and flow selection.

---

## Flow Selection

```
What did the user provide?
│
├─ Ad creative (image URLs / screenshot)
│  → AD-TO-PAGE FLOW (analyze creative → extract style → generate matched page)
│
├─ Reference URL (competitor / inspiration)
│  → DESIGN-FIRST FLOW (agent screenshots URL → extracts tokens → uses as theme → generate)
│
├─ Brand brief only (name, industry, tone)
│  → STANDARD FLOW (context → assets → generate → validate → write)
│
├─ Existing page (wants edits)
│  → EDIT FLOW (read page → modify sections → validate → write)
│
├─ Product focus (PDP, collection)
│  → PRODUCT FLOW (lexsis_catalog.list first → build around real product data)
│
└─ Multiple inputs (ad + products + brand)
   → STANDARD FLOW with enriched context
```

---

## Standard Flow (5 Phases)

See `generation-protocol.md` for the full Phases 1-5 execution protocol (context gathering, asset preparation, HTML generation, validation, publishing + visual verification).

---

## Ad-to-Page Flow

```
Phase 2: Context
├─ lexsis_campaigns.analyze({ image_urls, ad_format })  → visual signals, CTA, headline
├─ get_storefront_skills({ brief from ad analysis, page_type: "landing" })
└─ lexsis_catalog.list()

Phase 3: Assets
├─ Use ad creative images directly where appropriate
├─ lexsis_drafts.asset_generate for additional sections (testimonial bg, trust section bg)
└─ lexsis_drafts.asset_generate with reference_images to adapt ad images (crop, extend, composite)

Phase 4-4: Same as Standard Flow
```

---

## Design-First Flow (Reference URL)

```
Phase 2:
├─ Agent screenshots URL               → extracted palette, fonts, spacing, tone
├─ get_storefront_skills(brief)
└─ lexsis_catalog.list()

Phase 3: Use extracted tokens as theme_css base
Phase 4-4: Same as Standard Flow
```

---

## Edit Flow (Safe Iteration)

```
1. lexsis_pages.find({ query })                              → locate page by handle/title/UUID
2. lexsis_pages.edit_context({ page_id })                 → resolve store/workspace + current version
3. lexsis_pages.source({ page_id })                       → read round-trip source when available
4. lexsis_pages.inspect({ page_id })                 → inspect current compiled sections
5. Identify which sections to modify
6. lexsis_drafts.page_update_section({ page_id, source, expected_version }) → compile, preflight, commit
7. lexsis_pages.integrity({ page_id, archetype })       → structural QA pass
8. [Optional] lexsis_pages.diff({ page_id, version_a, version_b })  → review all changes
9. [If broken] lexsis_live_ops.rollback({ page_id, target_version })    → revert to prior version
```

**Key rules:**
- `lexsis_drafts.page_update_section` compiles and runs the full-page preflight before it writes
- Existing page writes derive store/workspace from `page_id`; omit redundant `store_id`
- A `version_conflict` means another write landed first; re-read and rebase
- Run `lexsis_pages.integrity` after all edits complete — catches archetype violations (e.g. PDP without BuyBox)
- Use `lexsis_pages.diff` to verify your changes look correct before publishing
- Use `lexsis_live_ops.rollback` if integrity check fails — creates a new forward version, preserves history

---

## Duplication Flow (Idempotent)

```
1. lexsis_pages.find({ query })                                     → locate source page
2. lexsis_drafts.page_duplicate({ page_id, handle, idempotency_key })     → safe clone (retries won't create extras)
3. Edit sections on the duplicate (use Edit Flow above)
4. lexsis_pages.integrity({ page_id, archetype })             → final QA
```

**Idempotency key:** Pass a deterministic string (e.g. `"${handle}-v2-from-${source_handle}"`) so that retrying the same operation returns the existing duplicate instead of creating another.

---

## Parallelization Rules

| Can parallelize | Cannot parallelize |
|---|---|
| All Phase 2 context calls | Phase 3 needs Phase 2 results (brand_colors for asset gen) |
| Multiple lexsis_drafts.asset_generate calls | validate must complete before write |
| Asset generation for different sections | Reference-based generation needs source image URLs first |

---

## Cost Control

- `lexsis_asset_library` action `search` before `lexsis_drafts` action `asset_generate` — existing assets are free
- Use `quality: "medium"` for most assets, `"high"` only for hero images
- One hero image + one lifestyle shot usually enough for a PDP
- Landing pages: hero + 2-3 section backgrounds max
- Skip asset gen for sections using solid color/gradient backgrounds

---

## Page Type Defaults

### PDP Sections (6-8)
```
hero (product gallery + buybox) → trust-badges → benefits → ingredients → reviews → faq → sticky-cta → cart-drawer
```

### Landing Page Sections (7-10)
```
hero → trust-bar → problem/solution → features → before-after → testimonials → pricing → faq → cta → exit-intent
```

### Homepage Sections (5-7)
```
hero → featured-products → brand-story → social-proof → collections → newsletter → footer
```

### Collection Sections (4-6)
```
collection-header → filters → product-grid → featured-pick → trust-bar → newsletter
```

---

## Credit Costs

Always call `lexsis_workspace` with action `credits` before expensive
operations. If balance is 0, inform the user before proceeding.

| Tool | Cost | Notes |
|------|------|-------|
| `lexsis_drafts` → `asset_generate` | credits | AI image generation, editing, and compositing |
| `lexsis_page_create` → `create` | credits | Draft page generation |
| `lexsis_drafts` → `page_variation` | credits | A/B variant creation (requires Pro plan) |
| `lexsis_drafts` → `experiment_create` | credits | Experiment setup (requires Pro plan) |
| `lexsis_drafts` → `page_update_section` | credits | Section regeneration |
| `lexsis_pages` → `compile` | FREE | Always validate before creating or publishing |
| `lexsis_pages` → `integrity` | FREE | Structure/accessibility check |
| All read/list/get tools | FREE | No cost for browsing data |

**Preflight pattern:**
```
lexsis_workspace(credits) → check cost → warn if insufficient → proceed or abort
```

Source-format pages persisted through `lexsis_page_create` still cost credits
(the write action, not the compiler, bills). Draft previews also consume
credits.
