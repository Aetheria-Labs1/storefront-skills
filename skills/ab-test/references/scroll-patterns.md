# Native scrolling

Use the browser's scrolling behavior for galleries, product lists and long
comparison tables. Static structure does not need section JavaScript.

## Horizontal content

Use `overflow-x-auto`, a flex or grid row, and `snap-x snap-proximity` with
`snap-start` on items when snapping aids inspection. Keep a visible cue that
more content exists, preserve keyboard access, and do not require dragging.
A specialist media island is appropriate only when its behavior is needed;
resolve it through `references/workflows/island-selection-workflow.md`.

## In-page navigation

Use native anchors to stable section ids. Page-wide smooth scrolling, if
chosen, belongs in `theme_css` with reduced-motion handling. Apply a
scroll margin for a sticky header instead of calculating document positions.
Never combine mandatory snapping with a second programmatic scroll system.

## Ownership

Do not intercept wheel events, lock the document body, start raw timers, or
query global DOM from section JS. Overlays own their focus and scroll-lock
behavior through the active island; a real custom motion requirement belongs
in `references/animation-system.md`, subject to the house motion budget.
