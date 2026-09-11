# Source authoring

The compiler owns acceptance of source. House requirements are in
`references/design-rules.md`; CSS is owned by
`references/authoring/css-and-styling.md`. This file owns markup mechanics,
not another style policy or island-selection table.

## Source inputs

Author one source value and pass it directly to MCP. Pass structured `head`,
optional `scripts` and any page-wide `theme_css` separately from the HTML.
`references/source-artifact-workflow.md` owns the direct-input contract and
persisted version evidence; no HTML or CSS file is created.

## Section identity

A section starts at `<!-- section: kebab-case-id -->` and continues to the
next delimiter. Use one matching `<section id="kebab-case-id">` per delimiter.
Ids come from `references/page-types/_checklist-format.md`, including its
suffix convention. Keep ids stable across patches; renaming can break
anchors and version history. Announcement, header, footer and navigation are
ordinary source sections in the declared order, not a hidden renderer shell.

## Island markup

Resolve interactive decisions through
`references/workflows/island-selection-workflow.md`. For the chosen island,
use `<lx-island name="...">` with one readable `application/json` child
containing the props confirmed by its current schema. Use the live schema's
authoring example rather than a static prop map.

Allowed source attributes are `name`, `hydrate`, `class`, `id`, `style`,
and `headless` where supported. Read the hydration default and headless
contract live. A different island's defaults or hooks are not evidence.
Source uses `hydrate`; `data-island`, `data-props` and `data-hydrate` are
compiled renderer markers and are not hand-authored source.

A fallback is one `data-lx-island-fallback` child alongside the JSON child.
It contains readable static information, not a competing purchase handler.
Supported headless behavior is different from fallback content: fetch the
current required hooks, preserve their state contract, and test the result.
Navigation hydration hooks likewise come from the selected live schema.

Cart behavior comes from `head.use_cart_v2` and the published cart profile,
not an authored cart section. Required singleton roles and linked purchase
state are resolved in the island-selection owner.

## Native content

Use semantic HTML for content that does not need an island: disclosures,
comparison tables, static statistics, linked logos and product navigation.
Preserve native keyboard/focus behavior. A radio group needs real labels;
a table needs meaningful headers and an appropriate caption. House A11 owns
control sizing. Native markup is not a license to recreate cart logic.

## Head and external code

- `head.title` contains the real title; approved font stylesheet URLs belong
  in structured `head.fonts`, not CSS imports or section link tags.
- `scripts[]` is for approved integrations and analytics. Animation engines
  use the managed loaders described in `references/animation-system.md`.
- Keep JSON and JSON-LD scripts in their supported HTML locations. Never
  escape a whole section into an HTML string; valid HTML entities in text
  and attribute values remain ordinary HTML.
- Custom motion uses `application/lexsis-motion` under the house budget.
  Follow the managed API contract rather than copying raw timers, global
  DOM access, observers, storage, networking or programmatic clicks into JS.
- Plain top-level section script is compatibility behavior, not a route
  around the compiler's managed-code checks.

## Compile handoff

Write complete source, then follow `references/generation-protocol.md` for
exact-input compilation, repair, draft creation or versioned editing. A clean
compile does not prove visual quality. Hosted design review and production
readiness follow `references/qa-recipe.md`.
