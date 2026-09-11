# Collection landing

One category or curated collection: a short heading, a filterable grid and
the cards as the call to action. Visitors arrive from the header nav, a
category search ("women's running shoes"), Google Shopping or a category ad,
solution-aware and comparing. The page's job is product finding: get the
shopper to the right card in as few filter taps as possible, then to the PDP
or a quick-add. Baymard's list-design research puts the spread between good
and poor list design at up to 400% in product-finding success
(https://baymard.com/learn/ecommerce-category-page). Depth for the grid and
filter UI lives in `references/generate-collection.md` and
`references/product-grid.md`; this file is the contract.

## Identify it

Signals in the brief: "collection", "category", "shop all", "PLP", "browse",
a named category, six or more SKUs the shopper self-selects, an ad promoting
a category rather than a SKU.

Near neighbours:

- `homepage`: the whole store; if one category is named, this type (index
  tie-break).
- `gift-guide`: grouped by recipient or budget for a giver; a collection is
  grouped by product attributes for the buyer.
- `sale-clearance-flash`: more than five products at reduced prices in a
  window; a collection may contain some compare-at items but has no window.
- `lookbook-shop-the-look`: imagery-led, looks not filters; choose it when
  context drives the purchase and the catalogue is fashion or home.
- `bundle-kit`: two or more products sold as a set with savings math.

## Anatomy

Sections between chrome: 5 to 8. Intro copy 100 to 300 words; the grid does
the rest.

1. `header` (mandatory). Full navigation with a visible search field and a
   breadcrumb (Home, Collections, Name). RESEARCH: 22% of sites hide search
   (https://baymard.com/blog/ecommerce-homepage-ux).
2. `hero` (mandatory). Collection title in the shopper's words, one or two
   sentences, no taller than 200px at 390px and 300px at 1280px
   (`references/generate-collection.md`). Subcategory tiles sit here when
   subcategories exist. RESEARCH: 76% of sites fail to show subcategory
   navigation above the grid
   (https://baymard.com/blog/current-state-product-list-and-filtering).
3. `qualifier` (recommended; conditional: solution-aware search traffic).
   A 120 to 200 word "how to choose" intro naming the two or three
   attributes that matter; links to the filters.
4. `product-grid` (mandatory). Sticky filter and sort bar with five
   essential filters (price, type, rating, size, colour) plus
   category-specific ones, applied-filter chips, mobile bottom sheet with
   "Show N results"; two cards per row on mobile; each card carries image
   with a second image on hover or swipe, title, price and compare-at,
   rating with count when reviews exist, colour swatches, quick-add for
   single-variant products and "Choose options" for multi-variant; "Load
   more" with a total count. Observed: Mamaearth's collection cards carry
   benefit bullets, rating and count, price and add-to-cart
   (internal teardown audit, 2026-09-10).
5. `offer` (conditional: a verified offer row exists). One mid-grid
   promotional card after 6 to 8 products, visually distinct from product
   cards, one CTA; never a second competing banner.
6. `trust-bar` (recommended). Shipping threshold, returns window, warranty
   or certifications as facts, one row below the grid.
7. `about` (recommended). Category description and SEO copy at the bottom,
   100 to 200 words, in the shopper's vocabulary; correct for UX and fine
   for search.
8. `faq` (conditional: the category has fit, sizing, care or compatibility
   questions in support data). Three to five questions.
9. `email-capture` (mandatory). One field at the end: new arrivals or
   restocks for this collection; no incentive claim without an offer row.
10. `footer` (mandatory).

## Workflow

### Context reads
1. `lexsis_catalog.list` for the collection: product count (decides "Load
   more" at 12 or more), price range, option axes for filters (size, colour
   with hex, type, tags), compare-at prices with their ledger basis,
   inventory per variant, media count per product. `lexsis_catalog.get` per
   product: first media item as the card identity image, second media item
   as the swipe image, variant images for swatches. Record products without
   an identity image for the merchant message.
2. `lexsis_brand.navigation` for header links, the breadcrumb path and
   subcategory links; `lexsis_brand.brand_kit` for tokens, voice and banned
   phrases; `lexsis_brand.context` for the `theme_id`.
3. `lexsis_catalog.reviews_status`, then `lexsis_catalog.reviews` per
   product for the card average and count; stars only at 5 or more reviews
   per product (`references/proof/reviews-sourcing.md`, band table).
4. Policy page URL for the trust-bar facts as `policy-fact` ledger rows
   (`references/proof/proof-ledger.md`); the offer ledger for the one
   mid-grid promo card (`references/offers/offer-ledger.md`).
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`, one call
   each for `banner`, `hero`, `lifestyle`, `product-shot`; then semantic
   "<collection> in use"; view candidates with `lexsis_assets.view`
   (`references/assets/asset-sourcing-sequence.md`).
6. `lexsis_capture.form_schemas` for the email capture; support data for
   FAQ questions (fit, sizing, care, compatibility).
7. `lexsis_design.islands` for the active catalog; `lexsis_workspace.credits`
   only if a promo `card_bg` is planned
   (`references/assets/generation-policy.md`).

### Section by section
Media per section follows `references/workflows/section-asset-workflow.md`:
when nothing covers a slot, tell the merchant what is missing (job, aspect,
count), offer upload via `lexsis_asset_upload.upload` or generation where the
purpose is ALLOW or ASK in `references/assets/generation-policy.md`, and skip
or merge the section only when the merchant chooses; a fast draft uses the
closest existing asset or leaves the slot `planned` and lists every gap in the
plan and the draft summary. No asset is used sight unseen: every candidate is
opened with `lexsis_assets.view` and judged against the section per section 1b
of that file (subject, crop to the slot aspect, a quiet area for the copy, the
lighting and styling of the neighbouring slots, the plan's palette, no
baked-in text, watermark or overlay); candidates for one grid, set or lookbook
are viewed together so the set reads as one shoot, and a generated asset is
viewed the same way after it returns. Islands follow
`references/workflows/island-selection-workflow.md`: the lines below name the
island and the inputs; variants and props are resolved live from
`lexsis_design.island_schema`, with autoplay, hover-advance and entry motion
off unless the plan names that motion moment (N10). Grid and card depth is in
`references/generate-collection.md` and `references/product-grid.md`; copy
ceilings follow `references/anti-patterns/copy-anti-patterns.md`.

**`header`**
- Purpose: full navigation with a visible search field and a breadcrumb.
- Media: logo from the brand kit.
- Island: SiteHeader (one verified shipping fact in the strip) or Navbar;
  links from `lexsis_brand.navigation`; the breadcrumb is HTML under the
  nav; resolve from `lexsis_design.island_schema`; preset
  `siteheader/sticky-light`.
- Copy: nav labels; breadcrumb Home, Collections, Name.
- Decide with: the navigation result.

**`hero`**
- Purpose: the collection title in the shopper's words, one or two
  sentences, subcategory tiles when subcategories exist; no taller than
  200px at 390 and 300px at 1280.
- Media: treatment `typographic`
  (`references/assets/image-jobs-by-page-type.md`, section 5); a photograph
  beside or behind the title only within the height cap: library `banner`,
  then `hero`, then a catalog lifestyle image. Subcategory tiles want one
  `context` image each from library `lifestyle` or the subcollection's first
  product identity image. Generation: none (a 200px band gains nothing from a
  backdrop). Missing tile images: tell the merchant (context per subcategory,
  one aspect, count) and offer upload; if skipped, tiles become text links,
  never icon tiles. No-go: a hero that pushes the first card row below the
  fold; an autorotating banner. View every candidate with `lexsis_assets.view`
  and run the section fit review; view any banner or tile beside the first
  card row so backgrounds agree.
- Island: none; HeroMedia is not used (its default height is a full
  screen against the cap).
- Copy: H1 6 words or fewer ("Running shoes for wide feet"); one or two
  sentences.
- Decide with: subcategory count from navigation; hero height measured in
  the hosted draft at 390.

**`qualifier`** (conditional: solution-aware search traffic)
- Purpose: a 120 to 200 word "how to choose" intro naming the two or three
  attributes that matter, linking to the filters.
- Media: outside the loop as an opening text line; one `detail` image from
  catalog media only when it explains an attribute (a sole, a weave). View
  every candidate with `lexsis_assets.view` and run the section fit review;
  view the tile images together so lighting, backgrounds and crops agree.
- Island: none.
- Copy: grade 6 to 8, under 200 words in a 60ch measure; each attribute a
  link to its filter.
- Decide with: the traffic source in the brief.

**`product-grid`**
- Purpose: filterable, sortable grid with the cards as the CTA.
- Media: yes; job `identity` per card from catalog media, one aspect (3:4 or
  1:1) across every card, second image on hover or swipe, `swatch` chips as
  CSS from catalog hex when colour variants exist. Generation: none ("needs a
  real photo"). Missing: list the products without an image and offer upload;
  if skipped, those cards leave and the deviation is recorded. No-go:
  generated or stock products; mixed aspects (SS10); a countdown on a card.
  View every candidate with `lexsis_assets.view` and run the section fit
  review; view the grid images together so lighting, backgrounds and crops
  agree.
- Island: the card composition from `references/product-grid.md` (there is
  no grid island) with QuickAdd per card; decide direct add or picker from
  the variant axes; sold-out variants visible and disabled; the filter and
  sort bar, applied-filter chips, mobile bottom sheet and "Load more" with
  the total count are HTML controls; InventoryIndicator on a card only with
  a live variant binding; FeaturedCollectionStage only for a "featured"
  rail of three to eight highlights above the grid; motion off; resolve
  from `lexsis_design.island_schema`; preset
  `inventoryindicator/badge-outline` for the live badge.
- Copy: card line under 12 words; badges "New", "Best seller", "Low stock"
  only from data; filter labels in customer language.
- Decide with: product count, option axes, image count per product, review
  band per product, live inventory availability.

**`offer`** (conditional: verified offer row; after six to eight products)
- Purpose: one mid-grid promotional card, visually distinct, one CTA.
- Media: yes; a bundle card wants `included-items` or the bundle's identity
  image from catalog media; a threshold or subscribe card wants a `context`
  image from library `lifestyle` or `banner`. Generation: `card_bg` (ALLOW)
  only behind a real product cut-out. Missing: tell the merchant (one image,
  card aspect) and offer upload or `card_bg` with a cut-out; if skipped, the
  offer terms sit in the trust-bar as a fact. No-go: an accent-coloured text
  card (N8); a percentage pill (N9); a second competing banner. View every
  candidate with `lexsis_assets.view` and run the section fit review before
  use.
- Island: none; QuickAdd on the bundle SKU when the card sells one; resolve
  from `lexsis_design.island_schema`.
- Copy: one sentence and one CTA; 20 words.
- Decide with: the offer-ledger row and the grid length (one card per six
  to eight products, one offer per page).

**`trust-bar`** (recommended)
- Purpose: shipping threshold, returns window, warranty or certification as
  facts, one row below the grid.
- Media: policy facts stand without an image; certification marks only as
  issuer artwork with a ledger row
  (`references/proof/trust-badges-certifications.md`); icons only from the
  page's single inline SVG set. No-go: icon tiles, generated badges (GN5).
- Island: none.
- Copy: three facts, 8 words each.
- Decide with: `policy-fact` ledger rows from the policy URL.

**`about`** (recommended)
- Purpose: category description and search copy at the bottom, 100 to 200
  words.
- Media: yes where it exists: one `context` or `in-use` image from library
  `lifestyle` or catalog media beside the copy in a split layout. Generation:
  none. Missing: offer upload; if skipped, the text runs alone in a 60ch
  measure under 200 words. View every candidate with `lexsis_assets.view` and
  run the section fit review before use.
- Island: none.
- Copy: shopper vocabulary, grade 6 to 8, no filler ("curated",
  "handpicked").
- Decide with: library `lifestyle` count for this category.

**`faq`** (conditional: fit, sizing, care or compatibility questions in
support data)
- Purpose: three to five questions.
- Media: no.
- Island: none; native `<details>` and `<summary>` (the FAQ island is
  deprecated).
- Copy: answer in the first sentence, 60 words each.
- Decide with: support data.

**`email-capture`**
- Purpose: new arrivals or restocks for this collection, one field.
- Media: a card image from the grid beside the form; the form alone is the
  object when none is spare (N8).
- Island: EmailCapture, one per page, or the Footer newsletter layout
  (never both); incentive only with a `first-order` row; resolve from
  `lexsis_design.island_schema`; preset `footer/newsletter-split-light` in
  the footer case.
- Copy: one line and one field.
- Decide with: `lexsis_capture.form_schemas` and the offer ledger.

**`footer`**
- Purpose: policies, payment marks, contact.
- Media: logo; payment marks only as issuer artwork.
- Island: Footer with columns from `lexsis_brand.navigation`; resolve from
  `lexsis_design.island_schema`; preset `footer/columns-dark`.
- Decide with: the navigation result.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` per card, second images, swatch hex | subcategory `context` tiles, a promo-card image | reuse a product's lifestyle media as the tile; generate `card_bg` (ALLOW) behind a real cut-out or `product_composite` for `context`; ask the merchant to upload tile and promo images; text links or no promo card only on the merchant's call |
| asset library | `banner` for the short hero, `lifestyle` for tiles and the about block | category-specific lifestyle | semantic query, then ask the merchant to upload; the hero stays typographic either way |
| generation | backdrops, textures, composites only | product, people, results, logos, text | never; these are "needs a real photo" in the merchant message |

With minimal assets the page is a header with search, a typographic title, the
filter bar, the real catalog grid with quick add, three policy facts, an email
field and a footer; zero generated assets is the normal outcome, four is the
ceiling, and every missing card or tile image is listed in the plan and the
draft summary with upload, generate or skip. Every asset, found or generated,
was viewed and passed the section fit review before use.

## Above the fold (390px)

In order: compact header with search; breadcrumb; H1 and one line; the
filter and sort bar; the first row of two cards with image, title and price.
The grid is the page. Observed collection recipe: promo bar, filter chips,
result count, first cards (internal teardown audit, 2026-09-10).

Must not appear: a hero taller than 200px, an autorotating carousel, a
countdown on a card, a popup, a promotional banner that pushes the first
cards below the fold ("a navigation failure dressed as a marketing win",
Baymard).

## Proof

Modules: 1 to 2. Proof lives on the cards and in one facts row.

- `policy-fact` (required): shipping threshold, returns window, warranty in
  the `trust-bar`, sourced from the policy page URL
  (`references/proof/proof-ledger.md`).
- `review-summary` on every card that has 5 or more reviews: average to one
  decimal plus count; hide stars below 5 reviews.
- `stock-count` badges on cards only from a live inventory binding
  (RESEARCH: PLP scarcity badges +3% in Cro Metrics' portfolio,
  https://crometrics.com/blog/urgency-that-actually-works/).
- Never: `social-proof-popup`, `live-viewer-count`, `press-logo-unlinked`,
  a collection-level testimonial carousel.

Zero-review store: the trust-bar alone; cards show no stars
(`references/proof/reviews-sourcing.md`).

## Offer and CTA

- CTAs: the cards. Quick-add pattern `add-to-cart` ("Add to cart", "Add to
  bag" for fashion and beauty); multi-variant products link to the PDP.
  At most one standalone CTA, inside the mid-grid `offer` card. No sticky
  CTA button; the filter bar is what sticks.
- Price reveal: price on every card in the first screen; compare-at as
  struck text only with a ledger basis; never a "% OFF" pill (design-rules
  N9).
- Urgency: verified only. Live stock badges are allowed; no countdowns.
- Offer types that fit: `none`, `free-shipping` threshold in the trust-bar
  and one promo card, `bundle` or `bogo` promo card, `tiered-volume` for
  consumables, `subscribe-save` promo card, `first-order` in the email
  capture only when the code exists, `gwp`, `bnpl`, `loyalty`.
- Offer types that do not fit: `percent-off` and `fixed-off` across the
  collection (that is `sale-clearance-flash`), `flash-sale`, `clearance`,
  `mystery`, `pre-order-price`, `price-lock`, `referral`, `trial-sample`,
  `student-military`, `charity`, `bundle-decoy`.
- One promo card per 6 to 8 products, one offer per page
  (`references/offers/offer-ledger.md` rule 6).

## Imagery

Required job: `identity` per product from catalog media, one aspect ratio
across all cards (3:4 or 1:1), `object-fit: cover`. Recommended: `in-use` or
on-model as the first card image where the vertical warrants it, second image
as the alternate, `context` for subcategory tiles, `variation` swatches from
catalog hex, `swatch` when colour variants exist.

Hero treatment: `typographic`, title and one line; a photograph may sit
behind or beside the title only within the height cap. Video optional and
never in the hero. Minimum 6 image slots (cards). RESEARCH: 80% of sites show
fewer than three thumbnails per list item; give each card a second image
(https://baymard.com/blog/current-state-product-list-and-filtering). No
generated product imagery; existing catalog media wins
(`references/assets/image-jobs-by-page-type.md`).

## Copy

Framework: AIDA-lite in the intro (guide the browser to a filter and a
click); FAB micro-copy on badges and card lines.

- H1 in the shopper's search words, 6 words or fewer ("Running shoes for
  wide feet").
- Intro 100 to 300 words total across `qualifier` and `about`; grade 6 to 8.
- Card lines under 12 words, concrete (fabric, size range, serving count).
- Badges: "New" (publish date), "Best seller" (orders data), "Low stock"
  (live) only; no "Hot", "Trending", "Must have".
- Filters labelled in customer language ("Fit: relaxed, slim"); price filter
  shows the range with unit price where volumes vary.
- Vocabulary: no superlatives without a proof row; no "curated" or
  "handpicked" as filler.

## Never

- Never let the hero push the first product row below the fold at 390px.
- Never hide "on sale" inside the price filter; make it a filter of its own.
- Never ship a filter that silently returns zero results without saying so.
- Never omit price from a card or hide it behind hover.
- Never show more than one promotional card per 6 to 8 products or two
  competing banners.
- Never use pagination or endless scroll; "Load more" with a total count.
- Never mix card aspect ratios.
- Never place a countdown on a card (observed anti-pattern: Mamaearth's
  timer on one of four cards).
- Never write the category description at the top as a wall of text.
- Never render stars on a card with fewer than 5 reviews.
- Never send cold paid social traffic here; category ads land here, story
  ads do not (OPERATOR: MHI,
  https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/).

## Examples

- Mamaearth Onion Range, https://mamaearth.in/collections/onion-range:
  filter chips by product type, result count, cards with benefit bullets,
  rating and count, price and add-to-cart; footer certification badges.
- Blue Tokai coffee subscriptions,
  https://bluetokaicoffee.com/collections/subscriptions: numbered benefit
  strip above the grid, tasting notes on cards, "Limited release" and "Sold
  out" states inline.
- REI category pages, cited by Baymard as best in class for subcategory
  navigation and filtering (https://baymard.com/learn/ecommerce-category-page).

## Checklist

```json
{
  "page_type": "collection-landing",
  "aliases": ["collection page", "category page", "PLP", "product listing", "shop all", "curated edit"],
  "funnel_stage": ["mof"],
  "awareness": ["solution-aware"],
  "traffic": ["organic", "direct", "google-search", "google-shopping"],
  "sections": { "min": 5, "max": 8 },
  "mandatory_sections": ["header", "hero", "product-grid", "email-capture", "footer"],
  "recommended_sections": ["qualifier", "trust-bar", "about", "offer", "faq"],
  "forbidden_sections": ["countdown", "buy-box", "dateline", "hook", "agitation", "offer-bridge", "us-vs-them"],
  "nav": "full",
  "price_above_fold": "required",
  "cta": { "min": 0, "max": 1, "first_after_section": 0, "sticky": "forbidden", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 1, "max_modules": 2, "required_kinds": ["policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity"], "hero": "typographic", "video": "optional", "min_images": 6 },
  "copy_framework": ["aida", "fab"],
  "offer_compat": { "allowed": ["none", "free-shipping", "bundle", "bogo", "tiered-volume", "subscribe-save", "first-order", "gwp", "bnpl", "loyalty"], "forbidden": ["percent-off", "fixed-off", "flash-sale", "clearance", "mystery", "pre-order-price", "price-lock", "referral", "trial-sample", "student-military", "charity", "bundle-decoy"] },
  "urgency": "verified-only"
}
```

## Sources

- internal research audit (2026-09-10) section 5 block 19; section 2 row 19.
- internal research audit (2026-09-10) teardowns 31, 32 and Part D.
- internal research audit (2026-09-10) sections 1.2 and 13.
- internal research audit (2026-09-10) sections 1.1, 1.2, 3.
- `references/generate-collection.md`, `references/product-grid.md`.
- Baymard category page: https://baymard.com/learn/ecommerce-category-page
- Baymard product lists and filtering: https://baymard.com/blog/current-state-product-list-and-filtering
- Baymard homepage UX (search visibility): https://baymard.com/blog/ecommerce-homepage-ux
- Baymard applied filters: https://baymard.com/blog/how-to-design-applied-filters
- NN/g homepages and listing pages: https://www.nngroup.com/articles/ecommerce-homepages-listing-pages/
- Cro Metrics urgency portfolio: https://crometrics.com/blog/urgency-that-actually-works/
- MHI landing page vs product page: https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/
