---
name: build
description: Create the fastest useful unpublished Lexsis storefront draft from a prompt, optional template URL, or automatically selected page kit. Use for first versions and rapid iteration; use generate for production-ready QA.
---

# Build a Fast Draft

Create an unpublished draft without requiring the full planning and visual
approval workflow.

Read:

- `references/fast-build.md`
- `references/page-types/_index.md`, then only the matching
  `references/page-types/<type>.md` and its `## Workflow`
- `references/workflows/section-asset-workflow.md` and
  `references/workflows/island-selection-workflow.md`
- `references/authoring/css-and-styling.md` and
  `references/authoring/source-authoring.md`
- `references/assets/generation-policy.md` and
  `references/proof/reviews-sourcing.md`
- `references/animation-system.md` when the request names custom motion
- `references/consumer-behavior-cro.md`
- `references/workflow-intent.md`

Use `lexsis_catalog.list`, `lexsis_catalog.get`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`,
`lexsis_template_library.get_kit`, `lexsis_design.get_section`,
`lexsis_design.islands`, `lexsis_design.island_schema`,
`lexsis_asset_library.search`, `lexsis_brand.context`,
`lexsis_brand.get_theme`, `lexsis_pages.compile`, and
`lexsis_page_create.create`.

Use `lexsis_workspace.credits`, `lexsis_assets.capabilities`,
`lexsis_assets.view`, and `lexsis_drafts.asset_generate` only when existing
media cannot satisfy a required production slot. Confirm before paid
generation unless the user already explicitly authorized it.

Infer the complete request:

- A supplied template or page-kit URL is authoritative.
- Without a template, select the best coherent page kit for `fast-draft`
  intent.
- If the user asks to choose among templates, show the picker and wait.
- If the user asks for a visual mockup before source, route to
  `/design-page`'s concept-first path instead.
- If the user asks to publish live, route to `/publish`; this skill creates
  with `publish:false` only.

Build the page around real imagery, not around colour and copy. Identify the
page type first, then per section decide the media before the copy: catalog
media, then the asset library, then merchant-owned sources. Open every
candidate with `lexsis_assets.view` and run the fit review in
`references/workflows/section-asset-workflow.md` before using it, viewing a
section's set together so it reads as one shoot, so the kit's sample imagery is replaced with viewed catalog or library assets. When a slot
cannot be filled, leave it `planned` and name it in the draft summary so the
merchant can upload the file or authorise generation; never spend generation
credits without that yes, and never substitute a colour band, an emoji row or
icon tiles for a missing image. Resolve islands live through
`lexsis_design.islands` and `lexsis_design.island_schema`.

Follow `references/fast-build.md`. Compile once, permit one targeted repair,
create the draft, and return `DRAFT_CREATED` immediately. Do not run design
critique, hosted QA, commerce QA, hash reconciliation, or full workspace
validation before returning the preview.
