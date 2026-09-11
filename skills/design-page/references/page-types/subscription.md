# Subscription page

A page whose subject is the recurring plan: cadence, saving per delivery,
first-order terms, and how to skip, pause or cancel, stated plainly beside
the plan choice. Shoppers arrive product-aware from a PDP link, email or ads
for a replenishable product; their job is to choose between one-time and
subscribe (or between plans) and start. The page removes the lock-in fear by
showing the exit before asking for the commitment. Subscription mechanics on
an ordinary PDP are a `subscription-toggle` inside `pdp`, not this type.

## Identify it

- Brief says "subscribe", "subscription", "auto-ship", "membership",
  "subscribe and save", "recurring", or names a churn or retention goal.
- Product is consumable or replenishable (supplements, coffee, pet food,
  razors, skincare) and the merchant has Shopify selling plans.
- Visitor mode is "replenish" or "complete" (`references/consumer-behavior-cro.md`).
- Near neighbours:
  - `pdp`: the product is the subject and subscription is one purchase
    option; choose `pdp` when the brief is about the product.
  - `bundle-kit`: a one-time set; choose bundle when cadence is not the
    point.
  - `trial-sample`: a first low-risk purchase that may convert into a plan;
    choose trial when the first order is a sample.
  - `referral-loyalty-vip`: a membership with tiers and points but no
    recurring shipment.
- RESEARCH and OPERATOR: subscribers place about 3x more orders than
  one-time shoppers across Recharge's merchant base
  https://getrecharge.com/reports/subscription-trend-report-2026/ ; the
  page's job is to protect 90-day retention by setting expectations, not only
  to win the first order.

## Variants

- **Subscribe-and-save plan.** One product, a `plan-selector` with one-time
  and subscribe side by side, frequency choices, saving per delivery.
- **Plan tiers.** Two or three plans (monthly, 3-month prepay, 6-month
  prepay) in a `plan-selector` with a `comparison` table; the saving grows
  with prepay; totals shown per delivery and per month, never only the
  prepaid lump sum.
- **Subscription-only product** (Seed DS-01). No one-time option exists; the
  FAQ's first question is still "Do I have to subscribe?" and the answer is
  "Yes" with the cancel path in the same sentence.
- **Curated box** (Blue Tokai mixed bag). A configurator for count, size,
  grind and frequency; the same terms rules apply to every configuration.

## Anatomy

Counts exclude chrome. Observed order is from the Seed, Huel and Blue Tokai
teardowns in internal research audit (2026-09-10).

1. `announcement`: conditional: a verified first-order term or free-shipping
   fact. Never a countdown.
2. `header`: mandatory, minimal. Full navigation when the page is a permanent
   store page; record the override.
3. `hero`: mandatory. Outcome headline, product in its routine context,
   `review-summary` when 5 or more reviews exist, one sentence naming the
   cadence ("30-day supply delivered monthly").
4. `plan-selector`: mandatory. One-time and subscribe prices side by side,
   frequency options, saving per delivery in currency and percent, per-day or
   per-serving line where the label states servings, renewal price and
   cadence stated before the button, "skip, pause or cancel anytime in your
   account" in the same block. Nothing pre-selected unless the merchant
   confirms subscription is the primary offer and the price difference is
   shown in the same block. Selling-plan binding is chosen by design-page.
5. `how-it-works`: mandatory, within one scroll of the plan selector. Three
   steps: choose, we deliver, skip or pause or cancel. Names the first charge
   date, the renewal notice (Blue Tokai: "email a day before every delivery"),
   and the cancel path in one sentence.
6. `savings-math`: recommended. Per-delivery saving, first-order terms
   ("first box 20% off, then $45 every 4 weeks"), prepay saving where tiers
   exist.
7. `benefits`: recommended. Subscriber-only value: price, free shipping,
   early access, welcome kit shown as items with value (Seed glass jar and
   travel vial; AG1 value stack with struck free items).
8. `features`: recommended (flexibility proof). Real portal screenshots of
   skip, swap, pause and cancel, labelled; no mock-ups.
9. `comparison`: conditional: two or more plans or a one-time vs subscribe vs
   bundle choice. One "best for" line per column; no ribbon.
10. `testimonial-spotlight` or `reviews`: mandatory. Quotes that carry tenure
    ("month 14"), verbatim and dated; the review list where 20 or more exist.
11. `guarantee`: mandatory. Money-back terms plus "cancel in two clicks"
    reassurance with the exact path.
12. `faq`: mandatory. First question: "Do I have to subscribe?" Then billing
    date, how to change frequency or flavour, how to cancel, what if I have
    too much, what the renewal price is.
13. `sticky-cta`: optional. Plan name plus price per delivery plus "Start my
    subscription"; opens the plan selector when no plan is chosen.
14. `closing-cta`: mandatory. Restates plan, price per delivery, cancel path.
15. `legal`: recommended chrome. Full subscription terms link; the material
    terms are already on the page beside the selector (ROSCA).
16. `footer`: mandatory chrome.

## Workflow

Assets first: the routine, the delivery contents and the portal are shown
before they are described. A section that would end up as a colour band, an
emoji row, icon tiles or a wall of text is rebuilt around imagery or, on the
merchant's call, merged or skipped. Per-slot sourcing:
`references/workflows/section-asset-workflow.md`; island choice:
`references/workflows/island-selection-workflow.md`. Missing media is never
dropped silently: every Media line ends by telling the merchant what is
missing (job, aspect, count), offering upload via `lexsis_asset_upload.upload`
or MCP generation when the purpose is feasible under
`references/assets/generation-policy.md`, and skipping or merging the section
only if the merchant chooses. In fast-draft the agent proceeds with the closest
existing asset or leaves the slot `planned`, and lists every missing asset in
the plan and the draft summary.

### Context reads

1. `lexsis_catalog.get`: selling plans (ids, cadence, price or discount per
   plan), the one-time price, `media[]` mapped to jobs per
   `references/assets/image-jobs-by-page-type.md` (identity, included-items
   for one delivery and any welcome kit, context in the routine, in-use,
   packaging, label), inventory, servings on the label for a per-day line
   (`references/offers/price-presentation.md` PP9).
2. `lexsis_catalog.reviews_status`; `lexsis_catalog.reviews` with
   `product_id` (band, newest date); `lexsis_catalog.reviews_search` with
   `query` "month", "months", "year", "since", "still" for tenure quotes
   (`pending` until confirmed, `references/proof/reviews-sourcing.md` RS16);
   `review_collections` with `collection_status: "active"`.
3. Offer ledger `subscribe-save` row and `policy-fact` rows
   (`references/offers/offer-types.md` subscribe-save, first-order,
   price-lock): renewal price, cadence, first charge date, renewal notice,
   skip, pause and cancel path with the exact clicks; the merchant's
   confirmation that one-time stays the default (or that subscription is the
   primary offer, recorded).
4. `lexsis_brand.context`, `lexsis_brand.brand_kit`, `lexsis_brand.navigation`.
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"` for
   `lifestyle`, `flat-lay`, `product-shot`, `social-proof`; then semantic
   "<product> morning routine", "unboxing". Sequence and checks:
   `references/assets/asset-sourcing-sequence.md`.
6. `lexsis_asset_import.import` for real subscriber-portal screenshots from the
   merchant (skip, swap, pause, cancel), cropped only, labelled as
   screenshots; no mock-ups.
7. `lexsis_cart.get`: how the selling plan is carried into the cart; cart v2.
   `lexsis_design.islands`, then `lexsis_design.island_schema` for each island
   named below. `lexsis_workspace.credits` only if a `product_composite` for
   the routine context is planned.

### Section by section

No asset is used sight unseen: open every candidate with `lexsis_assets.view`
and run the section 1b fit review in `references/workflows/section-asset-workflow.md`
before use (subject does the job, crops to the slot without losing the product,
quiet area for the copy, lighting and styling match neighbouring slots, palette,
no baked-in text or watermark); view a section's or gallery's candidates
together so the set reads as one shoot, and view a generated asset the same way
after it returns.

**`announcement`**
- Purpose: one verified first-order term or free-shipping fact.
- Media: none; text; never a countdown.
- Island: SiteHeader announcement strip or AnnouncementBar, one message; resolve from `lexsis_design.island_schema`; preset `announcementbar/static-dark`. Omit without a ledger row.
- Copy: under 60 characters; the renewal price is never hidden behind the intro line (`references/anti-patterns/copy-anti-patterns.md`).
- Decide with: offer ledger row; `lexsis_cart.get` threshold.

**`header`**
- Purpose: minimal chrome; full nav only for a permanent store page.
- Media: brand logo or wordmark. View every candidate with `lexsis_assets.view` and run the section fit review (section 1b of `references/workflows/section-asset-workflow.md`) before use.
- Island: SiteHeader minimal with the CTA anchoring to the plan selector, or Navbar for the store-page override; resolve from `lexsis_design.island_schema`; preset `siteheader/minimal-light` or `navbar/sticky-light`.
- Copy: store names.
- Decide with: `lexsis_brand.navigation`.

**`hero`**
- Purpose: outcome headline, the product in its routine, review summary, one cadence sentence.
- Media: yes, context (`product-in-context`): catalog media showing the routine, library `lifestyle`, merchant upload, then a `product_composite` (ALLOW) of the real cut-out on a plain surface, captioned when the surface is photoreal; `product_lifestyle` is ASK. Alternate `packshot` with the included items. Never a grid of plans, never a generated person. Missing: tell the merchant (context, landscape and portrait); offer upload or the composite; the packshot ships meanwhile. View the candidates together with `lexsis_assets.view` and run the section fit review so the set reads as one shoot, not a pile of found images.
- Island: none (one static image with a portrait mobile crop); ProductHero in a split layout when three or more real images exist, no autoplay (N10); resolve from `lexsis_design.island_schema`; preset `producthero/split-rail-light`.
- Copy: outcome plus cadence ("Your daily probiotic, delivered every 30 days"), 10 words; cadence sentence 14 words; review summary only at 5 or more reviews.
- Decide with: context image found in steps 1 and 5; review band.

**`plan-selector`**
- Purpose: one-time and subscribe side by side with the saving, cadence, renewal price and cancel path in the same block; nothing pre-selected.
- Media: none new; the hero image sits beside it in a split layout. The block is a form.
- Island: one product, one-time vs subscribe: SubscriptionToggle bound to the selling plans, one-time default, paired with a BuyBox that listens to it. Two or three plans (prepay tiers) or one-time vs subscribe vs bundle: PlanSelector in card or stacked form bound to the selling plan ids, no default plan or the one-time plan, no badge (N9), paired with the listening BuyBox. A subscription default only with the merchant's recorded confirmation and both prices visible. Decision inputs: selling plan count and structure, the confirmation in step 3. Resolve variant and props from `lexsis_design.island_schema`.
- Copy: 14 words per microcopy line: recurring amount, cadence, first charge date, "skip, pause or cancel anytime in your account"; per-delivery before totals; per-day line only when servings are on the label (PP9).
- Decide with: step 1 selling plans; step 3 confirmation.

**`how-it-works`**
- Purpose: choose, we deliver, skip or pause or cancel, within one scroll of the selector.
- Media: yes, sequence: three real frames (the product, the delivery packaging, the real portal screenshot) from catalog, merchant upload, library; an inline SVG flow authored in HTML when frames are missing (allowed for `sequence` in `image-jobs-by-page-type.md` section 7). Never generated frames or a mock portal. Missing: tell the merchant (packaging shot, portal screenshot); offer upload; the SVG flow ships meanwhile. View the candidates together with `lexsis_assets.view` and run the section fit review so the set reads as one shoot, not a pile of found images. View the frames in order so they read as one flow.
- Island: none; optional click-to-play portal walkthrough per `references/assets/video-rules.md`.
- Copy: 25 words per step; first charge date, renewal notice, cancel path each named once.
- Decide with: packaging and portal assets from steps 5 and 6.

**`savings-math`**
- Purpose: per-delivery saving, first-order terms, prepay saving.
- Media: none; a price table.
- Island: none; the struck one-time price carries `data-source="compare_at_price"` or the ledger row id.
- Copy: "first box 20% off, then $45 every 4 weeks"; per-delivery and per-month before any lump sum (PP9, PP10).
- Decide with: offer ledger rows.

**`benefits`**
- Purpose: subscriber-only value shown as items with value (welcome kit, free shipping, early access).
- Media: yes, included-items: flat lay of one delivery plus the welcome kit from catalog media, library `flat-lay`, or merchant upload; never generated. Missing: tell the merchant (included-items, landscape, one shot); offer upload; fold the facts into the plan-selector microcopy only on the merchant's call. View every candidate with `lexsis_assets.view` and run the section fit review before use.
- Island: none.
- Copy: item name plus value ("glass jar and travel vial, $18 value"); 18 words per item.
- Decide with: flat lay found; kit item prices from the catalog.

**`features`**
- Purpose: flexibility proof: real portal screens for skip, swap, pause and cancel.
- Media: yes, real screenshots imported in step 6, cropped only, labelled "screenshot of your account" (`policy-fact` rows). Missing: tell the merchant which four screens are needed; offer import; the cancel path stays in text meanwhile; skip only on the merchant's call. View the candidates together with `lexsis_assets.view` and run the section fit review so the set reads as one shoot, not a pile of found images.
- Island: none.
- Copy: one label per screen (6 words).
- Decide with: screenshots supplied.

**`comparison`**
- Purpose: two or more plans, or one-time vs subscribe vs bundle, one "best for" line per column.
- Media: optional identity image per column when plans differ physically; otherwise a plain HTML table. View the candidates together with `lexsis_assets.view` and run the section fit review so the set reads as one shoot, not a pile of found images.
- Island: none; PlanSelector already renders the tiers, so this is the attribute table beneath it.
- Copy: "best for" 12 words; per-delivery and per-month figures in every column.
- Decide with: plan count from step 1.

**`testimonial-spotlight`** or **`reviews`**
- Purpose: tenure proof: quotes that say month fourteen.
- Media: review photos from the records; avatars real or CSS initials. View every candidate with `lexsis_assets.view` and run the section fit review before use.
- Island: by band per `references/proof/reviews-sourcing.md`: B1 static verbatim dated cards; B2 ReviewCarousel one card at a time, autoplay off (N10), bound to the product id or an active collection, tenure candidates once confirmed; B3 or more ReviewList sorted by recent with filters. Resolve from `lexsis_design.island_schema`; preset `reviewcarousel/single-quiet`.
- Copy: quotes verbatim, 60 words, dated, tenure kept in the text.
- Decide with: band and confirmed `reviews_search` candidates.

**`guarantee`**
- Purpose: money-back terms plus "cancel in two clicks" with the exact path.
- Media: none.
- Island: none.
- Copy: two sentences; the minimum term stated if one exists.
- Decide with: `policy-fact` rows.

**`faq`**
- Purpose: "Do I have to subscribe?" first, then billing date, changing frequency, cancelling, too much product, renewal price.
- Media: none.
- Island: none; native `<details>` (the FAQ island is deprecated).
- Copy: answers 60 words; first sentence "Yes" or "No".
- Decide with: terms from step 3.

**`sticky-cta`**
- Purpose: plan name plus price per delivery plus "Start my subscription".
- Media: product thumbnail or a text-only bar. View every candidate with `lexsis_assets.view` and run the section fit review before use.
- Island: StickyBar in product mode appearing after the selector; the schema has no plan sync, so it is used only when one plan (or the one-time price) is the label, otherwise omitted; resolve from `lexsis_design.island_schema`; preset `stickybar/product-light`.
- Copy: the label names the plan and per-delivery price.
- Decide with: plan count; page length past about three mobile screens.

**`closing-cta`**
- Purpose: restate plan, price per delivery, cancel path.
- Media: hero context image reused small; no new asset.
- Island: none; anchor to the plan selector.
- Copy: price and cadence verbatim from the selector; cancel path one line.
- Decide with: mirrors the plan selector.

**`legal`** and **`footer`**
- Purpose: full subscription terms link; footer chrome.
- Media: brand logo. View every candidate with `lexsis_assets.view` and run the section fit review before use.
- Island: Footer; the terms link as a column item; preset `footer/simple-light` or `footer/columns-dark`.
- Copy: "Subscription terms"; the material terms are already beside the selector (ROSCA).
- Decide with: terms URL confirmed.

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | identity, sometimes a kit or delivery flat lay, label photo | product in the routine, portal screenshots, sequence frames, packaging | generate `product_composite` of the real cut-out for the hero context; ask the merchant to upload the flat lay, packaging and screenshots or approve the composite; SVG flow for how-it-works meanwhile; skip benefits or features only on the merchant's call |
| asset library | `lifestyle` routine scenes, `flat-lay` deliveries, `social-proof` with rights | portal screenshots (only present when the merchant imported them), tenure UGC | ask the merchant to upload; label imports as screenshots |
| generation | backdrops, textures, a single-product composite only | the delivery contents, the portal, people, results, logos, text | never |

Minimal assets (one identity image): packshot hero with the context slot `planned`, the plan selector, an SVG how-it-works flow, savings math, tenure quotes or static cards by band, guarantee, native FAQ; benefits and features wait on the merchant, and every missing asset is listed in the plan and draft summary. Generated assets: zero or one composite for the hero context, never more than the house cap of four. Every asset, generated ones included, is opened with `lexsis_assets.view` and passes the fit review in `references/workflows/section-asset-workflow.md` section 1b before it ships; a paid render earns no exemption.

## Above the fold (390px)

In order: header, outcome headline, product-in-routine image (no more than
60% of viewport height), review summary with count, the cadence sentence, the
plan selector's first row showing one-time and subscribe prices side by side
with the saving. "Skip, pause or cancel anytime" is visible within the same
block or the next screen; the full how-it-works is within one scroll of the
toggle. Not above the fold: a countdown, a pre-selected plan, a prepaid lump
sum without its per-delivery equivalent, a popup.

## Proof

- Modules: 2 to 3. Module one is `review-summary` in the hero. Module two is
  `review-quote` with tenure or `review-list`. Module three is `guarantee` or
  `policy-fact` (the cancellation path as a verifiable store policy) or
  `test-data` for clinical products.
- Tenure in quotes is the differentiating evidence: the shopper's fear is
  regret at month three, so the proof shows month fourteen.
- Portal screenshots count as `policy-fact` only when they are real
  screenshots of the store's own portal; never generated.
- `customer-count` ("over 4,000,000 customers", Huel) only with an export or
  analytics screenshot, rounded down, "over N", as-of month when older than
  90 days.
- No reviews: guarantee with exact terms, cancellation policy as a fact,
  certifications with issuer, founder note. Nothing review-shaped
  (`references/proof/reviews-sourcing.md`).

## Offer and CTA

- CTA count: 2. "Start my subscription" (or "Subscribe and save 15%") in the
  plan selector, and the closing CTA. A "Buy once" secondary action is part
  of the plan selector, not a third CTA.
- First CTA position: the plan selector (section index 1 of the body, directly
  under the hero); the hero itself may anchor to it.
- Sticky: optional; carries plan and per-delivery price.
- CTA copy: names the plan, not the purchase ("Start my subscription",
  "Start your first 30 days"). Renewal terms sit directly beneath in one line.
- Price reveal: immediate. Both prices side by side; saving per delivery;
  per-day framing for consumables where exact (RESEARCH, Gourville 1998:
  "85 cents a day" drew 52% vs 30% for the identical annual figure
  https://doi.org/10.1086/209517 ); prepay tiers shown per delivery and per
  month before the lump sum.
- Terms within one scroll of the toggle: recurring amount, cadence, first
  charge date, how to cancel. LAW: US ROSCA requires material terms before
  billing information, express informed consent and simple cancellation
  https://www.ftc.gov/business-guidance/blog/2024/10/click-cancel-ftcs-amended-negative-option-rule-what-it-means-your-business
  (the 2024 Negative Option Rule was vacated in July 2025; ROSCA and state
  auto-renewal laws still apply); UK DMCC subscription-contract rules phase in
  from 2026 https://cms.law/en/gbr/legal-updates/game-changing-consumer-protection-provisions-under-the-dmcc-act-come-into-force-are-you-prepared ;
  India CCPA lists "subscription trap" as a dark pattern
  https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf .
- Default state: one-time selected, or no selection, unless the merchant
  confirms subscription is the primary offer and the block shows the price
  difference (`references/anti-patterns/dark-patterns.md`, basket sneaking
  and subscription trap).
- Offers that fit: `subscribe-save` (default), `first-order` (first box
  discount with the renewal price beside it), `gwp` (welcome kit shown as
  items with value), `price-lock` ("your price stays $45 per delivery for 12
  months"), `free-shipping`, `loyalty`, `trial-sample` (a first sample that
  converts, with the conversion date stated), `bundle` and `bundle-decoy`
  (plan tiers with a table), `none`.
- Offers that do not fit: `percent-off` or `fixed-off` as a standalone
  discount, `bogo`, `flash-sale`, `clearance`, `mystery`, `bnpl`, `cashback`,
  `limited-edition`. A countdown never appears on a subscription page.
- Intro discount depth: OPERATOR, Recharge 2022 flagged churn at expiry when
  the first-box discount is far deeper than the ongoing saving; keep the gap
  visible and modest.

## Imagery

- Required jobs: `identity`, `included-items` (what one delivery contains,
  plus any welcome kit), `sequence` (choose, deliver, manage: three real
  frames or an inline SVG flow). Recommended: `in-use`, `context` (product in
  the routine), `scale`, `packaging`, `diagram` (cadence over months),
  `ugc` when rights exist, `label-or-facts-panel` for regulated consumables.
- Hero: `product-in-context` (the product in its routine); alternate
  `packshot` with the included items. Never a `grid` of plans as the hero.
- Minimum images: 4 (identity, included-items per delivery, sequence, in-use).
  Seed's gallery of five (jar, mechanism diagram, welcome kit, lifestyle, one
  companion product) is the observed reference.
- Portal screenshots are real captures of the merchant's subscriber portal,
  cropped only, labelled as screenshots.
- Video: optional; a 45 to 90 second "how it works" or portal walkthrough as
  click-to-play with poster; never autoplay with sound.
- Slots the plan creates: one `included-items` slot when no delivery flat lay
  exists; one `sequence` slot (or an SVG flow authored in HTML) when no
  how-it-works imagery exists.

## Copy

- Framework: `bab` for the page spine (before: running out, reordering;
  after: it just arrives; bridge: the plan), `fab` for plan features.
- Headline: the outcome plus the cadence ("Your daily probiotic, delivered
  every 30 days"), never the discount alone.
- Reading level grade 6 to 8; 500 to 1,000 words total.
- Length ceilings: plan-selector microcopy 14 words per line; how-it-works
  step 25 words; testimonial quote 60 words; FAQ answer 60 words, first
  sentence is the answer ("Yes" or "No").
- Vocabulary: "every 4 weeks" not "recurring billing cycle"; "cancel in your
  account in two clicks" not "flexible"; per-delivery framing before totals
  ("$45 every 4 weeks" before "$135 for 3 months"). Never "unlock", "lock in
  your spot", "limited".
- Microcopy under the CTA: renewal price and cadence, "skip, pause or cancel
  anytime", guarantee, shipping.

## Never

- Never pre-select the subscription option unless the merchant confirms it
  is the primary offer and the block shows both prices.
- Never hide the cancellation path from the page or leave it only in the
  footer terms.
- Never state a prepaid total without its per-delivery or per-month
  equivalent beside it.
- Never omit the renewal price after an introductory discount.
- Never make the one-time option visually subordinate (smaller, grey, or a
  text link beside a button).
- Never place a countdown or stock count on a subscription page.
- Never use mock-up portal screens; real captures only.
- Never show tenure-free testimonials as the only social proof when tenured
  ones exist.
- Never bury "Do I have to subscribe?" below other FAQ questions.
- Never set an intro discount so deep that the renewal price is a shock; the
  gap is visible on the page.
- Never require payment details for a "free" first box without stating the
  conversion date and price in the CTA block.
- Never call the plan "cancel anytime" if a minimum term applies; state the
  term.

## Examples

- Seed, DS-01 Daily Synbiotic https://seed.com/daily-synbiotic : "30-day
  supply delivered monthly. Pause or cancel anytime." beside the price; the
  welcome kit framed as items rather than a discount; the FAQ answers "Do I
  have to sign up for a subscription?" head-on. Avoid its mechanism diagram
  before any human proof.
- Blue Tokai, Coffee Subscriptions https://bluetokaicoffee.com/collections/subscriptions :
  numbered benefit strip above the configurator, prepay savings that grow
  with term (6 deliveries 12.5%, 12 deliveries 17.5%), "email a day before
  every delivery, skip" microcopy. Avoid burying prepaid-only in the FAQ and
  the missing hero.
- Huel, Black Edition https://huel.com/products/huel-black-edition :
  per-meal price in the hero, intra-range comparison to prevent plan
  paralysis, taste guarantee as the risk reversal.

## Checklist

```json
{
  "page_type": "subscription",
  "aliases": ["subscribe and save page", "membership page", "auto-ship page", "plan selector page"],
  "funnel_stage": ["mof", "bof"],
  "awareness": ["product-aware"],
  "traffic": ["direct", "email", "meta", "retargeting"],
  "sections": { "min": 7, "max": 10 },
  "mandatory_sections": ["header", "hero", "plan-selector", "how-it-works", ["testimonial-spotlight", "reviews"], "guarantee", "faq", "closing-cta", "footer"],
  "recommended_sections": ["savings-math", "benefits", "features", "comparison", "sticky-cta", "legal"],
  "forbidden_sections": ["countdown", "stock-indicator", "offer-bridge", "problem", "agitation", "quiz", "final-offer", "hook"],
  "nav": "minimal",
  "price_above_fold": "required",
  "cta": { "min": 2, "max": 2, "first_after_section": 1, "sticky": "optional", "copy_pattern": "subscribe" },
  "proof": { "min_modules": 2, "max_modules": 3, "required_kinds": ["review-quote", "policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked", "stock-count"] },
  "imagery": { "required_jobs": ["identity", "included-items", "sequence"], "hero": "product-in-context", "video": "optional", "min_images": 4 },
  "copy_framework": ["bab", "fab"],
  "offer_compat": { "allowed": ["subscribe-save", "first-order", "gwp", "price-lock", "free-shipping", "loyalty", "trial-sample", "bundle", "bundle-decoy", "none"], "forbidden": ["percent-off", "fixed-off", "bogo", "flash-sale", "clearance", "mystery", "bnpl", "cashback", "limited-edition"] },
  "urgency": "none"
}
```

`cta.first_after_section` is 1 because the first button sits in the
`plan-selector` directly under the hero. `proof.required_kinds` `policy-fact`
is the cancellation path as a verifiable store policy row. `nav` may be `full`
for a permanent store page; record the override in the plan.

## Sources

- Recharge subscription trend report 2026 https://getrecharge.com/reports/subscription-trend-report-2026/ ;
  subscription landing page guide https://getrecharge.com/blog/how-to-write-the-best-subscription-landing-page/ ;
  state of subscription commerce 2022 (intro-discount churn) http://getrecharge.com/downloads/state-of-subscription-commerce-report-2022.pdf
- Zerglo, PDP conversion for subscriptions https://zerglo.com/us/blog/pdp-conversion-subscriptions
- Gourville 1998, pennies a day https://doi.org/10.1086/209517
- FTC ROSCA and negative option guidance https://www.ftc.gov/business-guidance/blog/2024/10/click-cancel-ftcs-amended-negative-option-rule-what-it-means-your-business
- UK DMCC subscription contract provisions https://cms.law/en/gbr/legal-updates/game-changing-consumer-protection-provisions-under-the-dmcc-act-come-into-force-are-you-prepared
- India CCPA Dark Patterns Guidelines 2023 https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf ;
  summary https://www.scconline.com/blog/post/2023/12/04/ccpa-notifies-guidelines-for-prevention-and-regulation-of-dark-patterns-2023-legal-news/
- Sibling references: `references/offers/offer-types.md` (subscribe-save, price-lock, first-order),
  `references/offers/offer-ledger.md`, `references/offers/price-presentation.md` (PP9),
  `references/anti-patterns/dark-patterns.md`, `references/proof/proof-ledger.md`,
  `references/assets/image-jobs-by-page-type.md`, `references/consumer-behavior-cro.md`
