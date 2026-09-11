# Asset sourcing sequence

The ordered algorithm `/plan-page` runs for every asset slot, the checks at
each step, how the result is recorded, the single asset question, and what
happens when the merchant postpones a slot. `/design-page` runs the same
sequence for slots the plan left `planned`. Tool mechanics (arguments,
picker behaviour, import flow) are in `references/asset-prep.md` and
`references/design-assets.md`; this file is the policy above them. Jobs come
from `references/assets/image-jobs-by-page-type.md`, technical thresholds from
`references/assets/slot-spec.md`, generation limits from
`references/assets/generation-policy.md`.

Tags: LAW, RESEARCH, OPERATOR, HEURISTIC as defined in
`image-jobs-by-page-type.md`.

## 1. The algorithm

Run per slot. Stop at the first step that yields an asset passing every
check in section 3. Record the step name in the plan's Source decision column.

```text
for slot in plan.asset_slots:
  if slot.status == verified and slot picked by the user: keep; next slot
  1. SHOPIFY PRODUCT MEDIA      lexsis_catalog.get (product and variant media)
  2. STORE ASSET LIBRARY        lexsis_asset_library.search (mode: tags, then semantic)
  3. MERCHANT-SUPPLIED MEDIA    lexsis_asset_import.import (URLs, base64, attachments) or lexsis_asset_upload.upload (local-file UI)
  4. SUPPLIER OR MANUFACTURER   lexsis_asset_import.import after a written licence check
  5. LICENSED STOCK             backdrop, context or raw-material roles only; import
  6. GENERATION                 references/assets/generation-policy.md (ALLOW auto after credit confirmation; ASK after merchant yes; NEVER blocked)
  else: slot stays planned; visible "asset needed" note in the draft; no placeholder
```

Steps 3 to 6 run only for the jobs their row in section 7 of
`image-jobs-by-page-type.md` allows. An identity-bound job (product, variant,
included items, label, packaging, founder, UGC, result) ends at step 4.

## 2. Step details

| Step | Call | What qualifies | Step-specific checks | Rights basis | Source decision string | Manifest `sourceType` |
|---|---|---|---|---|---|---|
| 1 Shopify media | `lexsis_catalog.get` with the product id; read `media` (images and video, up to 250 per product https://help.shopify.com/en/manual/products/product-media/add-media ) and variant-to-media mapping | The exact SKU and variant the slot needs | Variant image exists for every `variation` slot; first media item is the identity packshot; no stale sold-out variant art | Merchant's catalog; no record needed | `shopify media` | `shopify` with `productId` and `mediaId` |
| 2 Asset library | `lexsis_asset_library.search` with `theme_id` (required), `kind: image` or `svg` or `video`, `mode: "tags"` using `product-shot`, `hero`, `lifestyle`, `flat-lay`, `social-proof`, `logo`, `banner`, `before-after`; then a semantic `query` | Approved brand assets, prior imports, UGC with a rights record | Licence scope covers "website or landing page"; UGC has a proof-ledger row; consent for people depicted; not expired; purpose tag matches the job | Existing library record | `library <asset id>` | `lexsis` with `assetId` |
| 3 Merchant-supplied | `lexsis_asset_import.import` with exactly one source: `url`, image `data` + `mime_type`, or `attachments`; `lexsis_asset_upload.upload` exclusively opens the local-file UI, then wait for the user's uploaded-asset message | Files the merchant sends; originals from the merchant's own site, Instagram or TikTok accounts pulled with the merchant's authorisation for this store | Original file, not a screenshot; if the post shows a creator or customer, treat as UGC and require their permission; music or third-party IP cleared for video | Merchant states ownership; record "merchant owns, <date>" | `merchant-upload (owner: merchant, <date>)` | `lexsis` after import |
| 4 Supplier | `lexsis_asset_import.import` with tag `supplier` | Manufacturer or distributor imagery of the exact SKU | Written licence for retail marketing use; not a sibling model; watermark removal only if the licence permits; resolution per slot | Supplier licence; record reference | `supplier (licence: <ref>)` | `lexsis` after import |
| 5 Licensed stock | External search (Unsplash, Pexels or a paid library per `references/asset-prep.md`), then `lexsis_asset_import.import` with tag `stock` | Backdrops, occasion scenes without the product, raw ingredient or material flat lays, scenes with people who are clearly not presented as customers | Licence covers commercial web use and the store's territories; no editorial-only licence; model release when a face is visible; no recognisable brands, logos or signage | Stock licence id | `stock (licence: <id>)` | `lexsis` after import |
| 6 Generation | `lexsis_workspace.credits`, then `lexsis_drafts.asset_generate` | ALLOW purposes; ASK purposes with a logged merchant yes | Section 8 checklist in `generation-policy.md`; provenance recorded | Merchant's credit confirmation and, for ASK, written yes | `generated (<purpose>, library: none)` | `lexsis` with `generated: true`, `provider` |

Never scrape third-party posts, competitor sites or marketplaces for images.
Never hotlink; every external file is imported before use so it lives in the
brand library and survives the source going away.

Search-mode notes: tags are free-form, so a zero-result tag query means the
tag is unused rather than the library being empty; `mode: "semantic"` is the
fallback. After the first asset for a section is chosen, `mode: "similar"`
with `similar_to_asset_id` finds its neighbours so the section reads as one
shoot. `mode: "ocr"` locates baked-in text before a candidate is opened.
Result `width`, `height` and `preview_candidates[]` settle aspect and
resolution before viewing (`references/workflows/section-asset-workflow.md`
section 1a).

## 3. Universal checks at every step

Every candidate passes all of these before the slot becomes `verified`.
Thresholds by slot are in `references/assets/slot-spec.md`.

| Check | Threshold | How to run |
|---|---|---|
| Identity verified | The image shows the SKU, variant, shade or component the slot needs | Open it with `lexsis_assets.view` (asset id, or URL where the discovered schema allows). Never trust a filename, tag or alt text |
| Resolution | Short side at or above the slot's min px; hero 1920 wide or more (1600 absolute floor) | `width` and `height` from the import response or `lexsis_assets.view`; for local files `sips -g pixelWidth -g pixelHeight <file>` |
| Aspect fit | Crops to the slot aspect without cutting the product; mobile hero needs its own portrait crop or focal point | View at both crops; record `object-position` or focal point in the plan row |
| Colour profile | sRGB | `sips -g space <file>` prints `RGB`; CMYK or wide-gamut files are rejected or converted before import |
| No watermark, border, badge or promo overlay | None visible | View; Google disapproves such images https://support.google.com/merchants/answer/6101131 |
| No baked-in text | Only text printed on the physical product or label | View; WCAG 1.4.5 https://www.w3.org/WAI/tutorials/images/ ; Shopify Theme Store forbids embedded text in images https://shopify.dev/docs/storefronts/themes/store/requirements |
| No duplicate | No near-identical image already assigned in the same gallery or grid | View candidates side by side; two images that differ only by crop count as one |
| No stretched or clipped product | Uniform scale; whole product visible for `identity` | View |
| Rights recorded | Source decision string carries the basis (section 2) | Plan row is non-empty |
| Focal point | Set for every hero, lifestyle or cover-cropped asset | Plan row or `object-position` in source |
| Section fit | The asset does the section's job, crops to the slot without losing the subject, leaves a quiet area where the copy sits, and matches the lighting and styling of the neighbouring slots | The fit review in section 1b of `references/workflows/section-asset-workflow.md`, run on the viewed image |
| Set coherence | Slots in the same section or gallery read as one shoot | View the candidates together, not one at a time |

## 4. Recording the result

Plan (`page-plan.md`, "## Asset slots"). Columns are fixed by
`skills/plan-page/SKILL.md`; put the job and the rights basis inside
Role/purpose and Source decision:

```markdown
| Slot | Section | Role/purpose | Aspect | Source decision | Id / URL | Status |
|---|---|---|---|---|---|---|
| A1 | gallery | product_media (identity) | 1:1 | shopify media, viewed | gid://shopify/MediaImage/123 | verified |
| A2 | gallery | product_media (scale) | 4:5 | merchant-upload (owner: merchant, 2026-09-10), viewed | asset 8c1f... | verified |
| A3 | hero | hero_bg | 16:9 + 4:5 | generated (hero_bg, library: none), credits confirmed | asset 2d9a... | verified |
| A4 | ugc-grid | proof (ugc, ledger P5) | 1:1 | library, rights record P5 | asset 71bb... | verified |
| A5 | benefits | product_media (in-use) | 3:2 | pending: no in-use media; NEVER for generation | | planned |
```

Manifest (`page-manifest.json`, `assets[]`, schema in
`skills/plan-page/references/page-files.md`). One entry per slot; the manifest
holds ids and status only, never prompts, licences or reasoning:

```json
{ "slotId": "A1", "role": "product_media", "sectionId": "gallery", "sourceType": "shopify", "productId": "gid://shopify/Product/1", "mediaId": "gid://shopify/MediaImage/123", "url": "https://cdn.shopify.com/...", "status": "verified" }
{ "slotId": "A3", "role": "hero_bg", "sectionId": "hero", "sourceType": "lexsis", "assetId": "2d9a...", "url": "https://cdn.trylexsis.com/...", "status": "verified", "generated": true, "provider": "lexsis" }
{ "slotId": "A5", "role": "product_lifestyle", "sectionId": "benefits", "sourceType": "pending", "status": "planned" }
```

Merchant uploads, supplier files and stock all become `sourceType: lexsis`
after import; the origin step survives only in the plan's Source decision.
Licence ids, consent references and prompts live in the plan, never in the
manifest.

## 5. The single asset question

Ask once, after steps 1 and 2 have run for every slot, and only when a slot
remains unresolved or generation would spend credits. Group with any other
open questions; never more than three questions in one turn
(`references/consumer-behavior-cro.md`). Name the slot ids, jobs, count,
aspects, placements and credit cost. Never ask "Do you want custom images?".

```text
Asset slots: 6 of 9 resolved from the catalog and library.
Unresolved: A4 (scale, gallery), A7 (in-use, benefits), A3 (hero backdrop).
Options:
  1. You pick: choose from the library or upload files for A4 and A7.
  2. I pick: I use the best existing match for A3 (library asset 5e2...); A4 and A7 have no match.
  3. Generate the gaps: A3 only, hero_bg, landscape + portrait, 2 credits (balance 40).
     A4 and A7 need the real product in use and cannot be generated; they stay planned unless you upload.
```

Answer handling:

| Answer | Action | Status after |
|---|---|---|
| User picks | Call `lexsis_asset_library.search` with `query: ""` per slot group; wait for the `Design asset selection:` message; map `assets[]` to slot ids in `selection_order`; local files not in the library use `lexsis_asset_upload.upload`, then wait for the user's uploaded-asset message; supplied URLs or attachments use `lexsis_asset_import.import` | `verified` after viewing |
| I pick | Use the best match per slot from steps 1 and 2; view identity-sensitive picks | `verified`, or `planned` where nothing matched |
| Generate the gaps | Check `lexsis_workspace.credits`; run section 8 of `generation-policy.md` per slot; generate ALLOW purposes; ASK purposes only with the merchant's explicit yes in the same reply | `verified` with `generated: true` |
| No answer, fast-draft | Proceed with "I pick"; leave the rest `planned`; state it in the summary | mixed |
| No answer, production-ready | Plan is not approved while any hero or `R` job slot is `planned` | `planned` |

If the host has no inline UI, ask for a URL or conversation attachment and
import it with `lexsis_asset_import.import`. Never call import with no source
to open a panel; never treat opening the upload UI as a completed upload.
Keep every import and upload scoped to the selected workspace and theme.

## 6. User postponed the slot

| Slot situation | fast-draft | production-ready | Never |
|---|---|---|---|
| Identity-bound job (identity, variation, included-items, swatch, label, packaging, founder, ugc, result) | Stays `planned`; `/design-page` builds the section without it or removes the section with a note; the return summary lists it under Unresolved assets | Same; `PLAN_APPROVED` may be given only with the merchant's acknowledgement that the section ships without the image | A placeholder, a stock stand-in, a generated stand-in, or a product from another merchant |
| Backdrop or context job (hero_bg, section_bg, context via composite) | `/design-page` resolves from library or Shopify; asks before paid generation | `/design-page` asks once: generate or pick existing | Generation without a credit confirmation |
| Hero image postponed | Use the first Shopify identity image as a `packshot` hero; record "hero pending merchant media" in the plan | Plan not approved until resolved | Typographic hero as a workaround where section 5 of `image-jobs-by-page-type.md` forbids it |
| Video slot postponed | Build without video; drop the poster slot; `imagery.video: optional` types lose nothing | Same, unless `imagery.video: required` (`video-sales-page`, `ugc-creator-collab`): return blocked with the reason | A generated video of the product or of people |
| Icon set postponed | Text labels only; no icons (allowed by N3 in `references/design-rules.md`) | Same | Emoji or raster icons |
| Logo missing | Accessible text wordmark | Same | Product image or generic logo placeholder |
| UGC rights pending | No UGC section; proof ledger row stays `pending` | Same | Rendering pending UGC |

## 7. Rules

`$W` is the page workspace.

AS1. Run the six steps in order for every slot and stop at the first passing asset. OPERATOR.
Rationale: existing media wins (`references/consumer-behavior-cro.md`); each later step adds cost or rights risk.
Check: every slot row's Source decision begins with one of `shopify media`, `library`, `merchant-upload`, `supplier`, `stock`, `generated`, `pending`.

AS2. Search Shopify media and the library before any generation call. OPERATOR.
Rationale: generation is the last step and spends credits; duplicates of existing brand media are waste.
Check: every `generated` Source decision carries `library: none`; no `lexsis_drafts.asset_generate` call precedes the slot's `lexsis_asset_library.search` in the session.

AS3. Verify identity by viewing the asset, never by filename, tag or alt text. OPERATOR.
Rationale: `references/asset-prep.md`: asset names alone do not establish identity; a wrong shade or sibling model on the page is a misrepresentation.
Check: every `verified` slot for an identity-bound job carries `viewed` in its Source decision.

AS4. Never source the product, customers, founders, staff, before/after pairs or press from stock. LAW, RESEARCH.
Rationale: fake testimonials and endorsements are banned under 16 CFR 465 https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers ; stock people are ignored and read as filler https://www.nngroup.com/articles/photos-as-web-content/ .
Check: `grep -E '^\| A[0-9]+ .*(product_media|proof).*\| stock' $W/page-plan.md | wc -l` prints 0.

AS5. Import every external file before use; no hotlinks, no local files, no placeholders. OPERATOR.
Rationale: assets must survive the source disappearing and be reusable from the library (`references/asset-prep.md`).
Check: `grep -oE '(src|poster)="https?://[^"]+"' $W/lexsis-source.html | grep -vE 'cdn\.trylexsis\.com|cdn\.shopify\.com' | wc -l` prints 0 after adding the store's configured CDN host to the pattern.

AS6. Record the rights basis for every slot in the Source decision. LAW.
Rationale: UGC needs recorded, scoped permission; a tag or hashtag is not a licence https://later.com/blog/user-generated-content-rules/ ; stock needs a commercial licence for the territories.
Check: no slot row has an empty Source decision; every `proof (ugc...)` row cites a proof-ledger id (`P[0-9]+`).

AS7. Reject near-duplicates within one gallery or grid. RESEARCH.
Rationale: every gallery position must add information; truncated or repeated images waste the positions shoppers do see https://baymard.com/blog/truncating-product-gallery-thumbnails .
Check: view all slots of one section together; near-identical pairs count is 0 (yes/no in `qa-report.md`).

AS8. Ask the asset question once, naming slot ids, jobs, count, aspects, placements and credits; group at most three questions per turn. OPERATOR.
Rationale: `references/consumer-behavior-cro.md` merchant-question rules.
Check: the question text contains at least one slot id and job; the phrase "custom images?" does not appear.

AS9. Follow the postponed-slot table; never ship a placeholder. OPERATOR.
Rationale: `/design-page` forbids local or temporary placeholder assets.
Check: `grep -ciE 'placeholder|placehold\.(it|co)|via\.placeholder|picsum\.photos|unsplash\.com/random|lorem' $W/lexsis-source.html` prints 0.

AS10. Accept an asset only after the slot-spec resolution and aspect checks; art-direct the mobile hero instead of scaling the desktop crop. RESEARCH.
Rationale: scaled-down landscape heroes shrink the product and push the CTA below the fold https://www.nngroup.com/articles/big-pictures-small-screens/ ; https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images .
Check: import response `width`/`height` meets `slot-spec.md`; the hero `<picture>` has a `<source media="(max-width: 767px)">` whose dimensions are portrait.

AS11. Reject any candidate with a watermark, supplier logo, price sticker, border or baked-in copy. LAW.
Rationale: Google disapproves promotional overlays https://support.google.com/merchants/answer/6101131 ; WCAG 1.4.5 images of text https://www.w3.org/WAI/tutorials/images/ .
Check: view each candidate; on-pack text only (yes/no).

AS12. Check `lexsis_workspace.credits` and obtain the merchant's confirmation before any paid call. OPERATOR.
Rationale: `/design-page` authorises one page-creation credit, not asset generation.
Check: the session shows `lexsis_workspace.credits` before the first `lexsis_drafts.asset_generate`, and the merchant's reply contains a yes to the named batch.

AS13. Treat brand-owned social posts that show a creator or customer as UGC, not as brand lifestyle. LAW.
Rationale: copyright sits with the creator; consent of people depicted is separate https://thesocialmedialawfirm.com/blog/social-media-compliance/ugc-legal-risks-and-compliance-a-2026-guide/ .
Check: any `merchant-upload` slot whose alt names a person or handle also cites a ledger `P` id.

## Sources

- Shopify media limits https://help.shopify.com/en/manual/products/product-media/add-media ; media types https://help.shopify.com/en/manual/products/product-media/product-media-types
- Google Merchant image requirements https://support.google.com/merchants/answer/6324350 ; promotional overlay https://support.google.com/merchants/answer/6101131 ; product data spec https://support.google.com/merchants/answer/7052112
- Shopify Theme Store requirements https://shopify.dev/docs/storefronts/themes/store/requirements
- W3C images tutorial https://www.w3.org/WAI/tutorials/images/ ; alt decision tree https://www.w3.org/WAI/tutorials/images/decision-tree/
- MDN responsive images https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images
- NN/g photos as web content https://www.nngroup.com/articles/photos-as-web-content/ ; big pictures small screens https://www.nngroup.com/articles/big-pictures-small-screens/
- Baymard truncated thumbnails https://baymard.com/blog/truncating-product-gallery-thumbnails
- FTC consumer reviews rule Q&A https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers
- UGC rights: Later https://later.com/blog/user-generated-content-rules/ ; Social Media Law Firm https://thesocialmedialawfirm.com/blog/social-media-compliance/ugc-legal-risks-and-compliance-a-2026-guide/
- Amazon image resolution guidance https://sellercentral.amazon.com/help/hub/reference/external/G1881
