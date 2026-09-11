# Island wrapper contract

An island supplies behavior inside authored source. Select it through
`references/workflows/island-selection-workflow.md`; author it through
`references/authoring/source-authoring.md`; style it through
`references/authoring/css-and-styling.md`.

## Wrapper responsibilities

- Give each section one stable id and let its wrapper own placement.
- Apply the plan's spacing, type, radius and alignment decisions from
  `references/design-rules.md` A1-A6; island internals do not define page rhythm.
- Keep wrappers transparent over the page background. N2 owns the exhaustive
  exceptions; there is no alternating-background or CTA-band recipe.
- Use the contrast-checked text and control pairings under A7. Muted text uses
  `--lx-text-muted`, not opacity on the primary text color.
- Meet A11's 48px minimum for authored tap targets, including small controls.
  A lower external accessibility floor does not lower the house requirement.
- N10 owns the motion budget. Wrappers are static unless they participate in
  the single plan-named moment or respond to a user action.

## Composition boundary

The page-type contract determines placement and singleton roles. Purchase,
variant and subscription state belongs to the selected commerce island,
not a second custom click handler. Cart V2 is enabled through
`head.use_cart_v2`; it is not an authored cart section.

Use the live schema to discover supported parts and CSS variables. A selector
must start with the owning section id; never paste a page-global part
selector. Preset labels record intent, not frozen props. The styling owner
contains the implementation procedure and conforming examples.
