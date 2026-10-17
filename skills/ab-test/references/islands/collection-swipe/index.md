# CollectionSwipe

For `CollectionSwipe`, fetch `lexsis_design.islands` and
`lexsis_design.island_schema` during the decision that needs this behavior.
Use the current authoring example, variants, props, parts, hydration and
headless support; the bundled JSON is a compatibility reference, not a
second source of defaults.

`references/workflows/island-selection-workflow.md` owns selection and
linked state. `references/authoring/source-authoring.md` owns source syntax;
`references/authoring/css-and-styling.md` owns styling. Placement and evidence
come from the selected page-type contract and its domain policies.

## When to use

The mobile view of a live collection: one card at a time, swipe right (or
tap the bag button) to add, swipe left to pass, tap the left or right side
of the photo to step through images, undo the last card. It renders and
fetches nothing at 768px and wider.

Use it only in the same section as a CollectionGrid with
`"hideOnMobile": true`, so desktop gets the grid and mobile gets the deck.
Neither island fetches while hidden. Either one alone leaves a viewport with
no products; the compiler warns with `collection_view_pairing`.

Not as the only collection view, and not for a handful of hand-picked
products. Choose the deck when the catalog is visual and browsed for taste
(fashion, jewellery, home); keep the two-column grid on mobile when shoppers
filter by spec or compare many cards at once.

## Props that carry decisions

- `collection`: the same handle as the paired grid, or `"$resource"` on a
  collection resource template (`references/resource-templates.md`).
- `showFilters`: filter chips above the deck (default on). Filter and sort
  state shares the URL with the grid (`syncUrl`).
- `quickAdd`: a right swipe adds to bag; `false` makes it a "like" only.
  `openCartOnAdd` defaults to `false` (silent add, bag counter updates) so
  the shopper keeps swiping; set `true` only when the plan wants the cart
  after every add.
- `pageSize` (default 12), `initialSort`, `hideSoldOut`, `aspectRatio`,
  `metafields`.
- Labels: `likeLabel`, `skipLabel`, `emptyText`, `endText`, in the brand
  voice and the plan's copy.

## Card template

`<template data-slot="card">` and `<template data-slot="empty-state">` use
the same `data-lx-product*` bindings and paths as CollectionGrid
(`references/islands/collection-grid/index.md`). `<lx-slot name="media">`
receives the tap-through photo viewer. Do not put
`<lx-slot name="quick-add">` in the card: the deck's own controls add to
bag, and the compiler rejects it.

The island owns card motion. Do not animate cards with page CSS transforms;
style with parts and `--lx-swipe-*` tokens.

## Parts

`root`, `toolbar`, `filters`, `filter-group`, `filter-chip`,
`filter-price`, `filter-clear`, `filter-count`, `sort`, `count`, `deck`,
`card`, `card-media`, `card-photo-bars`, `card-body`, `card-title`,
`card-desc`, `card-price`, `compare-price`, `stamp-like`, `stamp-skip`,
`controls`, `like`, `skip`, `undo`, `empty`, `end`, `error`.

## Examples

Desktop grid and mobile deck in one section:

```html
<!-- section: product-grid -->
<section id="product-grid">
  <lx-island name="CollectionGrid">
    <script type="application/json">{"collection":"festive-jewellery","hideOnMobile":true,"filterPlacement":"sidebar"}</script>
  </lx-island>
  <lx-island name="CollectionSwipe">
    <script type="application/json">{"collection":"festive-jewellery","likeLabel":"Add to bag","skipLabel":"Not for me"}</script>
  </lx-island>
</section>
```

Collection template bound to the URL's collection:

```html
<lx-island name="CollectionGrid">
  <script type="application/json">{"collection":"$resource","hideOnMobile":true}</script>
</lx-island>
<lx-island name="CollectionSwipe">
  <script type="application/json">{"collection":"$resource"}</script>
</lx-island>
```

Deck with a merchant card template:

```html
<lx-island name="CollectionSwipe">
  <script type="application/json">{"collection":"festive-jewellery"}</script>
  <template data-slot="card"><li class="xg-card"><div class="xg-media"><lx-slot name="media"></lx-slot></div><p class="xg-name" data-lx-product="title"></p><p class="xg-price" data-lx-product="price"></p></li></template>
</lx-island>
```
