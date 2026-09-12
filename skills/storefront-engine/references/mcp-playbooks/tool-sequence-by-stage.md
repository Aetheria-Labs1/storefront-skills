# Lexsis MCP Tool Sequence by Stage

Resolve unfamiliar schemas with exact router/action discovery. **R** is read,
**W** is reversible write, **$** spends credits, and **!** requires explicit
live-operation approval.

## Stage 0: Setup

| Order | Calls | Purpose |
|---|---|---|
| 1 | `lexsis_workspace.list`, `.get`, `.stores` | binding |
| 2 | `lexsis_brand.context`, `.brand_kit`, `.navigation` | brand context |
| 3 | `lexsis_brand.list_themes`, `.get_theme`; `lexsis_design.guide` | theme and design |
| 4 | paginated `lexsis_catalog.list`, batched `.get` | product map |
| 5 | `lexsis_catalog.reviews_status`, `.review_collections` | rules/proof availability |

Output: `work/storefront/setup.md` and the selected store's structured context
files.

## Stage 1: Plan Page

Identify the page type before template search.

| Order | Calls | Purpose |
|---|---|---|
| 1 | read setup context | brand, product map, personas, rules, theme |
| 2 | `lexsis_catalog.list`, `.get` | refresh selected products and media jobs |
| 3 | `lexsis_catalog.reviews_status`, `.review_collections`, `.reviews`, `.reviews_search` | proof and claims |
| 4 | `lexsis_capture.funnel_templates`, `.funnel_template` | quiz/lead structure only |
| 5 | `lexsis_template_library.search_page_kits` | after sections are planned |
| 6 | `.search_sections`, `.get_kit` | section fallback or selected kit |

Output: complete plan with final copy and asset requirements;
`PLAN_READY_FOR_APPROVAL`, then `PLAN_APPROVED`.

## Stage 1a: Visualize Page (Optional)

1. Read the approved plan, store design context, theme, and real product media.
2. Discover currently available image-generation/editing capabilities.
3. When Lexsis is used, call `lexsis_assets.capabilities`, then
   `lexsis_workspace.credits`, obtain batch approval, call
   `lexsis_drafts.asset_generate`, and inspect with `lexsis_assets.view`.
4. Import a retained external concept with `lexsis_asset_import.import` and
   mark it `concept-only`.

Output: ordered frames and `VISUAL_DIRECTION_APPROVED`, or
`VISUAL_DIRECTION_SKIPPED`.

## Stage 1b: Plan Assets

Run for every requirement:

| Order | Calls | Purpose | Gate |
|---|---|---|---|
| 1 | `lexsis_catalog.get` | exact real product/variant media | always |
| 2 | `lexsis_asset_library.search` | existing library candidates | always |
| 3 | `lexsis_assets.view` | crop, identity, fit, rights review | every candidate |
| 4 | `lexsis_asset_upload.upload` or `lexsis_asset_import.import` | merchant/external source | wait for completion |
| 5 | discover client capabilities; `lexsis_assets.capabilities` as fallback | choose production operation | missing eligible slot |
| 6 | `lexsis_workspace.credits` | known Lexsis cost | before paid generation |
| 7 | `lexsis_drafts.asset_generate` | approved fallback production | W $ |
| 8 | `lexsis_asset_import.import` | persist external output | before binding |
| 9 | `lexsis_assets.view` | final verification | every produced asset |

Output: permanent slot bindings and `ASSETS_READY`,
`ASSETS_PENDING_USER`, or `ASSETS_BLOCKED`.

## Stage 2: Design Page

1. Read `PLAN_APPROVED`, `ASSETS_READY`, and optional visual decisions.
2. Refresh theme and commerce facts.
3. Fetch selected kit/section source.
4. Resolve current islands and schemas.
5. Author and compile the complete page.
6. Create one `publish:false` hosted draft.
7. Review at 390, 768, and 1280 and repair with version-safe edits.

Output: `DRAFT_CREATED`, then `DESIGN_APPROVED`.

## Stage 3: Publish and Experiment

| Call | Type | Purpose |
|---|---|---|
| `lexsis_live_ops.publish` | W ! | publish the named approved version |
| `lexsis_analytics.page`, `.timeseries`, `.attribution` | R | performance read |
| `lexsis_drafts.page_duplicate`, `.experiment_create` | W | draft challengers |
| `lexsis_analytics.experiment` | R | evaluate |
| `lexsis_live_ops.scale_winner` | W ! | scale after explicit approval |

## Invariants

- Asset search and view precede generation.
- External outputs are imported before binding.
- Concepts never fill production slots.
- `ASSETS_READY` requires permanent verified bindings.
- Page creation is not publication.
- No `lexsis_live_ops` call runs without explicit approval for the named
  resource and version.
