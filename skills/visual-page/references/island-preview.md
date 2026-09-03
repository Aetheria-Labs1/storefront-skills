# Island Preview

The browser runtime hydrates compiled `data-island` markers, not raw
`<lx-island>` authoring tags.

## Build

1. Resolve the live island schema.
2. Add readable `<lx-island>` source with preview props.
3. Include a direct `data-lx-island-fallback` child.
4. Dry-run compile the complete visual source.
5. Save the compile response as JSON.
6. Run:

```bash
python3 skills/visual-page/scripts/build_visual_preview.py \
  compile-response.json \
  work/visual-pages/<page-handle>/visual-preview.html \
  --theme-css work/storefront/setup/stores/<store-id>/themes/<theme-id>.css
```

The builder uses the bundled shell, the exported Lexsis island runtime, and
the compiled section markup. Never hand-author `data-island` or `data-props`.

## Preview Data

Prefer real read-only product and media data. Use direct poster/video sources
and complete product objects when supported. If valid safe data is unavailable,
leave the fallback visible and record `previewMode: "fallback"`.

ShoppableVideoFeed can run with real media while using a presentation mode
that does not navigate or write. Commerce and navigation islands should use
read-only props or fallback HTML.

## Preview Boundary

The shell does not add a content-security policy or replace browser network,
form, popup, or link behavior. Keep visual-stage props presentation-focused
and avoid configuring real checkout or external navigation actions.

Real product resolution, add-to-cart, cart totals, and checkout are verified
only on the hosted Lexsis draft.
