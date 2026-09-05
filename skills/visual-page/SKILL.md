---
name: visual-page
description: Turn an approved storefront plan into a responsive, theme-aware mockup using compiled Lexsis templates and islands. Static fallbacks are limited to isolated preview failures.
---

# Create the Visual Page

Create the real page source and its browser-reviewable preview. Do not prepare
final assets, create a Lexsis draft, or publish.

Read:

- `references/visual-layout.md`
- `references/island-preview.md`

Complete the MCP preflight before reading or changing standard page artifacts.
MCP unavailable means `BLOCKED_LEXSIS_MCP`, not a silent static replacement.
Discover the exact brand, template, design, island, and compile actions needed
by this run.

When the full Lexsis skill pack is installed, also read
`storefront-engine/references/lexsis-design-capabilities.md` for the detailed
LX token, Tailwind, template, and island styling contract. The workflow below
remains complete when that shared reference is unavailable.

## Inputs

Use an approved `page-plan.md` and its saved store/theme binding. If the user
explicitly skips `/plan-page`, write a short plan from the brief and record the
skip. Never run `/setup` or `/plan-page` automatically.

Use existing Lexsis or Shopify media first. When an image is still missing,
copy an appropriate neutral file from `assets/placeholders/` into the page
workspace. Placeholders are for design approval only.

## Load the Design System

1. Read the saved brand design and exact selected theme CSS.
2. Refresh the complete theme with the discovered `lexsis_brand` action when
   the binding is stale or the task needs current theme configuration.
3. Search page kits before custom composition.
4. Fetch the selected section-template source in batches of at most three.
5. Choose one coherent style treatment for the page.
6. Use LX theme tokens for brand values and Tailwind utilities for responsive
   layout.

## Build the Page Source

1. Write readable `lexsis-source.html` with stable section delimiters. This is
   the only editable HTML source used by later skills.
2. Write global tokens and page-wide custom CSS to `page-theme.css`. Keep
   section-specific CSS beside its section in `lexsis-source.html`.
3. Use ordinary HTML for static content.
4. Discover candidate islands, then resolve each selected island's current
   schema, lifecycle, native variants, required props, styling parts, and
   headless hooks.
5. Prefer a native variant and schema-supported `data-part` styling. Use
   headless mode only when the native variants cannot satisfy the approved
   design and all required hooks are implemented.
6. Author supported interactions as `<lx-island>` with schema-valid preview
   props and a readable `[data-lx-island-fallback]` child.
7. Dry-run `lexsis_pages` action `compile` with the complete source,
   `page-theme.css`, manifest head, and manifest scripts. Fix missing Tailwind
   candidates and all blocking compiler errors.
8. Save the exact compile response and its input hashes in
   `compile-artifact.json`, then run
   `scripts/build_visual_preview.py <compile-artifact.json>
   <page-workspace>/visual-preview.html`, passing `page-theme.css` and
   optional preview data files.
9. Save the returned style manifest in `design.compiledStyleManifest`.
10. Load the preview at 390px, 768px, and 1280px. Confirm
    `window.__LEXSIS_PREVIEW_STATUS__.state` and
    `data-lx-hydration-status` report `passed`. Copy the browser-observed
    expected and hydrated instance lists, checked time, and bundle hash into
    `visual.hydrationEvidence`.

The preview shell loads Lexsis's exported island runtime without changing
normal browser behavior. Keep visual-stage props presentation-focused and do
not treat local add-to-cart, checkout, or navigation behavior as certified.
The preview may demonstrate selection, video, carousel, and other client
interactions; commerce behavior is tested on the hosted draft.

For an island that cannot compile or lacks safe preview data, use static
fallback HTML only while iterating and record `previewMode: "fallback"` in the
manifest. The visual cannot be approved while a required production island
remains in fallback mode. Never invent island names or props.

## Complex Islands

Shoppable video, galleries, before/after, and other active islands should use
the real island runtime whenever valid media and props exist. Follow lifecycle
replacement guidance when an interaction is deprecated; for example, use
supported native markup when the schema recommends it.
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

Wait for visual approval. Update the canonical source or page theme first,
recompile, and regenerate the preview after changes. On approval, store the
source, theme CSS, page configuration, structure, and compiled bundle hashes
in the manifest. The preview must be generated from that same bundle.

## Return

Return `source_html_path`, `page_theme_path`, `visual_preview_path`,
`compile_artifact_path`, the approved section list, island preview modes,
template evidence, MCP evidence, and `VISUAL_APPROVED`. The next normal command
is `/asset-prep`.
