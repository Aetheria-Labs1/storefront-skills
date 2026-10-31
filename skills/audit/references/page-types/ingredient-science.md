# Ingredient and science page

The page explains why the product works: mechanism, what is inside, the
studies behind the claims, and who certified what. The visitor is a
solution-aware or product-aware researcher who arrived from a PDP link, a
"does X work" or "X ingredients" search, or a retargeting ad after a doubtful
first visit. Their job is to read, verify, and then click through to the
product or subscription. The page sells by substantiation, not by offer, and
its headline metric is assisted conversion (view then buy) and click-through
to the buy point.

## Identify it

- The brief names ingredients, materials, actives, strains, "clinical",
  "studies", "how it works", "what's inside", "formulation", or asks to
  justify a premium price against a cheaper alternative.
- Category is supplements, skincare actives, functional food, textiles with a
  technical fibre, or hardware with a proprietary mechanism.
- Near neighbours: `brand-story-founder` sells belief and people; choose
  science when the brief names ingredients or studies. `comparison-us-vs-them`
  ranks against a named rival; a science page compares only against the
  generic category. `pdp` is the buy point; the science page is the depth
  layer linked from it. `advertorial` hides the product until late; here the
  product is named in the hero.

## Variants

- Supplement or functional food: facts panel, dose per serving, strain or
  form, third-party testing, structure/function wording, disclaimer.
- Skincare or haircare: full INCI, active percentages where disclosed,
  consumer-perception and instrumental studies, tolerance testing.
- Material or hardware: material spec, test method (ASTM, ISO, lab), results
  against the category baseline, warranty as evidence.

## Anatomy

1. `hero` mandatory: product name plus a plain-language outcome with footnote
   markers that jump to the studies; one editorial ingredient or material
   image; one verifiable trust fact (certification with issuer, or "12-week
   study, 105 adults") with an in-page link.
2. `mechanism` mandatory: how it works in three to five plain-language steps
   with one diagram; each step names the ingredient or component doing the
   work.
3. `ingredients` or `materials` mandatory: one card per hero ingredient or
   material with what it is, dose or spec as shipped, why it is there, and a
   citation marker; the `label-or-facts-panel` image sits beside the cards
   for regulated consumables.
4. `science` mandatory: a table of studies with design, n, duration,
   population, endpoint, result, and a column stating whether the study
   tested this product or the ingredient at this dose; when no product study
   exists, ingredient-level literature is shown and labelled as such.
5. `certifications` conditional: the merchant holds a certificate with
   issuer, number, scope and date (`references/proof/trust-badges-certifications.md`).
6. `expert-endorsement` recommended: one verbatim quote with name,
   credential line, registration number where the profession has one, and a
   connection label; never a logo in place of the person.
7. `sourcing` recommended: where and how it is made, testing lab standard
   (ISO 17025), certificate of analysis per batch, formulation change history.
8. `usage` or `routine` recommended: how to take or apply, when results are
   typically noticed, what changes nothing.
9. `faq` mandatory: objection-phrased questions ("Is this the same dose as in
   the study?", "Is it FDA approved?") answered in the first sentence.
10. `buy-box` or `closing-cta` mandatory: `buy-box` when this page is the
    conversion point for a single SKU; otherwise one `closing-cta` to the PDP
    or plan selector.
11. `disclaimer` conditional: regulated claims (US supplement
    structure/function, India FSSAI or AYUSH wording, cosmetic claims);
    rendered in the same viewport as the first regulated claim and again at
    the end.
12. `science-references` conditional: studies are cited; full reference list
    with journal, year, volume and link (satisfies `science`).

When the count would exceed ten, fold `science-references` into the `science`
section as footnotes and the end-of-page disclaimer into `legal`.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.get` for the product this page substantiates: which jobs the media already covers (`identity` at position one, `ingredient-or-material` flat lay, `label-or-facts-panel` at 1600 px or more, `sequence` routine shots, real video), mapped with the type's row in `references/assets/image-jobs-by-page-type.md`; variant axes and whether the page targets one SKU; price and compare-at (compare-at needs a ledger row); selling plans (gates `subscribe-save` in the buy box). Inventory is read but never shown as a stock statement.
2. `lexsis_catalog.reviews_status` for the count band; `lexsis_catalog.reviews` only at 5 or more, for a `review-summary` with average and count.
3. `lexsis_brand.context` and `lexsis_brand.brand_kit` for `theme_id`, palette hexes (any generation call), voice and banned phrases; `lexsis_brand.navigation` for the full header and footer and the buy-point URL.
4. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`: `flat-lay`, `product-shot`, `hero`, `logo` (issuer marks only), then semantic "<ingredient> macro", "facts panel", "lab", "farm"; view candidates with `lexsis_assets.view`. Inventory the result by job.
5. Merchant-confirmed facts as proof ledger rows before any section is chosen: each study (document or URL, design, n, duration, population, endpoint, whether it tested this product at this dose); each certification (issuer, number, scope, date); the expert (name, credential, registration number, written approval, connection); lab standard and certificate of analysis; formulation change dates; the regulated-claim wording for the market. Substantiation and wording rules: `references/proof/before-after-and-claims.md`, `references/proof/trust-badges-certifications.md`. A claim with no row is not written.
6. `lexsis_design.islands` for the active catalog, then `lexsis_design.island_schema` for each island named below; deprecated entries take their replacement per `references/workflows/island-selection-workflow.md`.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `hero` | name the product, state the outcome in the shopper's words with footnote markers, show the ingredient or material, give one trust line. | yes. Job `ingredient-or-material` as an `editorial-lifestyle` hero; `identity` packshot is the alternate. Catalog media, then library tags `flat-lay` and `hero`, then semantic "<ingredient> macro", then merchant upload; view with `lexsis_assets.view` and confirm the macro shows the named ingredient, the portrait crop keeps it and a quiet area holds the headline. Gap: ask the merchant (job, aspect, count); upload, or `hero_bg` as a backdrop behind HTML text when the hero is the plan's bold moment; the ingredient itself is never generated (GN11); the typographic hero only if the merchant chooses it. No-go: a person, a before/after pair, clinical props, stock raw material presented as the merchant's sourcing. | `none` for the hero (one static `<picture>`, portrait crop for mobile). Header `SiteHeader` (announcement plus nav) or `Navbar` (nav only) from `lexsis_brand.navigation`. | outcome plus mechanism noun, footnoted; headline 12 words, body 40 words; the trust line is one sentence that links down the page. | the job inventory from reads 1 and 4; the ledger row behind the trust line. |
| `mechanism` | three to five plain-language steps, each naming the ingredient or component doing the work, beside one diagram. | yes. Job `diagram`: merchant diagram via `lexsis_asset_import.import` (view with `lexsis_assets.view`: labels legible at 390px, no baked-in numbers), then library semantic "mechanism diagram", then an authored inline SVG with labels and numbers as SVG `<text>` or HTML. Raster generation is never used for a diagram (GN6); the SVG is the offer when nothing exists. No-go: icon tiles in place of the diagram, stock lab imagery, a step list on a colour band. | `none` for the diagram. `VideoPlayer` only when a real captioned explainer under 60 seconds exists in catalog media or the library. The first CTA of the page sits after this section. | 30 words per step; step title is a verb plus the ingredient. | whether a merchant diagram exists; otherwise the ledger's mechanism steps drive the SVG. |
| `ingredients` or `materials` | one card per hero ingredient or material with what it is, dose or spec as shipped, why it is there, and a citation marker; the facts panel sits beside the cards for regulated consumables. | yes. Jobs `ingredient-or-material` per card and `label-or-facts-panel` when the product carries a label. Catalog media, then library tags `flat-lay` and `product-shot`, then semantic "<ingredient> close-up", then merchant upload, then supplier photo with a written licence, then licensed stock raw material as a plain macro never captioned as the merchant's sourcing. View each macro with `lexsis_assets.view` and confirm it shows the ingredient named beside it; view the label photo at 390px and confirm the panel text is legible. Gap: ask the merchant (which ingredients lack a macro, square, count); upload only, since the ingredient is never generated (GN11); `texture_fill` may back the card object (N8) but never stands in for the ingredient. Facts panel as HTML text first with the real label photo zoomable beside it. No-go: an emoji or icon per ingredient, cards falling back to colour tiles, fillers before actives. | `IngredientExplorer` when three or more ingredients carry a description and a dose (inputs: ingredient count, image coverage, dose data); one or two ingredients or a material spec table are plain HTML; grouping by concern or actives vs full list uses CSS-only tabs with radio inputs or grouped `<details>`. Resolve layout and props from `lexsis_design.island_schema`. | 60 words per card in FAB order with the citation marker on the benefit; doses exactly as printed on the label. | ingredient count and per-ingredient image coverage from read 4; doses from the label in read 1. |
| `science` | the studies table with design, n, duration, population, endpoint, result and a "tested this product at this dose?" column. | no by default; the table is the object. A `result-or-context` image only from a `verified` ledger row, never a before/after pair on this type (`references/proof/before-after-and-claims.md`); study figures only with the publisher's licence. No-go: charts with baked-in text, stock lab photos, generated clinical imagery (GN4, GN6). | `none` (HTML `<table>`, one row per study, the disclaimer in the same viewport as the first regulated claim). | 40 words per row plus the numbers copied exactly; design named; "was associated with" not "proven". | the `test-data` ledger rows. With no product or ingredient study the section says so in one sentence and links the literature; it never implies a trial. |
| `certifications` (conditional) | real marks with issuer wording. | yes, issuer artwork only: library tag `logo`, then `lexsis_asset_import.import` of the issuer's file, then a monochrome SVG redraw the issuer permits; view each mark with `lexsis_assets.view` against its ledger row and confirm it is the real issuer's artwork. Gap: ask the merchant for the issuer file; never generated (GN5, TB10). No-go: a mark without issuer text and number, the ISO logo, "FDA registered facility", a badge row repeated per section. | `none` (one row, three to five marks, one height, issuer text beside each, per `references/proof/trust-badges-certifications.md`). | the issuer's permitted phrase plus the licence number. | `certification` ledger rows holding issuer, number, scope and current date; a row missing any of the four does not render. |
| `expert-endorsement` (recommended) | one verbatim quote from a named, credentialed person. | yes or none. A real photo of the named expert with consent (merchant upload or library, viewed with `lexsis_assets.view` to confirm it is the named person), or the quote runs as text with the credential line and no photo. Gap: ask the merchant for the photo; never stock, never generated (GN3), never a logo in place of the person (`references/proof/before-after-and-claims.md`, endorsements table). | `none` (a `<blockquote>` with name, credential, registration number, date and connection label). | verbatim; nothing paraphrased. | an `expert-quote` ledger row with written approval; without a row the merchant is told what is needed and the section waits. |
| `sourcing` (recommended) | where and how it is made, the lab standard, the certificate of analysis, formulation change history. | yes. Job `founder-or-team`, or a facility, farm or lab photo (`context`, `sequence`): library tag `lifestyle`, then semantic "facility", "lab", "farm", then merchant upload; view with `lexsis_assets.view` and confirm a real facility or process with lighting that matches the neighbouring slots. Gap: ask the merchant for facility or process photos; stock is never captioned as their facility and generation is never used; merging the facts into `science` as text is the merchant's call. No-go: a stock laboratory, a generated factory, a world map as the only visual. | `none`. | 80 words; the COA is a link; the change history is a dated list. | facility photo coverage from read 4 and the merchant's answer. |
| `usage` or `routine` (recommended) | how to take or apply, when results are typically noticed, what changes nothing. | yes. Job `sequence` (three to five real step photos) or one captioned how-to video: catalog media, then library tag `lifestyle` and semantic "how to use <product>", then merchant upload; view each step with `lexsis_assets.view` and confirm the action is legible at 390px. Gap: ask the merchant for step photos (count, square or 4:5); never generated; folding the steps into one `faq` answer is the merchant's call. No icon tiles. | `VideoPlayer` when a real how-to video exists; otherwise `none`. | one sentence per step; the "typically noticed" line cites its study row. | `sequence` coverage from read 4 and the merchant's answer. |
| `faq` | objection-phrased questions answered in the first sentence. | no. | `none`; native `<details>` and `<summary>`, all collapsed. | five to eight questions, 60 words per answer; "Is this the same dose as in the study?" is mandatory when a study is cited. | the claims in `science` and the merchant's stated objections. |
| `buy-box` or `closing-cta` | the conversion point, or the one link to it. | yes. Job `identity` from catalog media position one, viewed with `lexsis_assets.view` against the variant sold (whole product, clean background matching the gallery). Gap: ask the merchant for the packshot; never generated (GN1). No-go: a lifestyle image in place of the packshot. | `BuyBox` when this page sells a single SKU (inputs: variant count, selling plans from read 1, whether the page has its own icon set). | next-step verb, or "Add to cart" with the buy box; price stated once, per-day framing only when arithmetically true. | the brief (is this page the conversion point), variant count and selling plans from read 1. |
| `disclaimer` (conditional) | the regulated wording beside the first regulated claim and again at the end. | no. Island: `none`. | Use the shared procedure. | the regulator's text verbatim at 12 px or larger. | market and claim type from read 5. |
| `science-references` (conditional) | full citations with journal, year, volume and link. | no. Island: `none`. | Use the shared procedure. | one reference per line; folds into `science` as footnotes when the section count would pass ten. | the `test-data` ledger rows. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` packshot, `label-or-facts-panel` photo, sometimes one `ingredient-or-material` flat lay or a routine shot | per-ingredient macros, `diagram`, facility photos, expert photo | reuse the flat lay across cards where honest; ask the merchant to upload macros (supplier photo with licence is acceptable); author the diagram as inline SVG; skip a section only on the merchant's call |
| asset library | prior ingredient macros (`flat-lay`), issuer marks (`logo`), an editorial hero | video, sequence steps | ask the merchant to upload; no generated video; merge steps into `faq` only if they choose |
| generation | backdrops, textures, composites only (`hero_bg` behind the bold-moment hero, `texture_fill` inside a card object) | product, ingredients, people, results, labels, diagrams, badges, text | never |

With minimal assets the page is a typographic hero (merchant's choice), an SVG mechanism diagram, the facts panel as HTML text with the label photo beside it, text ingredient cards with their gaps listed for the merchant, the studies table, native `<details>` FAQs and a packshot at the buy box. Generated assets on this type are usually zero and never more than one backdrop or texture; the house cap is four per page. Every asset placed, generated ones included, was opened with `lexsis_assets.view` and passed the fit review before use.

## Above the fold (390px)

In order: full header; product name and the outcome statement in the
shopper's words with footnote markers; one sentence naming the mechanism;
one verifiable trust line (issuer-named certification or a study line with
n) that links down the page; the hero image showing the ingredient or
material, not a person. A single text link to the buy point is allowed in
the header only.

Must not appear: a price as the lead, any discount, a countdown, star glyphs
without a count, "clinically proven" without the study link, a before/after
pair, a benefit list longer than three items.

## Proof

Two to four modules. `test-data` is required: the studies table is the
spine of the page and every claim in the hero traces to a row in it.
Recommended second and third modules: `certification` with issuer wording
from `references/proof/trust-badges-certifications.md`, `expert-quote` with
credential line, and `review-summary` with average and count from
`lexsis_catalog.reviews`. Proof sits beside the claim it supports: a study
result under the benefit it proves, a certification next to the quality
statement, not pooled at the end.

Minimum evidence per kind: a study row needs a document or URL with method,
sample size, duration and endpoint; numbers are copied exactly and the
disclaimer for structure/function claims sits in the same viewport
(`references/proof/before-after-and-claims.md` holds the claims
substantiation table). A certification needs issuer, certificate or licence
number, scope and current date. An expert quote needs a named person, a
verifiable credential, written approval and a disclosed material connection
(LAW, 16 CFR 255.3, https://www.law.cornell.edu/cfr/text/16/255.3).

When the store has none: show the facts panel and full ingredient list with
supplier names as product evidence, the manufacturing standard with the
certifier, and a signed founder note on why the formula is what it is
(`references/proof/reviews-sourcing.md`, Tier 5 substitutes). A science page
with no studies says so plainly and links to ingredient literature; it never
implies a trial that did not happen.

Wording rules (LAW):

- "Clinically proven" and "clinically tested" require a study whose
  endpoints and dose match the claim and the product as sold; FTC health
  products guidance: competent and reliable scientific evidence
  (https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance).
- Never "FDA approved" for a supplement, cosmetic or food; FDA does not
  approve them, and "made in an FDA registered facility" has drawn warning
  letters as misbranding
  (https://www.fda.gov/consumers/consumer-updates/it-really-fda-approved).
- India: write "FSSAI Lic. No. [14 digits]" with the logo, never "FSSAI
  approved" or "FSSAI certified"; claims follow the FSSAI Advertising and
  Claims Regulations 2018 and disease claims are out of scope
  (https://www.fssai.gov.in/upload/uploadfiles/files/Comp_Labelling.pdf,
  https://www.fssai.gov.in/upload/uploadfiles/files/Compendium_Advertising_Claims_Regulations_04_03_2021.pdf).
- EU cosmetics: claims meet the six common criteria of Regulation 655/2013
  (legal compliance, truthfulness, evidential support, honesty, fairness,
  informed decision-making)
  (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0655).
- Disclose formulation changes next to reviews or studies that predate them
  (OPERATOR, AG1 labels reviews before a reformulation date,
  https://drinkag1.com/ag1-ingredients).

Vertical depth: `references/vertical-supplements.md` (Clinical Proof
Section, FDA Disclaimer wording), `references/vertical-beauty.md`
(Ingredient Section Pattern, Clinical Stats).

## Offer and CTA

One or two CTAs. The first appears after the mechanism section, never in
the hero body; the second is the `buy-box` or `closing-cta` at the end.
Sticky CTA optional, and only when the page carries a `buy-box`. Copy
pattern: next-step ("See the full formula", "Start the routine", "View the
product"); when the page has a buy box the button reads "Add to cart".

Price reveal: price is optional above the fold and belongs in the buy box or
closing CTA, stated once with unit or per-day framing where accurate
(`references/offers/price-presentation.md`). Offers that fit: `none`,
`free-shipping`; `subscribe-save`, `bundle`, `first-order` and
`trial-sample` only when the merchant confirms them and the offer renders in
the closing section, not beside the evidence. Offers that do not fit:
`percent-off`, `fixed-off`, `bogo`, `gwp`, `flash-sale`, `clearance`,
`mystery`. No countdown, no stock statement. A discount beside a study
reads as an advertisement and undercuts the page's only asset.

## Imagery

Required jobs: `identity` (packshot at the buy point), `ingredient-or-material`
(real ingredient or material flat lay, no clinical props), `diagram`
(mechanism, numbers and labels in HTML not baked into the image).
Conditional: `label-or-facts-panel` for regulated consumables and any
product with an INCI or nutrition label; `sequence` when usage has steps;
`founder-or-team` or lab photo for the sourcing section. Minimum four images
(HEURISTIC, `references/assets/image-jobs-by-page-type.md`).

Hero treatment: `editorial-lifestyle` of the ingredient or material; a
`typographic` hero is the fallback. Never a `before-after` hero; study
imagery renders inside `science` with the protocol beside it. Studio to
lifestyle ratio leans studio: macro and flat lay carry information here.
Video optional; a mechanism explainer under 60 seconds with captions and a
pause control is the only good use. Slots the plan must create: hero
ingredient image, one diagram, one tile per hero ingredient or material,
facts-panel photo when applicable, packshot at the buy point.

## Copy

Framework: FAB per ingredient or material card (feature, advantage, benefit
with a citation marker) inside a 4Ps spine (promise in the hero, picture in
the mechanism, proof in the studies, push at the buy point). Headline
pattern: outcome in the shopper's words plus the mechanism noun, footnoted;
never a superlative. Reading level grade 6 to 8 with every technical term
translated in the same sentence; ecommerce pages written at grade 5 to 7
converted 5.6% against 1.5% for professional-level copy (OPERATOR, Unbounce,
https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/).

Length ceilings: hero 40 words; mechanism 30 words per step; ingredient card
60 words; study row 40 words plus the numbers; FAQ answer 60 words with the
answer in the first sentence; whole page 800 to 1,500 words. Vocabulary:
"supports", "was associated with", "in a study of n" instead of "cures",
"proven", "guaranteed results"; dose units as on the label; study design
named (randomised, placebo-controlled, single-arm, ex vivo). Copy rules and
the AI-tell blacklist live in `references/copy/copy-frameworks.md`.

## Never

- Never state a study result without design, n, duration and whether it
  tested this product at this dose.
- Never cite an ingredient study at a dose the product does not contain.
- Never write "FDA approved", "FDA registered", "FSSAI approved" or "GMP
  certified" without a named certifier.
- Never show a certification mark without issuer text and a certificate or
  licence number in the ledger.
- Never render an expert as a logo, a stock photo or an unnamed "doctors
  recommend".
- Never place a before/after pair on this page.
- Never lead the fold with price, discount or a countdown.
- Never leave the page without a CTA to the buy point; a dead-end library
  is the most common failure.
- Never use jargon without a plain-language translation in the same
  sentence.
- Never hide the structure/function or cosmetic disclaimer in the footer
  alone.

## Examples

- AG1 ingredients page, https://drinkag1.com/ag1-ingredients: outcome
  checklist with footnote markers, ingredient categories one takeaway each,
  third-party certification named, research footnotes that disclose design
  and n, reviews labelled by formulation date.
- Seed DS-01, https://seed.com/daily-synbiotic: two-capsule mechanism
  diagram, strain table with counts, "tested for" badge grid, "us vs other
  probiotics" table with honest competitor cells, "Do I have to subscribe?
  Yes." in the FAQ.
- Ritual HyaCera study write-up,
  https://ritual.com/blogs/life-habits/hyacera-skincare-routine: 12-week
  randomised controlled trial described with population and endpoints, full
  journal citations at the end, one link to the product.

## Checklist

```json
{
  "page_type": "ingredient-science",
  "aliases": ["ingredients page", "science page", "how it works", "clinical results page", "formulation page", "materials page"],
  "funnel_stage": ["mof"],
  "awareness": ["solution-aware", "product-aware"],
  "traffic": ["organic", "google-search", "direct", "retargeting"],
  "sections": { "min": 7, "max": 10 },
  "mandatory_sections": ["hero", "mechanism", ["ingredients", "materials"], "science", "faq", ["buy-box", "closing-cta"]],
  "recommended_sections": ["expert-endorsement", "sourcing", ["usage", "routine"], "certifications", "review-summary", "disclaimer"],
  "forbidden_sections": ["before-after", "countdown", "stock-indicator", "offer", "final-offer", "savings-math", "us-vs-them"],
  "nav": "full",
  "price_above_fold": "optional",
  "cta": { "min": 1, "max": 2, "first_after_section": 2, "sticky": "optional", "copy_pattern": "next-step" },
  "proof": { "min_modules": 2, "max_modules": 4, "required_kinds": ["test-data"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked", "stock-count"] },
  "imagery": { "required_jobs": ["identity", "ingredient-or-material", "diagram"], "hero": "editorial-lifestyle", "video": "optional", "min_images": 4 },
  "copy_framework": ["fab", "4ps"],
  "offer_compat": { "allowed": ["none", "free-shipping", "subscribe-save", "bundle", "first-order", "trial-sample"], "forbidden": ["percent-off", "fixed-off", "bogo", "gwp", "flash-sale", "clearance", "mystery"] },
  "urgency": "none"
}
```

## Sources

- FTC Health Products Compliance Guidance: https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance
- FTC Endorsement Guides, expert endorsements, 16 CFR 255.3: https://www.law.cornell.edu/cfr/text/16/255.3
- FDA, "Is it really FDA approved?": https://www.fda.gov/consumers/consumer-updates/it-really-fda-approved
- FSSAI labelling compendium: https://www.fssai.gov.in/upload/uploadfiles/files/Comp_Labelling.pdf
- FSSAI Advertising and Claims Regulations compendium: https://www.fssai.gov.in/upload/uploadfiles/files/Compendium_Advertising_Claims_Regulations_04_03_2021.pdf
- EU Regulation 655/2013, common criteria for cosmetic claims: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0655
- Unbounce ecommerce conversion benchmark (reading level): https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/
- AG1 ingredients and research: https://drinkag1.com/ag1-ingredients ; https://drinkag1.com/en-eu/learn/research/scientific-research
- Seed DS-01: https://seed.com/daily-synbiotic
- Ritual HyaCera study write-up: https://ritual.com/blogs/life-habits/hyacera-skincare-routine
- Research notes: internal research audit (2026-09-10) block 18; internal research audit (2026-09-10) sections 6, 9, 13; internal research audit (2026-09-10) Part D pattern 9.
