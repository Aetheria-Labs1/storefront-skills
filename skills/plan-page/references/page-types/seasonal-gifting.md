# Seasonal gifting

An occasion assortment with a hard purchase window: the visitor is buying for
someone else before a date (Valentine's Day, Mother's Day, Raksha Bandhan,
Diwali, Christmas, BFCM gifting). They land from email, SMS, occasion-creative
social ads or "gifts for" searches, already intending to buy. The page must
tell them what will arrive in time, help them choose by recipient or price
band, let them add a note and wrap, and get them to a card CTA or the cart
without a detour. Delivery confidence, not discount depth, is the conversion
lever (OPERATOR: CustomFit.ai festive CRO,
https://www.customfit.ai/blog/d2c-ecommerce/ecommerce-holiday-optimization-festive).

## Identify it

Signals in the brief: a named occasion or festival with a date; buyer is not
the user ("for mom", "for my sister"); shipping deadlines matter; 1 to 30
SKUs framed by the occasion; gift wrap, gift note or gift receipt mentioned;
campaign trigger `gifting` or `seasonal` in
`references/offers/campaign-calendar.md`.

Near neighbours:

- `gift-guide`: curation without a hard date or cutoff; evergreen recipient
  and price-band browsing. If the brief has a delivery cutoff, it is this
  type, not the guide (index tie-break).
- `sale-clearance-flash`: many products at reduced prices for a window; price
  is the message, not the recipient. BFCM sitewide sale pages are that type;
  a BFCM gift edit with cutoffs is this type.
- `offer-page`: one named promotion, one buy box; no assortment.
- `collection-landing`: a category grid with a festive banner is a failure
  mode of this type, not a variant (see Never).

## Variants

- **Planner wave** (US Dec 1 to 10; India 10 to 12 days before Rakhi or
  Diwali): gift guide framing, standard shipping, modest offer or free
  standard shipping.
- **Deadline wave** (Dec 11 to 20; final week before an Indian festival):
  express cutoffs in the hero, no discount needed, ships-by on every card.
- **Rescue wave** (Dec 21 to 25; final 48 hours in India via quick
  commerce): `gift-card` becomes the hero, express only, no discount.
- **BFCM gifting**: one sitewide offer stated once; VIP or member early
  access is the plus-up, not a deeper percent (OPERATOR: Klaviyo and CTC via
  `references/offers/campaign-calendar.md` CC6, CC10).
- **India festive**: adds `payment-options` (COD, UPI, no-cost EMI over
  ₹3,000), bank cashback strip, "inclusive of all taxes", pincode delivery
  date (campaign-calendar CC13).

## Anatomy

Sections between chrome: 7 to 10. Word budget 300 to 700.

1. `announcement` (chrome, conditional: a verified sitewide cutoff or offer
   exists). Standard and express cutoff dates with timezone, rolling
   automatically; never a countdown.
2. `header` (mandatory). Full navigation from `lexsis_brand.navigation`;
   occasion shoppers browse the rest of the store.
3. `hero` (mandatory). Occasion plus edit name, the giver addressed about the
   recipient, the standard cutoff line, one CTA to the first grouping.
   Observed in 2 of 2 gifting teardowns as H1 plus one-line intro
   (internal teardown audit, 2026-09-10).
4. `delivery-cutoff` (mandatory). Standard, express and international dates
   computed by the cutoff procedure in `references/offers/campaign-calendar.md`,
   bound to offer-ledger rows, phrased "Order by Dec 18 for expected delivery
   by Dec 24 with standard shipping". This section is the only urgency on the
   page.
5. `product-grid` (mandatory). Grouped by recipient or by price band (four to
   six groups, round price points such as under ₹999 or under $50); each card
   carries price, rating and count when reviews exist, and a per-product
   ships-by line; products that cannot arrive in time are hidden or marked
   "arrives after [occasion]". Price-band grids appear in 2 of 2 gifting
   teardowns (Sea Bags, Born Primitive).
6. `product-spotlight` (recommended; conditional: curated gift sets exist in
   the catalog). Two or three sets at round prices with contents shown
   together and separately and a computed "vs buying separately" line.
7. `gift-options` (mandatory). Gift note field with character limit and
   preview, gift wrap as an un-ticked priced add-on, gift receipt wording
   ("prices hidden"), gift returns window.
8. `shipping-returns` (recommended). Express options and prices, extended
   holiday returns if the store offers them, international notes.
9. `payment-options` (conditional: India in store markets). COD or UPI on
   delivery, no-cost EMI line for items over ₹3,000, bank cashback strip,
   tax-inclusive wording.
10. `reviews` (conditional: verified review quotes about a recipient's
    reaction exist). Two or three recipient-reaction quotes with dates;
    never a star-heavy carousel (proof-density table, gifting row,
    internal research audit (2026-09-10) section 13).
11. `offer` (conditional: a verified offer row exists). GWP, free-shipping
    threshold, bundle saving or, after the cutoffs, `gift-card` with
    schedule-send and message.
12. `faq` (recommended). Cutoffs by speed and destination, gift returns,
    wrap and note, what the recipient sees on the packing slip.
13. `email-capture` (conditional: more than five days remain before the
    standard cutoff). "Last-call alerts before the cutoff", one field.
14. `footer` (mandatory). Policies, contact with hours during the window.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. Merchant facts first: the occasion and its date (lunar and Hindu dates confirmed against an almanac, CC3), markets, shipping speeds with carrier last-ship dates, processing days and buffer. Run the cutoff procedure in `references/offers/campaign-calendar.md` and write one offer-ledger delivery row per speed and destination. Gift wrap price, note character limit, gift receipt wording and gift returns window from the policy page URL (`references/offers/offer-ledger.md`).
2. `lexsis_catalog.list` for the gift edit: ids, prices (to place round bands), option axes, inventory, media count per product. `lexsis_catalog.get` per candidate: first media item as the identity image, lifestyle, packaging or gift-box shots, variant images. Record which products lack an identity image or a ships-by row; they are raised with the merchant, not silently excluded.
3. `lexsis_brand.navigation` for header and footer; `lexsis_brand.brand_kit` for tokens, voice and banned phrases; `lexsis_brand.context` for the `theme_id` every asset call needs.
4. `lexsis_catalog.reviews_status`, then `lexsis_catalog.reviews_search` per grouping with "gift", "for my", "she loved", "arrived in time"; candidates stay `pending` until confirmed (`references/proof/reviews-sourcing.md`, tier 3 and band table).
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`, one call per tag `banner`, `hero`, `lifestyle`, `flat-lay`, `product-shot`, `social-proof`; record counts; then semantic "<occasion> gift table with <category>". View candidates with `lexsis_assets.view` (`references/assets/asset-sourcing-sequence.md`).
6. `lexsis_cart.get` for the cart profile: gift note field, wrap add-on SKU and price, nothing pre-ticked (`references/cart-profile-management.md`).
7. `lexsis_design.islands` for the active catalog; `lexsis_workspace.credits` before any generation is planned (`references/assets/generation-policy.md`).

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `announcement` (conditional: verified cutoff or offer row) | standard and express cutoff in one line. | no (chrome, outside the loop). | SiteHeader announcement strip, or AnnouncementBar when the strip should scroll away; one message, no dismissal, never CountdownTimer. | "Order by Dec 18 (IST) for standard delivery before Dec 24", under 60 characters. | the offer-ledger delivery row; no row, no announcement. |
| `header` | full navigation; occasion shoppers browse onward. | logo from the brand kit; a text wordmark when none. | SiteHeader when an announcement exists, else Navbar; links from `lexsis_brand.navigation`. | nav labels only. | the navigation result and the announcement decision. |
| `hero` | name the occasion and the recipient, state the standard cutoff, send the giver to the first grouping. | yes; job `context`, treatment `product-in-context` (`references/assets/image-jobs-by-page-type.md`, section 5). Search catalog lifestyle media of the flagship set, then library `banner`, `hero`, `lifestyle`, then semantic, then merchant upload. Generation: `hero_bg` behind a real cut-out, bold moment only. Missing media: (context scene, 16:9 plus 4:5, one image) ; alternative: `hero_bg`; if skipped, the first catalog identity image serves as a packshot hero and the plan records "hero pending merchant media". No-go: a festive motif as wallpaper; a generated product; text in the image. view it beside the first grid row so lighting and backgrounds agree. | none by default (static art-directed `<picture>`, `references/assets/slot-spec.md`); HeroMedia only when the hero is the plan's full-bleed bold moment, image mode, no autoplay | H1 recipient-first, 10 words or fewer; one cutoff line as information; one CTA "Shop gifts under ₹999"; 40 words total. | `lexsis_assets.view` of the chosen frame at both crops; the ledger date row; the grouping list for the CTA target. |
| `delivery-cutoff` | the only urgency on the page: dates per speed and destination. | no (buy-box sub-element, outside the loop). | DeliveryEstimate for the dispatch line, ticking countdown off (this type forbids a clock); the occasion "Order by" lines per speed are HTML bound to the ledger rows because the island has no occasion-date or pincode input, and the publish schedule removes each passed line (CC5); international rows are text only. | "Order by Dec 18 for expected delivery by Dec 24 with standard shipping", one line per speed with timezone and destination, three to five lines; never "guaranteed". | the cutoff procedure output in the offer ledger. |
| `product-grid` | gifts grouped by recipient or by price band, four to six groups. | yes; job `identity` per card from catalog media, one aspect across every card (`references/product-grid.md`), second image where present. Generation: none ("needs a real photo"). Missing: list the products without an image to the merchant with a count and; if skipped, those cards leave and a group under three products merges into its neighbour. No-go: a generated or stock product; mixed aspects; a countdown on a card. view the grid images together so lighting, backgrounds and crops agree. | FeaturedCollectionStage per group of three or more, or the card composition from `references/product-grid.md` with QuickAdd per card for smaller groups; decide from group size, image availability and variant axes; quick add opens the picker for multi-variant items; motion off Ships-by per card is HTML from the ledger; a product that cannot arrive is hidden or marked "arrives after <occasion>" (gifting deltas, `campaign-calendar.md`). | group heading 6 words or fewer; one reason per card under 15 words; price on every card; rating and count only at 5 or more reviews. | `lexsis_catalog.list` price distribution, product count per group, image availability per product, the ledger ships-by rows. |
| `product-spotlight` (conditional: curated sets exist) | two or three sets at round prices, shown together and apart. | yes; jobs `included-items` and `identity`. Search catalog media of the set SKU, then library `product-shot` and `flat-lay`, then merchant upload. Generation: none (identity-bound, GN1, GP13). Missing media: (set flat lay, 1:1, one per set) and; fast draft shows the set image beside each component's identity image; view the set images together so lighting, backgrounds and crops agree. | QuickAdd per set; decide from variant count (direct add or picker) | 30 words per set; "vs buying separately" only from a computed offer-ledger savings row. | set SKUs in the catalog and the savings row. |
| `gift-options` | note, un-ticked priced wrap, gift receipt wording, gift returns. | yes; job `gift-presentation` (the real box, wrap and card that ship). Search catalog media of the wrap SKU, then library `product-shot` and `lifestyle`, then semantic "<brand> gift box", then merchant upload. Generation: none (identity-bound; a composite may not add wrap, GP13). Missing media: (a photo of what ships, 1:1 or 4:5, one image) and; if skipped, the note and wrap controls stay as the section's object and the production-ready plan waits for the photo (`gift-presentation` is required for this type). | note field and wrap add-on come from the cart profile (`lexsis_cart.get`, `head.use_cart_v2`); QuickAdd on the wrap SKU when wrap is a product Nothing pre-ticked (CC12). | label with the character limit, wrap price beside the control, "Gift receipt hides prices", returns window; four lines. | cart profile flags and the policy URL. |
| `shipping-returns` (recommended) | express options with prices, holiday returns, international notes. | no (stands without an image per the asset workflow). | none; DeliveryEstimate with the free-shipping threshold only when the threshold is a ledger row and shipping is domestic. | one line per speed with its price, the extended returns date, five lines at most. | the policy URL and the offer ledger. |
| `payment-options` (conditional: India in store markets) | COD or UPI on delivery, no-cost EMI over ₹3,000, bank cashback, tax-inclusive wording, pincode delivery date (CC13). | provider marks only as issuer artwork with a ledger row; never generated (GN5). | PaymentOptions for providers enabled at checkout; decide from `lexsis_workspace.stores` markets and the enabled rails; COD, UPI, EMI and the pincode line are static HTML from the ledger because the island has no pincode input | three lines; "inclusive of all taxes". | store markets and enabled checkout providers. |
| `reviews` (conditional: recipient-reaction quotes verified) | "will they like it" answered in customers' words. | quotes are the artefact; reviewer photos only real with consent, else CSS initials (`references/proof/proof-ledger.md`, display rules). | ReviewCarousel for three to six quotes bound to an active collection, static blockquotes for one or two, nothing review-shaped in band B0; decide from the band in `references/proof/reviews-sourcing.md`; autoplay off. | verbatim, dated, two or three quotes, 60 words each. | `reviews_status` band and confirmed candidates. |
| `offer` (conditional: verified offer row) | the one offer, or the gift card after the cutoffs. | yes; job `identity` of the GWP item or the gift-card product from catalog media. Generation: none. Missing:; if skipped, the offer terms sit as one line beside the grid. | QuickAdd on the gift-card product after the express cutoff; none for a threshold line | one sentence, no percentage pill (N9), 25 words. | the offer-ledger row and the current cutoff state. |
| `faq` (recommended) | cutoffs by speed and destination, gift returns, wrap and note, the packing slip. | no. | none; native `<details>` and `<summary>`. | four to six questions, answer in the first sentence, 60 words each. | support data and the ledger rows. |
| `email-capture` (conditional: more than five days to the standard | last-call alerts before the cutoff. | the hero or a set image sits beside the form; the form is the object when no image is spare (N8). | EmailCapture, one per page, or the Footer newsletter layout when the footer carries the form; incentive only with a ledger row. | one line and one field. | days remaining to the standard cutoff; `lexsis_capture.form_schemas`. |
| `footer` | policies, contact with hours during the window. | logo only. | Footer with columns from `lexsis_brand.navigation`. | Use the shared procedure. | the navigation result. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` per card, set images, wrap SKU image | `context` occasion scene, `gift-presentation`, `included-items` flat lay | reuse the best set lifestyle shot for the hero; generate `hero_bg` (ALLOW) or `product_composite` for `context` (ALLOW over a real cut-out); ask the merchant to upload the box, wrap and flat lay; skip a set only on the merchant's call |
| asset library | `banner` and `hero` occasion imagery, `lifestyle`, `social-proof` UGC with rights | occasion-specific scenes for a new festival, unboxing UGC | semantic query, then ask the merchant to upload; UGC only with a ledger row; skip only on the merchant's call |
| generation | backdrops, textures, composites only | product, people, results, logos, text | never; these are "needs a real photo" in the merchant message |

With minimal assets the page is a header, a hero built from the best set photo, the cutoff lines, one price-band grid of real catalog cards, the gift options with the merchant's own box photo and a footer; at most one generated asset (`hero_bg`), never more than four per page, and every missing asset listed in the plan and the draft summary with upload, generate or skip.

## Above the fold (390px)

In order: compact header; H1 naming the occasion and addressing the giver
about the recipient; the standard cutoff line as information ("Order by
Aug 22 for delivery before Rakhi"); one CTA to the first grouping ("Shop
gifts under ₹999"); the first grouping tiles or first grid row peeking.
Observed above-the-fold recipe for gifting: H1, intro line, first price-band
grid (internal teardown audit, 2026-09-10).

Must not appear: a countdown clock, a discount pill, a popup, an autoplaying
video, a regional decoration used as wallpaper (a diya or rakhi thread is an
accent inside a product photograph, not a background).

## Proof

Modules: 1 to 3. The gifting shopper's doubts are "will it arrive" and "will
they like it", so proof is policy first and recipient reaction second.

- `policy-fact` (required): delivery cutoff by speed, gift returns window,
  gift receipt behaviour. Source is the store policy page URL or the
  merchant's written confirmation (`references/proof/proof-ledger.md`).
- `review-quote` (recommended when it exists): quotes that mention giving or
  the recipient's reaction, verbatim with date; two or three, inline beside
  the sets or grid.
- `review-summary` on cards (when the product has 5 or more reviews).
- `ugc-photo` of unboxing (conditional: rights recorded).
- Never: `social-proof-popup`, `live-viewer-count`, `press-logo-unlinked`,
  "500 gifts sent this week" unless it is a live query bound to orders
  (truthful-count rules, internal research audit (2026-09-10) section 10).

When the store has no reviews: policy facts and a founder note about how
gifts are packed replace review modules; nothing review-shaped is rendered
(`references/proof/reviews-sourcing.md`).

## Offer and CTA

- CTAs: one in the hero, one optional closing CTA, plus the card CTAs. Every
  standalone CTA points at a grouping or the cart, never at a discount
  claim. Copy pattern `shop-collection`: "Shop gifts for her", "Shop gifts
  under $50".
- First CTA in the hero. Sticky CTA optional; a sticky recipient or price
  filter bar is more useful than a sticky button on a grid page.
- Price reveal: prices on every card; price bands may appear in the hero.
- Urgency: the cutoff date only, phrased as information. LAW and RESEARCH: a
  dispatch-cutoff line added +27.1% revenue at 95% confidence with no clock
  (CXL Bob and Lush test via
  https://cleancommit.io/blog/do-countdown-timers-work/); countdown timers
  averaged +1.5% across 6,700 tests and are the most-faked element
  (https://gwern.net/doc/economics/advertising/2017-browne.pdf). A clock
  belongs to `sale-clearance-flash`, not here.
- Offer types that fit: `none`, `gwp`, `free-shipping`, `bundle`,
  `gift-card` (post-cutoff hero), `fixed-off` with a threshold, `bogo` framed
  as "one for you, one for them", `loyalty` early access, `cashback` and
  `bnpl` for India, `limited-edition`, modest `percent-off` in the planner
  wave only.
- Offer types that do not fit: `flash-sale`, `clearance`, `subscribe-save`,
  `referral`, `trial-sample`, `mystery`, `pre-order-price`, `price-lock`,
  `student-military`, `tiered-volume`.
- OPERATOR: deepest December discounts belong after Dec 26; deadline-driven
  and rescue shoppers pay for speed and certainty, not price
  (https://www.growthsuite.net/resources/shopify-holiday-campaigns/christmas-holiday-season).
  A `percent-off` dated Dec 11 to 25 is flagged in the plan with the
  merchant's reason (campaign-calendar CC11).
- Gift wrap is never pre-ticked (LAW: basket sneaking; campaign-calendar
  CC12). One offer per page; VIP plus-ups go to email and SMS
  (`references/offers/offer-ledger.md` rule 6).

## Imagery

Required jobs: `identity` per product, `context` (recipient or occasion
scene at true scale), `packaging` (what arrives), `gift-presentation` (the
real box, wrap and note; nothing shown that does not ship). Recommended:
`included-items` for sets shown together and apart, `in-use`, `ugc` unboxing
with rights, `scale`.

Hero treatment: `product-in-context`, festive but product-first; the product
legible in one second; regional cues as accents. Studio to lifestyle balance
follows the vertical table in `references/assets/image-jobs-by-page-type.md`.
Video optional (a 6 to 15 second muted unboxing loop with a pause control).
Minimum 6 image slots. Plan slots: hero, one gift-presentation, one per set,
one context, card images from the catalog.

## Copy

Framework: dual-audience BAB, one line for the recipient's experience and one
for the giver's safety ("She will wear it every day. Free swaps until Jan 15
if she wants a different size."), then FAB on cards. Lead with the
relationship for Rakhi and Mother's Day; lead with price bands only for
Dhanteras, Diwali and BFCM (OPERATOR: Appbrew,
https://www.appbrew.com/blogs/festive-season-marketing-india).

- Headline: recipient-first, 10 words or fewer: "Gifts for the one who runs
  before sunrise".
- Reading level grade 6 to 8; one line of "why it is a good gift" per card,
  under 15 words.
- Section ceilings: hero 40 words; set descriptions 30 words each; FAQ
  answers 60 words with the answer in the first sentence.
- Vocabulary: "expected delivery by", never "guaranteed"; "order by", never
  "hurry" or "last chance" unless bound to the cutoff row; no "perfect gift".
- Every date carries its timezone and destination scope.

## Never

- Never publish a cutoff copied from last year or without the carrier table,
  processing days and buffer recorded in the offer ledger (campaign-calendar
  CC4).
- Never show a countdown; the `delivery-cutoff` date line is the urgency.
- Never keep a passed cutoff on the page; the island removes it and the hero
  switches to express, then to `gift-card` (CC5).
- Never pre-tick gift wrap, a card or insurance.
- Never run the same page for every festival with a swapped banner; recipient
  groups, cutoffs and payment rails differ per occasion.
- Never write "guaranteed delivery"; carriers publish estimates.
- Never blend three grouping axes in one page ("for the home baker under $50
  who loves vintage"); one axis per grouping, a product may appear in more
  than one group.
- Never show a product in the grid that cannot arrive before the occasion
  without marking it.
- Never state a recipient-reaction count ("2,000 moms gifted this") without a
  verified proof-ledger row.
- Never tear the page down the day after; pivot to self-gifting and "spend
  your gift card" (OPERATOR: identixweb,
  https://www.identixweb.com/how-to-build-shopify-gift-guides/).

## Examples

- Sea Bags holiday gift guide, https://seabags.com/pages/holiday-gift-guide:
  price-band grids ("Under $50", "$50 to $100"), Christmas delivery notes
  and shipping cutoff dates on the page, e-gift card as the fallback section.
  Missing recipient groups.
- IGP Rakhi sale, https://www.igp.com/rakhi/sale: occasion hub with
  rakhi add-ons, delivery-date framing and sibling gifting groups for a
  cross-city Indian audience.
- Ace Vanity Rakshabandhan 2026,
  https://acevanity.in/pages/rakshabandhan-sale-2026: bundles at round
  prices, gift card offer, FAQ and COD line on one page.

## Checklist

```json
{
  "page_type": "seasonal-gifting",
  "aliases": ["holiday landing page", "festive edit", "occasion page", "BFCM gift edit", "Rakhi edit", "Diwali gift sets"],
  "funnel_stage": ["mof"],
  "awareness": ["solution-aware", "product-aware"],
  "traffic": ["email", "sms", "meta", "google-search", "organic"],
  "sections": { "min": 7, "max": 10 },
  "mandatory_sections": ["header", "hero", "delivery-cutoff", "product-grid", "gift-options", "footer"],
  "recommended_sections": ["product-spotlight", "shipping-returns", "payment-options", "reviews", "offer", "faq", "email-capture"],
  "forbidden_sections": ["countdown", "buy-box", "dateline", "hook", "agitation", "offer-bridge", "quiz"],
  "nav": "full",
  "price_above_fold": "optional",
  "cta": { "min": 1, "max": 2, "first_after_section": 0, "sticky": "optional", "copy_pattern": "shop-collection" },
  "proof": { "min_modules": 1, "max_modules": 3, "required_kinds": ["policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "context", "packaging", "gift-presentation"], "hero": "product-in-context", "video": "optional", "min_images": 6 },
  "copy_framework": ["bab", "fab"],
  "offer_compat": { "allowed": ["none", "gwp", "free-shipping", "bundle", "gift-card", "fixed-off", "percent-off", "bogo", "loyalty", "cashback", "bnpl", "limited-edition"], "forbidden": ["flash-sale", "clearance", "subscribe-save", "referral", "trial-sample", "mystery", "pre-order-price", "price-lock", "student-military", "tiered-volume"] },
  "urgency": "verified-only"
}
```

## Sources

- internal research audit (2026-09-10) section 5 block 10; section 2 row 10.
- internal research audit (2026-09-10) sections 3, 4.3, 7.
- internal research audit (2026-09-10) sections 10, 13.
- internal research audit (2026-09-10) sections 1.1, 12.
- internal research audit (2026-09-10) teardown 39 and Part D.
- `references/offers/campaign-calendar.md` (occasion table, cutoff procedure, gifting deltas, CC4, CC5, CC11, CC12, CC13).
- CustomFit.ai festive CRO: https://www.customfit.ai/blog/d2c-ecommerce/ecommerce-holiday-optimization-festive ; Raksha Bandhan: https://www.customfit.ai/blog/seasonal-cro/raksha-bandhan-marketing-cro
- Appbrew festive calendar: https://www.appbrew.com/blogs/festive-season-marketing-india
- Growthsuite December waves: https://www.growthsuite.net/resources/shopify-holiday-campaigns/christmas-holiday-season
- Shopify holiday shipping guide: https://www.shopify.com/blog/holiday-shipping-guide
- Countdown evidence: https://cleancommit.io/blog/do-countdown-timers-work/ ; https://gwern.net/doc/economics/advertising/2017-browne.pdf
- Valentine's final-five-days share (35%): https://easyappsecom.com/guides/shopify-valentines-day-marketing
- Last-orders messaging: https://glazedigital.com/blogs/news/guide-to-last-orders-messaging-for-christmas
- identixweb gift guides: https://www.identixweb.com/how-to-build-shopify-gift-guides/
