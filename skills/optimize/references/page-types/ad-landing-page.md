# Ad landing page

One product, one action, one story that continues the ad. The visitor arrives cold or warm from a paid social or paid search click, has not bought from the merchant before, and must add the product to cart (or reach checkout) without leaving the page. Everything that is not the story, the proof or the action is removed.

## Identify it

Signals in the brief:
- An ad platform plus one product plus one angle ("Meta ads for the sleep gummies, angle is falling asleep faster").
- "Landing page", "campaign page", "post-click", "LP" without "article", "story", "reasons" or "vs".
- One to three SKUs, no date trigger, no named creator.
- Traffic is meta, tiktok or google-search; awareness problem-aware to product-aware.

Near neighbours:
- `advertorial`: choose it when the audience is unaware or problem-aware and the ad is a story or "I tried it" hook; cold readers need the premise before the price.
- `pdp-hybrid-landing`: choose it when the product has three or more variants or a gallery that decides the sale; hybrid keeps PDP buy mechanics.
- `listicle`: choose it when the ad or the headline is a number or "reasons".
- `retargeting-warm`: choose it when the visitor already saw the product; this type assumes nothing.
- `video-sales-page`: choose it when one long video carries the pitch.

Traffic depth lives in `references/traffic-source-meta.md`, `references/traffic-source-tiktok.md` and `references/traffic-source-google.md`; the section recipe and hero patterns by niche in `references/generate-landing-page.md`; the ad extraction workflow in `references/ad-to-page.md`. This file holds the contract.

## Variants

- **Bridge (pre-sell) page.** Same anatomy, shorter (8 sections), the CTA links to the PDP instead of adding to cart. Use when the merchant insists on the PDP as the buy surface. CTA copy pattern becomes `next-step`. Price still appears on the page before the first CTA (LAW: a hidden price is an invitation-to-purchase omission under UK DMCC and fails India Rule 6(5)(b); `references/offers/price-presentation.md`).
- **Problem page.** Problem-aware evergreen destination for problem-led ads and problem keywords ("why is my hair falling out"). Same anatomy with `problem` and `agitation` expanded, price after the first proof, soft product introduction. Research block 36 in internal research audit (2026-09-10).

## Anatomy

1. `hero` mandatory. H1 restates the ad promise; subhead names the mechanism or outcome in under 20 words; `review-summary` inline when 5 or more reviews exist (count only at 1 to 4); one CTA; ad-matched image. Nik Sharma: the hero carries problem-solving copy, social proof and a strong CTA together (OPERATOR, https://www.linkedin.com/posts/mrniksharma_despite-the-investment-be-it-100000-100-activity-7172971979602403328-_EzJ).
2. `trust-bar` recommended. Shipping, returns and guarantee facts from the offer ledger; a `press-marquee` only with linked articles.
3. `problem` conditional: awareness is problem-aware or solution-aware. Two to four sentences or three bullets naming the pain in the buyer's words.
4. `how-it-works` or `mechanism` mandatory (one of). Three steps or the named mechanism: the answer to "why does this work".
5. `benefits` mandatory. Three to six outcome-led items, each carrying a number, material, time or test.
6. `reviews` mandatory. Three to six verbatim quotes with dates and stored attribution, within the first two scrolls, never in the footer. Zero reviews: see Proof.
7. `video` conditional: a demo or UGC clip exists with rights. Click to play, poster, captions; inside `how-it-works` or beside the objection it answers, never in the hero.
8. `comparison` recommended. Us versus "the usual way" (a category, not a named competitor); outcomes with numbers; one honest concession row.
9. `buy-box` mandatory (`offer` when the CTA links out). Product, price, compare-at only with a ledger basis, variant picker, quantity, shipping and returns line, guarantee, CTA.
10. `faq` recommended. Four to six objections mined from reviews and ad comments; shipping, returns and "who it is not for" always present.
11. `closing-cta` mandatory. Restates the promise and the guarantee; the last-word proof (one attributed quote) sits directly above it.

Forbidden: `header` (logo only, not clickable), `product-grid`, `cross-sell`, `related-reads`, `email-capture` and `sms-capture` (no capture competes with the buy), `quiz`. The research matrix observes 7 to 9 sections, the index sets 8 to 11; the index governs.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.get` with the product id: media list with alt and order, each item mapped to a job (`identity`, `scale`, `in-use`, `detail`, `included-items`, `variation`) per `references/assets/image-jobs-by-page-type.md`; variant axes and whether colour variants carry their own images (identify which variant images need coordinated selection); price and compare-at (a ledger basis only); selling plans; inventory.
2. Read the supplied campaign message and creative. Record its hook, promise, audience, CTA verb, awareness, claims, product and variant; for video, select the real frame the hero must echo. Use `references/copy/message-match.md`.
3. `lexsis_catalog.reviews_status`, then `review_collections` (active) and `reviews` (`product_id`, `limit: 100`): count band B0 to B4, newest date, `has_media` count, per `references/proof/reviews-sourcing.md`. `reviews_search` with the mechanism claim and the top two objections for inline quotes (candidates stay pending until confirmed).
4. `lexsis_brand.context` and `brand_kit` (`theme_id`): tokens, voice, logo or text wordmark, shipping, returns and guarantee facts for the offer ledger (`references/offers/offer-types.md` for the offer id and its anatomy delta). Skip `navigation`; this type has no nav.
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`: `hero`, `lifestyle`, `product-shot`, `social-proof`, `logo`; then one semantic query per job still missing. Inventory by job before any slot is planned; view candidates with `lexsis_assets.view` (identity is never trusted from a filename).
6. `lexsis_workspace.credits` only if a backdrop or composite slot is still open after steps 1 to 5.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `hero` | continue the ad; H1 restates its promise, one proof element, one CTA, the product legible within one second. | yes; `in-use` or `context` in the ad's concept (`product-in-context`, `product-in-hand`, `ugc-screenshot` when the ad was UGC), portrait crop for mobile per `references/assets/slot-spec.md`. Search: the supplied clean campaign frame when rights permit, then catalog media in the ad's variant and angle, then library tag `hero` then `lifestyle`, then semantic "<product> in use, <ad scene>", then merchant upload. Generation: `hero_bg` (landscape plus portrait) only as a backdrop under a real cut-out (`product_composite`) and only when the plan names the hero as the bold moment. Gap: feasible purpose `hero_bg` behind a real cut-out, nothing else; a delegated brief uses the first Shopify identity image and records "hero pending merchant media". No-go: packshot-only hero for cold social, typographic hero unless the ad was, generated product or person, a carousel. Message match is judged by eye against the creative: same SKU, variant, angle and colourway, never by filename. `lexsis_asset_library.search` with `mode: "ocr"` flags library candidates that carry baked-in text before they are viewed. | `none` for a static `<picture>` with `fetchpriority="high"`. `HeroMedia` only when the hero is the plan's full-bleed bold moment with HTML text over it; its autoplay and effects default on and stay off unless the plan names that motion moment (N10). The CTA is an anchor to the buy box with the buy box's verb. | H1 at most 10 words with 60% token overlap with the ad headline (`references/copy/message-match.md`); subhead at most 20 words; `review-summary` (average plus n) at band B2 or higher, "n reviews" at B1, a guarantee fact at B0; two lines of shipping and returns microcopy under the CTA; no blacklist words (`references/anti-patterns/copy-anti-patterns.md`). | supplied campaign headline and frame; the catalog variant the ad shows; the review band. |
| `trust-bar` | shipping, returns and guarantee facts within one screen of the hero CTA. | photography no. Press logos only as monochrome outlet artwork from library tag `logo`, each linked to a fetched article in the proof ledger (`references/proof/press-and-media-mentions.md`). Gap: generation is not feasible for logos or badges (GN5); without facts or linked press the strip is skipped as the agreed alternative. | `none`. a static HTML row of text facts or linked logos, CSS motion only if it is the plan's motion moment. | three or four facts, at most six words each, from the offer ledger. | policy URLs from `lexsis_brand.context`; `press-logo-linked` ledger rows. |
| `problem` (conditional: problem-aware or solution-aware traffic) | name the pain in the buyer's words before the answer. | yes; one `context` image of the situation. Search: library tag `lifestyle`, then semantic "<situation without the product>", then merchant upload, then licensed stock for a scene with no product and nobody presented as a customer (model release on file). Gap: no generation purpose is feasible (a scene with people is NEVER, GN3); if the merchant chooses, the three bullets fold into `how-it-works` as its first step. No-go: a tinted band, a sad-face illustration, a generated person. | `none`. | `pas`; at most 80 words or three bullets; the pain phrased from `reviews_search` hits. | awareness from the supplied campaign brief. |
| `how-it-works` or `mechanism` | why it works, in three steps or one named mechanism. | yes; `sequence` (three real step photos), `diagram` (authored inline SVG, numbers in HTML) or `ingredient-or-material` (real flat lay). Search: catalog media, then library `product-shot` and `flat-lay`, then semantic "<mechanism> close-up", then merchant or supplier upload, then author the SVG. Gap: generation is not feasible for steps, ingredients or a raster diagram (GN11); the authored SVG carries the section meanwhile. No-go: stock lab scenes, three icon tiles. | `none` for stills and SVG. `VideoPlayer` when the `video` section sits here: click to play, real poster, captions carried with the media object. | three steps, at most 25 words each; test data footnoted with journal, year and n. | catalog coverage of `sequence`; `test-data` ledger rows. |
| `benefits` | three to six outcomes, each with a number, material, time or test. | yes; one `feature-image` per benefit with the product present: `detail`, `scale`, `in-use`, `included-items`. Search: catalog media by job, then library `product-shot` and `lifestyle`, then semantic per benefit, then merchant upload. Gap for a benefit: shared fallback; feasible purpose `product_composite` over a real cut-out for a `context` benefit only, never for `in-use` or `scale` (GP14); a benefit merges into a neighbour only on the merchant's choice. No-go: icon-tile-stack, emoji bullets, generated in-use. | `none`. | `fab`; outcome subhead at most 8 words; body at most 25 words; caption in HTML, never in the image. | the job map from `lexsis_catalog.get`; one slot per benefit. |
| `reviews` | human proof within the first two scrolls, before the buy box. | `ugc` tiles or review media where rights exist (`reviews` with `has_media: true`; library `social-proof` with a `P` ledger id). Nothing found: the section runs as text quotes; no generation is feasible (GN9); avatars are real or CSS initials. No-go: stock faces, screenshots without consent, a five-star-only wall. | by band per `references/proof/reviews-sourcing.md`. B1: static HTML cards plus an "n reviews" link. B2: `ReviewCarousel` bound to an active collection or the product id, three to six cards, autoplay off (its default is on, N10). B3 and B4: the carousel plus a "Read all n reviews" `ReviewList`, filters from 20 reviews, totals from the API. Never the first section. B0: `guarantee`, `certifications` or `founder-note` replace it (tiers 4 and 5) and the omission is recorded. | verbatim, dated, at most 60 words each, one mentioning a limitation. | `reviews_status` count band; an active `review_collections` id. |
| `video` (conditional: a demo or UGC clip with rights) | answer one objection by showing the product working. | a real video from catalog media, the library, or merchant-supplied campaign material; poster a real frame selected by viewing the clip, captions with the media or burned in (`references/assets/video-rules.md`). Nothing found: ask rule, naming the 45 to 90 second demo and the objection it would answer; generation is never feasible for video (VR13); the section exists only when the merchant supplies a clip. | `VideoPlayer` for one demo. `ShoppableVideoFeed` when three or more rights-cleared 9:16 clips exist, posters on every item, sound off until tapped | the objection as the heading; duration in HTML ("0:48"). | catalog media of type video; UGC ledger rows. |
| `comparison` | us against the usual way, outcomes with numbers, one concession row. | one `comparison-visual` of our attribute physically (`detail` or `scale` from catalog media, then library, then merchant upload); the alternative is an inline SVG silhouette labelled "other brands". Gap: generation is not feasible (GN8); the table stands with our identity image in the header cell meanwhile. No-go: competitor photos or logos, an all-green versus all-red tick grid. | `none`; a static HTML table (Tabs is deprecated; CSS-only tabs or `<details>` if a layout needs them). | four to six rows, cells at most 6 words, row labels as shopper questions. | `test-data` ledger rows for every cell. |
| `buy-box` (`offer` on the bridge variant) | the purchase: title, price, variant, quantity, shipping line, guarantee, CTA. | a gallery of three to five from catalog media (`identity`, `scale`, `variation`), per-variant images swapping on selection; position one only from Shopify media (GN12). Gap for `scale`: shared fallback; no generation is feasible in the gallery (GP11, GP14); the gallery ships with verified images only. | `BuyBox`, one per page; decide its form from the variant count and axes and whether the page has its own icon set (badges only when it does not); `VariantSwatches` beside it when colour variants carry images; gallery `ProductHero` at two to four images or `ProductGallery` at five or more, layout and thumbnails decided by the image count and the vertical; `DeliveryEstimate` for the dispatch cutoff (India pincode copy is static HTML); `StickyBar` bound to the buy section only when the page exceeds about three mobile screens, linked to the main purchase state. Bridge variant: no BuyBox; price and a link to the PDP. | "Add to cart, $39"; compare-at struck only with a ledger basis; shipping and returns line; guarantee; offer copy per `references/offers/offer-types.md`. | variant count and axes, per-variant image presence, page length, offer ledger rows. |
| `faq` | four to six objections, shipping, returns and "who it is not for" always present. | no. No-go: card-wrapped questions (N8). | `none`; native `<details>` and `<summary>`. | objection-phrased questions; answers at most 60 words. | `reviews_search` on objection topics; merchant-supplied campaign comments when available. |
| `closing-cta` | restate the promise and the guarantee; the last-word quote sits directly above. | optional; reuse one verified `in-use` or `identity` slot, no new job, no generation. No-go: an accent-colour band with a button as the only content (N2). | `none`; the CTA anchors to the buy box with the same verb, object and destination. | two lines plus the guarantee; the same CTA text as the hero. | the last-word `review-quote` ledger row. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | `identity`, `variation`, `detail`, sometimes `scale` | ad-matched `in-use`, `included-items`, `sequence` | reuse the ad frame for the hero; `scale` and `in-use`: ask the merchant to upload (identity-bound, no generation); a benefit merges only on the merchant's call |
| asset library | `hero` and `lifestyle` tags, `social-proof` UGC with rights, `logo` | in-use of this exact SKU | tag search, then semantic; view every candidate; UGC only with a `P` row |
| ad creatives | the hero frame (message match), persona, hook copy | everything below the hero | import the brand-owned frame with `lexsis_asset_import.import`; a creator frame needs scoped rights |
| generation | `hero_bg` (bold moment only), `product_composite` for a `context` benefit, `texture_fill` | product, people, results, logos, text | never; ask the merchant to upload instead |

With only an identity shot and one in-use image the page still ships: hero (ad frame or the in-use shot), `how-it-works` as three text steps beside the identity image, `benefits` as three items around one product image, `reviews` at any band above B0, `buy-box`, `faq`, `closing-cta`; `problem`, `comparison` and `video` are listed as missing assets with the upload offer, and leave the page only if the merchant chooses. Generated assets: at most four per page, usually zero or one `hero_bg`.

## Above the fold (390px)

Visible, in order:
1. Logo (not clickable) or nothing.
2. H1, at most 10 words, sharing the ad headline's noun phrase and promise.
3. Subhead under 20 words: mechanism or outcome plus who it is for.
4. One proof element: `review-summary` (average plus n at 5 or more reviews), "n reviews" text at 1 to 4, or a guarantee fact when no reviews exist.
5. Primary CTA, full width, 48px minimum, with two lines of risk-reversal microcopy under it (shipping, returns).
6. The top of the ad-matched hero image; the product is legible within one second.

Price: in the hero for product-aware traffic; after the first proof for problem-aware traffic (RESEARCH, Schwartz awareness mapping, https://www.getlandra.com/blog/5-stages-of-awareness). Desktop hero height 420 to 550px; Seton.de cut 850 to 420px for -11% bounce and +19% form fills (OPERATOR, single case, cited in `references/generate-landing-page.md`).

Must not appear: a second CTA with a different destination, a countdown, a stock count, an email popup, press logos above the H1, a carousel, autoplay video with sound.

## Proof

Density: 2 to 4 modules (index). The research minimum for a cold direct-response page is a star summary near the hero, one quote beside the primary claim, a policy fact beside the CTA and a last-word quote above the final CTA (internal teardown audit, 2026-09-10).

| Kind | Where | Minimum evidence |
|---|---|---|
| `review-summary` | hero, beside title or CTA | 5 or more reviews for an average with n beside it; 1 to 4 shows the count only (RESEARCH, Baymard n=670, https://baymard.com/blog/user-ratings-distribution-summary) |
| `review-quote` | `reviews`; one inline beside the strongest claim; one above `closing-cta` | verbatim, dated, attribution as stored; at least one mentions a limitation |
| `policy-fact` or `guarantee` | `trust-bar`, under every CTA | policy page URL, exact terms |
| `ugc-photo` or `ugc-video` | `reviews` or a UGC band of 4 to 8 tiles | rights record, handle, paid disclosure when paid |
| `press-logo-linked` | `trust-bar` | fetched article URL naming the brand; 3 to 6 logos, monochrome |
| `test-data` or `certification` | beside the mechanism claim | report or issuer on file |

Placement by scroll depth: one number in the top 20%, human proof at 40 to 80% before the buy box, the last word at the bottom. Interleave, do not stack (research section 13, Nik Sharma "brag bar").

Forbidden kinds: `social-proof-popup`, `live-viewer-count`, `press-logo-unlinked`. Never five identical five-star quotes; never round an average.

Zero reviews: run `references/proof/reviews-sourcing.md` tiers 4 and 5. `reviews` is replaced by `guarantee`, `certifications` or a `founder-note`, and the plan lists `reviews` under "Mandatory sections omitted" with the tier reached.

## Offer and CTA

- CTA count: exactly 3 (hero; after proof or at the buy box; closing). All three carry the same verb, object and destination. Research observes 3 to 5; the index fixes 3; a sticky bar is chrome and does not count.
- First CTA: hero (`first_after_section: 0`).
- Sticky: optional. The evidence is mixed. Vendor A/B tests report +5% to +26%, Intelligems a median +8.3% (OPERATOR, https://onlinestorenews.com/are-sticky-add-to-cart-bars-finally-killing-the-scroll-to-buy-problem/); Growth Rock measured +6% clicks and no order lift from a scroll-to-buy variant (OPERATOR, https://revenueflows.ai/blog/do-sticky-add-to-cart-buttons-increase-shopify-conversion-rate). When used: appears only after the hero CTA scrolls out, 56 to 64px, one button, price in the label, hidden on cart.
- Copy pattern: `add-to-cart` (verb plus object plus price where space allows: "Add to cart, $39"). Bridge variant: `next-step` ("See the serum"). Never "Shop now", "Buy now", "Learn more" (design-rules A12). The verb mirrors the ad's CTA (`references/copy/message-match.md`).
- Price reveal: hero for product-aware; after the first proof and before the first CTA for problem-aware. Never hidden until cart.
- Offer fit: `none`, `free-shipping`, `first-order`, `trial-sample` at any awareness. `percent-off`, `fixed-off`, `gwp`, `bundle`, `bnpl` only below the fold after the mechanism for cold traffic (offer-types OF7) and in the hero for product-aware traffic; each needs an offer-ledger row.
- Offer misfit: `tiered-volume` and `bundle-decoy` demand arithmetic a cold reader will not do; `flash-sale`, `clearance`, `mystery`, `loyalty` assume most-aware traffic; `referral`, `cashback`, `student-military`, `gift-card`, `pre-order-price`, `price-lock` belong to other types. The compatibility table in `references/offers/offer-types.md` governs.
- Urgency: `verified-only`, never in the hero (urgency-scarcity UR6). Prefer the dispatch cutoff line inside the buy box.

## Imagery

Required jobs: `identity`, `in-use`, `scale`. Strongly recommended: `ugc` (when rights exist), `detail`, `included-items`, `result-or-context` (only with substantiation), `founder-or-team`.
- Hero: `product-in-context`, the same creative concept as the ad (same model, colourway, angle); `product-in-hand` when the ad used it; `ugc-screenshot` when the ad was a lo-fi UGC ad (RESEARCH, scent, https://cxl.com/blog/give-your-advertising-roi-a-serious-boost-by-maintaining-scent/). A packshot-only hero fails for cold social traffic.
- Balance: lifestyle to studio about 60:40 for this type; the vertical table in `references/assets/image-jobs-by-page-type.md` adjusts it.
- Video: optional. Click to play with poster and captions; 45 to 90 seconds for a demo, 20 to 40 for a testimonial. A muted 6 to 15 second loop is the only autoplay allowed and never the hero LCP element.
- Minimum images: 6 (7 for beauty and home, 8 for apparel).
- Slots the plan must create: hero (ad-matched); mechanism visual or `diagram`; one image per benefit or a benefits grid image; UGC band of 4 to 8 tiles when rights exist; buy-box gallery of 3 to 5 (identity, scale, variation); founder photo when a founder note exists. Existing catalog media wins; generation only for a named missing job.

## Copy

- Framework: `aida` for the page spine, `pas` inside `problem`, `fab` inside `benefits`. Alternate education and CTA sections (push and pull, Nik Sharma, https://askthepods.com/episode/the-importance-and-value-of-landing-pages-nik-sharma-sharma-brands-bonus-episode).
- Headline by awareness: problem-aware leads with the problem named more precisely than the reader can ("Sweat through your shirt by 11am? Deodorant is not the fix"); solution-aware leads with result plus mechanism ("Odour-free for 48 hours without aluminium"); product-aware leads with product plus the strongest verified claim ("The mat 47,000 yogis stopped slipping on"). Never assume a higher awareness than the traffic supplies.
- Message match (mandatory): the H1 shares the ad headline's core noun phrase and promise (60% token overlap, or the identical claim rephrased no longer than the ad); same offer, same variant in the hero image, same CTA verb, same persona named. Unbounce audit: 98% of 300 paid ads failed message match (RESEARCH, https://unbounce.com/ppc/poor-message-match/). Rules and checks in `references/copy/message-match.md`.
- Reading level: grade 6 to 8. Unbounce: pages at 5th to 7th grade convert at 5.6% median against 1.5% for professional-level copy, correlational (https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/).
- Length ceilings: H1 10 words; subhead 20; `problem` 80 words; each benefit 25; each review card 60; each FAQ answer 60; total body 285 to 930 words (Unbounce ecommerce range, same source).
- Vocabulary: second person; numbers over adjectives; none of the blacklist words (elevate, unlock, seamless, game-changer, "say goodbye to"); sentence case; no exclamation marks outside verbatim reviews; no "Buy now" on TOF traffic. Framework detail in `references/copy/copy-frameworks.md`.

## Never

- Never render a clickable header, nav, footer link farm or search.
- Never place two CTAs with different destinations on the page.
- Never reinterpret the ad headline; the H1 repeats its promise.
- Never show the price in the hero to problem-aware traffic, and never hide it until cart for any traffic.
- Never put proof only in the footer.
- Never autoplay video with sound or make video the hero LCP.
- Never show a countdown, stock count or viewer count in the hero.
- Never use a packshot-only hero for cold social traffic.
- Never open an email or SMS capture before the buy box.
- Never exceed 3 CTAs or vary their copy between instances.
- Never show an average rating with fewer than 5 reviews.
- Never fabricate a testimonial, count, logo or badge (design-rules N11).

## Examples

- Hims message-matched landing pages feeding an assessment: the hero repeats the ad promise, proof sits under the hero, one path (https://www.convertflow.com/campaigns/hims-full-funnel-marketing-examples-templates).
- HexClad funnel landing pages: single product, single CTA, warranty as proof (https://www.convertflow.com/blog/hexclad-funnel-teardown).
- AG1 homepage used as a direct-response hero: "Goodbye bloat, hello energy", one sentence, CTA, guarantee line, then expert quotes with credential lines and a value stack (https://drinkag1.com/). Its trust row and value stack model `trust-bar` and `buy-box`.

## Checklist

```json
{
  "page_type": "ad-landing-page",
  "aliases": ["dedicated landing page", "campaign LP", "post-click page", "pre-sell bridge", "problem page"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["problem-aware", "solution-aware", "product-aware"],
  "traffic": ["meta", "tiktok", "google-search"],
  "sections": { "min": 8, "max": 11 },
  "mandatory_sections": ["hero", ["how-it-works", "mechanism"], "benefits", "reviews", ["buy-box", "offer"], "closing-cta"],
  "recommended_sections": ["trust-bar", "problem", "video", "comparison", "faq"],
  "forbidden_sections": ["header", "product-grid", "cross-sell", "related-reads", "email-capture", "sms-capture", "quiz"],
  "nav": "none",
  "price_above_fold": "optional",
  "cta": { "min": 3, "max": 3, "first_after_section": 0, "sticky": "optional", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 2, "max_modules": 4, "required_kinds": ["review-quote", "policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "in-use", "scale"], "hero": "product-in-context", "video": "optional", "min_images": 6 },
  "copy_framework": ["aida", "pas", "fab"],
  "offer_compat": { "allowed": ["none", "free-shipping", "first-order", "trial-sample", "percent-off", "fixed-off", "gwp", "bundle", "bnpl"], "forbidden": ["tiered-volume", "bundle-decoy", "bogo", "referral", "loyalty", "cashback", "mystery", "pre-order-price", "price-lock", "flash-sale", "clearance", "gift-card", "student-military"] },
  "urgency": "verified-only"
}
```

## Sources

- https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/
- https://unbounce.com/ppc/poor-message-match/
- https://www.getlandra.com/blog/5-stages-of-awareness
- https://www.linkedin.com/posts/mrniksharma_despite-the-investment-be-it-100000-100-activity-7172971979602403328-_EzJ
- https://askthepods.com/episode/the-importance-and-value-of-landing-pages-nik-sharma-sharma-brands-bonus-episode
- https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/
- https://docs.replo.app/use-cases/ecommerce/landing-pages
- https://revenueflows.ai/blog/do-sticky-add-to-cart-buttons-increase-shopify-conversion-rate
- https://onlinestorenews.com/are-sticky-add-to-cart-bars-finally-killing-the-scroll-to-buy-problem/
- https://baymard.com/blog/user-ratings-distribution-summary
- https://cxl.com/blog/give-your-advertising-roi-a-serious-boost-by-maintaining-scent/
- https://www.convertflow.com/campaigns/hims-full-funnel-marketing-examples-templates
- https://www.convertflow.com/blog/hexclad-funnel-teardown
- https://drinkag1.com/
