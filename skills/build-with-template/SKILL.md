---
name: build-with-template
description: Create an unpublished Lexsis storefront draft directly from a supplied page-kit or section-template URL. Use when the template is already chosen and visual design approval should be skipped.
---

# Build with a Chosen Template

Require a page-kit or section-template URL, slug, or id. If none is supplied,
ask for it or route a general fast-build request to `/build`.

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
- `references/animation-system.md` when the template contains custom motion
- `references/consumer-behavior-cro.md`
- `references/workflow-intent.md`

Use `lexsis_template_library.get_kit`, `lexsis_design.get_section`,
`lexsis_catalog.get`, `lexsis_design.islands`,
`lexsis_design.island_schema`, `lexsis_asset_library.search`,
`lexsis_brand.context`, `lexsis_brand.get_theme`,
`lexsis_pages.compile`, and `lexsis_page_create.create`.

Use `lexsis_workspace.credits`, `lexsis_assets.capabilities`,
`lexsis_assets.view`, and `lexsis_drafts.asset_generate` only for required
production gaps and only after credit authorization.

Build the page around real imagery, not around colour and copy. Identify the
page type first, then per section decide the media before the copy: catalog
media, then the asset library, then merchant-owned sources. Open every
candidate with `lexsis_assets.view` and run the fit review in
`references/workflows/section-asset-workflow.md` before using it, viewing a
section's set together so it reads as one shoot, so the template's sample
imagery is replaced with viewed catalog or library assets. When a slot cannot
be filled, leave it `planned` and name it in the draft summary so the merchant
can upload the file or authorise generation; never spend generation credits
without that yes, and never substitute a colour band, an emoji row or icon
tiles for a missing image. Re-check the template's island props against the
current schema through `lexsis_design.island_schema` rather than trusting them.

Treat the supplied template direction as authoritative. Follow
`references/fast-build.md`, skip the visual-concept and design-approval stages,
compile once with at most one targeted repair, create with `publish:false`, and
return `DRAFT_CREATED`.

This skill never publishes live and never upgrades the result to
`DRAFT_READY`; use `/generate` and `/publish` for those outcomes.
