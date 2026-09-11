# Video sales page

One long video does the selling; the page frames it, catches the people who will not press play, and presents the offer after the pitch. The visitor arrives cold or warm from a video ad, a YouTube description or an email, is problem-aware or solution-aware, and must watch, then add to cart or claim the offer. Nothing competes with the player until the video has made its case.

## Identify it

Signals in the brief:
- "Video", "VSL", "watch this", "presentation", "founder explains", or the ad creative is long-form video.
- A strong presenter or founder, or a product that must be seen working (demo, transformation, mechanism).
- Nutra or info-product heritage; the merchant already has a 2 to 5 minute (DTC) or longer (nutra) video.

Near neighbours:
- `ugc-creator-collab`: choose it when many short creator clips carry the proof rather than one long video (index tie-break).
- `advertorial`: choose it when the story is text and the reader is unaware.
- `ad-landing-page`: choose it when a 30 to 90 second demo is a supporting element, not the pitch.
- `pdp` with an embedded closer video: warm traffic that needs the full buy box; a "closer" VSL is a gallery slot there, not this type.

Traffic tone: `references/traffic-source-meta.md` (video hero pattern) and `references/traffic-source-tiktok.md`. This file holds the contract.

## Variants

- **DTC short VSL (2 to 5 minutes).** Offer block visible below the player from the start; CTA count 2; text summary short. Tagada and Teleprompter place DTC ecommerce VSLs at 2 to 5 minutes (OPERATOR, https://www.tagada.io/blog/video-sales-letter).
- **Long-form VSL (20 to 35 minutes, nutra).** Delayed CTA revealed when the video reaches the pitch; text summary carries the whole argument for non-watchers. Observed scaling specimen: mechanism named at 15% of runtime, product at 63%, price at 74% (OPERATOR, https://dailyintelservice.com/blog/funnels-and-vsl/vsl-breakdown-a-30-minute-winner-minute-by-minute). Regulated categories keep claims structure-function and cite studies by journal and year.
- **Text-VSL hybrid.** The transcript rendered as a readable sales letter under the player; when it exceeds 2,000 words the page is a long-form sales letter (research block 16) and this type no longer applies.

## Anatomy

1. `hero` mandatory. A headline directly above the player that is "an ad for the video" and matches the video's opening promise; one-line subhead with length ("4 minutes") and what the viewer will learn. No price, no CTA for long-form; the DTC variant may show a muted CTA beside the player (OPERATOR, AgencyFlux anatomy, https://www.agencyflux.co/blog/high-converting-vsl-page-anatomy).
2. `video` mandatory. The one video: click to play, poster frame that represents the content honestly (a real frame with the presenter or product, not a black frame), captions, length indicator, transcript toggle; 60 to 70% of desktop width, 100% on mobile; never autoplay with sound (LAW: WCAG 1.4.2; browsers block it anyway). A sticky mini-player while scrolling is allowed on mobile; a sticky button bar is not.
3. `benefits` or `solution` mandatory (one of). The non-viewer path: the argument in five to eight bullets or 150 to 250 words, with the key points a watcher would have heard (problem, mechanism, result). 59% of users skip product-page videos (RESEARCH, Baymard, https://baymard.com/ecommerce-design-examples/video-and-360-views), so this section carries the sale for most visitors.
4. `offer` mandatory. After the video: product, price, guarantee, terms, the CTA. For long-form the block is revealed when playback reaches the pitch timestamp and stays visible afterwards; for the DTC variant it is visible from load but below the player.
5. `reviews` mandatory. The proof wall: three to six verbatim quotes, screenshots or UGC tiles with rights; raw screenshots read as more authentic than polished testimonials (OPERATOR, AgencyFlux). `ugc-grid` recommended beside it.
6. `faq` recommended. Top five objections, collapsed; mandatory questions: shipping cost and time, returns, who it is not for.
7. `guarantee` recommended. Restated before the close; guarantee gets more space than any scarcity.
8. `closing-cta` mandatory. Same action as the offer CTA; the last-word quote sits above it.

Forbidden: `header`, `announcement` (a bar competes with the player), `product-grid`, `cross-sell`, `countdown`, `stock-indicator`, `email-capture`, `sms-capture`, `quiz`. Index length 5 to 8; research counts 4 to 6 blocks around the video; the index governs and the mandatory six fit inside it.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.get` with the product id: media of type video (the VSL itself may live here), the `identity` image for `offer`, `ingredient-or-material` or `label-or-facts-panel` media for the summary, variant count (decides the offer block's form), price and compare-at (ledger basis; the value stack needs the component prices, `references/offers/offer-types.md`), selling plans (ignored: subscribe-save is a misfit), inventory (never shown).
2. `lexsis_campaigns.creatives`, `analyze` and `frames`: the video ad's opening line (the headline repeats it, `references/copy/message-match.md`), its length, the presenter or product frame that becomes the poster, and the offer it states.
3. `lexsis_catalog.reviews_status`, `review_collections` (active), `reviews` (`product_id`, `limit: 100`, `has_media`): band and dated quotes for the proof wall per `references/proof/reviews-sourcing.md`; `reviews_search` with the mechanism claim and the top objections. The video's own testimonials are not page proof unless each speaker has a ledger row.
4. `lexsis_brand.context` and `brand_kit` (`theme_id`): tokens, voice, guarantee terms, the presenter or founder record, the compliance wording the category requires. Skip `navigation`; nav is none.
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`: `product-shot`, `social-proof`, `flat-lay`, `hero`; `kind: "video"` for the VSL and for UGC clips with a `P` row; then semantic. View poster candidates with `lexsis_assets.view`.
6. `lexsis_workspace.credits` is not needed; nothing on this page is generated.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `hero` | the headline that is an ad for the video, a one-line subhead with the length, directly above the player. | no image of its own; the video poster below is the LCP image and is preloaded (`references/assets/slot-spec.md`). No-go: a hero photo above the player, press logos above the headline, a second video, an announcement bar. Any logo or mark is still opened with `lexsis_assets.view` before use. | `none`. | headline at most 12 words matching the video's opening line (60% token overlap with the ad, `references/copy/message-match.md`); subhead at most 20 words with the duration ("4 minutes") and what the viewer will learn; no price, no CTA for long-form; no "shocking" or "miracle" (`references/anti-patterns/copy-anti-patterns.md`). | `lexsis_campaigns.analyze` opening line and length. |
| `video` | the one video, click to play, poster frame, captions, length indicator, transcript toggle. | yes; the real VSL (16:9 or 1:1, never letterboxed 9:16) from catalog media or the library, or imported with `lexsis_asset_import.import`; the poster a real frame with the presenter or product chosen from `lexsis_campaigns.frames` or by viewing frames, never the auto-selected black frame; captions carried with the media or burned in; music rights recorded. Nothing found: shared fallback for the video and its poster; generation is never feasible for video or a still (VR13); the type is blocked until the merchant supplies the clip. No-go: a third-party embed that injects autoplay or cookies without consent; autoplay with sound. View the chosen poster frame and confirm it shows what the video opens with, so the click is not a bait. | `VideoPlayer`: click to play with the poster, the file fetched only on interaction, captions supplied with the media object On mobile the player wrapper may stick as a mini-player while scrolling, a layout choice, not a `StickyBar` (forbidden on this type). The transcript is a native `<details>` block under the player. | duration in HTML ("4:12"); play control drawn in HTML at 48px or more; transcript verbatim, under 2,000 words on the page. | the video's source, length and aspect from the import response; `references/assets/video-rules.md` section 3. |
| `benefits` or `solution` | the non-viewer path: the argument in five to eight bullets or 150 to 250 words. | yes; one or two stills beside the text: `identity` from catalog media, a `diagram` as authored inline SVG, or `ingredient-or-material` as a real flat lay. Search: catalog media, then library `product-shot` and `flat-lay`, then merchant or supplier upload. Gap: generation is not feasible for ingredients or a raster diagram (GN11); the authored SVG carries the section meanwhile. No-go: a wall of text without an image, icon tiles, stock lab scenes. | `none`. | `pas`; problem, mechanism, result; test data footnoted with journal, year, n and design; typical-results disclosure where the claim is an outcome. | the video's beat map from `lexsis_campaigns.analyze`; `test-data` ledger rows. |
| `offer` | product, price, guarantee, terms and the CTA, after the video and the summary. | yes; the `identity` image from catalog media; `included-items` flat lay when the offer is a bundle or value stack. Gap: no generation is feasible (GP11, GP13); the offer runs as HTML with the price meanwhile. | `BuyBox`, one per page, its form decided by the variant count, badges off; the value stack with struck free items is HTML from the offer ledger. DTC variant: visible from load, below the player. Long-form variant: revealed at the pitch timestamp only when the plan records how it is wired; otherwise the DTC placement is used and recorded as a deviation. No `StickyBar`. | `add-to-cart` ("Get the <product>, $59") or `claim-offer` with a real ledger offer (`references/offers/offer-types.md`); the price on the page before the first CTA to cart; at most 80 words plus terms; guarantee beside the button. | variant count; offer ledger rows; the variant (DTC or long-form). |
| `reviews` | the proof wall: three to six verbatim quotes, screenshots or UGC tiles. | yes; `ugc` and `review-with-media` tiles from `reviews` with `has_media: true` and library `social-proof`, each with a `P` row; raw screenshots only with the sender's written consent, channel and month labelled, phone numbers and surnames redacted. Nothing found: the wall runs as dated text quotes; generation is never feasible (GN9). No-go: fabricated chat UI, stock faces, polished quote cards with no source. | `none`; two or three dated quotes inline as HTML, never a carousel on this type (display table in `references/proof/reviews-sourcing.md`); at band B3 or higher an average plus n sits at `offer` from the API total. B0: `guarantee`, `certifications`, `test-data` and a named `founder-note` replace the wall and the omission is recorded. | verbatim, dated, attributed as stored, at most 60 words; one mentions a limitation. | `reviews_status` band; `has_media` count; consent records. |
| `ugc-grid` (recommended beside the wall) | creator or customer clips with rights, click to play. | yes; 9:16 `ugc` clips with `P` rows (rights, paid disclosure, captions, music cleared); posters as real frames (`references/proof/ugc-rights-and-display.md`). Search: library `social-proof` with `kind: "video"`, then merchant upload with the creator's consent. Fewer than three: ask rule naming the count and rights each clip needs; generation is never feasible; a smaller grid or none as the agreed alternative. | `ShoppableVideoFeed` when three or more clips exist, posters on every item, sound off until tapped, the product tagged; native `<video>` tiles for one or two clips. | handle and "Paid partnership" in frame where paid; duration in HTML. | UGC ledger rows; clip count. |
| `faq` | the top five objections; shipping cost and time, returns, who it is not for. | no. | `none`; native `<details>` and `<summary>`. | answers at most 60 words. | `reviews_search` on objection topics; questions the video leaves open. |
| `guarantee` | risk reversal restated before the close, with more space than any scarcity (there is none). | no; a certification mark only as issuer artwork. Any logo or mark is still opened with `lexsis_assets.view` before use. | `none`. | exact terms and policy URL. | the `guarantee` ledger row. |
| `closing-cta` | the same action as the offer CTA; the last-word quote above it. | optional reuse of the offer identity slot; no new job. | `none`; the CTA anchors to the offer block. | the same verb, object and destination as `offer`; at most two CTAs on the page. | the last-word `review-quote` row. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | `identity`, sometimes the demo video and `label-or-facts-panel` | the VSL itself, an honest poster frame, `included-items` for a value stack | the video is required: ask the merchant to import it (blocked until then); the poster is derived by viewing frames, never chosen by filename; contents: ask to upload, no generation |
| asset library | the VSL or UGC clips with `P` rows, `social-proof` screenshots with consent, `product-shot` | a mechanism flat lay | tag search with `kind: "video"`, then semantic; view before assigning |
| ad creatives | the opening line, the poster frame, the stated offer | anything below the player | import the brand-owned video and frame with `lexsis_asset_import.import`; a creator ad needs scoped rights |
| generation | nothing on this type in practice (`texture_fill` at most) | video, poster, product, people, results, logos, text | never; ask the merchant to upload instead |

With only the video and one identity shot the page still ships: headline, player with a real poster and transcript, the summary with an authored SVG, the offer around the identity image, guarantee and closing; the proof wall runs as dated text quotes at any band above B0, and `ugc-grid` is listed as a missing asset with the upload offer, leaving the page only on the merchant's decision. Generated assets: zero on this type; the four-per-page cap is never reached.

## Above the fold (390px)

Visible, in order:
1. Logo (not clickable) or nothing.
2. Headline above the player, at most 12 words, matching the video's opening line.
3. One-line subhead with the video length.
4. The player with its poster frame and a visible play control, filling the width; the poster is the LCP image and is preloaded.

Must not appear: price (`price_above_fold: forbidden`), a buy button beside or above the player on long-form, an announcement bar, a countdown, a stock count, autoplay with sound, a wall of text above the player, a second video, press logos above the headline. No CTA before value is "sales resistance" (OPERATOR, Daily Intel, https://dailyintelservice.com/blog/copywriting/vsl-landing-page).

## Proof

Density: 1 to 3 modules (index). Research asks for a proof wall below the fold and, inside long videos, 3 to 7 minutes of dedicated proof; the on-page wall is the minimum.

| Kind | Where | Minimum evidence |
|---|---|---|
| `review-quote` or `review-with-media` | `reviews` wall; one above `closing-cta` | verbatim, dated, attribution as stored; screenshots only with the sender's written consent, channel and month labelled, phone numbers and surnames redacted |
| `ugc-video` | `ugc-grid` | rights record, handle, paid disclosure when paid, captions, click to play |
| `test-data` | `benefits` summary, footnoted | journal, year, n, design copied exactly; typical-results disclosure for outcome claims (LAW, FTC endorsement guides) |
| `guarantee` or `policy-fact` | `offer`, `guarantee`, under every CTA | policy URL, exact terms |
| `expert-quote` or `founder-note` | `benefits` or `reviews` | named, credential verifiable, approval, connection disclosed |

Placement: no proof above the player except the headline's own promise; the wall sits directly after the offer at 60 to 80% of the page; the last word above the closing CTA. Forbidden kinds: `social-proof-popup`, `live-viewer-count`, `press-logo-unlinked`. `before-after` only under `references/proof/before-after-and-claims.md` and never beside a specific result number in a regulated category.

Zero reviews: `references/proof/reviews-sourcing.md` tiers 4 and 5. The wall becomes `guarantee`, `certifications`, `test-data` and a named `founder-note`; the plan records the omission. The video's own testimonials are not rendered as page proof unless each speaker has a ledger row.

## Offer and CTA

- CTA count: 1 to 2 (index). The offer CTA and the closing CTA carry the same verb, object and destination. Research observes one delayed CTA plus one or two below, which the index caps at two; the sticky mini-player is not a CTA.
- First CTA: in `offer`, after the video and the non-viewer summary (`first_after_section: 2`). Long-form: revealed at the pitch timestamp; DTC: visible from load, below the player.
- Sticky: forbidden for the button bar. The player may stick as a mini-player on mobile; a sticky buy bar before the pitch is exactly the premature CTA the format avoids (OPERATOR, research matrix "sticky player, not button").
- Copy pattern: `add-to-cart` ("Add to cart", "Get the [product], $59"); `claim-offer` when the ledger holds a real offer ("Claim the 3-pack offer"). Never "Watch now" as the buy CTA; never "Buy now" on cold traffic.
- Price reveal: after the video's pitch and after the guarantee, in `offer`; never above the player. The price is on the page before the first CTA to cart (LAW: `references/offers/price-presentation.md`).
- Offer fit: `none`, `bundle` (value stack with struck free items is the observed VSL close, AG1 pattern), `trial-sample`, `free-shipping`, `first-order`, `gwp`; `percent-off`, `fixed-off`, `bnpl` only inside `offer` after the pitch (offer-types OF7).
- Offer misfit: `bogo`, `tiered-volume`, `bundle-decoy`, `subscribe-save` (a ladder under a VSL splits attention), `referral`, `loyalty`, `cashback`, `mystery`, `limited-edition`, and every timing offer. `references/offers/offer-types.md` governs.
- Urgency: `none`. No timer, count or "this video will be taken down" line (OPERATOR: now counterproductive, Rob Palmer, https://robpalmer.com/blog/supplement-vsl-copywriting; urgency-scarcity UR6). Objections are handled before any close; the guarantee gets more airtime than scarcity.

## Imagery

Required jobs: `identity`, `in-use`. Strongly recommended: `ugc` for the wall, `result-or-context` (substantiated only), `ingredient-or-material` or `diagram` for the mechanism, `founder-or-team` for the presenter.
- Hero: `video-poster`, a real frame showing the presenter or the product in use with a face or hands, sized for LCP (under 200 KB mobile), preloaded, never a generated still.
- Balance: the video is the imagery; below it, product stills and proof screenshots about 40:60.
- Video: required. Controls: captions (burned in or track), click to play with poster, pause control, `preload="none"` so only the poster loads before interaction; 16:9 or 1:1 for a presenter or demo, never letterboxed into 9:16; never the LCP element itself (RESEARCH and house rule, internal research audit (2026-09-10) section 4.3).
- Minimum images: 4 (poster, product identity, two proof or mechanism stills); research range 4 to 8.
- Slots the plan must create: poster frame; product identity image in `offer`; mechanism diagram or ingredient image in the summary; UGC or screenshot tiles for the wall when rights exist; presenter photo when a founder note exists.

## Copy

- Framework: `hook-story-offer` for the page and the script; `pas` for the non-viewer summary; `aida` for short DTC versions. Long-form script beats: hook, problem, promise, mechanism, proof, offer, urgency-free close; write at about 150 words per minute (OPERATOR, https://dailyintelservice.com/vsl-copywriting-guide-scaling-offers-2026).
- Headline by awareness: problem-aware leads with the problem and a promise to explain ("Why your knees still ache after stretching, in 4 minutes"); solution-aware leads with result plus mechanism ("How a 90-second cold-brew method removes the bitterness"). The headline never over-promises what the mechanism can pay off.
- Message match: the headline repeats the video ad's opening line or hook (60% token overlap); the poster frame is the ad's presenter or product; the offer matches the ad's offer (`references/copy/message-match.md`).
- Reading level: grade 6 to 8 for the summary; the video's key claim lands in the first 5 seconds (RESEARCH, Wistia, https://wistia.com/blog/does-length-matter-it-does-for-video-2k12-edition).
- Length ceilings: headline 12 words; subhead 20; non-viewer summary 150 to 250 words or eight bullets; offer block 80 words plus terms; each quote 60 words; FAQ answer 60. DTC video 2 to 5 minutes; long-form 20 to 35 minutes with the product named after the mechanism.
- Vocabulary: second person; specific numbers; no blacklist words; no "shocking", "miracle", "doctors hate" (Meta and Google review the destination page); supplements keep structure-function wording beside the claim; sentence case; no exclamation marks.

## Never

- Never autoplay with sound or start the video without a user action.
- Never show price, a buy button or an offer bar above or beside the player on long-form.
- Never use a poster frame that promises something the video does not show.
- Never omit the non-viewer text summary.
- Never render a sticky buy bar before the pitch.
- Never show a countdown, stock count, viewer count or "this video will be taken down".
- Never embed a second video or a carousel above the player.
- Never make the video file the LCP element.
- Never render a header, navigation or footer links.
- Never exceed 2 CTAs or point them at different destinations.
- Never place a before-and-after beside a specific result claim in a regulated category.
- Never let the transcript exceed 2,000 words on the page; that is a sales letter, not this type.

## Examples

- Nutra VSL beat map: hook 0 to 3 minutes, problem 3 to 8, promise 8 to 12, mechanism 12 to 18, proof 18 to 25, offer 25 to 30; product named at 63% of runtime, price at 74% (https://dailyintelservice.com/blog/funnels-and-vsl/vsl-breakdown-a-30-minute-winner-minute-by-minute).
- AgencyFlux VSL page anatomy: headline as an ad for the video, dominant player with honest poster, delayed CTA at the pitch, proof wall of raw screenshots, FAQ, guarantee (https://www.agencyflux.co/blog/high-converting-vsl-page-anatomy).
- AG1 homepage close as the model `offer` block after a pitch: value stack with struck free items, per-month price, 90-day guarantee, cancel-anytime line (https://drinkag1.com/).

## Checklist

```json
{
  "page_type": "video-sales-page",
  "aliases": ["VSL", "video sales letter", "video-first landing page", "watch-this page", "text-VSL hybrid"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["problem-aware", "solution-aware"],
  "traffic": ["meta", "youtube", "email"],
  "sections": { "min": 5, "max": 8 },
  "mandatory_sections": ["hero", "video", ["benefits", "solution"], "offer", "reviews", "closing-cta"],
  "recommended_sections": ["faq", "guarantee", "ugc-grid"],
  "forbidden_sections": ["header", "announcement", "product-grid", "cross-sell", "countdown", "stock-indicator", "email-capture", "sms-capture", "quiz"],
  "nav": "none",
  "price_above_fold": "forbidden",
  "cta": { "min": 1, "max": 2, "first_after_section": 2, "sticky": "forbidden", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 1, "max_modules": 3, "required_kinds": ["review-quote"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "in-use"], "hero": "video-poster", "video": "required", "min_images": 4 },
  "copy_framework": ["hook-story-offer", "pas", "aida"],
  "offer_compat": { "allowed": ["none", "bundle", "trial-sample", "free-shipping", "first-order", "gwp", "percent-off", "fixed-off", "bnpl"], "forbidden": ["bogo", "tiered-volume", "bundle-decoy", "subscribe-save", "referral", "loyalty", "cashback", "mystery", "pre-order-price", "price-lock", "flash-sale", "clearance", "limited-edition", "gift-card", "student-military", "charity"] },
  "urgency": "none"
}
```

## Sources

- https://www.agencyflux.co/blog/high-converting-vsl-page-anatomy
- https://dailyintelservice.com/blog/copywriting/vsl-landing-page
- https://dailyintelservice.com/vsl-copywriting-guide-scaling-offers-2026
- https://dailyintelservice.com/blog/funnels-and-vsl/vsl-breakdown-a-30-minute-winner-minute-by-minute
- https://robpalmer.com/blog/supplement-vsl-copywriting
- https://www.tagada.io/blog/video-sales-letter
- https://neutrinomarketing.com/blog/vsl-funnel-optimization
- https://baymard.com/ecommerce-design-examples/video-and-360-views
- https://baymard.com/blog/embedding-product-page-videos
- https://unbounce.com/landing-pages/video-on-landing-pages-means-more-conversions-right-wrong-heres-why/
- https://wistia.com/blog/does-length-matter-it-does-for-video-2k12-edition
- https://www.w3.org/WAI/WCAG22/Techniques/failures/F93.html
- https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
- https://drinkag1.com/
