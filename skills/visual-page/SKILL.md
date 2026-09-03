---
name: visual-page
description: Turn an approved storefront plan into a responsive visual mockup. Uses real Lexsis islands in a safe local preview when possible and placeholders only when data or runtime support is unavailable.
---

# Create the Visual Page

Create the design-stage mockup only. Do not prepare final assets, create a
Lexsis draft, or publish.

Read:

- `references/visual-layout.md`
- `references/island-preview.md`

## Inputs

Use an approved `page-plan.md` and its saved store/theme binding. If the user
explicitly skips `/plan-page`, write a short plan from the brief and record the
skip. Never run `/setup` or `/plan-page` automatically.

Use existing Lexsis or Shopify media first. When an image is still missing,
copy an appropriate neutral file from `assets/placeholders/` into the page
workspace. Placeholders are for design approval only.

## Build the Mockup

1. Write readable `visual-source.html` with stable section delimiters.
2. Use ordinary HTML for static content.
3. Before adding an interactive component, resolve its current active schema
   with `lexsis_design` action `island_schema`.
4. Author supported interactions as `<lx-island>` with schema-valid preview
   props and a readable `[data-lx-island-fallback]` child.
5. Dry-run `lexsis_pages` action `compile` on the complete visual source.
6. Save the compile response and run
   `scripts/build_visual_preview.py <compile-response.json>
   <page-workspace>/visual-preview.html`, passing the selected theme CSS and
   optional preview data files.
7. Load the preview at 390px, 768px, and 1280px.

The preview shell loads Lexsis's exported island runtime without changing
normal browser behavior. Keep visual-stage props presentation-focused and do
not treat local add-to-cart, checkout, or navigation behavior as certified.
The preview may demonstrate selection, video, carousel, and other client
interactions; commerce behavior is tested on the hosted draft.

For an island that cannot compile or lacks safe preview data, use static
fallback HTML and record `previewMode: "fallback"` in the manifest. Never
invent island names or props.

## Complex Islands

Shoppable video, galleries, before/after, accordions, and similar islands
should use the real island runtime whenever valid media and props exist.
BuyBox and other commerce islands may render with preview data, but real
variant/cart behavior is tested later on the hosted draft.

## Approval

Show:

```text
Visual mockup: [path]
Store/theme: [names]
Sections: [ordered list]
Interactive previews: [islands]
Static fallbacks: [islands]
Temporary assets: [list]
```

Wait for visual approval. Update the source first, recompile, and regenerate
the preview after changes.

## Return

Return `visual_source_path`, `visual_preview_path`, the approved section list,
island preview modes, and `VISUAL_APPROVED`. The next normal command is
`/asset-prep`.
