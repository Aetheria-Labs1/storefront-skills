# Comparison: us vs them

An attribute table against a named competitor, a generic alternative or the merchant's own tiers. The visitor arrives from a "X vs Y" or "alternative to X" search, a comparison ad or a retargeting click, is solution-aware or product-aware, currently uses or is considering the alternative, and must decide to switch. The page wins by being honest about who each option is for.

## Identify it

Signals in the brief:
- "vs", "compared to", "alternative to", "why switch", "us vs them", a competitor named, or "the old way" named (foam earplugs, drip coffee, grocery-store beef).
- Audience "currently uses X" or "is comparing us to X".
- A comparison ad in the campaign (Zipify-style two-column creative).

Near neighbours:
- `listicle`: choose it when the frame is "N reasons" for one product without a named alternative.
- `seo-buyers-guide`: choose it when the query is "best X" and the page ranks several products with methodology; handled by `references/generate-listicle.md`.
- `pdp-hybrid-landing`: choose it when the comparison is one table inside a buy page; RISE DTC places it below the description.
- `ingredient-science`: choose it when the brief is "how it works" without a rival.

Search-intent inputs live in `references/traffic-source-google.md`; this file owns the comparison structure and native table decisions.

## Variants

- **Named competitor (Ekster vs Ridge).** Three columns: us, the named rival, "Others". A fair "In focus: [rival]" paragraph precedes the verdict. Competitor facts are merchant-confirmed with a source URL and a checked date; re-verify quarterly.
- **Generic alternative (Radius Butcher vs grocery-store beef).** Second column is the category norm the visitor uses today; rows are outcomes with numbers.
- **Intra-brand tiers (Huel Black vs Powder vs Essential; Wakefit series; Endy compare).** Columns are the merchant's own SKUs; every row is a decision fact (price per meal, firmness, height); "most loved by" persona rows and a one-line who-it-is-for per tier prevent choice paralysis. One CTA per tier, so at most three tiers on a page.

## Anatomy

Observed order from the two fetched comparison pages (internal teardown audit, 2026-09-10): question headline, matrix, verdict, trust row, reasons to switch, stats, in-focus narrative, head-to-head sections, conditional verdict, reviews, decision-question FAQ.

1. `hero` mandatory. Question headline or switching headline with a verified count ("What is the best smart wallet? Ekster vs Ridge", "Why 10,000 customers switched"), one-line pain hook, "full comparison below". Compact; the table is one thumb-scroll away.
2. `verdict` recommended. One sentence per option stating who it is best for, before the table. Honesty here is what makes the table believable (RESEARCH, Grow and Convert finding via https://aitoolsguidebook.com/en/articles/product-comparison-copy-ai/).
3. `us-vs-them` mandatory (`comparison` for the intra-brand variant). Four to six rows, decision-driving attributes only, outcomes with numbers ("Ride up to 40 km", not "long range"); our column emphasised by position and a hairline, not by colour shouting; at least one row where the alternative wins or a "pick them if" line; a third "Others" column where the category has many players; header row carries our product photo and text labels for the others; a "facts checked [month year]" line with source URLs under the table.
4. `features` or `benefits` recommended. Row-by-row expansion with the proof for each row beside it.
5. `stats` recommended. Verified numbers (customers, reviews, years, warranty length) with ledger rows.
6. `reviews` mandatory. Switcher testimonials: "I tried three other brands before this"; two to three, dated, attributed; product tag on each review for the intra-brand variant (Endy).
7. `guarantee` mandatory. Migration and risk reversal: trial nights, returns, warranty, a switcher offer where ledgered.
8. `product-spotlight` or `buy-box` recommended. Our product with price, variant and the CTA; for the intra-brand variant one card per tier with a one-line fit sentence.
9. `faq` recommended. "Is it really better than X?" and decision questions written as self-diagnosis ("Do you prefer to sleep higher off the ground?", Endy).
10. `closing-cta` mandatory. Conditional verdict in one line ("If your wallet still lives in isolation, X is fine; if you want Y, choose us"), then the CTA.

Forbidden: `header` beyond a logo and one utility link (nav is `minimal`), `product-grid`, `countdown`, `stock-indicator`, `email-capture`, `sms-capture`, `quiz`, `cross-sell`. Index length 7 to 10; research says 6 to 9; the index governs.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.get` with the product id (each tier for the intra-brand variant): media mapped to jobs (`identity`, `detail`, `scale`, `in-use`, `included-items`), variant axes, price and compare-at (ledger basis; a compare-at never becomes a "sale" framing here, `references/offers/offer-types.md`), per-use arithmetic inputs, selling plans (subscribe-save only for the intra-brand variant), inventory (never shown).
2. `lexsis_campaigns.creatives` and `analyze` only when a comparison ad drives the traffic: the two columns the ad shows and its claim, which the H1 repeats (`references/copy/message-match.md`). Search traffic: the query as typed supplies both names.
3. `lexsis_catalog.reviews_status`, `review_collections` (active), `reviews` (`product_id`, `limit: 100`): band per `references/proof/reviews-sourcing.md`; `reviews_search` with "switched from", "tried other brands" and the alternative's category name for switcher quotes; product tag per review for tiers.
4. `lexsis_brand.context` and `brand_kit` (`theme_id`): tokens, voice, guarantee and trial terms, certifications with issuer, the one utility link for the minimal header. `navigation` is not read; nav is minimal (logo plus one link).
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`: `product-shot`, `lifestyle`, `social-proof`, `logo`; then semantic per contested row ("<attribute> close-up"); view candidates with `lexsis_assets.view`.
6. Competitor facts: merchant-confirmed, sourced to the rival's public page or a third-party test with a checked date, recorded in the ledger before any row is written. `lexsis_workspace.credits` is rarely needed; the hero is a packshot type and generation would sit below the fold behind the ASK line.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `hero` | a question or switching headline naming both sides, a one-line pain hook, the table one thumb-scroll away. | yes; `packshot` of our product, or `product-in-hand` for accessories. Search: catalog media `identity`, then library `product-shot`, then merchant upload. Gap: no generation is feasible for the product (GN1) and a backdrop does not fit a compact hero; fast-draft runs the headline over the page background and lists the hero as missing. No-go: a side-by-side with the rival's product photo, a competitor logo, a before-and-after. | `none`; a static `<img>`. The header above it is plain HTML with the logo and one utility link, no `Navbar` island. | H1 at most 12 words with both names as typed in the query, or the ad's claim; a verified count only with a ledger row; no blacklist words (`references/anti-patterns/copy-anti-patterns.md`). | the query or `lexsis_campaigns.analyze`; a `customer-count` row. |
| `verdict` | one sentence per option stating who it is best for, before the table. | no. | `none`. | one sentence per option; "best for", not "better". | the merchant-confirmed positioning of each option. |
| `us-vs-them` (`comparison` for the intra-brand variant) | four to six decision rows, outcomes with numbers, our column emphasised by position and a hairline, one row the alternative wins, sources and a checked date under the table. | yes; our `identity` image in the header cell (one per tier for the intra-brand variant), text labels for the others; one `comparison-visual` that shows our attribute physically (thickness, layers, capacity) without the rival's product. Search: catalog media `identity` and `detail`, then library `product-shot`, then merchant upload; the alternative as an inline SVG silhouette labelled "other brands". Nothing found: shared fallback for the comparison visual; generation is not feasible (GN8) and the table is never an image; the table stands with the header photo meanwhile. Confirm by eye that no competitor product, logo or text is in frame. | `none`; a static HTML table. On 390px the row-label column stays pinned and the option columns scroll, or the rows stack per option; the Tabs island is deprecated and a tabbed table hides the comparison (CSS-only tabs or `<details>` only if a layout truly needs them). | `comparison`; cells at most 6 words; row labels as shopper questions ("Cards it holds"); a price row only when the rival's price is confirmed and dated; "facts checked <month year>" with source URLs. | `test-data` and `certification` rows for every cell; the ledger's competitor-fact rows. |
| `features` or `benefits` | row-by-row expansion with the proof beside each row. | yes; one `detail` macro per contested row where a photo proves it (`scale` or `included-items` where the row is size or contents). Search: catalog media, then library `product-shot`, then merchant upload. Gap for a row: shared fallback; no generation is feasible for detail, scale or contents (GP14); the row runs as sourced text meanwhile. | `none`. | at most 60 words per row; metrics, not adjectives. | the rows in the table; ledger rows per row. |
| `stats` | verified numbers: customers, reviews, years, warranty length. | no photography; an award mark only as issuer artwork with a ledger row (`references/proof/press-and-media-mentions.md`). No-go: count-up animation, icon tiles. Any logo or mark is still opened with `lexsis_assets.view` before use. | `none`; HTML numbers (StatCards is deprecated). | two to four numbers, each with unit and as-of date where older than 90 days. | ledger rows for every numeral. |
| `reviews` | two or three switcher testimonials that name the alternative. | `review-with-media` where rights exist; otherwise text; generation is never feasible (GN9). | by band per `references/proof/reviews-sourcing.md`. B1: one quote that names the alternative, static. B2 and above: an average plus n near the verdict and static switcher quotes here; `ReviewCarousel` bound to an active collection built from the `reviews_search` hits only when three or more switcher reviews exist, autoplay off (its default is on, N10). Intra-brand: the product tag shown on each review. B0: `guarantee` plus product `test-data` replace it; the switching headline becomes a question headline; the omission is recorded. | verbatim, dated, attributed as stored; each quote mentions the switch or the rival category. | `reviews_search` candidates confirmed by the merchant or an active collection; `reviews_status` band. |
| `guarantee` | migration and risk reversal: trial nights, returns, warranty, a switcher offer where ledgered. | no; a certificate mark only as issuer artwork. Any logo or mark is still opened with `lexsis_assets.view` before use. | `none`. | exact terms and policy URL; the switcher offer only from a ledger row (`references/offers/offer-types.md`). | `guarantee` and offer ledger rows. |
| `product-spotlight` or `buy-box` | our product with price, variant and the CTA; one card per tier for the intra-brand variant. | yes; one `identity` image per product or tier from catalog media; `included-items` where the box contents were a row. Gap: no generation is feasible (GP11). | `BuyBox`, one per page, for a single product, its form decided by the variant count and axes, with `VariantSwatches` when colour variants carry images. Intra-brand tiers: static cards with one identity image and a fit sentence each, `QuickAdd` per card when the page runs cart v2 and the tier needs a variant picker, otherwise a link per tier; at most three tiers. `StickyBar` bound to the buy section after the table for the single-product variant only, no timer. | `next-step` with a low-pressure verb for search traffic ("Try it for 30 nights"); `add-to-cart` on a buy box or card; per-use or per-meal framing when true; BNPL line under the price on high-ticket rows (`references/offers/offer-types.md`). | the variant (named competitor, generic, intra-brand); variant count; offer ledger rows. |
| `faq` | "Is it really better than X?" and decision questions written as self-diagnosis. | no. | `none`; native `<details>` and `<summary>`. | answers at most 60 words; respectful about the rival. | `reviews_search` on decision doubts; the concession row. |
| `closing-cta` | the conditional verdict in one line, then the CTA. | optional reuse of the hero identity slot; no new job. | `none`; the CTA anchors to the spotlight or buy box. | "If X, they are fine; if Y, choose us"; the same verb as the first CTA. | the verdict section. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | `identity`, some `detail` | the `comparison-visual` (attribute shown physically), a macro per contested row, `included-items` | ask the merchant to upload the row's photo (identity-bound, no generation); the row runs as sourced text meanwhile |
| asset library | `product-shot`, `lifestyle`, `social-proof` with rights | the physical comparison shot | tag search, then semantic "<attribute> close-up"; view before assigning |
| ad creatives | the two columns and the claim for a comparison ad | imagery (the ad's rival side is never reused) | only the claim and column names travel to the page |
| generation | `texture_fill`, a `decorative_element`; the alternative's silhouette is authored SVG, not generated | product, competitor products, people, results, logos, text | never; ask the merchant to upload instead |

With only an identity shot the page still ships: hero, verdict, the HTML table with the identity image in its header, stats, switcher quotes at any band above B0, guarantee, spotlight with the same image, faq, closing; `features` runs as sourced text rows and the missing macros are listed with the upload offer. Generated assets: at most four per page, usually zero.

## Above the fold (390px)

Visible, in order:
1. Logo with one utility link (cart or store).
2. Question or switching headline, at most 12 words, naming both sides (or the tiers).
3. One-line pain hook or "full comparison below".
4. The first two rows of the table, or the verdict sentence, so the visitor sees the comparison has started.

Price: optional above the fold; a price row appears in the table only when the competitor's price is merchant-confirmed with a dated source; otherwise the row is omitted rather than estimated. Must not appear: a countdown, a stock count, competitor logos, competitor product photos, competitor reviews, an all-green versus all-red tick grid, an email popup, a carousel.

## Proof

Density: 2 to 3 modules (index). Research: the table itself must be sourced; two to three switcher quotes; a verified count in the headline; a link out to the competitor signals confidence (internal teardown audit, 2026-09-10).

| Kind | Where | Minimum evidence |
|---|---|---|
| `test-data` or `certification` | inside table rows, footnoted | spec sheet, lab report, certificate or the competitor's own public page, each with URL and checked date; numbers copied exactly |
| `review-quote` | `reviews`, one beside the row the visitor will doubt most | verbatim, dated, attribution as stored; mentions the switch or the rival category |
| `customer-count` or `review-summary` | `hero`, `stats` | export or API count, rounded down; average only at 5 or more reviews |
| `guarantee` or `policy-fact` | `guarantee`, beside every CTA | policy URL, exact terms (365-night trial, lifetime warranty, 30-day returns) |
| `award` | `stats` | issuer, year, category |

Competitor facts: merchant-confirmed, sourced to the competitor's public page or a third-party test, dated, re-verified quarterly (OPERATOR). Competitor reviews, star ratings, logos and product photographs are never rendered; the competitor is a text label. Forbidden kinds: `social-proof-popup`, `live-viewer-count`, `press-logo-unlinked`.

Placement: number in the top 20%, sourced rows at 20 to 40%, switcher quotes at 60 to 80% before the buy CTA, guarantee beside the closing CTA. Zero reviews: `references/proof/reviews-sourcing.md` tiers 4 and 5; the `reviews` section becomes `guarantee` plus product `test-data`; the switching headline becomes a question headline; the plan records the omission.

## Offer and CTA

- CTA count: 2 to 3. One directly under the table, one at `closing-cta`; the intra-brand variant may carry one per tier card instead (three tiers maximum). A sticky bar is chrome and does not count.
- First CTA: directly under the table, never above it (`first_after_section: 1`; when `verdict` is present the table is section 3 and the CTA follows it).
- Sticky: optional. Comparison shoppers scroll to evaluate; a bar that appears after the table scrolls out is acceptable, one button, no timer.
- Copy pattern: `next-step` with a low-pressure verb for search traffic ("Try it for 30 nights", "See the [product]"); `add-to-cart` on a buy box or tier card. Never "Switch now" as a demand; never petty copy about the rival (OPERATOR, Zipify, https://zipify.com/blog-ocu-us-vs-them-ad/).
- Price reveal: our price in the table row and on the product card; per-use or per-meal framing when arithmetically true (Huel table shows price per meal). Competitor price only when confirmed and dated.
- Offer fit: `none`, `free-shipping`, `trial-sample` (the natural switcher offer), `first-order` as a switcher offer, `gwp`, `subscribe-save` for the intra-brand variant, `bnpl` on high-ticket rows. `percent-off`, `fixed-off` and `bundle` only with a ledger basis and below the table.
- Offer misfit: `bogo`, `tiered-volume`, `bundle-decoy`, `referral`, `loyalty`, `cashback`, `mystery` and every timing offer; a discount makes the comparison read as a pitch. `references/offers/offer-types.md` governs.
- Urgency: `none`. Evaluative visitors punish pressure; no timers, counts or "last chance" anywhere.

## Imagery

Required jobs: `identity`, `comparison-visual`, `detail`. Strongly recommended: `scale`, `in-use`, `included-items` (what ships in the box against the rival's), `result-or-context` when substantiated.
- Hero: `packshot` of our product, or `product-in-hand` for accessories; no side-by-side with the competitor's product photograph (their column is text).
- Balance: studio 50%, in-use 35%, macro comparison shot 15%; the table is the centrepiece and stays HTML, never an image.
- Video: optional; a 45 to 90 second demo of the row the visitor doubts most, click to play with poster and captions.
- Minimum images: 3 (research range 3 to 6).
- Slots the plan must create: hero packshot; a `comparison-visual` that shows our attribute physically (thickness, layers, capacity) without the rival's product; one detail macro per contested row where a photo proves it; tier cards for the intra-brand variant (one image each).

## Copy

- Framework: `comparison` for the table and the "not for you if" prose; `4ps` around it (promise in the hero, picture in the rows, proof in quotes and sources, push at the close).
- Headline by awareness: solution-aware asks the question ("Which smart wallet actually protects your cards? Ekster vs Ridge"); product-aware states the switch with a verified count ("Why 46,351 reviewers chose Ekster over the alternatives"). Intra-brand: "Which [product] is right for you?".
- Message match: for search traffic the H1 contains both names as typed in the query; for comparison ads the H1 repeats the ad's claim and the same two columns (`references/copy/message-match.md`).
- Reading level: grade 6 to 8; table cells at most 6 words; a row label is a shopper question in plain words ("Cards it holds", not "Capacity").
- Length ceilings: H1 12 words; verdict one sentence per option; 4 to 6 table rows; row expansion 60 words each; concession paragraph 40 to 80 words; total 500 to 900 words.
- Vocabulary: metrics not adjectives ("affordable", "eco-friendly" fail); "best for" rather than "better"; every competitor fact is "as of [month year], per [source]"; no superlatives without substantiation ("#1", "most trusted" need market data, LAW: ASCI and FTC); respectful tone; no blacklist words; sentence case.

## Never

- Never render competitor logos, product photos, star ratings or reviews.
- Never publish a competitor fact without a source URL, a checked date and merchant confirmation.
- Never build an all-green-versus-all-red grid with no concession row.
- Never compare features when the row can compare outcomes with numbers.
- Never include a price row with an estimated or undated competitor price.
- Never write petty or mocking copy about the rival.
- Never place the first CTA above the table.
- Never show a countdown, stock count or "last chance" line.
- Never add a discount pill or "sale" framing to the comparison.
- Never exceed six table rows or three tier columns.
- Never let an unrelated product card interrupt the comparison (Ekster's collab card mid-page).
- Never render full store navigation.

## Examples

- Ekster vs Ridge: question headline, ten-attribute matrix with a third "Others" column, a fair "In focus: Ridge" paragraph before the head-to-head sections, a conditional verdict, 46,351 dated reviews; the matrix lacks a row Ridge wins, which is the concession to add (https://www.ekster.com/en-eu/pages/ekster-vs-ridge).
- Endy compare: two tier cards with one-line positioning, attribute rows (layers, height, firmness, cooling), "most loved by" persona rows, trust row, reviews tagged by product, FAQ written as self-diagnosis questions (https://www.endy.com/compare).
- Huel range table inside the Black Edition page: three SKUs, eight rows including price per meal; the intra-brand pattern that prevents choice paralysis (https://huel.com/products/huel-black-edition).
- Radius Butcher vs Whole Foods chart: outcome rows with numbers against a generic alternative (https://swipefile.com/us-vs-them-chart-that-converts).

## Checklist

```json
{
  "page_type": "comparison-us-vs-them",
  "aliases": ["comparison page", "competitor comparison", "why switch", "alternatives page", "versus page", "compare tiers"],
  "funnel_stage": ["mof"],
  "awareness": ["solution-aware", "product-aware"],
  "traffic": ["google-search", "retargeting"],
  "sections": { "min": 7, "max": 10 },
  "mandatory_sections": ["hero", ["us-vs-them", "comparison"], "reviews", "guarantee", "closing-cta"],
  "recommended_sections": ["verdict", ["features", "benefits"], "stats", ["product-spotlight", "buy-box"], "faq"],
  "forbidden_sections": ["header", "product-grid", "countdown", "stock-indicator", "email-capture", "sms-capture", "quiz", "cross-sell"],
  "nav": "minimal",
  "price_above_fold": "optional",
  "cta": { "min": 2, "max": 3, "first_after_section": 1, "sticky": "optional", "copy_pattern": "next-step" },
  "proof": { "min_modules": 2, "max_modules": 3, "required_kinds": ["review-quote", "test-data"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "comparison-visual", "detail"], "hero": "packshot", "video": "optional", "min_images": 3 },
  "copy_framework": ["comparison", "4ps"],
  "offer_compat": { "allowed": ["none", "free-shipping", "trial-sample", "first-order", "gwp", "subscribe-save", "bnpl", "percent-off", "fixed-off", "bundle"], "forbidden": ["bogo", "tiered-volume", "bundle-decoy", "referral", "loyalty", "cashback", "mystery", "pre-order-price", "price-lock", "flash-sale", "clearance", "limited-edition", "gift-card", "student-military", "charity"] },
  "urgency": "none"
}
```

## Sources

- https://daily.risedtc.com/p/the-us-vs-them-comparison-chart
- https://community.funnelish.com/t/how-to-build-a-high-converting-us-vs-them-comparison-table/9957
- https://swipefile.com/us-vs-them-chart-that-converts
- https://zipify.com/blog-ocu-us-vs-them-ad/
- https://aitoolsguidebook.com/en/articles/product-comparison-copy-ai/
- https://www.get-ryze.ai/blog/how-to-make-your-comparison-pages-ai-citable
- https://asktalha.me/case-studies/loop-earplugs-marketing-case-study/
- https://www.ekster.com/en-eu/pages/ekster-vs-ridge
- https://www.endy.com/compare
- https://huel.com/products/huel-black-edition
- https://www.wakefit.co/mattress/orthopaedic-memory-foam-mattress/WOMFM72366
- https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business
- https://www.ascionline.in/wp-content/uploads/2022/09/asci_june_july_2020_ccc_pr.pdf
