# Sale, clearance and flash sale page

Many products at reduced prices for a real window. Shoppers arrive most-aware
from email, SMS or social, already on the list, and want to see what is
reduced, by how much, until when, and add to cart from the grid. The grid does
the work; the hero states depth, scope and end time in one sentence; every
compare-at has a legal basis; every stock badge reads live inventory. This
type is exempt from the one-offer rule because each card can carry its own
ledgered reduction (`offer-ledger.md` rule 6).

## Identify it

- Brief says "sale", "flash sale", "clearance", "end of season", "last
  chance", "warehouse sale", "48 hours", "BFCM", with more than five
  discounted SKUs and a start and end.
- Audience is the existing list or past visitors; awareness is most-aware.
- Near neighbours:
  - `offer-page`: one named promotion on one product or a set; choose sale
    when more than five products are discounted (index tie-break).
  - `seasonal-gifting`: an occasion with delivery cutoffs and gift options;
    choose gifting when the assortment is for giving and cutoffs matter more
    than the markdown.
  - `collection-landing`: a category at full price; choose sale when the
    reduction is the reason for the page.
  - `restock`: one product back in stock; no markdown.
  - `launch-waitlist-preorder`: a drop with a clock but no reduction.

## Variants

- **Flash sale.** Hours, not days; SMS-led; server-side countdown to the real
  end in the final 24 to 48 hours; price reverts at zero. OPERATOR: bookend
  hours convert highest (first hour 6.2%, last 30 minutes 7.1%)
  https://www.getattribute.com/blog/flash-sale-performance-report .
- **Sale event** (BFCM, anniversary, festive). One sentence offer, code
  auto-applied, category shortcuts, shipping cutoff strip; curated grid of 10
  to 30 SKUs.
- **Clearance.** Broader grid with size, price and availability filters;
  "Final sale, no returns" stated on every card and again in the buy path;
  sizes remaining from live inventory. Statutory rights survive "final sale"
  (UK CRA 2015; EU 14-day withdrawal; India return-terms disclosure).
- **India festive sale.** MRP struck with "X% off MRP" as text, "inclusive of
  all taxes", bank or UPI cashback strip, no-cost EMI line, pincode delivery
  date before the festival, COD badge (`price-presentation.md` PP5, PP22,
  PP25).

## Anatomy

Counts exclude chrome. Order follows the fudge.ai BFCM roundup, the Heartly
sale-page guidance and the boAt and Mamaearth grids in
internal research audit (2026-09-10).

1. `announcement`: mandatory. End date and time with timezone as text
   ("Ends Sunday 11:59pm IST"), code or "prices as marked"; becomes the
   `countdown` host only inside the final 48 hours.
2. `header`: mandatory, full navigation. The sale lives inside the store and
   the shopper may browse beyond it.
3. `hero`: mandatory. Depth, scope and end time in one plain sentence ("30%
   off all outerwear. Ends Sunday 11:59pm ET."); `grid` or `typographic`
   hero; primary anchor to the grid.
4. `offer`: mandatory (terms line). Automatic or code, exclusions, stacking,
   regions, "final sale" where it applies, near the top and within one scroll
   of the hero.
5. `product-grid`: mandatory. Curated: best sellers, giftable and high-margin
   first; 10 to 30 SKUs for an event, broader for clearance with filters.
   Each card: identity image, name, struck compare-at with basis, sale price,
   saving text, `review-summary` when 5 or more reviews, variant availability,
   add to cart.
6. `stock-indicator`: conditional: live inventory binding exists. "12 left in
   size M" on the card, conservative threshold, disappears when replenished.
   OPERATOR: product-list scarcity badges were the strongest urgency
   placement in one agency portfolio (+3 to 3.2%)
   https://crometrics.com/blog/urgency-that-actually-works/ .
7. `countdown`: conditional: ledger `endsAt` confirmed and the page is inside
   the final 48 hours; sits beside the primary CTA and in the announcement,
   never in the grid cards.
8. `review-summary`: recommended. Store-level aggregate ("4.8 from 12,400
   reviews on Judge.me") linked to its source, or per card.
9. `shipping-returns`: mandatory. Returns on sale items, final-sale wording
   where it applies, shipping threshold and delivery estimate; for a festive
   sale, the delivery cutoff.
10. `waitlist-form`: conditional: sold-out items remain on the grid. "Notify
    me" on the card, variant-specific.
11. `closing-cta`: mandatory. Anchor back to the grid plus the end time
    restated as text.
12. `legal`: recommended chrome. Full sale terms.
13. `footer`: mandatory chrome.

Never include education (`problem`, `agitation`, `mechanism`, `story`), a
`quiz`, an `email-capture` overlay over the offer, or a `buy-box` for a single
product (that is `offer-page`).

## Workflow

Assets first: the grid is the page, and every card exists only because a real
identity image of that SKU exists. A section that would end up as a colour
band, an emoji row, icon tiles or a wall of text is rebuilt around imagery or,
on the merchant's call, merged or skipped. Per-slot sourcing:
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

1. Offer ledger: `offer.endsAt` (ISO with timezone, confirmed, never
   extended), code or "prices as marked", exclusions, stacking, regions,
   final-sale flag, and a `compareAtBasis` per SKU for the market
   (`references/offers/price-presentation.md` PP1 to PP5, PP11;
   `references/offers/offer-types.md` flash-sale, clearance).
2. `lexsis_catalog.list` filtered to the sale items, then `lexsis_catalog.get`
   per SKU: first media item as the card identity (view every card image
   together with `lexsis_assets.view` for one background, crop and
   orientation, `image-jobs-by-page-type.md` IJ9), price, compare-at,
   variants with availability, live inventory per variant, per-variant images
   for swatches where colour drives the choice.
3. `lexsis_catalog.reviews_status`; `lexsis_catalog.reviews` per SKU for card
   summaries (B2 or more), or the store-level aggregate labelled as a store
   rating and linked to its source (`references/proof/reviews-sourcing.md`).
4. `lexsis_cart.get`: code auto-apply, threshold, cart v2 (QuickAdd needs it).
5. `lexsis_brand.context`, `lexsis_brand.brand_kit`, `lexsis_brand.navigation`
   (full nav; the sale lives inside the store). India festive: market tokens
   and MRP wording (PP5, PP21, PP22, PP25).
6. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"` for
   `product-shot` (cards missing a catalog image) and `banner` (a real campaign
   backdrop for a typographic hero); no `lifestyle` sections on this type.
   Sequence and checks: `references/assets/asset-sourcing-sequence.md`.
7. `lexsis_design.islands`, then `lexsis_design.island_schema` for each island
   named below. `lexsis_workspace.credits` only when the hero is typographic
   and the plan names it as the bold moment: one `hero_bg` (landscape plus
   portrait) is the only ALLOW generation on this type.

### Section by section

No asset is used sight unseen: open every candidate with `lexsis_assets.view`
and run the section 1b fit review in `references/workflows/section-asset-workflow.md`
before use (subject does the job, crops to the slot without losing the product,
quiet area for the copy, lighting and styling match neighbouring slots, palette,
no baked-in text or watermark); view a section's or gallery's candidates
together so the set reads as one shoot, and view a generated asset the same way
after it returns.

**`announcement`**
- Purpose: end date and time with timezone as text, code or "prices as marked".
- Media: none.
- Island: SiteHeader strip or AnnouncementBar with one message ("Ends Sunday 11:59pm IST. Prices as marked."); inside the final 48 hours the bar keeps the text and the timer sits beside the hero CTA, since the bar has no timer slot; resolve from `lexsis_design.island_schema`; preset `siteheader/sticky-light`.
- Copy: under 60 characters; plain time; vocabulary per `references/anti-patterns/copy-anti-patterns.md`.
- Decide with: `offer.endsAt`; code from `lexsis_cart.get`.

**`header`**
- Purpose: full store navigation.
- Media: brand logo. View every candidate with `lexsis_assets.view` and run the section fit review (section 1b of `references/workflows/section-asset-workflow.md`) before use.
- Island: SiteHeader, sticky, cart drawer, links from `lexsis_brand.navigation`; hydration mode allowed; resolve from `lexsis_design.island_schema`.
- Copy: store names.
- Decide with: `lexsis_brand.navigation`.

**`hero`**
- Purpose: depth, scope and end time in one sentence; anchor to the grid.
- Media: yes, `grid` of four to six card identity images reused from the product grid (no new asset), or `typographic` on a real `banner` asset or a generated `hero_bg` (ALLOW, only as the plan's bold moment, quiet zone under the HTML sentence, one legibility overlay at most). Never a single-product hero, a lifestyle campaign image that hides the products, or a homepage carousel (IJ8). Missing backdrop for a typographic hero: tell the merchant; offer upload or the `hero_bg` generation with its credit cost; the card grid hero ships meanwhile. View every backdrop candidate, generated ones included, with `lexsis_assets.view` and run the section fit review (quiet zone under the sentence, palette, no baked-in text) before use.
- Island: none (HTML); or FeaturedCollectionStage for a curated hero set of four to eight products with quick add, badges off, no autoplay or entry animation (N10); resolve from `lexsis_design.island_schema`.
- Copy: `[depth] off [scope]. Ends [day, time, timezone].`, 14 words; CTA "Shop the sale".
- Decide with: card images available; whether the plan names a bold moment.

**`offer`**
- Purpose: the terms line within one scroll of the hero.
- Media: none.
- Island: none.
- Copy: automatic or code, exclusions, stacking, regions, "final sale" where it applies; three lines of 18 words.
- Decide with: ledger terms.

**`product-grid`**
- Purpose: the sale, 10 to 30 curated SKUs (broader with filters for clearance), best sellers and high-margin first.
- Media: yes, one identity image per card from that SKU's catalog media (uniform aspect per `slot-spec.md`, SS10), library `product-shot` for a card whose catalog lacks one. Never stock, never generated, never a hero image cropped into a card; swatch chips from the catalog hex only beside a real variant image. Missing card images: tell the merchant which SKUs (identity, square, one each); offer upload; those cards wait off the grid until then. View the candidates together with `lexsis_assets.view` and run the section fit review so the set reads as one shoot, not a pile of found images.
- Island: an HTML grid per `references/product-grid.md` with QuickAdd per card (variant picker when sizes or colours exist), or ProductCarousel with quick add and animation off for a "best sellers first" rail above the grid; each card carries name, `<s data-source="compare_at_price">` (or the ledger row id) with a per-SKU basis, sale price larger and higher-contrast, saving as text, review summary at B2 or more, variant availability inline; no pills or ribbons (N9, `offer-types.md` OF10). Resolve from `lexsis_design.island_schema`; preset `productcarousel/cards-quickadd-light`.
- Copy: card saving text 4 words ("Save $28"; "Save 30%" under $100, PP10); no microcopy under card CTAs.
- Decide with: SKU list and images from step 2; per-SKU basis from step 1; cart v2.

**`stock-indicator`**
- Purpose: "12 left in size M" on the card from live inventory.
- Media: none.
- Island: InventoryIndicator in its inline text form bound to the card's variant, conservative threshold, hiding itself above it and on replenish; never on made-to-order or pre-order stock, never a fixed number in copy (`urgency-scarcity.md` UR3); resolve from `lexsis_design.island_schema`; preset `inventoryindicator/text-quiet`.
- Copy: island-rendered; no "Selling fast", no "N people viewing".
- Decide with: `offer.stockVerified` and a live inventory binding (`plan_lint.py` T10).

**`countdown`**
- Purpose: the real end inside the final 48 hours, beside the primary CTA.
- Media: none.
- Island: CountdownTimer bound to `offer.endsAt`, hiding itself at zero while prices revert server-side; never inside grid cards; the Countdown island is deprecated (UR2, UR7); resolve from `lexsis_design.island_schema`.
- Copy: the end time as text beside the timer.
- Decide with: `offer.endsAt` confirmed and now within 48 hours.

**`review-summary`**
- Purpose: store-level aggregate linked to its source, or per-card summaries.
- Media: none.
- Island: none; an HTML line "4.8 from 12,400 reviews on Judge.me" with the link, labelled as a store rating, never relabelled as a product rating (RS7).
- Copy: one line.
- Decide with: `reviews_status` source and count.

**`shipping-returns`**
- Purpose: returns on sale items, final-sale wording, threshold, delivery estimate or festive cutoff.
- Media: none.
- Island: DeliveryEstimate for single-zone domestic shipping before a festival cutoff, else none; the India pincode line is static HTML (no pincode prop); resolve from `lexsis_design.island_schema`; preset `deliveryestimate/inline-quiet`.
- Copy: 40 words; statutory rights survive "final sale".
- Decide with: `policy-fact` rows; shipping zones.

**`waitlist-form`**
- Purpose: "Notify me" on a sold-out card, variant-specific.
- Media: the card's identity image stays; no new asset.
- Island: EmailCapture in compact form, one per sold-out variant in the card's add position, labelled "Notify me"; marketing consent is a separate un-ticked HTML checkbox or absent; resolve from `lexsis_design.island_schema`.
- Copy: "One email when it is back."
- Decide with: variant availability from step 2.

**`closing-cta`**
- Purpose: anchor back to the grid plus the end time restated as text.
- Media: no new asset.
- Island: StickyBar in collection mode ("Shop the sale" to the grid, end time as the subtitle), animation off; never a product-level add to cart; resolve from `lexsis_design.island_schema`; preset `stickybar/collection-light`.
- Copy: "Shop the sale" or "Shop all outerwear"; the end as text.
- Decide with: page length; `offer.endsAt`.

**`legal`** and **`footer`**
- Purpose: full sale terms; chrome.
- Media: brand logo. View every candidate with `lexsis_assets.view` and run the section fit review before use.
- Island: Footer with the terms as a column link; preset `footer/columns-dark`.
- Copy: the store's.
- Decide with: terms URL.

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (one identity per SKU) | card identity, variant images for swatches | a consistent background across shots, images for a few long-tail SKUs | reuse library `product-shot`; ask the merchant to upload identity shots for the listed SKUs; those cards wait off the grid until then, never composited |
| asset library | `product-shot` fills, a real `banner` for a typographic hero | nothing else is needed on this type | none |
| generation | one `hero_bg` for a typographic hero named as the bold moment (landscape plus portrait) | products, card images, people, badges, text, timers | never |

Minimal assets (identity per SKU, nothing else): announcement, hero built from the card images, terms, the grid with struck prices and QuickAdd, shipping and returns, closing anchor; SKUs without an image are listed in the plan and draft summary and no lifestyle section is added to fill space. Generated assets on a sale page: zero or one backdrop, never more than the house cap of four. Every asset, generated ones included, is opened with `lexsis_assets.view` and passes the fit review in `references/workflows/section-asset-workflow.md` section 1b before it ships; a paid render earns no exemption.

## Above the fold (390px)

In order: announcement with the end time as text, header, hero sentence with
depth, scope and end time, the terms line or a one-line summary of it, the
first row of grid cards with struck compare-at, sale price and add to cart.
Not above the fold: a countdown outside the final 48 hours, an email popup,
"N people viewing", a homepage carousel repurposed as the sale hero, a single
product hero.

## Proof

- Modules: 1 to 2. Module one is `review-summary` on cards or the store-level
  aggregate linked to its source. Module two is `policy-fact` (returns on
  sale items, shipping) or `stock-count` from a live binding.
- The deal is the message; proof confirms the store is real and the items are
  worth having. No quote walls, no press marquee.
- `stock-count` is proof only when bound to inventory at render
  (`proof-ledger.md` kind table); a fixed number in copy is a violation.
- Store-level aggregates are labelled as store ratings and linked; never
  relabelled as a product rating (`reviews-sourcing.md`).
- No reviews: returns and shipping facts, certifications with issuer.
  Nothing review-shaped.

## Offer and CTA

- CTA count: one add to cart per card (6 to 30 cards) plus the hero anchor and
  the closing anchor. All card buttons are identical in label.
- First CTA position: hero anchor to the grid (section index 0); the first
  card's add to cart is one screen below.
- Sticky: optional. A sticky bar carries the end time as text (and the
  countdown inside 48 hours) plus "Shop the sale"; it never carries a
  product-level add to cart.
- CTA copy: "Add to cart" on cards; "Shop the sale" or "Shop all outerwear"
  on anchors. Never "Buy Now", "Grab", "Hurry".
- Price display per card: compare-at struck text only, with a ledger basis
  per SKU; sale price larger and higher-contrast than the compare-at; saving
  as plain text ("Save $28" over $100, "Save 30%" under $100, both when space
  allows). No "31% OFF" pills, no ribbons (`design-rules.md` N9; `offer-types.md`
  OF10). Compare-at legality by market: EU 30-day lowest prior price; UK
  duration and volume tests; US bona fide former price; India MRP only.
  Pointer: `references/offers/price-presentation.md` PP1 to PP5, PP11.
- "Up to X% off" only when a meaningful share of SKUs sit at X; otherwise the
  range or the modal depth (PP11).
- Depth and window: OPERATOR, 25 to 50% off and 24 to 48 hours for broad
  audiences; under 25% "fails to break inertia" https://www.heartly.io/blog/flash-sale-best-practices ;
  80% of BFCM offers in a 3,000-brand database were 25% or deeper
  https://commonthreadco.com/blogs/ecommerce-playbook/how-to-craft-the-best-bfcm-offer-this-year .
  Model margin first.
- End datetime: real, ISO with timezone in the ledger, honoured with no
  extension; banner, timer, "last chance" copy and prices all bind to the same
  `endsAt` and revert together (`urgency-scarcity.md` UR2, UR10, UR13). A
  countdown renders only inside the final 24 to 48 hours (UR7). RESEARCH:
  deceptive timers are the UK banned practice verbatim and 80% of shoppers
  reported regret on learning a deadline was fake
  https://gunesacar.net/assets/CHI-EA-23-Time-is-Ticking-Deceptive-Countdown-Timers.pdf .
- Stock badges: only on cards, only from live inventory, conservative
  threshold, auto-removed on replenish (UR3). Never "limited stock" without a
  number, never "N people viewing", never "N bought in the last hour" (UR12).
- Cart reservation timers are false on Shopify and never rendered (UR11).
- Offers that fit: `flash-sale`, `clearance`, `percent-off`, `fixed-off`,
  `bogo`, `gwp`, `free-shipping`, `bundle`, `loyalty` (early access for
  members), `cashback` and `bnpl` (India festive), `mystery` (existing
  customers, guaranteed value with basis).
- Offers that do not fit: `first-order` (conflicts with the sale),
  `subscribe-save`, `bundle-decoy`, `referral`, `trial-sample`,
  `pre-order-price`, `price-lock`, `limited-edition`, `gift-card` (belongs on
  `seasonal-gifting` after cutoffs), `charity`.
- Luxury never runs this type (`offer-types.md` OF3).

## Imagery

- Required jobs: `identity`, one per card, consistent background, lighting
  and crop across the grid (`image-jobs-by-page-type.md` IJ9). Recommended:
  `variation` or `swatch` where colour or size drives the choice.
- Hero: `grid` of sale items; alternate `typographic` (depth, scope, end
  time). Never a single-product hero; never an editorial lifestyle campaign
  image that hides the products.
- Minimum images: one identity image per card; the hero may reuse card
  images. No lifestyle storytelling sections.
- Balance: studio-led; the grid is the page.
- Video: forbidden.
- Slots the plan creates: none beyond a missing card identity image, which is
  filled only from Shopify media or the library, never generated.

## Copy

- Framework: `aida` compressed to the direct offer for most-aware readers
  (`_index.md` section 5): attention is the depth and scope, action is the
  grid.
- Headline: `[depth] off [scope]. Ends [day, time, timezone].` "30% off all
  outerwear. Ends Sunday 11:59pm ET." "Final sale: up to 50% off last-season
  styles, sizes as shown." Loss framing is allowed when the end is real.
- Reading level grade 6 to 8; 150 to 400 words total; the grid does the
  work.
- Length ceilings: hero sentence 14 words; terms line 3 lines of 18 words;
  card saving text 4 words; shipping and returns 40 words.
- Vocabulary: plain arithmetic and plain time ("ends Sunday 11:59pm IST",
  "12 left in size M"); India "MRP ₹4,490, ₹999, 78% off MRP" with lakh
  grouping and whole rupees. Never "Hurry", "Don't miss out", "Selling
  fast", "Almost gone", "LIMITED TIME", exclamation marks, ALL CAPS, "up to"
  on a token SKU, "extended", "back by popular demand".
- Microcopy under card CTAs: none; the terms line and shipping section carry
  the conditions once.

## Never

- Never render a countdown without a ledger `endsAt`, outside the final 48
  hours, client-side, or one that resets.
- Never extend a deadline the page called final; a new window is a new
  campaign with new copy.
- Never show a compare-at without a per-SKU basis for the market (EU 30-day
  low, UK duration and volume, US bona fide, India MRP).
- Never show "up to X% off" when few SKUs sit at X.
- Never render "31% OFF" pills, "BEST VALUE" ribbons or percent badges on
  cards; struck text and a plain saving line only.
- Never show "limited stock", "only a few left" or a count from static copy;
  live inventory or nothing.
- Never show "N people viewing", "N bought today", or a social-proof popup.
- Never put ineligible items in the grid or hide exclusions in the footer.
- Never repurpose the homepage or a carousel as the sale hero.
- Never cover the grid with an email popup.
- Never show a cart reservation timer.
- Never run a sale every ten days; full-price conversion falls and the
  compare-at loses its legal basis (UK duration and volume).
- Never let sold-out cards sit without a "Notify me" or drop off silently.
- Never call "final sale" a waiver of statutory return rights.

## Examples

- fudge.ai, Black Friday Shopify landing page examples
  https://www.fudge.ai/blog/black-friday-shopify-landing-page-examples/ :
  real BFCM pages with one-sentence offers, auto-applied codes, curated grids
  of 10 to 30 SKUs and category shortcuts.
- LSKD, pre-BFCM shutdown to a countdown and sign-up (Tapcart case)
  https://www.tapcart.com/case-studies/lskd : a real event window with early
  access for app members and a single honoured end; 40% of BFCM sales came
  through the app.
- boAt, storefront sale grid https://www.boat-lifestyle.com/ : struck MRP
  with "inclusive of all taxes", live sold-out states and engraving tags on
  cards. Avoid its percent-off pill on every card (N9) and its deal-first
  hero on an evergreen homepage.

## Checklist

```json
{
  "page_type": "sale-clearance-flash",
  "aliases": ["flash sale page", "sale event page", "clearance page", "end of season sale", "last chance", "BFCM landing"],
  "funnel_stage": ["bof"],
  "awareness": ["most-aware"],
  "traffic": ["email", "sms", "meta", "direct"],
  "sections": { "min": 5, "max": 8 },
  "mandatory_sections": ["announcement", "header", "hero", "offer", "product-grid", "shipping-returns", "closing-cta", "footer"],
  "recommended_sections": ["review-summary", "legal", "sticky-cta"],
  "forbidden_sections": ["buy-box", "problem", "agitation", "mechanism", "story", "quiz", "email-capture", "offer-bridge", "hook", "bundle-builder"],
  "nav": "full",
  "price_above_fold": "required",
  "cta": { "min": 6, "max": 32, "first_after_section": 0, "sticky": "optional", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 1, "max_modules": 2, "required_kinds": ["policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity"], "hero": "grid", "video": "forbidden", "min_images": 6 },
  "copy_framework": ["aida"],
  "offer_compat": { "allowed": ["flash-sale", "clearance", "percent-off", "fixed-off", "bogo", "gwp", "free-shipping", "bundle", "loyalty", "cashback", "bnpl", "mystery"], "forbidden": ["first-order", "subscribe-save", "bundle-decoy", "referral", "trial-sample", "pre-order-price", "price-lock", "limited-edition", "gift-card", "charity"] },
  "urgency": "encouraged"
}
```

`cta.min` and `cta.max` count one add to cart per card (six or more cards,
since fewer than six discounted products is an `offer-page`) plus the hero and
closing anchors. `imagery.min_images` is one identity image per card at the
six-card floor. `countdown` and `stock-indicator` are conditional: they render
only from `offer.endsAt` and a live inventory binding (`plan_lint.py` T10).
`urgency: encouraged` still means verified.

## Sources

- Cro Metrics urgency test portfolio https://crometrics.com/blog/urgency-that-actually-works/
- Heartly flash sale practices https://www.heartly.io/blog/flash-sale-best-practices ;
  urgency guide https://www.heartly.io/blog/urgency-marketing-guide
- Attribute flash sale performance report https://www.getattribute.com/blog/flash-sale-performance-report
- Common Thread Collective BFCM offer database https://commonthreadco.com/blogs/ecommerce-playbook/how-to-craft-the-best-bfcm-offer-this-year
- Tiemessen et al., CHI 2023, deceptive countdown timers https://gunesacar.net/assets/CHI-EA-23-Time-is-Ticking-Deceptive-Countdown-Timers.pdf ;
  evidence review https://cleancommit.io/blog/do-countdown-timers-work/
- UK CMA reference pricing principles https://assets.publishing.service.gov.uk/media/66ab4347a3c2a28abb50db3c/Discount_and_reference_pricing_principles.pdf ;
  CMA unfair commercial practices https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices ;
  Emma Sleep countdown settlement https://www.gov.uk/government/news/court-endorses-cma-action-as-emma-sleep-agrees-to-change-sales-practices
- EU Price Indication Directive Art 6a guidance https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52021XC1229%2806%29 ;
  UCPD Annex I https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32005L0029
- FTC 16 CFR 233.1 https://www.law.cornell.edu/cfr/text/16/233.1
- India Legal Metrology Rules https://www.legitquest.com/act/legal-metrology-packaged-commodities-rules-2011/97B4 ;
  CCPA Dark Patterns 2023 https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf
- Attentive flash sale timing https://www.attentive.com/black-friday-cyber-monday-2026/articles/bfcm-campaigns-that-convert
- fudge.ai BFCM examples https://www.fudge.ai/blog/black-friday-shopify-landing-page-examples/ ;
  Tapcart LSKD case https://www.tapcart.com/case-studies/lskd
- Sibling references: `references/offers/price-presentation.md` (PP1 to PP5, PP11, PP22),
  `references/offers/urgency-scarcity.md` (UR2, UR3, UR7, UR10 to UR13),
  `references/offers/offer-types.md` (flash-sale, clearance, OF3, OF10),
  `references/offers/offer-ledger.md`, `references/design-rules.md` (N9),
  `references/proof/proof-ledger.md`, `references/assets/image-jobs-by-page-type.md`
