# Interactive Island Preview

Use this only for `/visual-page`.

## Why Compilation Is Required

The browser runtime hydrates compiled `data-island` markers; it does not
hydrate raw `<lx-island>` authoring tags. Keep authoring readable, then call
`lexsis_pages` action `compile` without saving.

Compiled runtime reference:

```html
<div data-island="ShoppableVideoFeed" data-props="..."></div>
```

Do not author that runtime markup by hand. Use the compiler output so prop
escaping remains correct.

## Build the Preview

1. Resolve the island's live schema.
2. Add `<lx-island>` to `visual-source.html`.
3. Include a static direct child marked `data-lx-island-fallback`.
4. Compile the full visual source.
5. Save the compile response as JSON.
6. Run `visual-page/scripts/build_visual_preview.py` to fill the reusable shell
   with:
   - selected theme CSS
   - compiled section wrappers and section CSS
   - the compiled section array
   - optional test cart data, commerce config, and product binding
7. Save the result as `visual-preview.html`.

The shell loads:

```text
https://storefront.trylexsis.com/islands/storefront.css
https://storefront.trylexsis.com/islands/islands.js
```

Then it calls `window.LexsisIslands.hydrateIslands(...)`.

## Preview Data

- Prefer real read-only product and media data.
- Preview copy may be temporary.
- Use direct media URLs and full product objects when supported.
- Never invent unsupported props.
- If valid data is unavailable, leave the fallback visible and record
  `previewMode: "fallback"`.

ShoppableVideoFeed can use the real island with direct poster/video sources.
Use an action mode that does not claim a successful cart write during visual
approval.

## Preview Boundary

The shell does not add a content-security policy or override normal browser
network, form, popup, or link behavior. It is a design preview, not a Shopify
storefront.

Do not configure preview islands with checkout, external navigation, or other
write-oriented actions. Use presentation-focused modes or static fallback HTML
when an island cannot provide a useful visual preview without live commerce.

Selection, playback, galleries, accordions, and other client behavior can be
reviewed locally. Real product resolution, add-to-cart, cart totals, checkout,
and store-origin behavior must be verified on the Lexsis-hosted draft created
by `/generate`.
