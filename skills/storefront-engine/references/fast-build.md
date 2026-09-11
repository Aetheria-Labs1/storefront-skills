# Fast Storefront Build

Create a useful unpublished draft from a prompt or template direction with the
fewest reversible steps. This workflow owns first-draft speed, not visual
approval, exhaustive QA, or live publishing.

## Inputs and Intent

Reuse a saved workspace, store and theme triple from
`work/storefront/setup/setup.json`: the one the user names, otherwise the
defaults, stated in one line. Read products, variants, prices, availability,
permissions, assets, and island schemas live.

Group the page with its campaign evidence under `references/page-files.md`.
Keep planning and source values in the task; create no local page files.

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
runs the external tier). Review the type checklist and record intentional
deviations before compilation.

## Assets First, Even on the Fast Path

Apply `references/workflows/_how-to-read.md` to the selected type. Fast mode
changes the repair/question budget, not source eligibility, inspection,
interactive schema resolution or copy policy. Use the shared workflow's
fast-draft fallback and return unresolved slots with `DRAFT_CREATED`.

Local-file UI remains `lexsis_asset_upload.upload`; supplied sources use
`lexsis_asset_import.import`. The exact split and fallback are owned by
`references/lexsis-mcp-contract.md`. A fast build grants neither paid asset
generation nor publication permission.

## Minimum decision evidence

Record the page type, objective, audience, product, CTA, template direction,
section order, design direction, asset decisions and proof/offer ledgers.
Use the minimum Consumer decision model from `consumer-behavior-cro.md`.
Record skipped stages in `workflow.skippedSkills`; this does not imply those
approval workflows ran. Prepare source values directly for MCP under
`references/source-artifact-workflow.md`, with current catalog bindings,
permanent asset URLs and valid font URLs or an intentional system stack.

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
5. Return the page id, version, preview URL, selected template,
   skipped skills, and `DRAFT_CREATED`.

If the compile id expires, recompile the same verified inputs once. Expiry is
not permission to repeat template search, planning, asset selection, critique,
or approval.

Do not block the first preview on screenshots, design critique, hosted QA,
commerce QA, reviewed/persisted hash reconciliation, or completed production-readiness checks.
Do not run repeated repair loops. If the one targeted repair still fails,
return the compiler blockers and the retained source values without claiming a
draft.

## After the First Draft

Keep the working draft visible even when later review finds an issue. Use
`/generate` to upgrade it to `DRAFT_READY`, and `/publish` only after explicit
approval for the named page and version.
