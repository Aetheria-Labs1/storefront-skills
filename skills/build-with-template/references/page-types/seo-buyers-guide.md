# SEO buyer's guide

A search-intent roundup: "best X for Y", "top N X", "X buyer's guide". The
visitor typed a category, not a brand, and expects a ranked, methodical
comparison they can skim by anchor, verify by method and act on per entry.
The page ranks 3 to 6 options with a verdict and CTA each, discloses how they
were chosen and by whom, ends with a comparison table and FAQ, and says
plainly that the merchant sells one of them. Depth for markup, anchor nav
and entry layout lives in `references/generate-listicle.md` and the
comparison-intent rules in `references/traffic-source-google.md`; this file
is the contract.

## Identify it

Signals in the brief: traffic is Google organic or Google Ads on a
non-brand query; the query contains "best", "top", a number, "buyer's
guide", "roundup", "for [use case]"; the merchant wants to rank and convert
over months, not run a paid campaign.

Near neighbours:

- `listicle`: paid social, one product, "N reasons" framing; this type is
  search traffic and a ranked roundup (index tie-break).
- `comparison-us-vs-them`: the visitor named a competitor or searched "vs"
  or "alternatives"; a table against one named rival, not a ranked list.
- `pdp` search-intent variant: product or category intent with one product;
  no ranking.
- `ingredient-science`: informational intent ("how X works"); no ranking or
  CTA per entry.

## Variants

- **Multi-brand roundup**: the merchant's product plus two or more
  dominant alternatives ranked on consistent attributes with "pick them if"
  honesty; the strongest E-E-A-T posture (OPERATOR: get-ryze on citable
  comparison pages,
  https://www.get-ryze.ai/blog/how-to-make-your-comparison-pages-ai-citable).
- **Single-brand roundup**: the merchant's own range ranked by use case
  ("best for sensitive skin", "best for travel"), disclosed as such in the
  dateline; closer to Endy's intra-brand comparison with persona rows
  (internal teardown audit, 2026-09-10).

## Anatomy

Sections between chrome: 9 to 14. Long-form: over 2,000 words across the
page (`references/generate-listicle.md` quality bar). Entries: 3 to 6.

1. `header` (mandatory). Full navigation; search visitors need the store
   around the article.
2. `hero` (mandatory). H1 matching the query, an answer-first summary of two
   or three sentences naming the top pick and for whom, a group image of the
   contenders or an in-use editorial image. No CTA yet.
3. `dateline` (mandatory). Author byline with name, role and relevant
   experience, last-updated date, and the disclosure line: "Published by
   [Merchant], which makes [product]." LAW and RESEARCH: undisclosed
   self-interest in an editorial-looking page is a disguised advertisement
   (FTC dark-patterns report,
   https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf).
4. `toc` (mandatory). Anchor navigation to every entry, the table, the
   verdict and the FAQ; sticky on desktop; "Jump to verdict" last.
5. `methodology` (mandatory). How the options were chosen and tested:
   criteria, units tested, duration, who tested, when; the E-E-A-T spine.
   150 to 200 words. A guide without a methodology is a `listicle`.
6. `qualifier` (recommended). Who this guide is for and not for; the two or
   three needs that decide the ranking.
7. `list-item` (mandatory, one per entry, 3 to 6). H2 "[Product]: best for
   [use]", product image, 150 to 250 word review, pros and cons as two
   lists, key facts table (price, size, materials or specs, warranty),
   rating with count when reviews exist, a one-line verdict, one CTA.
   Attribute labels identical across entries.
8. `comparison` (mandatory). Table of every entry on the same attributes,
   dated, first column sticky on mobile, "best for" row; near the end,
   before the verdict. Observed pattern: Ekster's three-column matrix with
   an "Others" column and a fair "In focus: [rival]" paragraph before the
   verdict (teardown 35).
9. `verdict` (mandatory). Top pick with the reason in two sentences, plus
   who should choose a different entry and why.
10. `winner` (conditional: the merchant's product genuinely leads on the
    stated criteria and the dateline disclosure is present). A factual badge
    ("Our pick for wide feet"), never "Editor's choice" styling on a
    self-published page.
11. `faq` (mandatory). Five to eight questions from "People also ask" and
    support data, answer in the first sentence, FAQPage JSON-LD.
12. `disclaimer` (mandatory). Repeat of the self-publication disclosure and
    any affiliate or testing-unit notes, within one scroll of the verdict.
13. `related-reads` (recommended). Three or four internal links to adjacent
    guides and collections.
14. `closing-cta` (recommended). Link to the top pick's PDP or collection.
15. `footer` (mandatory).

## Workflow

### Context reads
1. The brief: the query (H1 target), the three to six entries, the criteria
   and units, the author (name, role, experience) and the last-updated
   date; the self-publication disclosure wording. Each becomes a ledger
   row (`expert-quote` for the byline, `test-data` for the method,
   `references/proof/proof-ledger.md`).
2. `lexsis_catalog.get` for every merchant entry: first media item as the
   identity image, a lifestyle image if any, price or "from" price, specs
   and metafields for the facts table, availability, single or
   multi-variant.
3. Alternatives: merchant-confirmed facts with source URLs per attribute;
   licensed imagery imported with `lexsis_asset_import.import` and the
   licence reference recorded, otherwise an inline SVG silhouette labelled
   "other brands". Never a competitor photo without licence (GN8).
4. `lexsis_catalog.reviews_status`, then `lexsis_catalog.reviews` per
   merchant product: average and count labelled by product at 5 or more
   reviews; never one guide-level average
   (`references/proof/reviews-sourcing.md`, display decision table).
5. `lexsis_brand.navigation` for header, footer and the related-reads
   links; `lexsis_brand.brand_kit` for tokens, voice and banned phrases;
   `lexsis_brand.context` for the `theme_id`;
   `references/traffic-source-google.md` for the comparison-intent rules.
6. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`, one call
   each for `lifestyle`, `hero`, `product-shot`, `banner`; then semantic
   "<category> in use" and "<top pick> on a desk"; view candidates with
   `lexsis_assets.view`. Testing photos from the merchant via
   `lexsis_asset_import.import`.
7. "People also ask" questions and support data for the FAQ; press rows for
   any outlet that reviewed an entry
   (`references/proof/press-and-media-mentions.md`).
8. `lexsis_design.islands` for the active catalog; `lexsis_workspace.credits`
   before planning the one permitted `hero_bg`
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
`lexsis_design.island_schema`, with autoplay and entry motion off unless the
plan names that motion moment (N10). Entry layout, anchor nav and markup are
in `references/generate-listicle.md`; copy ceilings follow
`references/copy/copy-frameworks.md` and
`references/anti-patterns/copy-anti-patterns.md`.

**`header`**
- Purpose: full navigation; search readers need the store around the
  article.
- Media: logo from the brand kit.
- Island: SiteHeader or Navbar with links from `lexsis_brand.navigation`,
  search visible; resolve from `lexsis_design.island_schema`; preset
  `siteheader/sticky-light` or `navbar/sticky-light`.
- Copy: nav labels only.
- Decide with: the navigation result.

**`hero`**
- Purpose: H1 matching the query, a two or three sentence answer-first
  summary naming the top pick, an editorial image; no CTA.
- Media: yes; job `in-use` of the top pick or the contenders (own products
  real, alternatives only licensed), treatment `editorial-lifestyle`;
  alternate `grid` composed from the entries' identity images
  (`references/assets/image-jobs-by-page-type.md`, section 5). Search library
  `lifestyle`, then `hero`, then catalog lifestyle media, then merchant
  upload. Generation: `hero_bg` (ALLOW) only behind a real cut-out composite.
  Missing: tell the merchant (one in-use frame, 16:9 plus 4:5) and offer
  upload or `hero_bg`; if skipped, the `grid` alternate from the entries' own
  images stands. No-go: a packshot of the own product alone (reads as an ad);
  a gradient wash; text in the image. View every candidate with
  `lexsis_assets.view` and run the section fit review; view it beside the
  entry images so the contenders read as one shoot.
- Island: none (static `<picture>`); HeroMedia in image mode only when the
  hero is the plan's full-bleed bold moment, autoplay off; resolve from
  `lexsis_design.island_schema`.
- Copy: H1 10 words or fewer with the keyword once; answer box 40 to 60
  words, first sentence names the pick and for whom.
- Decide with: `lexsis_assets.view` of the chosen frame; the entries list.

**`dateline`**
- Purpose: byline with name, role and experience, last-updated date, the
  disclosure line.
- Media: outside the loop as an opening text line; the author's real photo
  only with approval, never generated (GN3); no photo means no avatar. View
  every candidate with `lexsis_assets.view` and run the section fit review
  before use.
- Island: none.
- Copy: "Published by <Merchant>, which makes <product>"; date in full.
- Decide with: the `expert-quote` ledger row for the author.

**`toc`**
- Purpose: anchors to every entry, the table, the verdict and the FAQ;
  sticky on desktop.
- Media: no.
- Island: none; an ordered list of anchor links, sticky above `lg`, "Jump
  to verdict" last (the BackToTop and Tabs islands are deprecated; a native
  anchor link replaces any return control).
- Copy: entry names as written in their H2s.
- Decide with: the final section ids.

**`methodology`**
- Purpose: how the options were chosen and tested: criteria, units,
  duration, who, when; 150 to 200 words.
- Media: yes where it exists: a real photo of the testing from the merchant or
  an authored inline SVG `diagram` of criteria weights; the HTML criteria
  table is the object that keeps this from being a wall of text. Generation:
  never a lab, chart or result image (GN4). Missing photo: the merchant is
  told a testing photo could be uploaded; the table carries the section
  meanwhile. View every candidate with `lexsis_assets.view` and run the
  section fit review before use.
- Island: none.
- Copy: "we tested", "we measured" only when true; numbers copied from the
  `test-data` row.
- Decide with: the `test-data` ledger row; without it the page is a
  `listicle` and is retyped with the merchant informed.

**`qualifier`** (recommended)
- Purpose: who this guide is for and not for; the two or three needs that
  decide the ranking.
- Media: outside the loop; two short lists.
- Island: none.
- Copy: two lists of three items, 12 words each.
- Decide with: the criteria in the brief.

**`list-item`** (one per entry, three to six)
- Purpose: "<Product>: best for <use>", image, 150 to 250 word review, pros
  and cons, facts table, rating with count, verdict line, one CTA.
- Media: yes; job `identity` per entry: own product from catalog media (first
  media item, viewed); an alternative from licensed imagery or an inline SVG
  silhouette. Alternate the image left and right per entry. A `detail` or
  `scale` second image for the top two entries where catalog media has one.
  Generation: none. Missing own-product image: tell the merchant and offer
  upload; an entry without any image is a silhouette with the facts table,
  never image-less text. No-go: a competitor photo without licence; a
  generated product; emoji or icon pros-and-cons. View every candidate with
  `lexsis_assets.view` and run the section fit review; view the entry images
  together so lighting, backgrounds and crops agree.
- Island: QuickAdd on the merchant's own entries; decide direct add or
  picker from the variant axes; alternatives use a plain outbound link
  ("See the <product>"); BuyBox is not mounted mid-article; resolve from
  `lexsis_design.island_schema`.
- Copy: H2 "<Product>: best for <use>" with identical label grammar; 150 to
  250 words; three pros and three cons as facts; facts table with the same
  attribute labels and units across entries; one verdict sentence.
- Decide with: `lexsis_catalog.get` for own facts; the merchant's sourced
  facts for alternatives; `lexsis_catalog.reviews` band per own product.

**`comparison`**
- Purpose: every entry on the same attributes, dated, "best for" row, first
  column sticky on mobile.
- Media: yes; a header row of small `comparison-visual` thumbnails: own
  product real from catalog media, alternatives as silhouettes. View every
  candidate with `lexsis_assets.view` and run the section fit review; view the
  thumbnail images together so lighting, backgrounds and crops agree.
- Island: none; an HTML table with a sticky first column (the Tabs island is
  deprecated).
- Copy: identical units per row; a "last checked" date under the table.
- Decide with: the attribute list fixed in `methodology`.

**`verdict`**
- Purpose: the top pick with the reason in two sentences, plus who should
  choose a different entry.
- Media: yes; the top pick's `identity` image from catalog media beside the
  text (reuse of the entry slot). View every candidate with
  `lexsis_assets.view` and run the section fit review before use.
- Island: QuickAdd on the top pick when it is the merchant's product,
  otherwise a link; resolve from `lexsis_design.island_schema`.
- Copy: two sentences for the pick, one sentence per alternative
  recommendation; pattern `next-step`.
- Decide with: the ranking from the criteria.

**`winner`** (conditional: the merchant's product leads on the stated
criteria and the disclosure is present)
- Purpose: a factual badge such as "Our pick for wide feet".
- Media: no; HTML text beside the entry heading, never a generated badge
  (GN5) or "Editor's choice" styling.
- Island: none.
- Copy: 5 words naming the criterion.
- Decide with: the criteria table showing the lead.

**`faq`**
- Purpose: five to eight questions from "People also ask" and support data,
  answer in the first sentence, FAQPage JSON-LD.
- Media: no.
- Island: none; native `<details>` and `<summary>` (the FAQ island is
  deprecated) plus the JSON-LD script.
- Copy: answers 60 words each, fact first.
- Decide with: the question list gathered in the reads.

**`disclaimer`**
- Purpose: the self-publication disclosure repeated, affiliate or
  testing-unit notes, within one scroll of the verdict.
- Media: no (stands without an image per the asset workflow).
- Island: none.
- Copy: two sentences.
- Decide with: the disclosure wording in the ledger.

**`related-reads`** (recommended)
- Purpose: three or four internal links to adjacent guides and collections.
- Media: yes when each target has a real image (a collection's representative
  product identity from catalog media or a library `lifestyle` frame); one
  aspect across the row. Missing: tell the merchant; if skipped, the block is
  a plain list of links, never image-less cards. View every candidate with
  `lexsis_assets.view` and run the section fit review; view the tile images
  together so lighting, backgrounds and crops agree.
- Island: none.
- Copy: anchor text in the adjacent keyword, 8 words each.
- Decide with: `lexsis_brand.navigation` targets and their images.

**`closing-cta`** (recommended)
- Purpose: link to the top pick's PDP or collection.
- Media: the merchant's related products with images when a carousel is used
  (`references/product-grid.md`). View every candidate with
  `lexsis_assets.view` and run the section fit review before use.
- Island: ProductCarousel with four or more products, or a single link;
  motion off; resolve from `lexsis_design.island_schema`; preset
  `productcarousel/cards-quiet`.
- Copy: one line; pattern `next-step`.
- Decide with: catalog product count with images.

**`footer`**
- Purpose: full footer; search readers need the store.
- Media: logo only.
- Island: Footer with columns from `lexsis_brand.navigation`; resolve from
  `lexsis_design.island_schema`; preset `footer/columns-dark`.
- Decide with: the navigation result.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` per own entry, `detail` and `scale` for the top picks | the editorial `in-use` hero, any image of an alternative | compose the `grid` hero from entry identity images; generate `hero_bg` (ALLOW) behind a real cut-out; ask the merchant to upload an in-use frame or a licensed alternative image; inline SVG silhouettes for alternatives; never a competitor photo without licence |
| asset library | `lifestyle` frames for the hero, `logo` SVGs for press quotes | testing photos, author portrait with approval | ask the merchant to upload; the methodology carries its HTML criteria table and the byline runs without an avatar meanwhile |
| generation | backdrops, textures, composites only | product, people, results, logos, text | never; these are "needs a real photo" in the merchant message |

With minimal assets the page is a header, a grid hero of the entries' own
images, the byline and disclosure, a sticky TOC, a methodology with its table,
three entries each with one real image and silhouettes for alternatives, the
comparison table, verdict, FAQ, disclaimer and footer; at most one generated
asset (`hero_bg`), never more than four per page, and every missing image
listed in the plan and the draft summary with upload, generate or skip. Every
asset, found or generated, was viewed and passed the section fit review before
use.

## Above the fold (390px)

In order: header; H1 that answers the query; the two- or three-sentence
answer-first summary naming the top pick; byline with name and date;
disclosure line; the TOC starting. RESEARCH: the first paragraph gets 81%
of readers, the fourth 32%, so the answer goes first
(https://www.nngroup.com/articles/website-reading/).

Must not appear: a CTA, a discount, a countdown, a popup, a "sponsored"
looking badge without the disclosure, a hero that is only a lifestyle image.

## Proof

Modules: 2 to 4. Proof is method and evidence, not testimonials.

- `test-data` (required): the methodology's evidence, what was measured, on
  how many units, over what period, by whom; a document or URL in the ledger
  (`references/proof/proof-ledger.md`). Without it the page is a `listicle`.
- `expert-quote` as the author credential (recommended): named author,
  verifiable role; the byline is a ledger row.
- `review-summary` per entry (conditional: 5 or more reviews for that
  product, from `lexsis_catalog.reviews` for the merchant's own items;
  third-party ratings only where the platform's terms allow and with the
  source named).
- `certification` or `award` per entry (conditional: issuer, year, link).
- `press-quote-linked` (conditional: editorial, within 24 months).
- Never: `social-proof-popup`, `live-viewer-count`, `stock-count`,
  `press-logo-unlinked`, invented "tested by our team" when nothing was
  tested, star glyphs without a count.

Zero-review store: entries carry facts, test data and policy facts; no
review-shaped element (`references/proof/reviews-sourcing.md`).

## Offer and CTA

- CTAs: one per entry plus one in the verdict; pattern `next-step` ("See
  the [product]", "Check price"); the merchant's own entries may use "Add to
  cart" with the price shown. First CTA arrives with the first entry, after
  hero, dateline, TOC and methodology. No sticky CTA; a sticky TOC is the
  navigation.
- Price reveal: the answer box may state a price range; each entry shows
  price or "from" price in its facts table; the table repeats it.
- Urgency: none.
- Offer types that fit: `none`, `free-shipping` as a fact in the merchant
  entry, `bnpl` line, `bundle` when the merchant's entry is a set,
  `subscribe-save` as a fact, `first-order` only below the fold in the
  merchant's entry, `loyalty`.
- Offer types that do not fit: `percent-off`, `fixed-off`, `bogo`,
  `flash-sale`, `clearance`, `gwp`, `tiered-volume`, `bundle-decoy`,
  `mystery`, `pre-order-price`, `price-lock`, `trial-sample`,
  `student-military`, `cashback`, `gift-card`, `referral`,
  `limited-edition`, `charity`. A promotion on a guide reads as an ad and
  costs the E-E-A-T posture.

## Imagery

Required jobs: `identity` per entry (real product media; competitor products
only with licence or as generic silhouettes) and `in-use` for the hero or
the top entries. Recommended: `comparison-visual` (own product real,
alternatives generic), `detail`, `scale`, `diagram` for the facts table
where a visual helps, `ugc` with rights.

Hero treatment: `editorial-lifestyle` with the contenders or the top pick in
use; alternate image left and right per entry. Video optional (a testing
clip with a poster). Minimum 5 image slots: hero plus one identity image per
entry. No gradient washes or generated backgrounds (design-rules N7, N14).

## Copy

Framework: answer-first (the summary), comparison (table and verdict),
listicle numbering across entries.

- H1 answers the query in 10 words or fewer and contains the keyword once;
  year in the H1 only if the methodology is refreshed yearly.
- Answer box 40 to 60 words; first sentence names the pick and for whom.
- Entry headings "[Product]: best for [use]" with identical label grammar.
- Entries 150 to 250 words; pros and cons three each, each a fact.
- Claims self-contained at sentence level so they can be quoted; every
  comparative claim has the same unit across entries.
- Reading level grade 6 to 8; H2 every 400 to 600 words; keyword in the
  first paragraph and two or three H2s, naturally
  (`references/traffic-source-google.md`).
- Vocabulary: "we tested", "we measured", "we chose" only when true; no
  "ultimate", "best of the best", "hands down"; no rhetorical-question
  headings beyond one.
- Every numeral in an entry or the table traces to the facts table source
  or a ledger row.

## Never

- Never publish without an author byline, a last-updated date and the
  self-publication disclosure above the fold.
- Never omit the methodology; without it the page is a `listicle`.
- Never badge the merchant's product the winner when it does not lead on
  the stated criteria, or without the disclosure.
- Never rank fewer than three entries.
- Never use different attribute labels or units across entries.
- Never place the comparison table before the entries; it belongs near the
  end for readers who skipped to decide.
- Never show a discount, countdown or stock line.
- Never strip navigation or the footer; search readers need the store.
- Never invent testing ("our lab") or a tester.
- Never show competitor product photography without licence.
- Never leave a year in the H1 when the content was not refreshed.

## Examples

- Endy compare, https://www.endy.com/compare: an intra-brand decision helper
  with "most loved by" persona rows and consistent attributes; the
  single-brand variant's table pattern.
- Ekster vs Ridge, https://www.ekster.com/en-eu/pages/ekster-vs-ridge: a
  three-column matrix with an "Others" column, a fair "In focus: [rival]"
  paragraph before the verdict, and decision-question FAQs; the fairness
  posture this type needs even though it is a two-way comparison.
- AG1 "5 Health Benefits of Taking AG1 in 2025",
  https://drinkag1.com/5-reasons-why-variant-a: a year-stamped,
  footnoted single-brand article; shows the maintenance cost of a year in
  the H1 and the value of a stat with a footnote in every entry.

## Checklist

```json
{
  "page_type": "seo-buyers-guide",
  "aliases": ["best X for Y", "top N roundup", "buyer's guide", "best of guide", "roundup review"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["problem-aware", "solution-aware"],
  "traffic": ["google-search", "organic"],
  "sections": { "min": 9, "max": 14 },
  "mandatory_sections": ["header", "hero", "dateline", "toc", "methodology", "list-item", "comparison", "verdict", "faq", "disclaimer", "footer"],
  "recommended_sections": ["qualifier", "winner", "related-reads", "closing-cta"],
  "forbidden_sections": ["countdown", "stock-indicator", "hook", "agitation", "offer-bridge", "final-offer", "quantity-breaks", "savings-math"],
  "nav": "full",
  "price_above_fold": "optional",
  "cta": { "min": 4, "max": 7, "first_after_section": 4, "sticky": "forbidden", "copy_pattern": "next-step" },
  "proof": { "min_modules": 2, "max_modules": 4, "required_kinds": ["test-data"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "stock-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "in-use"], "hero": "editorial-lifestyle", "video": "optional", "min_images": 5 },
  "copy_framework": ["answer-first", "comparison", "listicle"],
  "offer_compat": { "allowed": ["none", "free-shipping", "bnpl", "bundle", "subscribe-save", "first-order", "loyalty"], "forbidden": ["percent-off", "fixed-off", "bogo", "flash-sale", "clearance", "gwp", "tiered-volume", "bundle-decoy", "mystery", "pre-order-price", "price-lock", "trial-sample", "student-military", "cashback", "gift-card", "referral", "limited-edition", "charity"] },
  "urgency": "none"
}
```

## Sources

- internal research audit (2026-09-10) section 5 block 37 ("Best X" SEO page), block 4 (listicle), section 3 (solution-aware headline), section 4.3 (reading).
- internal research audit (2026-09-10) teardowns 18, 35, 36 and Part D (listicle synthesis, study-methodology footnote module).
- internal research audit (2026-09-10) sections 1.2 (disguised advertisement), 7.1 (headlines), 7.7 (FAQ), 9 (message match).
- internal research audit (2026-09-10) sections 5, 10.
- `references/generate-listicle.md`, `references/traffic-source-google.md` (comparison intent, SEO-ready structure), `references/proof/proof-ledger.md`.
- get-ryze citable comparison pages: https://www.get-ryze.ai/blog/how-to-make-your-comparison-pages-ai-citable
- NN/g website reading (paragraph attention): https://www.nngroup.com/articles/website-reading/
- NN/g how little users read: https://www.nngroup.com/articles/how-little-do-users-read/
- FTC dark patterns report (disguised ads): https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf
- Google landing page experience: https://support.google.com/google-ads/answer/7636512
- Google intrusive interstitials: https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials
- Landra awareness mapping: https://www.getlandra.com/blog/5-stages-of-awareness
