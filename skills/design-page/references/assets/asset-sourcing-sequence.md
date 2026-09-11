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

## 3. Acceptance

`references/workflows/section-asset-workflow.md` section 2 owns visual fit
and set review. `references/assets/slot-spec.md` owns dimensions, crop,
focal point and color-profile requirements. Check source rights through
section 2 of this file before accepting a slot. The original research
sources remain under Rules and Sources below.

## 4. Recording the result

Plan (`page plan`, "## Asset slots"). Columns are fixed by
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

Manifest (`page record`, `assets[]`, schema in
`skills/plan-page/references/page-files.md`). One entry per slot; the page record
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

## 5. Acquisition and unresolved slots

Execute `references/workflows/section-asset-workflow.md` sections 1 and 2.
That owner defines the grouped merchant question, UI/import split, missing
slot handling and view-and-fit review. This file defines source eligibility,
not a second fallback procedure or draft/production state table.

## 7. Rules

Checks use persisted MCP source and the hosted draft.

AS1. Execute the acquisition procedure in `references/workflows/section-asset-workflow.md` section 1; use this file to decide source eligibility. OPERATOR.

AS2. Search Shopify media and the library before any generation call. OPERATOR.
Rationale: generation is the last step and spends credits; duplicates of existing brand media are waste.
Check: every `generated` Source decision carries `library: none`; no `lexsis_drafts.asset_generate` call precedes the slot's `lexsis_asset_library.search` in the session.

AS3. Verify identity through the shared fit procedure in `references/workflows/section-asset-workflow.md` section 2. OPERATOR.

AS4. Never source the product, customers, founders, staff, before/after pairs or press from stock. LAW, RESEARCH.
Rationale: fake testimonials and endorsements are banned under 16 CFR 465 https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers ; stock people are ignored and read as filler https://www.nngroup.com/articles/photos-as-web-content/ .

AS5. Import every external file before use; no hotlinks, no local files, no placeholders. OPERATOR.
Rationale: assets must survive the source disappearing and be reusable from the library (`references/asset-prep.md`).

AS6. Record the rights basis for every slot in the Source decision. LAW.
Rationale: UGC needs recorded, scoped permission; a tag or hashtag is not a licence https://later.com/blog/user-generated-content-rules/ ; stock needs a commercial licence for the territories.
Check: no slot row has an empty Source decision; every `proof (ugc...)` row cites a proof-ledger id (`P[0-9]+`).

AS7. Reject near-duplicates within one gallery or grid. RESEARCH.
Rationale: every gallery position must add information; truncated or repeated images waste the positions shoppers do see https://baymard.com/blog/truncating-product-gallery-thumbnails .
Check: view all slots of one section together; near-identical pairs count is 0 (yes/no in `QA record`).

AS8. Use the grouped unresolved-slot handling in `references/workflows/section-asset-workflow.md` section 1. OPERATOR.

AS9. Follow the shared asset workflow for postponed slots; never ship a placeholder. OPERATOR.
Rationale: `/design-page` forbids local or temporary placeholder assets.

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
