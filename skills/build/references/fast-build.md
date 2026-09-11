# Fast Storefront Build

Create a useful unpublished draft from a prompt or template direction with the
fewest reversible steps. This workflow owns first-draft speed, not visual
approval, exhaustive QA, or live publishing.

## Inputs and Intent

Reuse a saved workspace, store and theme triple from
`work/storefront/setup/setup.json`: the one the user names, otherwise the
defaults, stated in one line. Read products, variants, prices, availability,
permissions, assets, and island schemas live.

Infer the campaign folder from the prompt with the table in
`references/page-files.md` and create the page under
`work/campaigns/<campaign-slug>/pages/<page-handle>/`, with `campaign.json`
carrying the binding. A prompt with no campaign shape uses `adhoc-<yyyy-mm>`.
Say which folder is in use.

Accept:

- a prompt with a page-kit or section-template URL;
- a prompt with a kit slug or section-template id;
- a prompt without a template, when the user wants the skill to select a
  suitable page kit.

Use `fast-draft` unless the user explicitly asks for production-ready
verification. A production-ready request still gets the draft first and then
hands off to `/generate` for synchronization and QA. Never infer live
publishing.

## Resolve the Template Direction

For a page-kit URL or slug:

1. Resolve it with `lexsis_template_library` action `get_kit`.
2. Fetch all ordered section ids with `lexsis_design` action `get_section`,
   using batches of at most three. Independent batches may run in parallel.
3. Reassemble the returned source in the kit's original order.

For a section-template URL or id, fetch it with `lexsis_design` action
`get_section` and add only the minimum supporting source needed for a complete
page, such as navigation, commerce, proof, or a closing CTA when the prompt
requires them.

When no template is supplied, search page kits from the page type, objective,
industry, and mood. In a fast-draft request, choose the best coherent result
without waiting for a picker. Wait only when the user explicitly asks to
choose. If the shelf is empty, search sections and assemble the smallest
coherent page.

## Identify the Type Before Choosing a Kit

Walk `references/page-types/_index.md` from the prompt and record
`page.pageType`, `funnelStage`, `awareness` and `trafficSource` in the
manifest before searching kits. Load only that type's file and skim its `## Workflow`. A fast build
uses the type's checklist as the default anatomy; a kit whose structure
differs is adapted where cheap and the difference is noted in the plan.
Reviews render only from real data
(`references/proof/reviews-sourcing.md`, tiers 1 and 2; the fast path never
runs the external tier). Run
`python3 <plan-page-skill>/scripts/plan_lint.py <page-workspace>` once before
compiling when the script is available and note its WARN rows in the plan.

## Assets First, Even on the Fast Path

Speed changes how many questions are asked, never whether the page is built
around real imagery. Every section gets its media decided before its copy, by
the same loop as the reviewed route
(`references/workflows/section-asset-workflow.md`): catalog media through
`lexsis_catalog.get`, then `lexsis_asset_library.search` (tags, then semantic,
then `mode: "similar"` from the first accepted asset to keep a section's set
coherent), then merchant-owned sources including `lexsis_campaigns.creatives`.
A section that would ship as a colour band, an emoji row, icon tiles or a wall
of text is rebuilt around imagery.

Three rules hold at fast-draft speed:

1. **Nothing is used sight unseen.** Open every candidate with
   `lexsis_assets.view` and run the fit review in section 1b of
   `references/workflows/section-asset-workflow.md`: does the subject do the
   job, does it crop to the slot without losing the product, is there a quiet
   area where the copy sits, does it match the neighbouring slots, no baked-in
   text or watermark. View a section's or gallery's candidates together so the
   set reads as one shoot. This is the one check speed does not buy out,
   because an unviewed image is the fastest way to a page that looks wrong.
2. **A gap is reported, not hidden.** The fast path resolves what it can from
   existing media and leaves the rest `planned`, then lists every missing slot
   (section, job, aspect, count) in the plan and in the `DRAFT_CREATED`
   summary so the merchant can upload files through
   `lexsis_asset_upload.upload`, supply a URL or conversation attachment for
   `lexsis_asset_import.import`, or authorise generation. Wait for the user's
   uploaded-asset message when using the upload UI; without inline UI, use
   the URL/attachment import route. Paid generation is
   not part of the implicit fast path: ask once, with the exact slots, before
   spending credits, and use only ALLOW purposes from
   `references/assets/generation-policy.md`.
3. **Islands are resolved live.** Take the section's interaction need to
   `lexsis_design.islands`, then `lexsis_design.island_schema` for the one
   island chosen, and set the variant and props from what that schema offers
   (`references/workflows/island-selection-workflow.md`). Never carry a kit's
   island props forward without checking them against the current schema, and
   never use an island the catalog marks deprecated.

## Minimum Local Artifacts

Create the ordinary page workspace with:

- a concise `page-plan.md` containing the Page type block, objective,
  audience, product, CTA, template direction, section order, design
  direction, asset decisions, a minimum Proof ledger (and Offer ledger when
  the prompt names an offer), and a minimum Consumer decision model from
  `consumer-behavior-cro.md`;
- a compact schema-v3 `page-manifest.json`;
- `lexsis-source.html`;
- `page-theme.css`.

Record `plan-page` and `design-page` in `workflow.skippedSkills`; the minimum
artifacts do not imply those approval workflows ran. Record the inferred intent
evidence. Use current catalog bindings and permanent asset URLs. Custom fonts
must use complete HTTPS stylesheet URLs or an intentional system stack.

Use template source as the starting point, not an untouchable artifact. Make
only changes needed to satisfy the prompt and current store:

- replace sample copy and claims;
- bind current products and variants;
- apply the selected theme and brand tokens;
- replace placeholder or foreign media with viewed catalog or library assets;
- resolve only islands actually used;
- preserve the kit's coherent structure unless the prompt requires a change.

Reuse catalog and library media, viewed before use. Map the current gallery to
its relevant decision jobs first, then follow the three rules above for gaps.

Select at most two behavioral patterns for the first draft. Prefer a complete
first decision area and one page-specific uncertainty over adding many CRO
modules. Guided merchandising uses two or three products, a named
relationship, and a reason for every recommendation.

## One-Pass Draft Creation

1. Prepare exact source, theme, head, scripts, commerce configuration, and
   product bindings.
2. Call `lexsis_pages` action `compile` once.
3. If compilation fails, make one targeted repair from the reported blocking
   errors and compile once more.
4. Immediately call `lexsis_page_create` action `create` with
   `publish:false`.
5. Return the page id, version, preview URL, workspace paths, selected template,
   skipped skills, and `DRAFT_CREATED`.

If the compile id expires, recompile the same verified inputs once. Expiry is
not permission to repeat template search, planning, asset selection, critique,
or approval.

Do not block the first preview on screenshots, design critique, hosted QA,
commerce QA, remote/local hash reconciliation, or a `DRAFT_READY` validator.
Do not run repeated repair loops. If the one targeted repair still fails,
return the compiler blockers and the current source paths without claiming a
draft.

## After the First Draft

Keep the working draft visible even when later review finds an issue. Use
`/generate` to upgrade it to `DRAFT_READY`, and `/publish` only after explicit
approval for the named page and version.
