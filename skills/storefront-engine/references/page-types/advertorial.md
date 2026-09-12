# Advertorial

An editorial article that sells by story. The visitor arrives cold from a story or problem hook on Meta, TikTok or a native network, is unaware or problem-aware, and reads. The product appears only after the premise, the mechanism and the proof have earned it; the price arrives last; the reader leaves through one soft next step.

## Identify it

Signals in the brief:
- "Story", "article", "editorial", "we tried it", "here is what happened", "special report", native placement (Taboola, Outbrain, MSN).
- Audience "does not know they need it" or "does not know solutions exist"; product needs a mechanism explained; price above about $70; regulated category (supplements, skincare actives).
- Ad creative is a first-person hook or a contrarian claim, not a product shot.

Near neighbours:
- `ad-landing-page`: choose it when the audience already knows the category and the ad is direct response; an advertorial to product-aware traffic wastes the click.
- `listicle`: choose it when the ad or headline is a number or "reasons"; frame must match the click.
- `video-sales-page`: choose it when one long video carries the story.
- `brand-story-founder`: choose it for organic "who are you" traffic; an advertorial sells a product, a brand story sells belief.

Landra's rule: advertorial for cold and problem-aware, listicle for solution-aware comparison shoppers, product page for decided buyers (OPERATOR, https://www.getlandra.com/blog/how-to-write-an-advertorial). Traffic tone lives in `references/traffic-source-meta.md` and `references/traffic-source-tiktok.md`. This file holds the contract.

## Variants

- **First-person story.** A named narrator's account ("I tried it for 30 days"). The narrator is real, consented and named; a fictional persona is a disguised-ad violation (LAW, FTC native advertising guidance; ASA MPJ Invest ruling on a fake blogger persona).
- **Mechanism explainer.** Science-journalism voice: "Researchers discover..."; every claim carries a citation; product turn after the mechanism. Supplements: mechanism-led, not transformation-led, typical results labelled (https://www.getlandra.com/blog/listicle-vs-advertorial-supplement-brands).
- **Hybrid listicle-advertorial.** Story lead, then three to five numbered beats inside the article (Stars + Honey). Still one destination; still no price above the fold. When the numbered frame dominates, use `listicle` instead.

## Anatomy

Fixed order. Moving the product earlier "almost always hurts" (OPERATOR, Landra, https://www.getlandra.com/blog/how-to-build-an-advertorial-landing-page).

1. `dateline` mandatory. Disclosure label "Advertisement" or "Sponsored" visible at the top (LAW: FTC native advertising guidance; UK ASA; India ASCI disguised-ad rule), publication-style kicker, byline with a real named author, date. Present in 3 of 4 fetched advertorials as a kicker; the compliance label was missing on 2 of 3, which is the failure to avoid.
2. `hero` mandatory. Article headline: story, identity, startling fact or the problem in the reader's words; never the product or the price. Editorial image that echoes the ad creative, not a designed hero. No CTA.
3. `hook` mandatory. Lead paragraph; the reader thinks "this is about me" within two sentences; first-person or contrarian ("viral diet advice is harmful for women over 40").
4. `problem` mandatory. Problem recognition in the reader's words; a symptom checklist as self-qualification (Skinesa pattern).
5. `agitation` recommended. Failed alternatives and the hidden cost ("what you have tried and why it did not work").
6. `mechanism` or `discovery` mandatory (one of). Root-cause reframe: why the problem persists; the moment the narrator found the mechanism. Adlibrary calls the criteria step that follows the most-skipped section (https://adlibrary.com/posts/advertorial-landing-pages).
7. `solution` recommended. What a real fix would need to do, stated before the product is named.
8. `offer-bridge` mandatory. The product turn: the product named as the logical consequence of the criteria, past the page midpoint and after 800 to 1,500 words. The first CTA lives here and is soft.
9. `reviews` mandatory. Three specific, dated testimonials placed where scepticism appears; proof lives inside the narrative, not pooled.
10. `benefits` recommended; `comparison` conditional: the category has a dominant incumbent the reader uses.
11. `qualifier` recommended. Who it is for and who it is not for.
12. `buy-box` conditional: the merchant wants on-page purchase. Only after `offer-bridge`; otherwise the CTA links to the PDP or a quiz.
13. `faq` recommended; `guarantee` recommended.
14. `closing-cta` mandatory. The same action repeated; price stated on the page before it.
15. `disclaimer` recommended. Compliance footer: advertisement statement, typical-results disclosure, structure-function wording for supplements (present on Miracle, absent on Skinesa and Stars + Honey).

Forbidden: `header`, `announcement` (an offer bar puts price above the fold), `product-grid`, `cross-sell`, `countdown`, `stock-indicator`, `email-capture`, `sms-capture`. Index length 8 to 12; research allows 8 to 13; the index governs.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.get` with the product id: the `identity` image for `offer-bridge`, any `in-use` or `label-or-facts-panel` media, variant count (a single variant keeps the turn simple), price and compare-at (ledger basis; price appears last but on the page), selling plans (ignored: subscribe-save is a misfit per `references/offers/offer-types.md`), inventory (never shown).
2. `lexsis_campaigns.creatives` and `analyze`: the ad's hook, its first-person or contrarian voice, the persona, and the scene the hero must echo (`references/copy/message-match.md`); `frames` when the ad was video. `match_persona` for the narrator's register.
3. `lexsis_catalog.reviews_status`, `review_collections` (active), `reviews` (`product_id`, `limit: 100`, `has_media`): band and dated, specific quotes per `references/proof/reviews-sourcing.md`. `reviews_search` with the mechanism claim, the failed-alternatives beat and the "who it is not for" beat; candidates stay pending until confirmed.
4. `lexsis_brand.context` and `brand_kit` (`theme_id`): voice, the real named author for the byline, the founder record if a narrator photo is wanted, guarantee terms, the compliance wording the category requires. Skip `navigation`; nav is none.
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`: `lifestyle`, `hero`, `flat-lay`, `social-proof`, `product-shot`; then semantic per beat ("<situation>", "<ingredient> flat lay"). View candidates with `lexsis_assets.view`.
6. `lexsis_workspace.credits` only if a `context` composite is wanted after the turn; the editorial hero is never generated.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `dateline` | the "Advertisement" or "Sponsored" label, a publication-style kicker, a real named byline and a date. | no; an author portrait only as a real `founder-or-team` photo with consent, at byline size. Nothing found: the byline runs as text; generation is never feasible for people (GN3). No-go: a fabricated publication mark, a stock face. | `none`. | label first, at most one line; byline "By <real name>, <date>". | the author record from `lexsis_brand.context`; FTC, ASA and ASCI disclosure wording. |
| `hero` | the article headline over an editorial image that echoes the ad; no product, no price, no CTA. | yes; `editorial-lifestyle` of a person in the situation or the situation itself (`context`); `ugc-screenshot` when the ad was UGC; portrait crop for mobile (`references/assets/slot-spec.md`). Search: the ad frame via `lexsis_campaigns.frames` (import the brand-owned original with `lexsis_asset_import.import`; a creator frame needs a rights row; use the clean original, since the exported ad usually carries baked-in text), then library `lifestyle` then `hero`, then semantic "<situation>", then merchant upload, then licensed stock for a scene with no product and nobody presented as a customer (model release on file). Gap: no generation purpose is feasible (a scene with people is NEVER, and a backdrop is not editorial); a delegated brief runs the headline with the first two sentences of the lead and lists the hero as missing. No-go: packshot, price or offer visuals, a generated person. The scene echo is judged by eye against the creative, never by filename. `lexsis_asset_library.search` with `mode: "ocr"` flags library candidates that carry baked-in text before they are viewed. | `none`; a static `<picture>` or no image. | headline at most 12 words in the reader's words, never the product; the ad's promise continued with 60% token overlap (`references/copy/message-match.md`); no blacklist words (`references/anti-patterns/copy-anti-patterns.md`). | `lexsis_campaigns.analyze` hook and scene; awareness stage. |
| `hook` | the lead paragraph; the reader thinks "this is about me" within two sentences. | no; a text beat by design, carried by the hero above it. | `none`. | `story-lead`; first person or contrarian; paragraphs at most three lines on mobile. | the narrator's voice from the ad. |
| `problem` | problem recognition in the reader's words; a symptom checklist as self-qualification. | yes; one `context` image of the situation without the product. Search: library `lifestyle`, then semantic, then merchant upload, then licensed stock (scene only, model release). Gap: no generation purpose is feasible; the checklist runs as HTML text meanwhile. No-go: illustration of pain, red tint, competitor packaging. | `none`. | `pas`; checklist of three to six symptoms, each one line. | `reviews_search` phrasing of the pain. |
| `agitation` | the failed alternatives and their hidden cost. | no new image; the beat stays short; competitor products are never shown (GN8). | `none`. | at most 120 words; a transition hook into the mechanism. | `reviews_search` for "tried everything" quotes (pending until confirmed). |
| `mechanism` or `discovery` | the root-cause reframe, or the moment the narrator found it. | yes; `diagram` as authored inline SVG with numbers in HTML, `ingredient-or-material` as a real flat lay, `founder-or-team` for a real narrator, or a click-to-play narrator clip with a real poster and captions (`references/assets/video-rules.md`). Search: catalog media, then library `flat-lay` and `product-shot`, then merchant or supplier upload, then licensed stock for a raw ingredient not presented as the merchant's own sourcing. Gap: generation is not feasible for ingredients, people or a raster diagram (GN3, GN11); the authored SVG carries the beat meanwhile. No-go: lab coats, stethoscopes, generated doctors. | `none` for stills and SVG; `VideoPlayer` for the narrator clip, click to play | every claim cites journal, year, n and design; the product is still unnamed. | `test-data` and `expert-quote` ledger rows. |
| `solution` | what a real fix would need to do, before the product is named. | no; a short criteria list carried by a subhead. | `none`. | three to five criteria, one line each. | the mechanism beat above. |
| `offer-bridge` | the product turn past the midpoint; the first, soft CTA. | yes; the first `identity` image from catalog media, plus one `in-use` image. Search: catalog media, then library `product-shot` and `lifestyle`, then merchant upload. Gap: feasible purpose `product_composite` for a `context` image over a real cut-out only, never the product itself (GN1); the turn ships as text with the CTA meanwhile and the slot stays `planned`. | `none` for the identity image; the CTA is an HTML link to the single destination the plan names: the on-page `buy-box`, the PDP or a quiz. | `next-step` ("See why people switch", "Check availability"); the price is on the page before the first CTA to cart (`references/offers/price-presentation.md`). | the merchant's choice of buy surface; offer ledger rows. |
| `reviews` | three specific, dated testimonials placed where scepticism appears, the first directly after the turn. | `ugc` or `review-with-media` screenshots per quote where rights exist (`has_media: true`; library `social-proof` with a `P` row); original aspect, no beautifying edits. Nothing found: the quotes run as text; generation is never feasible (GN9). | `none`; two or three dated quotes inline as HTML, never a carousel on this type (display table in `references/proof/reviews-sourcing.md`). At band B3 or higher an average plus n sits at `offer-bridge` from the API total. B0: `test-data`, `guarantee` and a named `founder-note` replace the section and the omission is recorded. | verbatim, dated, at most 60 words, falsifiable ("stopped waking at 3am by week two"); never "amazing product". | `reviews_status` band; `reviews_search` candidates confirmed by the merchant or an active collection. |
| `benefits` | three outcomes now that the product is named. | yes; one `in-use` or `detail` image with the product present, per benefit or shared across three. Search: catalog media, then library, then merchant upload. Gap: feasible purpose `product_composite` for a `context` image only; merge only on the merchant's choice. | `none`. | `fab`; at most 25 words each. | the job map. |
| `comparison` (conditional: a dominant incumbent the reader uses) | us versus the incumbent category, outcomes with numbers, one concession row. | one `comparison-visual` of our attribute physically; the incumbent is an inline SVG silhouette. Gap: generation is not feasible (GN8); the table stands with the identity image meanwhile. | `none`; a static HTML table (Tabs is deprecated). | four to six rows, cells at most 6 words. | `test-data` rows per cell. |
| `qualifier` | who it is for and who it is not for. | no; two short lists. | `none`. | three items each, one line each. | `reviews_search` on fit and misfit. |
| `buy-box` (conditional: the merchant wants on-page purchase, after `offer-bridge`) | one place to buy without leaving the article. | one or two identity images as static `<img>`; no gallery island on this type. Gap: no generation is feasible for the product. | `BuyBox`, one per page; decide its form from the variant count, badges off (the article has no icon set); `VariantSwatches` only when colour variants carry images; no `ProductGallery` or `ProductHero`. `StickyBar` only after the turn, bound to the offer and appearing once the reader passes `offer-bridge`, soft label. | price with compare-at only on a ledger basis; guarantee beside the button; the same soft verb as the bridge (`references/offers/offer-types.md`). | variant count; offer ledger rows; the sticky rule. |
| `faq` | the objections the story did not settle. | no. | `none`; native `<details>` and `<summary>`. | answers at most 60 words. | `reviews_search` on objection topics. |
| `guarantee` | risk reversal beside every CTA after the turn. | no; a certification mark only as issuer artwork with a ledger row. Any logo or mark is still opened with `lexsis_assets.view` before use. | `none`. | exact terms, policy URL. | the `guarantee` ledger row. |
| `closing-cta` | the same action repeated; price stated on the page before it; last-word quote above. | optional reuse of the `offer-bridge` identity slot; no new job. | `none`; a link to the single destination. | `next-step`; never "Buy now" or "Shop now". | the last-word `review-quote` row. |
| `disclaimer` | advertisement statement, typical-results disclosure, structure-function wording for supplements. | no. | `none`. | the mandated wording, verbatim from the category rule. | category and market from the brief. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | `identity` for the turn, sometimes `label-or-facts-panel` | editorial `in-use`, situation `context`, a real narrator portrait | ask the merchant to upload (people and in-use are never generated); the text beats stand meanwhile and the hero stays `planned` |
| asset library | `lifestyle` and `hero` scenes, `social-proof` screenshots with rights, `flat-lay` | the exact situation the ad shows | tag search, then semantic; view before assigning; a screenshot needs a `P` row |
| ad creatives | the hero scene and the narrator's voice | anything after the turn | import the brand-owned frame with `lexsis_asset_import.import`; a creator frame needs scoped rights |
| generation | `product_composite` for one `context` image after the turn, `texture_fill` | product, people, results, ingredients, logos, text | never; ask the merchant to upload instead |

With only an identity shot the page still ships: dateline, a text-led hero (headline plus lead), hook, problem checklist, mechanism with an authored SVG, offer-bridge around the identity image, quotes at any band above B0, guarantee, closing and disclaimer; `agitation`, `solution` and `qualifier` stay as short text beats, and the missing hero, situation and in-use images are listed with the upload offer, with `comparison` and `buy-box` leaving the page only on the merchant's decision. Generated assets: at most four per page, usually zero.

## Above the fold (390px)

Visible, in order:
1. Disclosure label ("Advertisement") and the publication-style kicker or byline.
2. Article headline, at most 12 words, in the reader's words; no product name, no number that is a price.
3. Editorial image or the first two sentences of the lead; the reader recognises themself before the fold ends.

Must not appear: any CTA, price, discount, buy button, star rating, brand logo larger than a byline mark, countdown, stock count, offer bar, product packshot. Awareness levels 1 and 2 never show price, discount or a buy button above the fold (RESEARCH, Schwartz mapping, https://www.getlandra.com/blog/5-stages-of-awareness). No CTA above the fold in 3 of 4 fetched advertorials.

## Proof

Density: 2 to 4 modules (index). Research minimum: disclosure before any proof; two to three dated quotes; every number with a source (internal teardown audit, 2026-09-10).

| Kind | Where | Minimum evidence |
|---|---|---|
| `review-quote` | `reviews`, one inline right after `offer-bridge`, one above `closing-cta` | verbatim, dated, attribution as stored; specific and falsifiable ("stopped waking at 3am by week two"), never "amazing product" |
| `test-data` | inside `mechanism` | journal, year, n and design copied exactly (Skinesa cites JAMA Dermatology; AG1 discloses n=35 single-arm) |
| `expert-quote` or `founder-note` | `discovery` or `solution` | named, credential verifiable, approval, material connection disclosed; never "a team of doctors" |
| `customer-count` | `offer-bridge` or `reviews` | export or analytics with date, rounded down, "over N" |
| `ugc-photo` or `review-with-media` | `reviews` | rights record; original aspect; no beautifying edits |
| `guarantee` | beside every CTA after the turn | policy URL, exact terms |

Placement by scroll depth: nothing review-shaped before the mechanism; first human proof directly after the product turn (60 to 80% in the teardown heat-map); the last word above the closing CTA. Forbidden kinds: `social-proof-popup`, `live-viewer-count`, `press-logo-unlinked`. `before-after` never sits beside a specific result number in a regulated category (LAW, FTC health claims; ASA before-and-after guidance).

Zero reviews: `references/proof/reviews-sourcing.md` tiers 4 and 5. The `reviews` section becomes `test-data` plus `guarantee` plus a named `founder-note`; the plan records the omission. An advertorial with zero customer proof (Miracle Brand teardown) is the pattern to avoid.

## Offer and CTA

- CTA count: 1 to 3, one action, repeated only after the product turn. The index and research agree (research: one action repeated two to four times; the index caps at three).
- First CTA: at `offer-bridge`, never before section 5 (`first_after_section: 4`) and normally past the midpoint.
- Sticky: optional, and only after the product turn. A soft "See the offer" bar may appear once the reader passes `offer-bridge`; no sticky buy bar before it.
- Copy pattern: `next-step`. Transitional copy: "See why people switch", "Check availability", "See today's offer" (https://landgoose.com/blog/advertorial-landing-page-template). Never "Buy now", never "Shop now".
- Price reveal: last, after proof and guarantee, and always on the page or one click away before the first CTA to cart (LAW: hiding the price entirely is a UK DMCC invitation-to-purchase omission and fails India Rule 6(5)(b); `references/offers/price-presentation.md`).
- Offer fit: `none` and `trial-sample` fit the frame. `first-order`, `free-shipping`, `gwp`, `bundle`, `percent-off`, `fixed-off` only inside `offer-bridge` or later, after the mechanism (offer-types OF7); a discount before the mechanism reads as an ad and is skipped.
- Offer misfit: `bogo`, `tiered-volume`, `bundle-decoy`, `subscribe-save` need arithmetic that breaks the editorial frame; `flash-sale`, `clearance`, `limited-edition`, `mystery`, `loyalty`, `referral`, `cashback`, `bnpl`, `gift-card`, `student-military`, `pre-order-price`, `price-lock` assume awareness this reader lacks. `references/offers/offer-types.md` governs.
- Urgency: `none`. No timers, counts or "last chance" anywhere (urgency-scarcity UR6). The Miracle Brand offer bar with a 15-minute timer and "16 orders remaining" is the anti-pattern.

## Imagery

Required jobs: `identity` (after the turn only), `in-use`, `result-or-context`. Strongly recommended: `ingredient-or-material`, `diagram` for the mechanism, `founder-or-team` for the narrator, `ugc` for review screenshots.
- Hero: `editorial-lifestyle`, documentary feel, echoing the ad creative; a person in the situation, not a product. No studio packshot in the first half of the page.
- Balance: editorial and in-use about 70%, product and diagram 30%; UGC as review screenshots.
- Video: optional; a narrator or mechanism clip, click to play with poster and captions, placed at `discovery` or `reviews`, never in the hero.
- Minimum images: 4 (research range 4 to 8).
- Slots the plan must create: editorial hero; problem or situation image; mechanism `diagram` or ingredient flat lay; product identity image at `offer-bridge`; one review screenshot or UGC tile per quote where rights exist. Reproducing the full ingredient label as proof (Noble Origins) is a valid identity slot.

## Copy

- Framework: `story-lead` into `pas` for unaware readers; `pas` for problem-aware; `hook-story-offer` for the hybrid. Five-step arc: problem, why it persists, proof, objections, one CTA.
- Headline by awareness: unaware leads with a story, identity or startling fact ("The 3pm habit that quietly ages your skin"); problem-aware names the pain more precisely than the reader can ("Still scratching at 2am? Here is what your moisturiser is missing"). Never the product, never a discount, never "Introducing".
- Message match: the H1 continues the ad's promise in the ad's words (60% token overlap or the identical claim rephrased no longer); the hero image echoes the ad creative; the narrator matches the ad's voice (`references/copy/message-match.md`).
- Reading level: grade 6 to 8; subheads every 300 to 500 words carry the argument because 81% look at paragraph 1 and 32% at paragraph 4 (RESEARCH, NN/g, https://www.nngroup.com/articles/website-reading/). The product turn is carried by a subhead, not buried in prose.
- Length ceilings: 800 to 1,500 words before the product turn; 400 to 800 after it; paragraphs at most three lines on mobile; each quote at most 60 words; each FAQ answer at most 60 words. Transition hooks between beats ("Which brings us to the real reason people stay") keep the slide moving.
- Vocabulary: second person or first person, never brand-corporate; falsifiable specifics; regulated categories keep mandated wording beside the claim; no blacklist words; no exclamation marks; no fabricated publication names, reporters or experts.

## Never

- Never name the product, show its packshot or its price before `offer-bridge`.
- Never place a CTA, buy button or offer bar above the fold.
- Never omit the "Advertisement" or "Sponsored" label or bury it in the footer.
- Never invent a narrator, reporter, publication, doctor or comment thread.
- Never show a countdown, stock count, viewer count or "last chance" line.
- Never render a header, navigation, footer links or social icons.
- Never send the reader to more than one destination.
- Never place a before-and-after image beside a specific result claim in a regulated category.
- Never write "amazing product" proof; every quote is specific, dated and attributed.
- Never use "Buy now" or "Shop now" as the CTA.
- Never hide the price entirely ("see price in cart") for UK, EU or India traffic.
- Never exceed 3 CTAs or place the first before section 5.

## Examples

- Stars + Honey "5 reasons women over 40 are switching": bylined, contrarian lead, macro specs inside a beat, proof and named quotes as the final beat; no price or CTA in the article body, which is the gap to fix with `offer-bridge` (https://starsandhoney.com/advertorials/women-over-40-5-reasons).
- Skinesa "Special skin health report": news-style headline, symptom checklist as self-qualification, JAMA citation inside a reason, guarantee as the closing header; the "special report" kicker without a disclosure label is the compliance gap (https://www.skinesa.com/pages/5-reasons-why).
- Noble Origins long-form advertorial: transition hooks between beats, full ingredient label reproduced as proof, bottom-line recap and future-pacing before a single CTA (https://nobleorigins.com/pages/lp-5-reasons-bundle-v2).
- MUD\WTR runs three advertorial types by awareness stage on third-party publishers (https://blog.funneloftheweek.com/p/bloody-ocean-advertorial-strategy-what-mud-wtr-uses-to-thrive-in-the-4b-mushroom-coffee-market).

## Checklist

```json
{
  "page_type": "advertorial",
  "aliases": ["editorial pre-sell", "native article", "pre-lander", "story page", "sponsored article", "special report"],
  "funnel_stage": ["tof"],
  "awareness": ["unaware", "problem-aware"],
  "traffic": ["meta", "native", "tiktok"],
  "sections": { "min": 8, "max": 12 },
  "mandatory_sections": ["dateline", "hero", "hook", "problem", ["mechanism", "discovery"], "offer-bridge", "reviews", "closing-cta"],
  "recommended_sections": ["agitation", "solution", "qualifier", "benefits", "guarantee", "faq", "disclaimer"],
  "forbidden_sections": ["header", "announcement", "product-grid", "cross-sell", "countdown", "stock-indicator", "email-capture", "sms-capture"],
  "nav": "none",
  "price_above_fold": "forbidden",
  "cta": { "min": 1, "max": 3, "first_after_section": 4, "sticky": "optional", "copy_pattern": "next-step" },
  "proof": { "min_modules": 2, "max_modules": 4, "required_kinds": ["review-quote"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "in-use", "result-or-context"], "hero": "editorial-lifestyle", "video": "optional", "min_images": 4 },
  "copy_framework": ["story-lead", "pas", "hook-story-offer"],
  "offer_compat": { "allowed": ["none", "trial-sample", "first-order", "free-shipping", "gwp", "bundle", "percent-off", "fixed-off"], "forbidden": ["bogo", "tiered-volume", "bundle-decoy", "subscribe-save", "referral", "loyalty", "cashback", "bnpl", "mystery", "pre-order-price", "price-lock", "flash-sale", "clearance", "limited-edition", "gift-card", "student-military", "charity"] },
  "urgency": "none"
}
```

## Sources

- https://www.getlandra.com/blog/how-to-build-an-advertorial-landing-page
- https://www.getlandra.com/blog/how-to-write-an-advertorial
- https://www.getlandra.com/blog/listicle-vs-advertorial-supplement-brands
- https://www.getlandra.com/blog/5-stages-of-awareness
- https://landgoose.com/blog/advertorial-landing-page-template
- https://adlibrary.com/posts/advertorial-landing-pages
- https://openadlibrary.com/blog/advertorial-landing-page-examples/
- https://www.fudge.ai/guides/shopify-advertorial-landing-page/
- https://ecommercegrowth.co.uk/advertorial-landing-pages-for-dtc/
- https://www.nngroup.com/articles/website-reading/
- https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance
- https://www.asa.org.uk/advice-online/before-and-after-photos.html
- https://starsandhoney.com/advertorials/women-over-40-5-reasons
- https://www.skinesa.com/pages/5-reasons-why
- https://nobleorigins.com/pages/lp-5-reasons-bundle-v2
- https://try.miraclebrand.co/a/s6-reasons-new
- https://blog.funneloftheweek.com/p/bloody-ocean-advertorial-strategy-what-mud-wtr-uses-to-thrive-in-the-4b-mushroom-coffee-market
