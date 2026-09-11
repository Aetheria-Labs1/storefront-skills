# Retargeting warm

The visitor has already seen the product. They viewed the PDP, watched the ad twice, or left a cart, and a Meta or Google retargeting click brings them back. The page skips education, names the objection that stopped them, answers it with narrow proof, restates the offer they already saw, and puts the buy box early. Short, direct, product-aware to most-aware.

## Identify it

Signals in the brief:
- "Retargeting", "remarketing", "came back", "saw the ad already", "visited but did not buy", "abandoned cart", "warm audience".
- Traffic is a retargeting audience on meta or google; the visitor has a prior touch recorded.
- The merchant wants a different angle from the cold page.

Near neighbours:
- `offer-page`: choose it when the offer is the message and objections are secondary (index tie-break: retargeting when the offer is secondary to objection handling).
- `pdp`: choose it for cart and checkout abandoners and branded search. In MHI's practitioner data the PDP beat a landing page for cart abandoners (7.2% against 6.5%) and branded search (6.8% against 5.1%) (OPERATOR, https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/).
- `comparison-us-vs-them`: choose it when the retargeted visitor came from a comparison or blog visit and is still evaluating.
- `ad-landing-page`: choose it when the brief is silent on stage; the type that assumes less wins.

Segment before building (OPERATOR, Conversion Bros, https://conversionbros.com/retargeting-landing-pages-how-to-convert-warm-audiences/): content or blog visitors get an educational or comparison page; PDP and pricing viewers get this page; cart and checkout abandoners get the PDP or a risk-reversal variant of this page. One page for all segments is the first mistake.

## Variants

- **Objection page (PDP viewers).** The default. The one objection this segment left with, answered head-on: price becomes per-day framing or BNPL; trust becomes hyper-specific testimonials; fit becomes a size guide or FAQ.
- **Risk-reversal page (cart abandoners).** Buy box first with the exact variant they left, guarantee and returns beside it, a completion line ("Your cart is waiting"); no deeper discount than the one they abandoned on (offer-types OF8). Hims' "complete your assessment" flow uses the completion principle with no discount (https://www.convertflow.com/campaigns/hims-full-funnel-marketing-examples-templates).
- **Branded-search landing (most-aware).** Bestseller, guarantee and delivery promise above the fold, no story; the PDP usually wins here (research block 39).

## Anatomy

1. `hero` mandatory. References the prior action ("Still thinking about the Miracle Balm?"), shows the exact product and variant viewed (dynamic where possible), one verified proof number, the price, one direct CTA. No brand introduction, no category explanation.
2. `buy-box` mandatory, early (section 2). Variant pre-selected where known, price, shipping and returns line, the offer restated exactly as previously seen or as risk reversal, guarantee, add-to-cart.
3. `objections` mandatory. The one objection this segment left with, first; then the top three (fit, results timeline, returns) each answered in two sentences with the proof beside it (OPERATOR, internal research audit (2026-09-10) section 5 retargeting rules).
4. `reviews` mandatory. Objection-specific quotes ("saved me 14 hours a month", not "great service"); two to four, dated, attributed; `before-after` beside a results objection only when substantiated and permitted.
5. `guarantee` mandatory. Risk reversal stated in full: days, scope, friction ("60-day returns, used or unused, email us").
6. `faq` recommended. Three to five, compact, early rather than late: price, delivery, "what if it does not work for me".
7. `comparison` conditional: the segment came from a comparison or content visit. A short us-versus-the-alternative table.
8. `closing-cta` mandatory. Same action as the buy box; the last-word quote above it.

A different angle from the cold page is mandatory: if the cold page led with speed, this one leads with proof or risk removal (OPERATOR, landerlab, https://landerlab.io/blog/retargeting-landing-pages). Forbidden: `header` beyond logo plus one utility link (`minimal`; `none` also satisfies the index), `about`, `story`, `founder-note`, `problem`, `agitation`, `mechanism` (all re-education), `product-grid`, `email-capture`, `sms-capture`, `quiz`, `related-reads`. Index length 5 to 8; research 5 to 7; the index governs.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.get` with the product id: the `identity` image per variant (the viewed variant comes from the retargeting URL or platform parameter), `detail` and `scale` media for the objection, `included-items`, variant axes (identify which variant images need coordinated selection), price and compare-at (the ledger records the offer depth the visitor already saw, `references/offers/offer-types.md` OF8), selling plans (subscribe-save allowed), live inventory (the only source for a stock line).
2. `lexsis_campaigns.creatives` and `analyze` for the retargeting ad: the objection angle it leads with (this page must differ from the cold page's angle), the offer it states (never exceeded here), the segment (PDP viewer, cart abandoner, content visitor); `references/copy/message-match.md` for the H1.
3. `lexsis_catalog.reviews_status`, `review_collections` (active), `reviews` (`product_id`, `limit: 100`): band per `references/proof/reviews-sourcing.md`; `reviews_search` with each objection in the visitor's words (fit, results timeline, durability, taste, price) for objection-matched quotes; generic praise is excluded even when verified.
4. `lexsis_brand.context` and `brand_kit` (`theme_id`): tokens, guarantee terms with days, scope and friction, returns and shipping facts, the cart URL for the one utility link. `navigation` is not read; nav is minimal (logo plus the cart link).
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`: `product-shot`, `social-proof`, `before-after` (only with a `P` row), `lifestyle` last; then semantic for the objection image ("<product> close-up of <material>"); view candidates with `lexsis_assets.view`.
6. `lexsis_workspace.credits` is not needed; the hero is a packshot type and nothing on this page is generated.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `hero` | reference the prior action, show the exact product and variant viewed, one verified proof number, the price, one direct CTA. | yes; `identity` or `product-in-hand` in the viewed variant, less scene and more object; dynamic where the platform supplies the variant. Search: catalog media for that variant, then library `product-shot`, then merchant upload. Gap for the viewed variant: ask rule naming the variant; no generation is feasible for the product (GN1); fast-draft shows the default variant's identity image with the variant named in the H1 and lists the gap. No-go: an editorial scene, a brand introduction, a carousel, a countdown, a before-and-after. Confirm the variant by eye against the catalog variant image, never by filename. | `none` for the static image; the header above is plain HTML with the logo and a cart link, no `Navbar` island. On desktop the hero and the buy box may compose as one split section (`ProductHero` beside the `BuyBox`, decided by having two or three variant images), which satisfies "buy box early" and keeps price and add-to-cart in the first viewport. The hero CTA anchors to the buy box when they are separate sections. | H1 at most 12 words naming the product and the visit ("Still thinking about the Miracle Balm?"); a proof number with a ledger row beside the price; guarantee as CTA microcopy; no "learn more" or blacklist words (`references/anti-patterns/copy-anti-patterns.md`). | the variant parameter; `lexsis_campaigns.analyze` angle; `review-summary` or `customer-count` ledger rows. |
| `buy-box` | variant pre-selected, price, shipping and returns line, the offer exactly as previously seen or as risk reversal, guarantee, add-to-cart. | a gallery of two or three from catalog media (`identity` in the viewed variant, `variation`, `detail`) when variants exist. Gap: no generation is feasible in the gallery (GP11). | `BuyBox`, one per page, its form decided by the variant count and axes; `VariantSwatches` to pre-select the viewed variant (coordinate its selection with the main purchase state) and when colour variants carry images. `DeliveryEstimate` for the dispatch cutoff (India pincode copy is static HTML). `InventoryIndicator` only when bound to live inventory. `CountdownTimer` only when a real offer window ends within 48 hours, bound to the ledger's end date, placed here and never in the hero; the old Countdown island is deprecated. `StickyBar` bound to the buy section, carrying the pre-selected variant (linked to the main purchase state), appearing after the buy box scrolls out; recommended because the page is short. | "Add the Medium to cart"; cart abandoners "Complete your order" or "Back to your cart"; per-day or BNPL line under the price when the objection is price and the arithmetic is true; never the first-order code, never a deeper discount than the one abandoned on (`references/offers/offer-types.md`). | variant parameter and axes; offer ledger row with prior depth and end date; live inventory. |
| `objections` | the one objection this segment left with first, then the top three, each answered in two sentences with proof beside it. | yes, one image per objection by kind: fit takes `size-reference` or `scale`; quality or durability takes a `detail` macro; results timeline takes `result-or-context` (a verified before-and-after pair with a `P` row, otherwise a truthful context image); price takes no image, the per-day arithmetic is the visual. Search: catalog media by job, then library `product-shot` and `before-after` (with a `P` row), then merchant upload. Gap for an objection: ask rule naming the objection, job and aspect; no generation is feasible for scale, detail or results (GP14, GN4); the answer runs as two sentences plus its matched quote meanwhile. No-go: icon tiles, a mechanism explainer, generated results. | `none`; `BeforeAfter` for a verified pair with one shared aspect ratio | `4ps`; at most 40 words per objection; the objection named in the visitor's own words from `reviews_search`. | the segment and angle from `lexsis_campaigns.analyze`; `reviews_search` hits; `P` row status. |
| `reviews` | two to four objection-specific quotes ("saved me 14 hours a month", not "great service"). | one `ugc` tile or review screenshot with consent where it exists (`has_media: true`; library `social-proof` with a `P` row). Nothing found: the quotes run as text; generation is never feasible (GN9). | by band per `references/proof/reviews-sourcing.md`. B1: one dated quote that answers the objection, static. B2 and above: an average plus n in the hero and `ReviewCarousel` bound to an active collection built from the confirmed `reviews_search` hits, a short strip near the buy box for one-line quotes or all cards visible for longer ones, autoplay off (its default is on, N10). B0: `guarantee`, `policy-fact`, `test-data` and product evidence answer the objections; the section is omitted and recorded. | verbatim, dated, at most 50 words; every quote names the objection topic. | `reviews_status` band; `reviews_search` candidates confirmed by the merchant or an active collection. |
| `guarantee` | risk reversal in full: days, scope, friction. | no; a certification mark only as issuer artwork with a ledger row. Any logo or mark is still opened with `lexsis_assets.view` before use. | `none`. | "60-day returns, used or unused, email us"; policy URL. | the `guarantee` ledger row. |
| `faq` (recommended, early rather than late) | three to five compact answers: price, delivery, "what if it does not work for me". | no. | `none`; native `<details>` and `<summary>`. | answers at most 50 words. | `reviews_search` on the segment's doubts. |
| `comparison` (conditional: the segment came from a comparison or content visit) | a short us-versus-the-alternative table. | our `identity` image in the header cell; the alternative as an inline SVG silhouette; generation is not feasible (GN8). | `none`; a static HTML table (Tabs is deprecated). | three or four rows, cells at most 6 words, one concession row. | `test-data` rows per cell; the segment. |
| `closing-cta` | the same action as the buy box; the last-word quote above it. | optional reuse of the hero identity slot; no new job. | `none`; the CTA anchors to the buy box. | the same verb and object as the buy box; the whole page under 500 words. | the last-word `review-quote` row. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | `identity` per variant, `variation`, often `detail` | the objection image (`scale`, `size-reference`, a specific `detail`), `included-items` | ask the merchant to upload the objection image (identity-bound, no generation); the answer runs as text plus quote meanwhile |
| asset library | `product-shot`, `social-proof` with rights, `before-after` with a `P` row | a consented proof image for this product | tag search, then semantic; view before assigning; a pair without a `P` row never renders |
| ad creatives | the objection angle and the offer already seen | imagery (the cold page's creative is not reused) | only the angle and offer depth travel to the page |
| generation | nothing on this type | product, people, results, logos, text | never; ask the merchant to upload instead |

With only the viewed variant's identity image the page still ships: hero, buy box with the variant pre-selected, objections as text plus matched quotes, reviews at any band above B0, guarantee, faq and closing; the missing `detail` and proof images are listed with the upload offer, and `comparison` is planned only when the segment needs it. Generated assets: zero on this type.

## Above the fold (390px)

Visible, in order:
1. Logo with one utility link (cart, so abandoners can return to it).
2. H1 referencing the prior visit and the product name, at most 12 words.
3. The product image they viewed, in the variant they viewed.
4. One verified proof number (rating with count, or customer count) beside the price.
5. Price with the offer as previously seen, and the primary CTA, full width, 48px minimum, with the guarantee as microcopy.

Must not appear: a brand introduction, a trust bar re-explaining who the merchant is, a countdown, a stock count, a first-order code, a deeper discount than the visitor already saw, an email popup, a carousel, a "learn more" button. Urgency in the hero of a warm page has no evidence behind it: cart and mini-cart urgency tested flat or negative in Cro Metrics' portfolio (OPERATOR, https://crometrics.com/blog/urgency-that-actually-works/).

## Proof

Density: 2 to 4 modules (index). Research: high but narrow, every proof element answers the objection this segment left with.

| Kind | Where | Minimum evidence |
|---|---|---|
| `review-summary` or `customer-count` | `hero` | API count and average at 5 or more reviews; export with date for counts |
| `review-quote` | `objections` (one per objection) and `reviews` | verbatim, dated, attribution as stored; mentions the objection topic (fit, timeline, durability, taste) |
| `guarantee` or `policy-fact` | `buy-box`, `guarantee`, under every CTA | policy URL, exact terms |
| `before-after` | beside a results objection | merchant-supplied, same subject and framing, consented, timeframe stated, category permitted, never in the hero |
| `test-data` or `certification` | beside a trust objection | report or issuer on file |

Placement: number in the hero, objection-matched quotes at 20 to 60% next to each objection, guarantee at the buy box and the close, last word above `closing-cta`. Forbidden kinds: `social-proof-popup`, `live-viewer-count`, `press-logo-unlinked`. Generic praise is excluded even when verified; a quote that does not name the objection does not earn a slot.

Zero reviews: `references/proof/reviews-sourcing.md` tiers 4 and 5. Objections are answered with `guarantee`, `policy-fact`, `test-data` and product evidence; the `reviews` section is omitted and recorded. A warm visitor who left over trust and finds no proof will not return a third time, so the substitutes are mandatory.

## Offer and CTA

- CTA count: 2 to 3. Buy box, optional repeat after `reviews`, closing. Same verb and object throughout. A sticky bar is chrome and does not count.
- First CTA: hero (`first_after_section: 0`).
- Sticky: optional, recommended for the objection variant because the page is short and the buy box scrolls away quickly; appears after the buy box scrolls out, price in the label, one button, carries the pre-selected variant.
- Copy pattern: `add-to-cart` ("Add to cart", "Add the Medium to cart"); cart abandoners: "Complete your order" or "Back to your cart" (`references/offers/offer-types.md` CTA table). Never a soft CTA ("Learn more", "See how it works"); they already saw how it works.
- Price reveal: immediately, in the hero and the buy box; per-day or per-use framing when the objection is price and the arithmetic is true; BNPL line under the price on goods over about $80 or 3,000 rupees.
- Offer fit: `none` (Hims completes assessments with no discount), `free-shipping`, `gwp`, `bundle`, `subscribe-save`, `bnpl`, `trial-sample`, `loyalty` (early access for known customers), `cashback`, `percent-off`, `fixed-off`, `bogo`, `tiered-volume`, `limited-edition`. Any discount is the same one the visitor already saw or a risk-reversal framing of it; rotate the creative and angle every 14 days rather than deepening the discount (OPERATOR, landerlab).
- Offer misfit: `first-order` (they already saw the welcome offer; offer-types OF8), a deeper discount than the one abandoned on (trains abandonment), `referral`, `pre-order-price`, `gift-card`, `charity`, `mystery`, `clearance`, `bundle-decoy`, `price-lock`, `flash-sale`, `student-military`. Discounting every retargeting page trains customers to wait (OPERATOR, Conversion Bros). `references/offers/offer-types.md` governs.
- Urgency: `verified-only`, never in the hero. A dispatch cutoff line in the buy box is the default; a countdown only bound to `offer.endsAt` in the final 48 hours of a real window and placed at the buy box, not the hero; a stock line only from live inventory. The research note that "earned urgency is credible here" is overridden by the flat-to-negative cart urgency data above and by urgency-scarcity UR14.

## Imagery

Required jobs: `identity`, `detail`. Strongly recommended: `in-use`, `variation` (the variant they viewed), `result-or-context` when substantiated, `ugc` for one review screenshot.
- Hero: `product-in-hand` or a product-on-surface identity shot; less scene, more object. The visitor is managing risk, not discovering (OPERATOR, Levinger, https://sarahlevinger.co/articles/most-creative-strategy-stops-one-layer-too-soon...here-are-7-ways-to-go-deeper). Dynamic product image where the platform supplies it.
- Balance: studio and detail about 60%, in-use and proof 40%; no editorial sprawl.
- Video: optional; one 20 to 40 second review clip beside the trust objection, click to play, captions.
- Minimum images: 3 (identity, detail, one proof image); research range 3 to 5.
- Slots the plan must create: hero identity in the viewed variant; one detail macro for the fit or quality objection; one proof image (review screenshot with consent, before-and-after where permitted, or certificate); buy-box gallery of two or three when variants exist.

## Copy

- Framework: `pas` compressed into the hero (they already feel the problem, so one line names it), then `4ps` (promise, picture, proof, push) through objections and close. Loss framing is acceptable when it states a fact ("Your cart is saved until Sunday"), never when it invents a deadline.
- Headline by awareness: product-aware references the visit and stacks proof ("Still thinking about the Miracle Balm? 30-day returns, 24,000 reviews"); most-aware states product plus offer plus terms ("Your Nightly Serum, 1,299 rupees, free shipping, 60-day returns"). Never a story, never a category explanation.
- Message match: the H1 names the product the visitor viewed; the hero image is that variant; the offer equals the one in the retargeting ad and never exceeds the one previously seen (`references/copy/message-match.md`). A most-aware retargeting click never lands on an educational page.
- Reading level: grade 6 to 8; sentences at most 15 words; the whole page reads in under two minutes.
- Length ceilings: H1 12 words; hero subhead 20; each objection answer 40 words; each quote 50; FAQ answer 50; total 250 to 500 words, shorter than the cold page.
- Vocabulary: direct verbs; the objection named in the visitor's own words from reviews and support tickets; no "learn more", "discover", "explore"; no blacklist words; no exclamation marks; sentence case; guarantee stated with days, scope and friction.

## Never

- Never re-introduce the brand, the category or the problem.
- Never repeat the cold page's angle or copy verbatim.
- Never serve one page to content visitors, PDP viewers and cart abandoners alike.
- Never show the first-order welcome code or a deeper discount than the visitor already saw.
- Never place a countdown, stock count or viewer count in the hero.
- Never render a soft CTA ("Learn more", "See how it works").
- Never render full store navigation; logo plus one utility link at most.
- Never show generic praise as proof; every quote names the objection.
- Never hide the price or the guarantee below the buy box.
- Never run the same offer for more than about 14 days without rotating the angle.
- Never exceed 8 sections or 500 words of body copy.
- Never show a before-and-after in the hero or without substantiation.

## Examples

- Hims "complete your assessment" abandonment flow: references the unfinished action, completion principle, no discount (https://www.convertflow.com/campaigns/hims-full-funnel-marketing-examples-templates).
- MHI Growth Engine landing page against product page by traffic temperature: the PDP wins for cart abandoners and branded search, the landing page for cold and warm prospecting; the basis for segmenting before building (https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/).
- Jones Road Miracle Balm PDP guarantee row (free returns 30 days, free shade matching, free exchanges 45 days) and FAQ that routes the shade objection to a quiz: the objection-first modules a retargeting page borrows (https://www.jonesroadbeauty.com/products/miracle-balm).

## Checklist

```json
{
  "page_type": "retargeting-warm",
  "aliases": ["retargeting landing page", "remarketing page", "welcome back page", "abandoner page", "warm-traffic variant", "objection page"],
  "funnel_stage": ["bof"],
  "awareness": ["product-aware", "most-aware"],
  "traffic": ["retargeting", "meta", "google-search"],
  "sections": { "min": 5, "max": 8 },
  "mandatory_sections": ["hero", "buy-box", "objections", "reviews", "guarantee", "closing-cta"],
  "recommended_sections": ["faq", "comparison"],
  "forbidden_sections": ["header", "about", "story", "founder-note", "problem", "agitation", "mechanism", "product-grid", "email-capture", "sms-capture", "quiz", "related-reads"],
  "nav": "minimal",
  "price_above_fold": "required",
  "cta": { "min": 2, "max": 3, "first_after_section": 0, "sticky": "optional", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 2, "max_modules": 4, "required_kinds": ["review-quote", "guarantee"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "detail"], "hero": "product-in-hand", "video": "optional", "min_images": 3 },
  "copy_framework": ["pas", "4ps"],
  "offer_compat": { "allowed": ["none", "free-shipping", "gwp", "bundle", "subscribe-save", "bnpl", "trial-sample", "loyalty", "cashback", "percent-off", "fixed-off", "bogo", "tiered-volume", "limited-edition"], "forbidden": ["first-order", "referral", "pre-order-price", "gift-card", "charity", "mystery", "clearance", "bundle-decoy", "price-lock", "flash-sale", "student-military"] },
  "urgency": "verified-only"
}
```

## Sources

- https://landerlab.io/blog/retargeting-landing-pages
- https://conversionbros.com/retargeting-landing-pages-how-to-convert-warm-audiences/
- https://www.growthlens.io/blog/cold-vs-warm-traffic-landing-page
- https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/
- https://foundrycro.com/blog/landing-pages-convert-differently-by-campaign-2026/
- https://crometrics.com/blog/urgency-that-actually-works/
- https://conversion.studio/blog/customer-awareness-stages
- https://robpalmer.com/blog/eugene-schwartz-breakthrough-advertising-lessons
- https://sarahlevinger.co/articles/most-creative-strategy-stops-one-layer-too-soon...here-are-7-ways-to-go-deeper
- https://www.convertflow.com/campaigns/hims-full-funnel-marketing-examples-templates
- https://www.jonesroadbeauty.com/products/miracle-balm
