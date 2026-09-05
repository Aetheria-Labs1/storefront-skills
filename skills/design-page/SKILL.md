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
4. Read the compact island catalog and select only the likely interactive
   components. Do not fetch every full schema in advance.
5. Write a rough but complete `lexsis-source.html` with stable section
   delimiters, minimal island props, and the documented examples as a starting
   point.
6. Write global page rules to `page-theme.css`; keep section-specific CSS
   beside its section.
7. Use LX tokens for brand values and compile-time Tailwind utilities for
   layout. Do not use a runtime Tailwind CDN.
8. Compare explicit `NEVER`, `must`, and `non-negotiable` rules in the saved
   brand design with matching theme tokens. On a direct contradiction, return
   `THEME_CONTEXT_CONFLICT` with both values. Do not silently choose one.
9. Use ordinary HTML for static content and `<lx-island>` source for supported
   interactions. Use headless mode only with complete required hooks.
10. Keep preview props safe and presentation-focused. Real commerce is tested
   on the hosted draft.

## Compile and Preview

Compile the rough complete source, CSS, head, scripts, and bindings early. The
compiler is the authoritative compatibility check.

1. Use `validation_errors` as the work list.
2. Fetch a full island schema only for an island named by an error or when a
   required behavior remains unclear.
3. Fix the source while preserving the planned composition.
4. Recompile until blocking errors are clear.
5. Save the exact clean response and input hashes in `compile-artifact.json`.

Build the preview with the script bundled beside this skill. Resolve its path
from the loaded skill directory rather than assuming the repository is the
current working directory:

```bash
python3 <design-page-skill>/scripts/build_page_preview.py \
  <page-workspace>/compile-artifact.json \
  <page-workspace>/page-preview.html \
  --theme-css <page-workspace>/page-theme.css
```

Show the first compiled preview as soon as the section structure and responsive
hierarchy are recognizable. Label it `ROUGH_PREVIEW`; asset polish and final
validation may continue after the user can see the direction.

Inspect 390px and 1280px. Confirm the expected islands hydrate and there is no
overflow, clipping, broken hierarchy, or unusable responsive layout. Tablet,
hosted visual comparison, and real cart behavior belong to `/generate`.

The local hydration check must respect each island's strategy:

- `immediate` must hydrate during initial readiness.
- `visible`, `idle`, and `interaction` may remain pending until their trigger.
- Browser QA should scroll through visible islands and exercise interaction
  islands before final approval.

If browser automation cannot access the preview, return
`DESIGN_PREVIEW_READY_QA_PENDING` with the preview path and the checks that still
need manual confirmation. Never record hydration as passed without evidence.

When a store has no usable logo image, use an accessible text wordmark or plain
HTML header for the local design. Do not substitute a product image or generic
logo placeholder.

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
