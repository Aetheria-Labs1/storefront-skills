# Trial and sample page

A low-risk first purchase (a sample, a discovery set, a home try-on, a
starter size) for a shopper who knows the category but not this product and
fears it will not work for them. Traffic is paid social or email; awareness is
solution-aware; stage is tof or mof. The page sells the trial, not the full
product, and its first job is to state what happens after the trial: nothing,
a full-size purchase they choose, or an auto-conversion with a date, price and
cancel path stated before the button. A fee on a "free" trial is explained in
the same phrase.

## Identify it

- Brief says "sample", "trial", "try before you buy", "home try-on",
  "starter kit", "discovery set", "try it free", "pay only shipping", or
  names fit, taste, shade or efficacy risk as the objection.
- Categories with high return anxiety: eyewear, apparel fit, fragrance,
  skincare actives, supplements, coffee, mattresses.
- Near neighbours:
  - `subscription`: the recurring plan is the subject; choose trial when the
    first order is a sample and the plan is optional.
  - `ad-landing-page`: a full-price product sold on one story; choose trial
    when the CTA is the sample, not the product.
  - `quiz-funnel`: answers route to a recommendation; a trial page may embed
    a fit quiz as one section, but the page's job is the trial start.
  - `pdp` with a guarantee: a 100-night trial on a mattress PDP is a
    risk-reversal fact on a `pdp`, not this type.
  - `lead-capture-giveaway`: a free item for an email with no purchase.

## Variants

- **Paid sample.** Small size at a small price ("Try the 15ml for $8"),
  full-size price visible, credit toward full size where the merchant offers
  it.
- **Free plus shipping.** "Free sample, $3.95 shipping" in one phrase; the
  reason for the fee answered in the FAQ ("Why is there a $3 fee?").
- **Home try-on.** Several items shipped, a return window, a prepaid label,
  a hold or deposit stated with its release date (Warby Parker's five frames
  for five days, now replaced by virtual try-on and a quiz).
- **Trial that converts.** The sample is the first delivery of a plan;
  conversion date, price and cancel path sit beside the CTA and are the first
  FAQ answer. LAW: FTC 16 CFR 251.1 requires the shipping charge on a "free"
  offer at the outset https://www.law.cornell.edu/cfr/text/16/251.1 ; US ROSCA
  requires material terms before billing information and simple cancellation
  https://www.ftc.gov/business-guidance/blog/2024/10/click-cancel-ftcs-amended-negative-option-rule-what-it-means-your-business ;
  India CCPA lists forced payment details for a free trial under "subscription
  trap" https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf .

## Anatomy

Counts exclude chrome. Order follows the Warby Parker home try-on flow and
the trial rules in internal research audit (2026-09-10) type 30 and
internal research audit (2026-09-10) section 1.14.

1. `header`: mandatory, minimal.
2. `hero`: mandatory. The trial offer in one line ("Pick 5 frames. Try them
   free for 5 days."), what it costs (free, shipping only, refundable deposit)
   in the same line, the CTA naming the trial, and a one-sentence "what
   happens after" directly under it.
3. `pricing`: mandatory. Trial price, shipping fee and its reason, full-size
   price, credit toward full size if any, and for a converting trial the
   conversion date, recurring price and cancel path. Within one scroll of the
   hero.
4. `how-it-works`: mandatory. Three or four steps with a timeline: choose,
   we ship, try, keep or return with the prepaid label (or "nothing happens;
   buy the full size if you like it"). The after-trial step is always the
   last step and is never omitted.
5. `product-spotlight`: mandatory (what is in the kit). Every item, sample
   size shown to scale against the full size, one line on what each is for.
6. `product-finder` or `size-guide`: conditional: fit, shade or size risk.
   A short quiz or sizing tool that changes which sample ships; virtual try-on
   where the merchant has it.
7. `testimonial-spotlight` or `reviews`: mandatory. Trier quotes ("I kept
   the tortoiseshell") verbatim and dated; the review list where 20 or more
   exist; count of trials shipped only from an export.
8. `guarantee` or `shipping-returns`: mandatory. Return window, prepaid
   label, no-charge or refund rules, hygiene policy where relevant, stated in
   short form near the hero and in full here.
9. `faq`: mandatory. First question is the post-trial terms ("What happens
   after the 14 days?" or "Will I be charged?"), then "Why is there a $3
   fee?", shipping both ways, hygiene, timing, how to cancel.
10. `closing-cta`: mandatory. Trial CTA repeated with the cost and the
    after-trial sentence.
11. `sticky-cta`: optional; carries the trial price.
12. `legal`: recommended chrome; full terms link; material terms are already
    in `pricing`.
13. `footer`: mandatory chrome.

Never include `countdown`, `stock-indicator`, `final-offer`,
`bundle-builder`, `quantity-breaks`, or a `subscription-toggle` that is
pre-selected. A trial page that runs a timer is selling pressure, not a
trial.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.get` for the trial SKU: `media[]` mapped per `references/assets/image-jobs-by-page-type.md` (identity, scale, that is the sample in hand or beside the full size, included-items, in-use, packaging, label); price; variants (shade or size chosen by the finder); selling plans when the trial converts into a plan. Then `lexsis_catalog.get` for the full-size SKU: price and identity for the scale comparison and the credit line.
2. Offer ledger `trial-sample` row (`references/offers/offer-types.md` trial-sample, OF5; `references/offers/price-presentation.md` PP27): trial price, shipping fee and its reason, full-size price, credit toward full size, and for a converting trial the conversion date, recurring price and cancel path, each confirmed by the merchant. `lexsis_cart.get`: the fee the cart will actually charge, cart v2.
3. `lexsis_catalog.reviews_status`; `lexsis_catalog.reviews_search` with `query` "sample", "trial", "kept", "full size", "tried" for trier quotes (`pending` until confirmed); `lexsis_catalog.reviews` for the band; `review_collections` (`references/proof/reviews-sourcing.md`). Result claims in quotes need typicality wording in the same block.
4. `lexsis_brand.context`, `lexsis_brand.brand_kit`, `lexsis_brand.navigation` (minimal nav).
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"` for `product-shot`, `flat-lay`, `lifestyle`, `social-proof`; then semantic "<product> sample in hand", "next to full size". Sequence and checks: `references/assets/asset-sourcing-sequence.md`.
6. `lexsis_capture.funnel_templates` then `lexsis_capture.funnel_template` when a fit, shade or size finder decides which sample ships; the finder is one section, not the page. `lexsis_design.islands`, then `lexsis_design.island_schema` for each island named below.
7. No generation is planned on this type: identity, scale and included-items are identity-bound and the hero is `product-in-hand`.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `header` | minimal chrome. | brand logo or wordmark. | SiteHeader minimal with the CTA anchoring to the trial block. | store names. | `lexsis_brand.navigation`. |
| `hero` | the trial in one line with its cost, the CTA naming the trial, the "what happens after" sentence, the sample shown in hand at scale. | yes, scale and identity (`product-in-hand`; alternate `packshot`): catalog media, library `product-shot` or semantic "in hand", merchant upload of the sample beside the full size. Never generated (GP14 forbids generated scale), never a lifestyle hero, never the full-size product as the hero image. Missing scale shot: (scale, portrait, one phone photo of the sample beside the full size is enough at 1600 px); the packshot ships meanwhile and the slot stays `planned`. | BuyBox for the trial SKU, compact for one variant, default when a shade or size is chosen; a converting trial keeps the selling plan out of the default state, with the conversion terms as HTML beside the button and a separate un-ticked consent checkbox in the same block; never a pre-selected SubscriptionToggle. | trial line 14 words with its cost in the same phrase ("Free sample, $3.95 shipping", PP27); after-trial sentence 18 words directly under the CTA; vocabulary per `references/anti-patterns/copy-anti-patterns.md`. | scale image found in steps 1 and 5; ledger row from step 2. |
| `pricing` | trial price, fee and reason, full-size price, credit, and conversion terms, within one scroll of the hero. | optional scale image reused beside the table; the table is an object and may stand alone. | none; an HTML table; any struck price carries `data-source`. | five labelled figures; "on day 15 your card is charged $45 for the full size; cancel any time before in your account" when a conversion exists. | ledger row; `lexsis_cart.get` fee. |
| `how-it-works` | choose, we ship, try, keep or return with the prepaid label (or "nothing happens"); the after-trial step is always last. | yes, sequence and packaging: real frames of the box, the sample, the prepaid label from catalog media or merchant upload; library `flat-lay`; an inline SVG flow authored in HTML when frames are missing. Never generated frames. Missing media: (packaging and label photos, count); the SVG flow ships meanwhile. View the frames in order so they read as one flow. | none; optional click-to-play how-it-works video per `references/assets/video-rules.md`. | three or four steps of 22 words; timeline stated ("arrives in 3 to 5 days", "14 days to try"). | packaging and label imagery from steps 1 and 5. |
| `product-spotlight` | what is in the kit: every item, sample size shown to scale against the full size, one line on what each is for. | yes, included-items flat lay and identity per item from catalog media, library `flat-lay`, or merchant upload; the scale image here if not used in the hero. Never a generated sample render. Missing: per item (identity, square) and for the flat lay (landscape); under a delegated brief the rows ship text-only and are listed under Unresolved assets. | none (HTML rows), or ProductCarousel in compact row form for kits of three to five items, quick add off, animation off. | item line 16 words; sizes stated in ml, g or count. | kit item count; flat lay found. |
| `product-finder` or `size-guide` | a short quiz or sizing tool that changes which sample ships. | yes for a finder: answer options carry real swatch or variation images from catalog variant media (shade on skin for colour cosmetics); text options for use-case questions; never stock people as "you". A size guide is an HTML table, an image only when the merchant's chart cannot be transcribed. Without swatches, use text options while the slots remain planned. | FunnelRuntime inline, built from a `lexsis_capture.funnel_template` through `lexsis_drafts.funnel_create`, validated with `lexsis_capture.validate_funnel` and checked with `lexsis_capture.preview_funnel`, its result pre-selecting the BuyBox variant; SizeGuide only when the merchant supplies measurements. | questions 12 words; options 4 words; "why we ask" 16 words. | fit, shade or size risk named in the brief; a template available. |
| `testimonial-spotlight` or `reviews` | trier quotes naming what they kept or bought, verbatim and dated. | trier photos only from records with rights (`social-proof` with a `P` row, or `has_media` reviews); avatars real or CSS initials. | by band per `references/proof/reviews-sourcing.md`: B1 static verbatim dated cards; B2 ReviewCarousel one card at a time, autoplay off (N10), bound to the trial id or an active collection; B3 or more ReviewList with filters. Confirmed `reviews_search` candidates only. | quote 60 words; a typicality line in the same block for any result claim; "over 40,000 trials shipped" only from an export. | band and confirmed candidates from step 3. |
| `guarantee` or `shipping-returns` | return window, prepaid label, no-charge or refund rules, hygiene policy; short form near the hero, full here. | the prepaid label or return packaging photo from how-it-works reused; no new asset. | DeliveryEstimate for single-zone domestic shipping, else none. | 60 words; "prepaid return label", "expected to arrive in 3 to 5 days". | `policy-fact` rows. |
| `faq` | the first question is the post-trial terms ("Will I be charged?"), then the fee reason, shipping both ways, hygiene, timing, how to cancel. | none. | none; native `<details>`. | answers 60 words; the first sentence is the answer. | ledger terms. |
| `closing-cta` and `sticky-cta` | the trial CTA repeated with cost and the after-trial sentence; a bar with the trial price. | the hero in-hand image reused small; product thumbnail for the bar. | the closing CTA anchors to the trial block (one BuyBox per page); StickyBar in product mode with the trial label, animation off, only when the page runs past about three mobile screens. | the label identical to the hero CTA; the after-trial sentence repeated. | page length. |
| `legal` and `footer` | full terms link; chrome. | brand logo. | Footer with the terms as a column link. | "Trial terms". | terms URL. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | identity of the sample and the full size, sometimes a kit flat lay | the sample at scale in hand or beside the full size, packaging and prepaid label, sequence frames | ask the merchant to upload (a phone photo of the sample beside the full size is enough at 1600 px); SVG flow for how-it-works meanwhile; scale and included-items slots stay `planned`, never generated |
| asset library | `product-shot`, `flat-lay` kits, one `lifestyle` in-use, `social-proof` trier UGC with rights | scale and packaging | ask the merchant to upload |
| generation | nothing on this type (scale, identity and included-items are identity-bound; the hero is `product-in-hand`) | the sample, the kit, people, results, text | never |

Minimal assets (one packshot of the sample): packshot hero with the BuyBox and after-trial sentence, pricing table, SVG how-it-works, kit items as text rows flagged for images, trier quotes or static cards by band, policy facts, native FAQ; every missing shot is listed in the plan and draft summary, and the finder waits for a template. Generated assets on a trial page: zero.

## Above the fold (390px)

In order: header, the trial line with its cost, the CTA naming the trial, the
"what happens after" sentence, the sample shown in hand at scale (no more than
60% of viewport height), a trier review summary with count when 5 or more
exist. The full pricing block is within the next screen. Not above the fold:
the full-size product pitch, a countdown, a pre-ticked plan, "free" without
its fee, an email popup.

## Proof

- Modules: 2 to 3. Module one is `review-quote` from triers, verbatim, dated,
  naming what they kept or bought. Module two is `policy-fact` (return window,
  prepaid label, refund rule) placed beside the CTA. Module three is
  `review-summary` or `ugc-photo` (trier photos with rights; the Warby Parker
  home try-on hashtag produced over 50,000 posts, per the G&Co case study
  https://www.g-co.agency/insights/warby-parker-advertising-and-marketing-strategy-case-study ).
- `customer-count` for "over 40,000 trials shipped" needs an export, rounded
  down, dated.
- Result claims in trier quotes ("cleared my skin in 10 days") trigger the
  typicality rule; substantiate or state generally expected results in the
  same block (FTC Endorsement Guides).
- No reviews: guarantee and return facts as the proof, certifications with
  issuer, a founder note. Nothing review-shaped.

## Offer and CTA

- CTA count: 2. Hero CTA and closing CTA, identical label and destination.
- First CTA position: hero (section index 0 of the body).
- Sticky: optional; carries the trial price ("Start my trial, $8").
- CTA copy names the trial: "Start my 5-day home try-on", "Try the 15ml for
  $8", "Get my sample, $3.95 shipping". Never "Buy Now", "Get started",
  "Claim", "Unlock".
- Price reveal: immediate. Trial price and any fee in the headline or the
  line beneath; full-size price visible in `pricing` so the trial is
  understood as a step, not the product.
- Terms adjacent to every CTA: return window, refund rule, and for a
  converting trial the conversion date, recurring price and cancel path in the
  same block (`references/anti-patterns/dark-patterns.md`, subscription trap;
  `offer-types.md` trial-sample).
- "Free" rules: LAW, FTC 16 CFR 251.1; UK banned practice on "free" with
  costs beyond the unavoidable response cost; EU UCPD Annex I point 20. "Free
  sample, $3.95 shipping" in one phrase, never "Free" with an asterisk
  (`price-presentation.md` PP27).
- Consent: a converting trial has a separate, un-ticked consent line stating
  the recurring charge; payment details for a "free" trial are asked only
  after the conversion terms are shown.
- Offers that fit: `trial-sample` (default), `free-shipping`, `none`,
  `subscribe-save` only when the trial converts into a plan and the terms are
  stated as above.
- Offers that do not fit: `percent-off`, `fixed-off`, `bogo`, `gwp`,
  `bundle`, `bundle-decoy`, `tiered-volume`, `first-order`, `flash-sale`,
  `clearance`, `mystery`, `bnpl`, `cashback`, `pre-order-price`,
  `limited-edition`, `referral`, `gift-card`. The trial is the offer; a second
  offer on top confuses what the shopper is agreeing to.
- Urgency: none. No timers, no stock counts, no "spots left".
- Guard metric: trial-to-full conversion and return rate together; a page
  that lifts starts and raises returns has failed.

## Imagery

- Required jobs: `identity` (the sample), `scale` (the sample against the
  full size or in hand), `included-items` (every item in the kit). Recommended:
  `in-use`, `sequence` (choose, ship, try, return), `packaging` (what arrives,
  the prepaid label), `ugc` when rights exist, `label-or-facts-panel` for
  regulated consumables.
- Hero: `product-in-hand` with the sample at scale; alternate `packshot`.
  Never an editorial lifestyle hero; the shopper needs to see how small the
  sample is and what arrives.
- Minimum images: 4 (identity, scale against full size, included-items,
  in-use).
- Balance: studio-led with one in-use image; UGC where rights exist.
- Video: optional; a 45 to 90 second how-it-works as click-to-play with a
  poster; never autoplay with sound; never the hero.
- Slots the plan creates: a `scale` slot when no sample-versus-full-size image
  exists; an `included-items` slot when the kit has no flat lay; never a
  generated sample render.

## Copy

- Framework: `bab` (before: uncertainty about fit, taste or effect; after:
  confidence; bridge: the trial), `fab` for kit contents.
- Headline: the trial in one line with its cost: "Try 5 frames at home for 5
  days. Free, returns prepaid." "Try the serum for 14 days, $8, credited to
  your full size."
- Reading level grade 6 to 8; 300 to 600 words total.
- Length ceilings: hero line 14 words; after-trial sentence 18 words;
  how-it-works step 22 words; kit item line 16 words; FAQ answer 60 words,
  first sentence is the answer.
- Vocabulary: "nothing happens after 14 days unless you buy" or "on day 15
  your card is charged $45 for the full size; cancel any time before in your
  account"; "prepaid return label"; "expected to arrive in 3 to 5 days".
  Never "risk-free" without the refund rule, "free" without its fee,
  "limited spots", "no commitment" when a conversion exists.
- Microcopy under the CTA: cost, return window, refund rule, conversion terms
  where applicable, shipping time.

## Never

- Never hide the shipping or restocking fee behind "free".
- Never auto-convert a trial without the date, price and cancel path stated
  before the CTA and a separate un-ticked consent.
- Never ask for payment details for a "free" trial before showing the
  conversion terms.
- Never leave kit contents or sample size unstated.
- Never sell the full product instead of the trial in the hero.
- Never make the trier re-select variants when converting to full size.
- Never render a countdown, stock count or "spots left".
- Never place the post-trial terms anywhere but the first FAQ question and
  the pricing block.
- Never show result claims in trier quotes without typicality wording.
- Never stack a second offer on the trial.
- Never call a converting trial "no commitment".
- Never omit the return path (prepaid label, window, hygiene rule) from the
  first screen's neighbourhood.

## Examples

- Warby Parker, Ways to try https://www.warbyparker.com/ways-to-try : the
  trial mechanics in one line each (virtual try-on, quiz, in-store), returns
  and the prepaid path stated plainly; the retired home try-on stated "Pick
  5 frames. Try them free for 5 days." with the cost in the headline.
- Ridge, Carbon Fiber Wallet https://ridge.com/products/carbon-fiber :
  "Try it for 99 days, no questions asked" as the risk-reversal line beside
  the price and repeated at four depths; a trial framing on a full-price PDP
  that shows how the terms travel with the CTA.
- Klassy Pet, VIP Reservation https://klassypet.com/products/klassy-vip-reservation :
  a refundable $3 deposit with "Why is there a $3 fee?" answered in the FAQ
  and "Fully refundable" under the CTA; the fee-reason pattern this type
  requires. Avoid its missing product imagery.

## Checklist

```json
{
  "page_type": "trial-sample",
  "aliases": ["free sample page", "trial kit page", "home try-on", "discovery set", "try before you buy", "starter kit"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["solution-aware"],
  "traffic": ["meta", "tiktok", "email"],
  "sections": { "min": 6, "max": 9 },
  "mandatory_sections": ["header", "hero", "pricing", "how-it-works", "product-spotlight", ["testimonial-spotlight", "reviews"], ["guarantee", "shipping-returns"], "faq", "closing-cta", "footer"],
  "recommended_sections": [["product-finder", "size-guide"], "legal", "sticky-cta"],
  "forbidden_sections": ["countdown", "stock-indicator", "final-offer", "bundle-builder", "quantity-breaks", "offer-bridge", "savings-math", "hook"],
  "nav": "minimal",
  "price_above_fold": "required",
  "cta": { "min": 2, "max": 2, "first_after_section": 0, "sticky": "optional", "copy_pattern": "next-step" },
  "proof": { "min_modules": 2, "max_modules": 3, "required_kinds": ["review-quote", "policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked", "stock-count"] },
  "imagery": { "required_jobs": ["identity", "scale", "included-items"], "hero": "product-in-hand", "video": "optional", "min_images": 4 },
  "copy_framework": ["bab", "fab"],
  "offer_compat": { "allowed": ["trial-sample", "free-shipping", "none", "subscribe-save"], "forbidden": ["percent-off", "fixed-off", "bogo", "gwp", "bundle", "bundle-decoy", "tiered-volume", "first-order", "flash-sale", "clearance", "mystery", "bnpl", "cashback", "pre-order-price", "limited-edition", "referral", "gift-card"] },
  "urgency": "none"
}
```

`subscribe-save` is allowed only for a converting trial whose conversion
date, recurring price and cancel path appear in `pricing` beside the CTA and
as the first FAQ answer. `cta.copy_pattern` `next-step` covers "Start my
trial" and "Get my sample"; the label always names the trial and its cost.

## Sources

- FTC 16 CFR 251.1 (Free offers and shipping charges) https://www.law.cornell.edu/cfr/text/16/251.1
- FTC ROSCA and negative option guidance https://www.ftc.gov/business-guidance/blog/2024/10/click-cancel-ftcs-amended-negative-option-rule-what-it-means-your-business
- India CCPA Dark Patterns Guidelines 2023 (subscription trap) https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf
- UK DMCC subscription contract provisions https://cms.law/en/gbr/legal-updates/game-changing-consumer-protection-provisions-under-the-dmcc-act-come-into-force-are-you-prepared
- FTC Endorsement Guides 2023 (typicality) https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising
- Warby Parker ways to try https://www.warbyparker.com/ways-to-try ;
  G&Co case study https://www.g-co.agency/insights/warby-parker-advertising-and-marketing-strategy-case-study ;
  Growthegy virtual try-on analysis https://www.growthegy.com/2026/04/06/warby-parker-ai-ar-conversion-virtual-try-on-case-study/
- Offer catalogue trial and sample entry: internal research audit (2026-09-10) section 1.14
- Sibling references: `references/offers/offer-types.md` (trial-sample, OF5),
  `references/offers/price-presentation.md` (PP27), `references/anti-patterns/dark-patterns.md`,
  `references/proof/proof-ledger.md`, `references/assets/image-jobs-by-page-type.md`,
  `references/consumer-behavior-cro.md` (risk reversal, post-purchase clarity)
