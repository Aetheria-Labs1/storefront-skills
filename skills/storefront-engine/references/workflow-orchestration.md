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
│  → PRODUCT FLOW (list_products first → build around real product data)
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
├─ analyze_ad_creative({ image_urls, ad_format })  → visual signals, CTA, headline
├─ get_storefront_skills({ brief from ad analysis, page_type: "landing" })
└─ list_products()

Phase 3: Assets
├─ Use ad creative images directly where appropriate
├─ generate_asset for additional sections (testimonial bg, trust section bg)
└─ edit_asset to adapt ad images (crop, extend, composite)

Phase 4-4: Same as Standard Flow
```

---

## Design-First Flow (Reference URL)

```
Phase 2:
├─ Agent screenshots URL               → extracted palette, fonts, spacing, tone
├─ get_storefront_skills(brief)
└─ list_products()

Phase 3: Use extracted tokens as theme_css base
Phase 4-4: Same as Standard Flow
```

---

## Edit Flow (Safe Iteration)

```
1. find_page({ query })                              → locate page by handle/title/UUID
2. get_page_content({ page_id })                     → read current sections + head
3. Identify which sections to modify
4. preview_section_update({ page_id, section_id, html })  → dry-run validation (repeat per section)
5. update_page_section({ page_id, section_id, html })     → commit change (bumps version)
6. check_page_integrity({ page_id, archetype })           → structural QA pass
7. [Optional] diff_page_versions({ page_id, version_a, version_b })  → review all changes
8. [If broken] rollback_page_version({ page_id, target_version })    → revert to prior version
```

**Key rules:**
- Always `preview_section_update` before `update_page_section` — catches validation errors without bumping version
- Run `check_page_integrity` after all edits complete — catches archetype violations (e.g. PDP without BuyBox)
- Use `diff_page_versions` to verify your changes look correct before publishing
- Use `rollback_page_version` if integrity check fails — creates a new forward version, preserves history

---

## Duplication Flow (Idempotent)

```
1. find_page({ query })                                     → locate source page
2. duplicate_page({ page_id, handle, idempotency_key })     → safe clone (retries won't create extras)
3. Edit sections on the duplicate (use Edit Flow above)
4. check_page_integrity({ page_id, archetype })             → final QA
```

**Idempotency key:** Pass a deterministic string (e.g. `"${handle}-v2-from-${source_handle}"`) so that retrying the same operation returns the existing duplicate instead of creating another.

---

## Parallelization Rules

| Can parallelize | Cannot parallelize |
|---|---|
| All Phase 2 context calls | Phase 3 needs Phase 2 results (brand_colors for asset gen) |
| Multiple generate_asset calls | validate must complete before write |
| Asset gen for different sections | edit_asset needs source image URLs first |

---

## Cost Control

- `search_design_library` before `generate_asset` — existing assets are free
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

Always call `get_credits_balance` before expensive operations. If balance is 0, inform the user before proceeding.

| Tool | Cost | Notes |
|------|------|-------|
| `generate_asset` | credits | AI image generation |
| `edit_asset` | credits | AI image editing/compositing |
| `publish_vibe_page` | credits | Page generation (only on publish, not drafts) |
| `create_page_variation` | credits | A/B variant creation (requires Pro plan) |
| `create_ab_test` | credits | Experiment setup (requires Pro plan) |
| `update_page_section` | credits | Section regeneration |
| `validate_vibe_page` | FREE | Always validate before publishing |
| `check_page_integrity` | FREE | Structure/accessibility check |
| All read/list/get tools | FREE | No cost for browsing data |

**Preflight pattern:**
```
get_credits_balance → check cost → warn if insufficient → proceed or abort
```

Hand-authored VibePage JSON persisted via `publish_vibe_page` still costs credits (it's the publish action, not the AI generation, that bills). Draft previews (`draft: true`) also consume credits.
