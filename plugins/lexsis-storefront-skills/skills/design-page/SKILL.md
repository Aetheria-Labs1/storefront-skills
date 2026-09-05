---
name: design-page
description: Turn an approved one-page storefront plan into canonical Lexsis source and a responsive interactive preview, including the page-specific asset decision.
---

# Design the Page

Create the real page source and its browser-reviewable preview. Do not create
a remote draft or publish.

Read:

- `references/page-layout.md`
- `references/island-preview.md`

Use `lexsis_brand.context`, `lexsis_brand.get_theme`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`, `lexsis_design.guide`,
`lexsis_design.islands`, `lexsis_design.island_schema`,
`lexsis_design.get_section`, `lexsis_asset_library.search`,
`lexsis_catalog.get`, `lexsis_assets.view`, `lexsis_workspace.credits`,
`lexsis_drafts.asset_generate`, `lexsis_asset_upload.import`, and
`lexsis_pages.compile`.
Resolve only unfamiliar argument schemas through exact router/action
discovery.

## Inputs

Use the approved `page-plan.md` and its saved store/theme binding. The plan
defines strategy and section intent; it must not define islands or
implementation details.

If the user explicitly skips `/plan-page`, write a short one-page plan and
record the skip. Never run `/setup` or `/plan-page` automatically.

## Asset Decision

Before composing the page:

1. Read product media from Shopify and search the Lexsis asset library for the
   planned media roles.
2. Inspect identity-sensitive product or creator media.
3. Classify the roles as `available`, `missing`, or `optional`.
4. Present one concise summary of reusable assets, missing assets, and optional
   enhancements.
5. Ask once which missing or optional roles the user wants generated.

For approved generation:

- Prefer Lexsis asset generation.
- If other image-generation tools are available in the current agent context,
  present the available providers and let the user choose before invoking one.
- Generate independent roles in parallel where supported.
- Import externally generated media into Lexsis before production use.
- Use Lexsis icons, supported SVG, or CSS for ordinary interface icons. Image
  generation is for custom artwork, imagery, banners, and illustrations.

If generation is declined or postponed, copy suitable bundled placeholders
into the page workspace. Placeholders are allowed only in the local preview
and cannot pass `/generate`.

## Compose

1. Read the saved brand design and selected theme CSS.
2. Use the template direction from the plan. Fetch selected section source;
   search again only when the plan has no usable template direction.
3. Convert each planned section into responsive layout and copy.
4. Select islands only now, resolve each current active schema, and prefer
   native variants. Use headless mode only with complete required hooks.
5. Write readable `lexsis-source.html` with stable section delimiters.
6. Write global page rules to `page-theme.css`; keep section-specific CSS
   beside its section.
7. Use LX tokens for brand values and compile-time Tailwind utilities for
   layout. Do not use a runtime Tailwind CDN.
8. Use ordinary HTML for static content and schema-valid `<lx-island>` source
   for supported interactions.
9. Keep preview props safe and presentation-focused. Real commerce is tested
   on the hosted draft.

## Compile and Preview

Compile the complete source, CSS, head, scripts, and bindings once. Fix
blocking compiler errors, save the exact response and input hashes in
`compile-artifact.json`, then run:

```bash
python3 skills/design-page/scripts/build_page_preview.py \
  <page-workspace>/compile-artifact.json \
  <page-workspace>/page-preview.html \
  --theme-css <page-workspace>/page-theme.css
```

Inspect 390px and 1280px. Confirm the expected islands hydrate and there is no
overflow, clipping, broken hierarchy, or unusable responsive layout. Tablet,
hosted visual comparison, and real cart behavior belong to `/generate`.

## Approval

Show:

```text
Preview: [path]
Sections: [ordered list]
Interactive components: [islands]
Reused assets: [roles]
Generated assets: [roles]
Temporary placeholders: [roles]
```

On approval, record only final IDs, compact island schema evidence, and source,
theme, configuration, structure, and bundle hashes in the manifest. Do not
store creative explanations or tool transcripts there.

Any later visible source, CSS, copy, layout, island, or asset change returns
the design to `changes-pending-approval`.

## Return

Return the source, theme, preview, compile-artifact paths, sections, selected
islands, asset summary, and `DESIGN_APPROVED`.
