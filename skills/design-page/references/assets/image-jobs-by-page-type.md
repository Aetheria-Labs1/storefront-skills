# Image jobs by page type

The image job taxonomy, the page type x job matrix, minimum image counts, hero
treatment and the lifestyle/studio balance per vertical. `/plan-page` loads it
while mapping the existing gallery to jobs and creating asset slots;
`/design-page` re-reads it when a `planned` slot must be resolved. It extends
the "Gallery Job Coverage" section of `references/consumer-behavior-cro.md`
and uses only the job ids from `references/page-types/_checklist-format.md`.
Sourcing order lives in `references/assets/asset-sourcing-sequence.md`;
generation limits in `references/assets/generation-policy.md`; per-slot
technical specs in `references/assets/slot-spec.md`.

Tags: LAW (regulation or platform terms), RESEARCH (cited study), OPERATOR
(practitioner or teardown evidence), HEURISTIC (house threshold anchored to
evidence but not itself a standard).

## 1. Job taxonomy

A slot has one primary job. An image may do two jobs; the plan records the
primary one in the slot's Role/purpose or a Job column. "Identity-bound" jobs
show the product itself and may only be filled by real media of the exact SKU.

| Job id | Shopper question | Content rule | Identity-bound | Evidence |
|---|---|---|---|---|
| `identity` | What exactly is it? | Whole product, brand-consistent background, product fills 85% or more of the frame, true colour, sRGB | yes | Amazon main image rules https://sellercentral.amazon.com/help/hub/reference/external/G1881 ; Google Merchant "accurately display the product" https://support.google.com/merchants/answer/6324350 |
| `detail` | Is it well made? | One feature in extreme close-up, sharp, never upscaled | yes | Baymard textural type https://baymard.com/blog/ux-product-image-categories |
| `scale` | How big is it? | Product beside a hand, body, room or object of known size | yes | 42% of users judge size from images; 37% of sites give no in-scale image https://baymard.com/blog/current-state-ecommerce-product-page-ux |
| `texture` | What does it feel like? | Macro of fabric, surface or formula under even light | yes | Baymard textural type; Sharma "see the texture on skin" https://sharmabrands.com/blogs/newsletter/7-biggest-landing-page-mistakes |
| `in-use` | What is it like to use? | Real product used by a real person in a realistic setting; product legible | yes | NN/g: real people are scrutinised, stock is ignored https://www.nngroup.com/articles/photos-as-web-content/ |
| `context` | Where does it belong? | Room, table or occasion at realistic scale; the product may be composited from a real cut-out | partial | Baymard in-scale and lifestyle https://baymard.com/blog/in-scale-product-images |
| `variation` | What does my colour, size or flavour look like? | One image per variant; gallery swaps on selection | yes | 54% of sites fail to update thumbnails to the chosen colour https://baymard.com/research/ecommerce-product-lists |
| `included-items` | What do I receive? | Flat lay of every shipped component, labelled in HTML when more than four | yes | "What's included" test: +30.5% CVR, n=12,412 https://www.processcreative.com.au/blog/a-b-testing-does-showing-whats-in-the-box-actually-lift-conversions |
| `sequence` | How do I use or install it? | Three to five numbered steps, each a real photo; step text in HTML | yes | How-to is the most watched content type https://wistia.com/blog/video-marketing-statistics |
| `result-or-context` | Does it work, or what situation is this for? | A verified before/after pair from the proof ledger; when none exists, a truthful context image of the situation | yes for result | ASA before/after https://www.asa.org.uk/advice-online/before-and-after-photos.html ; FTC health guidance https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance |
| `ingredient-or-material` | What is it made of? | Flat lay of ingredients or materials; no implied clinical setting | no | FTC "net impression" includes images (same URL) |
| `packaging` | What arrives at my door? | Outer box, inner presentation, unboxing | yes | Amazon slot logic (G1881 above) |
| `founder-or-team` | Who is behind this? | Real, named people who work there | yes | NN/g photos as web content (above) |
| `ugc` | What do people like me experience? | Rights-cleared customer media, cropped only, labelled as customer content | yes | 71% say shopper photos raise purchase likelihood https://www.bazaarvoice.com/press/sei-2022-press-release/ |
| `diagram` | How does it work or measure? | Mechanism, dimensions or flow; every number in HTML; inline SVG preferred | no | WCAG images of text https://www.w3.org/WAI/tutorials/images/ |
| `comparison-visual` | How is it different from the alternative? | Own product real; alternative as a generic silhouette or "other brands"; never a competitor photo without licence | own side yes | Trademark and comparative advertising exposure (HEURISTIC) |
| `gift-presentation` | Is it giftable? | Real gift box, wrap, card; nothing shown that does not ship | yes | Gift purchase relevance (OPERATOR) |
| `size-reference` | Will it fit me? | Model with stated height and size worn; fit table in HTML; body-part placement | yes | Baymard human model https://baymard.com/blog/human-model |
| `swatch` | Which shade or fabric is mine? | Real swatch per variant; shade on skin for colour cosmetics; flat colour chips may be CSS from catalog hex | yes for photos | Baymard health and beauty https://baymard.com/blog/health-and-beauty-ux-research |
| `label-or-facts-panel` | What does the label say? | Legible real photo of the panel, or the panel as HTML text | yes | 21 CFR 101.36 supplement facts https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-101/subpart-C/section-101.36 |

## 2. Page type x job matrix

Legend: `R` required (a slot exists, or the plan lists the job under
"Mandatory sections omitted" with the merchant's reason); `R*` required when
the footnoted condition holds; `S` recommended; `-` usually skip. The 30 ids
are those listed in `references/page-types/_index.md`. A type file's
`imagery.required_jobs` must contain every `R` in its row and may add `S`
jobs; it may not drop an `R` without a footnote condition.

Footnotes: (a) variants exist; (b) product is worn or applied to the body;
(c) product ships as a set or multi-part; (d) consumable with a regulated
label (food, supplement, cosmetic); (e) a verified before-after ledger row
exists, otherwise fill with a context image; (f) real prototype media exists,
otherwise typographic hero and no product slot; (g) on the results screen
only; (h) the offer includes a gift or bundle.

### 2.1 Jobs 1 to 10

| Page type | identity | detail | scale | texture | in-use | context | variation | included-items | sequence | result-or-context |
|---|---|---|---|---|---|---|---|---|---|---|
| `ad-landing-page` | R | S | R | - | R | S | R*a | R*c | S | S |
| `pdp` | R | R | R | S | R | S | R*a | R*c | S | - |
| `pdp-hybrid-landing` | R | R | R | S | R | S | R*a | R*c | S | S |
| `advertorial` | R | - | - | - | R | S | - | - | S | R*e |
| `listicle` | R | S | - | - | R | - | - | - | S | S |
| `seo-buyers-guide` | R | S | - | - | S | - | - | - | - | - |
| `comparison-us-vs-them` | R | S | S | - | S | - | - | S | - | - |
| `quiz-funnel` | R*g | - | - | - | S | - | S | - | - | - |
| `bundle-kit` | R | S | S | - | R | S | S | R | R | - |
| `offer-page` | R | - | S | - | S | - | S | R*h | - | - |
| `sale-clearance-flash` | R | - | - | - | - | - | S | - | - | - |
| `seasonal-gifting` | R | S | S | - | S | R | S | S | - | - |
| `gift-guide` | R | - | S | - | S | S | - | - | - | - |
| `launch-waitlist-preorder` | R*f | S | S | - | S | - | - | - | - | - |
| `restock` | R | S | - | - | S | - | R*a | - | - | - |
| `subscription` | R | - | S | - | S | S | S | R | R | - |
| `ugc-creator-collab` | R | S | - | - | R | - | S | - | - | S |
| `video-sales-page` | R | - | - | - | S | - | - | S | - | S |
| `brand-story-founder` | S | S | - | S | S | R | - | - | S | - |
| `ingredient-science` | R | S | - | S | - | - | - | - | S | S*e |
| `collection-landing` | R | - | - | - | S | S | S | - | - | - |
| `homepage` | R | - | - | - | R | S | - | - | - | - |
| `lookbook-shop-the-look` | R | S | - | S | R | R | S | - | - | - |
| `lead-capture-giveaway` | R | - | - | - | S | - | - | - | - | - |
| `referral-loyalty-vip` | S | - | - | - | - | - | - | - | - | - |
| `retargeting-warm` | R | S | S | - | S | - | S | S | - | S |
| `thank-you-post-purchase` | S | - | - | - | - | - | - | S | S | - |
| `faq-support-led` | S | - | - | - | - | - | - | - | S | - |
| `trial-sample` | R | - | R | - | S | - | - | R | S | - |
| `wholesale-b2b` | R | S | S | - | - | - | S | S | - | - |

### 2.2 Jobs 11 to 20

| Page type | ingredient-or-material | packaging | founder-or-team | ugc | diagram | comparison-visual | gift-presentation | size-reference | swatch | label-or-facts-panel |
|---|---|---|---|---|---|---|---|---|---|---|
| `ad-landing-page` | R*d | - | S | S | - | - | - | R*b | R*a | R*d |
| `pdp` | R*d | - | - | S | S | - | - | R*b | R*a | R*d |
| `pdp-hybrid-landing` | R*d | - | S | S | - | - | - | R*b | R*a | R*d |
| `advertorial` | S | - | S | S | - | - | - | - | - | - |
| `listicle` | S | - | S | S | - | S | - | - | - | - |
| `seo-buyers-guide` | S | - | - | S | S | R | - | - | - | S |
| `comparison-us-vs-them` | S | - | - | S | S | R | - | - | - | S |
| `quiz-funnel` | - | - | - | - | S | - | - | - | S | - |
| `bundle-kit` | S | S | - | S | - | - | S | - | - | S*d |
| `offer-page` | - | S | - | S | - | - | - | - | - | - |
| `sale-clearance-flash` | - | - | - | - | - | - | - | - | S | - |
| `seasonal-gifting` | - | R | - | S | - | - | R | - | - | - |
| `gift-guide` | - | S | - | - | - | - | R | - | - | - |
| `launch-waitlist-preorder` | S | S | R | - | S | - | - | - | - | - |
| `restock` | - | - | - | S | - | - | - | - | S*a | - |
| `subscription` | S | S | - | S | S | - | - | - | - | S*d |
| `ugc-creator-collab` | - | - | - | R | - | - | - | - | - | - |
| `video-sales-page` | - | - | S | S | - | - | - | - | - | - |
| `brand-story-founder` | S | - | R | S | - | - | - | - | - | - |
| `ingredient-science` | R | - | S | - | R | - | - | - | - | R*d |
| `collection-landing` | - | - | - | - | - | - | - | - | S*a | - |
| `homepage` | - | - | S | S | - | - | - | - | - | - |
| `lookbook-shop-the-look` | - | - | - | S | - | - | - | S*b | S | - |
| `lead-capture-giveaway` | - | S | - | - | - | - | - | - | - | - |
| `referral-loyalty-vip` | - | - | - | S | S | - | - | - | - | - |
| `retargeting-warm` | - | - | - | S | - | - | - | - | - | - |
| `thank-you-post-purchase` | - | S | - | - | - | - | - | - | - | - |
| `faq-support-led` | - | - | - | - | S | - | - | S | - | - |
| `trial-sample` | - | S | - | S | - | - | - | - | - | S*d |
| `wholesale-b2b` | - | R | - | - | S | - | - | - | S*a | S |

Why `ugc` is `S` almost everywhere: it depends on rights the merchant may not
hold (`references/proof/ugc-rights-and-display.md`). When a rights-cleared
UGC set exists in the library, treat `S` as `R` for `pdp`,
`pdp-hybrid-landing`, `ad-landing-page`, `listicle`, `advertorial` and
`retargeting-warm`. Rationale: 67% of sites lack UGC images and shoppers who
engage with UGC convert more (correlational) https://baymard.com/blog/current-state-ecommerce-product-page-ux ,
https://www.yotpo.com/blog/increase-conversion-rate-ecommerce/ .

## 3. Minimum image counts per page type

Counts are total image slots on the page, hero included, before video.
"per item" means one identity image per product card, list item or look. All
rows HEURISTIC unless an anchor is given. The vertical table in section 4
raises the PDP gallery minimum; the higher number wins.

| Page type | Min images | Composition of the minimum | Anchor |
|---|---|---|---|
| `ad-landing-page` | 6 | hero, identity, scale, in-use, two supporting jobs from the row | Baymard: one or two images is insufficient https://baymard.com/blog/secondary-hover-information |
| `pdp` | vertical gallery min + 2 | gallery per section 4, plus one in-use and one context or proof image below the buy box | same |
| `pdp-hybrid-landing` | vertical gallery min + 2 | as `pdp` | same |
| `advertorial` | 4 | editorial hero, identity near the offer bridge, in-use, result-or-context | checklist example in `_checklist-format.md` |
| `listicle` | items + 1 | one image per reason plus identity at the buy box | teardowns: per-reason images on Miracle (1 hero + 6), HexClad, Skinesa (OPERATOR) |
| `seo-buyers-guide` | entries + 1 | one identity per ranked entry (own product real; others licensed or silhouette) plus one hero | HEURISTIC; comparison rules as `comparison-us-vs-them` |
| `comparison-us-vs-them` | 3 | identity, comparison-visual, in-use or detail | HEURISTIC |
| `quiz-funnel` | 1 + results | optional entry visual; identity per recommended product on results | HEURISTIC |
| `bundle-kit` | components + 3 | identity per component, set flat lay, in-use, sequence | Salt of the Earth builder teardown (OPERATOR) |
| `offer-page` | 3 | identity, gift or bundle contents when (h), in-use | HEURISTIC |
| `sale-clearance-flash` | per item | one identity per card; hero optional | HEURISTIC |
| `seasonal-gifting` | per item + 2 | cards plus one occasion context and one gift-presentation | Sea Bags gift guide teardown (OPERATOR) |
| `gift-guide` | per item + 1 | cards plus one gift-presentation | same |
| `launch-waitlist-preorder` | 2 | real prototype or none (f), founder | Klassy Pet teardown: no product imagery was the page's weakest point (OPERATOR) |
| `restock` | 3 | identity, variation when (a), ugc or in-use | HEURISTIC |
| `subscription` | 4 | identity, included-items per delivery, sequence, in-use | Seed teardown: 5 gallery images incl. welcome kit and diagram (OPERATOR) |
| `ugc-creator-collab` | 5 | four ugc tiles or clips plus identity | Baymard UGC gaps (above) |
| `video-sales-page` | 2 | video poster, identity at the offer | HEURISTIC |
| `brand-story-founder` | 4 | founder-or-team, place (context), process (sequence), product | NN/g real people (above) |
| `ingredient-science` | 4 | identity, ingredient-or-material, diagram, label-or-facts-panel when (d) | HEURISTIC |
| `collection-landing` | per item | one identity per card; banner optional | HEURISTIC |
| `homepage` | 4 | hero in-use, two category or best-seller identity images, one story image | HEURISTIC |
| `lookbook-shop-the-look` | 4 looks | each look with its shoppable items visible | HEURISTIC |
| `lead-capture-giveaway` | 1 | identity of the prize or product | HEURISTIC |
| `referral-loyalty-vip` | 0 to 1 | rewards identity optional | HEURISTIC |
| `retargeting-warm` | 3 | identity, the objection image (scale, detail or included-items), proof | HEURISTIC |
| `thank-you-post-purchase` | 0 to 1 | ordered item or one add-on | HEURISTIC |
| `faq-support-led` | 0 to 2 | care or sizing sequence, diagram | HEURISTIC |
| `trial-sample` | 4 | identity, scale against the full size, included-items, in-use | HEURISTIC |
| `wholesale-b2b` | 3 | identity, case or carton packaging, detail | HEURISTIC |

## 4. Minimum image counts per vertical

Gallery minimums apply to `pdp` and `pdp-hybrid-landing`; the LP column
applies to single-product landing types. HEURISTIC anchored to the cited
research. Show all thumbnails up to 10 to 14; beyond that an explicit "+N"
control. Hidden thumbnails are missed by 50 to 80% of users
https://baymard.com/blog/truncating-product-gallery-thumbnails .

| Vertical | PDP gallery min | LP total min | Anchor |
|---|---|---|---|
| Supplements, simple consumables | 5 | 6 | 3+ thumbnails needed even in lists https://baymard.com/blog/current-state-product-list-and-filtering |
| Beauty | 6, plus one per shade shown on skin | 7 | Arm swatch, human model per shade, applied makeup https://baymard.com/blog/health-and-beauty-ux-research |
| Fashion, accessories | 8 to 12 | 8 | "5 to 15 thumbnails" for apparel https://baymard.com/blog/secondary-hover-information |
| Home, furniture | 8 | 7 | In-scale and dimension image mandatory https://baymard.com/blog/furniture-and-home-decor-ux-research |
| Electronics | 7 | 7 | Compatibility, in-box, in-hand scale (Baymard 7 types) |
| Food, beverage | 5 | 6 | Appetising food is a "magnetic" image feature http://ptgmedia.pearsoncmg.com/images/9780321498366/excerpts/eyetrackwebu_06to226.pdf |
| Jewellery | 6 | 6 | Macro plus on-body scale https://baymard.com/blog/human-model |
| Pets | 6 | 6 | Baymard "animate" type; photos critical in pets https://www.bazaarvoice.com/wp-content/themes/bazaarvoice/_sei-2019/static/downloads/BV19-SEI-Main-NA-Final.pdf |
| Baby | 6 | 6 | Safety details and correct use (HEURISTIC) |
| Luxury | 6 | 6 | Fewer, larger, more whitespace https://speero.com/post/how-product-image-size-impacts-value-perception-original-research |

## 5. Hero treatment per page type

Values are the `imagery.hero` vocabulary from `_checklist-format.md`.
`before-after` is a vocabulary value that no type uses: display rule 9 in
`references/proof/proof-ledger.md` forbids before/after in the hero.
`typographic` is allowed only where listed or when the ad that sent the
traffic was typographic (`references/copy/message-match.md`).

| Page type | Primary hero | Alternate | Never |
|---|---|---|---|
| `ad-landing-page` | `product-in-hand` or `product-in-context`, matched to the ad frame | `ugc-screenshot` when the ad was UGC-style | `grid`, `typographic` unless the ad was |
| `pdp` | `packshot` with the selected variant | `product-in-hand` | `editorial-lifestyle` as first gallery image |
| `pdp-hybrid-landing` | `product-in-context` matched to the ad | `product-in-hand` | `grid` |
| `advertorial` | `editorial-lifestyle` | `ugc-screenshot` | `packshot`, price or offer visuals |
| `listicle` | `editorial-lifestyle` | `product-in-context` | `grid` |
| `seo-buyers-guide` | `editorial-lifestyle` | `grid` (the ranked entries) or `typographic` | `packshot` of the own product alone (reads as an ad to a search reader) |
| `comparison-us-vs-them` | `packshot` (own product) | `product-in-hand` | `before-after` |
| `quiz-funnel` | `typographic` | `editorial-lifestyle` | `packshot` before routing |
| `bundle-kit` | `grid` (components laid out) | `packshot` of the set | `editorial-lifestyle` without the components |
| `offer-page` | `packshot` | `product-in-hand` | text of the offer inside the image |
| `sale-clearance-flash` | `grid` | `typographic` | any single-product hero |
| `seasonal-gifting` | `product-in-context` (occasion) | `grid` | `packshot` alone |
| `gift-guide` | `editorial-lifestyle` | `grid` | `packshot` alone |
| `launch-waitlist-preorder` | `packshot` when (f) | `typographic` | generated product render |
| `restock` | `packshot` | `product-in-hand` | `editorial-lifestyle` |
| `subscription` | `product-in-context` (routine) | `packshot` with included items | `grid` |
| `ugc-creator-collab` | `video-poster` (9:16) | `ugc-screenshot` | `packshot` |
| `video-sales-page` | `video-poster` | none | anything else |
| `brand-story-founder` | `editorial-lifestyle` (real founder or place) | `typographic` | `packshot` |
| `ingredient-science` | `editorial-lifestyle` (ingredient or material) | `typographic` | `before-after` |
| `collection-landing` | `grid` | `editorial-lifestyle` banner above the grid | `packshot` alone |
| `homepage` | `editorial-lifestyle` with the product legible | `product-in-context` | `grid` of logos or badges |
| `lookbook-shop-the-look` | `editorial-lifestyle` | none | `packshot` |
| `lead-capture-giveaway` | `packshot` (prize) | `product-in-context` | `typographic` when a prize exists |
| `referral-loyalty-vip` | `typographic` | `product-in-context` | `packshot` |
| `retargeting-warm` | `packshot` or `product-in-hand` | `product-in-context` | `editorial-lifestyle` |
| `thank-you-post-purchase` | `typographic` | `packshot` of the ordered item | `editorial-lifestyle` |
| `faq-support-led` | `typographic` | none | any photo hero |
| `trial-sample` | `product-in-hand` (sample at scale) | `packshot` | `editorial-lifestyle` |
| `wholesale-b2b` | `packshot` | `grid` (line sheet) | `editorial-lifestyle` |

Traffic overrides (RESEARCH, OPERATOR): cold paid social wants the same
creative concept as the ad, product identifiable within one second
https://cxl.com/blog/give-your-advertising-roi-a-serious-boost-by-maintaining-scent/ ;
"ugly" UGC ads must not land on a polished studio hero
https://www.hottgrowth.com/post/ugly-ads-dont-mean-bad-ads-try-these-expert-tips-for-high-intent-ads ;
Shopping-feed clicks land on the same packshot used in the feed
https://support.google.com/merchants/answer/6324350 .

## 6. Lifestyle vs studio balance per vertical

Share of all image slots on the page (gallery plus landing slots). HEURISTIC
anchored to the cited evidence. "Studio" includes packshot, cut-out, swatch,
facts panel; "Lifestyle" includes in-use, context, on-model; "UGC" is
rights-cleared customer media only.

| Vertical | Studio | Lifestyle | UGC | Anchor |
|---|---|---|---|---|
| Fashion, accessories | 30% | 50% | 20% | On-model needed for fit and drape https://baymard.com/blog/human-model |
| Beauty | 35% | 45% | 20% | Arm swatches and model per shade https://baymard.com/blog/health-and-beauty-ux-research |
| Supplements, wellness | 50% | 35% | 15% | Show the powder mixing (Sharma, above) |
| Home, furniture | 30% | 55% | 15% | 28 to 37% of sites miss in-scale https://baymard.com/blog/in-scale-product-images |
| Electronics | 55% | 35% | 10% | Larger images raise perceived value for spec goods https://speero.com/post/how-product-image-size-impacts-value-perception-original-research |
| Food, beverage | 45% | 40% | 15% | Appetising food is magnetic (NN/g excerpt, above) |
| Luxury | 60% | 35% | 5% | Whitespace raised perceived value for experience goods (Speero, above) |
| Jewellery | 45% | 40% | 15% | Baymard human model (above) |
| Pets | 35% | 45% | 20% | Baymard animate type |
| Baby | 40% | 45% | 15% | Safe, correct use with caregiver (ASCI draft, see `generation-policy.md`) |

## 7. When a required job is missing

Procedure:

1. Map every existing Shopify media item and library asset to one job
   (view it; do not trust the filename).
2. For each `R` or `R*` job with no image, create a slot with the job in
   Role/purpose (`product_media` plus the job, or the generation purpose for
   backdrop jobs) and `Status: planned`.
3. Resolve the slot through `references/assets/asset-sourcing-sequence.md`.
   Only the source types below may fill the job.
4. A slot that no allowed source fills stays `planned`; the section is built
   without it or removed with a note. Never a placeholder.

| Job | shopify | library | merchant-upload | supplier | stock | generated |
|---|---|---|---|---|---|---|
| `identity` | yes | yes (product-shot tag) | yes | yes, exact SKU | never | never |
| `detail` | yes | yes | yes | yes | never | never |
| `scale` | yes | yes | yes | no | never | never |
| `texture` | yes | yes | yes | yes | raw material only, not the product | never |
| `in-use` | yes | yes | yes (brand-owned) | no | never as "customer" | ASK only (`product_lifestyle` with identity preserved) |
| `context` | yes | yes | yes | no | scene without the product | ALLOW (`product_composite` over a real cut-out, `hero_bg` backdrop) |
| `variation` | yes | yes | yes | yes | never | never |
| `included-items` | yes | yes | yes | no | never | never |
| `sequence` | yes | yes | yes | no | never | never (steps become HTML text with the icon set) |
| `result-or-context` | no | yes (ledger row) | yes (ledger row) | no | never | never for result; context as above |
| `ingredient-or-material` | yes | yes | yes | yes | raw ingredient, not presented as own sourcing | never |
| `packaging` | yes | yes | yes | no | never | never (merchant's own render only, captioned) |
| `founder-or-team` | no | yes | yes | no | never | never |
| `ugc` | no | yes (rights record) | yes (rights record) | no | never | never |
| `diagram` | no | yes | yes | yes | no | author inline SVG; raster generation never |
| `comparison-visual` | own side | own side | own side | no | never | never; alternative as inline SVG silhouette |
| `gift-presentation` | yes | yes | yes | no | never | never |
| `size-reference` | yes | yes | yes | no | never | never; fit table in HTML |
| `swatch` | yes | yes | yes | yes | never | never; flat chips as CSS from catalog hex |
| `label-or-facts-panel` | yes | yes | yes | yes | never | never; panel as HTML text preferred |

## 8. Rules

Format: imperative; tag; rationale; a check. `$W` is the page workspace.
Checks use BSD grep and perl on macOS.

IJ1. Give every image on the page a named job from section 1; remove imagery that has none. RESEARCH.
Rationale: users look at 42% of images for under 0.2 seconds, ignore stock 85% of the time, and look at content-related images twice as often as unrelated ones http://ptgmedia.pearsoncmg.com/images/9780321498366/excerpts/eyetrackwebu_06to226.pdf .
Check: every `<img>` with non-empty alt in `$W/lexsis-source.html` maps to a slot id in `page-plan.md` whose row names a job; unmapped count is 0.

IJ2. Create a `planned` slot for every `R` job in the type's row that the existing media does not cover, before asking any asset question. OPERATOR.
Rationale: `references/consumer-behavior-cro.md` forbids asking "do you want custom images" before the gap is named.
Check: for the type's `R` jobs, `grep -c '<job>' page-plan.md` under "## Asset slots" is at least 1 each, or the job appears under "Mandatory sections omitted".

IJ3. Never fill an identity-bound job from stock or generation. LAW.
Rationale: feed and marketplace rules require the real product https://support.google.com/merchants/answer/7052112 ; fake customers and testimonials are banned under 16 CFR 465 https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers .
Check: `python3 -c "import json;m=json.load(open('$W/page-manifest.json'));print(sum(1 for a in m['assets'] if a.get('generated') and a['role'] in ('product_media','proof','logo')))"` prints 0; no slot row pairs `stock` with `product_media` or `proof`.

IJ4. Show the same SKU, variant and angle family in the hero as in the ad creative that sends the traffic. RESEARCH, OPERATOR.
Rationale: 98% of paid ads have poor message match https://unbounce.com/conversion-glossary/definition/message-match/ ; same photo, not the same type of product https://cxl.com/blog/give-your-advertising-roi-a-serious-boost-by-maintaining-scent/ .
Check: yes/no in `page-plan.md` message-match line after comparing the `lexsis_campaigns.creatives` frame and the hero slot with `lexsis_assets.view`.

IJ5. Provide one `scale` image wherever the matrix marks it `R`; a hand, body, room or known object. RESEARCH.
Rationale: 42% of users try to judge size from images https://baymard.com/blog/current-state-ecommerce-product-page-ux .
Check: a slot with job `scale` exists and its alt matches `perl -ne 'print if /held|in hand|next to|for scale|on a .* table|in a .* room/i'`.

IJ6. Give worn or applied products an on-body image (`size-reference` or `in-use` with a model). RESEARCH.
Rationale: cut-outs alone hide fit, length and who the product is for https://baymard.com/blog/human-model .
Check: for beauty, fashion and jewellery pages, at least one slot alt names a body part or "model".

IJ7. Meet the vertical gallery minimum and show every thumbnail or an explicit "+N" control. RESEARCH.
Rationale: hidden thumbnails are missed by 50 to 80% of users https://baymard.com/blog/truncating-product-gallery-thumbnails .
Check: gallery slot count is at least the section 4 minimum; in the hosted draft at 390 the thumbnail strip shows all items or a "+N" control (yes/no in `qa-report.md`).

IJ8. Use one static hero; never a hero carousel. RESEARCH.
Rationale: about 1% of visitors click a carousel and 84% of those clicks go to slide 1 https://erikrunyon.com/2013/01/carousel-interaction-stats/ ; auto-forwarding is a known usability failure https://www.nngroup.com/articles/auto-forwarding/ .
Check: `perl -0ne 'print scalar(() = /section: hero.*?(carousel|slider|data-slide|Swiper)/gis), "\n"' $W/lexsis-source.html` prints 0.

IJ9. Keep one background, lighting, orientation and crop scale for every image of the same job on the page. RESEARCH.
Rationale: consistent product photography makes lists scannable and comparable https://www.nngroup.com/articles/product-photos-listing-pages/ .
Check: open all `identity` slots together with `lexsis_assets.view`; record yes/no "consistent set" in `qa-report.md`.

IJ10. Keep the hero image, headline and first CTA inside the first 390px screen; hero media takes no more than 60% of the viewport height on mobile. HEURISTIC anchored to RESEARCH.
Rationale: big pictures on small screens push the task below the fold https://www.nngroup.com/articles/big-pictures-small-screens/ .
Check: at 390 the hero CTA (types with `cta.first_after_section: 0`) appears above y=844 in the hosted screenshot.

IJ11. Point a hero face toward the headline, product or CTA, not the camera, except in beauty and eyewear where the face is the canvas. RESEARCH.
Rationale: product-directed gaze increased attention to product, logo and copy https://doi.org/10.1002/acp.1763 ; https://www.objectiveexperience.com/eye-tracking-ux-research/ .
Check: view the hero; yes/no in `qa-report.md`.

IJ12. Use a typographic hero only where section 5 lists it or the plan's message-match line records a typographic ad. RESEARCH.
Rationale: shoppers rely on product imagery for the decision (Baymard, NN/g above).
Check: the type file's `imagery.hero` equals the primary or alternate value in section 5, or the plan records the override with the ad reference.

IJ13. Never place before/after imagery in the hero on any type. LAW, OPERATOR.
Rationale: before/after is an objective claim needing signed, dated substantiation https://www.asa.org.uk/advice-online/before-and-after-photos.html ; `references/proof/proof-ledger.md` display rule 9.
Check: `grep -c '"hero": "before-after"' references/page-types/*.md` prints 0; the hero section contains no element with `before-after` in its id or class.

IJ14. Record the job coverage result in the plan's Consumer decision model block ("Gallery jobs: covered; missing; slots created"). OPERATOR.
Rationale: `/design-page` implements the block without reopening it.
Check: `grep -c '^\*\*Gallery jobs\.\*\*' $W/page-plan.md` prints 1 and the line lists no "TBD".

## Sources

- Baymard, product image types https://baymard.com/blog/ux-product-image-categories ; in-scale https://baymard.com/blog/in-scale-product-images ; human model https://baymard.com/blog/human-model ; PDP UX 2026 https://baymard.com/blog/current-state-ecommerce-product-page-ux ; thumbnails https://baymard.com/blog/secondary-hover-information ; truncation https://baymard.com/blog/truncating-product-gallery-thumbnails ; health and beauty https://baymard.com/blog/health-and-beauty-ux-research ; furniture https://baymard.com/blog/furniture-and-home-decor-ux-research ; product lists https://baymard.com/research/ecommerce-product-lists
- NN/g, photos as web content https://www.nngroup.com/articles/photos-as-web-content/ ; eyetracking excerpt http://ptgmedia.pearsoncmg.com/images/9780321498366/excerpts/eyetrackwebu_06to226.pdf ; listing photos https://www.nngroup.com/articles/product-photos-listing-pages/ ; big pictures small screens https://www.nngroup.com/articles/big-pictures-small-screens/ ; auto-forwarding https://www.nngroup.com/articles/auto-forwarding/
- Erik Runyon, carousel stats https://erikrunyon.com/2013/01/carousel-interaction-stats/
- Gaze: Hutton and Nolte 2011 https://doi.org/10.1002/acp.1763 ; Breeze https://www.objectiveexperience.com/eye-tracking-ux-research/
- Speero/CXL image size study https://speero.com/post/how-product-image-size-impacts-value-perception-original-research
- Process Creative, what's included test https://www.processcreative.com.au/blog/a-b-testing-does-showing-whats-in-the-box-actually-lift-conversions
- Unbounce message match https://unbounce.com/conversion-glossary/definition/message-match/ ; CXL scent https://cxl.com/blog/give-your-advertising-roi-a-serious-boost-by-maintaining-scent/ ; Sharma Brands https://sharmabrands.com/blogs/newsletter/7-biggest-landing-page-mistakes ; Hott Growth https://www.hottgrowth.com/post/ugly-ads-dont-mean-bad-ads-try-these-expert-tips-for-high-intent-ads
- Bazaarvoice SEI 2022 https://www.bazaarvoice.com/press/sei-2022-press-release/ ; SEI 2019 https://www.bazaarvoice.com/wp-content/themes/bazaarvoice/_sei-2019/static/downloads/BV19-SEI-Main-NA-Final.pdf ; Yotpo https://www.yotpo.com/blog/increase-conversion-rate-ecommerce/
- Platform rules: Amazon https://sellercentral.amazon.com/help/hub/reference/external/G1881 ; Google Merchant https://support.google.com/merchants/answer/6324350 , https://support.google.com/merchants/answer/7052112
- Regulation: FTC reviews rule Q&A https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers ; FTC health guidance https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance ; ASA before/after https://www.asa.org.uk/advice-online/before-and-after-photos.html ; 21 CFR 101.36 https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-101/subpart-C/section-101.36 ; W3C images tutorial https://www.w3.org/WAI/tutorials/images/
- Wistia https://wistia.com/blog/video-marketing-statistics
