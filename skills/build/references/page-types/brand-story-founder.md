# Brand story and founder

The page that sells belief rather than a SKU: who makes this, why it exists,
what the brand refuses to do, and what it has done so far. Visitors arrive
from the header nav, press coverage, organic search for the brand, or a
retargeting ad aimed at sceptics; most are checking legitimacy before or
after a first purchase. The page must tell one specific origin story in the
founder's voice, state the mission in a sentence, back it with documented
numbers and real faces, and end with one next step. OPERATOR: 82% of about
pages in a WebMedic audit of 80 stores had no call to action
(https://webmedic.com/ecommerce-about-page).

## Identify it

Signals in the brief: "about", "our story", "founder", "mission",
"manifesto", "why we exist"; the differentiator is provenance, process or
values rather than a mechanism.

Near neighbours:

- `ingredient-science`: the brief names ingredients, studies or "how it
  works"; mechanism, not meaning (index tie-break).
- `homepage`: routes to everything; the story is one teaser there.
- `advertorial`: a story that sells one product to cold traffic with a late
  price reveal; this page has no offer and full navigation.
- `ugc-creator-collab`: community content as the proof; here the founder
  and the record are the proof.
- Editorial magazine page (`references/generate-editorial.md`): long-form
  narrative with commerce moments; use its pacing for luxury heritage
  stories, but keep this contract's ceilings.

## Anatomy

Sections between chrome: 6 to 9. Word budget 300 to 500; heritage or luxury
brands up to 800.

1. `header` (mandatory). Full navigation; readers move on to shop or to the
   finder.
2. `hero` (mandatory). A belief-first or problem-first headline in the
   customer's words, not the category; a real photograph of the founder,
   team, workshop or place. No product packshot, no CTA.
3. `story` (mandatory). The origin: a specific moment with names, dates and
   the thing done differently, in first person; 120 to 200 words. Follows
   the Shopify story arc (status quo, problem, journey, milestones,
   mission; https://www.shopify.com/blog/how-to-write-an-about-us-page).
4. `mission` (mandatory). One sentence: "We make [product] for [audience]
   so they can [outcome]."
5. `values` (recommended). Three to five commitments, each with a concrete
   practice ("Every batch tested by a third-party lab; reports on each
   PDP"), not adjectives. `sourcing` replaces or joins it when provenance
   is the differentiator.
6. `founder-note` (mandatory). Signed note with real full name, title and
   photo; written approval recorded in the proof ledger.
7. `stats` (conditional: documented numbers exist). Three to five numbers:
   orders shipped, years, countries, certifications, retail partners; each
   a verified ledger row, rounded down (`references/proof/proof-ledger.md`).
8. `press-quotes` or `press-marquee` (conditional: verified, linked editorial
   coverage within 24 months). Quotes verbatim with outlet, author and date.
9. `community-count` (conditional: a documented count exists, "over 82,000
   on Instagram" from a live read). Otherwise omit.
10. `ugc-grid` (conditional: rights-cleared customer media). Six tiles with
    handles.
11. `product-grid` (recommended). A best-seller carousel of four to six
    products, placed last before the closing CTA, never earlier.
12. `closing-cta` (mandatory). One next step: "Shop best sellers" or "Find
    your match" (finder), with a one-line reason.
13. `footer` (mandatory).

## Workflow

### Context reads
1. `lexsis_brand.brand_kit` for tokens, voice notes, banned phrases and the
   merchant-stated brand rules; `lexsis_brand.context` for the `theme_id`;
   `lexsis_brand.navigation` for header and footer.
2. Merchant facts into the proof ledger (`references/proof/proof-ledger.md`):
   founder full name and title with written approval for the note and
   photo; the origin moment with its date, place and the thing done
   differently; the mission sentence; three to five values each with a
   concrete practice; documented numbers (orders export, years, countries,
   retail partners, certifications with issuer and number); any charity
   commitment with organisation and amount
   (`references/offers/campaign-calendar.md`, `cause` row).
3. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`, one call
   each for `lifestyle` (people, workshop, place), `hero`, `product-shot`,
   `logo` (press), `social-proof` (UGC with rights); record counts; then
   semantic "<founder name>", "<workshop or farm> at <place>", "making
   <product>". View every candidate with `lexsis_assets.view`; a person in
   the frame must be named and employed, or a customer with a rights row
   (`references/proof/ugc-rights-and-display.md`).
4. `lexsis_asset_import.import` for the merchant's founder, team and
   process photos (original files, owner and date recorded,
   `references/assets/asset-sourcing-sequence.md` step 3).
5. Press: fetch each claimed article, write ledger rows, count `verified`
   editorial rows within 24 months
   (`references/proof/press-and-media-mentions.md`). Community count only
   from a live read (`references/proof/numbers-and-counts.md`).
6. `lexsis_catalog.list` for four to six best sellers with media for the
   closing carousel; `lexsis_catalog.get` for each identity image and
   price.
7. `lexsis_design.islands` for the active catalog; `lexsis_workspace.credits`
   is read for completeness; generation is not planned on this type
   because people and places are the content and both are identity-bound
   (`references/assets/generation-policy.md`, GN3).

### Section by section
Media per section follows `references/workflows/section-asset-workflow.md`:
when nothing covers a slot, tell the merchant what is missing (job, aspect,
count), offer upload via `lexsis_asset_upload.upload` (generation is never
feasible for people or places presented as the brand's own), and skip or merge
the section only when the merchant chooses; a fast draft uses the closest
existing asset or leaves the slot `planned` and lists every gap in the plan
and the draft summary. No asset is used sight unseen: every candidate is
opened with `lexsis_assets.view` and judged against the section per section 1b
of that file (subject, crop to the slot aspect, a quiet area for the copy, the
lighting and styling of the neighbouring slots, the plan's palette, no
baked-in text, watermark or overlay); candidates for one grid, set or lookbook
are viewed together so the set reads as one shoot, and a generated asset is
viewed the same way after it returns. Islands follow
`references/workflows/island-selection-workflow.md`: the lines below name the
island and the inputs; variants and props are resolved live from
`lexsis_design.island_schema`, with autoplay and entry motion off unless the
plan names that motion moment (N10). Editorial pacing for heritage brands is
in `references/generate-editorial.md`; copy ceilings follow
`references/copy/copy-frameworks.md` and
`references/anti-patterns/copy-anti-patterns.md`.

**`header`**
- Purpose: full navigation; readers move on to shop or to the finder.
- Media: logo from the brand kit.
- Island: SiteHeader or Navbar with links from `lexsis_brand.navigation`;
  resolve from `lexsis_design.island_schema`; preset
  `siteheader/sticky-light` or `navbar/sticky-light`.
- Copy: nav labels only.
- Decide with: the navigation result.

**`hero`**
- Purpose: a belief-first or problem-first headline over a real photograph
  of the founder, team, workshop or place; no product, no CTA.
- Media: yes; job `founder-or-team` or `context`, treatment
  `editorial-lifestyle` (`references/assets/image-jobs-by-page-type.md`,
  section 5). Search library `lifestyle`, then `hero`, then merchant upload.
  Generation: none (GN3, AS4; a backdrop without people is not this hero).
  Missing: tell the merchant (a real photo of named people or the real place,
  16:9 plus 4:5, one image) and offer upload only; if the merchant has none,
  the hero is `typographic` (the listed alternate) and the plan records it.
  View every candidate with `lexsis_assets.view` and run the section fit
  review; view it with the story and founder photos so the people and place
  read as one shoot.
- Island: HeroMedia in image mode only when the hero is the plan's
  full-bleed bold moment, autoplay off; otherwise a static split
  `<picture>`; resolve from `lexsis_design.island_schema`.
- Copy: H1 10 words or fewer in the customer's words; one sentence that
  opens the story.
- Decide with: a viewed photo of named people or the real place, approval
  recorded.

**`story`**
- Purpose: the origin in first person, 120 to 200 words, with names, dates
  and the thing done differently.
- Media: yes; one `context` (the place) or `sequence` (the making) photo
  beside the text in a split layout so the section is never a wall of text.
  Search library `lifestyle`, then merchant upload; never stock or generated.
  Missing: tell the merchant (one place or process photo, 3:2 or 4:5) and
  offer upload; if skipped, the story shortens to 120 words in a 60ch measure
  directly under the hero photograph. View every candidate with
  `lexsis_assets.view` and run the section fit review before use.
- Island: none.
- Copy: paragraphs under 45 words; a date, a place, a number or a name in
  each; no "we saw a gap in the market".
- Decide with: the origin facts the merchant confirmed and a viewed photo.

**`mission`**
- Purpose: one sentence: "We make <product> for <audience> so they can
  <outcome>."
- Media: no; a single sentence set large on the page background.
- Island: none.
- Copy: one sentence, 25 words or fewer.
- Decide with: the merchant's approved wording.

**`values`** (recommended)
- Purpose: three to five commitments, each with a concrete practice.
- Media: yes; each value paired with a real photograph of the practice
  (`detail`, `texture`, `ingredient-or-material`, `sequence`: the lab report
  on the bench, the fabric, the farm). Search library `lifestyle` and
  `product-shot`, then merchant upload; stock raw material only as context and
  never presented as own sourcing (GN11); never generated. Missing: tell the
  merchant which values lack a photo (count, 1:1 or 4:5) and offer upload; if
  skipped, those values become sentences in the story. No-go: icon tiles,
  adjective lists, a coloured band per value. View every candidate with
  `lexsis_assets.view` and run the section fit review; view the value images
  together so lighting, backgrounds and crops agree.
- Island: none.
- Copy: value name 3 words; practice one sentence under 20 words.
- Decide with: the count of values that have a viewed photograph.

**`founder-note`**
- Purpose: signed note with real full name, title and photo.
- Media: yes; job `founder-or-team` portrait (4:5, in the workshop or kitchen)
  from library or merchant upload, written approval in the ledger; never stock
  or generated. Missing: tell the merchant (one portrait, 4:5) and offer
  upload only; the signed text stands on its own meanwhile (allowed by the
  asset workflow) and production-ready approval waits for the photo. View
  every candidate with `lexsis_assets.view` and run the section fit review
  before use.
- Island: none.
- Copy: first person, under 120 words, signature with name and title.
- Decide with: the `founder-note` ledger row.

**`stats`** (conditional: documented numbers exist)
- Purpose: three to five verified numbers, rounded down, "over N".
- Media: the numbers sit beside a real photograph of the thing counted when
  one exists (the warehouse, the shipments); otherwise plain text on the page
  background. Missing photo: the merchant is told; no generated chart or scene
  (GN4). View every candidate with `lexsis_assets.view` and run the section
  fit review before use.
- Island: none; static HTML figures from the proof ledger (the StatCards
  island is deprecated, and N10 forbids count-up motion).
- Copy: number, unit and as-of month per item.
- Decide with: a `verified` ledger row per number; no row, no stats
  section, and the merchant is told which documents would unlock it.

**`press-quotes`** or **`press-marquee`** (conditional: verified, linked,
within 24 months)
- Purpose: verbatim quotes with outlet, author and date, or three to six
  linked monochrome logos.
- Media: outlet SVGs from library `logo`, each inside a link; never retyped or
  generated (GN5). Missing files: ask the merchant for outlet artwork or
  article URLs; fewer than three verified rows renders quotes only. View every
  candidate with `lexsis_assets.view` and run the section fit review before
  use.
- Island: none; a static linked row (the Marquee island is deprecated).
- Copy: one to three quotes, verbatim; caption "In the press".
- Decide with: the count of `verified` editorial press rows.

**`community-count`** (conditional: documented and live)
- Purpose: "over 82,000 on Instagram" from a live read.
- Media: no.
- Island: none; one HTML line.
- Copy: one line with the platform and as-of month.
- Decide with: the live read recorded in the ledger; otherwise omit and
  tell the merchant why.

**`ugc-grid`** (conditional: rights-cleared customer media)
- Purpose: six tiles with handles.
- Media: yes; job `ugc` from library `social-proof` with a ledger `P` row per
  tile, one aspect, original grading. Missing rights: tell the merchant which
  requests are open; pending UGC never renders. View every candidate with
  `lexsis_assets.view` and run the section fit review; view the tile images
  together so lighting, backgrounds and crops agree.
- Island: none for the grid; GalleryLightbox mounted once for expansion;
  resolve from `lexsis_design.island_schema`.
- Copy: handle per tile; labelled as customer content.
- Decide with: six or more `verified` UGC rows.

**`product-grid`** (recommended; last before the closing CTA)
- Purpose: four to six best sellers.
- Media: yes; job `identity` per product from catalog media
  (`references/product-grid.md`). Missing: name the products without an image
  and offer upload; if skipped, they leave the carousel. View every candidate
  with `lexsis_assets.view` and run the section fit review; view the grid
  images together so lighting, backgrounds and crops agree.
- Island: ProductCarousel with four or more products, the card composition
  for three; decide from best-seller count and image availability; no quick
  add on a story page; motion off; resolve from
  `lexsis_design.island_schema`; preset `productcarousel/cards-quiet`.
- Copy: heading 6 words or fewer; prices from the catalog; no badges.
- Decide with: `lexsis_catalog.list` best-seller count and images.

**`closing-cta`**
- Purpose: one next step with a one-line reason.
- Media: no; the carousel above carries the imagery.
- Island: none; one button to the collection or the finder.
- Copy: "Shop best sellers" or "Find your routine" plus one sentence;
  pattern `shop-collection`.
- Decide with: the navigation result for the destination.

**`footer`**
- Purpose: policies, contact, social.
- Media: logo only.
- Island: Footer with columns from `lexsis_brand.navigation`; resolve from
  `lexsis_design.island_schema`; preset `footer/columns-dark`.
- Decide with: the navigation result.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` for the closing carousel, sometimes a making-of shot in product media | everything else this page needs: people, place, process | ask the merchant to upload founder, team, workshop and process originals ("needs a real photo"); typographic hero and story-sentence values only on the merchant's call |
| asset library | `lifestyle` (workshop, team), `logo` SVGs for press, `social-proof` UGC with rights | a portrait with written approval, process `sequence` frames, `texture` or material macros | ask the merchant to upload with approval and date recorded; press quotes instead of logos; `stats` waits for documents |
| generation | backdrops, textures, composites only | product, people, results, logos, text | never; this type has no backdrop job, so the generated count is zero |

With minimal assets the page is a header, a typographic hero, a 120-word story
beside one real workshop photo, the mission line, a signed founder note, a
best-seller carousel, one closing CTA and a footer; zero generated assets, a
page that is honest with no proof section at all, and every missing photograph
listed in the plan and the draft summary with upload or skip. Every asset,
found or generated, was viewed and passed the section fit review before use.

## Above the fold (390px)

In order: header; a belief- or problem-first H1 (10 words or fewer); a real
photograph of people or place; one sentence that opens the story. No CTA, no
product, no price, no numbers yet.

Must not appear: a packshot, a discount, a countdown, a review carousel, a
stock photograph, a video that autoplays with sound, a "Shop now" button.

## Proof

Modules: 1 to 2. Light and documentary; identity carries the page.

- `founder-note` (required): real name, title, photo, approval.
- `sales-count`, `customer-count` or years in business in `stats`
  (conditional: merchant export or document, rounded down, "over").
- `press-quote-linked` or `press-logo-linked` (conditional): editorial
  decision by the outlet, brand named, live URL, within 24 months
  (`references/proof/press-and-media-mentions.md`; LAW: ASA "as seen in"
  rulings, https://www.asa.org.uk/advice-online/as-seen-on-tv.html).
- `certification` (conditional): issuer, number, scope beside the mark.
- `community-screenshot` or `ugc-photo` (conditional: rights).
- Never: `social-proof-popup`, `live-viewer-count`, `stock-count`,
  `press-logo-unlinked`, "trusted by countless", any number without a row.

Zero-review or zero-press store: the founder note, real photographs and
policy facts are the whole proof; a page with no proof section is honest
(`references/proof/proof-ledger.md` fallback order).

## Offer and CTA

- CTAs: one mandatory `closing-cta` at the end; one optional secondary link
  after the mission for DTC brands. Pattern `shop-collection` ("Shop best
  sellers", "Find your routine"). No CTA in the hero, story or mission
  (first CTA after section 3). No sticky CTA.
- Price reveal: none; prices appear only on the best-seller cards at the end.
- Urgency: none.
- Offer types that fit: `none`; `referral` and `loyalty` as programme links
  in the closing section; `charity` as a documented cause commitment in
  `values` with the organisation and the amount.
- Offer types that do not fit: every discount, gift, shipping threshold,
  bundle, subscription, trial, pre-order or sale type. A brand page with a
  discount reads as an ad and undercuts the story ("less sales, more
  identity", Shopify About Us guide).

## Imagery

Required jobs: `founder-or-team` (real, named people who work there) and
`context` (the workshop, farm, kitchen, city or studio at true scale).
Recommended: `in-use`, `detail` and `texture` of the making, `sequence` of
the process, `ingredient-or-material`, `ugc` with rights. `identity`
appears only in the closing best-seller cards.

Hero treatment: `editorial-lifestyle`, people or place, product incidental.
RESEARCH: users scrutinise photographs of real people and ignore stock
(https://www.nngroup.com/articles/photos-as-web-content/). Founder video
optional, 60 to 120 seconds, click to play with captions. Four to eight
images; minimum 4 slots: hero, founder portrait, two process or place shots.
No generated people, no stock (`references/assets/image-jobs-by-page-type.md`).

## Copy

Framework: story-lead (status quo, problem, journey, milestones, mission;
Problem, Origin, Proof, CTA per WebMedic). StoryBrand posture: the customer
is the hero, the brand is the guide.

- H1 10 words or fewer, the customer's frustration or a belief; never the
  category or "About us".
- First person singular or plural; no third-person corporate voice.
- Specifics over adjectives: a date, a place, a number, a name in every
  paragraph; "we were passionate about quality" is a fail.
- Paragraphs under 45 words; total under 500 words (800 for heritage).
- Mission one sentence; values one practice each.
- Reading level grade 6 to 8; "you" and "we" outnumber the brand name.
- Vocabulary: no "journey", "passion", "curated", "elevate", "disrupt",
  "trusted by countless", "family" for customers.

## Never

- Never end without a CTA.
- Never place a product carousel before the founder note; it goes last.
- Never show a discount, code, countdown or stock line.
- Never use stock photography or generated people.
- Never write a generic origin ("we saw a gap in the market").
- Never state a number ("17 million pairs", "10,000 customers") without a
  verified ledger row.
- Never show a community count that is not documented and live.
- Never exceed 800 words even for heritage brands.
- Never write in the third person about the founder on a founder page.
- Never render press logos without a link to the article.
- Never turn the page into a mechanism explainer; that is
  `ingredient-science`.

## Examples

- Grace Loves Lace, https://graceloveslace.com/pages/our-story: founder and
  designer bios with names and photographs, a specific origin, values tied
  to practice.
- The Whole Truth, https://thewholetruthfoods.com/: a manifesto-first
  story with a factory tour as the trust module and named people rather
  than logos; the homepage carries the story, so the pattern transfers.
- Shopify's brand storytelling roundup (Allbirds with its problem, material
  and pairs-sold numbers; Hiut Denim "We make jeans. That's it."),
  https://www.shopify.com/ca/blog/brand-storytelling-examples: problem-first
  headlines and numbers over adjectives.

## Checklist

```json
{
  "page_type": "brand-story-founder",
  "aliases": ["about us", "our story", "founder page", "mission page", "manifesto", "why we exist"],
  "funnel_stage": ["tof", "retention"],
  "awareness": ["unaware", "problem-aware"],
  "traffic": ["organic", "direct"],
  "sections": { "min": 6, "max": 9 },
  "mandatory_sections": ["header", "hero", "story", "mission", "founder-note", "closing-cta", "footer"],
  "recommended_sections": ["values", "stats", "product-grid", "press-quotes", "ugc-grid"],
  "forbidden_sections": ["buy-box", "offer", "pricing", "savings-math", "final-offer", "countdown", "stock-indicator", "dateline", "hook", "agitation", "offer-bridge", "comparison", "us-vs-them", "quantity-breaks", "subscription-toggle", "bundle-builder"],
  "nav": "full",
  "price_above_fold": "forbidden",
  "cta": { "min": 1, "max": 2, "first_after_section": 3, "sticky": "forbidden", "copy_pattern": "shop-collection" },
  "proof": { "min_modules": 1, "max_modules": 2, "required_kinds": ["founder-note"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "stock-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["context", "founder-or-team"], "hero": "editorial-lifestyle", "video": "optional", "min_images": 4 },
  "copy_framework": ["story-lead"],
  "offer_compat": { "allowed": ["none", "referral", "loyalty", "charity"], "forbidden": ["percent-off", "fixed-off", "bogo", "gwp", "free-shipping", "tiered-volume", "bundle", "bundle-decoy", "subscribe-save", "first-order", "cashback", "bnpl", "trial-sample", "mystery", "pre-order-price", "price-lock", "flash-sale", "clearance", "limited-edition", "gift-card", "student-military"] },
  "urgency": "none"
}
```

## Sources

- internal research audit (2026-09-10) section 5 block 17; section 2 row 17; section 6 (StoryBrand, story lead).
- internal research audit (2026-09-10) sections 5, 10, 13.
- internal research audit (2026-09-10) sections 1 (founder_team), 6 (no generated people).
- internal research audit (2026-09-10) sections 6, 7, 8.
- `references/proof/press-and-media-mentions.md`, `references/proof/proof-ledger.md`, `references/generate-editorial.md`.
- WebMedic about page audit: https://webmedic.com/ecommerce-about-page
- Shopify About Us guide: https://www.shopify.com/blog/how-to-write-an-about-us-page
- Shopify brand storytelling examples: https://www.shopify.com/ca/blog/brand-storytelling-examples
- NN/g photos as web content: https://www.nngroup.com/articles/photos-as-web-content/
- ASA "as seen in" guidance: https://www.asa.org.uk/advice-online/as-seen-on-tv.html
- Grace Loves Lace: https://graceloveslace.com/pages/our-story
