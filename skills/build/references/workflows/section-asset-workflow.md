# Section asset workflow

The per-section media loop. `/plan-page` runs it for every section in the
type file's Anatomy order while filling the `## Workflow` block; `/design-page`
runs it again for any slot the plan left `planned`. It operationalises the
policy layer in `references/assets/` and never overrides it: sourcing order
and checks live in `references/assets/asset-sourcing-sequence.md`, ALLOW / ASK
/ NEVER in `references/assets/generation-policy.md`, jobs and minimum counts in
`references/assets/image-jobs-by-page-type.md`, aspects and resolutions in
`references/assets/slot-spec.md`, video in `references/assets/video-rules.md`,
vertical additions in `references/assets/imagery-by-vertical.md`. Trust
elements pass through `references/proof/proof-ledger.md` before they are
imagery. House rules in `references/design-rules.md` apply to every outcome.
The island half of each section is `references/workflows/island-selection-workflow.md`.

The premise: a section is imagery plus a few words, or it is not on the page.
Copy is written after the image is found, as its caption. A section that ends
up as a colour band (N2), an emoji row (N1), an icon tile stack (N3, N12), a
gradient wash (N7), a text-only card (N8) or a paragraph of filler is not a
fallback; it is the failure this loop exists to prevent.

## 1. The loop

Run once per section, in Anatomy order, before any copy is drafted. Stop at
the first step that yields an asset passing the universal checks in section 3
of `asset-sourcing-sequence.md` (identity viewed, resolution, aspect, no
baked-in text, no watermark, rights recorded) **and** the fit review in
section 1b below. No asset is ever used sight unseen: a search result, a
filename, a tag or an alt text is a candidate, not a decision. Every stop
writes one row in the plan's Asset slots table.

1. **Does this section need imagery?** Default yes. The only sections that
   stand without an image: `faq`, `objections`, `legal`, `shipping-returns`,
   `disclaimer`, a `trust-bar` made of policy facts, and a text-only
   `founder-note` with a real name and signature. Two more cases follow from
   other files and are not new exemptions: a hero on a type whose row in
   section 5 of `image-jobs-by-page-type.md` lists `typographic` as the primary
   treatment (`quiz-funnel`, `referral-loyalty-vip`, `thank-you-post-purchase`,
   `faq-support-led`) or where the plan's message-match line records a
   typographic ad; and a proof quote (`reviews`, `testimonial-spotlight`,
   `expert-endorsement`, `press-quotes`), because a verbatim attributed quote
   is itself the artefact under N8 and takes real customer media or none.
   Chrome (`announcement`, `header`, `footer`, `sticky-cta`), buy-box
   sub-elements (`variant-picker`, `quantity-breaks`, `subscription-toggle`,
   `plan-selector`, `bnpl-line`, `payment-options`, `delivery-cutoff`,
   `countdown`, `stock-indicator`, `review-summary`) and opening text lines
   (`dateline`, `hook`, `toc`, `qualifier`) sit beside another section's image
   and are outside the loop. Everything else continues to step 2.
2. **Which job, which aspect?** Name one primary job from the vocabulary in
   `references/page-types/_checklist-format.md`, taken from the type's row in
   section 2 of `image-jobs-by-page-type.md` plus the vertical's additions in
   section 0 of `imagery-by-vertical.md`. Take the aspect and minimum
   resolution from the matching slot role in `slot-spec.md`. Create slot `A<n>`
   with `Status: planned`. The section-type table in section 2 below gives the
   usual job per section id.
3. **Catalog media first.** `lexsis_catalog.get` for the product returns the
   media list with alt text and order. View every candidate with
   `lexsis_assets.view`; alt text and filenames do not establish identity
   (AS3). A media item that does the job is the answer: Source decision
   `shopify media, viewed`, `sourceType: shopify`. A PDP hero or gallery never
   generates when product media exists (GN1, GN12). Stop here when it fits.
4. **Library by tag, then semantic, then filename.** `lexsis_asset_library.search`
   with `theme_id` (required), `kind: image` (`svg` for logos and badges),
   `limit: 48`. First `mode: tags` with the tag from the section-type table:
   `hero` or `banner` for heroes and closing images, `lifestyle` for in-use and
   context, `product-shot` for identity, detail, flat lays and cards, `logo`
   for press and issuer marks, `social-proof` for customer media. Then
   `mode: semantic` with the job in plain words ("serum held in a hand for
   scale", "founder in the workshop"). Then `mode: filename` when the merchant
   named a file. The host may open the asset picker and return a
   `Design asset selection:` message; map its `assets[]` to slot ids in
   `selection_order`. View; check the licence scope and any ledger row.
   Outlet logos qualify only through `references/proof/press-and-media-mentions.md`
   and customer media only through `references/proof/ugc-rights-and-display.md`;
   neither fills a slot without its ledger row. Stop when it fits: Source
   decision `library <id>, viewed`.
5. **Merchant-owned sources.** In order: `lexsis_campaigns.creatives` for ad
   images the merchant already runs (the best hero source for message match;
   reject frames with baked-in text under AS11 and request the clean layered
   original); originals from the brand site or the brand's own Instagram or
   TikTok, captured and brought in with `lexsis_asset_import.import` (the
   merchant owns them; a post that shows a creator or customer is UGC and
   needs a ledger row, AS13); supplier or manufacturer media of the exact SKU
   after a written licence check. Identity-bound jobs (identity, detail,
   scale, texture, in-use, variation, included-items, sequence, result,
   packaging, founder, UGC, swatch, size-reference, label) end at this step:
   found here or not at all.
6. **Generation, only for an ALLOW purpose that fits the job.** Generation
   fills backdrops, textures, decoration and `context` composites over a real
   cut-out. It never fills an identity-bound job (GP14) and never enters
   `gallery`, `buy-box`, `product-hero` or any proof section (GP11). Decide
   the purpose from the table below; run the section 8 checklist of
   `generation-policy.md`; draft the Generation record row. Do not call
   `lexsis_drafts.asset_generate` yet: `lexsis_workspace.credits` and the
   merchant's yes for the named batch are part of step 7 (AS12). On a type
   whose checklist sets `imagery.hero` to `packshot` or `ugc-screenshot`
   (`pdp`, `restock`, `offer-page`, `comparison-us-vs-them`,
   `ugc-creator-collab` and others in section 5 of `image-jobs-by-page-type.md`)
   even an ALLOW purpose needs the "backdrops sit below the hero only" confirm
   line from section 4 of `generation-policy.md`.

   | Section type | Job the gap left | Purpose that fits | Placement | Class |
   |---|---|---|---|---|
   | `hero`, `closing-cta` (bold moment only) | backdrop behind a real cut-out or HTML type | `hero_bg` landscape plus portrait | the one full-bleed moment (N2) | ALLOW |
   | the one full-bleed section the plan names | backdrop | `section_bg` | bold moment only; never behind body copy | ALLOW |
   | `benefits`, `features`, `discovery`, `solution` | `context` | `product_composite` with the real cut-out first in `reference_images` | feature image, lifestyle inset; never gallery | ALLOW |
   | a card wrapping a product, table or form (N8) | flat tone behind the object | `card_bg` | inside that card only | ALLOW |
   | page-wide grain at 8% or less, or inside a media object | texture | `texture_fill`, `pattern_tile` | one page background (N2) | ALLOW |
   | at most two per page, never behind text | brush mark or silhouette | `decorative_element` (transparent, separate provider) | static, `aria-hidden` (N7, N10) | ALLOW |
   | `benefits`, `how-it-works`, `story` where `in-use` is missing | a scene around the composited real product | `product_lifestyle` | captioned "AI-generated scene"; never `ugc-grid`, `reviews`, gallery position one | ASK, `askApproved` |
   | `gallery`, `reviews`, `ugc-grid`, `before-after`, `press-marquee`, `certifications`, `founder-note`, `ingredients` (as own sourcing), anything with people, text, logos, results or the product itself | any | none | none | NEVER |

   An approved `product_lifestyle` fills the slot an `in-use` gap left, but
   the job it performs is `context` (no people, no hands) and the plan records
   the `in-use` requirement as still unmet; the slot's Role/purpose job is
   written as `context` so GP14 holds. Prompt constraints, negative lists,
   quality tiers and disclosure labels are in sections 3 to 6 of
   `generation-policy.md`; do not paraphrase them here.
7. **Tell the user what is missing and offer the remedies.** A missing asset
   is never a silent drop. After steps 3 to 5 have run for every slot on the
   page (AS8), list each unresolved slot with its section, image job, aspect,
   count and why it matters to the shopper's decision. Then offer, per slot,
   the three answers: **upload it** (`lexsis_asset_upload.upload` for the
   local-file UI, or `lexsis_asset_import.import` with exactly one source:
   a URL, image base64 plus MIME type, or conversation attachments),
   **generate it** when the purpose is feasible under
   `generation-policy.md` (ALLOW: directly after `lexsis_workspace.credits`
   and the merchant's credit confirmation; ASK: with the merchant's yes for
   that slot, logged per its section 7; NEVER: say "needs a real photo" and
   the one-line reason), or **skip the section** with what the page does
   instead. Group into one turn with at most three questions
   (`references/consumer-behavior-cro.md`); section 4 gives the exact pattern.
   In `fast-draft`, proceed with a reversible, placeholder-free choice (reuse
   the closest existing asset that honestly does a related job, or leave the
   slot `planned`) and still list every missing asset with the same three
   answers in the plan and in the draft summary, so the user can upload or
   approve generation later. Credits are never spent without a yes.
   Scope upload/import to the selected workspace and theme. For the upload
   UI, wait for the user's uploaded-asset message. Without inline UI, ask
   for a URL or conversation attachment and import it; import never opens
   the upload UI. `lexsis_asset_library.search` with `query: ""` is a separate
   option for choosing existing library assets, not uploading local files.
8. **Skip or merge only when the user chooses it.** Then the section leaves
   the page or its one fact moves to a neighbour: a benefit without an image
   becomes a buy-box bullet; a stat without a real image becomes one line in
   the trust-bar or hero subhead; a how-it-works without step photos becomes
   `usage` text under the buy box. A mandatory section goes under "Mandatory
   sections omitted" with "user chose skip" and the date; anything else under
   "Deviations from the type default". The page background and a hairline
   replace the section. While the answer is pending, the slot stays `planned`
   and the section follows the postponed-slot table in section 6 of
   `asset-sourcing-sequence.md`. Never a placeholder (AS9), never a colour
   band, never emoji, never an icon row, never a paragraph standing in for
   the picture.

The loop as a decision table, by job class:

| Job class | Needs image | Catalog | Library tag | Merchant-owned | Generation | Tell the user, then offer |
|---|---|---|---|---|---|---|
| identity-bound (identity, detail, scale, texture, in-use, variation, included-items, sequence, swatch, size-reference, label, packaging) | yes | first | `product-shot`, `lifestyle` | ads, brand site, supplier (licence) | never | upload a real photo, or skip; generation "needs a real photo" |
| people (founder-or-team, ugc, expert) | yes | no | `lifestyle`, `social-proof` | merchant photo with consent; UGC with ledger row | never (GN3, GN9) | upload with consent or rights, or text-only note or quote, or skip; generation not feasible |
| proof artefacts (press logo, badge, before-after pair) | yes | no | `logo` (svg), ledger asset id | issuer or outlet artwork | never (GN4, GN5) | supply the artwork with its URL or issuer, or skip; generation not feasible |
| context (room, surface, occasion) | yes | if a context shot exists | `lifestyle`, `banner` | brand site | `product_composite` over the real cut-out (ALLOW) | upload, or generate after credits, or skip |
| backdrop, texture, decoration | only in the bold moment or page grain | no | `hero`, `banner` | brand site | `hero_bg`, `section_bg`, `texture_fill`, `pattern_tile`, `decorative_element` (ALLOW after credits) | upload, or generate after credits, or plain page background |
| diagram, comparison-visual | yes | own product real | `product-shot` for own side | merchant drawing | authored inline SVG only; raster never | upload a drawing, or an authored inline SVG, or an HTML table |
| text-exempt (faq, legal, shipping-returns, disclaimer, policy trust-bar, signed founder note) | no | | | | | nothing to ask; copy with a hairline |

## 1a. Using the asset library well

`lexsis_asset_library.search` takes `query`, `kind` (`image`, `video`, `svg`),
`limit`, `cursor`, `theme_id` and a `mode`. Four facts change how the loop
uses it:

- **Tags are free-form, not an enum.** `mode: "tags"` matches the `query`
  against each asset's own `tags[]`, so `hero`, `banner`, `lifestyle`,
  `product-shot`, `logo` and `social-proof` are conventions worth trying
  first, not a closed list. A store may tag `flat-lay`, `swatch` or a campaign
  name; a zero-result tag query means that tag is unused, not that the library
  is empty. Fall through to `mode: "semantic"`.
- **`mode: "similar"` with `similar_to_asset_id` builds the set.** Once one
  asset for a section is chosen, ask for its neighbours to fill the remaining
  slots in the same section or gallery. This is the cheapest way to get one
  shoot instead of a pile of found images, and it beats running independent
  searches per slot. It takes only `similar_to_asset_id` and `limit`: `query`,
  `kind` and `theme_id` are ignored, and the call fails without a seed asset.
- **`mode: "ocr"` finds text inside images.** It searches text extracted from
  the image itself. Use it to catch baked-in headlines, prices and promo
  overlays before a candidate is viewed, and to find a specific label or
  packaging shot by the words printed on it. `filename`, `alt_text`, `tags`
  and `ocr` all resolve to the library's `search_field`; `limit` caps at 48.
- **Results carry the geometry.** Each result has `width`, `height`, `format`,
  `size_bytes`, `tags`, `usage_hint` and `preview_candidates[]` with a role
  (`thumbnail`, `card`, `gallery`, `poster`, `original`) and its own
  dimensions. Check the aspect and minimum resolution from `slot-spec.md`
  against these numbers before viewing, so a candidate that cannot fill the
  slot is dropped without spending a view.

`mode: "all"` and `mode: "alt_text"` exist for broad or metadata-only lookups.
None of these modes replaces the fit review below: geometry and tags decide
whether a candidate is worth opening, the image decides whether it is used.

## 1b. Inspect before you commit

Open every candidate with `lexsis_assets.view` (it returns the image itself
for a vision-capable model, plus `width`, `height`, `url` and the asset id) or,
where the host cannot render it, fetch the `url` and inspect the file. Then
answer these questions about **this asset in this section**, not about the
asset alone. A candidate that fails any line is rejected and the loop
continues at the next step; the plan row records what was wrong so the same
asset is not proposed again.

| Question | Reject when | Note in the plan |
|---|---|---|
| Subject: does it show what the job needs? | The job is `identity` and the shade or variant is wrong; the job is `scale` and nothing gives size; the job is `in-use` and no one is using it | the job it actually performs, if different |
| Framing: does it crop to the slot aspect without losing the subject? | The product sits where the slot crops, or the mobile portrait crop cuts it | the focal point or `object-position` to use |
| Typography fit: can the section's headline and body sit on it legibly? | Text would land on busy detail, or contrast fails 4.5:1 against the copy colour (A7) | which corner is quiet, or that the copy moves out of the image |
| Page consistency: does it belong beside the other images on this page? | Different lighting temperature, background, model styling or era from the neighbouring slots; a studio packshot dropped into a lifestyle run | the run it belongs to |
| Palette: do its colours sit inside the plan's palette? | It introduces a hue the Design direction does not name and cannot be desaturated or cropped into agreement | the treatment applied |
| Density: does it survive at the rendered size? | Fine detail disappears at the slot's mobile width, or the image is an upscale with visible artefacts | the size it works at |
| Cleanliness | Watermark, promo overlay, baked-in text, competitor branding, or a border | reject, no note |

Two operational notes. `lexsis_assets.view` warns when its rendered preview is
a near-uniform colour: that means the preview failed, not that the asset is
blank, so open the `url` before discarding it and never regenerate a
replacement on that signal alone. And when several slots in one section or
gallery are being filled, view the candidates together and judge the set, not
each file in isolation, so the page reads as one shoot rather than a pile of
found images.

The same review applies to a generated asset after
`lexsis_drafts.asset_generate` returns: view it, judge fit, and either accept
it, adjust the prompt once, or fall back to asking the merchant. A generated
image that does not fit is not used because it was paid for.

## 2. Section-type table

Every section id that normally carries media. Imagery is the picture the
shopper needs; Job is the primary job id; Tag is the first
`lexsis_asset_library.search` tag; Purpose is the generation purpose that is
feasible for the gap, or `none`, which the user hears as "needs a real photo";
If skipped is what the section becomes when the user, told what is missing and
offered upload or generation, chooses to skip; No-go is the specific failure
for that section. Chrome, buy-box sub-elements and opening text lines are
outside the loop (section 1, step 1). Detail per proof kind lives in
`references/proof/press-and-media-mentions.md` (logos),
`references/proof/ugc-rights-and-display.md` (customer media) and
`references/proof/proof-ledger.md` (everything else); per video slot in
`references/assets/video-rules.md`.

| Section id | Imagery it wants | Job | Catalog | Tag | Purpose | If skipped | No-go |
|---|---|---|---|---|---|---|---|
| `hero` | the type's hero treatment (section 5 of `image-jobs-by-page-type.md`): selected-variant packshot, product in hand or context matched to the ad, editorial lifestyle, real video poster | identity, in-use or context | yes; ad creative first on paid traffic | `hero`, then `banner` | `hero_bg` behind a real cut-out or HTML type, bold moment only | first catalog identity image as a packshot hero, "hero pending merchant media"; production-ready not approved until resolved | generated product; before/after; carousel; typographic where section 5 forbids it |
| `trust-bar` | policy facts as text; issuer badge artwork; optionally one product macro | detail; certification | detail yes | `product-shot`; `logo` (svg) for marks | none | facts alone with a hairline; badges without an issuer row leave | generated badges, seals or payment marks (GN5); "as seen in" |
| `press-marquee` | three to six monochrome outlet logos, each linked to the article in the ledger | press-logo-linked | no | `logo`, `kind: svg` | none | section leaves the page; a policy-facts `trust-bar` takes its place | generated or unlinked logos; wire releases; coverage older than 24 months |
| `stats` | verified numbers in HTML beside one real product or context image | detail or context (reuse) | reuse | `lifestyle` | none | the strongest number moves into the hero subhead or trust-bar | generated charts, lab or clinic imagery (GN4); numbers inside the image (GN6) |
| `certifications`, `awards` | issuer artwork with issuer text beside it | certification, award | no | `logo`, `kind: svg` | none | section leaves the page | generated or redrawn marks (GN5); "FDA approved" art |
| `problem`, `agitation` | the situation, without the product; real people only when not presented as customers | context | no | `lifestyle` | none | the copy folds into `hook` | generated person; stock "customer"; a product shot posing as the problem |
| `discovery`, `solution`, `mechanism` | the product entering the story; a mechanism diagram with numbers in HTML | identity, in-use, diagram | yes | `product-shot`, `lifestyle` | `product_composite` for `context`; diagram as authored inline SVG | folds into `how-it-works` | generated product; raster diagram; clinical props |
| `story`, `about`, `values`, `mission` | real place, process and the people who work there | context, founder-or-team, sequence | no | `lifestyle` | none | section leaves the page | stock or generated people; a generated "workshop" |
| `founder-note` | the named founder, in their real setting, with a signature | founder-or-team | no | `lifestyle` (semantic: founder name) | none | text-only note with name and signature | stock or generated founder (GN3) |
| `benefits`, `features` | one real image per item: a detail macro, an in-use frame, a context composite | detail, in-use, context | detail yes | `product-shot`, `lifestyle` | `product_composite` (`context` only) | fewer items, each with an image; the remainder become buy-box bullets | text-only cards (N8); icon tiles (N12); emoji bullets (N1) |
| `how-it-works`, `usage`, `routine` | three to five real step photos, or a click-to-play demo with a real poster | sequence | yes if the merchant shot steps | `lifestyle` (semantic: step, apply, pour) | none | one in-use or identity image beside numbered HTML steps; else `usage` text under the buy box | generated steps; icon tiles standing for steps; autoplay with sound |
| `ingredients`, `materials`, `sourcing`, `science` | real flat lay, legible label photo, material macro | ingredient-or-material, label-or-facts-panel, texture | label and macro yes | `product-shot` (semantic: flat lay) | none; stock raw material only as context, never as own sourcing | HTML INCI or spec table beside a catalog detail macro | generated food, ingredient or formula (GN11); lab coats |
| `specs` | HTML spec table beside one detail image or an inline SVG dimension diagram | detail, diagram | yes | `product-shot` | none (diagram authored) | table alone on the page background | dimensions baked into an image; a generated exploded view |
| `results-timeline` | a ledgered result pair, else a truthful context image of the situation | result-or-context | no | ledger asset id | none | text timeline beside the in-use image, or leaves | generated or composite results (GN4); results in the hero |
| `gallery`, `product-hero` | catalog media in job order: identity, in-use, detail, scale, variation, included-items; one video thumbnail at most | identity, detail, scale, variation, included-items | always | `product-shot` | none | ships with fewer images; deviation recorded | any generated or stock image (GP11); first position not the feed image (GN12); duplicates (AS7) |
| `size-guide` | HTML size table plus an on-model image with height and size worn in HTML | size-reference | yes if on-model exists | `lifestyle` (semantic: model wearing) | none | table only | size chart as an image alone; generated model |
| `product-grid`, `product-spotlight`, `list-item`, `cross-sell` | one identity image per card, same background and crop scale across the grid | identity | yes | `product-shot` | none | cards without an image leave | mixed aspects (SS10); generated product; unlabeled recommendation carousel |
| `lookbook`, `shop-the-look` | editorial lifestyle frames with every shoppable item visible | in-use, context | rarely | `lifestyle`, `banner` | none | `product-grid` instead | a composite presented as a real look; stock scene with other brands' products |
| `bundle-builder`, `quantity-breaks` | identity per component plus a real flat lay of the set | identity, included-items | per component yes; set from the merchant | `product-shot` | none | builder with component images only, no set image | generated set or added props (GN13); a composite as `included-items` |
| `offer`, `offer-bridge`, `pricing`, `savings-math` | the selected variant packshot; the gift or bundle contents when the offer includes them | identity, included-items | yes | `product-shot` | none | terms as text beside the buy box | offer text or price inside the image (GN6); a "% off" pill as imagery (N9) |
| `gift-options` | the real box, wrap and card that ship | gift-presentation | yes if photographed | `product-shot` (semantic: gift box) | none | gift-note toggle in the buy box | generated wrap or box (GN13); a box that does not ship |
| `reviews`, `testimonial-spotlight` | verbatim quotes; customer photos only with a ledger row; avatars real with consent or CSS initials | ugc | no | `social-proof` | none | text-only quotes with stored attribution | stock or generated faces (GN3, SS13); brand shots captioned as customer photos (GN9) |
| `ugc-grid`, `video-testimonials` | rights-cleared customer photos or 9:16 clips at native aspect, captioned and labelled as customer content | ugc | no | `social-proof` | none | no UGC section | brand lifestyle posing as UGC; generated people; content without a `P` row |
| `before-after` | a ledgered pair, same crop, interval in HTML | result-or-context | no | ledger asset id | none | section leaves the page | generated or composite pairs; any before/after in the hero (display rule 9) |
| `expert-endorsement`, `press-quotes`, `case-study` | the named person or outlet with written approval | founder-or-team (expert), press-quote-linked | no | `social-proof`, `logo` | none | quote with name, credential and link in HTML | stock or generated "doctor" (GN3); unlinked outlet |
| `comparison`, `us-vs-them`, `alternatives`, `verdict`, `winner` | own product real; the alternative as an inline SVG silhouette labelled "other brands" | comparison-visual | own side yes | `product-shot` | none | table with the own identity image only | competitor photo or generated competitor (GN8); a winner ribbon |
| `quiz`, `product-finder`, `calculator` | typographic entry is allowed on `quiz-funnel`; one identity image per recommended product on the results screen | identity (results) | yes | `product-shot` | none | recommendation cards without an image leave | a packshot before routing; generated result products |
| `video`, `shoppable-video` | a real product or demo video with a real-frame poster, click to play | sequence, ugc | catalog video yes | library video assets | none | no video; `imagery.video: required` types return blocked | generated video (VR13); auto-selected black poster; autoplay with sound |
| `email-capture`, `sms-capture`, `waitlist-form`, `referral-form`, `giveaway-entry` | the product or prize identity beside the form | identity | yes | `product-shot` | none | the form alone as the distinct object (N8) when the page sells nothing yet | a decorative generated image as the form's only visual; a prize render |
| `closing-cta`, `final-offer` | a second crop of the hero or identity image | identity, in-use (reuse) | reuse | `hero` | `hero_bg` only when this section is the bold moment | reuse the hero slot | a new colour band; a second full-bleed backdrop (N2) |
| `post-purchase-next-steps`, `related-reads` | the ordered item; real article covers | identity | yes | `product-shot` | none | text list | stock "unboxing"; generated covers |

## 3. PDP gallery budget

`N` is the count of distinct catalog images after viewing (two images that
differ only by crop count as one, AS7). Required PDP jobs are `identity`,
`detail`, `scale`, `in-use`, plus `variation` and `swatch` with variants,
`included-items` for sets, `size-reference` for worn goods,
`ingredient-or-material` and `label-or-facts-panel` for regulated
consumables; the vertical raises the gallery minimum (5 supplements and food,
6 beauty and jewellery, 7 electronics, 8 home, 8 to 12 fashion) and the page
total is that minimum plus two.

| N | Probably covered | Probably missing | Decision per gap |
|---|---|---|---|
| 1 | identity | detail, scale, in-use, variation, included-items, label | Tell the user detail, scale and in-use are missing; upload or skip (identity-bound: never generated). Offer one `product_composite` for `context` below the buy box after the packshot-hero confirm line. Ship a one-image gallery in `fast-draft` with the deviation recorded and the gaps listed; `production-ready` is not approved with `R` jobs `planned`. |
| 2 to 3 | identity plus detail or one variation | scale, in-use, texture, included-items | Tell the user scale (a hand or known object) and in-use are missing, in one paragraph; upload or skip. Texture only from a merchant macro. Offer one composite for `context` in `benefits`. Duplicate the identity image nowhere. |
| 4 to 5 | identity, detail, variation when variants exist, sometimes one in-use | scale, texture, included-items, label | View each and assign one job. Tell the user scale and, for sets, included-items are missing; upload or skip. Reuse the in-use frame as the hero alternate and in `benefits`; it is not a second gallery slot. |
| 6 to 9 | identity, detail, variation, in-use, often scale | texture, included-items, label, on-model | Fill from the library `product-shot` tag, then tell the user what is left; upload or skip. No generation touches the gallery; at most one composite below the buy box. |
| 10 or more | most jobs | duplicates and stale variant art | Dedupe, reorder by job, drop sold-out variant art. Show every thumbnail up to 10 to 14, then an explicit "+N" control (IJ7). Generation: none. |

Rules that hold at every N:

- Generation never replaces, re-renders, cleans up or recolours the product
  (GN1, GN2, GP2). A `product_composite` places the untouched real cut-out on
  a surface and fills `context` only, outside the gallery.
- The first gallery position is the real feed image (GN12).
- Ceiling: four generated assets per page (GP9); a PDP normally uses zero
  to two, all below the buy box, and each needs the packshot-hero confirm
  line because the PDP hero is `packshot`.
- A missing `scale` image is a planned slot on every physical product (IJ5);
  it is never generated (GP14). Tell the user; upload or skip.
- Beauty adds one on-skin image per shade; fashion adds on-model with height
  and size worn in HTML; these come from the merchant or do not exist
  (`imagery-by-vertical.md`).

## 4. Asking well

The user always hears what is missing. One message, sent once after steps 3
to 5 have run for every slot, never more than three questions in the turn,
never the phrase "custom images?" (AS8). Per missing slot the message states:
what is missing (the image job in plain words), for which section, the aspect
and count, why it matters, and the three answers: upload it, generate it
(feasible with purpose and credits, or not feasible and why), or skip the
section (with what the page does instead). A merchant who reads only this
text can answer with one word per slot.

```text
Missing assets: 3 of 9 slots.

A4, gallery, scale, 1:1, 1 image. Nothing shows the bottle against a hand or
a known object, and shoppers judge size from the gallery.
  Upload it (a photo of the bottle in a hand), or skip (the gallery ships
  with 4 images). Generate: not feasible, needs the real product.

A7, benefits, in-use, 4:5, 1 image. The third benefit has no picture.
  Upload it (the serum being applied), or skip (benefits keeps two items).
  Generate: feasible only as a scene with your real bottle composited in
  (product_lifestyle, 1 credit, carries an "AI-generated scene" caption,
  counts as context, not as a real in-use photo). Say "yes A7" for that.

A3, hero, backdrop, 16:9 plus 4:5, 1 image. The headline needs a quiet
surface behind the cut-out.
  Upload a surface photo, or generate hero_bg (2 credits, balance 40), or
  use library asset 5e2 (linen).
```

Feasibility wording comes from `generation-policy.md`: ALLOW purposes are
offered plainly with credits and balance; ASK purposes name the caption and
the conditions and require a yes for that slot; NEVER jobs are stated as
"needs a real photo" with the one-line reason (the product itself, a person
shown as a customer, results, logos, badges, text in images).

Batching: identity-bound gaps share one paragraph; anything that spends
credits is its own paragraph because it needs its own yes; a proof question
(reviews collection, press URL) is the third at most. When a fourth question
would be needed, the least valuable slot goes into the plan's missing-asset
list with the same three answers and is not asked this turn.

`fast-draft`: do not block on the answer. Make the reversible,
placeholder-free choice (reuse the closest existing asset that honestly does a
related job, or leave the slot `planned`), then list every missing asset in
the plan's Asset slots table and in the draft summary under "Missing assets"
with the same three answers, so the user can upload or approve generation
afterwards. Credits are still never spent without a yes.

`production-ready`: ask once; a plan with a `planned` hero or `R` job is not
approved until the user uploads, approves generation, or chooses to skip.

How a postponed slot is recorded: the plan row keeps `Status: planned` with a
Source decision beginning `pending:` and naming the job and the feasible
remedy ("pending: no in-use media; upload or skip; NEVER for generation");
the manifest entry has `"sourceType": "pending"` and `"status": "planned"`;
the draft shows a visible "asset needed" note, never a placeholder file or
stock stand-in (AS9); the return summary lists the slot under Missing assets.
Section 6 of `asset-sourcing-sequence.md` gives the per-situation table (hero
postponed, video postponed, icon set, logo, UGC rights).

## 5. Recording

Plan, `## Asset slots`: one row per slot with the fixed columns from
`skills/plan-page/SKILL.md`. Role/purpose carries the job in brackets
(`product_media (scale)`, `proof (ugc, ledger P5)`, `hero_bg`); Source decision
starts with the step name (`shopify media`, `library <id>`, `merchant-upload
(owner: merchant, <date>)`, `supplier (licence: <ref>)`, `stock (licence:
<id>)`, `generated (<purpose>, library: none)`, `pending: ...`) and carries
`viewed` for every identity-bound slot; Status is `verified` or `planned`.
Generated slots also get a row in `## Generation record` with the verbatim
prompt, negatives, brand hexes, provider, asset id, metadata value, visible
label and who approved (section 7 of `generation-policy.md`).

Manifest, `assets[]` (schema in `references/page-files.md`): one entry per
slot holding ids and status only. `sourceType` is `shopify` with `productId`
and `mediaId`, `lexsis` with `assetId` (merchant uploads, supplier files,
stock and generated assets all become `lexsis` after import), or `pending`.
A generated slot adds `"generated": true` and `"provider": "<provider>"` and
its `role` equals the purpose; an approved ASK slot has `role:
"product_lifestyle"` and `"askApproved": true`, with the merchant's words in
the plan record. Prompts, licences, consent references and reasoning never
enter the manifest. Full examples: section 4 of `asset-sourcing-sequence.md`.
The draft summary repeats every `planned` slot under "Missing assets" with
the same three answers (upload, generate where feasible, skip), so nothing
missing is visible only in the plan.

The `## Workflow` block of the type file is where the per-section decision is
written in prose (Media line: job and source; when missing, what the user
was offered: upload, generate, or skip) and the
Asset budget table sums it up; the plan's "Imagery and background plan" line
per section names the slot ids and the treatment (full-bleed, inset, grid,
background image with legibility overlay), with the single full-bleed being
the bold moment.

## 6. Copy discipline inside the loop

Copy is the caption to the image, not the filler for a missing one. Write it
after the slot is resolved, so the image count shapes the copy: three real
benefit images mean three benefits, not five with two text-only cards.

- Headline at most 10 words and two lines at 375px; subhead at most 20
  (`references/copy/headline-and-cta-rules.md` HC4).
- Body at most three lines at 375px per paragraph, about 45 words; sentences
  average 15 words (HC31). One idea per paragraph beside one image.
- Every benefit, step or feature line carries a number, a material, a time
  or a test (HC12); adjective-only lines are the text version of a colour
  band.
- No emoji anywhere outside the plan's "Emoji in copy" allowance (N1); no
  icon rows standing in for imagery (N3, N12); icons only as one inline SVG
  set beside a visible label.
- None of the blacklist in `references/anti-patterns/copy-anti-patterns.md`
  ("premium quality", "elevate", "seamless", "crafted with care" and the
  rest); a section that needs those words to feel full is a section that
  needs an image or needs to go.
- Alt text follows the slot template in `slot-spec.md`: under 125
  characters, never "image of", `alt=""` for backdrops and decoration.

## 7. Worked walk-throughs

### (a) PDP for a serum, five catalog images, no lifestyle shots

Context reads: `lexsis_catalog.get` returns five images, in order: bottle
front on white, back label, dropper macro with a drop, bottle beside its box,
bottle front at a second angle. Viewed: images 1 and 5 differ only by angle
and count as one identity image (AS7). Jobs covered: identity (1), label
(2), detail and texture (3), packaging (4). Beauty vertical, one shade, no
variants. `lexsis_asset_library.search` with `mode: tags`: `product-shot`
returns the same five, `lifestyle` and `hero` return nothing; semantic
"serum applied to skin" returns nothing. `lexsis_campaigns.creatives`: no
campaigns. Missing required jobs: scale, in-use; beauty adds texture on skin
and INCI as HTML.

Section by section:

- `gallery`: A1 identity, A2 detail and texture (the macro), A3 label, A4
  packaging. Four images against a beauty minimum of six: deviation recorded.
  Hero is A1 as `packshot`; nothing generated (GN1, GP11).
- `buy-box`: beside the gallery; INCI rendered as an HTML list from the label.
- `trust-bar`: returns window and shipping threshold from the offer ledger,
  text only, hairline.
- `benefits`: three items, each with a real image: the macro (A2) for
  texture, a tight crop of the label (A3) for the actives with percentages
  in HTML, and one `context` composite (A6, `product_composite`, square, the
  A1 cut-out on a bathroom shelf surface) for "where it lives in the
  routine". The composite needs the packshot-hero confirm line and credits.
  The fourth benefit the brief wanted (absorbs in 30 seconds) has no image
  and becomes a buy-box bullet.
- `how-it-works`: no step photos. Three numbered HTML steps sit beside the
  macro (A2 reused); no icon tiles.
- `ingredients`: HTML INCI table beside A3.
- `ugc-grid`: no rights-cleared media; the user is told, and the section is
  omitted only if they do not supply customer media with rights.
- `reviews`: quotes from `lexsis_catalog.reviews`, text only, CSS initials.
- `faq`, `legal`: text, exempt.

Asset budget: catalog supplies identity, detail, texture, label, packaging;
missing scale and in-use (planned A5, A7, `pending: upload or skip; NEVER for
generation`), context filled by one composite if approved. One message:

```text
Missing assets: 3 of 8 slots.
A5, gallery, scale, 1:1, 1 image. Nothing shows the bottle's size.
  Upload it (held in a hand), or skip (gallery ships with 4 images).
  Generate: not feasible, needs the real product.
A7, benefits, in-use, 4:5, 1 image. The third benefit has no picture.
  Upload it (the serum being applied), or skip (benefits keeps two items).
  Generate: not feasible as a real in-use photo.
A6, benefits, context, square, 1 image. The routine benefit has no setting.
  Upload a shelf or bathroom photo, or generate a composite of your real
  bottle on a generated surface (product_composite, 1 credit, balance 40,
  captioned "Product photo on a generated background"), or skip.
A8, ugc-grid, customer photos, 1:1, 4 to 8 images. No customer media with
  rights exists. Upload photos with the customer's permission, or skip the
  section. Generate: not feasible, customer content cannot be generated.
```

### (b) Ad landing page, three ad creatives, two lifestyle banners in the library

Context reads: `lexsis_campaigns.creatives` returns three Meta images; the
spending winner shows the product in a hand on a kitchen counter with a
headline baked into the frame. `lexsis_asset_library.search` `mode: tags`
`lifestyle` returns two 16:9 banners: one is the same kitchen scene without
text (viewed: same colourway, product legible), the other shows a model
pouring the product. `lexsis_catalog.get` returns identity, one detail, one
included-items flat lay. Traffic is product-aware Meta.

Section by section:

- `hero`: the clean library banner (A1) matches the ad frame; the creative
  itself is rejected for the page because of the baked-in text (AS11, GN6)
  and the merchant is asked for the layered original only if a future page
  needs it. Message-match line: yes. Mobile crop: the banner is viewed at
  4:5 and a focal point recorded; no separate portrait needed. No `hero_bg`.
- `trust-bar`: policy facts, text.
- `how-it-works`: the pouring banner (A2) does the `in-use` job beside three
  HTML steps; the model is brand-shot, not captioned as a customer.
- `benefits`: three items: catalog detail (A3), included-items flat lay (A4),
  and the hero banner cropped tight (A1 reused). No composite needed.
- `reviews`: API quotes, no media; `social-proof` tag returns nothing.
- `comparison`: own identity image (A5) against an inline SVG silhouette.
- `buy-box`: gallery of identity, detail, included-items; `scale` is missing
  and planned as A6.
- `closing-cta`: A1 second crop.

Six images on the page meets the type minimum. Generation: none. One
message: "A6, buy-box gallery, scale, 1:1, 1 image. Nothing shows the pack's
size. Upload a photo of the pack in a hand, or skip (the gallery ships with
three images). Generate: not feasible, needs the real product." In
`fast-draft` the draft is created with A6 `planned` and the same line in the
summary.

### (c) A trust section when the merchant has no press coverage

The brief asks for an "as seen in" strip. Proof ledger check: no
`press-logo-linked` rows; `lexsis_asset_library.search` `mode: tags` `logo`
`kind: svg` returns only the brand's own wordmark; the web check in
`references/proof/press-and-media-mentions.md` finds one wire release, which
is `dropped`. Generating logos is NEVER (GN5); rendering unlinked logos is
never (proof-ledger display rule 6).

The user is told before anything changes:

```text
Press marquee: no linked coverage found. The library holds only your own
logo, and the one release found is a wire release, which cannot be shown.
  Paste article URLs where an outlet covered the brand and I will add the
  outlet logos with links, or skip the marquee. Generate: not feasible,
  logos and badges cannot be generated.
  If skipped: a trust-bar with your returns window, shipping threshold and
  warranty takes its place.
```

If the user skips, the fallback order in `proof-ledger.md` gives a
`trust-bar` of policy facts: 30-day returns, free shipping over the
threshold, one-year warranty, each with its policy URL in the ledger. The
strip is text with a hairline above and below; where the wireframe gives it
an image, it takes one catalog detail macro (A3 reused), never a badge grid.
If none of the three facts is verified either, the user is told that too and
the hero subhead carries the one confirmed fact. The plan records
"press-marquee: omitted, no linked coverage, user chose skip" under
Deviations from the type default.
