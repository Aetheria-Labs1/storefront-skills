# CollectionGrid

For `CollectionGrid`, fetch `lexsis_design.islands` and
`lexsis_design.island_schema` during the decision that needs this behavior.
Use the current authoring example, variants, props, parts, hydration and
headless support; the bundled JSON is a compatibility reference, not a
second source of defaults.

`references/workflows/island-selection-workflow.md` owns selection and
linked state. `references/authoring/source-authoring.md` owns source syntax;
`references/authoring/css-and-styling.md` owns styling. Placement and evidence
come from the selected page-type contract and its domain policies.

## When to use

The product grid of a collection or category page, and any edit with more
than about 24 products. It loads the collection live from the Storefront API
by handle, so every product stays reachable with current price and stock.
Filters (the store's Search & Discovery filters), sort and the loaded page
live in the URL under Shopify theme names (`filter.p.product_type`,
`filter.v.price.gte`, `sort_by`, `page`), so a filtered view can be shared,
reloaded and crawled. "Load more" is a real link to the next `page`, not
endless scroll.

Not for a hand-picked rail of three to eight products (ProductCarousel or
FeaturedCollectionStage) or one product (BuyBox). A small curated edit whose
cards are chosen by hand may stay a static card list from
`references/product-grid.md`.

## Props that carry decisions

- `collection`: the collection handle from `lexsis_catalog.collections`.
  On a collection resource template use `"$resource"` (or omit it); the
  URL's collection binds at render time (`references/resource-templates.md`).
- `filterPlacement`: `chips` (default), `sidebar` (desktop column), `none`.
- `initialSort`, `pageSize` (default 24), `columns` per breakpoint,
  `aspectRatio` (one aspect across every card).
- `quickAdd`: on by default; Quick Add per card, direct add for one variant
  and a picker for several. `openCartOnAdd` opens the cart after each add
  (grid default); set `false` for a silent add that only updates the bag.
- `hideSoldOut`, `showCompareAt` (only with a ledger basis for compare-at),
  `hoverSecondImage`, `showSort`, `syncUrl`, `loadMoreLabel`, `emptyText`.
- `hideOnMobile`: render and fetch nothing below 768px. Use only together
  with a CollectionSwipe in the same section.
- `metafields`: every metafield a card template reads, as `namespace.key`.

## Card and empty-state templates

The default card is image, second image on hover, title, price and Quick
Add. For a merchant card, put `<template data-slot="card">` inside the
island; `<template data-slot="empty-state">` replaces the no-results message.
Card markup binds to each product with read-only attributes:

- `data-lx-product="<path>"` sets text; `data-lx-product-src`,
  `data-lx-product-href` (URL paths `url` or `images.N.url`) and
  `data-lx-product-alt` set attributes.
- `data-lx-product-if` / `data-lx-product-unless` keep or remove a node
  when the path is truthy, or for `tag:<tag>`.
- Paths: `id`, `handle`, `url`, `title`, `type`, `vendor`, `description`,
  `price`, `compareAt`, `available`, `images.0` to `images.3` with `.url`
  or `.alt`, and `metafields.<ns>.<key>` (listed in `metafields`).

Managed slots inside the card: `<lx-slot name="quick-add">` receives Quick
Add and is required exactly once while `quickAdd` is on;
`<lx-slot name="media">` receives a photo carousel of the product's images.

The compiler rejects unknown slots or paths, bindings outside the card
template, metafields missing from `metafields`, `<script>` and inline
handlers, emoji, and hover scale or translate classes. Hover feedback is
colour, shadow or the second-image crossfade.

## Parts

Style through the section id plus parts: `root`, `toolbar`, `filters`,
`filter-group`, `filter-chip`, `filter-price`, `filter-clear`,
`filter-count`, `sort`, `count`, `grid`, `card`, `card-media`, `card-image`,
`card-image-alt`, `card-title`, `card-price`, `compare-price`, `card-tag`,
`card-skeleton`, `quick-add`, `load-more`, `empty`, `error`, plus the
`quick-add-*` picker parts. Column count and aspect come from `columns` and
`aspectRatio` (`--lx-cg-*`), not page CSS.

## Examples

Live collection with chip filters:

```html
<lx-island name="CollectionGrid">
  <script type="application/json">{"collection":"festive-jewellery","pageSize":24,"initialSort":"best-selling","columns":{"mobile":2,"tablet":3,"desktop":4},"filterPlacement":"chips","quickAdd":{"enabled":true}}</script>
</lx-island>
```

Collection template bound to the URL's collection:

```html
<lx-island name="CollectionGrid">
  <script type="application/json">{"collection":"$resource","filterPlacement":"sidebar"}</script>
</lx-island>
```

Merchant card template with a metafield line:

```html
<lx-island name="CollectionGrid">
  <script type="application/json">{"collection":"festive-jewellery","metafields":["lexsis.card_line"]}</script>
  <template data-slot="card"><li class="xg-card"><a class="xg-card-media" data-lx-product-href="url"><lx-slot name="media"></lx-slot><span class="xg-tag" data-lx-product-unless="available">Sold out</span></a><a class="xg-card-name" data-lx-product-href="url" data-lx-product="title"></a><p class="xg-card-line" data-lx-product="metafields.lexsis.card_line"></p><p class="xg-card-price" data-lx-product="price"></p><lx-slot name="quick-add"></lx-slot></li></template>
</lx-island>
```

Desktop grid paired with the mobile deck: see
`references/islands/collection-swipe/index.md`.
