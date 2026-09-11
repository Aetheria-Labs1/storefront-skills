# Lexsis MCP Tool Sequence by Stage

The exact `router.action` order for a page, from setup to publish. Skills list
the actions they own; this file shows how they chain and what each call must
return before the next one runs. Resolve an unfamiliar argument schema with
`lexsis_discover` using structured `router` and `action` fields, never a
prose query for a known pair (`references/lexsis-mcp-contract.md`).

Legend: **R** read, **W** reversible write, **$** spends credits (confirm
first), **!** requires explicit approval (`lexsis_live_ops`).

## Stage 0: Setup (once per store/theme)

| # | Call | Type | Needed before |
|---|---|---|---|
| 1 | `lexsis_workspace.list` then `.get` | R | everything |
| 2 | `lexsis_workspace.stores` | R | choosing the store |
| 3 | `lexsis_brand.context` | R | any design decision |
| 4 | `lexsis_brand.brand_kit` | R | palette, fonts, voice, banned phrases |
| 5 | `lexsis_brand.list_themes` then `.get_theme` | R | `page-theme.css` |
| 6 | `lexsis_brand.navigation` | R | header/footer links (full-nav types only) |
| 7 | `lexsis_design.guide` | R | `brand-design.md` |

Output: `work/storefront/setup/setup.json` plus saved brand and theme files.
Everything below reads the saved pair and refreshes only volatile data.

## Stage 1: Plan

Order matters: identify the type before searching anything.

| # | Call | Type | Purpose | Gate |
|---|---|---|---|---|
| 1 | read `setup.json` | local | one store/theme pair | stop if missing |
| 2 | `lexsis_catalog.list` then `.get` per product | R | title, variants, prices, availability, media, description | every product on the page |
| 3 | walk `references/page-types/_index.md`, then the type's `## Workflow` context reads | local | `pageType`, funnel stage, awareness, offer, campaign; image count and jobs, variant axes, review band | record `## Page type` block |
| 4 | `lexsis_campaigns.creatives` then `.analyze` (or view the creative yourself) | R | message match for ad-driven types | ad-landing, advertorial, listicle, retargeting |
| 5 | `lexsis_campaigns.personas` then `.match_persona` | R | vocabulary, pain points | when personas exist |
| 6 | `lexsis_catalog.reviews_status` | R | is a review source connected, how many imported | before any proof plan |
| 7 | `lexsis_catalog.review_collections` (`collection_status: "active"`) | R | curated sets with counts | if connected |
| 8 | `lexsis_catalog.reviews` (`rating_min`, `has_media`, `product_id`) | R | count, media, distribution | if connected |
| 9 | `lexsis_catalog.reviews_search` (`query` = the page's key claim) | R | proof-proximity candidates | one call per top decision question |
| 10 | host web search + `lexsis_assets.view` | R | zero-review playbook tiers 3 to 5 | only when 6 to 8 return nothing usable (`references/proof/reviews-sourcing.md`) |
| 11 | `lexsis_template_library.search_page_kits` (`query: ""`, filters) | R | user picks or skill picks a direction | after page type is fixed |
| 12 | `lexsis_template_library.search_sections` | R | when no kit fits | at most three candidates |
| 13 | `lexsis_template_library.get_kit` | R | resolve a slug or URL | user-picked kit |
| 14 | `lexsis_asset_library.search` (`theme_id`, `mode: "tags"`, then semantic) | R | resolve slots the user did not pick | after gallery jobs mapped |
| 15 | `lexsis_assets.view` | R | verify identity-sensitive picks | every product or person image |
| 16 | `lexsis_asset_import.import` or `lexsis_asset_upload.upload` | W | import a supplied URL, image base64 plus MIME type, or attachments; use upload only for the local-file UI | before any generation; wait for the user's uploaded-asset message for UI uploads; without inline UI, ask for a URL or attachment and import it |
| 17 | `lexsis_workspace.credits` | R | balance before asking | before 18 |
| 18 | `lexsis_drafts.asset_generate` | W $ | only ALLOW-list purposes (`references/assets/generation-policy.md`) | one confirmation per batch |
| 19 | `lexsis_capture.funnel_templates` then `.funnel_template` | R | quiz, gift-reveal, personalised-offer structure | quiz-funnel and lead-capture types |
| 19b | `lexsis_capture.form_schemas`, then `.submissions` for an existing form | R | field shapes; whether a live form already collects what the page needs (PII is redacted) | lead-capture, giveaway, wholesale, waitlist |
| 20 | `lexsis_drafts.review_collection_create` | W | draft shortlist for the merchant to activate | only when asked |

Output: `page-plan.md` with Page type, Design direction, Consumer decision
model, Proof ledger, Offer ledger, Imagery plan, Asset slots; compact
`page-manifest.json`. Run `plan_lint.py` before approval.

## Stage 2: Design

| # | Call | Type | Purpose | Gate |
|---|---|---|---|---|
| 1 | read plan + manifest + page-type file | local | follow its `## Workflow`; note deviations | ask only when a deviation is unexplained |
| 2 | `lexsis_brand.context`, `.get_theme` | R | live tokens | compare with saved; `THEME_CONTEXT_CONFLICT` on value clash |
| 3 | `lexsis_template_library.get_kit` then `lexsis_design.get_section` (1 to 3 ids per call, kit order) | R | authoring source | only ids in the manifest |
| 4 | `lexsis_template_library.list_mine` then `.get_mine` | R | merchant's saved sections | when the user names one |
| 5 | `lexsis_design.islands` | R | compact catalog | select only interactive needs |
| 6 | `lexsis_design.island_schema` | R | exact props | per island actually used, or per compile error |
| 7 | `lexsis_catalog.get` | R | current variant ids, prices | before binding BuyBox |
| 8 | `lexsis_catalog.reviews` / `.review_collection_items` | R | `collectionId` or `productIds`, `minRating`, real totals | review islands only |
| 9 | `lexsis_asset_library.search`, `lexsis_assets.view`, `lexsis_asset_import.import`, `lexsis_asset_upload.upload` | R/W | resolve `planned` slots; import supplied sources, upload for local-file UI only | never placeholders; wait for the user's uploaded-asset message for UI uploads |
| 10 | `lexsis_workspace.credits` then `lexsis_drafts.asset_generate` | W $ | remaining ALLOW-list gaps | ask first |
| 11 | `lexsis_pages.compile` | R | validation_errors as the work list | loop until clean |
| 12 | `lexsis_page_create.create` (`publish: false`) | W | one hosted draft | once per page; reuse `remote.pageId` after |
| 13 | host browser at 390 and 1280 | local | hosted design review | production-ready only |
| 14 | `lexsis_drafts.page_update_section` / `.page_patch` (`expected_version`) | W | fix review findings | never a second draft |

Output: `lexsis-source.html`, `page-theme.css`, `compile-artifact.json`,
`DRAFT_CREATED`, later `DESIGN_APPROVED`.

## Stage 3: Generate (sync + QA)

| # | Call | Type | Purpose |
|---|---|---|---|
| 1 | `lexsis_pages.edit_context` then `.source` | R | detect version drift |
| 2 | `lexsis_catalog.get` | R | refresh variants and prices |
| 3 | `lexsis_design.island_schema` | R | islands still active |
| 4 | `lexsis_pages.compile` | R | clean artifact |
| 5 | `lexsis_pages.integrity` then `.qa` | R | hosted QA record |
| 6 | `lexsis_drafts.page_record_qa` | W | store QA evidence |
| 7 | `lexsis_drafts.page_update_head` | W | title, description, fonts |
| 8 | `lexsis_cart.get` then `lexsis_drafts.cart_set` | R/W | cart profile matches the offer |
| 9 | `lexsis_capture.get_funnel`, `.validate_funnel`, `.preview_funnel`; `lexsis_drafts.funnel_update` | R/W | a funnel draft's steps read back, validated, previewed and adjusted before review |
| 10 | `lexsis_support.search_docs` | R | only when a Lexsis behaviour is unclear |

Output: `DRAFT_READY`.

## Stage 4: Publish and after

| # | Call | Type | Purpose |
|---|---|---|---|
| 1 | `lexsis_live_ops.publish` | W ! | named page and version only |
| 2 | `lexsis_analytics.page`, `.timeseries`, `.attribution` | R | first-week read |
| 3 | `lexsis_drafts.page_variation` then `.experiment_create` | W | challengers (`/ab-test`) |
| 4 | `lexsis_analytics.experiment` then `lexsis_live_ops.scale_winner` | R / W ! | evaluate, then scale |
| 5 | `lexsis_live_ops.rollback` / `.unpublish` | W ! | undo |

## Never

- Never call `lexsis_page_create.create` when `remote.pageId` exists.
- Never call `lexsis_drafts.asset_generate` before `lexsis_asset_library.search`
  and `lexsis_catalog.get` have been checked for the same slot.
- Never fill review props from anything other than `lexsis_catalog.reviews`
  or `.review_collection_items`.
- Never use `lexsis_discover` as a health check; a zero-count directory
  result is a lookup miss.
- Never call a `lexsis_live_ops` action without the user's explicit approval
  for that page and version in the current conversation.
