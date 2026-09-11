# Restock page

A product that sold out is available again, and the page converts the demand
that built up while it was gone. Shoppers arrive most-aware from a
back-in-stock email, SMS or push with a specific variant in mind; their job is
to confirm the variant is there and add it to cart in two taps. When a variant
is still out, the add-to-cart position holds a variant-specific alert form
instead of a greyed button. No education, no markdown; the reviews that
accumulated during the stock-out carry the proof.

## Identify it

- Brief says "restock", "back in stock", "it's back", "notify me", "sold
  out", or a hero SKU with recurring stock-outs and a waitlist.
- The product has sold before and has review data (index tie-break against
  `launch-waitlist-preorder`).
- Traffic is the merchant's own list; awareness is most-aware; stage is bof
  or retention.
- Near neighbours:
  - `launch-waitlist-preorder`: the product has never shipped; no reviews
    exist; choose launch.
  - `pdp`: the ordinary product page; choose restock when the page's reason
    to exist is the return of stock and the traffic is a restock send.
  - `offer-page`: a discount is the message; a restock needs no discount.
  - `retargeting-warm`: the visitor saw it and left; choose retargeting when
    objections, not availability, stopped them.

## Variants

- **Restock landing** (email or SMS destination). Product hero with the
  variant pre-selected from the link, "back in stock" stated plainly, price
  unchanged, live availability per variant, reviews, one CTA.
- **Sold-out state** (the product is still out, or one variant is). The
  add-to-cart slot holds a `waitlist-form` of the same size and position with
  the variant selector above it; reviews and product content stay below
  because the page still has to sell the wait. OPERATOR: replacing the greyed
  button with the form enrolled 22 to 38% of sold-out visitors vs 4 to 8% for
  a footer link https://ustechautomations.com/resources/blog/ecommerce-back-in-stock-notifications-how-to-2026 .
- **Capped restock.** A documented unit count ("Restocked: 400 units")
  rendered as `limited-edition` with a stopping counter and a persistent sold
  out state; no "only N left" in copy.
- **Members-first window.** The waitlist gets a stated early-access window
  before public listing; rendered as `loyalty`, terms stated.

## Anatomy

Counts exclude chrome. Order follows the back-in-stock guidance in
internal research audit (2026-09-10) type 12 and the Snitch and Salt of
the Earth sold-out patterns in internal research audit (2026-09-10).

1. `announcement`: conditional: a verified free-shipping threshold or
   early-access window. Never a countdown.
2. `header`: mandatory, minimal.
3. `product-hero`: mandatory. "Back in stock" as a plain statement, product
   packshot, `review-summary` with count, price unchanged (state "same price"
   only when true), the variant the link named already selected.
4. `buy-box`: mandatory. Variant options as buttons with live availability
   inline (sold-out sizes labelled, not hidden), quantity, add to cart,
   shipping and returns line. When the selected variant is still out, the add
   to cart position holds the `waitlist-form` for that variant.
5. `stock-indicator`: conditional: live inventory binding and a low count on
   a tracked variant. "12 left in size M" beside the picker, conservative
   threshold, disappears on replenish. Never on made-to-order stock.
6. `reviews`: mandatory. Prior reviews with distribution at 20 or more,
   dated, at least one critical review reachable. This is why the type exists.
7. `stats`: conditional: verified prior sell-out fact or waitlist size from
   an export ("Sold out in 9 hours in July"; "Over 2,400 people asked to be
   notified"). Rounded down, "over N", dated.
8. `waitlist-form`: conditional: any variant is still out. Variant-specific
   email with optional SMS consent (un-ticked), estimated restock date only
   when the merchant has a basis. OPERATOR: variant-specific alerts converted
   41% higher than product-level (RetailDive via ustech, same URL); an
   estimated date lifted sign-ups 18% (same).
9. `trust-bar` or `shipping-returns`: recommended. Returns window, dispatch
   cutoff for same-day, shipping threshold.
10. `cross-sell`: optional: a named relationship ("Meanwhile, the compatible
    replacement", "Complete the routine") for visitors whose variant is still
    out; two items at most.
11. `closing-cta`: mandatory. Add to cart (or the alert form) repeated with
    the variant state.
12. `footer`: mandatory chrome.

Never include `problem`, `agitation`, `mechanism`, `story`, `comparison`,
`quiz` or `countdown`. The visitor asked for this product by name.

## Workflow

Assets first: the exact variant the shopper asked for is shown before
anything is written. A section that would end up as a colour band, an emoji
row, icon tiles or a wall of text is rebuilt around imagery or, on the
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

1. `lexsis_catalog.get`: variants with live inventory per variant (which are
   back, which are still out), per-variant images (the `variation` job, so
   the gallery swaps on selection), `media[]` mapped per
   `references/assets/image-jobs-by-page-type.md` (identity, detail, in-use),
   price now versus the price before the stock-out ("same price" only when
   true), selling plans (subscribe-save for replenishables), the variant named
   in the send's deep link.
2. `lexsis_catalog.reviews_status`; `lexsis_catalog.reviews` with `product_id`
   (n, average, newest date, `has_media`). With zero reviews the page is not
   this type: route to `launch-waitlist-preorder`. `review_collections` with
   `collection_status: "active"`; bands per `references/proof/reviews-sourcing.md`.
3. Proof ledger: the prior sell-out fact or waitlist size from a merchant
   export, dated, rounded down (`sales-count`, `customer-count`); an estimated
   restock date for still-out variants only with a stated basis.
4. `lexsis_brand.context`, `lexsis_brand.brand_kit`, `lexsis_brand.navigation`
   (minimal nav).
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"` for
   `product-shot` (variant cut-outs), `social-proof` (rights-cleared UGC of
   this product); no lifestyle expansion. Sequence and checks:
   `references/assets/asset-sourcing-sequence.md`.
6. `lexsis_cart.get`: cart v2, threshold. `lexsis_design.islands`, then
   `lexsis_design.island_schema` for each island named below. No generation is
   planned on this type: the hero is a `packshot` and every job is
   identity-bound.

### Section by section

No asset is used sight unseen: open every candidate with `lexsis_assets.view`
and run the section 1b fit review in `references/workflows/section-asset-workflow.md`
before use (subject does the job, crops to the slot without losing the product,
quiet area for the copy, lighting and styling match neighbouring slots, palette,
no baked-in text or watermark); view a section's or gallery's candidates
together so the set reads as one shoot, and view a generated asset the same way
after it returns.

**`announcement`**
- Purpose: a verified free-shipping threshold or early-access window; never a countdown.
- Media: none.
- Island: AnnouncementBar or the SiteHeader strip, one message; resolve from `lexsis_design.island_schema`; preset `announcementbar/static-dark`. Omit without a ledger row.
- Copy: under 60 characters; "Waitlist access until Friday 6pm IST" states the window's end.
- Decide with: `lexsis_cart.get`; a `loyalty` ledger row for the window (`references/offers/offer-types.md`).

**`header`**
- Purpose: minimal chrome.
- Media: brand logo or wordmark. View every candidate with `lexsis_assets.view` and run the section fit review (section 1b of `references/workflows/section-asset-workflow.md`) before use.
- Island: SiteHeader minimal with the CTA anchoring to the buy box; resolve from `lexsis_design.island_schema`; preset `siteheader/minimal-light`.
- Copy: store names.
- Decide with: `lexsis_brand.navigation`.

**`product-hero`**
- Purpose: "Back in stock" stated plainly, the packshot of the linked variant, review summary, price.
- Media: yes, identity of the selected variant (`packshot`; alternate `product-in-hand`) and variation per variant from the variant-to-media mapping; detail when the catalog has it; catalog media, library `product-shot`, merchant upload, supplier for the exact SKU. Never a lifestyle hero, never stock, never generated (GN1). A variant with no image: tell the merchant (variation, square, one per variant); offer upload; the product-level identity shows meanwhile and the slot stays `planned`. View the candidates together with `lexsis_assets.view` and run the section fit review so the set reads as one shoot, not a pile of found images. View the image to confirm it is the restocked variant, not a sibling colour or size.
- Island: ProductGallery; decide layout from the image count (one or two: stacked, no thumbnails; three or more: main image with a thumbnail rail and swipe on mobile), variant sync on whenever per-variant images exist, contain fit for packshots on white, no autoplay (N10); ProductHero in a split layout for a premium product with three or more images. Resolve from `lexsis_design.island_schema`; preset `productgallery/rail-bottom-light` or `producthero/split-rail-light`. The statement, title and review summary are HTML beside it.
- Copy: statement 8 words ("The Field Jacket is back in stock."); sub-line "Same price. 412 reviews." only when both are true; vocabulary per `references/anti-patterns/copy-anti-patterns.md`.
- Decide with: `media[]` count and variant images; review band; the price check.

**`buy-box`**
- Purpose: variant buttons with live availability inline, quantity, add to cart, shipping and returns line; the alert form in the add position for a still-out variant.
- Media: swatch images per colour variant from catalog; no other imagery (the block is a form). Missing swatches: tell the merchant per variant; offer upload; not generated. View the candidates together with `lexsis_assets.view` and run the section fit review so the set reads as one shoot, not a pile of found images.
- Island: BuyBox with live availability per variant and the deep-linked variant pre-selected; VariantSwatches for a colour axis that carries images (BuyBox variants carry no image) and for a size grid with sold-out sizes labelled inline, never hidden; the BuyBox notify state in the CTA position for a still-out selected variant; EmailCapture replacing the BuyBox in the same position when the whole product is still out; SubscriptionToggle with one-time default only for replenishables with selling plans; never a discount, never QuantityBreaks. Resolve from `lexsis_design.island_schema`; preset `buybox/default-light`.
- Copy: "Size M: 12 left", "Size XL: notify me" inline; two microcopy lines (shipping, returns, dispatch cutoff).
- Decide with: per-variant inventory and images; the deep-link variant; cart v2.

**`stock-indicator`**
- Purpose: "12 left in size M" beside the picker, live only.
- Media: none.
- Island: InventoryIndicator in its inline text form bound to the selected variant, conservative threshold, disappearing on replenish; never on made-to-order stock; a documented cap uses the bar form; resolve from `lexsis_design.island_schema`; preset `inventoryindicator/text-quiet` or `inventoryindicator/bar-accent`.
- Copy: island-rendered; no "only N left" in page copy (`urgency-scarcity.md` UR3, UR12).
- Decide with: `offer.stockVerified`; a `limited-edition` ledger row for a cap.

**`reviews`**
- Purpose: the proof that accumulated during the stock-out; this is why the type exists.
- Media: review photos and videos from the records (`has_media`); avatars real or CSS initials. View every candidate with `lexsis_assets.view` and run the section fit review before use.
- Island: by band per `references/proof/reviews-sourcing.md`: B1 static verbatim dated cards, no average; B2 ReviewCarousel showing all cards, autoplay off (N10), bound to the product id or an active collection; B3 or more ReviewList with distribution filters, media and recent sort, one review of 3 stars or lower reachable. Never an endpoint prop. Resolve from `lexsis_design.island_schema`; preset `reviewcarousel/grid-flat` when it fits.
- Copy: island-rendered; one line disclosing the sort.
- Decide with: band from step 2.

**`stats`**
- Purpose: a verified prior sell-out fact or waitlist size.
- Media: none; one line of text under the hero or beside the reviews h2.
- Island: none (StatCards is deprecated; static HTML figures only from the proof ledger, no counters, N10).
- Copy: 12 words, rounded down, "over N", dated ("Sold out in 9 hours in July").
- Decide with: the export in the proof ledger (`sales-count`, `customer-count`).

**`waitlist-form`**
- Purpose: variant-specific alert for any variant still out.
- Media: the variant's identity image beside the form; no new asset.
- Island: EmailCapture in compact form, one per out variant, labelled "Notify me when [variant] is back"; SMS consent, if offered, is a separate un-ticked HTML checkbox (the island has no consent field); resolve from `lexsis_design.island_schema`.
- Copy: 20 words of microcopy: "One email when it is back. No marketing unless you tick the box."; an estimated date only with a basis.
- Decide with: variants with zero inventory; restock date basis from step 3.

**`trust-bar`** or **`shipping-returns`**
- Purpose: returns window, dispatch cutoff, shipping threshold.
- Media: none; text facts with the page's single icon set or none.
- Island: DeliveryEstimate for single-zone domestic dispatch ("Order by 2pm IST for same-day dispatch"), else none; resolve from `lexsis_design.island_schema`; preset `deliveryestimate/inline-quiet`.
- Copy: 40 words.
- Decide with: `policy-fact` rows; shipping zones.

**`cross-sell`**
- Purpose: "Meanwhile, the compatible replacement" for visitors whose variant is still out; two items at most.
- Media: yes, one identity image per item from its own `lexsis_catalog.get`; an item without an image: tell the merchant, offer upload, leave it out until then. View the candidates together with `lexsis_assets.view` and run the section fit review so the set reads as one shoot, not a pile of found images.
- Island: ProductCarousel in compact row form, quick add off, animation off (N10), shown only when a variant is still out; resolve from `lexsis_design.island_schema`; preset `productcarousel/rows-compact`.
- Copy: the relationship name as the h2; one line per item (18 words).
- Decide with: a real relationship in the catalog; out variants present.

**`closing-cta`** and **`sticky-cta`**
- Purpose: add to cart (or the alert form) repeated with the variant state; a bar with variant and price.
- Media: product thumbnail from catalog position 1 for the bar. View every candidate with `lexsis_assets.view` and run the section fit review before use.
- Island: the closing CTA is an anchor to the buy box (one BuyBox per page) or a second EmailCapture for the out variant. StickyBar in product mode only when the selected variant is in stock and the page runs past about three mobile screens; the schema has no notify state, so a still-out product gets no bar; resolve from `lexsis_design.island_schema`; preset `stickybar/product-light`.
- Copy: the label carries variant and price.
- Decide with: variant availability; page length.

**`footer`**
- Purpose: chrome.
- Media: brand logo. View every candidate with `lexsis_assets.view` and run the section fit review before use.
- Island: Footer; preset `footer/simple-light`.
- Copy: the store's.
- Decide with: `lexsis_brand.navigation`.

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | identity of the product, variant images for most colours, a detail shot | an image for a new or rarely photographed variant, in-use | reuse the product-level identity meanwhile with a `planned` variation slot; ask the merchant to upload the variant shot; review photos supply in-use when they exist |
| asset library | `product-shot` cut-outs, `social-proof` UGC with a `P` row | in-use without rights | ask the merchant to upload or to supply the rights record; no UGC without one |
| generation | nothing on this type (every job is identity-bound and the hero is a `packshot`) | product, variants, people, stock counts, text | never |

Minimal assets (one packshot): a stacked gallery, the buy box with live availability, reviews by band, shipping and returns, the alert form for out variants, closing CTA; missing variant images are listed in the plan and draft summary, and cross-sell and stats wait for a real relationship or an export. Generated assets on a restock page: zero. Every asset, generated ones included, is opened with `lexsis_assets.view` and passes the fit review in `references/workflows/section-asset-workflow.md` section 1b before it ships; a paid render earns no exemption.

## Above the fold (390px)

In order: header, "Back in stock" statement and product name, packshot of the
selected variant (no more than 60% of viewport height), review summary with
count, price, the variant row with live availability, add to cart (or the
alert form for a still-out variant). Not above the fold: a countdown, a
discount, "N people viewing", a cross-sell, an email popup over the buy box.

## Proof

- Modules: 1 to 2. Module one is `review-summary` in the hero. Module two is
  `reviews` (the list) or `stats` as `sales-count` or `customer-count` from a
  merchant export (prior sell-out time, waitlist size).
- The proof already exists; the page does not manufacture more. A verified
  "sold out in 9 hours" line is `sales-count`; a waitlist figure is
  `customer-count`; both need the export and date in the ledger, rounded down.
- `stock-count` only from a live binding (`proof-ledger.md`). Cart velocity
  ("21,100+ added to cart past week") is not renderable; it is unverifiable by
  the shopper and reads as `live-viewer-count`.
- No reviews: the product should not be this type; route to
  `launch-waitlist-preorder`. If reviews exist but are under 5, show the
  individual cards and "n reviews" with no average.

## Offer and CTA

- CTA count: 2. Add to cart in the buy box (or the alert form when out) and
  the closing repeat. The alert form counts as the CTA for its variant.
- First CTA position: buy box, section index 0 of the body.
- Sticky: optional; carries variant and price; opens the picker when none is
  chosen; switches to "Notify me" for an out variant.
- CTA copy: "Add to cart"; for the alert, "Notify me when [variant] is back";
  for members-first, "Get first access". Never "Buy Now", "Hurry".
- Price reveal: immediate, unchanged from the PDP. No discount is needed:
  OPERATOR, back-in-stock messages convert 12 to 25%, and 25% when sent within
  15 minutes of the restock vs 10% after four hours
  https://ustechautomations.com/resources/blog/ecommerce-back-in-stock-notifications-how-to-2026 ;
  a small incentive belongs in the third message to hesitators, not on the
  page (GOSH https://www.goshdigital.co/blog/klaviyo-back-in-stock ).
- Deep link: the send carries the variant so the page opens with it selected
  (saves two taps; OPERATOR +18%, same ustech source).
- Urgency: verified only. A live `stock-indicator` per variant, a documented
  cap, or a dispatch cutoff ("Order by 2pm IST for same-day dispatch"). No
  countdown: a restock has no end date. No "only N left" in copy; no "N
  people are waiting" unless it is the ledgered `customer-count`.
- Early access: a real window for waitlisters before public listing, stated
  with its end (OPERATOR +34%, same ustech source), rendered as `loyalty`.
- Offers that fit: `none` (default), `free-shipping`, `subscribe-save`
  (replenishables; one-time selected by default, both prices visible),
  `loyalty` (early access), `limited-edition` (documented cap).
- Offers that do not fit: `percent-off`, `fixed-off`, `bogo`, `first-order`,
  `flash-sale`, `clearance`, `mystery`, `pre-order-price`, `referral`,
  `trial-sample`, `gift-card`. A discounted restock trains the list to wait
  for the next one and undercuts the buyers who paid full price before the
  stock-out.

## Imagery

- Required jobs: `identity` (the selected variant's packshot); `variation`
  when variants exist, so the gallery swaps with the selection. Recommended:
  `detail`, `in-use` or `ugc` when rights exist, `swatch` for colour
  variants.
- Hero: `packshot`; alternate `product-in-hand`. Never an editorial lifestyle
  hero; the visitor knows the product and wants to see the exact variant.
- Minimum images: 3 (identity, variation when variants exist, one in-use or
  UGC image). Reviews with photos may supply the third.
- Balance: studio-led. No lifestyle expansion sections.
- Video: optional as a gallery thumbnail only; never autoplay with sound.
- Slots the plan creates: a `variation` slot for any variant lacking its own
  image; never a generated identity image.

## Copy

- Framework: `aida` compressed to the direct offer (`_index.md` section 5,
  most-aware): the product is back, here is the variant, add to cart.
- Headline: `[Product] is back in stock.` or `[Product], back in [colour or
  size].` Sub-line: "Same price. [n] reviews." only when both are true.
- Reading level grade 6 to 8; 100 to 250 words outside reviews.
- Length ceilings: hero statement 8 words; sub-line 14 words; stats line 12
  words; alert form microcopy 20 words; shipping and returns 40 words.
- Vocabulary: "back in stock", "restocked [date]"; plain availability
  ("Size M: 12 left", "Size XL: notify me"); "expected to ship [date]" for
  any estimated restock. Never "Hurry", "Selling fast", "Almost gone",
  "Don't miss out again", "Last chance", exclamation marks, ALL CAPS.
- Microcopy under the CTA: shipping cost or threshold, returns window,
  dispatch cutoff. Under the alert form: "One email when it is back. No
  marketing unless you tick the box."

## Never

- Never leave a greyed add to cart with no alert form when a variant is out.
- Never capture alerts at product level when the product has variants.
- Never show a discount on a restock page.
- Never render a countdown; a restock has no end date.
- Never show "only N left", "N people waiting" or "N added to cart this
  week" from static copy or analytics not in the ledger.
- Never hide sold-out variants; label them inline and offer the alert.
- Never re-educate: no problem, mechanism or comparison sections.
- Never state "same price" when the price changed.
- Never claim an estimated restock date the merchant has no basis for.
- Never pre-tick the SMS consent on the alert form.
- Never send the restock link to a generic PDP without the variant
  pre-selected.
- Never let the page outlive the stock: when it sells out again, the alert
  form returns automatically.

## Examples

- Salt of the Earth, Build Your Electrolyte Bundle
  https://drinksote.com/pages/sote-bundle-builder : sold-out flavours stay in
  the grid with a "Notify me" control in the add position instead of a greyed
  stepper.
- Snitch, Graphic Lines Black Shirt https://www.snitch.co.in/products/graphic-lines-black-shirt :
  sold-out sizes labelled inline in the size selector rather than hidden; the
  model's height and size worn stated for fit. Avoid its stacked promo bars
  and near-absent proof.
- RealGreek jacket restock (GOSH Digital case)
  https://www.goshdigital.co/blog/klaviyo-back-in-stock : one email to 2,400
  waitlisters produced $87k in 48 hours with no discount; the page opened on
  the product with reviews intact.

## Checklist

```json
{
  "page_type": "restock",
  "aliases": ["back in stock page", "notify me page", "restock landing", "sold-out PDP state"],
  "funnel_stage": ["bof", "retention"],
  "awareness": ["most-aware"],
  "traffic": ["email", "sms"],
  "sections": { "min": 5, "max": 7 },
  "mandatory_sections": ["header", "product-hero", "buy-box", "reviews", "closing-cta", "footer"],
  "recommended_sections": [["trust-bar", "shipping-returns"], "stats", "waitlist-form", "stock-indicator", "sticky-cta"],
  "forbidden_sections": ["countdown", "problem", "agitation", "mechanism", "story", "comparison", "quiz", "offer-bridge", "final-offer", "savings-math", "hook"],
  "nav": "minimal",
  "price_above_fold": "required",
  "cta": { "min": 2, "max": 2, "first_after_section": 0, "sticky": "optional", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 1, "max_modules": 2, "required_kinds": ["review-summary"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity"], "hero": "packshot", "video": "optional", "min_images": 3 },
  "copy_framework": ["aida"],
  "offer_compat": { "allowed": ["none", "free-shipping", "subscribe-save", "loyalty", "limited-edition"], "forbidden": ["percent-off", "fixed-off", "bogo", "first-order", "flash-sale", "clearance", "mystery", "pre-order-price", "referral", "trial-sample", "gift-card"] },
  "urgency": "verified-only"
}
```

`waitlist-form` and `stock-indicator` are conditional on a still-out variant
and a live inventory binding respectively; `plan_lint.py` T10 requires
`offer.stockVerified` for the indicator. `variation` becomes a required job
when variants exist. `cta.copy_pattern` is `add-to-cart`; the alert form's
label follows the `join-waitlist` shape for the out variant.

## Sources

- Back-in-stock notification research and benchmarks https://ustechautomations.com/resources/blog/ecommerce-back-in-stock-notifications-how-to-2026
- GOSH Digital, Klaviyo back in stock (RealGreek case) https://www.goshdigital.co/blog/klaviyo-back-in-stock
- Attentive, Back in Stock Waitlist https://help.attentive.com/hc/en-us/articles/17145192481172-Back-in-Stock-Waitlist-overview
- Poptin, back-in-stock popups and waitlists https://www.poptin.com/blog/back-in-stock-email-popups-waitlists/
- Shopper-side view of notify-me https://pagecrawl.io/blog/notify-me-when-back-in-stock
- Restock campaign rules: internal research audit (2026-09-10) section 4.2 ;
  SMS conversion benchmarks https://conversion.studio/blog/sms-marketing-benchmarks
- Urgency law: UK CMA unfair commercial practices https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices ;
  India CCPA Dark Patterns 2023 https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf
- Sibling references: `references/offers/urgency-scarcity.md` (UR1, UR3, UR9, UR12),
  `references/offers/offer-types.md` (limited-edition, loyalty, subscribe-save),
  `references/proof/proof-ledger.md`, `references/proof/reviews-sourcing.md`,
  `references/assets/image-jobs-by-page-type.md`, `references/design-rules.md` (A8, N9)
