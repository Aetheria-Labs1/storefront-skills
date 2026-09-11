# Homepage

The store's front door. Visitors arrive by typing the brand, clicking a
brand search result, following a bio link or returning as customers, at every
awareness level at once. The page's job is routing: say what the store sells
and for whom in one screen, show the breadth of the catalogue, surface best
sellers, offer the story for those who want it, and send each visitor to a
collection, a best seller or a finder. It is never the destination for cold
paid traffic (OPERATOR: Nik Sharma,
https://www.nik.co/resources/the-paid-media-bible-how-to-optimize-audiences-creative-and-your-website).
Composition depth and the editorial-not-catalog rule live in
`references/generate-homepage.md`; this file is the contract.

## Identify it

Signals in the brief: "homepage", "home page", "front page", "store home";
no campaign, no single SKU, whole-store scope.

Near neighbours:

- `collection-landing`: one category named; use it (index tie-break).
- `brand-story-founder`: the story is the page; a homepage links to it.
- `offer-page` or `sale-clearance-flash`: a live promotion is the page;
  the homepage points at it with one static block.
- Branded-search landing (`pdp` variant): for "[brand] [product]" queries a
  product page beats a homepage; for "[brand]" alone the homepage must show
  a best seller, guarantee and delivery promise in the first screen
  (OPERATOR: MHI 6.8% vs 5.1%,
  https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/).

## Anatomy

Sections between chrome: 7 to 10. Word budget 200 to 500.

1. `announcement` (chrome, conditional: a verified shipping or returns fact,
   or one live campaign with an end date). One line, no countdown.
2. `header` (mandatory). Full navigation from `lexsis_brand.navigation`
   showing product categories, not a single "Shop" link, and a visible
   search field. RESEARCH: 22% of sites hide search
   (https://baymard.com/blog/ecommerce-homepage-ux).
3. `hero` (mandatory). What the store sells, for whom, one differentiator,
   one primary path CTA; static, not an autorotating carousel. RESEARCH:
   static sections perform as well as a well-built carousel and 46% of
   carousels have usability issues (https://baymard.com/blog/homepage-carousel).
   Observed: AG1's hero is an outcome headline, one sentence, CTA, guarantee
   line (internal teardown audit, 2026-09-10).
4. `trust-bar` (recommended). Three verified facts: shipping, returns,
   guarantee or certification. Or `press-marquee` when linked press exists.
5. `product-grid` categories (mandatory). "Shop by" tiles showing catalogue
   breadth with representative product photos and creative-but-clear names;
   RESEARCH: sites that fail to show breadth are misjudged by visitors
   (Baymard homepage research above).
6. `product-grid` best sellers (mandatory). Four to eight products from
   orders data with price, rating and count where reviews exist, quick-add
   on single-variant items. RESEARCH: NN/g's homepage research recommends a
   best sellers category for every retailer
   (https://www.nngroup.com/articles/ecommerce-homepages-listing-pages/).
7. `story` (recommended). A brand story teaser in two to four sentences
   with a link to `brand-story-founder`; the manifesto-first hero of The
   Whole Truth is the alternative when the brand is the differentiator
   (teardown 29).
8. `review-summary` (mandatory when the store has 5 or more reviews). Store
   or best-seller average with count, two or three dated quotes, link to the
   full reviews. Omit and record the omission when no reviews exist.
9. `press-marquee` (conditional: verified, linked editorial coverage).
   Three to six monochrome logos, each linking to its article.
10. `ugc-grid` (conditional: rights-cleared customer media). Six to twelve
    tiles with handles.
11. `quiz` (conditional: catalogue with choice complexity and a routing quiz
    exists). Finder entry with one CTA.
12. `offer` (conditional: one live campaign with a verified end). The
    campaign as a static block linking to its own page; never the only route
    to it.
13. `email-capture` (recommended). One field; the incentive only when a
    `first-order` row is verified.
14. `footer` (mandatory). Policies, returns link, contact, social, payment
    icons, newsletter.

## Workflow

### Context reads
1. `lexsis_brand.navigation` first: header links (categories, not one
   "Shop"), footer columns, the collection hierarchy for the category
   tiles. `lexsis_brand.brand_kit` for tokens, logo, voice and banned
   phrases; `lexsis_brand.context` for the `theme_id`.
2. `lexsis_catalog.list` for best sellers (orders-ranked where the tool
   exposes it, else the merchant's list): four to eight products with price
   and media count; `lexsis_catalog.get` per product for the identity image
   and any lifestyle image; one representative product with an image per
   category tile. Record gaps for the merchant message.
3. `lexsis_catalog.reviews_status`, then `lexsis_catalog.reviews` for the
   store or best-seller average and count; band B2 or higher shows an
   average; B0 omits the section and records the omission
   (`references/proof/reviews-sourcing.md`).
4. Press: fetch every claimed outlet URL and write ledger rows per
   `references/proof/press-and-media-mentions.md`; count `verified`
   editorial rows within 24 months. UGC: library assets with a rights row
   (`references/proof/ugc-rights-and-display.md`).
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`, one call
   each for `hero`, `lifestyle`, `banner`, `product-shot`, `logo`,
   `social-proof`; record counts; then semantic "<brand> product in use at
   home"; view candidates with `lexsis_assets.view`
   (`references/assets/asset-sourcing-sequence.md`).
6. Policy page URL for trust-bar facts; the offer ledger for one campaign
   block and the `first-order` incentive
   (`references/offers/campaign-calendar.md` for the campaign's hero and
   urgency rules); `lexsis_capture.form_schemas` for the email capture.
7. `lexsis_design.islands` for the active catalog; `lexsis_workspace.credits`
   before planning a `hero_bg` (`references/assets/generation-policy.md`).

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
off unless the plan names that motion moment (N10). Composition depth is in
`references/generate-homepage.md`; copy ceilings follow
`references/copy/copy-frameworks.md` and
`references/anti-patterns/copy-anti-patterns.md`.

**`announcement`** (conditional: verified fact or one live campaign)
- Purpose: one line, a shipping or returns fact or the campaign end date as
  text.
- Media: no (chrome).
- Island: the SiteHeader announcement strip, one message, no dismissal;
  never CountdownTimer; resolve from `lexsis_design.island_schema`.
- Copy: under 60 characters.
- Decide with: a `policy-fact` or offer-ledger row.

**`header`**
- Purpose: categories and a visible search field.
- Media: logo from the brand kit; a light logo file for the transparent
  variant.
- Island: SiteHeader with categories from `lexsis_brand.navigation`; the
  transparent treatment only when the hero is the plan's full-bleed bold
  moment; never SiteHeader and Navbar together; resolve from
  `lexsis_design.island_schema`; preset `siteheader/sticky-light` or
  `siteheader/transparent-dark`.
- Copy: category labels 3 words or fewer.
- Decide with: the navigation result and the bold-moment line in the plan.

**`hero`**
- Purpose: what the store sells, for whom, one differentiator, one primary
  CTA, a guarantee line.
- Media: yes; job `in-use` (bespoke lifestyle, product legible in one second,
  face toward copy or product), treatment `editorial-lifestyle`
  (`references/assets/image-jobs-by-page-type.md`, section 5). Search library
  `hero`, then `lifestyle`, then catalog lifestyle media of a best seller,
  then merchant upload; stock never (people). Generation: `hero_bg` (ALLOW)
  behind a real cut-out, which makes the hero the `product-in-context`
  alternate; `product_lifestyle` is ASK and needs the merchant's yes for this
  slot. Missing: tell the merchant (in-use lifestyle, 16:9 plus 4:5, one
  image) and offer upload, `hero_bg` or the ASK composite; if skipped, the
  best catalog identity image serves as a packshot hero with "hero pending
  merchant media" in the plan. No-go: a carousel; stock people; a video with
  sound; text in the image. View every candidate with `lexsis_assets.view` and
  run the section fit review; view it beside the category and best-seller
  images so the page reads as one shoot.
- Island: none by default (static split `<picture>` with copy beside the
  photograph, `references/assets/slot-spec.md`); HeroMedia only as the
  full-bleed bold moment, image mode, autoplay off; never carousel mode;
  resolve from `lexsis_design.island_schema`.
- Copy: H1 10 words or fewer (what and for whom); subhead 20 words; one CTA
  to the main path; guarantee line from the ledger.
- Decide with: `lexsis_assets.view` at both crops; the plan's bold moment;
  the policy row for the guarantee line.

**`trust-bar`** (recommended) or **`press-marquee`**
- Purpose: three verified facts, or three to six linked editorial logos.
- Media: facts stand as text with hairlines (icons only from the page's single
  inline SVG set); press logos are the outlets' own monochrome SVGs from
  library `logo`, each inside a link to the article
  (`references/proof/press-and-media-mentions.md`). Generation: never (GN5).
  Missing logos: ask the merchant for the outlet files or article URLs; fewer
  than three verified rows renders quotes instead. View every candidate with
  `lexsis_assets.view` and run the section fit review before use.
- Island: none; a static HTML row of linked logos (the Marquee island is
  deprecated, and N10 forbids a ticker outside the plan's motion moment).
- Copy: facts 8 words each; caption "In the press".
- Decide with: `policy-fact` rows; count of verified press rows.

**`product-grid`** categories
- Purpose: "Shop by" tiles showing catalogue breadth.
- Media: yes; one `context` image per tile from library `lifestyle` or the
  collection's representative product identity image from catalog media; one
  aspect across tiles; four to six tiles. Generation: `card_bg` (ALLOW) only
  behind a real product cut-out. Missing: tell the merchant (one image per
  collection, one aspect, count) and offer upload or a cut-out on `card_bg`;
  if skipped, that collection is a text link in the header, never an icon tile
  or coloured square. View every candidate with `lexsis_assets.view` and run
  the section fit review; view the grid images together so lighting,
  backgrounds and crops agree.
- Island: none (static tiles linking to collections).
- Copy: names creative but clear, 3 words or fewer.
- Decide with: the collection hierarchy and image availability per
  collection.

**`product-grid`** best sellers
- Purpose: four to eight products from orders data with price, rating and
  count, quick add on single-variant items.
- Media: yes; job `identity` per product from catalog media. Generation: none.
  Missing: name the products without an image and offer upload; if skipped,
  they leave the rail. View every candidate with `lexsis_assets.view` and run
  the section fit review; view the grid images together so lighting,
  backgrounds and crops agree.
- Island: FeaturedCollectionStage, or ProductCarousel when the brief wants
  boxed cards and there are four or more products; decide from best-seller
  count, image availability, variant axes and whether the hero already took
  the bold moment; quick add only with `head.use_cart_v2`; motion off;
  resolve from `lexsis_design.island_schema`; preset
  `productcarousel/cards-quiet` in the carousel case.
- Copy: section heading 6 words or fewer; prices from the catalog; rating
  and count only at 5 or more reviews per product.
- Decide with: best-seller count, image availability, review band per
  product, the bold-moment line.

**`story`** (recommended)
- Purpose: a two to four sentence teaser linking to `brand-story-founder`.
- Media: yes; job `founder-or-team` or `context` (workshop, kitchen, place),
  real and named, from library `lifestyle` or merchant upload; never stock or
  generated (GN3). Missing: tell the merchant (a real photo of the founder,
  team or place, 4:5 or 3:2, one image) and offer upload only ("needs a real
  photo"); if skipped, the teaser becomes a signed two-sentence line under the
  review module and the story link stays in navigation. View every candidate
  with `lexsis_assets.view` and run the section fit review before use.
- Island: none.
- Copy: two to four sentences with a date, a place or a name; one link.
- Decide with: a viewed photo with approval recorded in the ledger.

**`review-summary`** (mandatory at 5 or more reviews)
- Purpose: real average with count, two or three dated quotes, link to all
  reviews.
- Media: quotes are the artefact; reviewer photos only real with consent,
  else CSS initials (`references/proof/proof-ledger.md`, display rule 3).
- Island: ReviewCarousel bound to an active collection; decide grid versus
  strip from quote length and count; average and count as HTML from
  `lexsis_catalog.reviews` for the same scope; autoplay off; resolve from
  `lexsis_design.island_schema`; preset `reviewcarousel/grid-flat` or
  `reviewcarousel/strip-compact`.
- Copy: verbatim, dated; heading names the scope ("Rated 4.6 by 212
  customers").
- Decide with: `reviews_status` band; B0 omits and records under
  "Mandatory sections omitted".

**`press-marquee`** (conditional: verified linked coverage)
- Purpose: three to six monochrome logos linking to their articles.
- Media: outlet SVGs from library `logo`, each linked; never generated.
  Missing: ask the merchant for outlet files or URLs; fewer than three renders
  quotes. View every candidate with `lexsis_assets.view` and run the section
  fit review before use.
- Island: none; static linked row (the Marquee island is deprecated).
- Copy: caption "In the press"; year on any item older than 12 months.
- Decide with: count of `verified` editorial press rows.

**`ugc-grid`** (conditional: rights-cleared media)
- Purpose: six to twelve customer tiles with handles.
- Media: yes; job `ugc` from library `social-proof` with a ledger `P` row per
  tile, one aspect, original grading; never staff or stock as customers.
  Missing: tell the merchant which rights requests are open
  (`references/proof/ugc-rights-and-display.md`); the section waits, never
  renders pending UGC. View every candidate with `lexsis_assets.view` and run
  the section fit review; view the tile images together so lighting,
  backgrounds and crops agree.
- Island: none for the grid; GalleryLightbox mounted once for expansion;
  resolve from `lexsis_design.island_schema`.
- Copy: handle and first name per tile; labelled as customer content.
- Decide with: count of `verified` UGC rows (six or more).

**`quiz`** (conditional: choice complexity and a routing quiz)
- Purpose: finder entry with one CTA.
- Media: yes; one `context` image beside the entry from library `lifestyle`.
  Missing: offer upload; if skipped, the entry is the hero's secondary CTA.
  View every candidate with `lexsis_assets.view` and run the section fit
  review before use.
- Island: FunnelRuntime with a published funnel from
  `lexsis_capture.funnel_templates`; resolve from
  `lexsis_design.island_schema`.
- Copy: one line and one CTA.
- Decide with: an existing funnel template.

**`offer`** (conditional: one live campaign with a verified end)
- Purpose: the campaign as one static block linking to its own page.
- Media: yes; the campaign's real imagery (catalog identity of the featured
  product or library `banner`). Missing: offer upload; if skipped, the
  campaign is the announcement line alone. View every candidate with
  `lexsis_assets.view` and run the section fit review before use.
- Island: none; never CountdownTimer on the homepage.
- Copy: one sentence with the end date as text; one CTA.
- Decide with: the offer-ledger row and its `endsAt`.

**`email-capture`** (recommended)
- Purpose: one field; the incentive only when a `first-order` row exists.
- Media: a best-seller image beside the form; the form alone is the object
  when none is spare (N8).
- Island: EmailCapture, one per page, or the Footer newsletter layout
  (never both); resolve from `lexsis_design.island_schema`; preset
  `footer/newsletter-split-light` in the footer case.
- Copy: one line and one field.
- Decide with: `lexsis_capture.form_schemas` and the offer ledger.

**`footer`**
- Purpose: policies, returns link, contact, social, payment marks,
  newsletter.
- Media: logo; payment marks as issuer artwork only.
- Island: Footer with columns from `lexsis_brand.navigation`; resolve from
  `lexsis_design.island_schema`; preset `footer/columns-dark`.
- Decide with: the navigation result.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` per best seller, one image per category tile | the bespoke `in-use` hero, `context` tiles that show a scene | reuse the best product lifestyle shot as the hero; generate `hero_bg` (ALLOW) behind a cut-out, `product_lifestyle` (ASK) with the merchant's yes, `card_bg` (ALLOW) behind a cut-out for a tile; ask the merchant to upload lifestyle and tile images; a packshot hero or text links only on the merchant's call |
| asset library | `hero` and `lifestyle` candidates, `logo` SVGs for press, `social-proof` UGC with rights | founder or team photo, press logos with fetched URLs | ask the merchant to upload with written approval and article URLs; press quotes instead of logos; the story teaser shrinks to a signed line only on the merchant's call |
| generation | backdrops, textures, composites only | product, people, results, logos, text | never; these are "needs a real photo" in the merchant message |

With minimal assets the page is a header with categories and search, a split
hero built from the best product photo, four category tiles from product
images, a best-seller stage of real cards, three policy facts, an email field
and a footer; at most one generated asset (`hero_bg`), never more than four
per page, and every missing asset listed in the plan and the draft summary
with upload, generate or skip. Every asset, found or generated, was viewed and
passed the section fit review before use.

## Above the fold (390px)

In order: header with categories and search; H1 stating what and for whom;
one sentence with the differentiator; one primary CTA to the main path; a
guarantee or delivery line under the CTA; the trust row or the first category
tile peeking. Observed recipe: "Goodbye X, hello Y" headline, one sentence,
CTA, guarantee line, three-item trust row (internal teardown audit, 2026-09-10).

Must not appear: an autorotating carousel, a popup on load (RESEARCH: 55% of
sites show aggressive interstitials on load, Baymard homepage UX above), a
countdown, a discount pill, stock photography, a hero video with sound.

## Proof

Modules: 2 to 3. Aggregate and linked, never long testimonials.

- `review-summary` (required when reviews exist): real average to one
  decimal with count; distribution when 20 or more reviews
  (`references/proof/proof-ledger.md` display rule 3).
- `press-logo-linked` or `press-quote-linked` (recommended): editorial
  coverage within 24 months, each logo linked; wire releases never qualify
  (`references/proof/press-and-media-mentions.md`).
- `expert-quote` with a credential line (conditional: written approval and
  disclosed connection); AG1 places four under the hero.
- `ugc-photo` grid (conditional: rights).
- `policy-fact` in the trust bar.
- Never: `social-proof-popup`, `live-viewer-count`, `stock-count`,
  `press-logo-unlinked`, "trusted by thousands".

Zero-review store: trust-bar facts, a founder note in the `story` teaser,
verified press if any; no review-shaped element and the `review-summary`
section is listed under "Mandatory sections omitted" with the reason
(`references/proof/reviews-sourcing.md`).

## Offer and CTA

- CTAs: 2 to 3 primary path CTAs to different destinations (a collection,
  best sellers, the finder or the story), pattern `shop-collection`. Cards
  add their own. No sticky CTA.
- First CTA in the hero.
- Price reveal: optional; best-seller cards show prices; the hero does not
  lead with price.
- Urgency: none. A homepage carries no countdown, no stock line and no
  "ends tonight"; the campaign page holds the deadline.
- Offer types that fit: `none`, `free-shipping` in the announcement and
  trust bar, `first-order` in the email capture, `subscribe-save` and
  `bundle` as best-seller card facts, `loyalty` and `referral` links,
  `gift-card`, `bnpl` line on cards, one `percent-off` or `fixed-off`
  campaign block pointing to the sale page during a verified window.
- Offer types that do not fit: `flash-sale`, `clearance`, `mystery`,
  `pre-order-price`, `price-lock`, `bogo`, `bundle-decoy`, `trial-sample`,
  `student-military`.
- One campaign block per page (`references/offers/offer-ledger.md` rule 6).

## Imagery

Required jobs: `identity` (best-seller cards from catalog media) and
`in-use` (bespoke lifestyle hero with the product legible). Recommended:
`context` for category tiles, `founder-or-team` in the story teaser, `ugc`
with rights.

Hero treatment: `editorial-lifestyle` or a split layout with copy beside a
product photograph; the product identifiable in one second; face gaze toward
copy or product. No stock people. Video optional as a muted 6 to 15 second
loop with a pause control and a poster still, never the LCP. Minimum 6 image
slots: hero, four to six category tiles, best-seller cards. Alternate
full-bleed and contained sections for rhythm (`references/generate-homepage.md`).

## Copy

Framework: AIDA in the hero (attention by outcome, desire by identity), FAB in
the trust and category strips.

- H1 10 words or fewer, says what and for whom; no brand-only headline.
- Subhead 20 words or fewer carrying the differentiator.
- Category names creative but clear ("The weekend edit" beside "Shirts"), 3
  words or fewer.
- Section headings sentence case, 6 words or fewer.
- Reading level grade 6 to 8; "you" outnumbers the brand name.
- Vocabulary: no "welcome to", no "discover our world", no "premium quality"
  without a fact; no ad-style urgency ("hurry", "ends soon").
- Copy speaks to identity and values, not features alone; the page reads as
  a magazine cover, not a spreadsheet (`references/generate-homepage.md`).

## Never

- Never use an autorotating carousel or make any content reachable only
  through a carousel slide.
- Never fire a popup on load or within 10 seconds.
- Never send cold paid social traffic to the homepage.
- Never show a countdown, stock count or "ends tonight" line.
- Never hide search or collapse categories into one "Shop" link.
- Never show only one product type when the catalogue is broad.
- Never use stock lifestyle photography.
- Never render stars without a count or a "trusted by" line without a ledger
  row.
- Never point every CTA at the same destination; the homepage routes.
- Never lead with a discount in the hero; the campaign gets one static block.

## Examples

- AG1, https://drinkag1.com/: outcome headline with CTA and guarantee line,
  trust row, expert quotes with credential lines under the hero, value stack,
  dated review quotes inside benefit tabs, FAQ, UGC at the end.
- The Whole Truth, https://thewholetruthfoods.com/: manifesto-first hero,
  category tiles, factory tour as a trust module, celebrity names as names
  rather than logos, COD line in the footer. Weakness: no product or price
  in the first three sections.
- boAt, https://www.boat-lifestyle.com/: category tiles plus a deal grid
  with percent-off on every card; a deal-first pattern to avoid outside a
  verified sale window.

## Checklist

```json
{
  "page_type": "homepage",
  "aliases": ["home", "home page", "front page", "store home"],
  "funnel_stage": ["tof", "retention"],
  "awareness": ["unaware", "problem-aware", "solution-aware", "product-aware", "most-aware"],
  "traffic": ["direct", "organic", "google-search"],
  "sections": { "min": 7, "max": 10 },
  "mandatory_sections": ["header", "hero", "product-grid", "review-summary", "footer"],
  "recommended_sections": ["trust-bar", "story", "press-marquee", "ugc-grid", "email-capture", "quiz", "offer"],
  "forbidden_sections": ["countdown", "stock-indicator", "buy-box", "dateline", "hook", "agitation", "offer-bridge", "final-offer", "savings-math"],
  "nav": "full",
  "price_above_fold": "optional",
  "cta": { "min": 2, "max": 3, "first_after_section": 0, "sticky": "forbidden", "copy_pattern": "shop-collection" },
  "proof": { "min_modules": 2, "max_modules": 3, "required_kinds": ["review-summary"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "stock-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "in-use"], "hero": "editorial-lifestyle", "video": "optional", "min_images": 6 },
  "copy_framework": ["aida", "fab"],
  "offer_compat": { "allowed": ["none", "free-shipping", "first-order", "subscribe-save", "bundle", "loyalty", "referral", "gift-card", "bnpl", "percent-off", "fixed-off"], "forbidden": ["flash-sale", "clearance", "mystery", "pre-order-price", "price-lock", "bogo", "bundle-decoy", "trial-sample", "student-military"] },
  "urgency": "none"
}
```

## Sources

- internal research audit (2026-09-10) section 5 block 20; section 2 row 20; section 4b rule 10.
- internal research audit (2026-09-10) teardowns 28, 29 and Part D.
- internal research audit (2026-09-10) sections 5, 10, 13.
- internal research audit (2026-09-10) sections 1.1, 2.1, 2.6.
- `references/generate-homepage.md`, `references/proof/press-and-media-mentions.md`.
- Baymard homepage UX: https://baymard.com/blog/ecommerce-homepage-ux
- Baymard homepage carousel: https://baymard.com/blog/homepage-carousel
- Baymard navigation: https://baymard.com/blog/ecommerce-navigation-best-practice
- Baymard homepage and category research: https://baymard.com/research/homepage-and-category-usability
- NN/g homepages and listing pages: https://www.nngroup.com/articles/ecommerce-homepages-listing-pages/
- Nik Sharma paid media bible: https://www.nik.co/resources/the-paid-media-bible-how-to-optimize-audiences-creative-and-your-website
- MHI landing page vs product page: https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/
- ecommercecircle branded-search posture: https://www.ecommercecircle.com.au/shopify-customer-awareness-stages/
