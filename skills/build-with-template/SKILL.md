---
name: build-with-template
description: Create an unpublished Lexsis storefront draft directly from a supplied page-kit or section-template URL. Use when the template is already chosen and visual design approval should be skipped.
---

# Build with a Chosen Template

Require a page-kit or section-template URL, slug, or id. If none is supplied,
ask for it or route a general fast-build request to `/build`.

Read:

- `references/fast-build.md`
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

Treat the supplied template direction as authoritative. Follow
`references/fast-build.md`, skip the visual-concept and design-approval stages,
compile once with at most one targeted repair, create with `publish:false`, and
return `DRAFT_CREATED`.

This skill never publishes live and never upgrades the result to
`DRAFT_READY`; use `/generate` and `/publish` for those outcomes.
