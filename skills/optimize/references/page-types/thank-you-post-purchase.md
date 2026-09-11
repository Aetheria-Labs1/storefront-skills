# Thank-you and post-purchase page

The page confirms an order that is already paid and tells the shopper what
happens next: delivery expectation, setup or first use, where to get help.
It is reached from checkout (Shopify order status page or a redirect) by a
most-aware buyer whose risk is now about fulfilment, not price. Its jobs, in
order, are reassurance, next steps, one relevant add-on with a named
relationship, a referral ask, and an SMS or app opt-in where consent was not
taken at checkout. The metrics are support contacts per order, referral
share rate, opt-in rate, and attach rate measured against a holdout.

## Identify it

- The brief says "thank you page", "order confirmation", "post-purchase",
  "after checkout", "what to show after they buy", "increase AOV without
  hurting conversion".
- Near neighbours: the Shopify post-purchase one-click upsell is a separate
  surface between payment and this page
  (https://shopify.dev/docs/apps/build/checkout/product-offers/post-purchase);
  this file does not describe it. `referral-loyalty-vip` is the full
  programme page; this page carries only the share module. `offer-page`
  sells; this page confirms. A "cart" is not this type.

## Variants

- Standard: confirmation, next steps, one add-on, referral, opt-in.
- After a one-click upsell: drop the add-on (the shopper has already seen an
  offer); keep next steps, referral and opt-in.
- Subscription order: next steps include the renewal date, how to pause or
  cancel, and where to change the address.

## Anatomy

1. `hero` mandatory: "Order confirmed" with order number, item list with
   thumbnails, total paid, and the email address the confirmation went to;
   no selling in this section.
2. `post-purchase-next-steps` mandatory: delivery expectation as a date
   range from the store's estimate source, tracking link when available,
   what to do if the address is wrong, support path with hours and channel,
   returns window and warranty as written on the policy page.
3. `usage` conditional: the product needs setup, first use, care, or a
   routine; three steps or one short captioned video, no marketing copy.
4. `cross-sell` conditional: one verified add-on with a named relationship
   to the item bought (Complete the routine, Protect it, Refill the stack;
   `references/consumer-behavior-cro.md`, relationship-based merchandising);
   full price is acceptable; "Add to my order for ₹X" when the order can be
   amended, else "Add to a new order"; a decline of equal visual weight;
   never pre-ticked.
5. `referral-form` recommended: both-side reward in currency, email share
   first, copy-link second; the friend's landing states who referred them.
6. `sms-capture` or `email-capture` conditional: consent was not captured at
   checkout; single field, separate unticked consent, full disclosure text
   (consent rules in `references/page-types/lead-capture-giveaway.md`); an
   app download link may sit in the same block.

A page with only sections 1, 2 and 5 is complete. Six is the ceiling.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. The order object from the Shopify order status surface: order number, line items with variant, quantity and total, the confirmation email address, tracking URL when present, whether a one-click post-purchase offer already ran. This page's facts come from the order, not from copy.
2. `lexsis_catalog.get` for each line item (variant image for the thumbnails, viewed against the variant bought) and for the one add-on candidate: media position one as its `identity` packshot, price as listed, inventory (suppress when zero), variant count (a single variant adds in one tap), selling plans on the bought SKU (only then may "make this a subscription" appear). Jobs per `references/assets/image-jobs-by-page-type.md`.
3. The delivery source, confirmed by the merchant: carrier estimate or store policy in business days with cutoff hour, or pincode service; the returns window, warranty and support hours and channel copied from the policy page URL. Each is an offer ledger `shipping` row or a proof ledger `policy-fact` row.
4. `lexsis_brand.context` and `lexsis_brand.brand_kit` for `theme_id`, logo, voice; `lexsis_brand.navigation` only for the "Continue shopping" and account URLs (nav is `minimal`).
5. The add-on relationship from the merchant: which item, the relationship name from `references/consumer-behavior-cro.md` (Complete the Routine, Protect It, Refill the Stack, Make It Work), its kind and the mapping source; placement and consent guardrails in `references/offers/aov-levers.md` (post-purchase row) and `references/anti-patterns/dark-patterns.md` (DP4, DP5, DP6, DP10).
6. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`: `lifestyle` and `product-shot`; then semantic "setup <product>", "how to use <product>", "unboxing" for `sequence`; `packaging` only when the shopper must recognise the box; view with `lexsis_assets.view`.
7. Referral programme values (both sides in currency, friend's terms) from the programme configuration; `lexsis_capture.form_schemas` for the referral and SMS schemas; the checkout marketing-consent setting, which decides whether `sms-capture` or `email-capture` exists at all.
8. `lexsis_design.islands`, then `lexsis_design.island_schema` for `DeliveryEstimate`, `QuickAdd`, `EmailCapture` and, with a real video, `VideoPlayer` (`references/workflows/island-selection-workflow.md`).

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `hero` | "Order confirmed" with the number, the items with thumbnails, the total, the confirmation email address. No selling. | yes. The line-item thumbnails are `identity` images from catalog media (read 2), each viewed with `lexsis_assets.view` and matched to the variant bought. The hero itself is `typographic`; a `packshot` of the ordered item is the alternate. Gap: a line item with no variant image is reported to the merchant (SKU, square) and shown as text until they upload; never generated. No-go: a lifestyle hero, celebration graphics, confetti. | `none`. Header `SiteHeader` with the cart hidden (the cart is empty),. | "Order confirmed" or "Thanks, <first name>. Your order is on its way" with the order number beneath; 30 words. | which order fields the surface exposes (read 1). |
| `post-purchase-next-steps` | delivery date range, tracking, wrong-address path, support with hours, returns window and warranty as the policy states them. | no by default; an inline SVG `diagram` of the delivery timeline is optional. No stock couriers or parcels. | `DeliveryEstimate` when the store has a single-country estimate in business days (inputs: the shipping ledger row, cutoff hour). India pincode copy is static HTML (no pincode prop). When the order status surface supplies a carrier date, write that date range in HTML and drop the island; skip the island for international or variable transit. | one sentence per step; dates as dates ("Arrives 14 to 17 Sept"), never speeds; support hours and channel in one line. | the shipping source and policy rows from read 3; whether a tracking URL exists in read 1. |
| `usage` (conditional) | setup, first use, care or routine with no marketing copy. | yes. Job `sequence`: three real step photos, or one captioned video under 60 seconds. Catalog media (routine or setup shots), then library tag `lifestyle`, semantic "setup <product>", then merchant upload; view each step with `lexsis_assets.view` and confirm it shows the ordered product and the action is legible at 390px. Gap: ask the merchant for step photos (three, square or 4:5); never generated; folding the steps as text into next-steps is the merchant's call. No icon tiles. | `VideoPlayer` when a real video exists; otherwise `none`. | three steps, one sentence each; step text in HTML, not in the image. | does the product need setup (brief), `sequence` coverage from read 6 and the merchant's answer. |
| `cross-sell` (conditional) | one add-on with a named relationship to the item bought, at the listed price. | yes. Job `identity` for the add-on from catalog media position one, viewed with `lexsis_assets.view` to confirm the exact SKU on the same background as the order thumbnails. Gap: ask the merchant for the add-on packshot (square, one); never generated; a different add-on with an image is the merchant's call. No-go: a grid or carousel, more than one item, a generated composite, a discount by default, a pre-ticked add. | `QuickAdd` for the single add-on (inputs: variant count, inventory, Cart V2 via `head.use_cart_v2`); a product rail island needs four or more products and this section shows one. Resolve props from `lexsis_design.island_schema`; the button label carries the amount ("Add to a new order for ₹X"); the decline is a plain HTML link of equal size and contrast with neutral text ("No thanks, continue"). Amending the paid order belongs to the Shopify post-purchase surface; when that surface already ran, this section is omitted. | one sentence naming the relationship ("Fits the Transit Cabin you ordered"); price as listed; no "don't miss out". | the Guided merchandising line from read 5 (relationship, kind, mapping source), inventory above zero in read 2, no prior one-click offer in read 1. |
| `referral-form` (recommended) | both sides of the reward in currency, email share first, copy-link second. | no. | `EmailCapture` for the friend-email share (inputs: the referral schema in read 7); resolve props from `lexsis_design.island_schema`; the reward maths sit in HTML beside the form, not in a discount line; copy-link as a plain HTML button after it. | 25 words plus the friend's terms in one line; the friend's landing says who referred them. | programme values and the schema from read 7; no programme, no section. |
| `sms-capture` or `email-capture` (conditional) | consent not taken at checkout, one field, separate unticked consent, full disclosure; an app link may share the block. | no. | `EmailCapture` for email; `FunnelRuntime` inline with a single phone step from the read-7 SMS schema for SMS, or a plain HTML form to the messaging provider. Resolve props from `lexsis_design.island_schema`. The consent checkbox and disclosure are authored in HTML under the field, unticked, never `required` (DP5). | the market's consent text in full; frequency as a number. | the checkout consent setting from read 7; consent already given at checkout means the section does not exist. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | line-item thumbnails, the add-on `identity` packshot | `sequence` setup photos, a setup video | ask the merchant to upload step photos or a captioned video; fold the steps into next-steps as text only if they choose |
| asset library | occasional setup or routine photos (`lifestyle`) | `packaging` when the box matters | ask the merchant to upload; keep the text and drop the image only on their call |
| generation | nothing on this page (typographic hero, no bold-moment backdrop) | product, people, parcels, couriers, badges, text | never |

With minimal assets the page is order facts with catalog thumbnails, a delivery date range, support and returns lines, one add-on packshot with its button and decline, and the referral form; it is complete without any other image. Generated assets on this type are zero; the house cap of four per page is never approached. Every asset placed, generated ones included, was opened with `lexsis_assets.view` and passed the fit review before use.

## Above the fold (390px)

In order: minimal header (logo plus "Continue shopping" or account link);
"Order confirmed" and the order number; the items with thumbnails and the
total; the delivery date range and tracking link or "tracking arrives by
email"; the support line. Nothing that asks for money is visible before the
delivery expectation.

Must not appear: a discount, a countdown, a stock statement, a product
grid, a popup, an add-on above the confirmation facts, a pre-ticked box.

## Proof

Zero or one module. If one, it is either a `review-summary` on the add-on
card (average and count from `lexsis_catalog.reviews`) or the `guarantee`
or `policy-fact` line in next steps (returns window, warranty, exactly as
the policy page states). No press, no UGC, no testimonial block: the
shopper has bought; proof now is about fulfilment facts. When the store has
neither, the section is the delivery and returns facts alone.

## Offer and CTA

One or two CTAs, and none before the next-steps section: the add-on button
and the referral share button. Tracking, account and support links are
utilities, not CTAs. Sticky forbidden. Copy pattern: next-step ("Add to my
order for ₹X", "Share your link", "Track your order"); never "Don't miss
out".

Evidence and guardrails (pointer: `references/offers/aov-levers.md`):

- The thank-you page is the wrong place for a discount wall. One-click
  post-purchase offers take 3 to 8% and carry 62.1% of upsell revenue in
  Zipify's network, while thank-you page offers convert around 1%
  (OPERATOR, Zipify, https://zipify.com/blog-post-purchase-upsells-shopify-2026/).
  Use this page for opt-ins, referral and next steps; if the merchant wants
  a revenue upsell, that is the one-click surface before this page.
- Relevance beats discount depth: full-price post-purchase offers accepted
  at 17.89%, and offer price barely moved acceptance (OPERATOR, AfterSell,
  https://www.aftersell.com/2026-revenue-report). So the one add-on is the
  most useful related item, not the cheapest.
- Measure incrementality with a holdout, not take rate: a worked example
  showed $2.70 true incremental AOV against $3.30 implied (OPERATOR,
  Daymark, https://www.usedaymark.io/blog/post-purchase-upsell-measurement).
- One upsell surface per stage; if a one-click offer ran, this page shows
  no add-on (OPERATOR, internal research audit (2026-09-10) 6.6).
- Post-purchase is one of the three placements Yotpo recommends for
  referral (OPERATOR, https://support.yotpo.com/docs/referral-program-how-it-works).
- Adding to an existing order needs express consent language that names
  the amount ("Add to my order for ₹X"); pre-selection is basket sneaking
  under India's CCPA guidelines and fails FTC ROSCA-style consent (LAW,
  https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-and-regulation-dark-patterns-2023).
- A charity round-up is allowed only as an unticked choice with the
  recipient named.

Offers that fit: `none`, `referral`, `loyalty` (points earned on this
order, join prompt); `subscribe-save` only as "make this a subscription"
with cadence, price and cancellation stated; `charity` as above. Offers
that do not fit: `percent-off`, `fixed-off`, `first-order` (they have
ordered), `bogo`, `gwp`, `flash-sale`, `clearance`, `mystery`. No countdown,
no stock statement.

## Imagery

No required job; zero to one image beyond order thumbnails (HEURISTIC,
`references/assets/image-jobs-by-page-type.md`). Hero `typographic`;
`packshot` of the ordered item is the alternative. The add-on shows one
`identity` packshot. `sequence` or a short captioned video for setup when
the product needs it; `packaging` only when the shopper should recognise
the box. Nothing decorative. Slots the plan must create: none by default;
one add-on identity slot when `cross-sell` is present.

## Copy

Framework: answer-first, completion principle ("You're set. Here is what
happens next."). Headline pattern: "Order confirmed" or "Thanks, [first
name]. Your order is on its way" with the order number beneath; never a
sales headline. Reading level grade 5 to 6. Ceilings: hero 30 words; each
next step one sentence; add-on rationale one sentence naming the
relationship ("Fits the Transit Cabin you ordered"); referral 25 words;
whole page under 250 words. Dates are dates, not speeds ("Arrives 14 to 17
Sept", not "fast shipping"). Consent copy in full. Copy rules in
`references/copy/copy-frameworks.md`.

## Never

- Never place an offer above the delivery expectation.
- Never show more than one add-on, and never a grid.
- Never discount the add-on by default; relevance first, price as listed.
- Never pre-tick an add-on, subscription, insurance or donation.
- Never show a countdown or stock statement on a confirmation page.
- Never state a delivery date without a source (carrier estimate, pincode
  service, store policy).
- Never ask for SMS consent already given at checkout.
- Never bundle the referral share with a purchase condition the shopper
  cannot see.
- Never show a decline button smaller or lighter than the accept button.
- Never omit the support path and the returns window.

## Examples

Thank-you pages sit behind checkout, so the references below are documented
patterns rather than public URLs.

- Zipify, four thank-you page offers,
  https://zipify.com/blog-4-proven-thank-you-page-offers/: referral,
  opt-in and education outperform discounts on this surface.
- AfterSell best practices, https://docs.aftersell.com/aftersell/best_practices:
  one offer, one downsell, equal-weight decline, funnel logic kept on the
  one-click surface rather than the confirmation page.
- Shopify, post-purchase upsell guidance,
  https://www.shopify.com/blog/post-purchase-upsell: confirmation line
  first, one relevant add-on, no re-entering payment.

## Checklist

```json
{
  "page_type": "thank-you-post-purchase",
  "aliases": ["thank you page", "order confirmation page", "order status page", "post-checkout page"],
  "funnel_stage": ["retention"],
  "awareness": ["most-aware"],
  "traffic": ["direct"],
  "sections": { "min": 3, "max": 6 },
  "mandatory_sections": ["hero", "post-purchase-next-steps"],
  "recommended_sections": ["referral-form", "cross-sell", "usage", ["sms-capture", "email-capture"]],
  "forbidden_sections": ["offer", "final-offer", "countdown", "stock-indicator", "product-grid", "sticky-cta", "quantity-breaks", "savings-math", "bundle-builder"],
  "nav": "minimal",
  "price_above_fold": "optional",
  "cta": { "min": 1, "max": 2, "first_after_section": 2, "sticky": "forbidden", "copy_pattern": "next-step" },
  "proof": { "min_modules": 0, "max_modules": 1, "required_kinds": [], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "stock-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": [], "hero": "typographic", "video": "optional", "min_images": 0 },
  "copy_framework": ["answer-first"],
  "offer_compat": { "allowed": ["none", "referral", "loyalty", "subscribe-save", "charity"], "forbidden": ["percent-off", "fixed-off", "first-order", "bogo", "gwp", "flash-sale", "clearance", "mystery"] },
  "urgency": "none"
}
```

## Sources

- Zipify post-purchase upsells 2026: https://zipify.com/blog-post-purchase-upsells-shopify-2026/
- Zipify thank-you page offers: https://zipify.com/blog-4-proven-thank-you-page-offers/
- AfterSell 2026 revenue report: https://www.aftersell.com/2026-revenue-report
- AfterSell best practices: https://docs.aftersell.com/aftersell/best_practices
- Daymark, measuring post-purchase upsell incrementality: https://www.usedaymark.io/blog/post-purchase-upsell-measurement
- Shopify post-purchase upsell guide: https://www.shopify.com/blog/post-purchase-upsell
- Shopify post-purchase extension surface: https://shopify.dev/docs/apps/build/checkout/product-offers/post-purchase
- Shopify thank-you and order status page customisation: https://shopify.dev/docs/apps/build/checkout/thank-you-order-status
- Yotpo referral placements: https://support.yotpo.com/docs/referral-program-how-it-works
- India CCPA dark-pattern guidelines 2023 (basket sneaking): https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-and-regulation-dark-patterns-2023
- Research notes: internal research audit (2026-09-10) block 24 and section 4.2; internal research audit (2026-09-10) section 6.
