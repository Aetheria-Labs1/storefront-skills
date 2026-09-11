# Quiz funnel

A short sequence of questions that routes the visitor to one to three
products and shows why they match. Shoppers arrive problem-aware or
solution-aware from paid social or email and cannot self-select a shade,
size, formula or routine; their job is to answer, see a recommendation with
its reasons, and add the recommended set. The page has no navigation and no
price until the results screen. A quiz whose answers do not change the
recommendation is a form and routes to `lead-capture-giveaway`. The plan
describes anatomy only; design-page selects the runtime that renders
questions, branching and results.

## Identify it

- Brief says "find your", "which one is right for me", "shade finder",
  "routine builder", "assessment", "personalised", "match", or names a
  catalogue of 3 to 30 SKUs the shopper cannot choose between unaided.
- Traffic is cold or warm social where the audience is "entertainment, not
  shopping" (Jones Road sends TikTok traffic to an advertorial and then the
  quiz), or an email list the merchant wants to segment.
- Near neighbours:
  - `lead-capture-giveaway`: the answers do not change the outcome; choose
    capture (index tie-break: a quiz that does not route is a form).
  - `bundle-kit`: a set the merchant assembled; choose bundle when there is
    no routing.
  - `comparison-us-vs-them`: the visitor already named an alternative.
  - `product-finder` inside a `pdp` or `collection-landing`: a filter, not a
    funnel; choose quiz when the page's whole job is the routing.
- OPERATOR: cold-traffic quiz funnels are reported at 3 to 8% vs 1.5 to 3.5%
  for a PDP (MHI Growth Engine via Landra
  https://www.getlandra.com/blog/dtc-landing-page-conversion-benchmarks-2026 );
  Jones Road reports 16% quiz conversion and AOV $60 to $90
  https://www.octaneai.com/case-studies/jones-road-beauty ; Curlsmith 89%
  completion and 6.3% quiz conversion https://www.octaneai.com/case-studies/curlsmith .
  Vendor cases; use for relative expectations only.

## Variants

- **Shade or fit finder.** Image-choice answers (swatches on skin tones,
  body shapes); one product with the right variant pre-selected on results.
- **Routine or stack builder.** Answers fill two or three slots (cleanse,
  treat, protect); results show the set pre-loaded with per-item remove.
- **Assessment** (Hims, Traya). Framed as a diagnosis with a stage selector;
  results explain the stage before the products; regulatory disclaimer where
  the category requires it.
- **Quiz hub** (Jones Road quiz landing). Several product quizzes on one entry
  page, each a card with what it recommends and how long it takes, plus a
  human fallback ("send a selfie to our makeup artists, 1 to 2 business
  days").

## Anatomy

Counts exclude chrome. The question screens are one `quiz` section however
many screens they contain. Order follows the Traya and Jones Road entries in
internal research audit (2026-09-10) and the RevenueHunt, Octane AI and
Uplup guidance in internal research audit (2026-09-10) types 6 and 23.

1. `header`: mandatory chrome, nav `none` (logo only, not clickable). The
   only exit is the quiz.
2. `hero` (start screen): mandatory. Outcome headline ("Find your shade in 60
   seconds"), what they get, time estimate, one Start button. Proof on the
   start screen is one verified `customer-count` of takers or a
   `review-summary`, and an authorship line when real ("created by Bobbi").
   Concern chips (Traya's six concerns) may sit here as the first question.
3. `quiz`: mandatory. 5 to 8 questions, one per screen, large tap targets,
   image choice where possible, concrete questions first, use case or budget
   mid-quiz, every answer mapped to a product or collection, skip logic for
   irrelevant branches, a progress indicator, no open text fields. Ceiling:
   10 questions; more than 12 is forbidden (RevenueHunt
   https://docs.revenuehunt.com/customer-success/how-to-build-successful-quiz/ ).
   A question that does not change the recommendation is removed.
4. `email-capture`: conditional: the merchant has a lead goal. Placed after
   the last question and before results, never before question one; skippable
   ("Show my results" without email) unless the merchant confirms a hard gate
   and the plan records it. Marketing consent un-ticked; results shown either
   way. OPERATOR: Jones Road reports a 35% opt-in at the post-question gate
   (Octane AI, above).
5. `quiz-results`: mandatory. Personalised header using the answers ("Maya,
   here is your dry-skin routine"), a one to three line summary of what was
   learned, and the reason for the result. RESEARCH (vendor data): one
   results page converts 10.6% on average vs 7.1% for quizzes with 11 or more
   result pages (RevenueHunt, above).
6. `product-spotlight`: recommended (conditional in practice: two or three
   products). One card per recommended product with image, price,
   `review-summary` when 5 or more reviews, and a "why this matches you" line
   tied to a specific answer. One to three products total; a single product
   result carries its "why" inside `quiz-results`.
7. `buy-box`: mandatory. One "Add my set" CTA with the recommended set
   pre-loaded and trimmable, per-item add or remove, price of the set and any
   set saving shown as arithmetic; the quiz discount, if any, applied
   automatically. Side cart keeps the shopper on the results screen.
8. `guarantee`: recommended. Returns, shade or fit guarantee ("if we miss,
   we send the right one"), stated in one line beside the CTA.
9. `reviews` with a `-same-profile` suffix: optional. Two or three verbatim
   quotes from reviewers with the same result type.
10. `faq`: optional, on results only. "Can I change my answers?", "What if
    the shade is wrong?", returns.
11. `footer`: mandatory chrome; legal links only.

Never include `countdown`, `stock-indicator`, `product-grid`, `comparison`,
`problem` or `agitation` sections, an `announcement` bar with an offer, or
any price before the results screen. Sold-out products never appear in
results.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_capture.funnel_templates` then `lexsis_capture.funnel_template` for the quiz shape (shade or fit finder, routine builder, assessment): step types, branching, whether options carry images, how results map to products, whether the results step carries product slots or hands off to page sections.
2. `lexsis_catalog.list` then `lexsis_catalog.get` for the 3 to 30 candidate SKUs: identity media per product (results screen), per-variant images and colour hex for shade options (`swatch`, `variation` per `references/assets/image-jobs-by-page-type.md`), price, inventory (sold-out products never appear in results), selling plans (a plan option on results is `ask` in `references/offers/offer-types.md`).
3. `lexsis_catalog.reviews_status`; `lexsis_catalog.reviews` per candidate SKU for the results-screen summary band; `lexsis_catalog.reviews_search` with the result-profile words ("dry skin", "curly") for same-profile quotes (`pending` until confirmed); brand-level reviews for the start screen only as a labelled store rating (`references/proof/reviews-sourcing.md`).
4. Proof ledger: taker count from an export (`customer-count`), an authorship line with the named person's approval; guarantee terms for a shade or fit guarantee.
5. `lexsis_brand.context`, `lexsis_brand.brand_kit` (typographic start-screen tokens, voice); `lexsis_brand.navigation` is not needed (nav `none`).
6. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"` for `lifestyle` (start-screen alternate when the ad was a lifestyle frame; scene options such as "morning" or "evening"), `product-shot`, `social-proof`; the ad frame from `lexsis_campaigns` when traffic is paid, for message match. Sequence and checks: `references/assets/asset-sourcing-sequence.md`.
7. `lexsis_cart.get`: the side cart keeps the shopper on results; quiz discount auto-applied (`first-order`, first-time visitors only); cart v2. Then `lexsis_drafts.funnel_create`, `lexsis_capture.validate_funnel`, `lexsis_capture.preview_funnel`; the returned key feeds FunnelRuntime. `lexsis_design.islands`, then `lexsis_design.island_schema` for each island named below.
8. `lexsis_workspace.credits` only when the plan names the typographic start screen as the bold moment with a generated `hero_bg`.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `header` | logo only, not clickable; the only exit is the quiz. | brand logo or text wordmark; without a logo, use the wordmark. | none; a plain HTML header (Navbar carries navigation, and none belongs here). | none. | `lexsis_brand.brand_kit` logo asset. |
| `hero` (start screen) | outcome headline, what they get, time estimate, one Start button, one verified proof line. | `typographic` by default: HTML text on the page background, or on one generated `hero_bg` (ALLOW, landscape plus portrait, quiet zone, only as the plan's bold moment). Alternate `editorial-lifestyle` from library `lifestyle` when the sending ad was a lifestyle frame. Never a packshot before routing, never a generated person. Missing lifestyle frame for a message-matched start: (context, landscape and portrait); alternative: the `hero_bg` generation with its credit cost; typographic ships meanwhile. | none; the Start button is HTML anchoring to the quiz, or the FunnelRuntime click trigger bound to it; concern chips as the first question belong to the funnel. | headline outcome plus time ("Find your shade in 60 seconds"), 8 words; one sentence on what they get (16 words); proof line ledgered or a labelled store rating; authorship only when real; vocabulary per `references/anti-patterns/copy-anti-patterns.md`. | the ad frame from step 6; ledger rows from step 4; credits from step 8. |
| `quiz` | 5 to 8 questions, one per screen, image choice where possible, every answer mapped to a product or collection, skip logic, progress, no open text. | yes for visual questions: each option image from catalog variant media (real shade swatch on skin, fabric, texture) or library `lifestyle` scenes ("morning", "on the go"); CSS colour chips from the catalog hex only when the template's option type is colour and the real swatch appears on results; text options with 48 px targets for use-case and budget questions. Never stock or generated people as "you"; never product photography on question screens. Missing option imagery: (swatch or scene, square, count per question); generation is not feasible for swatches or skin; text options ship meanwhile. View option images at thumbnail size to confirm they are visually distinguishable from each other. | FunnelRuntime inline on the page, started immediately or from the Start button, keyed to the funnel created in step 7 and validated before design; title and subtitle only when the template does not render its own; ceiling 10 questions, and a question that does not change the recommendation is removed before `validate_funnel`. | questions 12 words; options 4 words; "why we ask" 16 words; second person. | template step schema from step 1; option imagery found in steps 2 and 6. |
| `email-capture` | after the last question and before results; skippable; consent un-ticked. | none. | the funnel template's capture step when it has one; otherwise EmailCapture in compact form labelled "Show my results" with a plain "Show my results without email" link beside it; marketing consent is a separate un-ticked HTML checkbox; a hard gate only with the merchant's recorded confirmation. | "we will send these results to you" (12 words) and the skip link in plain words. | lead goal in the brief; the template's capture step. |
| `quiz-results` | personalised header using the answers, a summary of what was learned, the reason for the result. | yes, the first recommended product's identity from catalog media leads the screen; an inline SVG diagram (AM and PM routine, stage) authored in HTML when the result is a routine or stage; never a generated result image (GN4). Without an identity image, keep the recommended product out of the mapping until its media is supplied. | none when the template hands results to page sections keyed by result; the funnel's own results step when the template renders them; `lexsis_capture.preview_funnel` shows which. | the header repeats the shopper's words ("You said your skin feels tight by noon"); summary 3 lines of 18 words; "results", never "diagnosis" without a clinician and disclaimer. | the results step shape from step 1. |
| `product-spotlight` | one card per recommended product (one to three) with image, price, review summary and a "why this matches you" line tied to an answer. | yes, identity per product from catalog media; never stock or generated. Missing media: (identity, square, per product); the product waits out of the results until then. | none (HTML cards) for one to three products; FeaturedCollectionStage when two or three products should share one large stage, quick add off, badges off, no autoplay or entry animation (N10); ProductCarousel is not used (it needs four or more products). Review summary per product by band. | "why this matches you" 18 words per product, each naming a specific answer. | result mapping from step 1; product bands from step 3. |
| `buy-box` | one "Add my set" CTA with the recommended set pre-loaded and trimmable, set price and any saving as arithmetic, quiz discount applied automatically. | component images already shown above; the builder reuses each product's catalog identity image. | two or three products: BundleBuilder with every recommended item pre-selected (per-item remove), the set saving from the ledger; one product: BuyBox with the recommended variant pre-selected through VariantSwatches; any plan option: SubscriptionToggle with one-time default and both prices visible, only when the merchant confirmed the `ask`; one BuyBox per page; never a redirect to a PDP per item. | "Add my set", "Add my routine"; the saving as arithmetic (`references/offers/price-presentation.md` PP10); the discount stated in one line ("10% off applied at checkout, first order only"). | product count per result; offer ledger; `lexsis_cart.get`. |
| `guarantee` | shade or fit guarantee in one line beside the CTA. | none. | none. | "If we miss, we send the right shade free" (12 words), exact terms. | `policy-fact` row. |
| `reviews` (`-same-profile`) | two or three verbatim quotes from reviewers with the same result type. | reviewer photos only from records; avatars real or CSS initials. | none; static verbatim dated cards from confirmed `reviews_search` candidates (RS16); no carousel, three quotes do not need motion. | quote 60 words; the profile label from the record's fields only. | confirmed candidates from step 3. |
| `faq` | on results only: change answers, wrong shade, returns. | none. | none; native `<details>`. | three to five questions; answers 50 words. | guarantee and returns policy rows. |
| `footer` | legal links only. | brand logo. | Footer with links limited to privacy, terms, contact. | the store's. | legal URLs. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images across candidates) | identity per recommended product, variant images and hexes for shade options | swatch on skin for every shade, scene images for lifestyle options | reuse text options with large tap targets for that question; ask the merchant to upload swatches or scenes; CSS chips only beside a real swatch on results; a product without an identity image waits out of the result mapping until the merchant supplies one |
| asset library | `lifestyle` scenes for the start screen and scene options, `social-proof` with rights | a scene per option | ask the merchant to upload; text option meanwhile; never stock people as the shopper |
| generation | one `hero_bg` for the typographic start screen as the bold moment; at most one or two `decorative_element` | products, swatches, skin, people, results, diagrams as raster | never |

Minimal assets (identity per product only): a typographic start screen on the page background, text-option questions, results led by the catalog identity image, the set builder, guarantee, native FAQ; missing swatches and scenes are listed in the plan and draft summary. Generated assets on a quiz funnel: zero or one start-screen backdrop, never more than the house cap of four.

## Above the fold (390px)

Start screen: logo, outcome headline, one sentence on what the shopper gets,
time estimate, the Start button, one verified proof line. Nothing else. Each
question screen: progress indicator, the question, its answer options with
tap targets of 48px or more, a back control. Results screen: the personalised
header, the first recommended product with its "why" line, the set CTA.
Not above the fold anywhere: price before results, an email field before
question one, a countdown, a navigation menu, an offer bar.

## Proof

- Modules: 1 to 2. Start screen: one `customer-count` ("over 800,000 people
  have taken this quiz", export-backed, rounded down) or a `review-summary`
  for the brand's reviews, plus an authorship or `expert-quote` line when the
  person is real and credentialed. Results screen: `review-summary` per
  recommended product; the match rationale is the proof the shopper values
  most.
- In-quiz reassurance ("most people with combination skin also...") counts as
  copy, not proof, and carries no numeral unless ledgered.
- `expert-quote` and `founder-note` need the named person, verifiable
  credential and written approval (`proof-ledger.md`).
- No reviews: the results screen shows the rationale and a `guarantee`
  (shade or fit guarantee) as the proof; nothing review-shaped.

## Offer and CTA

- CTA count: 2 to 3. Start on the entry screen, "Add my set" on results, and
  an optional per-item add that is part of the buy box. Each question screen
  has a Next or answer tap, which is navigation, not a CTA.
- First CTA position: the start screen (section index 0).
- Sticky: forbidden. Question screens are single-purpose; a sticky button on
  results duplicates the buy box.
- CTA copy: "Start the quiz", "Find my shade", "Take the hair test" on entry;
  "Show my results" at the gate; "Add my routine" or "Add my set" on results.
  Never "Submit", "Continue", "Buy Now", "Unlock my results".
- Price reveal: forbidden before results; on results the set price and each
  item price are shown at once, with any set saving as arithmetic
  (`bundle-kit` rules apply to the set).
- Offers that fit: `none`, `bundle` (the recommended set at a set price with
  visible saving), `trial-sample` (a sample of the recommended product as
  the low-risk first step), `first-order` (auto-applied at results, stated in
  the buy box, first-time visitors only). Curlsmith replaced its 10% popup
  with the quiz; Loop uses a quiz discount auto-applied at results (Octane
  AI, above).
- Offers that do not fit: `percent-off` or `fixed-off` as a standalone sale,
  `bogo`, `gwp`, `tiered-volume`, `flash-sale`, `clearance`, `mystery`,
  `bnpl`, `cashback`, `pre-order-price`, `limited-edition`, `referral`,
  `loyalty`, `gift-card`. `bundle-decoy` and `subscribe-save` are `ask` in
  `offer-types.md`: a plan option on results is allowed only with one-time
  selected by default and both prices visible.
- Urgency: none. No timers, no "N people took this today", no stock counts on
  results.
- Preload the set: the recommended items are in the cart-ready state with
  per-item remove; a redirect to a separate PDP for each add costs conversion
  (RevenueHunt, above).
- Follow-up: the results are emailed when an address was given; a segmented
  flow by result type is the merchant's job, not the page's.

## Imagery

- Required jobs: `identity` on the results screen, one per recommended
  product. Recommended: `swatch` or `variation` as answer options (shades on
  skin, fabrics), `in-use` on the start screen, `diagram` for a stage or
  routine visual (AM and PM timeline). Answer images may be swatches or
  lifestyle scenes; product photography stays off the question screens.
- Hero (start screen): `typographic`; alternate `editorial-lifestyle` when
  the ad that sent the traffic was a lifestyle frame. Never a `packshot`
  before routing.
- Minimum images: 1 on entry (optional) plus one identity image per
  recommended product on results.
- Balance: minimal chrome, brand colour, no photography carousel.
- Video: forbidden on question screens; optional on results as a click-to-play
  how-to for the recommended routine.
- Slots the plan creates: none on the question screens beyond swatches;
  identity images on results come from Shopify media, never generated.

## Copy

- Framework: `qualifier-lead` on the start screen (who this is for and what
  they get), a conversational consultation script through the questions (map
  the in-store associate's conversation, Octane AI), `bab` compressed on
  results ("You told us X; this routine gets you Y; here is why").
- Headline: the outcome and the time ("Find your shade in 60 seconds"; "Know
  the root cause of your hair loss"); never the product name; never a
  discount.
- Reading level grade 6 to 8. Questions 12 words or fewer; answer options 4
  words or fewer; "why we ask" lines 16 words; results summary 3 lines of 18
  words; "why this matches you" lines 18 words each.
- Vocabulary: second person throughout; the shopper's own answer words
  repeated on results ("you said your skin feels tight by noon"); "results"
  never "diagnosis" unless a clinician is involved and the disclaimer is
  present. Never "unlock", "reveal", "your perfect match awaits", "hurry".
- Microcopy at the gate: what the email is for ("we will send these results
  to you") and the skip control in plain words.

## Never

- Never ask for email or phone before question one.
- Never exceed 10 questions; never ship a question that does not change the
  recommendation.
- Never show more than three products on results, or more than one results
  page per outcome.
- Never show a sold-out product in results.
- Never show a result without its reason.
- Never show a price, offer bar or discount before the results screen.
- Never render navigation on question screens.
- Never use open text fields.
- Never redirect to a separate PDP for each add; preload the set.
- Never pre-select a subscription plan on results.
- Never render a countdown or a taker count that is not ledgered.
- Never use generic boilerplate across result types; each result type reads
  as written for that answer set.
- Never gate results behind marketing consent that is pre-ticked or required.

## Examples

- Traya, Hair Test entry https://traya.health/pages/hair-quiz : outcome
  headline, concern chips as the first self-selection, stage visuals by
  gender, a footnoted internal-study stat, returning-user CTA variants ("My
  recommended plan", "Buy again"). Avoid its unit-free "10 Mn+" claim.
- Jones Road, Quiz landing https://www.jonesroadbeauty.com/pages/quiz-landing :
  one hub for six product quizzes, each card stating what it recommends and
  how to use it, a human fallback (a selfie emailed to makeup artists) under
  the automated path; the quiz is the brand's top landing page (Octane AI
  case https://www.octaneai.com/case-studies/jones-road-beauty ).
- Curlsmith, Curl ID (case) https://www.octaneai.com/case-studies/curlsmith :
  the quiz replaced the discount popup, 89% completion, education-first
  results followed by the routine.

## Checklist

```json
{
  "page_type": "quiz-funnel",
  "aliases": ["product finder", "shade finder", "routine builder", "assessment", "recommendation quiz", "quiz results"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["problem-aware", "solution-aware"],
  "traffic": ["meta", "tiktok", "email"],
  "sections": { "min": 4, "max": 7 },
  "mandatory_sections": ["header", "hero", "quiz", "quiz-results", "buy-box", "footer"],
  "recommended_sections": ["product-spotlight", "guarantee", "email-capture"],
  "forbidden_sections": ["announcement", "countdown", "stock-indicator", "product-grid", "comparison", "problem", "agitation", "offer-bridge", "final-offer", "sticky-cta", "hook", "cross-sell"],
  "nav": "none",
  "price_above_fold": "forbidden",
  "cta": { "min": 2, "max": 3, "first_after_section": 0, "sticky": "forbidden", "copy_pattern": "start-quiz" },
  "proof": { "min_modules": 1, "max_modules": 2, "required_kinds": ["review-summary"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked", "stock-count"] },
  "imagery": { "required_jobs": ["identity"], "hero": "typographic", "video": "forbidden", "min_images": 1 },
  "copy_framework": ["qualifier-lead", "bab"],
  "offer_compat": { "allowed": ["none", "bundle", "trial-sample", "first-order"], "forbidden": ["percent-off", "fixed-off", "bogo", "gwp", "tiered-volume", "flash-sale", "clearance", "mystery", "bnpl", "cashback", "pre-order-price", "limited-edition", "referral", "loyalty", "gift-card"] },
  "urgency": "none"
}
```

`price_above_fold: forbidden` applies to the start and question screens; the
results screen shows price at once. `imagery.required_jobs` `identity` is
required on the results screen only (footnote g in
`references/assets/image-jobs-by-page-type.md`). `imagery.video: forbidden`
applies to question screens; a click-to-play routine video on results is an
allowed exception recorded in the plan. `proof.required_kinds`
`review-summary` falls to `guarantee` when no reviews exist; never fabricate.
`cta.copy_pattern` `start-quiz` names the entry CTA; the results CTA follows
the `add-to-cart` shape ("Add my set").

## Sources

- RevenueHunt, how to build a successful quiz (results page count, question
  rules) https://docs.revenuehunt.com/customer-success/how-to-build-successful-quiz/ ;
  recommend bundles and kits https://docs.revenuehunt.com/customer-success/recommend-bundles-kits/
- Octane AI cases: Jones Road https://www.octaneai.com/case-studies/jones-road-beauty ;
  Curlsmith https://www.octaneai.com/case-studies/curlsmith
- Uplup, product recommendation quiz guide https://uplup.com/blog/how-to-make-a-product-recommendation-quiz
- Convert.com, AI product quiz blueprint https://www.convert.com/blog/growth-marketing/high-converting-ai-product-quiz-blueprint/
- Lantern results page setup https://help.trylantern.com/en/articles/10307748-set-up-your-results-page ;
  Opinion Stage quiz results pages https://www.opinionstage.com/blog/quiz-results-page/
- Landra DTC landing page benchmarks 2026 https://www.getlandra.com/blog/dtc-landing-page-conversion-benchmarks-2026
- Hims message-matched quiz funnel (ConvertFlow) https://www.convertflow.com/campaigns/hims-full-funnel-marketing-examples-templates
- Sibling references: `references/page-types/bundle-kit.md` (set rules on results),
  `references/offers/offer-types.md` (bundle, first-order, trial-sample),
  `references/proof/proof-ledger.md`, `references/assets/image-jobs-by-page-type.md`,
  `references/anti-patterns/dark-patterns.md` (forced action, basket sneaking),
  `references/consumer-behavior-cro.md` (commitment and ownership, choice reduction)
