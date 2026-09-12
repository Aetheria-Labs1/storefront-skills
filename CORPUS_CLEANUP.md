# Reference corpus cleanup

## Plan

Baseline: `2350aa2` on `feat/workflow-corpus-v7.9.0`. Work stays on this
branch; no commit, push, release, or parent-submodule update is implied.
All requested baseline checks pass: 49 tests, 30 page types, zero island
errors, generated distributions current, and the corrected/rejected design
fixtures exit 0/1. The island validator reports 28 deprecation warnings.
The current MCP source declares 18 routers and 92 actions.

1. Resolve contradictions at their source. Replace misleading recipes, not
   their warning banners. Preserve the compiler contract and N1-N14/A1-A12.
   A11 currently requires 48px tap targets; retain that stronger house rule
   instead of weakening it to the external 24/44px floors.
2. Consolidate universal procedures into `workflows/`: asset acquisition and
   missing-slot handling, view-and-fit review, live island resolution, and
   copy execution. Policy remains in its existing domain owner. Page-type
   workflows retain only their context reads, per-section decisions, and
   asset budgets. Keep checklist JSON and required headings unchanged.
3. Retain specialized operational guidance and vertical/traffic decisions;
   replace duplicate legacy entry points with short routing paragraphs.
   Transfer unique evidence before removing prose. Preserve every original
   URL, with provenance for addresses moved to the citation ledger.
4. Update distribution dependencies and remove obsolete generated copies
   through the generator, not hand edits. Test reference closure, action
   validity, contradiction regressions, checklist preservation, and evidence
   preservation. Re-run every requested verification and record metrics.
5. Per the user's follow-up, remove local page workspaces and local QA
   entirely from the shipped workflows, not merely make them optional.
   Send source strings and optional theme CSS directly to MCP. Keep compiler
   validation, version protection, proof/offer review and hosted QA.
   Retire workspace adapters, migrations and their obsolete tests. Retain
   corpus/fixture regression checks under repository-only test support, not
   inside public skills. The old workspace/fixture command paths consequently
   change; report the replacement verification commands and test count.

## Rule owners

| Subject | Single owner | Other files retain |
|---|---|---|
| Visual/accessibility requirements | `references/design-rules.md` | Rule IDs and application-specific decisions |
| Section asset acquisition, fallback, view and fit | `references/workflows/section-asset-workflow.md` | Type-specific jobs, tags, crops, budgets |
| Generation permissions | `references/assets/generation-policy.md` | Purpose IDs and policy links |
| Rights and source eligibility | `references/assets/asset-sourcing-sequence.md` | Source choice, not another sourcing procedure |
| Island selection and schema resolution | `references/workflows/island-selection-workflow.md` | Candidate families and decision inputs |
| Copy execution | `references/workflows/copy-workflow.md` | Type-specific ceilings and message constraints |
| Proof and offer evidence | `references/proof/`, `references/offers/` | Relevant ledger kind/offer ID and placement |
| Section order | `references/page-types/<type>.md` | Links, never another default recipe |
| Source and CSS contracts | `references/authoring/` | Small conforming examples or links |
| MCP-first authoring and hosted verification | `references/source-artifact-workflow.md` | Direct source inputs and persisted version evidence |

## Per-file decisions

All paths in this table are relative to the canonical `references/` folder.
"Keep" means keep and correct; it does not preserve contradictory examples.
"Shrink" means one routing paragraph and links, with unique URLs retained
in the evidence ledger if they no longer appear in another canonical file.
No file requires deletion: retaining small entry points preserves existing
consumer links without retaining a second implementation.

| Legacy flat file | Decision | Retained value or destination |
|---|---|---|
| ab-test-variant.md | Shrink | ab-testing.md |
| ab-testing.md | Keep | URL-first control resolution and experiment lifecycle |
| ad-to-page.md | Keep | Extract the actual ad and bind the destination |
| analytics.md | Keep | Analytics operations and evidence boundaries |
| animation-system.md | Keep | Managed runtime APIs and declared capabilities |
| asset-pipeline.md | Shrink | workflows/section-asset-workflow.md |
| asset-prep.md | Keep | Import/upload mechanics and standalone asset handoff |
| blob-shapes.md | Keep | Static SVG clipping geometry |
| cart-composition.md | Keep | Cart V2 page integration |
| cart-profile-management.md | Keep | Cart profile lifecycle |
| competitor-remix.md | Keep | Reference provenance and merchant-owned adaptation |
| composition-patterns.md | Keep | Conforming static composition examples |
| consumer-behavior-cro.md | Keep | Behavioral hypothesis selection |
| conversion-psychology.md | Shrink | consumer-behavior-cro.md and copy/copy-frameworks.md |
| cro-research.md | Shrink | consumer-behavior-cro.md and citation ledger |
| design-assets.md | Shrink | assets/asset-sourcing-sequence.md |
| design-concepts.md | Keep | Concept-only approval boundary |
| design-enrichment.md | Shrink | assets/generation-policy.md |
| design-rules.md | Keep | Highest documentation authority; no semantic weakening |
| extract-template.md | Keep | Capture and reusable-source extraction |
| fast-build.md | Removed in 8.0.0 | superseded by /plan-page approval and /design-page hosted QA |
| generate-bundle-page.md | Shrink | page-types/bundle-kit.md |
| generate-collection.md | Shrink | page-types/collection-landing.md |
| generate-editorial.md | Shrink | page-types/advertorial.md and brand-story-founder.md |
| generate-homepage.md | Shrink | page-types/homepage.md |
| generate-landing-page.md | Shrink | page-types/ad-landing-page.md |
| generate-listicle.md | Shrink | page-types/listicle.md |
| generate-pdp.md | Shrink | page-types/pdp.md |
| generation-protocol.md | Keep | Compile, version, draft and QA state transitions |
| island-patterns.md | Shrink | workflows/island-selection-workflow.md and authoring/source-authoring.md |
| island-presets.md | Shrink | workflows/island-selection-workflow.md; remove frozen prop maps |
| lexsis-design-capabilities.md | Keep | Tool capability boundaries |
| lexsis-mcp-contract.md | Keep | MCP discovery, imports/uploads and errors |
| merchant-templates.md | Keep | Merchant-template lifecycle and authority |
| page-editing.md | Keep | Versioned edits and conflict recovery |
| page-files.md | Keep | Task-held page/campaign evidence; no local page files |
| page-generation.md | Shrink | page-types/_index.md and workflows/_how-to-read.md |
| page-redesign.md | Keep | Explicit redesign scope and comparison evidence |
| personalization-variant.md | Keep | Persona-specific hypothesis and provenance |
| plan-page.md | Shrink | workflows/_how-to-read.md and page-types/_index.md |
| premium-patterns.md | Shrink | page-types/_index.md and authoring/css-and-styling.md |
| primitives-guide.md | Shrink | authoring/source-authoring.md |
| product-grid.md | Keep | Static grid, native navigation, commerce boundary |
| publishing.md | Keep | Explicit publication and verification lifecycle |
| qa-recipe.md | Keep | Hosted QA evidence and release gate |
| reference-pdp-remix.md | Keep | Reference capture and fidelity evaluation |
| scroll-patterns.md | Keep | Native scrolling without scroll hijacking |
| section-library.md | Keep | Search and fetch editable section templates |
| source-artifact-workflow.md | Keep | Direct MCP inputs, persisted versions and hosted verification |
| source-format.md | Keep | Compact source syntax and compiler entry points |
| storefront-craft.md | Shrink | workflows/_how-to-read.md and authoring/ |
| style-packs.md | Keep | Scoped aesthetic direction without duplicate island props |
| traffic-source-google.md | Keep | Search intent and message-match decisions |
| traffic-source-meta.md | Keep | Creative-to-page continuity and cold/warm traffic |
| traffic-source-tiktok.md | Keep | Creator/video continuity and mobile entry context |
| vertical-beauty.md | Keep | Shade, texture, ingredient and suitability decisions |
| vertical-fashion.md | Keep | Fit, scale, fabric and variant decisions |
| vertical-food.md | Keep | Ingredients, serving, dietary and replenishment decisions |
| vertical-home.md | Keep | Dimensions, materials, placement and delivery decisions |
| vertical-luxury.md | Keep | Provenance, craftsmanship and service decisions |
| vertical-supplements.md | Keep | Label, dosage, evidence and suitability decisions |
| visual-craft.md | Shrink | authoring/css-and-styling.md |
| visual-layout-workflow.md | Shrink | workflows/_how-to-read.md |
| workflow-handoffs.md | Keep | Command handoff states |
| workflow-intent.md | Keep | Fast-draft versus production-ready routing |
| workflow-orchestration.md | Keep | Independent commands and explicit skips |

## Results

Implemented on `feat/workflow-corpus-v7.9.0` from baseline `2350aa2`.
The user subsequently authorized committing and pushing this feature branch.
This does not merge into `main`, publish a release, or update the parent
repository's submodule pin.

### MCP-only page workflow

The user's final instruction replaced the initial optional-workspace approach.
The public skills now create no per-page source, CSS, manifest, compile
artifact, preview or QA files. They send source and optional `theme_css`
directly through MCP, retain the returned page/version evidence, and review
the hosted draft. No local page validator, migration or compile adapter ships.
The mutually exclusive `compile_id` versus inline-source creation modes are
documented; source fields are not sent alongside a compile id.

Removed:

- `skills/generate/scripts/prepare_workspace_compile.py`
- `skills/generate/scripts/validate_page_workspace.py`
- `skills/generate/scripts/migrate_page_workspace_v3.py`
- `tests/test_page_workspace_validator.py` (20 tests for the retired workflow)
- Cached bytecode for the retired workspace and preview tools.

The existing checklist/design fixture checks moved from the public skills to
`tests/support/plan_lint.py` and `tests/support/design_lint.py`. These are
repository regression tests, not page-authoring steps or shipped skill tools.
Their advisory/strict behavior and copy-warning versus proof/offer-failure
split remain tested.

### Corpus size

Counts below include canonical Markdown only, grouped by the first folder
under `skills/storefront-engine/references/`. They exclude schema JSON,
generated skill copies and GPT output. The 30 page contracts include their
index/format files in the `page-types` folder count.

| Folder | Before lines | After lines | Before bytes | After bytes |
|---|---:|---:|---:|---:|
| Flat references | 17,231 | 3,238 | 818,246 | 153,052 |
| anti-patterns | 847 | 612 | 105,430 | 74,563 |
| assets | 1,510 | 1,414 | 148,449 | 136,509 |
| authoring | 734 | 160 | 38,624 | 7,926 |
| copy | 711 | 631 | 63,017 | 55,047 |
| islands | 1,379 | 521 | 56,196 | 26,777 |
| mcp-playbooks | 162 | 189 | 14,855 | 18,406 |
| offers | 1,248 | 1,212 | 140,656 | 136,422 |
| page-types | 12,495 | 8,573 | 901,439 | 800,831 |
| proof | 1,341 | 1,215 | 129,617 | 121,407 |
| sources | 0 | 61 | 0 | 4,515 |
| workflows | 933 | 261 | 69,531 | 15,161 |
| **Total** | **38,591** | **18,087** | **2,486,060** | **1,550,616** |

Canonical Markdown is 53% shorter by lines and 38% smaller by bytes.
Page types are 31% shorter by lines but 11% smaller by bytes: the decision
tables account for part of the line reduction, so this is not a claim of
31% less page-type content.

`gpt/knowledge.md`: 522,650 -> 375,231 bytes (28% smaller).

### Deleted or shrunk references

No canonical reference entry point was deleted or renamed. The 22 files
marked **Shrink** in the per-file table are now routing paragraphs:

`ab-test-variant.md`, `asset-pipeline.md`, `conversion-psychology.md`,
`cro-research.md`, `design-assets.md`, `design-enrichment.md`,
`generate-bundle-page.md`, `generate-collection.md`, `generate-editorial.md`,
`generate-homepage.md`, `generate-landing-page.md`, `generate-listicle.md`,
`generate-pdp.md`, `island-patterns.md`, `island-presets.md`,
`page-generation.md`, `plan-page.md`, `premium-patterns.md`,
`primitives-guide.md`, `storefront-craft.md`, `visual-craft.md`,
`visual-layout-workflow.md`.

Other retained files were corrected or condensed according to their table
entry, including the nine vertical/traffic references and the source,
styling, scrolling, generation and publishing contracts.

`page-layout.md`, `source-and-sync.md`, `industry-cro.md` and
`evidence-led-cro.md` previously existed only beside commands; they now have
canonical sources and generated command copies. New canonical additions are
the copy execution workflow, source-derived router/action inventory and
legacy evidence ledger.

The builder updates/prunes generated copies from declared roots and verified
dependencies. An explicit corpus-to-flat bridge allowlist keeps closure
bounded; reference-closure tests cover every public command.

### Preserved and deliberately retained

- All 30 checklist JSON objects, required headings, workflow section ids and
  their order match the baseline. No section/proof/image/offer/campaign
  vocabulary was added.
- All 26 house imperative clauses retain their requirements. File references
  became task records or MCP CSS values, and checks now use persisted source
  and hosted output. A11 retains 48px for every authored tap target.
- All 636 baseline Markdown URL tokens survive, with moved addresses tracked
  by original file. This count includes a literal URL placeholder; it is not
  a claim of 636 independent research citations. The non-ASCII URL is preserved
  with equivalent percent encoding.
- All 55 schema structures retain props, variants, defaults and authoring
  capabilities. Frozen authoring examples were removed, rather than leaving
  emoji-heavy or retired-island recipes below warnings. Recommendation
  annotations were corrected; the eight deprecated compatibility schemas
  remain available to interpret older pages, not to author new ones.
- Island choices/props come from live discovery. Preset labels retain only
  intent; static preset bundles and their retired workspace gate are gone.
- The current sibling MCP source still declares 18 routers and 92 actions.
  Import accepts supplied sources; upload alone owns the local-file UI.
- Domain evidence tables and type-specific media jobs, budgets, search tags,
  copy ceilings and decision inputs remain. Terms such as `compare-at`,
  `endsAt` and `ALLOW` still occur where a field, policy link or concrete
  type-specific decision needs them; they are not renamed to disguise usage.
- One-time multi-workspace setup caching remains: it is reusable connection/
  brand context, not per-page rendering or local QA. Standalone asset work
  remains an independent utility.

The repeated procedures have single owners. `sight unseen`, `one shoot` and
`closest existing asset` each occur only in the section-asset workflow, not
in the 30 page contracts. No warning banner is used to excuse invalid guidance.

### Verification

Baseline: all seven originally requested commands passed, including 49 tests
and design fixture exits 0/1. After the user's removal request, the two
fixture-check paths moved out of public skills; the original paths no longer
exist by design.

Final checks:

```text
python3 scripts/build-distributions.py                         PASS
python3 scripts/build-distributions.py --check                 up to date
python3 scripts/validate-page-types.py                         30/30
python3 scripts/validate-island-contracts.py                    errors 0, warnings 0
python3 -m unittest discover -s tests -p 'test_*.py'             43 passed
python3 tests/support/design_lint.py tests/fixtures/design-lint/corrected  exit 0
python3 tests/support/design_lint.py tests/fixtures/design-lint/rejected   exit 1
git diff --check                                               PASS
```

Test-count reconciliation: 49 baseline - 20 retired workspace tests +
14 corpus regression tests = 43. The old compile-adapter test was replaced
by a public-pack test that rejects reintroduced local QA tooling.

The island validator now scans every nested canonical Markdown reference.
There are no concrete frozen island prop examples left to validate; schema
structure preservation, active authored names and the nested scanner are
covered by separate tests. This is not a claim that live MCP compilation
or browser QA was performed on a storefront.

No live page, experiment, asset or infrastructure was created, edited or
published during this cleanup.
