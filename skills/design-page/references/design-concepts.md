# Visual Concept Preview

Use this optional path inside `/design-page` when the user wants to approve the
visual direction before source authoring. Do not run it merely because image
generation is available.

## Route by Intent

- Use concept-first when the user asks for a mockup, wants to see the design
  before it is built, or explicitly asks to approve the visual direction.
- Skip it for fast-build, template-first, or direct-draft requests.
- When intent is genuinely unclear, offer two concise choices: generate a
  visual concept first, or continue directly to the interactive page preview.
- A concept request authorizes the workflow, not an unpriced credit charge.
  Check capabilities and credits and confirm immediately before paid
  generation unless the user already explicitly authorized that generation.

## Generate Mobile First

Use the existing Lexsis image tools:

1. Read current image capabilities through `lexsis_assets` action
   `capabilities`.
2. Build the prompt from `page-plan.md`, the saved theme and brand direction,
   the wireframe, and real product or brand reference images.
3. Call `lexsis_drafts` action `asset_generate` with a portrait output suitable
   for a mobile concept.
4. Show the result with `lexsis_assets` action `view`.

The concept should communicate hierarchy, composition, typography character,
media treatment, color, and the one bold moment. Generated labels and body copy
are illustrative only; factual copy and commerce data still come from the
plan, catalog, and final source.

Return `CONCEPT_READY` with the concept asset id and ask for one of:

- approve the direction;
- request a focused revision;
- skip the concept and continue directly to source.

Generate a desktop adaptation only after the mobile direction is approved,
unless the user explicitly requested both outputs together. Use landscape
output and the same visual system rather than inventing a second direction.

## Turn Approval into Production Assets

The concept image is design evidence, never page media and never source.
Record it in `design-concept.md`, not in the manifest's production `assets[]`
slots.

After the concept is approved:

1. Compare it with the plan's asset slots.
2. Reuse verified Shopify and Lexsis assets first.
3. List only the production slots that still need generation.
4. Confirm the paid generation batch when authorization is still required.
5. Generate each real asset with its actual production purpose, aspect, brand
   colors, and suitable reference images.
6. Inspect identity-sensitive output and update the corresponding manifest
   slots to `verified`.

Do not crop the concept into production assets, use the concept URL in page
source, trust product text rendered inside it, or generate replacement product
shots when current Shopify product media exists.

