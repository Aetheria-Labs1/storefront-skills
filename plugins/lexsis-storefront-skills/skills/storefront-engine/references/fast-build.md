# Fast Storefront Build

Create a useful unpublished draft from a prompt or template direction with the
fewest reversible steps. This workflow owns first-draft speed, not visual
approval, exhaustive QA, or live publishing.

## Inputs and Intent

Reuse the saved store/theme binding from
`work/storefront/setup/setup.json`. Read products, variants, prices,
availability, permissions, assets, and island schemas live.

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

## Minimum Local Artifacts

Create the ordinary page workspace with:

- a concise `page-plan.md` containing objective, audience, product, CTA,
  template direction, section order, design direction, and asset decisions;
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
- replace placeholder or foreign media;
- resolve only islands actually used;
- preserve the kit's coherent structure unless the prompt requires a change.

Paid asset generation is not part of the implicit fast path. Reuse catalog and
library media, or ask once before generating the unresolved production gaps.

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

