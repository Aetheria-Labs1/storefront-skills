# Offer page

One named promotion (a code, a gift with purchase, a buy-one-get-one, a
first-order discount) presented to a shopper who already knows the product.
Traffic is email, SMS, retargeting, brand search or a creator code; the
visitor is product-aware or most-aware and wants the offer honoured with no
arithmetic and no surprises. The page states the offer in plain terms, puts
the conditions within one scroll, applies the code for them, and gets out of
the way. Offer mechanics and legality live in `references/offers/offer-types.md`;
this file is the contract.

## Identify it

- The offer is the message: "20% off your first order", "buy 2 get 1",
  "free tote with orders over $75", "code SAVE10", "claim your gift", and
  there is no date-bound event and fewer than six discounted products.
- Audience has seen the product or brand (list, cart abandoners, brand
  search, creator audience).
- Near neighbours:
  - `sale-clearance-flash`: more than five products at reduced prices for a
    window; grid, not buy box (index tie-break).
  - `seasonal-gifting`: a holiday or occasion attaches to the offer with
    cutoffs and gift options.
  - `bundle-kit`: the value is the set; offer page when the value is the
    discount.
  - `retargeting-warm`: the offer is secondary to objection handling; choose
    retargeting when the first screen must answer "why not".
  - `lead-capture-giveaway`: the visitor gives an email to get the offer;
    choose capture when no purchase happens on the page.
  - `ugc-creator-collab`: a creator code with the creator's content as the
    hero; choose creator when the content carries the page.

## Variants

- **Code offer.** Percent or fixed amount; code auto-applied from the URL and
  pre-filled in cart, with the string shown in a copyable form as fallback.
- **Gift with purchase.** The gift shown as a product with its retail value,
  the threshold line adjacent, "while supplies last" only with live stock
  bound to the gift SKU; the banner is removed when the gift sells out.
- **Buy X get Y.** Both items pictured, effective per-unit price stated, an
  explicit "add both to cart" instruction because native Shopify Buy X Get Y
  never auto-adds the get item.
- **First-order offer.** Eligibility ("first order only") stated beside the
  offer; hidden from returning customers where identity is known.
- **Payment offer** (India bank or UPI cashback, BNPL). Cap, minimum order,
  bank list and timing in one line beside the price.
- **Luxury or prestige.** No percent, no struck price, no timer. The offer is
  `gwp`, complimentary shipping or early access, phrased as a courtesy
  (`offer-types.md` OF3).

## Anatomy

Counts exclude chrome. Observed order is from the Hims offer page breakdown,
the Cozy Earth creator page and the Ace Vanity gift-card offer cited in
internal research audit (2026-09-10) section 5 type 8.

1. `announcement`: conditional: a sitewide fact (free-shipping threshold)
   that is not the offer itself. The offer lives in the hero, not the bar.
2. `header`: mandatory, minimal.
3. `hero`: mandatory. The offer in plain arithmetic in the headline ("Buy 2,
   get 1 free" beats "up to 33% off"), the product packshot, the code shown
   or "applied automatically", the primary CTA, the guarantee line under it.
4. `offer`: mandatory. Mechanics in one to three lines: what qualifies,
   minimum spend, exclusions, stacking, regions, end date and time with
   timezone if one exists, code or automatic. Within one scroll of the hero
   (`offer-ledger.md` rule 4).
5. `buy-box`, `product-spotlight` or `product-grid`: mandatory, one of the
   three. Price, struck compare-at with basis, computed saving in currency and
   percent per the Rule of 100, variant options, add to cart. Grid only for
   two to five eligible products.
6. `product-spotlight` with a `-gift` suffix: conditional: `gwp`. The gift
   pictured as a product, its retail value, the threshold, live stock status.
7. `trust-bar` or `review-summary`: mandatory. Rating plus count, one
   guarantee or policy fact, one linked press quote at most.
8. `benefits`: recommended. Three statements on why the product is worth
   having, each with a number, material, time or test.
9. `countdown`: conditional: ledger `endsAt` exists, the merchant confirmed
   it will be honoured, and the page is inside the final 48 hours; otherwise
   the end date is text in the `offer` section.
10. `guarantee` or `shipping-returns`: mandatory, one of the two. Returns on
    promotional items stated plainly; shipping cost or threshold; delivery
    estimate.
11. `faq`: recommended. Stacking with other codes, expiry, returns on promo
    items, whether the gift can be swapped, eligibility.
12. `final-offer`: mandatory. Restates the offer, the terms in one line and
    the CTA.
13. `legal`: recommended chrome. The full terms; the material terms are
    already in `offer`.
14. `sticky-cta`: optional. Carries the offer and the price.
15. `footer`: mandatory chrome.

Never include education sections (`problem`, `agitation`, `mechanism`,
`science`, `story`), a `quiz`, or an `email-capture` overlay covering the
offer. Most-aware visitors do not need the premise.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. Offer ledger block confirmed with the merchant (`references/offers/offer-types.md` for the id's rules): `offer.type` (one id), depth, code or automatic, exclusions, stacking, regions, minimum spend, `offer.endsAt` (ISO with timezone) or none, `offer.compareAtBasis`, gift SKU and threshold for `gwp`, eligibility for `first-order`.
2. `lexsis_catalog.get` for the offered product(s): `media[]` mapped per `references/assets/image-jobs-by-page-type.md` (identity at position 1, one in-use, variation per variant), price, compare-at with a basis, variants and availability, inventory. For `gwp`, `lexsis_catalog.get` for the gift SKU: its identity image, its retail price (the stated value), its live inventory (the only basis for "while supplies last").
3. `lexsis_cart.get`: whether the code auto-applies from the URL and pre-fills in cart, threshold behaviour, cart v2. A code that fails at checkout is the page's worst failure; confirm before design.
4. `lexsis_catalog.reviews_status` and `lexsis_catalog.reviews` with `product_id` for the review summary band (`references/proof/reviews-sourcing.md`); `review_collections`.
5. `lexsis_brand.context`, `lexsis_brand.brand_kit`, `lexsis_brand.navigation` (minimal nav).
6. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"` for `product-shot`, `flat-lay` (gift beside product, both items of a BOGO), `lifestyle` (one in-use); no video on this type. Sequence and checks: `references/assets/asset-sourcing-sequence.md`.
7. `lexsis_design.islands`, then `lexsis_design.island_schema` for each island named below. No generation is planned on this type: the hero is a `packshot` and the page is short.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `announcement` | a sitewide fact that is not the offer (free-shipping threshold, or the end date as text). | none. | AnnouncementBar paired with Navbar, or the SiteHeader strip; one message, not sticky; never the offer headline, never a countdown, never two offers. | under 60 characters. | `lexsis_cart.get` threshold; `offer.endsAt` as text. |
| `header` | minimal chrome. | brand logo or wordmark. | SiteHeader minimal with the CTA anchoring to the buy block, or Navbar with one link. | store names. | `lexsis_brand.navigation`. |
| `hero` | the offer in plain arithmetic, the product packshot, the code status, the primary CTA, the guarantee line. | yes, identity (`packshot`; alternate `product-in-hand`) from catalog media position 1; for BOGO both items pictured side by side from their own catalog media; for `gwp` the gift may appear beside the product. Never offer text baked into the image; never a generated product or gift render (GN1, GN2); mobile gets its own portrait crop (`references/assets/slot-spec.md`). Missing packshot or gift image: (identity, square and portrait, one each); generation is not feasible; the offer is not run as `gwp` until the gift image exists. | none (one static image, preloaded); the CTA anchors to the buy block, or the BuyBox sits in the hero when hero and buy block are one section. | headline `[depth or gift] [scope], [terms or end]` in plain arithmetic, 14 words; subhead 16 words; code shown or "applied automatically"; one guarantee or shipping line; vocabulary per `references/anti-patterns/copy-anti-patterns.md`. | `offer.type` and ledger figures; `media[]` position 1. |
| `offer` | mechanics in one to three lines within one scroll of the hero. | none; text on the page background. | none. | what qualifies, minimum spend, exclusions, stacking, regions, end date and time with timezone, code or automatic; three lines of 18 words; never an asterisk to a footnote (`offer-ledger.md` rule 4). | the ledger block from step 1. |
| `buy-box`, `product-spotlight` or `product-grid` | price, struck compare-at with basis, computed saving, variants, add to cart. | yes, identity per product from catalog media (uniform card aspect per `slot-spec.md`); variation images when variants exist. A grid card without an identity image: (identity, square, one per product); never stock or generated; the card is left out until then. | one product: BuyBox, with VariantSwatches when the colour axis carries images (resolve variant imagery from the live purchase contract). Two to five products: an HTML grid with QuickAdd per card, or ProductCarousel with quick add and entry animation off (N10); both need cart v2. The struck price carries `data-source="compare_at_price"` or the ledger row id; saving as text, no pill (N9). Decision inputs: eligible product count, variant axes, cart v2. | saving line per `references/offers/price-presentation.md` PP10 (currency first over the Rule-of-100 line); CTA "Add to cart" or "Add both to cart" for BOGO; two microcopy lines (code status, returns on promo items). | eligible product count; `offer.compareAtBasis`; `lexsis_cart.get`. |
| `product-spotlight` (`-gift`) | the gift as a product with name, image, retail value, threshold and live stock. | yes, gift identity and included-items from the gift SKU's catalog media; packaging when boxed. Missing gift image: never a generated gift render; no image means no gift module and no gift claim until it arrives. View the gift photo to confirm it is the real gift SKU, not a sibling. | InventoryIndicator bound to the gift variant so "while supplies last" reads live and the gift line comes off when it reads out; no purchase island, the gift is auto-added by the discount configuration, never theme script (`offer-types.md` OF11). | "Free travel kit ($30 value) on orders over $75" (retail value, never cost); CTA "Claim your free [gift]" only here. | gift SKU media, price and inventory; `offer.stockVerified`. |
| `trust-bar` or `review-summary` | rating plus count, one guarantee or policy fact, at most one linked press quote. | none; text facts with the page's single icon set or none; press as linked text, never unlinked logos. | none; the review summary from the API total for the exact product per `reviews-sourcing.md` bands. | four facts of six words or fewer. | band from step 4; `policy-fact` rows. |
| `benefits` | three statements on why the product is worth having at this price. | yes, one in-use image beside the three facts from catalog media not used in the hero, library `lifestyle`, or merchant upload. Missing media: (in-use, landscape, one shot); generation of an in-use scene is not feasible (GP14); merge into the trust strip as the agreed alternative. No-go: three icon tiles, a colour band. | none. | three items of 18 words, each with a number, material, time or test. | in-use image found in steps 2 and 6. |
| `countdown` | the real end inside the final 48 hours; otherwise the end date is text in `offer`. | none. | CountdownTimer bound to `offer.endsAt`, hiding itself at zero while the price reverts server-side, beside the primary CTA; the Countdown island is deprecated; never client-side dates, never a reset (`references/offers/urgency-scarcity.md` UR2, UR7) | "Ends Sunday 11:59pm IST" beside the timer; never "Hurry". | `offer.endsAt` confirmed and now within 48 hours of it. |
| `guarantee` or `shipping-returns` | returns on promotional items, shipping cost or threshold, delivery estimate. | none. | DeliveryEstimate for single-zone domestic shipping only, else none. | 40 words; "expected delivery by [date]". | `policy-fact` rows; shipping zones. |
| `faq` | stacking, expiry, returns on promo items, gift swap, eligibility. | none. | none; native `<details>`. | four to six questions; answers 50 words. | ledger terms. |
| `final-offer` | restate the offer, the terms in one line, the CTA. | the hero packshot reused small; no new asset. | none; the CTA anchors to the buy block (one BuyBox per page). | headline repeated verbatim; terms one line of 18 words. | mirrors the hero. |
| `legal`, `sticky-cta` and `footer` | full terms; a bar carrying the offer and price; chrome. | product thumbnail for the bar; brand logo in the footer. | StickyBar in product mode, label identical to the hero CTA, appearing after the buy block, only when the page runs past about three mobile screens; Footer with the terms link as a column item. | the bar label carries the price after the offer. | page length; terms URL. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | identity of the product and, for `gwp`, of the gift; variation per variant | gift beside product, both BOGO items together, one in-use | reuse two catalog identity images side by side in HTML; ask the merchant to upload an in-use shot or the gift image; skip benefits only on the merchant's call |
| asset library | `product-shot`, `flat-lay` of product plus gift, one `lifestyle` in-use | gift `packaging` | ask the merchant to upload; the gift module waits for the gift image |
| generation | nothing on this type in practice (backdrops only, below the fold, ASK because the hero is a `packshot`) | product, gift, people, results, logos, text | never |

Minimal assets (one packshot): hero, offer terms, buy box, review summary or policy facts, guarantee, native FAQ, final offer; benefits wait on an in-use shot and a `gwp` waits on its gift image, both listed in the plan and draft summary. Generated assets on an offer page: zero; the house cap of four is never approached.

## Above the fold (390px)

In order: header, offer headline in plain arithmetic, product packshot (no
more than 60% of viewport height), the price line (struck compare-at with
basis, sale price, saving), code shown or "applied at checkout", the primary
CTA, one guarantee or shipping line under it. The terms line is within the
next screen. Not above the fold: a countdown outside the final 48 hours, an
email popup, a percent-off pill, education copy, a second competing offer.

## Proof

- Modules: 1 to 3. Module one is `review-summary` (average plus count) in the
  trust strip or hero. Module two is `policy-fact` or `guarantee` (returns on
  promo items, shipping). Module three, optional, is one `press-quote-linked`
  or one `review-quote` beside the strongest product claim.
- Minimum evidence per kind: `references/proof/proof-ledger.md`. The offer is
  the message; proof confirms the product is worth having at the offered
  price and does not need to carry the page.
- Threshold offers: the progress toward the threshold shows in the cart
  profile, not as a claim on the page.
- No reviews: guarantee and returns facts, certifications with issuer.
  Nothing review-shaped.

## Offer and CTA

- CTA count: 2 to 3. Hero CTA, optional CTA after the product block, final
  offer CTA. All identical in label and destination.
- First CTA position: hero (section index 0 of the body).
- Sticky: optional; label carries the offer or the price.
- CTA copy: "Claim your free [gift]" on a gift module; "Add to cart" or "Add
  both to cart" on product blocks; "Get 20% off my first order" is acceptable
  when the code is auto-applied. Never "Unlock", "Grab", "Snag", "Buy Now".
- Price reveal: immediate; the offer is the headline. Compare-at struck text
  only with a verified basis (`price-presentation.md` PP1); saving in currency
  first over the Rule-of-100 line, percent first under it, both when space
  allows (RESEARCH, Berger; JBR 2015
  https://www.sciencedirect.com/science/article/abs/pii/S0148296315003513 ).
- Code handling: auto-apply from the URL and pre-fill in cart (OPERATOR, Cozy
  Earth creator pages auto-apply; Nik Sharma: show the code as an action
  "auto-applied at checkout" https://sharmabrands.com/blogs/newsletter/7-biggest-landing-page-mistakes ).
  A code that fails at checkout is the page's most damaging failure.
- Terms travel with the offer: exclusions, stacking, minimum spend, regions,
  end date within one scroll; LAW, FTC 16 CFR 251.1 requires conditions of a
  "Free" or gift offer "at the outset, in close conjunction with the offer",
  not by asterisk https://www.law.cornell.edu/cfr/text/16/251.1 ; India CCPA
  drip pricing https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf .
- Thresholds: 15 to 30% above current AOV, reachable with one small add-on
  (HEURISTIC; OPERATOR 1.5x AOV best revenue per session in a 14-store test
  https://www.72technologies.com/blog/free-shipping-threshold-bar-ab-test-results ).
- Countdown: only bound to a ledger `endsAt` the merchant confirmed, only in
  the final 24 to 48 hours, price reverting server-side at that instant
  (`urgency-scarcity.md` UR2, UR7). Before that window the end date is text.
- Gift with purchase: gift named and pictured with its retail value, never
  cost; "while supplies last" only with live gift stock via `stock-indicator`;
  banner and gift line removed when the gift sells out (`offer-types.md` gwp).
- Offers that fit: `percent-off`, `fixed-off`, `bogo`, `gwp`,
  `free-shipping`, `tiered-volume`, `bundle`, `first-order`, `cashback`,
  `bnpl`, `none` (a "no discount, complimentary gift wrap" courtesy page).
- Offers that do not fit: `referral` (the visitor has not bought),
  `flash-sale` and `clearance` (route to `sale-clearance-flash` when more
  than five SKUs; a single-SKU deadline is `percent-off` or `fixed-off` with
  an `endsAt`), `mystery`. `subscribe-save`, `bundle-decoy`, `trial-sample`,
  `loyalty`, `limited-edition`, `gift-card`, `pre-order-price`, `price-lock`,
  `student-military` and `charity` are `ask` in `offer-types.md` and need the
  merchant's confirmation recorded in the ledger.
- One offer per page (`offer-types.md` OF1). Two offers means two pages or a
  `sale-clearance-flash`.
- Luxury never shows a percent, a struck price or a timer (OF3); the offer
  page for a prestige brand is a gift, early access or complimentary service.

## Imagery

- Required jobs: `identity` (the product), plus `included-items` when the
  offer includes a gift or a bundle (the gift pictured beside the product).
  Recommended: `in-use`, `scale`, `variation` when variants exist,
  `packaging` for a gift, `ugc` when rights exist.
- Hero: `packshot`; alternate `product-in-hand`. Never bake the offer text
  into the image; the offer is HTML text over or beside it.
- Minimum images: 3 (identity, gift or bundle contents when applicable,
  in-use). No lifestyle storytelling; the shopper knows the product.
- Balance: studio-led; one in-use image is enough.
- Video: forbidden. A most-aware visitor needs the price, the terms and the
  button, not a demo.
- Slots the plan creates: one `included-items` slot when a gift or bundle has
  no image; never a generated gift render.

## Copy

- Framework: `aida` compressed to attention (the offer), desire (three
  benefits), action; the direct-offer posture for most-aware readers
  (`_index.md` section 5).
- Headline: `[depth or gift] [scope], [terms or end]` in plain arithmetic:
  "Buy one serum, get one free. Add both to cart." "Free travel kit ($30
  value) on orders over $75." "30% off the starter set, ends Sunday 11:59pm
  IST."
- Reading level grade 6 to 8; 200 to 500 words total.
- Length ceilings: hero subhead 16 words; terms block 3 lines of 18 words;
  benefits 3 items of 18 words; FAQ answers 50 words.
- Vocabulary: plain arithmetic ("buy 2, get 1 free") over derived percent
  ("33% off"); "applied automatically" over "use code"; "expected delivery by
  [date]"; loss framing ("your $30 discount ends Sunday") only when the end
  is real. Never "up to X%" when a flat number exists; never "Hurry", "Don't
  miss out", "LIMITED TIME"; never "free" with an asterisk.
- Microcopy under the CTA: code status, guarantee, shipping cost or
  threshold, returns on promo items.

## Never

- Never make the shopper calculate the saving; show it computed.
- Never show a code that fails at checkout or differs from the URL parameter.
- Never bury exclusions, stacking or minimum spend in the footer.
- Never show "up to X%" when one flat depth applies or when few SKUs sit at
  the maximum.
- Never render a countdown without a ledger `endsAt`, outside the final 48
  hours, or one that resets.
- Never say "while supplies last" without live gift stock bound to the
  banner.
- Never show a gift without its name, image and retail value.
- Never show a percent, a struck price or a timer on a luxury or prestige
  brand.
- Never run two offers on one page.
- Never add education sections; most-aware visitors leave when made to
  re-read the premise.
- Never cover the offer with an email popup.
- Never discount every retargeting touch; it trains waiting (OPERATOR).
- Never show a first-order code to a known returning customer.
- Never render "31% OFF" or "BEST VALUE" as a pill; struck text and a plain
  saving line only (`design-rules.md` N9).

## Examples

- Hims, post-quiz subscription offer page (breakdown)
  https://www.convertflow.com/campaigns/hims-full-funnel-marketing-examples-templates :
  monthly framing with the crossed-out regular price, the saving beside the
  price, a simple offer ladder, terms adjacent.
- Cozy Earth creator pages (case study)
  https://creatorcommerce.shop/brand-case-studies/cozy-earth : creator code
  auto-applied from the link, product and offer in the first screen, no
  re-education; +214% conversion and +67% AOV reported by the vendor.
- Ace Vanity, Raksha Bandhan offer https://acevanity.in/pages/rakshabandhan-sale-2026 :
  one offer stated as arithmetic ("Pay ₹4,000, gift ₹5,000"), terms beside
  it, no competing offers.

## Checklist

```json
{
  "page_type": "offer-page",
  "aliases": ["promo page", "deal page", "code page", "claim your offer", "welcome offer page", "GWP page"],
  "funnel_stage": ["mof", "bof"],
  "awareness": ["product-aware", "most-aware"],
  "traffic": ["email", "sms", "retargeting", "influencer", "direct"],
  "sections": { "min": 6, "max": 9 },
  "mandatory_sections": ["header", "hero", "offer", ["buy-box", "product-spotlight", "product-grid"], ["trust-bar", "review-summary"], ["guarantee", "shipping-returns"], "final-offer", "footer"],
  "recommended_sections": ["benefits", "faq", "legal", "sticky-cta"],
  "forbidden_sections": ["problem", "agitation", "discovery", "story", "mechanism", "science", "quiz", "email-capture", "offer-bridge", "hook"],
  "nav": "minimal",
  "price_above_fold": "required",
  "cta": { "min": 2, "max": 3, "first_after_section": 0, "sticky": "optional", "copy_pattern": "claim-offer" },
  "proof": { "min_modules": 1, "max_modules": 3, "required_kinds": ["review-summary"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity"], "hero": "packshot", "video": "forbidden", "min_images": 3 },
  "copy_framework": ["aida"],
  "offer_compat": { "allowed": ["percent-off", "fixed-off", "bogo", "gwp", "free-shipping", "tiered-volume", "bundle", "first-order", "cashback", "bnpl", "none"], "forbidden": ["referral", "flash-sale", "clearance", "mystery"] },
  "urgency": "verified-only"
}
```

`countdown` is conditional, not forbidden: it renders only with a ledger
`endsAt`, inside the final 48 hours, and is removed at the deadline. When
`proof.required_kinds` cannot be met (no reviews), the module count falls to
`guarantee` or `policy-fact` only; never fabricate to hit the minimum.

## Sources

- FTC 16 CFR 251.1 (Free and gift offers) https://www.law.cornell.edu/cfr/text/16/251.1 ;
  16 CFR 233.1 (deceptive pricing) https://www.law.cornell.edu/cfr/text/16/233.1
- India CCPA Dark Patterns Guidelines 2023 https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf
- Berger, Rule of 100 https://jonahberger.com/fuzzy-math-what-makes-something-seem-like-a-good-deal/ ;
  JBR 2015 replication https://www.sciencedirect.com/science/article/abs/pii/S0148296315003513
- Chen et al. 2012, bonus packs beat equivalent price cuts https://doi.org/10.1509/jm.10.0443
- Free-shipping threshold test https://www.72technologies.com/blog/free-shipping-threshold-bar-ab-test-results
- GWP vs discount popup test https://convertibles.dev/blogs/case-studies/free-gifts-vs-discounts-popup-offers-case-study
- Offer page and flash sale checklist https://onsale.marketing/flash-sale-landing-page-checklist
- Urgency evidence https://www.heartly.io/blog/urgency-marketing-guide ;
  countdown evidence review https://cleancommit.io/blog/do-countdown-timers-work/
- Nik Sharma, landing page mistakes (code as an action) https://sharmabrands.com/blogs/newsletter/7-biggest-landing-page-mistakes
- Shopify Buy X Get Y mechanics https://help.shopify.com/en/manual/discounts/discount-types/buy-x-get-y
- Sibling references: `references/offers/offer-types.md` (OF1, OF2, OF3, OF5, OF11, OF12),
  `references/offers/offer-ledger.md`, `references/offers/price-presentation.md`,
  `references/offers/urgency-scarcity.md`, `references/design-rules.md` (N9),
  `references/proof/proof-ledger.md`, `references/assets/image-jobs-by-page-type.md`
