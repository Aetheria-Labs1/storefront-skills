# Island Preview

The browser runtime hydrates compiled `data-island` markers, not raw
`<lx-island>` authoring tags.

## Build

1. Resolve the live island schema.
2. Confirm active lifecycle status, required props, native variants, styling
   parts, and any headless hooks.
3. Prefer native mode and style only schema-listed parts.
4. Add readable `<lx-island>` source with preview props to
   `lexsis-source.html`.
5. Include a direct `data-lx-island-fallback` child.
6. Dry-run compile the complete canonical source with `page-theme.css`.
7. Require no missing Tailwind candidates.
8. Save the compile response and exact input hashes in
   `compile-artifact.json`.
9. Run:

```bash
python3 skills/visual-page/scripts/build_visual_preview.py \
  compile-artifact.json \
  work/visual-pages/<page-handle>/visual-preview.html \
  --theme-css work/visual-pages/<page-handle>/page-theme.css
```

The builder uses the bundled shell, the exported Lexsis island runtime, and
the compiled section markup. Never hand-author `data-island` or `data-props`.

## Preview Data

Prefer real read-only product and media data. Use direct poster/video sources
and complete product objects when supported. If valid safe data is unavailable,
leave the fallback visible and record `previewMode: "fallback"`.

After opening the preview, require `data-lx-hydration-status="passed"` and
`window.__LEXSIS_PREVIEW_STATUS__.state === "passed"`. Fallback mode is useful
while iterating, but a required production island in fallback mode blocks
visual approval.

An island fallback is local to that island. It never authorizes replacing the
production island with custom controls.

ShoppableVideoFeed can run with real media while using a presentation mode
that does not navigate or write. Commerce and navigation islands should use
read-only props or fallback HTML.

## Preview Boundary

The shell does not add a content-security policy or replace browser network,
form, popup, or link behavior. Keep visual-stage props presentation-focused
and avoid configuring real checkout or external navigation actions.

Real product resolution, add-to-cart, cart totals, and checkout are verified
only on the hosted Lexsis draft.
