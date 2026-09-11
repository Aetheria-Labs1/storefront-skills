# Product detail page

The store's own page for one product: gallery and buy box first, then the
evidence that supports the price, then breadth of reviews and objections.
Shoppers arrive product-aware or most-aware from organic search, brand search,
email, navigation or a Shopping feed, and their job is to choose a variant and
add to cart. The page sells inside full store context; it does not re-educate.
Implementation depth (island recipes, per-vertical modules) lives in
`references/generate-pdp.md`, `references/island-patterns.md` and
`references/vertical-*.md`; this file is the contract.

## Identify it

- Brief says "product page", "PDP", "product detail", names one SKU with
  variants, and traffic is organic, brand search, email, navigation or
  Google Shopping.
- The visitor already knows the product or the category and wants to
  confirm and buy (`references/consumer-behavior-cro.md` mode "confirm").
- Near neighbours:
  - `pdp-hybrid-landing`: same buy mechanics, no navigation, one goal, paid
    traffic. Choose hybrid whenever traffic is paid and the brief wants one
    goal.
  - `ad-landing-page`: single story, single CTA, product has few variants.
  - `bundle-kit`: two or more products sold as a set.
  - `subscription`: the recurring plan is the page's subject, not one option
    in the buy box.
  - `restock`: the product sold out and is back; proof exists from prior
    reviews.
- RESEARCH, practitioner averages: product pages beat landing pages for hot
  and branded traffic (cart abandoners 7.2% vs 6.5%; branded search 6.8% vs
  5.1%) and lose for cold traffic (2.4% vs 3.8%)
  https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/ . Do not
  send cold paid social to this type.

## Variants

- **Search-intent PDP** (Google Shopping, PMax, transactional search). Title,
  price, currency, availability and the first gallery image match the feed;
  the feed variant is pre-selected from the URL; Product and Offer JSON-LD sit
  in the initial HTML; no interstitial covers product details; shipping cost
  and delivery date sit beside the buy box. LAW, Google Merchant Center
  landing-page requirements https://support.google.com/merchants/answer/4752265
  and https://support.google.com/merchants/answer/7331077 . Tone and section
  order for search intents: `references/traffic-source-google.md`.
- **India commerce rail** (market list includes IN). Conditional sections
  `pricing-mrp`, `delivery-cutoff-pincode`, `payment-options-india`,
  `legal-regulatory` appear as described in Anatomy. Observed on 9 of 9
  Indian PDPs in the teardowns; pincode check on 4 of 9; EMI, BNPL or COD
  line on 5 of 9 (internal teardown audit, 2026-09-10).
- **Cost-per-use PDP** (consumables, meal replacements, supplements). A
  per-serving, per-meal or per-day line sits under the price only when the
  arithmetic is exact and the label states the servings (Huel "$2.65 per
  meal", Mamaearth "₹1.11/ml"). RESEARCH: Gourville 1998 per-day framing
  https://doi.org/10.1086/209517 ; never on one-time goods over the Rule-of-100
  line (`references/offers/price-presentation.md` PP9).
- **Intra-brand comparison PDP** (2 to 4 sibling SKUs or tiers). A
  `comparison` table with one "best for" line per tier sits below the
  explanation sections (Huel 3-SKU table, Wakefit 4 tiers, Endy persona rows).

## Anatomy

Counts exclude chrome (`announcement`, `header`, `sticky-cta`, `footer`).
Frequencies are from the 15 PDP teardowns in
internal research audit (2026-09-10).

1. `announcement`: conditional: a verified free-shipping threshold or offer
   ledger row exists. Carries one fact, not a countdown.
2. `header`: mandatory, full navigation. The PDP lives inside the store.
3. `gallery`: mandatory. Vertical gallery minimum (5 to 12 images), first
   image is the selected variant packshot, video as a gallery thumbnail.
4. `buy-box`: mandatory. Untruncated title, `review-summary` (average plus
   count, 11 of 15), price and compare-at, unit price where law requires,
   variant options as buttons with a one-line fit sentence per option (Jones
   Road shades, Wakefit tiers, Man Matters stages; 3 of 15), quantity, add to
   cart, shipping and returns line with cost and delivery estimate, payment
   marks. Composition and viewport rules: `design-rules.md` A8.
5. `trust-bar`: recommended (13 of 15 show trust chips under the CTA):
   returns window, warranty, shipping threshold, guarantee. Facts only.
6. `benefits`: mandatory. Three to six outcome-led statements, each with a
   number, material, time or test.
7. `ingredients`, `specs` or `materials`: mandatory (13 of 15). Full label,
   composition percentages or spec table; supplier provenance where known.
8. `how-it-works` or `usage`: recommended (8 of 15). Steps with cadence and
   time-to-result where the merchant can substantiate it.
9. `comparison`: conditional: two or more sibling SKUs, tiers or a named
   category alternative (4 of 15). One "best for" line per column; no winner
   ribbon.
10. `ugc-grid`: conditional: rights-cleared customer media exists in the
    library. RESEARCH: 67% of sites lack it and shoppers seek unfiltered
    images https://baymard.com/blog/integrate-social-media-visuals-on-product-page .
11. `reviews`: mandatory (13 of 15; 12 of 15 place it in the last 20% of the
    page). Distribution bars as filters at 20 or more reviews, photo reviews
    navigable, at least one critical review reachable.
12. `faq`: recommended (10 of 15). Five to eight questions phrased as the
    shopper's objection ("Will it feel heavy or cakey?"), first sentence of
    each answer is the answer.
13. `cross-sell`: conditional: a named relationship exists (Complete the
    routine, Compatible replacement, Refill). Two or three items, one line on
    why each belongs, never between price and add to cart.
14. `legal`: conditional: market list includes IN. Regulatory block:
    marketed by, manufacturer or importer, country of origin, net quantity,
    licence number, consumer-care contact, best-before where applicable
    (Legal Metrology Rule 6(10); E-Commerce Rules 2020 Rule 6(5)). Observed on
    9 of 9 Indian PDPs.
15. `sticky-cta`: optional. Appears only after the buy box scrolls out,
    bottom-anchored on mobile, at most 64px, carries selected variant and
    price, opens the real variant picker when none is chosen.
16. `footer`: mandatory chrome.

India rail sections (conditional: IN in the market list) are placed as
suffixed ids inside or directly after the buy box: `pricing-mrp` ("MRP ₹X
(inclusive of all taxes)", selling price at or below MRP, "X% off MRP" as
struck text only), `delivery-cutoff-pincode` (pincode input returning a
delivery date and COD availability), `payment-options-india` (UPI, cards,
no-cost EMI with bank list and tenure, "Pay on delivery via UPI or cash",
prepaid incentive if the merchant runs one), and a GST note (GST-inclusive
price, business invoice available). Rules: `price-presentation.md` PP5, PP21,
PP22, PP23.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.get` with the product id: `media[]` with alt and order (count N; view each with `lexsis_assets.view` and map it to one job from `references/assets/image-jobs-by-page-type.md`: identity, detail, scale, in-use, variation, included-items, label-or-facts-panel); option axes and whether the colour axis carries per-variant images; price, compare-at and its basis; selling plans; inventory per variant; product type for the vertical gallery minimum (`references/assets/imagery-by-vertical.md`).
2. `lexsis_catalog.reviews_status`, then `lexsis_catalog.reviews` with `product_id` (n, average, newest date, per-star counts, `has_media` count) and `lexsis_catalog.review_collections` with `collection_status: "active"`: this fixes the review band B0 to B4 per `references/proof/reviews-sourcing.md`.
3. `lexsis_brand.context` and `lexsis_brand.brand_kit` (theme_id, tokens, voice, whether an SVG icon set exists); `lexsis_brand.navigation` for the full nav.
4. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"` for `product-shot`, `lifestyle`, `flat-lay`, `social-proof`; then one semantic `query` per gallery job still missing after step 1. Order and checks: `references/assets/asset-sourcing-sequence.md`; thresholds: `references/assets/slot-spec.md`.
5. `lexsis_cart.get`: free-shipping threshold, discount behaviour, cart v2.
6. `lexsis_design.islands` for the live island catalog, then `lexsis_design.island_schema` for each island named below before any prop is written; deprecated entries are never used.
7. Market list from the brief (IN adds the rail sections; shipping zones decide whether a delivery estimate is truthful). `lexsis_workspace.credits` only when a generation is on the table; the hero here is a `packshot`, so generation is an ASK below the fold and usually skipped.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `announcement` | one verified fact (free-shipping threshold or an offer ledger row). | none; text only, no countdown. | SiteHeader announcement strip when the header is SiteHeader, else AnnouncementBar; one message, not sticky, not dismissible; resolve props from `lexsis_design.island_schema`. Omit without a ledger row. | one sentence under 60 characters; vocabulary per `references/anti-patterns/copy-anti-patterns.md`. | `lexsis_cart.get` threshold or an offer ledger `O` row. |
| `header` | full store navigation. | brand logo from the brand kit; text wordmark when none. Without a logo, use the wordmark; never generated. | SiteHeader (with announcement) or Navbar (without); sticky, cart drawer, links from `lexsis_brand.navigation`; hydration mode from the live schema. | nav labels as the store names them. | `lexsis_brand.navigation`; announcement present or not. |
| `gallery` | decision support; every position answers a shopper question. | yes, identity-bound: identity, in-use, detail, scale, variation, included-items in that order, catalog media first, then library `product-shot` and `lifestyle`, then merchant upload, then supplier for the exact SKU; never stock, never a generated image in any gallery position (GP11). Video only as a real clip with a real poster (`references/assets/video-rules.md`). Below the vertical minimum or missing an R job: the job, aspect and count; generation is not feasible for gallery jobs; the gallery ships with what exists and the slot stays `planned`. | ProductGallery, or ImageZoom around a single image; decide layout, thumbnail rail, mobile behaviour and lightbox from the image count (1 to 2: stacked, no thumbnails; 3 to 5: main image with a thumbnail rail, swipe on mobile; 6 to 9: grid or collage with the first image large; 10 or more: masonry or two columns with every thumbnail visible or an explicit "+N"); variant sync on when the colour axis carries per-variant images and a VariantSwatches emitter is on the page; contain fit for packshots on white (aspect is CSS, not a prop); no autoplay or motion unless the plan's motion moment (N10); the first item is the feed image for Shopping traffic. | alt per the slot template, under 125 characters; no baked-in text. | `media[]` count and job map from step 1; variant image mapping; the vertical minimum. |
| `buy-box` | choose a variant and add to cart within 1.5 mobile viewports (`design-rules.md` A8). | swatch images per colour variant from the variant-to-media mapping; CSS chips from the catalog hex only beside a real swatch; a size chart as an HTML table, image only when the merchant's chart cannot be transcribed. The block is a form, exempt from the imagery rule. Missing swatches: per variant; not generated. | BuyBox, with VariantSwatches for a colour axis that carries images (resolve variant imagery from the live purchase contract), BuyBox's own buttons or a VariantSwatches size grid for sizes (sold-out sizes labelled inline), OptionResolver when three or more axes need coordinating; SizeGuide only with merchant measurements; SubscriptionToggle (one-time default) when selling plans exist; QuantityBreaks below the CTA, never between price and add to cart, at most four tiers; DeliveryEstimate for single-zone domestic shipping, while the India pincode line is static HTML (the island has no pincode input); PaymentOptions only above the provider floor (`references/offers/price-presentation.md` PP24); InventoryIndicator only with a live inventory binding. Decision inputs: option axes and per-variant images, selling plans, inventory binding, market list, cart v2. Resolve every variant and prop from `lexsis_design.island_schema`. VariantSelector belongs to cards and quick view, not the PDP. | untruncated title; one fit sentence per option (under 12 words); description 60 words; two microcopy lines under the CTA; India rail per `price-presentation.md` PP5, PP21 to PP23; offers per `references/offers/offer-types.md`. | step 1 axes and images; selling plans; inventory binding; market list; `lexsis_cart.get`. |
| `trust-bar` | returns window, warranty, shipping threshold, guarantee, as facts under the CTA. | none; text facts with the page's single SVG icon set or no icons; certification marks only as issuer artwork with a ledger row, never generated (GN5). | none. | four facts of six words or fewer. | `policy-fact` rows in the proof ledger. |
| `benefits` | three to six outcome statements, each with a number, material, time or test. | yes, one image per benefit (in-use, detail or context) from catalog media not used in the gallery, then library `lifestyle`, then merchant upload; `context` alone may be generated as `product_composite` over the real cut-out. Fewer images than benefits: record the missing jobs; alternative: the composite; meanwhile one real in-use image beside the facts; merge into facts or cut benefits as the agreed alternative. No-go: icon tiles, emoji rows, a colour band per benefit, a generated in-use scene (GP14). | none. | six items of 20 words; `fab`; the shopper's words from review mining; `references/anti-patterns/copy-anti-patterns.md`. | images left after the gallery map; `reviews_search` for vocabulary. |
| `ingredients`, `specs` or `materials` | full label, composition or spec table with provenance. | yes for regulated consumables and materials: the label as HTML text with a legible real label photo (1600 px or more) as the zoomable supplement; an ingredient or material flat lay from catalog, library `flat-lay`, merchant upload, or licensed stock raw material as context only (GN11); texture macro from catalog or merchant. Missing media: (label photo, flat lay); generation is not feasible for food, formula or panels; the HTML table ships regardless. | IngredientExplorer when four or more actives carry percentages or per-ingredient imagery, else an HTML table; choose layout from the ingredient count; use grouped `<details>` or CSS tabs, and never hide this block. | every number in HTML matching the label; supplier named where known; 150 words outside the table. | product type (regulated or not), ingredient count, label photo resolution via `lexsis_assets.view`. |
| `how-it-works` or `usage` | steps with cadence and time-to-result the merchant can substantiate. | yes, sequence: three to five real numbered frames from catalog, library `lifestyle`, or merchant upload; a demo video as click-to-play per `references/assets/video-rules.md`. Missing frames: (sequence, count, aspect); generation is not feasible for sequence; meanwhile three short steps beside one real in-use image; merge into benefits as the agreed alternative. | none; a plain video element for the demo. | 25 words per step; no result claim without a ledger row. | frame count from step 4; substantiation in the proof ledger. |
| `comparison` | sibling SKUs or a named category alternative, one "best for" line per column. | yes, one identity image per own column from each sibling's `lexsis_catalog.get`; the alternative as an inline SVG silhouette labelled "other brands"; never a competitor photo without licence. Missing sibling image: use a text column while the slot remains planned. | none; an HTML table, no winner ribbon (N9). | "best for" 12 words per column; per-unit prices per `price-presentation.md` PP8 and PP9. | the sibling list from the brief and catalog. |
| `ugc-grid` | rights-cleared customer photos in real use. | yes, only library `social-proof` assets with a `P` ledger row, and `has_media` reviews; uniform tiles labelled as customer content; never stock or generated people (GN3, GN9). No rights: what a rights record needs and offer the import path; the section waits for it (rules in `references/proof/reviews-sourcing.md`). | none; an HTML grid, GalleryLightbox mounted once if wanted. | caption with first name or handle when permitted. | `has_media` count and library rights records. |
| `reviews` | breadth of evidence with the distribution as a filter and a critical review reachable. | review photos and videos from the records; avatars real with consent or CSS initials. | by band per `references/proof/reviews-sourcing.md`: B1 static verbatim cards and an "n reviews" link; B2 ReviewCarousel showing all cards at once, autoplay off (N10), bound to an active collection or the product id; B3 ReviewList with distribution filters, sort and media; B4 the same plus media filter and merchant replies. Never an endpoint prop, never SocialProofPopup, never a rating filter on the full list (RS8). | island-rendered; one line disclosing the default sort; average to one decimal with its count. | band from step 2; active collection id. |
| `faq` | five to eight shopper objections answered in the first sentence. | none; page background (N8). | none; native `<details>` and `<summary>`. | questions in the shopper's words; answers 60 words. | `reviews_search` for objections; policy pages. |
| `cross-sell` | a named relationship (Complete the routine, Compatible replacement, Refill), two or three items. | yes, one identity image per item from its own `lexsis_catalog.get`; omit an item without an image until its media is supplied. | ProductCarousel in its compact row form for two or three items, quick add only with cart v2, entry animation off (N10); the section owns the h2; never between price and add to cart. | one line per item (18 words); relationship name as the h2. | a real relationship in the catalog; cart v2. |
| `legal` | India regulatory block. | none; HTML text. | none. | facts as stored; no two conflicting facts. | market list includes IN; merchant-confirmed facts. |
| `sticky-cta` | re-surface add to cart with variant and price after the buy box scrolls out. | product thumbnail from catalog position 1, or a text-only bar. | StickyBar in product mode, appearing after the buy box, animation off on quiet pages; resolve shared purchase state through the live schema; only when the page runs past about three mobile screens. | label carries variant and price. | estimated page height; cart v2. |
| `footer` | store footer chrome. | brand logo; text social links when the page has no icon set. | Footer; columns from `lexsis_brand.navigation`; hydration mode from the live schema. | the store's. | `lexsis_brand.navigation`. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | identity, variation per colour, one or two detail shots, sometimes a label photo and a video | scale, in-use with a real person, included-items, sequence frames, swatch on skin | reuse a gallery image below the buy box; generate `product_composite` for context only (never in the gallery); ask the merchant to upload scale, in-use, included-items, or to approve the composite; skip how-it-works or ugc-grid only on the merchant's call |
| asset library | `product-shot` cut-outs, `lifestyle` in-use, `flat-lay` kits, `social-proof` UGC with rights | on-body scale, sequence frames, a label photo at 1600 px | ask the merchant to upload; UGC waits for a `P` row |
| generation | backdrops, textures, composites only (`hero_bg`, `section_bg`, `card_bg`, `texture_fill`, `pattern_tile`, `decorative_element`, `product_composite`) | product, people, results, logos, text, anything in the gallery or a proof section | never |

Minimal assets (one or two catalog images): a stacked gallery or a single image with zoom, the buy box, an HTML spec table, reviews by band, a native FAQ, and `planned` slots for scale and in-use listed in the plan and draft summary; benefits fold into facts beside the one real image, and how-it-works and ugc-grid wait, each as the agreed alternative. Generated assets on a PDP: usually zero, at most one ASK backdrop below the fold, never more than the house cap of four.

## Above the fold (390px)

In order: header, first gallery image (no more than 60% of viewport height),
untruncated title, review summary with count (or "n reviews" link when n is
under 5), price with compare-at and unit or per-use line where it applies,
first variant row. Add to cart, the shipping and returns line and the India
rail land within 1.5 viewports (A8 check: price and add to cart above y =
1266px at 390). Not above the fold: countdowns, discount pills, cross-sell,
popups, a promo bar that pushes the title below the first screen, a hero
carousel.

## Proof

- Modules: 2 to 4. Module one is `review-summary` in the buy box. Module two
  is `reviews` with distribution and filters. Module three is one non-review
  kind beside the claim it supports: `certification`, `test-data`,
  `expert-quote`, `press-quote-linked` or `guarantee`. Module four is
  `ugc-photo` or `review-with-media` when rights exist.
- Minimum evidence per kind: `references/proof/proof-ledger.md`. Average only
  at 5 or more reviews; distribution at 20 or more; stars always paired with
  the count; one decimal.
- RESEARCH: up to 95% of users consult reviews and the distribution chart is
  the most used element https://baymard.com/blog/user-ratings-distribution-summary .
- Placement: the teardowns put the full reviews module in the last 20% of the
  page (12 of 15). `references/proof/reviews-sourcing.md` prefers the
  long-form list after the explanation sections and before the FAQ. Both are
  satisfied by placing `reviews` immediately before `faq`.
- No reviews: run the zero-review order in `reviews-sourcing.md`. Guarantee
  and policy facts, certifications with issuer, product evidence, a founder
  note. Nothing review-shaped.

## Offer and CTA

- CTA count: 2. Add to cart in the buy box and one repeat (`sticky-cta` or a
  closing add to cart after the FAQ). Buy now or express pay may sit beside
  the primary button; it is not a third CTA.
- First CTA position: in the buy box (section index 0 of the body).
- Sticky: optional. Evidence is mixed: +5% to +26% in vendor A/B roundups
  https://revenueflows.ai/blog/do-sticky-add-to-cart-buttons-increase-shopify-conversion-rate
  against one CRO shop that lost revenue per visitor when the hero rating
  anchored to a bottom reviews module https://ecommrumble.com/fighters/okendo .
  Ship it only with variant state and price in the label.
- CTA copy: "Add to cart" ("Add to bag" for fashion and beauty). Never "Buy
  Now", "Shop Now" or an arrow (A12).
- Price reveal: immediate, in the buy box. Shipping cost or the free-shipping
  threshold and a delivery estimate sit on the PDP. RESEARCH: 64% of users
  look for shipping cost on the product page; 43% of sites do not show it
  https://baymard.com/blog/show-shipping-costs-on-product-pages .
- Offers that fit: `none`, `gwp`, `free-shipping`, `bundle` (below the buy
  box), `subscribe-save` (toggle with one-time selected by default and both
  prices visible), `bnpl` (line under the price, total first), `cashback`
  (India), `tiered-volume` (consumables), `percent-off` and `fixed-off` only
  with a verified compare-at basis, `first-order` shown to first-time
  visitors only. Never `flash-sale`, `clearance` or `mystery` on a PDP; route
  those to `sale-clearance-flash`.
- Compare-at is struck text only; no "% OFF" pill, no "BEST VALUE" ribbon
  (`design-rules.md` N9). Savings line: currency first over the Rule-of-100
  line, percent first under it (`offer-types.md` OF2).
- Subscription option: never pre-selected unless the merchant confirms
  subscription is the primary offer and the recurring price, cadence and
  cancel path sit in the same block (`references/anti-patterns/dark-patterns.md`).

## Imagery

- Required jobs: `identity`, `detail`, `scale`, `in-use`; plus `variation`
  and `swatch` when variants exist, `included-items` when the product ships
  in parts, `size-reference` for worn or applied goods,
  `ingredient-or-material` and `label-or-facts-panel` for regulated
  consumables (`references/assets/image-jobs-by-page-type.md` section 2).
- Hero: `packshot` of the selected variant; alternate `product-in-hand`.
  Never an editorial lifestyle image as the first gallery slot; for Shopping
  traffic the first image is the feed image.
- Gallery minimum by vertical (5 supplements and food, 6 beauty and
  jewellery, 7 electronics, 8 home, 8 to 12 fashion), plus two images below
  the buy box (in-use, context or proof). Show every thumbnail or an explicit
  "+N" control.
- Balance: studio versus lifestyle per vertical table; identity-bound jobs
  never from stock or generation.
- Video: optional, as a gallery thumbnail with a poster and play badge, never
  autoplay with sound, never the hero. RESEARCH: 59% of users skip PDP
  videos; placement in the gallery is what gets it found
  https://baymard.com/blog/embedding-product-page-videos .
- Slots the plan creates: one per missing required job, with the job in the
  slot's purpose; an in-scale image is required for every physical product
  (42% of users judge size from images
  https://baymard.com/blog/current-state-ecommerce-product-page-ux ).

## Copy

- Framework: `fab` for the description and bullets; `4ps` (promise, picture,
  proof, push) for the argument below the buy box.
- Headline: the product name, optionally with the strongest verified claim
  as the subtitle ("Wireless earbuds, 42-hour playback"). Search-intent
  variant keeps the feed title. No "X without the Y" lead unless the page is
  `pdp-hybrid-landing`.
- Reading level: grade 6 to 8; sentences under 15 words on average.
- Length ceilings: buy-box description 60 words; benefits 6 items of 20
  words; how-to steps 25 words each; FAQ answers 60 words; total body 500 to
  1,200 words excluding reviews.
- Variant option copy: one fit sentence per option ("for fair to medium
  skin tones", "lumbar-reinforced foam for long-term back health").
- Vocabulary: the shopper's words from review mining; no "premium",
  "elevate", "seamless"; India prices as "₹1,24,999" with lakh grouping;
  "expected delivery by [date]", never "guaranteed".
- Microcopy under add to cart: two lines at most from shipping cost or
  threshold, returns window, payment methods, prepaid incentive.

## Never

- Never hide price, shipping cost or delivery estimate until cart or
  checkout.
- Never truncate the title or hide variant options behind a dropdown when
  they fit as buttons.
- Never show a star average without its count, or any average under 5
  reviews.
- Never show two different ratings for the same product on one page (Jones
  Road foundation page showed 4.88 and 4.61).
- Never place cross-sell, upsell or quantity breaks between price and add to
  cart.
- Never pre-select a subscription, multi-pack or paid add-on.
- Never render a countdown, "N people viewing", "N added to cart this week"
  or a stock count from static copy.
- Never use a horizontal tab layout that hides ingredients, specs or reviews.
- Never repeat the same block twice (shade list as accordion and grid; FAQ
  and description duplicated).
- Never contradict the feed: price, availability, variant name or first
  image on a Shopping landing page.
- Never show two conflicting regulatory facts (country of origin stated
  differently in two tables).
- Never let a promo bar plus countdown push title and price below the first
  screen at 390.

## Examples

- Jones Road Beauty, Miracle Balm
  https://www.jonesroadbeauty.com/products/miracle-balm : fifteen shades each
  with a skin-tone fit sentence, the first FAQ routes to the shade quiz, a
  three-part guarantee row, an honest 4.23 average with 85,425 reviews.
- Huel, Black Edition https://huel.com/products/huel-black-edition : price
  restated per meal in the hero, intra-range comparison table with price per
  meal, a stated taste guarantee.
- Minimalist, Salicylic Acid 2% https://beminimalist.co/products/salicylic-acid-2 :
  India rail done plainly (MRP, GST breakdown, regulatory block), supplier
  named per active, review summary with topic percentages and visible one-star
  reviews, usage cadence ramp in how to use.

## Checklist

```json
{
  "page_type": "pdp",
  "aliases": ["product page", "product detail page", "buy-box page", "search-intent PDP"],
  "funnel_stage": ["mof", "bof"],
  "awareness": ["product-aware", "most-aware"],
  "traffic": ["organic", "google-search", "google-shopping", "email", "direct"],
  "sections": { "min": 7, "max": 11 },
  "mandatory_sections": ["header", "gallery", "buy-box", "benefits", ["ingredients", "specs", "materials", "features"], "reviews", "footer"],
  "recommended_sections": ["trust-bar", ["how-it-works", "usage"], "faq", "comparison", "cross-sell", "ugc-grid", "sticky-cta"],
  "forbidden_sections": ["hook", "problem", "agitation", "discovery", "countdown", "quiz", "offer-bridge", "final-offer"],
  "nav": "full",
  "price_above_fold": "required",
  "cta": { "min": 2, "max": 2, "first_after_section": 0, "sticky": "optional", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 2, "max_modules": 4, "required_kinds": ["review-summary", "review-list"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "detail", "scale", "in-use"], "hero": "packshot", "video": "optional", "min_images": 7 },
  "copy_framework": ["fab", "4ps"],
  "offer_compat": { "allowed": ["none", "gwp", "free-shipping", "bundle", "subscribe-save", "bnpl", "cashback", "tiered-volume", "percent-off", "fixed-off", "first-order"], "forbidden": ["flash-sale", "clearance", "mystery"] },
  "urgency": "verified-only"
}
```

`imagery.min_images` is the supplements floor (gallery 5 plus 2); the
vertical table in `references/assets/image-jobs-by-page-type.md` raises it.
`percent-off` and `fixed-off` require a verified `compare-at` ledger row;
`first-order` renders for first-time visitors only.

## Sources

- Baymard product page research https://baymard.com/research/product-page ;
  PDP state 2026 https://baymard.com/blog/current-state-ecommerce-product-page-ux ;
  shipping cost on PDP https://baymard.com/blog/show-shipping-costs-on-product-pages ;
  ratings distribution https://baymard.com/blog/user-ratings-distribution-summary ;
  social media visuals https://baymard.com/blog/integrate-social-media-visuals-on-product-page ;
  video placement https://baymard.com/blog/embedding-product-page-videos ;
  review image navigation https://baymard.com/blog/allow-navigation-across-reviews-from-reviewer-images
- Landing page vs product page by traffic https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/
- Sticky add to cart evidence https://revenueflows.ai/blog/do-sticky-add-to-cart-buttons-increase-shopify-conversion-rate ;
  counter-evidence https://ecommrumble.com/fighters/okendo
- Google Merchant Center landing page requirements https://support.google.com/merchants/answer/4752265 ,
  https://support.google.com/merchants/answer/7331077 , https://support.google.com/merchants/answer/9479464
- Gourville 1998, pennies a day https://doi.org/10.1086/209517
- India Legal Metrology Rules https://www.legitquest.com/act/legal-metrology-packaged-commodities-rules-2011/97B4 ;
  E-Commerce Rules 2020 https://ibclaw.in/consumer-protection-e-commerce-rules-2020/
- Sibling references: `references/design-rules.md` (A8, N9),
  `references/proof/proof-ledger.md`, `references/proof/reviews-sourcing.md`,
  `references/offers/offer-types.md`, `references/offers/price-presentation.md`,
  `references/assets/image-jobs-by-page-type.md`, `references/generate-pdp.md`,
  `references/traffic-source-google.md`, `references/consumer-behavior-cro.md`
