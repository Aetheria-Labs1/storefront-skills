# Gift guide

A curated browsing page for people buying for someone else, organised the
way they shop: by recipient persona and by price band. There is no hard date
on the page; the guide is evergreen or refreshed each season. Visitors arrive
from "gifts for dad" searches, editorial email, social posts or the header
nav, solution-aware but undecided. The page must let a $30 shopper and a $200
shopper each find three plausible gifts in one scroll, say in one line why
each is a good gift, and hand off to the product card or quick-add.

## Identify it

Signals in the brief: "gift guide", "gifts for", "gifts under", "gift
finder"; buyer is not the recipient; several recipients or budgets; a broad
catalogue (30 to 50 products across 4 to 6 groups); no delivery cutoff and no
sale window.

Near neighbours:

- `seasonal-gifting`: the moment a delivery cutoff, a festival date or a gift
  window enters the brief, use that type (index tie-break). Research block
  22 puts a cutoff in the gift-guide hero; the index makes the cutoff the
  trigger for `seasonal-gifting`, so this file forbids `delivery-cutoff`.
- `collection-landing`: one category, filterable grid, shopper buying for
  themselves; a gift guide is grouped by recipient, not by product type.
- `bundle-kit`: one set with savings math; a guide may spotlight sets but is
  not one.
- `quiz-funnel`: a gift finder that asks questions and routes; embed a quiz
  entry here only when the catalogue exceeds about 50 SKUs.

## Anatomy

Sections between chrome: 6 to 9. Word budget 200 to 500. Products 30 to 50
in total, 6 to 8 per group.

1. `header` (mandatory). Full navigation; guide visitors browse onward.
2. `hero` (mandatory). Recipient-first headline ("Gifts for the dad who
   already owns every tool"), one-line editorial intro, optional anchor CTA
   to the first group. No cutoff, no offer.
3. `qualifier` (mandatory). The recipient and price-band selector: chips or
   tiles for "For her, For him, For kids, Under $50, Under $100"; sticky on
   scroll. RESEARCH: 61% of holiday shoppers find recipient and budget
   categories helpful and guides organised that way convert 3.0 to 5.0%
   (vendor data,
   https://www.growthsuite.net/resources/shopify-holiday-campaigns/christmas-holiday-season/gift-guide-that-converts).
4. `product-spotlight` (recommended). Three featured picks with a factual
   badge only when verified ("Best seller" from orders data, "New" from
   publish date); no "Sells out fast" without a live stock row.
5. `product-grid` (mandatory). Four to six groups, each 6 to 8 products in a
   2-column mobile grid, price visible, one line of "why it is a good gift"
   per card, rating and count when reviews exist, per-card CTA or quick-add.
   The same product may appear in more than one group. Observed: Born
   Primitive opens with best-selling gifts, then recipient groups, then
   "Gifts under $30" (internal teardown audit, 2026-09-10).
6. `product-spotlight` gift sets (conditional: sets exist). Two or three
   sets shown assembled and as separate items with a computed saving from
   the offer ledger; never a typed "worth $120".
7. `gift-options` (mandatory). Gift note, un-ticked priced wrap, gift receipt
   wording, gift returns window. This is the trust content for a guide.
8. `shipping-returns` (recommended). Standard and express options, returns
   for gifts, international notes; no dates.
9. `offer` (conditional: a verified `gwp`, `free-shipping` threshold or
   `gift-card` row exists). Gift card as the "for the person who has
   everything" group.
10. `quiz` (conditional: catalogue over 50 SKUs and a routing quiz exists).
    Gift-finder entry, three questions or fewer.
11. `faq` (recommended). Returns on gifts, wrap and note, what the recipient
    sees, exchanges for size.
12. `email-capture` (recommended). "New guides and restocks", one field, at
    the end.
13. `footer` (mandatory).

## Workflow

### Context reads
1. Merchant facts: recipient personas (four to six), price bands at round
   points, gift wrap price, note character limit, gift receipt wording,
   gift returns and exchange terms from the policy page URL. No dates: a
   cutoff retypes the page to `seasonal-gifting`
   (`references/offers/campaign-calendar.md`, gifting deltas).
2. `lexsis_catalog.list` for the candidate set (30 to 50 products): ids,
   prices, tags that map to recipients, option axes, media count. "Best
   seller" only from orders data the merchant supplies or the tool exposes;
   "New" only from the publish date. `lexsis_catalog.get` per product:
   first media item as identity, lifestyle images, variant images. Record
   products without an identity image for the merchant message.
3. `lexsis_brand.navigation` for header and footer; `lexsis_brand.brand_kit`
   for tokens, voice and banned phrases; `lexsis_brand.context` for the
   `theme_id`.
4. `lexsis_catalog.reviews_status`; above zero, `lexsis_catalog.reviews` per
   featured product for the card average and count (band B2 or higher) and
   `lexsis_catalog.reviews_search` with "bought this for", "gift" for one or
   two candidate quotes (`references/proof/reviews-sourcing.md`).
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`, one call
   each for `lifestyle`, `flat-lay`, `hero`, `banner`, `product-shot`;
   record counts per tag; then semantic "<recipient> using <category>" per
   group. View candidates with `lexsis_assets.view`
   (`references/assets/asset-sourcing-sequence.md`).
6. `lexsis_cart.get` for the cart profile (note field, wrap add-on);
   `lexsis_capture.form_schemas` for the email capture.
7. `lexsis_design.islands` for the active catalog; `lexsis_workspace.credits`
   before planning any generation (`references/assets/generation-policy.md`).

### Section by section
Media per section follows `references/workflows/section-asset-workflow.md`:
when nothing covers a slot, tell the merchant what is missing (job, aspect,
count), offer upload via `lexsis_asset_upload.upload` or generation where the
purpose is ALLOW or ASK in `references/assets/generation-policy.md`, and skip
or merge the section only when the merchant chooses; a fast draft uses the
closest existing asset or leaves the slot `planned` and lists every gap in the
plan and the draft summary. No asset is used sight unseen: every candidate is
opened with `lexsis_assets.view` and judged against the section per section 1b
of that file (subject, crop to the slot aspect, a quiet area for the copy, the
lighting and styling of the neighbouring slots, the plan's palette, no
baked-in text, watermark or overlay); candidates for one grid, set or lookbook
are viewed together so the set reads as one shoot, and a generated asset is
viewed the same way after it returns. Islands follow
`references/workflows/island-selection-workflow.md`: the lines below name the
island and the inputs; variants and props are resolved live from
`lexsis_design.island_schema`, with autoplay, hover-advance and entry motion
off unless the plan names that motion moment (N10). Copy ceilings follow
`references/copy/copy-frameworks.md` and
`references/anti-patterns/copy-anti-patterns.md`.

**`header`**
- Purpose: full navigation; guide visitors browse onward.
- Media: logo from the brand kit; a text wordmark when none.
- Island: SiteHeader when a verified shipping or returns fact fills the
  strip, else Navbar; links from `lexsis_brand.navigation`; resolve from
  `lexsis_design.island_schema`; preset `siteheader/sticky-light` or
  `navbar/sticky-light`.
- Copy: nav labels only.
- Decide with: the navigation result and the policy ledger row.

**`hero`**
- Purpose: recipient-first headline, one editorial line, optional anchor to
  the first group.
- Media: yes; job `context` (a recipient in context) or a styled flat lay of
  real products, treatment `editorial-lifestyle`, product legible
  (`references/assets/image-jobs-by-page-type.md`, section 5). Search library
  `lifestyle`, `flat-lay`, `hero`, `banner`, then catalog lifestyle media of a
  hero gift, then semantic, then merchant upload. Generation: `hero_bg`
  (ALLOW) behind a real cut-out, bold moment only. Missing: tell the merchant
  (lifestyle or flat lay, 16:9 plus 4:5, one image) and offer upload or
  `hero_bg`; if skipped, the first catalog identity image serves as a packshot
  hero with "hero pending merchant media" in the plan. No-go: a hero with no
  product in it; stock people; a cutoff or offer. View every candidate with
  `lexsis_assets.view` and run the section fit review; view it beside the
  group tiles and first cards so the page reads as one shoot.
- Island: none by default (static `<picture>`); HeroMedia only as the
  plan's full-bleed bold moment, image mode, no autoplay; resolve from
  `lexsis_design.island_schema`.
- Copy: H1 10 words or fewer naming a trait; intro 40 words; anchor CTA
  "Shop gifts under $50" (pattern `shop-collection`).
- Decide with: `lexsis_assets.view` at both crops; the group list.

**`qualifier`**
- Purpose: the recipient and price-band selector, tappable before the first
  scroll.
- Media: outside the loop as an opening text line; when the library holds one
  verified `context` image per group, the chips become four to six image tiles
  in one aspect. No-go: icon tiles, emoji, a generated illustration per
  persona. View every candidate with `lexsis_assets.view` and run the section
  fit review; view the tile images together so lighting, backgrounds and crops
  agree.
- Island: none; CSS-only tabs with radio inputs or anchor chips, sticky
  under the header on desktop (the Tabs island is deprecated).
- Copy: chip labels 3 words or fewer ("For him", "Under ₹1,000").
- Decide with: the count of viewed `lifestyle` images that match a group.

**`product-spotlight`** (recommended: three featured picks)
- Purpose: three picks with a factual badge only when verified.
- Media: yes; job `identity` per pick from catalog media, a lifestyle second
  image where one exists. Generation: none. Missing: name the pick without an
  image and offer upload; if skipped, another pick with an image takes its
  place. View every candidate with `lexsis_assets.view` and run the section
  fit review; view the set images together so lighting, backgrounds and crops
  agree.
- Island: FeaturedCollectionStage with exactly three products, or three
  cards with QuickAdd; decide from image availability and variant axes;
  badges only from ledger facts; motion off; resolve from
  `lexsis_design.island_schema`.
- Copy: one reason per pick under 15 words.
- Decide with: orders data for "Best seller"; publish date for "New".

**`product-grid`**
- Purpose: four to six groups of six to eight products, the cards as the
  CTA.
- Media: yes; job `identity` per card from catalog media, one aspect across
  the page (`references/product-grid.md`), second image on swipe where
  present. Generation: none ("needs a real photo"). Missing: list the products
  without an image and offer upload; if skipped, those cards leave and a group
  under three merges into a neighbour or becomes a text link. No-go: generated
  or stock products; groups organised by inventory category. View every
  candidate with `lexsis_assets.view` and run the section fit review; view the
  grid images together so lighting, backgrounds and crops agree.
- Island: FeaturedCollectionStage per group of three or more, or the card
  composition with QuickAdd per card; decide from group size, image
  availability and variant axes; a product may sit in two groups; motion
  off; resolve from `lexsis_design.island_schema`.
- Copy: group heading 6 words or fewer; one reason per card under 15 words;
  price or band on every card; rating and count only at 5 or more reviews.
- Decide with: `lexsis_catalog.list` prices and tags, image availability per
  product, review band per product.

**`product-spotlight`** gift sets (conditional: sets exist)
- Purpose: two or three sets shown assembled and as separate items.
- Media: yes; jobs `included-items` and `identity` from catalog media, then
  library `product-shot` or `flat-lay`, then merchant upload. Generation: none
  (identity-bound). Missing: tell the merchant (set flat lay, 1:1, one per
  set) and offer upload; fast draft shows the set image beside the component
  identity images; skip only on the merchant's call. View every candidate with
  `lexsis_assets.view` and run the section fit review; view the set images
  together so lighting, backgrounds and crops agree.
- Island: QuickAdd per set; decide from variant count; resolve from
  `lexsis_design.island_schema`.
- Copy: 30 words per set; a saving only from a computed offer-ledger row,
  never a typed "worth $120".
- Decide with: set SKUs in the catalog and the ledger savings row.

**`gift-options`**
- Purpose: note, un-ticked priced wrap, gift receipt wording, gift returns.
- Media: yes; job `gift-presentation` (the real wrap, box or card that ships).
  Search catalog media of the wrap SKU, then library `product-shot` and
  `lifestyle`, then semantic "<brand> gift wrap box", then merchant upload.
  Generation: none (GP13). Missing: tell the merchant (a photo of what ships,
  1:1 or 4:5, one image) and offer upload; if skipped, the note and wrap
  controls stay as the section's object and production-ready approval waits
  (the job is required for this type). No-go: stock boxes, ribbon
  illustrations, icon rows. View every candidate with `lexsis_assets.view` and
  run the section fit review before use.
- Island: note field and wrap add-on from the cart profile
  (`lexsis_cart.get`, `head.use_cart_v2`); QuickAdd on the wrap SKU when
  wrap is a product; resolve from `lexsis_design.island_schema`. Nothing
  pre-ticked (`references/anti-patterns/dark-patterns.md`).
- Copy: label with character limit, wrap price beside the control, "Gift
  receipt hides prices", "Free exchanges within 30 days"; four lines.
- Decide with: cart profile flags and the policy URL.

**`shipping-returns`** (recommended)
- Purpose: standard and express options, gift returns, international notes;
  no dates.
- Media: no (stands without an image per the asset workflow).
- Island: none; DeliveryEstimate is not used because it renders dates and
  a guide carries none.
- Copy: one line per option with its price, returns window, five lines.
- Decide with: the policy URL.

**`offer`** (conditional: verified `gwp`, `free-shipping` or `gift-card`
row)
- Purpose: the gift card as "for the person who has everything".
- Media: yes; job `identity` of the gift-card product or the GWP item from
  catalog media. Generation: none. Missing: offer upload; if skipped, the
  offer is one line beside the last group. View every candidate with
  `lexsis_assets.view` and run the section fit review before use.
- Island: QuickAdd on the gift-card product; none for a threshold line;
  resolve from `lexsis_design.island_schema`.
- Copy: one sentence, 25 words, no percentage pill (N9).
- Decide with: the offer-ledger row.

**`quiz`** (conditional: over 50 SKUs and a routing quiz exists)
- Purpose: a gift-finder entry, three questions or fewer.
- Media: yes; one `context` image beside the entry from library `lifestyle`.
  Generation: none. Missing: offer upload; if skipped, the entry is a single
  button inside the `qualifier` chips. View every candidate with
  `lexsis_assets.view` and run the section fit review before use.
- Island: FunnelRuntime with a published funnel from
  `lexsis_capture.funnel_templates`, validated with
  `lexsis_capture.validate_funnel`; resolve from
  `lexsis_design.island_schema`.
- Copy: one line and one CTA "Find a gift".
- Decide with: SKU count and an existing funnel template.

**`faq`** (recommended)
- Purpose: returns on gifts, wrap and note, what the recipient sees,
  exchanges for size.
- Media: no.
- Island: none; native `<details>` and `<summary>` (the FAQ island is
  deprecated).
- Copy: four to six questions, answer first, 60 words each.
- Decide with: support data and the policy ledger rows.

**`email-capture`** (recommended)
- Purpose: new guides and restocks, one field, at the end.
- Media: a set or hero image beside the form; the form alone is the object
  when no image is spare (N8).
- Island: EmailCapture, one per page, or the Footer newsletter layout; no
  incentive without a `first-order` row; resolve from
  `lexsis_design.island_schema`; preset `footer/newsletter-split-light` in
  the footer case.
- Copy: one line and one field.
- Decide with: `lexsis_capture.form_schemas` and the offer ledger.

**`footer`**
- Purpose: policies, contact, social.
- Media: logo only.
- Island: Footer with columns from `lexsis_brand.navigation`; resolve from
  `lexsis_design.island_schema`; preset `footer/columns-dark`.
- Decide with: the navigation result.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` per card, set images, wrap SKU image | `context` per recipient group, `gift-presentation`, `included-items` flat lay | reuse a product lifestyle shot as the group tile; generate `hero_bg` (ALLOW) or `product_composite` for `context` (ALLOW over a real cut-out); ask the merchant to upload the wrap photo and flat lays; text chips instead of tiles only on the merchant's call |
| asset library | `lifestyle` and `flat-lay` hero candidates, `product-shot` duplicates | one lifestyle image per persona, unboxing UGC with rights | semantic query per group, then ask the merchant to upload; UGC only with a ledger row; skip only on the merchant's call |
| generation | backdrops, textures, composites only | product, people, results, logos, text | never; these are "needs a real photo" in the merchant message |

With minimal assets the page is a header, a flat-lay hero of real products,
text chips, four groups of real catalog cards with prices, the gift options
with the merchant's wrap photo, an email field and a footer; at most one
generated asset (`hero_bg`), never more than four per page, and every missing
asset listed in the plan and the draft summary with upload, generate or skip.
Every asset, found or generated, was viewed and passed the section fit review
before use.

## Above the fold (390px)

In order: compact header; recipient-first H1; one-line intro; the `qualifier`
chips for recipient and price band; the first featured pick or first grid row
starting. The shopper should be able to tap a price band before scrolling.

Must not appear: a countdown, a cutoff date, a discount pill, a popup,
exact-price headlines in an evergreen guide (use bands), a hero image with no
product in it.

## Proof

Modules: 1 to 2. Proof is light; the guide sells through curation and the
safety of returns.

- `policy-fact` (required): gift returns window, gift receipt behaviour,
  exchange terms; source is the policy page URL
  (`references/proof/proof-ledger.md`).
- `review-summary` on cards (when a product has 5 or more reviews); never
  stars without a count.
- `review-quote` (optional): one or two verbatim quotes that mention giving
  ("bought this for my brother"), dated, placed beside the relevant group.
- Never: `social-proof-popup`, `live-viewer-count`, `stock-count` in static
  copy, `press-logo-unlinked`, gift counts without a ledger row.

Zero-review store: policy facts only; no review-shaped element
(`references/proof/reviews-sourcing.md`).

## Offer and CTA

- CTAs: the cards are the CTA. At most one standalone CTA, an anchor in the
  hero to the first group ("Shop gifts under $50", pattern
  `shop-collection`). No sticky CTA button; a sticky `qualifier` bar
  replaces it.
- Price reveal: price or price band on every card; bands rather than exact
  prices in evergreen headlines so the guide does not go stale.
- Urgency: none. A guide has no window; a window makes it `seasonal-gifting`.
- Offer types that fit: `none`, `gwp`, `free-shipping` threshold,
  `gift-card`, `bundle` sets with computed savings, `bnpl` and `cashback`
  lines for India, `limited-edition`, `loyalty`.
- Offer types that do not fit: `percent-off` and `fixed-off` (a discounted
  window is `seasonal-gifting`; an evergreen strike-through is illegal in
  the UK and trains waiting, campaign-calendar CC9), `flash-sale`,
  `clearance`, `bogo`, `subscribe-save`, `referral`, `trial-sample`,
  `mystery`, `pre-order-price`, `price-lock`, `student-military`,
  `tiered-volume`.
- Gift wrap ($3 to $8) and card ($2 to $5) are un-ticked add-ons with the
  price beside them (LAW: pre-selection is basket sneaking under the UK DMCC
  Act, EU UCPD guidance and India CCPA dark-pattern guidelines,
  internal research audit (2026-09-10) section 1).

## Imagery

Required jobs: `identity` per product (catalog media) and `gift-presentation`
(the real wrap, box or card the store ships). Recommended: `context`
(recipient-in-context lifestyle per group), `packaging`, `in-use`, `scale`.

Hero treatment: `editorial-lifestyle`, a recipient in context or a styled
flat lay of real products; product legible. Sets are shown assembled and as
separate items. Video optional. Minimum 8 image slots. Plan slots: hero, one
gift-presentation, one context image per group where the library has one,
card images from the catalog. Consistent aspect ratio across all cards
(`references/product-grid.md`).

## Copy

Framework: listicle numbering across groups is optional; FAB micro-copy on
cards. Recipient-first headlines that name a trait, not a demographic alone.

- H1 10 words or fewer; group headings 6 words or fewer ("For the early
  riser", "Under ₹1,000").
- One reason per card, under 15 words, concrete ("Fits a 13-inch laptop and
  a water bottle"), never "perfect for anyone".
- Reading level grade 6 to 8; intro under 40 words.
- Vocabulary: "gift receipt hides prices", "free exchanges within 30 days";
  no "must-have", "ultimate", "treat yourself" in a giving context.
- Mine gift-related reviews for phrasing before writing
  (internal teardown audit, 2026-09-10).

## Never

- Never add a delivery cutoff or festival date; retype to `seasonal-gifting`.
- Never blend three axes in one group ("for the home baker under $50 who
  loves vintage"); one axis per group.
- Never organise groups by inventory category ("Mugs", "Candles"); organise
  by recipient or budget.
- Never omit a price filter or band; a $30 shopper will not scroll past $200
  items.
- Never exceed about 50 products; a guide is curation, not the catalogue.
- Never use exact prices in evergreen headlines.
- Never pre-tick wrap or a card.
- Never badge "Sells out fast" or "Top pick" without a verified basis.
- Never restrict a product to one group when it fits several.
- Never write "guaranteed to delight" or promise a reaction.

## Examples

- Born Primitive men's gift guide,
  https://bornprimitive.com/pages/mens-gift-guide: best-selling gifts first,
  recipient groups, "Gifts under $30", e-gift cards as the fallback group.
- Sea Bags holiday gift guide, https://seabags.com/pages/holiday-gift-guide:
  clean price-band groups and a gift-card section; it also carries cutoff
  dates, which makes it `seasonal-gifting` under the index tie-break.
- Shopify's gift guide roundup (Gymshark by activity and price, Chubbies by
  humour persona, Mejuri bundles),
  https://www.shopify.com/blog/holiday-gift-guide: recipient and price-band
  grouping patterns with product-first imagery.

## Checklist

```json
{
  "page_type": "gift-guide",
  "aliases": ["gifts for", "gifts under", "gift finder", "gifting hub", "holiday gift guide"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["solution-aware"],
  "traffic": ["organic", "google-search", "email", "meta"],
  "sections": { "min": 6, "max": 9 },
  "mandatory_sections": ["header", "hero", "qualifier", "product-grid", "gift-options", "footer"],
  "recommended_sections": ["product-spotlight", "shipping-returns", "faq", "email-capture", "offer"],
  "forbidden_sections": ["delivery-cutoff", "countdown", "stock-indicator", "buy-box", "dateline", "hook", "agitation", "offer-bridge", "savings-math"],
  "nav": "full",
  "price_above_fold": "optional",
  "cta": { "min": 0, "max": 1, "first_after_section": 0, "sticky": "forbidden", "copy_pattern": "shop-collection" },
  "proof": { "min_modules": 1, "max_modules": 2, "required_kinds": ["policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "stock-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "gift-presentation"], "hero": "editorial-lifestyle", "video": "optional", "min_images": 8 },
  "copy_framework": ["listicle", "fab"],
  "offer_compat": { "allowed": ["none", "gwp", "free-shipping", "gift-card", "bundle", "bnpl", "cashback", "limited-edition", "loyalty"], "forbidden": ["percent-off", "fixed-off", "flash-sale", "clearance", "bogo", "subscribe-save", "referral", "trial-sample", "mystery", "pre-order-price", "price-lock", "student-military", "tiered-volume"] },
  "urgency": "none"
}
```

## Sources

- internal research audit (2026-09-10) section 5 block 22; section 2 row 22.
- internal research audit (2026-09-10) teardown 39 and Part D (Born Primitive partial).
- internal research audit (2026-09-10) sections 4.3 (gift guide anatomy) and 7.
- internal research audit (2026-09-10) section 13 (gifting row).
- internal research audit (2026-09-10) section 1.1.
- `references/offers/campaign-calendar.md` gifting anatomy deltas, CC9, CC12.
- Shopify gift guide: https://www.shopify.com/blog/holiday-gift-guide
- Growthsuite gift guide conversion: https://www.growthsuite.net/resources/shopify-holiday-campaigns/christmas-holiday-season/gift-guide-that-converts
- identixweb: https://www.identixweb.com/how-to-build-shopify-gift-guides/
- shelfy gift guide types: https://www.shelfy.today/blog/types-of-gift-guides
- ecommerce-today: https://ecommerce-today.com/holiday-gift-guide-for-shopify-stores-what-it-is-why-it-works-and-how-to-implement-it-step-by-step/
- Dark-pattern frame (pre-ticked add-ons): https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf
