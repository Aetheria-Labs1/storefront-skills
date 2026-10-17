# Resource templates

A resource template is an ordinary Lexsis page (source, CSS, islands) that
renders for many products or many collections. The store serves it at:

- `/a/lp/products/<handle>` and `/a/lp/collections/<handle>` (app proxy);
- `<custom domain>/products/<handle>` and `<custom domain>/collections/<handle>`.

The URL's handle decides which product or collection the page binds to.
Title, canonical URL, meta description and Product or CollectionPage JSON-LD
come from that resource automatically; do not hand-write them per product.

## When to build a template

Build a template, not one page per product, when:

- the layout should apply store-wide or to a whole group: every PDP, every
  product in a collection, tag, type or vendor, or every collection page;
- the merchant wants one design maintained in one place as the catalog
  changes;
- the layout may be A/B tested later (a route can point at an experiment
  whose variants are template pages).

Build a dedicated page when one product or one collection needs its own
story, offer, proof or copy that would be wrong on its siblings (a launch,
a hero SKU with its own ad traffic). A dedicated published page whose handle
equals the resource handle always wins over a template for that URL.

The plan records the scope as `product template`, `collection template` or
a single page, plus the sample handles used for preview.

## Build it

1. Plan and design the page as usual for its type (the pdp or
   collection-landing page-type contract).
   Copy must read true for every resource the route will cover: no single
   product's claim, review quote or offer in shared template text unless it
   is bound to the resource.
2. Pass `resource_type: "product"` or `"collection"` (and optionally
   `preview_resource_handle`) to `lexsis_pages.compile` and
   `lexsis_page_create.create`. To mark an existing draft, use
   `lexsis_drafts.set_resource_template` with
   `{ page_id, resource_type, preview_resource_handle }`;
   `resource_type: null` unmarks it.
3. Bind content to the resource; never hardcode one:
   - product islands (BuyBox, ProductGallery, StickyBar, QuickAdd and the
     rest) bind to the routed product when `productId` / `product` is
     omitted;
   - CollectionGrid and CollectionSwipe take `"collection": "$resource"`
     (or omit `collection`);
   - page text and media bind with the card-template attributes on any
     element: `data-lx-product`, `data-lx-product-src`,
     `data-lx-product-href`, `data-lx-product-alt`, `data-lx-product-if`,
     `data-lx-product-unless`, and the paths `id`, `handle`, `url`, `title`,
     `type`, `vendor`, `description`, `price`, `compareAt`, `available`,
     `images.N.url`, `images.N.alt`, `metafields.<ns>.<key>`, or
     `tag:<tag>` in conditions. They work on product and collection
     templates (`title`, `description`, `handle`, `url`,
     `images.0.url` resolve to the collection on a collection template).
4. Compile. `resource_template_hardcoded` warns on an island pinned to one
   resource; remove the pin unless that island is intentionally fixed (a
   cross-sell of one accessory).

## Preview against sample handles

Preview at `<renderer>/v/<template slug>?preview=1&resource=product:<handle>`
or `resource=collection:<handle>`. `preview_resource_handle` sets the
default. Review two or three different handles chosen to stress the layout:
the longest title, the product with the most variants or images, one with
few images or no reviews, one sold out; for collections, the largest and a
small or filter-poor collection. The hosted design review's template
checks apply to each.

## Publish, then route

Routes skip unpublished or deleted pages, so publish the template first
through `/publish`. Routing moves live traffic and is a live operation:
show the user the exact route and get explicit approval before
`lexsis_live_ops.resource_route_upsert` with
`{ resource_type, match_kind, match_value, priority, page_id | experiment_id, status }`.

| `match_kind` | `match_value` | Applies to |
|---|---|---|
| `default` | empty | every product or every collection without a better match |
| `handle` | one product or collection handle | that one URL (an override) |
| `collection` | collection handle | products in that collection |
| `tag` | tag | products with that tag |
| `product_type` | product type | products of that type |
| `vendor` | vendor | products from that vendor |

`collection`, `tag`, `product_type` and `vendor` rules match products only;
collection templates route with `default` and `handle`. Routes are unique
per store, resource type, kind and value; upserting the same key updates it.
`status: "paused"` keeps a route without serving it.
`lexsis_live_ops.resource_route_delete` with `{ route_id }` removes one.

## Precedence

For a requested handle, the first match wins:

1. a published, non-template page whose handle equals the resource handle;
2. a `handle` route;
3. rule routes (`collection`, `tag`, `product_type`, `vendor`) by
   `priority`, lower number first (default 100), then the oldest route;
4. the `default` route;
5. nothing: the URL returns 404.

## Verify

1. `lexsis_pages.resource_routes` lists every route with kind, value,
   priority, target and status.
2. `lexsis_pages.resolve_resource` with `{ resource_type, handle }` is a dry
   run: it returns the page or experiment that would serve the handle and
   why (`page`, `handle`, `rule` or `default`), or that the URL would 404.
3. Resolve the sample handles plus one handle each rule should not catch,
   before and after the upsert, and open the live URL for at least one.
