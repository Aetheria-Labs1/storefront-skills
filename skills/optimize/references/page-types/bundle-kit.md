# Bundle and kit page

Two or more complementary products sold as one set, either fixed at one price
or assembled by the shopper from matched options, with the saving against
buying separately shown as arithmetic. Shoppers arrive product-aware from
email, a PDP cross-link, quiz results or retargeting; their job is to accept
or adjust the set and add it to cart. The value is the set, so the page
proves completeness and shows the math. Builder mechanics and island props
live in `references/generate-bundle-page.md`; this file is the contract.

## Identify it

- Brief mentions "bundle", "kit", "starter set", "routine", "build your
  own", "pick any 3", "save when you buy together", or consumables with
  refills and a set price.
- Two to six SKUs that are complementary (cleanser plus serum plus SPF), not
  alternatives (three versions of one product).
- Visitor mode is "complete" (`references/consumer-behavior-cro.md`): the hero
  SKU is one part of the shopper's job.
- Near neighbours:
  - `offer-page`: choose offer when the value is the discount, bundle when
    the value is the set (index tie-break).
  - `pdp` with `cross-sell`: one hero product and optional add-ons; choose
    bundle only when the set itself is the product.
  - `subscription`: a recurring set; choose subscription when cadence is the
    subject, bundle when the one-time set is.
  - `quiz-funnel`: a routine assembled from answers; the results screen
    reuses bundle rules but is its own type.
  - `tiered-volume` on a PDP: multiples of one SKU are quantity breaks, not a
    bundle.

## Variants

- **Fixed kit.** One price, fixed contents, `product-hero` in place of a
  builder; each component still individually selectable to remove (defaults
  move baskets; removal keeps trust).
- **Build-your-own.** `bundle-builder` with one decision per step ("Choose 1
  base, then add any 2"), running total, rules in plain microcopy, in-stock
  items only, at most six slots (`offer-types.md` bundle anti-patterns).
- **Good, better, best ladder.** Three tiers with a visible `comparison`
  table; the target tier is the option that dominates the decoy; the decoy is
  a real purchasable option. No ribbon on the middle tier (N9); a plain "best
  for" line per tier instead. RESEARCH: asymmetric dominance replications
  move share 10 to 18 points, not 52 (`offer-types.md` bundle-decoy).
- **Routine kit.** Components in order of use (Step 1, Step 2, Step 3) with a
  `routine` timeline and time-to-result stated only when substantiated.

## Anatomy

Counts exclude chrome. Frequencies are from the Salt of the Earth builder,
Man Matters kit configurator and Huel trio teardowns in
internal research audit (2026-09-10).

1. `announcement`: conditional: verified bundle discount, free-shipping
   threshold or guarantee fact (Salt of the Earth: discount plus guarantee).
2. `header`: mandatory, minimal (logo plus one utility link). Full navigation
   is allowed when the page is a permanent store page linked from the header;
   record the override in the plan.
3. `hero`: mandatory. Names the outcome of the set ("Your complete morning
   routine"), shows every component laid out (`grid` hero), carries the
   `review-summary` when reviews exist, states the set price beside the sum
   of components.
4. `savings-math`: mandatory. Bundle price, sum of component list prices
   actually sold at those prices, saving in currency then percent ("₹3,297
   separately, ₹2,499 as a set, save ₹798 (24%)"). Sits within one scroll of
   the first price and again in the running total.
5. `bundle-builder` or `product-hero`: mandatory, one of the two. Builder for
   build-your-own (progress, running total, in-stock only, sold-out items
   show "Notify me"); product hero for a fixed kit with per-item remove.
6. `product-spotlight`: mandatory (what is inside). One row per component
   with its role ("Step 1, cleanse"), one line on why it belongs, per-item
   `review-summary` when the component has its own reviews, per-item price.
   The base id `product-spotlight` is used with a `-components` suffix when
   the plan needs to distinguish it from a hero spotlight.
7. `pricing` with `comparison`: conditional: a good, better, best ladder
   exists. Three tiers, price and per-item value on each, attributes in a
   visible table, "best for" line per tier.
8. `quantity-breaks`: conditional: the merchant runs a volume ladder on the
   components (Salt of the Earth 1, 2, 3, 5 bags). At most four tiers, per-unit
   price per tier, single unit as the reference price.
9. `routine` or `usage`: recommended. Order of use, cadence, what to expect
   and when; expectation-setting copy protects retention.
10. `reviews`: mandatory. Set-level reviews when they exist; otherwise
    component reviews labelled by product, never averaged into a bundle
    rating (internal teardown audit, 2026-09-10).
11. `guarantee`: recommended. Exact terms; "used or unused" where true.
12. `faq`: recommended, placed near the builder. "Does the discount apply at
    checkout?", "Can I swap an item?", "Can I mix scents?", returns on
    partially used kits.
13. `sticky-cta`: conditional: `bundle-builder` present. Running total plus
    saving plus "Add the set" on mobile; states "Select at least N" until the
    rule is met.
14. `closing-cta`: mandatory. Restates set price, saving and guarantee.
15. `footer`: mandatory chrome.

Never include `offer-bridge`, `problem`, `agitation`, `countdown` (a bundle
is evergreen unless a ledger `endsAt` exists, in which case the offer belongs
on `offer-page`) or a `subscription-toggle` that is pre-selected.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.get` for the bundle SKU (when the set is its own Shopify product): `media[]` (the set flat lay is the `included-items` job; view each item), price, compare-at, selling plans, inventory. Then `lexsis_catalog.get` for every component: first media item as that component's identity, current price (the "separately" figure must be a price it actually sells at), variants and per-variant images, inventory per variant. Job map per `references/assets/image-jobs-by-page-type.md`.
2. `lexsis_catalog.reviews_status`; `lexsis_catalog.reviews` with the bundle `product_id` for set-level reviews, then per component id, each scope kept separate (never averaged, `references/proof/reviews-sourcing.md` RS7); `review_collections` with `collection_status: "active"`.
3. `lexsis_brand.context`, `lexsis_brand.brand_kit` (theme_id, tokens, voice, icon set), `lexsis_brand.navigation` (minimal nav, or full when the page is a permanent store page).
4. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"` for `flat-lay`, `product-shot`, `lifestyle`, `social-proof`; then semantic "<kit name> laid out", "<component> step". Sequence and checks: `references/assets/asset-sourcing-sequence.md`.
5. Offer ledger: bundle price, sum of components, saving as `O` rows (`references/offers/offer-types.md` bundle, bundle-decoy, tiered-volume, OF2, OF4); `lexsis_cart.get` to confirm the discount applies in the cart and the cart edit flow matches the page.
6. Type variant from the brief: fixed kit, build-your-own, good, better, best ladder, or routine kit; it decides the purchase island. `lexsis_design.islands` for the live catalog, then `lexsis_design.island_schema` for each island named below before any prop is written.
7. `lexsis_workspace.credits` only when a `product_composite` for a routine context image is planned; the hero is a `grid` of real components and needs no generation.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `announcement` | one verified fact: bundle discount, free-shipping threshold or guarantee. | none; text. | SiteHeader announcement strip or AnnouncementBar, one message, not sticky. Omit without a ledger row. | under 60 characters; vocabulary per `references/anti-patterns/copy-anti-patterns.md`. | offer ledger `O` rows; `lexsis_cart.get` threshold. |
| `header` | minimal chrome, logo plus one utility link; full nav only for a permanent store page (record the override). | brand logo or text wordmark; without a logo, use the wordmark. | SiteHeader minimal (one link, CTA anchoring to the builder) or Navbar with full links for the override. | store names. | `lexsis_brand.navigation`; page permanence. |
| `hero` | name the outcome of the set and show every component at once with the set price beside the sum. | yes, included-items and identity: bundle SKU media (set flat lay) first, library `flat-lay`, merchant upload of the kit laid out; if none, compose the `grid` hero in HTML from each component's real catalog cut-out (layout, not a generated image). Never a lifestyle hero that hides the components; never a generated flat lay or a multi-product composite (GP13). Missing flat lay: (included-items, landscape and portrait, one shot); generation is not feasible; the cut-out grid ships meanwhile and the slot stays `planned`. | none for the HTML grid; ProductHero in a split layout when the bundle SKU carries three or more real images (flat lay first, then components), no autoplay (N10). | outcome headline 8 words; subhead 20 words; price line "₹3,297 separately, ₹2,499 as a set, save ₹798 (24%)"; review summary only with 5 or more set-level reviews. | bundle SKU `media[]`; component cut-out availability; set-level band. |
| `savings-math` | the arithmetic within one scroll of the first price and again in the running total. | none; a three-line price table is an object and sits alone. | none; the struck sum carries `data-source="O<n>"`; currency first over the Rule-of-100 line (`references/offers/price-presentation.md` PP10). | three figures and one saving line; never "unlock savings". | offer ledger rows. |
| `bundle-builder` or `product-hero` | the purchase control: build the set, or accept the fixed set and remove items. | yes, one identity image per component from each component's catalog media. A component without an image: (identity, square, one per component); not generated; the component is not offered until the image exists. | build-your-own: BundleBuilder, in-stock components only, at most six slots, rules as HTML microcopy, a sold-out component replaced by EmailCapture in compact form labelled "Notify me". Fixed kit whose components are separate SKUs: BundleBuilder with every component pre-selected (the checkbox is the remove control). Fixed kit sold as one SKU: BuyBox in compact form, one per page. SubscriptionToggle only with one-time as the default. Decision inputs: type variant, component inventory, cart v2. | rule microcopy 12 words per step; CTA "Add the set", "Get the kit". | step 6 variant; component inventory; `lexsis_cart.get`. |
| `product-spotlight` (`-components`) | what is inside: one row per component with its role and why it belongs. | yes, identity per component (catalog first media), detail where it exists; the row's image is the row. View the component cut-outs together so background, scale and lighting match across the set. Missing: per component; in fast-draft the row ships text-only and is listed under Unresolved assets. | none (HTML rows with per-item price and a labelled review summary), or ProductCarousel in compact row form for three to five components when per-item reviews are not shown, animation off. Per-item review summary from `reviews` for that component id, labelled, at 5 or more reviews. | role ("Step 1, cleanse"), one line on why it belongs (18 words), per-item price. | component count; per-component bands. |
| `pricing` with `comparison` | good, better, best ladder with a visible attribute table and a "best for" line per tier. | one identity image per tier when tiers differ physically; a table without images is allowed (a table is an object, N8). | PlanSelector in card form for the three tiers, the "best for" line as the tier note, no badge (N9), every tier purchasable at the shown price; the attribute table as HTML below | "best for" 12 words; per-item value on each tier. | three tiers confirmed in the offer ledger. |
| `quantity-breaks` | a volume ladder on components, at most four tiers, single unit as the reference. | pack imagery per tier from catalog media when the card form is used; none for the pill form. Missing pack image: use the schema-supported text option. | QuantityBreaks, card form with pack images or pill form without, single unit selected by default, no "MOST POPULAR" (N9) | per-unit price per tier; "Buy 2, save 10%" pattern (`offer-types.md` tiered-volume). | a real volume ladder in the ledger. |
| `routine` or `usage` | order of use, cadence, what to expect and when. | yes, sequence: real frames of the components in order of use from catalog, library `lifestyle`, merchant upload; a single routine context image may be a `product_composite` of one real component cut-out on a plain surface. Missing frames: (sequence, count); alternative: the single composite; merge into the component rows as the agreed alternative. Video per `references/assets/video-rules.md`. | none. | step 25 words; time-to-result only when substantiated. | frames found; proof ledger substantiation. |
| `reviews` | set-level reviews, or component reviews labelled by product. | review photos from the records only. | by band per `references/proof/reviews-sourcing.md`: B1 static verbatim cards; B2 ReviewCarousel showing all cards, autoplay off (N10), bound to the bundle id or an active collection; B3 or more ReviewList with filters. Component reviews: one module per component bound to that id with the product name as the h2; never one module spanning several products. | island-rendered; the h2 names the product. | bands per scope from step 2. |
| `guarantee` | exact terms, "used or unused" where true. | none; one line beside the CTA and a short block here. | none. | one sentence of terms; the exact claim path. | `policy-fact` ledger row. |
| `faq` | builder rules, discount at checkout, swaps, returns on partial kits. | none; page background. | none; native `<details>`. | four to six questions; answers 60 words. | builder rules and policies. |
| `sticky-cta` | running total plus saving plus "Add the set" on mobile. | set thumbnail from catalog, or a text-only bar. | StickyBar in product mode for a fixed kit sold as one SKU, appearing after the buy section; for build-your-own, BundleBuilder's own total and button are the sticky element, because StickyBar cannot bind a builder total; record the deviation. | "Select at least N" until the rule is met (HTML microcopy in the builder). | purchase island chosen above. |
| `closing-cta` | restate set price, saving and guarantee. | the set flat lay or component grid reused small; no new asset. | none; an anchor to the builder (one BuyBox and one BundleBuilder per page). | price line verbatim from savings-math; guarantee one line. | mirrors savings-math and guarantee. |
| `footer` | chrome. | brand logo. | Footer. | the store's. | page permanence. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images across bundle and components) | identity per component, sometimes a set flat lay on the bundle SKU, detail shots | set flat lay when the bundle is not its own SKU, in-use, sequence frames, packaging for giftable kits | reuse the cut-outs as an HTML grid; generate `product_composite` for one component's routine context only; ask the merchant to upload the flat lay and sequence or approve the composite; skip routine only on the merchant's call |
| asset library | `flat-lay` kit shots, `product-shot` cut-outs, `lifestyle` routine scenes, `social-proof` with rights | sequence in order of use, giftable packaging | ask the merchant to upload; UGC waits for a `P` row |
| generation | backdrops, textures, a single-product composite only | the set, any multi-product scene, people, results, logos, text | never |

Minimal assets (one identity image per component): an HTML grid hero of the cut-outs, savings math, the builder or buy box, component rows, reviews by band, guarantee, native FAQ; the `included-items` and sequence slots stay `planned` and are listed in the plan and draft summary, and routine waits on the merchant's call. Generated assets: zero or one composite for routine context, never the set itself, never more than the house cap of four.

## Above the fold (390px)

In order: header, hero headline naming the outcome, component layout image
(no more than 60% of viewport height), set price with the sum of components
struck or stated and the saving line, review summary with count when 5 or
more reviews exist, first builder step or "Add the set" button. The saving is
readable without scrolling. Not above the fold: a discount pill, a "MOST
POPULAR" ribbon, per-component reviews, the FAQ, a countdown.

## Proof

- Modules: 2 to 3. Module one is `review-summary` in the hero (set-level, or
  the hero component labelled). Module two is `reviews` or
  `testimonial-spotlight` mentioning the set or routine. Module three is
  `guarantee` or `expert-quote` with a credential line (Salt of the Earth: "Dr.
  Matt Feder, PT, DPT, CSCS").
- Per component: `review-summary` on its row when the component has 5 or more
  reviews; "n reviews" link at 1 to 4; nothing at 0.
- Never average component ratings into one bundle number; never show a
  bundle rating from reviews of a single component without the product name
  beside it.
- Routine kits may show `before-after` only from a verified ledger row, never
  in the hero, with interval and "individual results vary" where the category
  requires it.
- No reviews at all: guarantee with exact terms, certifications with issuer,
  lab or test evidence for the components, founder note. Nothing
  review-shaped (`references/proof/reviews-sourcing.md`).

## Offer and CTA

- CTA count: 2. "Add the set" (or the builder's running-total button) and one
  closing CTA. Per-item remove or swap controls are not CTAs.
- First CTA position: hero (section index 0) for a fixed kit; the builder's
  sticky total for build-your-own.
- Sticky: optional in the checklist; treat as required whenever
  `bundle-builder` is present (research: mandatory on mobile for
  build-your-own, running total visible). Never obstructs the builder steps.
- CTA copy: "Add the set", "Get the kit", "Add the bundle". Never "Save 15%
  now" as the button label; the saving sits beside the button.
- Price reveal: immediate. Set price, sum of components and saving in the
  hero and again in the running total; the saving is never revealed only at
  checkout.
- Math rules: OPERATOR and LAW. Compare-at for a bundle is the sum of
  component prices actually sold at those prices (UK CMA principles cover
  bundles https://assets.publishing.service.gov.uk/media/66ab4347a3c2a28abb50db3c/Discount_and_reference_pricing_principles.pdf ).
  Currency first over the Rule-of-100 line, percent first under it, both when
  space allows ("Save $28 (32%)") https://jonahberger.com/fuzzy-math-what-makes-something-seem-like-a-good-deal/ .
  Never pad the set with a cheap item to inflate the "separately" figure;
  RESEARCH: low-value components lower willingness to pay for the whole
  (Chernev, via `offer-types.md`).
- Offers that fit: `bundle` (default), `bundle-decoy` (three-tier ladder with
  table), `tiered-volume`, `bogo`, `gwp` (gift shown as a product with retail
  value), `free-shipping`, `subscribe-save` (toggle, one-time selected by
  default, both prices visible), `bnpl` (line under the set price, total
  first), `fixed-off`, `none`.
- Offers that do not fit: `percent-off` as the offer type (the bundle saving
  already carries the percent), `flash-sale`, `clearance`, `mystery`,
  `trial-sample`, `pre-order-price`, `referral`, `gift-card`.
- Default state: the full set pre-loaded and trimmable is allowed because the
  shopper sees every component and price; a pre-ticked paid add-on outside
  the set, a pre-selected subscription or a pre-selected multi-pack is not
  (`references/anti-patterns/dark-patterns.md`).
- Discount in the running total, never only at checkout; the cart edit flow
  matches the page (same components, same remove behaviour).

## Imagery

- Required jobs: `identity` per component, `in-use`, `included-items` (the
  whole set laid out and labelled in HTML when more than four items),
  `sequence` (order of use or setup). Recommended: `detail`, `scale`,
  `context`, `packaging` when the kit is giftable, `ugc` when rights exist,
  `label-or-facts-panel` for regulated consumables.
- Hero: `grid` of the components laid out; alternate `packshot` of the set in
  its box. Never an editorial lifestyle hero that hides the components.
  RESEARCH: a "what's included" section lifted conversion 30.5% (n=12,412)
  https://www.processcreative.com.au/blog/a-b-testing-does-showing-whats-in-the-box-actually-lift-conversions .
- Minimum images: components plus 3 (identity per component, set flat lay,
  in-use, sequence). Show items together and separated.
- Balance: studio for identity and flat lay, lifestyle for in-use and routine
  context; per-vertical ratios in `references/assets/image-jobs-by-page-type.md`.
- Video: optional, a 45 to 90 second routine or unboxing demo as a
  click-to-play thumbnail with poster; never the hero.
- Slots the plan creates: one `included-items` slot when no set flat lay
  exists; one `sequence` slot when the routine order has no imagery; never
  generate a component identity image.

## Copy

- Framework: `bab` for the whole set (before: gaps in the routine; after:
  complete; bridge: the kit), `fab` per component row.
- Headline: the outcome of the set, not the discount ("Your complete
  morning routine" beats "Bundle and save 24%"). The saving sits in the price
  line.
- Reading level grade 6 to 8; 400 to 800 words total.
- Length ceilings: hero subhead 20 words; component "why it belongs" line 18
  words; builder rule microcopy 12 words per step; FAQ answers 60 words.
- Vocabulary: name the relationship (Complete the routine, Build your stack,
  Set up the station) rather than "Recommended for you"
  (`references/consumer-behavior-cro.md`); "save ₹798" not "unlock savings";
  never "MOST POPULAR", "BEST VALUE" or "LIMITED TIME".
- Microcopy under the CTA: guarantee terms, shipping threshold, "discount
  applied automatically" or the code.

## Never

- Never show a bundle without the "vs buying separately" line and the
  computed saving.
- Never state a component's "separately" price at which it was never
  actually sold.
- Never pad the set with a low-value item to inflate the anchor.
- Never let a sold-out component be selectable; show "Notify me" instead.
- Never hide builder rules (required vs optional slots) until the cart.
- Never run a different bundle edit flow in the cart than on the page.
- Never mix alternatives (three sizes of one product) and call it a bundle.
- Never highlight a tier with "MOST POPULAR" or "BEST VALUE" chrome; use a
  plain "best for" line (`design-rules.md` N9).
- Never offer more than six builder slots or more than four quantity tiers.
- Never average component ratings into a single bundle star.
- Never pre-select a subscription toggle or a paid add-on outside the set.
- Never reveal the discount only at checkout.
- Never show the saving as percent alone on a set over the Rule-of-100 line.

## Examples

- Salt of the Earth, Build Your Electrolyte Bundle
  https://drinksote.com/pages/sote-bundle-builder : tier ladder above the
  grid, quantity steppers with "Notify me" on sold-out flavours, credentialed
  expert quote, lab-test modal with dated results, FAQ that tackles the
  category objection. Avoid its currency mismatch and duplicated quote.
- Man Matters, Hair Regrowth Kit https://manmatters.com/dp/hair-regrowth-kit/2023020 :
  four-step configurator inside the buy box (stage, age, duration, booster),
  root cause mapped to each component, routine length stated as an
  expectation. Avoid leading the hero with a 3.9 rating and contradicting
  routine lengths.
- Huel, Black Edition Bestseller Trio inside the PDP
  https://huel.com/products/huel-black-edition : three-SKU comparison table
  with price per meal, the trio priced beside single bags, a stated taste
  guarantee.

## Checklist

```json
{
  "page_type": "bundle-kit",
  "aliases": ["bundle page", "starter kit", "routine page", "build-your-own box", "good-better-best page"],
  "funnel_stage": ["mof", "bof"],
  "awareness": ["product-aware"],
  "traffic": ["email", "direct", "retargeting", "meta"],
  "sections": { "min": 7, "max": 10 },
  "mandatory_sections": ["header", "hero", "savings-math", ["bundle-builder", "product-hero"], "product-spotlight", "reviews", "closing-cta", "footer"],
  "recommended_sections": ["guarantee", "faq", ["routine", "usage"], "sticky-cta", "comparison", "quantity-breaks", "trust-bar"],
  "forbidden_sections": ["offer-bridge", "problem", "agitation", "discovery", "countdown", "quiz", "hook"],
  "nav": "minimal",
  "price_above_fold": "required",
  "cta": { "min": 2, "max": 2, "first_after_section": 0, "sticky": "optional", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 2, "max_modules": 3, "required_kinds": ["review-summary"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "in-use", "included-items", "sequence"], "hero": "grid", "video": "optional", "min_images": 6 },
  "copy_framework": ["bab", "fab"],
  "offer_compat": { "allowed": ["bundle", "bundle-decoy", "tiered-volume", "bogo", "gwp", "free-shipping", "subscribe-save", "bnpl", "fixed-off", "none"], "forbidden": ["percent-off", "flash-sale", "clearance", "mystery", "trial-sample", "pre-order-price", "referral", "gift-card"] },
  "urgency": "none"
}
```

`imagery.min_images` assumes three components (three identity images plus
set flat lay, in-use and sequence); add one per extra component.
`cta.sticky` is `optional` for a fixed kit and treated as required when
`bundle-builder` is present. `nav` may be `full` when the page is a permanent
store page; record the override in the plan.

## Sources

- UK CMA discount and reference pricing principles (bundles)
  https://assets.publishing.service.gov.uk/media/66ab4347a3c2a28abb50db3c/Discount_and_reference_pricing_principles.pdf
- Berger, Rule of 100 https://jonahberger.com/fuzzy-math-what-makes-something-seem-like-a-good-deal/ ;
  JBR 2015 replication https://www.sciencedirect.com/science/article/abs/pii/S0148296315003513
- Decoy and anchoring evidence https://cxl.com/blog/pricing-experiments-you-might-not-know-but-can-learn-from/ ;
  https://www.growthegy.com/2026/05/24/product-pricing-anchoring-decoy-ecommerce/
- Chernev 2003, choice overload https://ideas.repec.org/a/oup/jconrs/v30y2003i2p170-83.html
- Statlas AOV break-even data https://www.linkedin.com/posts/taylor-holiday-a169b322_we-track-store-and-analyze-conversations-activity-7471272309199265792-Xc7H
- "What's included" test https://www.processcreative.com.au/blog/a-b-testing-does-showing-whats-in-the-box-actually-lift-conversions
- Bundle builder UX https://ecomdesignpro.com/shopify-bundle-builder-ux/ ;
  build-your-own guide https://sledge-app.com/guide/build-your-own-bundle-guide/ ;
  RevenueHunt bundles and kits https://docs.revenuehunt.com/customer-success/recommend-bundles-kits/
- Sibling references: `references/design-rules.md` (N9), `references/offers/offer-types.md`
  (bundle, bundle-decoy, tiered-volume, OF2, OF4), `references/offers/offer-ledger.md`,
  `references/proof/proof-ledger.md`, `references/assets/image-jobs-by-page-type.md`,
  `references/generate-bundle-page.md`, `references/consumer-behavior-cro.md`
