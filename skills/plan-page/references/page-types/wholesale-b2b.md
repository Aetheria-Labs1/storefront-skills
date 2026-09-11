# Wholesale and B2B page

The page recruits retailers, distributors and corporate buyers who order in
volume for resale or internal use. The visitor is a professional buyer who
knows the product category and is judging margin, minimums, lead time,
terms and support. Their job is to read the terms, download the line sheet,
and submit an inquiry or application. The page speaks in retailer outcomes,
shows no consumer promotion, and is measured by qualified applications,
approval to first order, and opening order value.

## Identify it

- The brief says "wholesale", "B2B", "trade", "stockists", "retailers",
  "bulk", "corporate orders", "MOQ", "line sheet", "distributor".
- Near neighbours: `bundle-kit` sells a set to a consumer; volume pricing
  for a business is this type. `lead-capture-giveaway` collects a contact
  for an incentive; here the form is an application with business fields
  and no incentive. `collection-landing` browses products at retail; a line
  overview here carries case packs and trade terms. Corporate gifting with
  a consumer checkout is `seasonal-gifting`, not this type, unless volume
  terms and an inquiry form drive the page.

## Variants

- Open application: terms and tier structure public, unit prices on
  approval, application form on the page.
- Gated portal: public page carries who it is for, terms structure and the
  form; pricing and ordering live behind a B2B login after approval.
- Marketplace hand-off: the page explains terms and links to the brand's
  Faire or similar listing as an alternative ordering path.

## Anatomy

1. `hero` mandatory: who it is for ("For independent grocers and specialty
   retailers in India"), one retailer outcome (margin band, sell-through,
   support), the CTA "Apply for a wholesale account", and a "Log in" text
   link for existing accounts.
2. `qualifier` recommended: who qualifies and who does not (channels,
   regions, online-only resellers, exclusivity policy).
3. `pricing-terms` mandatory: one table with MOQ (units or currency), tier
   structure or margin band, lead time from order to dispatch, payment
   terms (prepaid, net 30, net 60), freight and shipping terms, damages and
   returns on opening orders, exclusivity; unit prices may read "on
   approval" but the structure is always public (satisfies `pricing`).
4. `product-grid-line` recommended: line overview with case pack, carton
   dimensions and weight, shelf life or warranty, barcode availability; the
   line sheet download link lives here (satisfies `product-grid`).
5. `case-study-stockists` recommended: trade proof: named stockists with
   consent and a link, one verbatim retailer quote with name and store,
   sell-through figures with the period; stockist count from an export
   (satisfies `case-study`).
6. `certifications` conditional: the merchant holds food safety, textile,
   safety or origin certificates; issuer wording per
   `references/proof/trust-badges-certifications.md`.
7. `features-trade-support` recommended: marketing assets, displays and
   shelf talkers, staff training, sampling, reorder cadence, account
   manager (satisfies `features`).
8. `email-capture-inquiry` mandatory: the inquiry or application form, six
   to eight fields across two steps with a progress indicator: business
   name, contact name and email or phone, business type and channel,
   country and region, tax identifier (GSTIN in India, VAT number in the EU
   and UK, EIN plus resale certificate upload in the US), store website or
   address, expected monthly volume; a B2B contact consent line; schema
   from `lexsis_capture.form_schemas` (satisfies `email-capture`).
9. `how-it-works` mandatory: what happens next in three steps: review time
   in business days, approval and account with trade pricing, first order
   and reorder; the alternative marketplace path if any.
10. `faq` recommended: MOQ, exclusivity, payment terms, shipping, damages,
    samples, price changes.

Five to eight sections between chrome; the plan chooses among the
recommended sections by what the merchant can verify.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. `lexsis_catalog.list` for the line, then `lexsis_catalog.get` per SKU: `identity` at position one (viewed, one background across the set), `packaging` case or carton with the pack count visible, `detail`, `scale`, `swatch` per colourway (CSS chips from the catalog hex are fine), `label-or-facts-panel`; variant count; barcodes and SKU codes for the line sheet (`references/assets/image-jobs-by-page-type.md`). Retail prices are read but never shown without wholesale context.
2. Merchant-confirmed trade terms as offer ledger rows: MOQ, tier breaks (at most four, per-unit price or "on approval"), lead time, payment terms, freight, damages and returns on opening orders, exclusivity, tax basis, review time in business days, sample policy, price-hold period, the marketplace listing URL if any; "free" freight claims follow `references/anti-patterns/dark-patterns.md` (DP12) and the FTC proximity rule cited in this file.
3. Trade proof as proof ledger rows: stockists with written consent and a link; one verbatim retailer quote with name and store; sell-through and door count from exports with the period; certifications with issuer, number, scope, date (`references/proof/trust-badges-certifications.md`).
4. `lexsis_brand.context` and `lexsis_brand.brand_kit` for `theme_id`, logo, palette hexes and voice; `lexsis_brand.navigation` only for the B2B log-in URL (nav is `minimal`).
5. `lexsis_capture.form_schemas` for the application schema: six to eight fields over two steps, the tax identifier conditional on country (GSTIN, VAT number, EIN plus a resale certificate upload), the B2B contact consent line. If the schema has no file upload, the certificate is requested by email after approval and the form says so.
6. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`: `product-shot` and `flat-lay` for the line, `logo` for consented stockist marks, `lifestyle` with semantic "in store shelf <brand>" for a real shelf or display shot; view with `lexsis_assets.view`.
7. `lexsis_asset_import.import` for the line sheet PDF (file or URL) so the download link points at a library asset id, and for stockist logos or shelf photos supplied with permission.
8. `lexsis_design.islands`, then `lexsis_design.island_schema` for `FunnelRuntime`; the logo row and any region tabs are native HTML per `references/workflows/island-selection-workflow.md`.

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `hero` | who the page is for, one retailer outcome, "Apply for a wholesale account", a "Log in" text link, a packshot of the line or case. | yes. Job `identity` as a `packshot` hero showing several SKUs in one frame, or `packaging` (case with pack count visible); a `grid` of the line is the alternate. Catalog media (group shot or case), then library tag `product-shot` or `flat-lay`, then merchant upload, then supplier packshot of the exact SKU with a licence; view with `lexsis_assets.view` and confirm every SKU in frame is in the line, the pack count is legible on a case and a quiet area holds the headline (a composite is viewed beside its source cut-outs). Gap: ask the merchant (group shot or case photo, landscape plus portrait); upload, or `product_composite` placing real cut-outs on a plain generated surface (ALLOW, alt naming the products), or `hero_bg` under HTML text; never a generated carton, store or product. No-go: models outside a store, a stock warehouse or handshake, a discount pill inside the frame. | `none` for the hero. Header `SiteHeader` with the cart hidden and "Log in" as the nav CTA to the B2B account URL from read 4. | audience plus outcome in 14 words, numbers only from a ledger row; one line naming the CTA's destination. | line media coverage from read 1 (group shot or case photo); the margin band row from read 2. |
| `qualifier` (recommended) | who qualifies and who does not. | no. Island: `none`. | Use the shared procedure. | channels, regions, online-only policy, exclusivity; 80 words. | the merchant's channel policy from read 2. |
| `pricing-terms` | the terms table: MOQ, tiers or margin band, lead time, payment, freight, damages and returns, exclusivity, tax basis. | no; the table is the object. | `none` (HTML `<table>`). Terms that differ by region sit in CSS-only tabs with radio inputs or stacked tables under region headings. | tax basis on the price line; at most four tiers with the per-unit price at each; "on approval" allowed for unit prices, never for the structure. | the offer ledger rows from read 2; a missing MOQ, lead time or payment term blocks the page. |
| `product-grid-line` (recommended) | line overview with case pack, carton dimensions and weight, shelf life or warranty, barcode availability; the line sheet download lives here. | yes. Jobs `identity` per SKU card (uniform background, crop and orientation), `packaging` for the carton, `scale` for carton dimensions, `swatch` per colourway, `label-or-facts-panel` where the buyer must see the label. Catalog media, then library tag `product-shot`, then merchant upload, then supplier packshot with a licence; view each card image with `lexsis_assets.view` and confirm the exact SKU, a uniform background and crop across the grid, and a label legible at card width. Gap: list the SKUs without an image to the merchant (count, square) and ask for uploads; never generated, and `product_composite` never fills an `identity` slot; leaving a SKU out or moving the line sheet link to `pricing-terms` is the merchant's call. No-go: placeholder tiles, a retail price on a card, hotlinked supplier images. | `none` (static grid composition per `references/product-grid.md`; retail add-to-cart islands do not apply before approval). The line sheet is an `<a>` to the imported PDF from read 7 with its size and date. | 30 words per card: case pack, carton dims and weight, shelf life or warranty, barcode. | SKU count and per-SKU image coverage from read 1; the line sheet asset id from read 7. |
| `case-study-stockists` (recommended) | named stockists, one retailer quote, sell-through with the period, a dated stockist count. | yes. Stockist logos only as `case-study` rows: monochrome, one height, each an `<a>` to the stockist's store or listing, from library tag `logo` or a retailer-supplied file imported in read 7 with consent on record, each viewed with `lexsis_assets.view` against its ledger row to confirm the real retailer's mark; a static HTML row, never a scrolling wall (proof-ledger display rule 6). The strongest image is a real `context` shot of the product on a store shelf from the merchant or stockist with consent, viewed to confirm the merchant's product on the shelf. Gap: ask the merchant for consented logos or a shelf photo; never generated logos, stores or people (GN3, GN5); no stock retail interior. | `none`. | one verbatim quote with name and store; sell-through as "N cases per week per door across N doors, <period>"; count as "stocked in over N stores, as of <month>". | proof ledger rows with consent and link per logo and an export per number; without rows the merchant is told what is needed and the terms, certifications and a founder note on production capacity carry the proof meanwhile. |
| `certifications` (conditional) | food safety, textile, safety or origin marks with issuer. | yes, issuer artwork only: library tag `logo`, then issuer-supplied file via `lexsis_asset_import.import`, then a monochrome SVG redraw the issuer permits; view each mark with `lexsis_assets.view` against its ledger row and confirm the real issuer's artwork. Gap: ask the merchant for the issuer file; never generated (GN5, TB10). No-go: the ISO logo, "certified" without a certifier, a badge without its number. | `none` (one row, three to five marks, issuer text beside each, per `references/proof/trust-badges-certifications.md`). | the issuer's permitted phrase and the certificate or licence number. | `certification` ledger rows holding issuer, number, scope and date. |
| `features-trade-support` (recommended) | marketing assets, displays and shelf talkers, training, sampling, reorder cadence, account manager. | yes when the merchant has real photos of the display kit, shelf talkers or marketing pack (`included-items`, `context`): library tag `lifestyle` or `flat-lay`, then merchant upload; view with `lexsis_assets.view` and confirm the kit shown is what a retailer receives. Gap: ask the merchant for kit photos (flat lay, square); a plain text list is their call; no icon tiles (N3, N12), no generated displays. | `none`. | what a retailer receives and when; 80 words. | merchant assets from reads 6 and 7. |
| `email-capture-inquiry` | the two-step application with a progress indicator. | no. | `FunnelRuntime` inline for the two-step application (inputs: the read-5 schema fields, country logic, file upload support), steps built through `lexsis_drafts.funnel_create` and checked with `lexsis_capture.validate_funnel`; resolve props from `lexsis_design.island_schema`. The progress indicator reflects the real step count (DP22); celebratory motion off (N10); the B2B consent line is unticked and never `required`; no consumer newsletter box. A single-field email island does not fit an application. | labels above fields with required and optional marked; one line on why the tax identifier is asked; button "Apply for a wholesale account". | the schema fields and country logic from read 5. |
| `how-it-works` | review time in business days, approval and account with trade pricing, first order and reorder; the marketplace alternative if any. | no. Island: `none`. | Use the shared procedure. | one sentence per step with the number of business days; the marketplace path in one line with its terms. | the review-time row from read 2 and the listing URL if the merchant sells on a marketplace. |
| `faq` (recommended) | MOQ, exclusivity, payment terms, shipping, damages, samples, price changes. | no. | `none`; native `<details>` and `<summary>`, all collapsed. | five to eight questions, answer first, 60 words each; every number matches the terms table. | read 2 and the merchant's inbound trade questions. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` packshot per SKU, `label-or-facts-panel`, swatches | `packaging` case or carton, `scale`, a group shot of the line, a shelf `context` photo | ask the merchant to photograph the case with a known object; generate `product_composite` of real cut-outs for the group shot (ALLOW); ask the merchant or stockist for the shelf photo; drop an image only on their call |
| asset library | prior packshots, issuer marks, consented stockist logos | display kit photos, the line sheet PDF | ask the merchant to upload; the line sheet is imported via `lexsis_asset_import.import` or the link waits |
| generation | backdrops and composites only (`hero_bg` under HTML text, `product_composite` over real cut-outs) | cartons, stores, people, logos, badges, text, product renders | never |

With minimal assets the page is a packshot hero from catalog media, the terms table, a grid of the imaged SKUs with the line sheet link, the two-step application and the three-step timeline; stockist and support sections are text or wait for the merchant's uploads. Generated assets on this type are at most two (one backdrop, one composite group shot); the house cap is four per page. Every asset placed, generated ones included, was opened with `lexsis_assets.view` and passed the fit review before use.

## Above the fold (390px)

In order: minimal header (logo plus "Log in"); the audience line; the
headline outcome; the "Apply" button; the first row of the terms table or
a three-fact strip (MOQ, lead time, payment terms); a `packshot` of the
line or case. Everything above the fold is a fact a buyer would write down.

Must not appear: retail prices without wholesale context, a discount pill,
a countdown, a stock statement, star glyphs, consumer review carousel,
"limited time" language, a consumer newsletter form.

## Proof

One to three modules. `policy-fact` is required: the terms table is proof
(MOQ, lead time, payment and return terms as the merchant will honour
them). Optional: `case-study` rows for named stockists (consent on file,
link to their store or listing), `review-quote` from a retailer (verbatim,
name and store), `sales-count` for sell-through ("sold through 3 cases per
week per door across 40 doors, Jan to Jun 2026", export-backed),
`customer-count` for stockists ("stocked in over 120 stores", dated),
`certification` with issuer. Retailer logos render only as `case-study`
rows with consent and a link; an unlinked logo wall is the same failure as
an unlinked press marquee (`references/proof/proof-ledger.md`, display
rule 6). Consumer review averages are not trade proof and stay off the
page unless a buyer question asks for them. When the store has no
stockists yet, the terms table, certifications and a founder note about
production capacity are the proof (`references/proof/reviews-sourcing.md`,
Tier 5).

## Offer and CTA

One or two CTAs: "Apply for a wholesale account" in the hero and repeated
above the form or at the close. The line sheet download is a text link
unless the merchant makes it the second CTA. "Log in" is a utility link.
Sticky forbidden. Copy pattern: next-step ("Apply for a wholesale account",
"Download the line sheet", "Request samples"); never "Get started".

Price and offer rules:

- `tiered-volume` here means MOQ price breaks, not a consumer promotion;
  show per-unit price and the break at each tier, no more than four tiers
  (RESEARCH, Chernev 2003 on choice overload,
  https://ideas.repec.org/a/oup/jconrs/v30y2003i2p170-83.html), and never
  a tier with a worse per-unit price than the one below.
- Prices are stated as exclusive or inclusive of tax on the same line;
  India B2B quotes are typically ex-GST with a GSTIN captured for tax
  invoices, unlike consumer MRP, and the page says which applies.
- Opening-order incentives (free freight, returns on the first order)
  sit next to the form with conditions adjacent (LAW, FTC 16 CFR 251.1 on
  "free" claims, https://www.law.cornell.edu/cfr/text/16/251.1).
- Marketplace comparison where relevant: Faire extends net 60 payment
  terms and free returns on opening orders to retailers, and Faire Direct
  charges brands 0% commission on retailers they bring versus the
  marketplace rate (OPERATOR, https://www.faire.com/brands,
  https://www.faire.com/how-faire-works); if the merchant lists there, say
  so and let the buyer choose the path.
- Application forms are multi-step with a progress indicator and
  conditional fields (OPERATOR, SparkLayer,
  https://www.sparklayer.io/forms/,
  https://docs.sparklayer.io/shopify-b2b-landing-page).

Offers that fit: `none`, `tiered-volume`; `free-shipping` (freight
threshold), `bundle` or `bundle-decoy` (starter assortments with the maths
shown), `trial-sample` (sample pack at cost), `price-lock` (price hold for a
contract period) when the merchant confirms. Offers that do not fit:
`percent-off`, `first-order`, `bogo`, `flash-sale`, `clearance`, `referral`,
`loyalty`, `cashback`, `mystery`. No urgency: lead times are facts, not
pressure.

## Imagery

Required jobs: `identity` (product line packshot) and `packaging` (case or
carton with pack count visible). Recommended: `detail` for finish or
construction, `context` for an in-store shelf or display shot, `scale` for
carton dimensions, `label-or-facts-panel` where a buyer must see the label,
`swatch` when the line has colourways. Minimum three images (HEURISTIC,
`references/assets/image-jobs-by-page-type.md`). Hero `packshot`; a `grid`
of the line sheet is the alternative. No lifestyle band with models unless
it shows the product in a store. Video optional and rarely useful. Slots
the plan must create: hero packshot, one carton or case image, one detail
or shelf image, line sheet PDF link.

## Copy

Framework: FAB aimed at retailer outcomes (feature, advantage to the store,
benefit in margin, velocity or support) with a qualifier lead ("For stores
that..."). Headline pattern: audience plus outcome ("Wholesale for
specialty grocers. 45 to 50% margin, 7-day dispatch."); numbers only when
verified. Reading level grade 7 to 8; professional tone; whole page 300 to
700 words excluding the terms table and form. Vocabulary: MOQ, case pack,
lead time, net terms, sell-through, planogram, as buyers use them; no
consumer superlatives, no "family of retailers". The form's labels are
visible above fields with required and optional marked. Copy rules in
`references/copy/copy-frameworks.md`.

## Never

- Never show retail prices without the wholesale context beside them.
- Never omit MOQ, lead time and payment terms from the page.
- Never use consumer urgency, discount pills or countdowns.
- Never render retailer or stockist logos without consent and a link.
- Never put a single long form on the page; two steps with progress.
- Never leave the approval timeline unstated.
- Never ask for a resale certificate or tax id without saying why.
- Never quote sell-through or door counts without an export in the ledger.
- Never mix a consumer newsletter capture into the application form.
- Never state a tax basis ambiguously; say ex-tax or inclusive on the price
  line.

## Examples

- Stumptown Coffee wholesale, https://www.stumptowncoffee.com/pages/wholesale:
  audience segments (cafes, office, hospitality, grocery, retail and
  events), named partner proof, a support list (consultation, menu
  development, training, marketing), one inquiry CTA.
- Faire for brands, https://www.faire.com/brands: net 60 terms and free
  returns for retailers stated as the value, Faire Direct 0% commission as
  the brand-sourced path, application as the single action.
- Blue Tokai Coffee wholesale, https://www.bluetokaicoffee.com/pages/wholesale:
  the minimum viable page, an inquiry form alone; what it lacks is the terms
  table, lead times and trade proof this type requires.

## Checklist

```json
{
  "page_type": "wholesale-b2b",
  "aliases": ["wholesale page", "trade page", "stockists page", "B2B portal landing", "bulk orders page", "distributor page"],
  "funnel_stage": ["mof"],
  "awareness": ["product-aware"],
  "traffic": ["organic", "email", "direct", "google-search"],
  "sections": { "min": 5, "max": 8 },
  "mandatory_sections": ["hero", "pricing", "email-capture", "how-it-works"],
  "recommended_sections": ["qualifier", "product-grid", "case-study", "features", "faq", "certifications"],
  "forbidden_sections": ["buy-box", "countdown", "stock-indicator", "offer", "final-offer", "sticky-cta", "savings-math", "bnpl-line", "subscription-toggle", "giveaway-entry", "referral-form"],
  "nav": "minimal",
  "price_above_fold": "forbidden",
  "cta": { "min": 1, "max": 2, "first_after_section": 0, "sticky": "forbidden", "copy_pattern": "next-step" },
  "proof": { "min_modules": 1, "max_modules": 3, "required_kinds": ["policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked", "stock-count"] },
  "imagery": { "required_jobs": ["identity", "packaging"], "hero": "packshot", "video": "optional", "min_images": 3 },
  "copy_framework": ["fab", "qualifier-lead"],
  "offer_compat": { "allowed": ["none", "tiered-volume", "free-shipping", "bundle", "bundle-decoy", "trial-sample", "price-lock"], "forbidden": ["percent-off", "first-order", "bogo", "flash-sale", "clearance", "referral", "loyalty", "cashback", "mystery"] },
  "urgency": "none"
}
```

## Sources

- SparkLayer B2B registration forms: https://www.sparklayer.io/forms/
- SparkLayer Shopify B2B landing page docs: https://docs.sparklayer.io/shopify-b2b-landing-page
- Faire for brands (terms, Faire Direct): https://www.faire.com/brands
- Faire, how it works: https://www.faire.com/how-faire-works
- Chernev 2003, assortment size and choice overload: https://ideas.repec.org/a/oup/jconrs/v30y2003i2p170-83.html
- FTC "Free" guide, 16 CFR 251.1: https://www.law.cornell.edu/cfr/text/16/251.1
- Shopify B2B (company profiles, catalogs, payment terms): https://help.shopify.com/en/manual/b2b
- Stumptown wholesale: https://www.stumptowncoffee.com/pages/wholesale
- Blue Tokai wholesale: https://www.bluetokaicoffee.com/pages/wholesale
- Research notes: internal research audit (2026-09-10) block 31; internal research audit (2026-09-10) section 1.6; internal research audit (2026-09-10) sections 5 and 10.
