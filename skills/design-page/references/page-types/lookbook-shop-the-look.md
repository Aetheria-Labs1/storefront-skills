# Lookbook and shop the look

Editorial imagery that is shoppable: outfits, rooms or routines photographed
as looks, each with the items tagged and purchasable beside the image.
Visitors arrive from an Instagram bio link, a "new collection" email, a
homepage module or a PDP module, solution-aware and browsing for inspiration.
The page sells through the photography; copy is two lines per look. The job
is to move the shopper from a look to two or three items in the cart, and
from one look to the next. Fashion and home are the main verticals
(`references/vertical-fashion.md` holds grid layouts and campaign pacing).

## Identify it

Signals in the brief: "lookbook", "shop the look", "outfit", "styled",
"editorial", "new drop", "room inspiration", "complete the look"; fashion,
home or beauty routines; a catalogue where context drives the purchase.

Near neighbours:

- `collection-landing`: filters and a grid; choose it when the shopper
  knows the category and wants to compare attributes.
- `homepage`: the whole store; a lookbook is one story.
- `bundle-kit`: a fixed set with savings math; a "shop the whole look" CTA
  is a bundle moment inside this page, not the page.
- `ugc-creator-collab`: creator or customer video is the hero and the proof;
  a lookbook is the brand's own photography.
- Editorial magazine page (`references/generate-editorial.md`): long-form
  narrative with two or three commerce moments per 1,000 words; a lookbook
  has a commerce moment under every image.

## Anatomy

Sections between chrome: 5 to 8. Word budget 100 to 300. Images 10 to 20 in
3 to 5 looks; 15 to 30 products tagged.

1. `header` (mandatory). Full navigation; lookbook visitors browse onward.
2. `hero` (mandatory). Named story ("Summer in the city"), one line of mood
   copy, optional "Shop all looks" anchor. Full-bleed image with the
   product legible; no price.
3. `lookbook` (mandatory). Ten to twenty images in one aspect ratio (4:5
   portrait for fashion, 4:3 for home), each with two or three hotspots at
   most, sitting on the product. Mixed-size grids follow
   `references/vertical-fashion.md`. OPERATOR: hotspot limits and aspect
   consistency per shopidevs
   (https://shopidevs.com/how-to-create-lookbook-in-shopify/).
4. `shop-the-look` (mandatory). Under each image, cards for every tagged
   item with price, variant swap where colour or size matters, quick-add or
   quick view; hotspots alone fail on mobile. An "Add the whole look" CTA
   with a computed saving when a bundle row is verified.
5. `story` (optional). One editorial paragraph or pull quote between looks;
   60 words or fewer.
6. `video` (optional). Ten-second styling clips interleaved, muted, click to
   play, captions.
7. `ugc-grid` (conditional: rights-cleared customer photos of the looks).
   Six to eight tiles with handles.
8. `email-capture` (recommended). "Early access to the next drop", one
   field, mid-gallery or at the end.
9. `product-grid` (recommended). "Shop the collection" grid of every item
   featured, at the end, with the same card anatomy as
   `references/product-grid.md`.
10. `footer` (mandatory).

## Workflow

### Context reads
1. `lexsis_brand.context` for the `theme_id`; `lexsis_asset_library.search`
   with `mode: "tags"`, one call each for `lifestyle`, `hero`, `flat-lay`,
   `product-shot`, `social-proof`; record counts; then semantic "<story
   name> on model outdoors" and "<room> styled with <category>". View every
   candidate with `lexsis_assets.view`; group frames into looks (wide,
   medium, detail) in one aspect (4:5 fashion, 4:3 home). A creator or
   customer in a brand-owned post is UGC and needs a rights row (AS13,
   `references/proof/ugc-rights-and-display.md`).
2. `lexsis_catalog.get` per tagged item: first media item as the card
   identity image, price, options, variant images and availability per size
   and colour. An item unavailable in every variant is not tagged; a
   sold-out variant stays visible and disabled.
3. `lexsis_brand.navigation` for header and footer; `lexsis_brand.brand_kit`
   for tokens, voice and banned phrases; `references/vertical-fashion.md`
   for grid layouts and pacing.
4. `lexsis_catalog.reviews_status`, then `lexsis_catalog.reviews` per tagged
   item; card average and count only at 5 or more reviews
   (`references/proof/reviews-sourcing.md`).
5. Policy page URL for the returns and exchange line beside quick add; the
   offer ledger for any verified "whole look" bundle saving
   (`references/offers/offer-ledger.md`).
6. Real video clips in the library with posters
   (`references/assets/video-rules.md`); no clip, no `video` section.
7. `lexsis_design.islands` for the active catalog; `lexsis_workspace.credits`
   is read, but generation is almost never used here: `in-use` is
   identity-bound and people are never generated
   (`references/assets/generation-policy.md`).

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
- Purpose: full navigation; lookbook visitors browse onward.
- Media: logo from the brand kit.
- Island: Navbar; the transparent treatment only when the hero is the
  plan's full-bleed bold moment; links from `lexsis_brand.navigation`;
  resolve from `lexsis_design.island_schema`; preset `navbar/sticky-light`
  or `navbar/transparent-dark`.
- Copy: nav labels only.
- Decide with: the bold-moment line in the plan.

**`hero`**
- Purpose: the story name and one line of mood over a full-bleed image.
- Media: yes; job `in-use` (on-model or in-room, product legible), treatment
  `editorial-lifestyle`, natural light, same grading as the gallery
  (`references/assets/image-jobs-by-page-type.md`, section 5). Search library
  `hero`, then `lifestyle`, then merchant upload of campaign photography.
  Generation: none (people and product, "needs a real photo"). Missing: tell
  the merchant (one editorial frame at 1920 wide with a portrait crop,
  `references/assets/slot-spec.md`) and offer upload; if skipped, the first
  look's wide frame is the hero and the plan records it. No-go: a
  white-background packshot; price or text on the image; a carousel. View
  every candidate with `lexsis_assets.view` and run the section fit review;
  view it with the first look's frames so grading and light agree.
- Island: HeroMedia in image mode when the hero is the full-bleed bold
  moment, autoplay off, never carousel mode; otherwise a static `<picture>`;
  resolve from `lexsis_design.island_schema`.
- Copy: story name 3 words or fewer; one line 15 words or fewer; optional
  anchor "Shop all looks".
- Decide with: a viewed frame that passes the hero slot spec.

**`lookbook`**
- Purpose: ten to twenty images in three to five looks, each with two or
  three hotspots on the product.
- Media: yes; jobs `in-use` and `context` per look (wide, medium, `detail`),
  one aspect across the gallery, under 500 KB each, lazy below the first look.
  Search library `lifestyle` and `flat-lay`, then merchant upload. Generation:
  none (GP14). Missing: tell the merchant which looks have fewer than two
  frames (job, aspect, count per look) and offer upload; if skipped, that look
  leaves, and a page under three looks retypes to `collection-landing` with
  the merchant's agreement. No-go: mixed aspects; packshots in the gallery; a
  PDF or flipbook; more than four hotspots on one image. View every candidate
  with `lexsis_assets.view` and run the section fit review; view the look
  images together so lighting, backgrounds and crops agree.
- Island: static `<figure>` grid per look with HTML hotspot buttons on the
  product; GalleryLightbox mounted once per page for expansion;
  MediaCarousel for a look with three or more frames on mobile; decide from
  frame count per look and the vertical's grid layout; swipe and dots on,
  autoplay off; looks stack vertically, never one carousel; resolve from
  `lexsis_design.island_schema`.
- Copy: two lines per look at most, mood not features.
- Decide with: verified frame count per look (two or more) and total (ten
  or more); hotspot count per image.

**`shop-the-look`**
- Purpose: cards for every tagged item under each image; hotspots alone
  fail on mobile.
- Media: yes; job `identity` per item from catalog media, `swatch` chips from
  catalog hex where colour matters, `size-reference` line (model height and
  size worn) as HTML. Generation: none. Missing: name the items without an
  image and offer upload; if skipped, the item is untagged and the merchant is
  told. No-go: a card that hides the sold-out state. View every candidate with
  `lexsis_assets.view` and run the section fit review; view the card images
  together so lighting, backgrounds and crops agree.
- Island: QuickAdd per item; decide direct add or picker from the variant
  axes, cart feedback through `head.use_cart_v2`; "Add the whole look" only
  with a bundle offer-ledger row and a supported bundle island resolving
  live variants; resolve from `lexsis_design.island_schema`.
- Copy: fabric, fit, size range or dimensions under 10 words; price on
  every card; "Free exchanges within 30 days" from the policy row beside
  the first quick add of each look; labels "Add to bag", never "Shop now".
- Decide with: `lexsis_catalog.get` availability per variant; the bundle
  ledger row.

**`story`** (optional)
- Purpose: one editorial paragraph or pull quote between looks.
- Media: no; the surrounding looks carry the imagery.
- Island: none.
- Copy: 60 words or fewer; a pull quote is one sentence.
- Decide with: whether the merchant's voice notes hold a line worth
  quoting; otherwise skip.

**`video`** (optional)
- Purpose: ten-second styling clips interleaved.
- Media: real footage only from the library with a poster frame that shows the
  product (`references/assets/video-rules.md`); never generated. No clip means
  no section; the merchant is told a clip could be uploaded. View every
  candidate with `lexsis_assets.view` and run the section fit review before
  use.
- Island: VideoPlayer, click to play, muted, captions when there is speech;
  decide aspect from the clip; resolve from `lexsis_design.island_schema`.
- Copy: one caption line.
- Decide with: a viewed clip and poster in the library.

**`ugc-grid`** (conditional: rights-cleared customer photos of the looks)
- Purpose: six to eight tiles with handles.
- Media: yes; job `ugc` from library `social-proof` with a ledger `P` row per
  tile, one aspect, original grading; never staff as customers. Missing: tell
  the merchant which rights requests are open; pending UGC never renders. View
  every candidate with `lexsis_assets.view` and run the section fit review;
  view the tile images together so lighting, backgrounds and crops agree.
- Island: none for the grid; the page's GalleryLightbox serves expansion.
- Copy: handle per tile; labelled as customer content.
- Decide with: count of `verified` UGC rows (six or more).

**`email-capture`** (recommended)
- Purpose: early access to the next drop, one field, mid-gallery or at the
  end.
- Media: a look frame beside the form; the form alone is the object when
  none is spare (N8).
- Island: EmailCapture, one per page, or the Footer newsletter layout; no
  incentive without a ledger row; resolve from
  `lexsis_design.island_schema`; preset `footer/newsletter-split-light` in
  the footer case.
- Copy: one line and one field.
- Decide with: `lexsis_capture.form_schemas`.

**`product-grid`** (recommended)
- Purpose: "Shop the collection": every featured item at the end.
- Media: yes; job `identity` per item from catalog media, same aspect as the
  cards above (`references/product-grid.md`). View every candidate with
  `lexsis_assets.view` and run the section fit review; view the grid images
  together so lighting, backgrounds and crops agree.
- Island: ProductCarousel with four or more items, FeaturedCollectionStage
  when the merchant wants one visual stage, the card composition with
  QuickAdd for three or fewer; decide from tagged item count and image
  availability; motion off; resolve from `lexsis_design.island_schema`;
  preset `productcarousel/cards-quickadd-light`.
- Copy: heading 6 words or fewer; prices from the catalog.
- Decide with: tagged item count.

**`footer`**
- Purpose: policies, contact, social.
- Media: logo only.
- Island: Footer with links from `lexsis_brand.navigation`; resolve from
  `lexsis_design.island_schema`; preset `footer/simple-light` or
  `footer/columns-dark`.
- Decide with: the navigation result.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` per tagged item, variant images, on-model product shots | wide `context` frames that place several items in one scene | reuse the strongest on-model catalog frame as a look's medium shot; ask the merchant to upload campaign originals; a look is cut only on the merchant's call |
| asset library | `lifestyle` and `hero` campaign frames, `social-proof` UGC with rights | consistent grading across looks, detail frames, styling clips | ask the merchant to upload detail frames and clips; `video` and `detail` are skipped only on the merchant's call; never stock people |
| generation | backdrops, textures, composites only | product, people, results, logos, text | never; a composite (`product_composite`) is `context` only and never a look frame |

With minimal assets the page is a header, one full-bleed frame, three looks of
two real frames each with quick-add cards, an email field and a footer; zero
generated assets is the expected outcome, and when fewer than six verified
lifestyle frames exist the merchant is told the count and offered upload or a
retype to `collection-landing`. Every asset, found or generated, was viewed
and passed the section fit review before use.

## Above the fold (390px)

In order: compact header; the story name and one line of mood copy over or
under a full-bleed image; the first look's image starting, with its hotspot
markers visible. The first product card should be one thumb-scroll away.

Must not appear: price in the hero, a countdown, a discount pill, a popup, a
white-background packshot as the hero, a text block longer than two lines,
autoplaying sound.

## Proof

Modules: 1 to 2. The imagery is the persuasion.

- `policy-fact` (required): returns and exchange window beside the quick-add
  ("Free exchanges within 30 days"), sourced from the policy page
  (`references/proof/proof-ledger.md`). Fit risk is the fashion shopper's
  main doubt.
- `review-summary` on cards for items with 5 or more reviews; average with
  count.
- `ugc-photo` (conditional: rights): customers wearing or using the look.
  RESEARCH: shoppers are 32% more likely to buy clothing modelled by a
  fellow customer (Yotpo, https://www.yotpo.com/blog/visual-reviews/).
- Never: `social-proof-popup`, `live-viewer-count`, `stock-count` in copy,
  `press-logo-unlinked`, testimonial carousels.

Zero-review store: the returns line only; cards show no stars.

## Offer and CTA

- CTAs: one per tagged item (quick-add, pattern `add-to-cart`, "Add to bag")
  and at most one standalone anchor in the hero ("Shop all looks"). One
  "Add the whole look" per look when the bundle is verified. No sticky CTA.
- Price reveal: on every card; never in the hero or on the image.
- Urgency: none. Edition sizes ("200 pieces") belong to a drop campaign and
  need a live stock binding; not on a lookbook.
- Offer types that fit: `none`, `bundle` ("shop the whole look" with
  computed savings), `free-shipping` line beside quick-add, `bnpl` line for
  items over $80 or ₹3,000, `limited-edition` as a factual label with a
  verified edition size, `loyalty` early access, `gift-card`.
- Offer types that do not fit: `percent-off`, `fixed-off`, `flash-sale`,
  `clearance`, `bogo`, `mystery`, `trial-sample`, `subscribe-save`,
  `referral`, `student-military`, `pre-order-price`, `price-lock`,
  `bundle-decoy`, `cashback`, `charity`.
- OPERATOR: outfitting lifts AOV (Rhone +39% AOV with Stylitics, vendor
  claim, https://stylitics.com/resources/blog/digital-lookbook/); measure
  multi-item baskets, not clicks.

## Imagery

Required jobs: `identity` per tagged item (catalog media on cards), `in-use`
(on-model or in-room photography as the gallery), `context` (the room,
street or occasion at true scale). Recommended: `detail` (fabric, finish),
`texture`, `variation` swatches, `ugc` with rights, `size-reference` (model
height and size worn) for worn items, `swatch`.

Hero treatment: `editorial-lifestyle`, full-bleed, product legible, natural
light, consistent grading across every image; diverse models; no
white-background packshots in the gallery; wide, medium and detail per
look. Images under 500 KB each, lazy-loaded below the first look; alt text
names the scene and the products. Video optional. Minimum 10 image slots.
Studio to lifestyle balance for fashion is about 30/50/20 studio, lifestyle,
UGC (`references/assets/image-jobs-by-page-type.md`).

## Copy

Framework: story-lead micro-copy per look, FAB on cards.

- Story name 3 words or fewer; hero line 15 words or fewer.
- Two lines per look at most; mood, not features ("Linen for the hour
  before the heat").
- Card lines: fabric, fit, size range or dimensions in under 10 words.
- Reading level grade 6 to 8; sentence case; no ALL-CAPS labels.
- CTA labels "Add to bag", "View", "Add the whole look"; never "Shop now".
- Vocabulary: no "effortless", "elevate", "curated", "must-have".

## Never

- Never tag an out-of-stock or unavailable size without showing it as such.
- Never place more than four hotspots on one image, or hotspots that do not
  sit on the product.
- Never mix aspect ratios inside the gallery.
- Never ship a PDF or flipbook lookbook without product links.
- Never rely on hotspots alone; every image has cards beneath it.
- Never position hotspots for desktop only.
- Never use white-background packshots in the gallery.
- Never add a countdown or an edition count without a live binding.
- Never write more than two lines of copy per look.
- Never treat the lookbook as one carousel; looks stack vertically and each
  look is its own commerce moment (OPERATOR: Elara,
  https://joinelara.com/blog/the-complete-guide-to-shop-the-look-for-shopify-fashion-brands).

## Examples

- JD Sports "Shop the model", described by Stylitics,
  https://stylitics.com/resources/blog/digital-lookbook/: outfit imagery
  with every worn item tagged and shoppable, colour toggles in the card.
- Adidas shoppable lookbook via Publitas,
  https://www.publitas.com/blog/how-to-create-ecommerce-lookbook/:
  campaign photography with hotspots leading to product cards; the vendor
  reports a large sales lift, unverified.
- Shopify's lookbook guide with brand examples,
  https://www.shopify.com/blog/lookbooks-how-to-use-high-quality-lifestyle-photos-to-boost-sales:
  consistent grading, natural light and one aspect ratio across looks.

## Checklist

```json
{
  "page_type": "lookbook-shop-the-look",
  "aliases": ["lookbook", "shop the look", "shoppable gallery", "outfit page", "room inspiration", "complete the look"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["solution-aware"],
  "traffic": ["organic", "email", "influencer"],
  "sections": { "min": 5, "max": 8 },
  "mandatory_sections": ["header", "hero", "lookbook", "shop-the-look", "footer"],
  "recommended_sections": ["product-grid", "email-capture", "ugc-grid", "video", "story"],
  "forbidden_sections": ["buy-box", "countdown", "stock-indicator", "dateline", "hook", "problem", "agitation", "offer-bridge", "comparison", "us-vs-them", "savings-math"],
  "nav": "full",
  "price_above_fold": "forbidden",
  "cta": { "min": 0, "max": 1, "first_after_section": 0, "sticky": "forbidden", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 1, "max_modules": 2, "required_kinds": ["policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "stock-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "in-use", "context"], "hero": "editorial-lifestyle", "video": "optional", "min_images": 10 },
  "copy_framework": ["story-lead", "fab"],
  "offer_compat": { "allowed": ["none", "bundle", "free-shipping", "bnpl", "limited-edition", "loyalty", "gift-card"], "forbidden": ["percent-off", "fixed-off", "flash-sale", "clearance", "bogo", "mystery", "trial-sample", "subscribe-save", "referral", "student-military", "pre-order-price", "price-lock", "bundle-decoy", "cashback", "charity"] },
  "urgency": "none"
}
```

## Sources

- internal research audit (2026-09-10) section 5 block 21; section 2 row 21.
- internal research audit (2026-09-10) sections 1.1, 3, 12.
- internal research audit (2026-09-10) sections 7, 13.
- `references/vertical-fashion.md` (lookbook grids, collection and drop pacing), `references/generate-editorial.md`, `references/product-grid.md`.
- shopidevs lookbook guide: https://shopidevs.com/how-to-create-lookbook-in-shopify/
- Stylitics digital lookbook: https://stylitics.com/resources/blog/digital-lookbook/
- Publitas lookbook guide: https://www.publitas.com/blog/how-to-create-ecommerce-lookbook/
- Shopify lookbook guide: https://www.shopify.com/blog/lookbooks-how-to-use-high-quality-lifestyle-photos-to-boost-sales
- Elara shop-the-look guide: https://joinelara.com/blog/the-complete-guide-to-shop-the-look-for-shopify-fashion-brands
- easyappsecom lookbook: https://easyappsecom.com/guides/how-to-create-shopify-lookbook
- Yotpo visual reviews: https://www.yotpo.com/blog/visual-reviews/
- Baymard human model imagery: https://baymard.com/blog/human-model
