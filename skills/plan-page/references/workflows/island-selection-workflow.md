# Island selection workflow

How to choose and configure an interactive component (island) for a section
using the Lexsis MCP. The catalog and every schema live in the MCP
(`lexsis_design.islands`, `lexsis_design.island_schema`); this file is the
procedure for reading them, not a copy. Variant names, prop names, enums and
defaults come from the live schema at the moment of the call, which wins over
the bundled copies under `references/islands/<slug>/schema.json`. Depth:
`references/island-presets.md`, `references/island-patterns.md`,
`references/proof/proof-ledger.md`, `references/workflows/section-asset-workflow.md`,
`references/design-rules.md`. Page-type files (`references/page-types/<type>.md`)
point here from their `Island:` lines.

## 1. Inputs the plan has already read

Signals the plan collected before design; do not call the catalog until they
are in `page-plan.md`.

| Signal | Source | What it decides |
|---|---|---|
| Image count, and which image jobs the media cover | `lexsis_catalog.get` media | gallery family; single-media, thumbnail or grid layouts; lightbox |
| Variant axes and per-value images; price, compare-at, selling plans, inventory | `lexsis_catalog.get` variants | swatch style, resolver, variant-linked media; purchase islands, subscription controls, live stock indicators |
| Review count, average, media flag | `lexsis_catalog.reviews` | review band: none, static quotes, carousel, paginated list |
| Theme tokens, voice, icon decision; nav links | `lexsis_brand.context`, `lexsis_brand.navigation` | preset tone; whether island glyphs are allowed; header and footer islands |
| Markets, payment methods, cart profile | `lexsis_workspace.stores`, `lexsis_cart.get` | payment islands, India rail, `head.use_cart_v2` |
| Video and UGC assets with rights | `lexsis_asset_library.search` | video islands; video items inside galleries |
| Page type, `nav`, `cta.sticky`; page length in 390px screens | plan Page type block, type checklist, wireframe | chrome islands, sticky permission, forbidden sections, return controls |
| The one motion moment, the one bold moment | plan Design direction | every autoplay, ticker, hover-advance, parallax, entry animation |
| Proof ledger and Offer ledger rows | `page-plan.md` | every review, count, logo, badge, countdown, discount, announcement |

## 2. Procedure, per section

### Step 1. Decide whether the section needs an island at all

Static HTML first. An island is justified only when the section needs cart or
variant state, live catalog data (stock, reviews, prices), media behaviour
(thumbnail sync, lightbox, video playback), an overlay, or a form that posts.
Accordions, tabs, stat rows, logo rows, trust strips, comparison tables and
back-to-top controls are HTML (section 4). No job in the plan, no island.

### Step 2. Pick the island from the compact catalog

Call `lexsis_design.islands`. For each candidate read, in this order:

1. `deprecated` and `replacement`: a deprecated island is never chosen for
   new source; use the replacement it names.
2. `when_to_use`: the island's stated job must match the section's job as
   written in the plan, not a nearby job.
3. `when_not_to_use`: any hit disqualifies it. This is where siblings are
   separated (card media away from the PDP gallery, collection add-to-cart
   away from the PDP purchase form, and so on).
4. `combine_with`: the islands it expects beside it. If the plan cannot
   supply a required companion (a purchase form for a sticky bar, a variant
   emitter for a variant-synced gallery), pick a simpler island. `category`
   is the sanity check that the island belongs to the section group.

### Step 3. Open the schema for that one island

Call `lexsis_design.island_schema` for the chosen island only. Read:

- `variants`: the visual modes on offer. The schema says whether the mode is
  carried by a `variant`, `layout`, `render`, `style` or `type` prop.
- `props`: name, type, enum values, default, required flag, description. A
  required prop with no source in the context reads means the island cannot
  be used on this page.
- `defaultHydrate`: the `hydrate` attribute to write on `<lx-island>` unless
  a preset says otherwise.
- `anti_patterns`: concrete misconfigurations; each is a check on the props
  you are about to set.
- `parts` and `css_vars`: what section CSS may target. Never style by class.
- `authoring.examples`: copy data shapes from here, not from memory.
- Unfamiliar action or argument: `lexsis_discover` with the router and
  action; never improvise.

### Step 4. Choose the variant from what the live schema offers

Map the plan's signals to the schema's options. The logic is stable; the
option names are whatever the schema lists today.

View before wiring. When an island takes media (gallery, hero, video, UGC
feed, carousel), open the assets bound to it with `lexsis_assets.view` and
judge them against the section first, per section 1b of
`references/workflows/section-asset-workflow.md`; view a gallery's set
together so the images read as one shoot. Wiring an island to unviewed media
is how a page ends up with mismatched crops and backgrounds.

| Signal | How to read the schema's options |
|---|---|
| 1 image, or 2 to 4 | 1: no gallery island, a static image; 2 to 4: a single-media mode with no thumbnail rail, dots or no indicators, capped height |
| 3 to 9 images | 3 to 5: the default thumbnail mode, thumbnails below or beside, lightbox on; 6 to 9: a rail or collage mode, a collage needing an explicit mobile mode |
| 10 or more images | a grid, masonry or stacked mode; stacked only beside a sticky purchase column |
| Media takes 50 to 60 percent of the desktop viewport beside the purchase form | the split-layout hero gallery, not the compact gallery |
| Colour axis | every value has an image: turn on the gallery's variant-sync option, pair an image-type swatch emitter, first media item is the selected variant; otherwise variant sync stays off and swatches use a colour or text type |
| Two or more option axes | one swatch emitter per axis plus the resolver island, the purchase form's own selector off; at three or more axes the form's built-in selector alone is acceptable |
| Vertical | fashion: tall portrait ratios, on-model first; home: wide ratios, collage or two-column; jewelry: square grid, `contain` fit, macro zoom; packshots on white: `contain` fit |
| Mobile-heavy traffic | the swipe mobile mode; stacked mobile only when the page can absorb the height; click triggers over hover |
| Review count 0 to 4 | no review island: the ledger fallback order at 0; static verbatim quotes with the count as text and no stars at 1 to 4 |
| Review count 5 or more | 5 to 19: the carousel island, grid mode when 3 to 6 fit at once, single-card mode for long bodies, strip mode as a one-line proof near the buy box; 20 or more: the paginated list island with filters on, summary numbers from the API total |
| Video asset exists | a video item inside the gallery (never first, never autoplay) or the standalone player with poster and click-to-play; three or more short clips with rights and tagged products: the shoppable feed |
| Page runs past 2 mobile screens after the buy box, and the type allows sticky | the sticky bar in product mode bound to the primary purchase section; collection mode when the CTA is a destination |
| Selling plans exist; Offer ledger has a tiered-volume row | plans: the toggle when subscription is one option, the plan-card selector when plan cards are the buy pattern, one-time selected by default, never both; tiers: the quantity-tier island as a pure selector when a purchase form owns the CTA |
| Plan names this element as the motion moment or the bold moment | motion moment: autoplay, interval, hover-advance or effect options may be on at the slowest interval allowed, otherwise every motion option is off including defaults that ship on; bold moment: the full-bleed or transparent modes, otherwise the contained modes |

### Step 5. Set props

1. Set only props the context justifies; everything else stays at its schema
   default. A prop with no decision input behind it is a guess.
2. Every review prop (ids, filters, page size, averages, counts) comes from a
   Proof ledger row; averages and totals from `lexsis_catalog.reviews`, never
   a filtered set; stars only beside an average with its count; no endpoint
   prop, the page supplies it at runtime.
3. Every countdown end, stock figure, discount value and announcement message
   comes from an Offer or Proof ledger row. No countdown without an `endsAt`.
4. Every motion prop traces to the plan's single motion moment. Check the
   schema defaults: several islands ship with motion on and must be turned
   off. Feedback motion that answers a user action (add-to-cart confirmation)
   is allowed.
5. Event wiring is explicit. When `combine_with` names an emitter and
   listener pair, set both sides. One emitter per axis; never two islands
   emitting the same event on one page.
6. Island glyphs (stars, checks, badge and social icons) count toward the
   page's single icon set; turn them off by prop or hide the named `parts`.
7. Apply a preset from `references/island-presets.md` when its `use` line
   fits the plan's tone; props verbatim, CSS into the section `<style>`.
   Record every deviation as `islands[].presetOverrides` (a JSON merge patch;
   `null` removes a preset prop). Never edit a preset in place.
8. Cart: every commerce page sets `head.use_cart_v2: true`; never author cart
   islands in page source (`lexsis_cart.get`, `lexsis_drafts.cart_set`,
   `references/cart-composition.md`). One-instance rules from the schemas:
   one purchase form, header island, footer, sticky bar, lightbox,
   auto-triggered overlay, announcement bar, option resolver. Compile with
   `lexsis_pages compile` before the draft; it is the authority on prop shape.

### Step 6. Record the decision

In `page-plan.md`, under the section: the island name and the inputs that
chose it (image count, axes, review band, screen count, motion moment, ledger
rows). In `page-manifest.json` `islands[]`, after the schema is resolved:
`{sectionId, name, schemaVersion, lifecycleStatus:"active", mode, preset,
presetOverrides}` plus the chosen variant and props, in source order.

## 3. Section job to island family

Names only; `lexsis_design.islands` decides which are active today. Wrapper
markup and presets: `references/island-patterns.md`, `references/island-presets.md`.

| Section job | Island family | Note |
|---|---|---|
| `gallery`, `product-hero`, `hero` background media | ProductGallery, ProductHero, HeroMedia | ProductHero for split layouts; both take video items; HeroMedia only as the plan's bold moment |
| `buy-box`, `sticky-cta` | BuyBox, StickyBar | one BuyBox per page; ProceedToCart only for buy-now or bridge pages, never beside BuyBox; StickyBar in product or collection mode, after the purchase section |
| `variant-picker` | VariantSwatches, VariantSelector, OptionResolver | swatches on the PDP, selector on cards and quick views, resolver for multi-axis |
| `quantity-breaks`, `subscription-toggle`, `plan-selector`, `bundle-builder` | QuantityBreaks, SubscriptionToggle, PlanSelector, BundleBuilder | only with the matching Offer ledger row or selling plans |
| `product-grid`, `cross-sell`, `shop-the-look` | QuickAdd, ProductCarousel, FeaturedCollectionStage | QuickAdd per card; the carousel needs 4 or more products |
| `delivery-cutoff`, `payment-options`, `stock-indicator`, `size-guide` | DeliveryEstimate, PaymentOptions, InventoryIndicator, SizeGuide | stock only with a live binding; size guide only with a chart asset |
| `reviews` | ReviewCarousel, ReviewList | by review band; never SocialProofPopup, which the ledger forbids |
| `before-after`, `countdown` | BeforeAfter, CountdownTimer | only with a verified ledger row or `endsAt`; never in the hero; Countdown is a deprecated alias |
| `video`, `shoppable-video` | VideoPlayer, ShoppableVideoFeed | poster and click-to-play; the feed only with rights and tagged products |
| `lookbook`, `ugc-grid` fullscreen; `ingredients` | GalleryLightbox, ImageZoom; IngredientExplorer | one lightbox per page, zoom for one inline detail image; explorer only with per-ingredient data |
| `faq` | none (native details); FAQ is deprecated in the current schema | if the live catalog shows FAQ active, the live catalog wins |
| `press-marquee`, `stats` | none (static linked logo row, static figures); Marquee and StatCards are deprecated in the current schema | logos only with `press-logo-linked` ledger rows, and if the live catalog shows Marquee active only its logos mode qualifies; ledger numbers only, no count-up |
| `email-capture`, `waitlist-form`, `giveaway-entry`, `quiz`, `product-finder` | EmailCapture, Modal (exit-intent wrapper), FunnelRuntime | capture never above the fold on paid landing types, one per page; the funnel needs a published key |
| `announcement`, `header`, `footer` | AnnouncementBar, SiteHeader, Navbar, MobileMenu, Footer | SiteHeader, or Navbar plus AnnouncementBar, never both; MobileMenu never beside either; hydration mode preferred |
| cart | none in page source | `head.use_cart_v2: true`; cart profile islands are injected |

## 4. Deprecated islands in the bundled schema

Choosing one is a failure; re-check `deprecated` in the live catalog per build.

| Deprecated | Replacement named by the schema |
|---|---|
| BackToTop | anchor link with CSS scroll-behavior |
| Carousel | CSS scroll-snap or a specialised media or commerce island |
| CartDrawer | Cart V2 via `head.use_cart_v2` |
| Countdown | CountdownTimer |
| FAQ | native `<details>` / `<summary>` |
| Marquee | CSS animation with static HTML |
| StatCards | HTML/CSS with optional IntersectionObserver |
| Tabs | CSS-only tabs with radio inputs or `<details>` |

## 5. Read the schema, not the docs

Bundled notes lag the schemas; re-check each item against the live schema.

- Motion defaults: ReviewCarousel and HeroMedia ship with autoplay on and
  ProductCarousel with an entry fade; under N10 each is turned off unless it
  is the plan's motion moment.
- StickyBar takes a product object with a variant id, or a collection link,
  plus a show-after target; the sync, selector and quantity options in its
  index note are not in the schema, and it cannot bind a bundle builder total.
- BuyBox takes a product object with variants, not a product id, and those
  variants carry no images, so image swatches are a separate island. Older
  recipes in `references/island-patterns.md` still show product-id props.
- VideoPlayer has no captions or controls prop; captions ride on the media
  object, and click-to-play is simply autoplay off.
- DeliveryEstimate has no pincode input; India pincode delivery is static
  HTML or dropped.
- Sibling islands name the same field differently (`src` in one gallery,
  `url` in the other); copy shapes from `authoring.examples`.
- Older reference files (`references/island-patterns.md` PDP recipes,
  `_contract.md` composition rules, some `vertical-*.md` files) still name
  islands that are not in the catalog (TrustBadgeBar, PDPInfoCards,
  CompareTable, ProductImage, AddToCart, ExitIntent) and still show deprecated
  ones; those blocks are HTML, and the catalog and schema always win over
  prose examples.

## 6. Worked examples

### 6.1 PDP, 5 images, 2 colour variants each with an image

Reads: `lexsis_catalog.get` gives 5 images, one Colour axis with an image per
value, no selling plans, inventory above threshold; `lexsis_catalog.reviews`
gives 47 reviews at 4.6; the plan names no motion moment and 4 mobile screens.

Reasoning: `lexsis_design.islands` routes 3 to 5 images to ProductGallery
(ProductHero's `when_to_use` asks for a split layout the wireframe lacks).
`lexsis_design.island_schema` for ProductGallery: default thumbnail mode,
swipe mobile mode, lightbox on, variant sync on because every colour has an
image. Its `combine_with` names the image-type swatch emitter and the
purchase form with its own selector off, so VariantSwatches and BuyBox
follow with both sides of the event pair set. 47 reviews is the 20+ band:
ReviewList, filters on, numbers from the reviews API. Four related products
with a named relationship: ProductCarousel, all motion off. Long page, sticky
allowed: StickyBar bound to the buy section. Presets:
`productgallery/rail-bottom-light`, `buybox/default-light` (overrides
recorded), `productcarousel/cards-quiet`, `stickybar/product-light`.

### 6.2 Ad landing page, 12 reviews, no video

Reads: one variant, 6 images, 12 long-bodied reviews, no video asset in
`lexsis_asset_library.search`, type forbids capture, nav none, bold moment is
a static hero image.

Reasoning: no header island; the hero is HTML because the plan did not name it
as a full-bleed island moment. Reviews at 12: ReviewCarousel; `island_schema`
shows a single-card mode for long bodies; autoplay off (the default is on);
the rating filter is omitted because no full list exists to link to. BuyBox
in its single-variant mode; DeliveryEstimate inline under the CTA. VideoPlayer
is not opened; the `video` section is dropped and recorded under "Deviations
from the type default". No EmailCapture or Modal. StickyBar allowed; Footer
simple. Presets: `reviewcarousel/single-quiet` with the filter removed via
`presetOverrides`, `buybox/default-light` (compact recorded), `footer/simple-light`.

### 6.3 Bundle page, fixed kit with a tiered-volume offer

Reads: the kit is one Shopify product with one variant and 4 images; the
Offer ledger holds a bundle saving and a tiered-volume row (1, 2, 3 sets);
`lexsis_catalog.reviews` gives 9 set-level reviews; nav minimal.

Reasoning: `bundle-kit.md` routes a fixed kit to a hero gallery plus purchase
form, not the builder. ProductHero in its split mode with a thumbnail rail,
motion off. QuantityBreaks with three ascending tiers, plain labels (no
"BEST VALUE", rule N9), its own CTA off and its emit flag on; `combine_with`
names BuyBox as the listener, so BuyBox gets its listen flag and the
single-variant mode. Nine long reviews: ReviewCarousel single-card mode,
autoplay off. Savings math is HTML from the ledger. StickyBar skipped on a
short page. Were the kit build-your-own, BundleBuilder would replace hero and
purchase form, QuantityBreaks would go (no builder listener for its event),
and the sticky running total the type file asks for is recorded as a
deviation (section 5). Presets: `producthero/split-rail-light`,
`buybox/default-light` (overrides recorded), `reviewcarousel/single-quiet`,
`siteheader/minimal-light`, `footer/simple-light`.
