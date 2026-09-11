# Listicle

Numbered reasons for one product, written for paid social. The visitor arrives from a Meta or TikTok ad whose headline was a number ("5 reasons", "7 signs"), is problem-aware or solution-aware, scans rather than reads, and must click through to the buy box or add to cart. Each reason answers one objection or desire and earns one click.

## Identify it

Signals in the brief:
- A number in the ad or brief: "5 reasons", "top 7", "N things you did not know", "7 signs your X is not working".
- Paid social traffic (meta, tiktok); audience knows the category or is comparing; benefits are parallel, not sequential.
- Merchant wants fast-to-fork variants by audience, product or offer (Javvy, Ridge run several at once).

Near neighbours:
- `seo-buyers-guide`: choose it when traffic is search and the query is "best X" or "top N X"; search readers expect a ranked roundup of several products with methodology, handled in `references/generate-listicle.md`. This file is the paid-social page for one product.
- `comparison-us-vs-them`: choose it when the visitor named a competitor or searched "vs"; intent is evaluative.
- `advertorial`: choose it when the audience is unaware and the ad is a story; a numbered frame to an unaware reader collapses.
- `ad-landing-page`: choose it when the ad is direct response without a number.

Landra: listicle for solution-aware and comparison shoppers, warm retargeting, high-intent "best X" search; it serves cold traffic only when the headline names the problem, not the product (OPERATOR, https://www.getlandra.com/blog/how-to-write-a-high-converting-listicle). Traffic tone: `references/traffic-source-meta.md`, `references/traffic-source-tiktok.md`. This file holds the contract.

## Variants

- **Problem-led list ("7 signs your current solution is not working").** Problem-aware traffic. Headline names the problem, not the product; price held until reason 3 or later; the product appears by reason 2.
- **Reasons list ("5 reasons N people switched").** Solution-aware traffic. Proof count or audience in the headline; price may appear in the offer bar.
- **Cost-per-use list.** One reason is the arithmetic reframe (per-day, per-serving, per-use against the alternative); the figure is an offer-ledger row (research block 38).

## Anatomy

Modal order from 12 fetched listicles (internal teardown audit, 2026-09-10): offer bar, numbered H1, optional proof strip, five to six reasons, review quotes, buy box or single CTA block, badges, rarely FAQ.

1. `announcement` (chrome, does not count) conditional: warm or solution-aware traffic with a ledgered offer. Discount or per-day price and free-shipping threshold; 8 of 12 teardowns open this way. No timer, no stock count.
2. `hero` mandatory. Numbered H1 with the audience or a verified proof count baked in ("5 reasons 1,000,000+ home chefs are making the switch"), one-line subhead or a verbatim customer quote as subhead (LOAM); editorial header image. 12 of 12 use a numbered headline; 4 of 12 carry the proof count or audience in it.
3. `stats` or `review-summary` recommended. Proof strip under the hero: rating with count, servings sold, expert credential; 5 of 12 teardowns.
4. `comparison` recommended. Category-reframing table or quick-stats bar above the first reason ("us versus the usual"); reported on Obvi and Javvy, absent from the fetched sample.
5. `list-item` mandatory, five to seven items (five in 10 of 12). Each: outcome subhead, two to three sentences, one image with a benefit caption, optional matched CTA. Reason 1 answers the category's biggest objection (6 of 12). One fear or tension reason mid-list with a third-party citation (Miracle "Your sheets are damaging your skin"). One identity reason ("the soda for the anti-soda club"). Proof inside at least two reasons (clinical stat in 6 of 12). The last reason is the guarantee, the offer or the proof count (7 of 12 combined); a founder story is the alternative (LOAM).
6. `reviews` mandatory. Three to six titled, named, dated quotes after the list (8 of 12); named quotes in 6 of 12, unattributed in 2 (the failure).
7. `buy-box` or `closing-cta` mandatory (one of). Embedded buy box on the same URL in 5 of 12 (Create, AG1, Lion Pose, Perfy, Jones Road); otherwise one closing CTA block linking to the PDP. Open loop optional ("reason 11 revealed at checkout", Javvy).
8. `trust-bar` recommended. Badge row with guarantee, shipping, certifications; 6 of 12.
9. `faq` conditional: the merchant has three or more real objections not covered by a reason; 2 of 12 teardowns.

Forbidden: `header`, `product-grid`, `cross-sell`, `countdown`, `stock-indicator`, `email-capture`, `sms-capture`, `quiz`. Index length 8 to 13; hero plus five reasons plus reviews plus buy box is the 8-section floor. Ten to eleven reasons (Obvi, Javvy, reported) exceed the ceiling; cap at eight reasons and fork a second page for the rest.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.get` with the product id: every media item mapped to a job (`identity`, `detail`, `scale`, `in-use`, `included-items`, `ingredient-or-material`, `label-or-facts-panel`, `variation`); variant count and axes (decides the close: buy box, quick add or a PDP link); price and compare-at (ledger basis), per-day arithmetic inputs, selling plans (a subscription ladder is a misfit, `references/offers/offer-types.md`), inventory (never shown).
2. `lexsis_campaigns.creatives` and `analyze`: the number in the ad headline (the H1 must match it), the noun phrase and promise, the persona, the scene for the editorial header (`references/copy/message-match.md`); `frames` for a video ad.
3. `lexsis_catalog.reviews_status`, `review_collections` (active), `reviews` (`product_id`, `limit: 100`, `has_media`): band per `references/proof/reviews-sourcing.md`; one quote per reason where a matching review exists via `reviews_search` with each reason's claim; a customer count only from an export or API total with an as-of date.
4. `lexsis_brand.context` and `brand_kit` (`theme_id`): tokens, voice, guarantee and shipping facts, certifications with issuer, the founder record when a founder reason is planned. Skip `navigation`; nav is none.
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`: `lifestyle`, `hero`, `product-shot`, `flat-lay`, `social-proof`, `logo`; then semantic per reason. Count usable images: the hero plus one per reason is the floor (six for five reasons); view candidates with `lexsis_assets.view`.
6. `lexsis_workspace.credits` only when the header backdrop is the plan's bold moment and nothing real fits.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `announcement` (conditional: warm or solution-aware traffic with a ledgered offer) | one line stating the offer or per-day price and the free-shipping threshold; the warm-traffic link. | no. No-go: a timer, a stock count, two bars. | `AnnouncementBar` with one static message for warm traffic, none for cold problem-led lists. | one line, under 60 characters, the offer exactly as the ad states it (`references/offers/offer-types.md`). | the offer ledger row; awareness from `lexsis_campaigns.analyze`. |
| `hero` | the numbered H1 with the audience or a verified count, a one-line subhead or verbatim quote, over an editorial header image. | yes; `editorial-lifestyle` echoing the ad, or `product-in-context`; the headline stays HTML text over a quiet zone. Search: the ad frame via `lexsis_campaigns.frames` (import the brand-owned original with `lexsis_asset_import.import`; a creator frame needs a rights row; use the clean original, since the exported ad usually carries baked-in text), then library `hero` then `lifestyle`, then semantic "<product> in use, <ad scene>", then merchant upload. Gap: feasible purpose `hero_bg` under a real cut-out only when the plan names the header as the bold moment; fast-draft uses the best in-use image and lists the hero as missing. No-go: a grid of thumbnails, a packshot on white for cold social, a generated scene with people. Message match is judged by eye against the creative: same SKU, variant, angle and colourway, never by filename. `lexsis_asset_library.search` with `mode: "ocr"` flags library candidates that carry baked-in text before they are viewed. | `none`; a static `<picture>`. `HeroMedia` only for the full-bleed bold moment, autoplay and effects off unless the plan names that motion moment (N10) | H1 at most 12 words, the number equal to the ad's number (`references/copy/message-match.md`); proof count rounded down with an as-of date, or the audience when reviews are below band B2; no blacklist words (`references/anti-patterns/copy-anti-patterns.md`). | `lexsis_campaigns.analyze`; `reviews_status` band; a `customer-count` ledger row. |
| `stats` or `review-summary` | the proof strip under the hero: rating with count, units sold, an expert credential. | no photography; an award or certification mark only as issuer artwork with a ledger row (`references/proof/press-and-media-mentions.md` for press). No-go: count-up animations, icon tiles, three conflicting counts. Any logo or mark is still opened with `lexsis_assets.view` before use. | `none`; HTML numbers (StatCards is deprecated). An average appears only at band B2 or higher, always beside n. | two or three numbers, each with its unit and as-of date where older than 90 days. | ledger rows for every numeral; RS3 in `references/proof/reviews-sourcing.md`. |
| `comparison` | a category-reframing table or quick-stats bar above the first reason. | one `comparison-visual` of our attribute physically (catalog `detail` or `scale`, then library, then merchant upload); the alternative is an inline SVG silhouette. Gap: generation is not feasible (GN8); the table stands with our identity image in the header meanwhile. | `none`; a static HTML table (Tabs is deprecated). | four to six rows, cells at most 6 words, one concession row. | `test-data` rows per cell. |
| `list-item` (five to seven, each its own section) | one objection or desire answered per reason, each with one image and a benefit caption. | yes, one real image per reason, job chosen by the reason's role: reason 1 (the category's biggest objection) takes `detail` or `scale`; the mechanism reason takes `ingredient-or-material`, `sequence` or an authored `diagram`; the fear or tension reason takes `result-or-context` (a context image of the situation; a result only with a verified `P` row); the identity reason takes `in-use` or rights-cleared `ugc`; the closing reason takes `included-items` or `packaging` for an offer, `founder-or-team` for a founder story, or the `identity` shot beside the guarantee. Search per reason: catalog media by job, then library `product-shot`, `lifestyle`, `flat-lay` or `social-proof`, then semantic "<reason claim>", then merchant upload. Gap for a reason: ask rule naming the reason, its job and aspect; feasible purpose `product_composite` for one `context` reason at most, never `in-use`, `scale`, results or ingredients (GP14); the same image at a second crop serves at most one extra reason; shortening the list or re-typing the brief as `ad-landing-page` happens only on the merchant's choice and is recorded. No-go: emoji or icon markers, a caption baked into the image, a reason that is a feature without an outcome. `lexsis_asset_library.search` with `mode: "similar"` and `similar_to_asset_id` set to the first accepted reason image pulls candidates that match its lighting and styling; that mode ignores `query`, `kind` and `theme_id` and takes only `limit` (at most 48), so it returns the seed asset's neighbours rather than a filtered set, and each one still goes through the fit review. | `none`. A matched per-reason CTA is an HTML anchor to the buy block, soft copy first. | `listicle` spine; each reason a mini `fab` (the fear reason a mini `pas`); subhead at most 8 words; body at most 60 words; a number, material, time, test or named person in every reason; a quote or citation inside at least two reasons; no blacklist words (`references/anti-patterns/copy-anti-patterns.md`). | the image inventory from context reads 1 and 5; `reviews_search` per reason; `test-data` rows. |
| `reviews` | three to six titled, named, dated quotes after the list. | `ugc` screenshots or `review-with-media` where rights exist (`has_media: true`; library `social-proof` with a `P` row). Nothing found: the quotes run as text; generation is never feasible (GN9). | by band per `references/proof/reviews-sourcing.md`. B1: one quote under the reason it matches, static. B2 and above: static quote blocks matched to reasons plus an average and n at the close, or `ReviewCarousel` bound to an active collection when the quotes do not map to reasons, all cards visible, autoplay off (its default is on, N10). Never first. B0: `guarantee`, `certifications` and product evidence replace it; the proof-count headline becomes an audience headline; the omission is recorded. | verbatim, dated, attributed as stored, titled where the data has titles; at most 60 words. | `reviews_status`; active `review_collections`; `reviews_search` hits confirmed by the merchant. |
| `buy-box` or `closing-cta` | the close: an embedded buy block on the same URL, or one CTA block to the PDP. | a gallery of three from catalog media (`identity`, `scale`, `variation`) for the embedded form; one identity image for the link form. Gap: no generation is feasible in a gallery (GP11). | `BuyBox`, one per page, when the close is a full buy block with shipping line and guarantee, its form decided by the variant count and axes, with `ProductHero` for the three images; `QuickAdd` when the close is one button beside the identity image and the product needs a variant picker but no quantity or subscription; `none` (one link) when the merchant keeps the PDP as the buy surface. `StickyBar` bound to the buy block, appearing after reason 1 scrolls out, the offer or per-day figure in its label; link it to the main purchase state using the live schema. | `add-to-cart` on the embedded button ("Add to cart, $39"); `next-step` on a link ("Get the pan"); savings math for a bundle close from the ledger (`references/offers/offer-types.md`); an open loop ("reason 11 revealed at checkout") optional. | variant count and axes; the merchant's buy surface; offer ledger rows; page length. |
| `trust-bar` | guarantee, shipping and certification facts under the close. | no photography; certification marks only as issuer artwork with a ledger row. Gap: generation is not feasible for badges (GN5). Any logo or mark is still opened with `lexsis_assets.view` before use. | `none`; a static HTML row (Marquee is deprecated). | three or four facts, at most six words each. | policy URLs and certification rows. |
| `faq` (conditional: three or more real objections not covered by a reason) | the leftovers, collapsed. | no. | `none`; native `<details>` and `<summary>`. | answers at most 60 words. | `reviews_search` on objection topics not already used as reasons. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | `identity`, `detail`, `variation`, sometimes `included-items` | `in-use` for the identity reason, `scale` for reason 1, `ingredient-or-material` for the mechanism reason | reuse one existing image at a second crop for at most one reason; ask the merchant to upload the rest (identity-bound, no generation); shorten or re-type only on their call |
| asset library | `lifestyle` header candidates, `social-proof` with rights, `flat-lay`, `logo` | in-use of this exact SKU in the ad's scene | tag search, then semantic per reason; view before assigning; UGC only with a `P` row |
| ad creatives | the header image and the number in the H1 | anything below the header | import the brand-owned frame with `lexsis_asset_import.import`; a creator frame needs scoped rights |
| generation | `hero_bg` under a real cut-out when the header is the bold moment, `product_composite` for one `context` reason, `texture_fill` | product, people, results, ingredients, logos, text | never; ask the merchant to upload instead |

With only an identity shot and one in-use image the page cannot carry five imaged reasons: the plan lists the four missing reason images with the upload offer, fast-draft ships hero, a two-reason list, reviews at any band above B0, the buy block and trust bar with the gaps recorded, and the list shortens or the brief is re-typed as `ad-landing-page` only on the merchant's decision. Generated assets: at most four per page, usually zero or one `hero_bg`.

## Above the fold (390px)

Recipe from the teardowns (part D section 3):
1. Offer bar, one line, when the traffic is warm: discount or per-day price plus threshold; none for cold problem-led lists.
2. Numbered H1, at most 12 words, carrying the audience or a verified count.
3. One-line subhead or a verbatim quote.
4. Proof strip: rating plus count, or count only under 5 reviews, or an expert credential.
5. The heading of reason 1 visible or one thumb-scroll away.

Price: in the offer bar for warm traffic; held until reason 3 or later for cold problem-led lists (OPERATOR, Landra). Must not appear: a hero CTA (the offer bar carries the warm-traffic link), a countdown, a stock count, a resetting timer (Lion Pose's 20-minute timer and Miracle's 15-minute bar are the anti-pattern), two offer bars, a product grid, press logos without links.

## Proof

Density: 2 to 4 modules (index). Research minimum: one quote or data point per reason where available, star summary at the close; each reason's proof sits beside it (internal teardown audit, 2026-09-10).

| Kind | Where | Minimum evidence |
|---|---|---|
| `customer-count` or `review-summary` | H1 or `stats` | export or API count, rounded down, as-of date; average only at 5 or more reviews |
| `test-data` | inside a reason | journal, year, n and design copied exactly (AG1 footnotes 3 of 5 reasons) |
| `review-quote` | inside reasons 3 and 5, and in `reviews` | verbatim, dated, attribution as stored; titled like a headline where the store's data has titles |
| `expert-quote` | inside a reason, credential line not a logo | named, verifiable credential, approval, connection disclosed (HexClad places the chef inside reason 4) |
| `guarantee` or `policy-fact` | last reason and `trust-bar` | policy URL, exact terms |
| `award` | subhead | issuer, year, category (Lion Pose "Allure Best of Beauty") |

Placement by scroll depth: a number in the top 20% (6 of 12), data inside reasons at 20 to 60%, human quotes at 60 to 80% immediately before the buy box (9 of 12), badges at the bottom. Forbidden kinds: `social-proof-popup`, `live-viewer-count`, `press-logo-unlinked`. Never three conflicting counts on one page (Create shows 22,000, 5,000 and 400,000); one ledger row per number.

Zero reviews: `references/proof/reviews-sourcing.md` tiers 4 and 5. `reviews` becomes `guarantee`, `certifications` and product evidence; the proof-count headline becomes an audience headline; the plan records the omission.

## Offer and CTA

- CTA count: 3 to 6. One matched CTA per reason is allowed (Sun Powder after reasons 1 and 3; Miracle in-copy links in reasons 1, 3 and 5), plus the closing CTA; the offer bar and a sticky bar are chrome and do not count. HexClad's single CTA at the very end is the under-count to avoid.
- First CTA: after reason 1 (`first_after_section: 1`; the hero carries no button). The first CTA is soft ("See why it made the list"); later CTAs name the action.
- Sticky: optional. Javvy's "Yes, get 58% off" bar and AG1's "$3/day" bar are the observed pattern (3 of 12 inferred); evidence for sticky bars is mixed (`references/page-types/ad-landing-page.md`). When used: appears after reason 1 scrolls out, price or per-day figure in the label, one button.
- Copy pattern: `next-step` for per-reason CTAs that scroll or link to the buy box ("See the offer", "Get the pan"); `add-to-cart` on the embedded buy box itself. The reason's outcome sits as microcopy under the button, not in it (design-rules A12: the CTA names the action).
- Price reveal: offer bar for warm traffic; reason 3 or later for cold problem-led lists; always before the first hard CTA. Per-day framing in 4 of 12 (AG1 under $3, LOAM under $2, Create $1.33) is an offer-ledger row when arithmetically true.
- Offer fit: `none`, `bundle` ("best value" as the last reason with savings math), `trial-sample`. `percent-off`, `fixed-off`, `gwp`, `free-shipping`, `first-order`, `bogo`, `bnpl` only below the fold after the first proof for cold traffic (offer-types OF7); in the offer bar for warm traffic.
- Offer misfit: `subscribe-save` (a ladder inside a listicle breaks the scan; Create embeds one and shows three conflicting proof counts beside it), `tiered-volume`, `bundle-decoy`, `referral`, `loyalty`, `cashback`, `mystery`, every timing offer. `references/offers/offer-types.md` governs.
- Urgency: `none`. No countdown, stock count or "sell-out risk" line anywhere (urgency-scarcity UR6). The offer bar states the offer, not a deadline.

## Imagery

Required jobs: `identity`, `in-use`. Strongly recommended: `ugc` (review screenshots inside reasons), `ingredient-or-material`, `result-or-context` (substantiated only), `comparison-visual` for the reframing table, `founder-or-team` when a founder reason exists.
- Hero: `editorial-lifestyle`, an editorial header photo that echoes the ad; the numbered headline stays HTML text over a quiet zone.
- Balance: one image per reason; about 60% in-use or editorial, 40% product, ingredient or graphic; benefit caption on each as HTML, never baked into the image.
- Video: optional; a UGC clip inside the identity or proof reason, 20 to 40 seconds, click to play with poster and captions.
- Minimum images: 6 (hero plus one per reason); research range 6 to 12.
- Slots the plan must create: hero; one per reason with its benefit caption; comparison graphic when `comparison` exists; buy-box gallery of three when the buy box is embedded; review screenshots when rights exist.

## Copy

- Framework: `listicle` as the spine; each reason is a mini `fab` (feature, advantage, benefit) or, for the fear reason, a mini `pas`. Transition hooks between reasons keep the slide moving.
- Headline by awareness: problem-aware names the problem, not the product ("7 signs your protein powder is working against you"); solution-aware names the switch with a verified count or the audience ("5 reasons 1,000,000+ home chefs are making the switch", "5 reasons Jones Road works for mature skin"). Never a product name to a problem-aware audience.
- Message match: the number in the H1 equals the number in the ad; the H1 shares the ad's noun phrase and promise (60% token overlap); the hero image echoes the ad creative; the offer in the bar equals the offer in the ad (`references/copy/message-match.md`).
- Reading level: grade 6 to 8; 79% of users scan and the F-pattern dominates without subheads (RESEARCH, NN/g, https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/), so every reason opens with an outcome subhead.
- Length ceilings: H1 12 words; reason subhead 8 words; reason body 60 words (Perfy's 20 to 40 word reasons are the thin end; AG1's two to three sentences with a stat are the model); quote 60 words; total 600 to 1,200 words.
- Vocabulary: reasons are objections and desires, not features; each reason carries a number, material, time, test or named person; no blacklist words; no emoji as reason markers (Create and Sun Powder use them; design-rules N1 forbids it); sentence case; numbering correct (AG1 numbers "5." twice); no typos on a paid page (Jones Road mature-skin page ships three).

## Never

- Never render a header, navigation or footer link columns; 9 of 12 teardowns strip them.
- Never write a reason that is a feature without an outcome.
- Never leave the only CTA at the bottom of the page.
- Never name the product in the H1 for problem-aware traffic.
- Never show a countdown, stock count, "sell-out risk" or resetting timer.
- Never run two offer bars or two competing offers.
- Never show unattributed quotes or conflicting proof counts.
- Never use emoji as bullets or reason markers.
- Never place a subscription ladder inside the list.
- Never exceed eight reasons on one page; fork instead.
- Never hide the price until the footer for warm traffic, or show it above the fold for cold problem-led traffic.
- Never send more than one destination from the CTAs.

## Examples

- HexClad "5 reasons 1,000,000+ home chefs are making the switch": proof count in the H1, celebrity chef inside reason 4, lifetime warranty as reason 5, 86,000 reviews and three named quotes before the close (https://hexclad.com/pages/listicle-one).
- AG1 "5 health benefits": per-day sticky bar, a footnoted stat in three of five reasons, 50,000 reviews line, value-stack offer box with struck free items, three-question FAQ (https://drinkag1.com/5-reasons-why-variant-a).
- Javvy "11 reasons why" template forked by product, audience (55+) and offer, with a sticky "Yes, get 58% off" bar and the offer as reason 9 (https://www.getlandra.com/blog/javvy-listicle-playbook).

## Checklist

```json
{
  "page_type": "listicle",
  "aliases": ["reasons page", "N reasons why", "problem-led list", "7 signs page", "editorial listicle", "listicle pre-sell"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["problem-aware", "solution-aware"],
  "traffic": ["meta", "tiktok"],
  "sections": { "min": 8, "max": 13 },
  "mandatory_sections": ["hero", "list-item", "reviews", ["buy-box", "closing-cta"]],
  "recommended_sections": [["stats", "review-summary"], "comparison", "trust-bar", "faq"],
  "forbidden_sections": ["header", "product-grid", "cross-sell", "countdown", "stock-indicator", "email-capture", "sms-capture", "quiz"],
  "nav": "none",
  "price_above_fold": "optional",
  "cta": { "min": 3, "max": 6, "first_after_section": 1, "sticky": "optional", "copy_pattern": "next-step" },
  "proof": { "min_modules": 2, "max_modules": 4, "required_kinds": ["review-quote"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "in-use"], "hero": "editorial-lifestyle", "video": "optional", "min_images": 6 },
  "copy_framework": ["listicle", "fab", "pas"],
  "offer_compat": { "allowed": ["none", "bundle", "trial-sample", "percent-off", "fixed-off", "gwp", "free-shipping", "first-order", "bogo", "bnpl"], "forbidden": ["subscribe-save", "tiered-volume", "bundle-decoy", "referral", "loyalty", "cashback", "mystery", "pre-order-price", "price-lock", "flash-sale", "clearance", "limited-edition", "gift-card", "student-military", "charity"] },
  "urgency": "none"
}
```

## Sources

- https://www.getlandra.com/blog/how-to-write-a-high-converting-listicle
- https://www.getlandra.com/blog/listicle-landing-page-examples-that-convert
- https://www.getlandra.com/blog/javvy-listicle-playbook
- https://www.getlandra.com/examples/hexclad
- https://www.getlandra.com/examples/ridge
- https://share.snipd.com/episode/59023fd3-a0c6-4c47-b1c6-38398a84118d
- https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/
- https://hexclad.com/pages/listicle-one
- https://drinkag1.com/5-reasons-why-variant-a
- https://try.miraclebrand.co/a/s6-reasons-new
- https://loamscience.com/pages/5-reasons-to-choose-loam
- https://trycreate.co/pages/5-reasons-try-create-sub
- https://drinksunpowder.com/pages/sun-powder-5-reasons-why
- https://lionpose.com/pages/5-reasons-placenta-facial
- https://try.drinkperfy.com/5-reasons-why-perfy-is-the-perfect-soda/
- https://www.jonesroadbeauty.com/pages/makeup-for-mature-skin-5-reasons-why
