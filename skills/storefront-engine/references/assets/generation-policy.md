# Generation policy

The ALLOW / ASK / NEVER model for AI-generated imagery on storefront pages.
It governs `lexsis_drafts.asset_generate` and any external generator
(image or video) reached through another MCP. `/plan-page` may plan a slot for
generation only from the ALLOW list; `/design-page` generates ALLOW slots after
credit confirmation and ASK slots only with the merchant's explicit yes; NEVER
items are not generated under any instruction. The only way to fill a NEVER
slot is for the merchant to supply real media through
`references/assets/asset-sourcing-sequence.md`. Prompt mechanics and
compositing recipes are in `references/design-enrichment.md`; where that file
suggests a prompt this policy forbids (gradient washes, hands holding the
product, generic lifestyle scenes), this policy wins.

Tags: LAW, RESEARCH, OPERATOR, HEURISTIC as defined in
`references/assets/image-jobs-by-page-type.md`.

## 1. What the MCP accepts

| `purpose` | `aspect` options | Output px | Transparent | Class |
|---|---|---|---|---|
| `hero_bg` | `landscape` | 1536 x 1024 | no | ALLOW |
| `hero_bg` | `portrait` (mobile crop) | 1024 x 1536 | no | ALLOW |
| `section_bg` | `landscape` | 1536 x 1024 | no | ALLOW |
| `card_bg` | `square` | 1024 x 1024 | no | ALLOW |
| `texture_fill` | `square`, seamless | 1024 x 1024 | no | ALLOW |
| `pattern_tile` | `square`, seamless | 1024 x 1024 | no | ALLOW |
| `decorative_element` | `square` | 1024 x 1024 | yes, separate provider | ALLOW |
| `product_composite` | `square` or `portrait` | 1024 x 1024 or 1024 x 1536 | no | ALLOW only over a real cut-out passed in `reference_images` |
| `product_lifestyle` | `portrait`, `square`, `landscape` | as above | no | ASK |

`icon_set` is a plan role, not an MCP purpose. It means "author one
monochrome inline SVG set" (one stroke width, 24px grid, `currentColor`),
allowed by N1 and N3 in `references/design-rules.md`. Raster icon generation is
NEVER. Every generated raster is at most 1536 px on its long side; that is
below the hero image minimum in `references/assets/slot-spec.md`, which is why
generation fills backdrops (low detail, cover-cropped) and never product
imagery.

## 2. NEVER

Blocking. No override by prompt, brief, design.md line or user instruction.
The merchant supplying real media is the only exit.

| Id | Never generate | Why | Instead |
|---|---|---|---|
| GN1 | The product itself when Shopify media exists or could exist, including a "cleaner" version of an existing shot | Misrepresentation of colour, size, texture or accessories; feed images must show the real product https://support.google.com/merchants/answer/7052112 ; ASCI draft prohibits exaggerating product features through visual representation https://www.ascionline.in/wp-content/uploads/2026/05/asci-ai-labelling-guidelines.pdf | Step 1 to 4 of the sourcing sequence; slot stays `planned` |
| GN2 | A different-looking or stand-in product when no media exists (pre-launch included) | Same as GN1; ASCI medium tier requires labelling of non-existent products and the shopper cannot tell a render from a photo | Merchant's own render captioned "Rendering; final packaging may vary", or typographic hero |
| GN3 | People presented as customers, reviewers, creators, founders, staff, experts or doctors | Testimonials by someone who does not exist are banned, 16 CFR 465 https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials ; ASCI "fabricating endorsements" and "AI generated fake doctor" are prohibited even if labelled | Real UGC with rights; real founder photo; no section |
| GN4 | Before/after, results, clinical or medical imagery (labs, charts implying efficacy, skin, hair or body change) | Before/after is an objective claim needing substantiation https://www.asa.org.uk/advice-online/before-and-after-photos.html ; "results not typical" does not cure deception https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance | `references/proof/before-after-and-claims.md` |
| GN5 | Press logos, certification badges, awards, seals, payment marks | Endorsement and certification fraud; `references/proof/trust-badges-certifications.md` requires issuer artwork | Issuer or outlet artwork with a ledger row |
| GN6 | Text, prices, labels, headlines, ingredient lists or facts panels inside an image | WCAG 1.4.5 https://www.w3.org/WAI/tutorials/images/ ; Google and Shopify overlay rules https://support.google.com/merchants/answer/6101131 , https://shopify.dev/docs/storefronts/themes/store/requirements | HTML text over the image |
| GN7 | Celebrities, lookalikes or any recognisable real person | Right of publicity; FTC celebrity avatar guidance https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers ; ASCI "likeness without consent" | None |
| GN8 | Competitor products or packaging, or generic products styled to resemble one | Trademark and comparative advertising exposure | Inline SVG silhouette labelled "other brands" |
| GN9 | Anything that will be captioned as a review, UGC, "from our customers" or a customer photo | 16 CFR 465 insiders and fake-review rules | Rights-cleared UGC only |
| GN10 | Unsafe use (baby, pets, tools, dosing) | ASCI prohibited tier "depicts unsafe situations" regardless of label | Real, correct-use photography |
| GN11 | Food, ingredients or formula presented as the merchant's own product or sourcing | GN1 by extension; net-impression deception | Real flat lays; stock raw material only as context |
| GN12 | Anything for the Google Shopping feed image slot or the first gallery position | Feed image must be a real, unobstructed photo https://support.google.com/merchants/answer/7052112 | Shopify media |

## 3. ALLOW

Generated after the merchant confirms the credit spend for the named batch.
Every ALLOW file: no people, no hands, no text, no products, no logos; brand
palette hexes from `lexsis_brand.brand_kit` passed in `brand_colors`;
provenance recorded per section 7.

| Purpose | Aspect | Prompt constraints | Negative list | Placement rule | Alt | Manifest role |
|---|---|---|---|---|---|---|
| `hero_bg` | `landscape` plus `portrait` for the mobile crop | Physical material or place (linen, paper, plaster wall, stone, wood, water, sky); soft depth; matte; a low-detail quiet zone where the HTML headline and CTA sit; luminance variance under 30% in that zone | text, letters, watermark, logo, person, hands, face, product, bottle, package, gradient wash, blob, bokeh, neon glow, 3D render | Only in the hero and only when the hero is the plan's bold moment (N2 full-bleed exception) or the section is typographic; a real cut-out is composited on top or no product is shown; one black-to-transparent legibility overlay at most (N7) | `alt=""`, `aria-hidden="true"` | `hero_bg` |
| `section_bg` | `landscape` | As `hero_bg`; even lower detail | As above | Only in the one full-bleed section the plan names as the bold moment (N2); never behind body copy blocks | `alt=""` | `section_bg` |
| `card_bg` | `square` | Flat material or tone; no objects | As above | Only inside a card that wraps a distinct object per N8 (product, proof artefact, table, form); never behind plain text | `alt=""` | `card_bg` |
| `texture_fill` | `square`, seamless | Abstract material grain (paper, linen, stone); tileable; no recognisable objects | As above plus "pattern of objects" | Page-wide behind the single `--lx-bg-color` at 8% opacity or less, or inside a media object; never per section (N2) | `alt=""` (inline `style` background on a `div`) | `texture_fill` |
| `pattern_tile` | `square`, seamless | Brand motif in one or two palette colours; geometric or botanical line work; tileable | As above | Same as `texture_fill`; never animated (N10) | `alt=""` | `pattern_tile` |
| `decorative_element` | `square`, `transparent: true` | Vector-like silhouette or brush mark in one palette colour; SVG preferred over PNG | As above plus "gradient", "glow", "3D" | At most two per page; never behind text; never floating, pulsing or parallax (N7, N10) | `alt=""`, `aria-hidden="true"` | `decorative_element` |
| `product_composite` | `square` or `portrait` | `reference_images` holds the real Shopify or library cut-out first, then a surface or scene; prompt places the product on the surface with realistic contact shadow; product pixels are not repainted, recoloured, relit beyond global grade or scaled non-uniformly; nothing added that could read as shipped with the product | text, hands, person, second product, brand signage, gift wrap, accessories | Fills `context` jobs only; never `identity`, `variation`, `included-items`, `gift-presentation` or gallery position one; caption "Product photo on a generated background" when the scene is photoreal (a room, a landscape) rather than a plain surface | Informative: "{Product} {variant} on {surface}" | `product_composite` |
| `icon_set` (authored SVG) | 24px grid | One stroke width, `stroke="currentColor"`, `fill="none"`, one size per context | Multi-colour, 3D, raster | Beside a visible text label, `aria-hidden="true"` (N3, A5) | n/a | `icon_set` |

Quality tier: `high` only for `hero_bg`; `medium` for `section_bg`,
`card_bg`, `product_composite`; `low` for `texture_fill`, `pattern_tile`,
`decorative_element` (`references/design-enrichment.md` cost table). House
cap: four generated assets per page (HEURISTIC).

## 4. ASK

Requires the merchant's explicit yes for the named slot in the same reply,
logged in the plan's Generation record with the merchant's words and date.
Never inferred from "go ahead" on the plan as a whole.

| Case | Question to put to the merchant | Conditions if approved |
|---|---|---|
| `product_lifestyle`: a scene around the real product where identity is preserved through a composited cut-out, or the merchant accepts illustrative context | "Slot A7 (in-use, benefits) would be a generated scene with your real product composited in. It will carry an 'AI-generated scene' caption and metadata, cannot be captioned as a customer photo, and Meta will label it if reused in ads. Generate it, or leave the section without an image?" | Visible caption near the image; `alt` names the product and says "generated scene"; never in `ugc-grid`, `reviews`, `testimonial-spotlight` or gallery position one; no people or hands; not for beauty shade or fit claims |
| Generated person or hands with the composited product (a synthetic model) | "This uses a synthetic model. It will be labelled 'AI-generated' and can never be presented as a customer, reviewer or staff. Proceed?" | Label visibly; ASCI medium tier "synthetic influencer" label; EU Art. 50 deep-fake label; never on `pdp` gallery, `ugc-creator-collab`, `brand-story-founder`; skin tone and body claims forbidden |
| Illustration or 3D-render style for the whole page | "The page would use an illustrated look for backdrops and decoration. Product images stay photographic. Accept the style?" | Products remain real photos; `alt` says "illustration"; style recorded in the Design direction block |
| Any generation on a page type whose checklist sets `imagery.hero` to `packshot` or `ugc-screenshot` | "This page type leads with a real product or customer image. Generated backdrops would sit below the hero only. Confirm?" | Hero stays real; generated assets only below the fold |
| Replacing a real but low-quality merchant photo with a composite | Show both; "Keep your photo or use the composite with your product cut out onto a generated surface?" | Original stays in the library; composite follows `product_composite` rules |
| Any batch beyond the four-asset cap or the plan's credit allowance | "This adds N generated assets at M credits (balance B). Proceed?" | Recorded count and cost |

RESEARCH context: when users did not know an image was generated there was no
trust penalty versus stock, but users who suspected generation reacted
negatively (n=77) https://www.nngroup.com/articles/ai-generated-images/ ;
marketers rank AI visuals far below UGC for trust (16% vs 33%)
https://www.nosto.com/blog/new-research-brands-prefer-ugc-for-diversity/ .
Default to real; spend generation on backdrops.

## 5. Prompt constraints for every call

1. Describe a material or place, never a mood word alone ("linen", not
   "premium vibe").
2. Add the negative list from the purpose row verbatim; always include
   "text, letters, logo, watermark, person, hands, face, product".
3. Pass `brand_colors` from `lexsis_brand.brand_kit`; never a default hex
   (N14).
4. Name the quiet zone position (left third, lower half) when HTML text will
   sit on the image.
5. Ask for even, diffuse light and low contrast; the legibility overlay does
   the rest (N7).
6. `style: photography` for backdrops unless the ASK illustration case is
   approved; never `3d_render` for anything near a product.
7. Store the exact prompt, negatives, aspect, style, quality, provider and
   returned asset id in the plan's Generation record.

## 6. Disclosure by jurisdiction

Applies to every generated or composited image on the page. "Metadata" means
`IPTC DigitalSourceType` = `TrainedAlgorithmicMedia` (fully generated) or
`CompositeSynthetic` (real product on generated scene), kept on the original
in the library. Hosts may re-encode and strip metadata, so the library record
and the plan carry provenance as well.

| Jurisdiction or platform | Obligation | What the page does | Tag | Source |
|---|---|---|---|---|
| EU, AI Act Art. 50 (applies 2026-08-02; marking grace to 2026-12-02 for earlier models) | Deployers label deep fakes (AI content resembling real persons, objects, places or events that would appear authentic) clearly at first exposure | ASK-tier realistic scene or human: visible label "AI-generated image" adjacent plus metadata. ALLOW backdrops without people or products: metadata only | LAW | https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems ; https://www.orrick.com/en/insights/2026/08/eu-ai-act-transparency-obligations-for-ai-generated-content-article-50 |
| India, ASCI draft AI labelling guidelines (May 2026), aligned to IT Rules amendment of 2026-02-10 | High tier prohibited even if labelled (fake testimonials, exaggerated results, fake settings, likeness without consent, fake authority); Medium tier label required (synthetic influencers, realistic AI settings, non-existent products); Low tier no label (decorative backgrounds, minor enhancement) | High tier blocked by section 2; Medium tier gets "Created using AI" label; ALLOW backdrops need none | LAW (draft) | https://www.ascionline.in/wp-content/uploads/2026/05/asci-ai-labelling-guidelines.pdf ; https://www.thehindubusinessline.com/info-tech/asci-proposes-risk-based-approach-for-responsible-labelling-on-ads-made-with-ai/article70969237.ece |
| US, FTC 16 CFR 465 and Section 5 | No federal AI label law; deception judged on the net impression including images; fake or AI testimonials banned; NY GBL 396-b requires disclosure of synthetic performers in ads from 2026-06-09 (secondary source, verify) | Section 2 blocks the deceptive cases; synthetic humans labelled anyway | LAW | https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-465-trade-regulation-rule-use-consumer-reviews-testimonials-final-rule ; https://craftshift.com/disclose-ai-generated-product-images-shopify-2026/ |
| UK, ASA/CAP | Visual claims must not exaggerate; before/after follows testimonial evidence rules; retouching of product-relevant areas misleads even with a disclaimer | GN4, GN6 | LAW | https://www.asa.org.uk/advice-online/cosmetics-the-use-of-production-techniques.html |
| Meta ads | Auto-applies an "AI info" label to images created or significantly edited with generative AI; photorealistic AI humans labelled next to "Sponsored" | Expect labels when page assets are reused as ads; keep metadata intact | LAW (platform) | https://www.facebook.com/business/help/1010479435004531 ; https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/ |
| Google Merchant Center | All generated images carry `IPTC DigitalSourceType`; do not strip it; no visible watermark or overlay; feed image is a real photo | Feed image never generated (GN12); metadata preserved on any other image | LAW (platform) | https://support.google.com/merchants/answer/7052112 |
| Shopify | No merchant-facing disclosure rule; Shopify Magic watermarks its own output invisibly; CDN re-encoding may strip IPTC (secondary claim) | Provenance kept in the library record and plan, not only in the file | OPERATOR | https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic/media-generation |

## 7. Recording

Plan (`page plan`), one block after "## Asset slots":

```markdown
## Generation record

| Slot | Purpose | Aspect | Style / quality | Prompt (verbatim) | Negatives | Brand hexes | Provider | Asset id | Metadata set | Visible label | Approved by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A3 | hero_bg | landscape + portrait | photography / high | "Unbleached linen surface, soft north window light, ..." | text, letters, logo, ... | #F5F0E6, #1F1D24 | lexsis | 2d9a... | TrainedAlgorithmicMedia | none | credits: merchant, 2026-09-10 |
| A7 | product_lifestyle | portrait | photography / medium | "..." | ... | ... | lexsis | 9f01... | CompositeSynthetic | "AI-generated scene" | "yes, generate A7" Aditi 2026-09-10 |
```

Manifest (`page record`): the slot's `assets[]` entry gets
`"sourceType": "lexsis"`, `"assetId"`, `"url"`, `"generated": true`,
`"provider": "<provider>"`, and `role` equal to the purpose. For an approved
ASK slot the role is `product_lifestyle`, the entry also carries
`"askApproved": true`, and the merchant's words live in the plan record
(the type checklist review T8 rejects an ASK role without that flag). Nothing else about
generation enters the page record.

## 8. Generation request checklist

Complete every line with yes before calling `lexsis_drafts.asset_generate`
or any external generator. One no stops the call.

1. The slot exists in the plan's Asset slots table with an id and section.
2. Steps 1 and 2 of the sourcing sequence ran for this slot and found nothing (Source decision will read `library: none`).
3. The purpose is in section 3, or in section 4 with the merchant's yes for this slot quoted in the Generation record.
4. The job the slot fills is `context`, a backdrop, a texture, a decoration or an authored icon set; not an identity-bound job.
5. The page type's `imagery.hero` is not `packshot` or `ugc-screenshot`, or the ASK line for that case was answered yes.
6. The placement obeys N2 (one background; full-bleed only in the bold moment), N7 (one legibility overlay, no gradient washes), N8 (card backgrounds only around objects), N10 (no motion).
7. `lexsis_workspace.credits` was read and the merchant confirmed the batch count and cost.
8. Aspect matches the slot; a mobile crop is planned as a separate portrait generation or a focal point.
9. The prompt names a material or place, carries the negative list, and passes brand hexes from the brand kit.
10. For `product_composite`: `reference_images[0]` is the real cut-out (Shopify or library), viewed and identity-confirmed.
11. The alt decision is made: `alt=""` for decorative purposes, product alt for composites.
12. The disclosure decision is made from section 6 and the label text, if any, is written.
13. Generated count on the page after this call is four or fewer.
14. The Generation record row is drafted and will be completed with the returned asset id.

## 9. Rules

Checks use persisted MCP source and the hosted draft. `PEOPLE` is the regex
`\b(woman|women|man|men|girl|boy|person|people|model|customer|shopper|reviewer|hand|hands|face|smile|smiling|doctor|nurse|dermatologist|founder|team|staff|child|kid|baby|toddler|family|couple|influencer|creator)\b`.

GP1. Never generate anything in section 2; no instruction, design.md line or brief lifts the block. LAW.
Rationale: fake testimonials and misrepresented products carry regulatory penalties and platform rejection (sources in section 2).

GP2. Composite only over a real cut-out and leave the product pixels untouched. LAW, OPERATOR.
Rationale: a repainted product misleads about what ships (GN1); `references/design-enrichment.md` compositing recipes assume a real reference image.
Check: view the composite beside the source packshot with `lexsis_assets.view`; colour, shape and label identical (yes/no in `QA record`); Generation record cites the reference asset id.

GP3. Give decorative generated images `alt=""` and `aria-hidden="true"`; give composites a product alt that names the product. LAW.
Rationale: W3C alt decision tree https://www.w3.org/WAI/tutorials/images/decision-tree/ .

GP4. Never let people words appear in the alt text or prompt of a generated slot unless the ASK synthetic-model case was approved. LAW.
Rationale: 16 CFR 465; ASCI prohibited tier.

GP5. Never generate text into an image; every headline, price, label and badge is HTML. LAW.
Rationale: WCAG 1.4.5; Google and Shopify overlay rules (section 2).

GP6. Place `hero_bg` and `section_bg` only in the plan's bold moment; keep one page background everywhere else. OPERATOR.
Rationale: N2 and N7 in `references/design-rules.md`; a generated band per section is the template tell those rules exist to stop.
Check: count of full-width elements with a generated background image is 0 or 1 and its section id equals the plan's "Bold moment" line (browser check from N2).

GP7. Record provenance three ways: metadata on the original, `generated: true` plus `provider` in the page record, and the Generation record in the plan. LAW.
Rationale: Google requires `IPTC DigitalSourceType`; EU and ASCI labelling decisions must be auditable; hosts may strip file metadata.

GP8. Show a visible label wherever section 6 requires one and place it adjacent to the image. LAW.
Rationale: EU Art. 50 first-exposure labelling; ASCI medium tier.

GP9. Read credits and obtain a yes for the named batch before spending; cap generated assets at four per page. OPERATOR, HEURISTIC.
Rationale: `/design-page` authorises page creation, not generation; more than a few generated backdrops read as a template.

GP10. Use `high` quality only for `hero_bg`; `medium` for section and card backgrounds and composites; `low` for textures and decoration. OPERATOR.
Rationale: cost table in `references/design-enrichment.md`.
Check: Generation record "Style / quality" column obeys the mapping.

GP11. Never place a generated image in the gallery, the first gallery position, the feed image or a proof section. LAW.
Rationale: GN12; feed and gallery positions carry product identity; proof sections carry testimony.
Check: no manifest entry with `generated: true` has `sectionId` in `gallery`, `buy-box`, `product-hero`, `reviews`, `ugc-grid`, `testimonial-spotlight`, `before-after`, `press-marquee`, `certifications`, `awards`.

GP12. Log every ASK approval with the merchant's words and the date; never infer approval from plan approval. OPERATOR.
Rationale: an ASK image carries a label and legal exposure the merchant must own.
Check: Generation record "Approved by" for ASK rows quotes text and a date; `PLAN_APPROVED` alone is not accepted.

GP13. Never add props, gifts, accessories or a second product to a composite that could read as shipped with the product. LAW.
Rationale: included-items misrepresentation; ASCI "exaggerating product features".
Check: view; the composite contains the product and a surface or scene only (yes/no).

GP14. Never use a generated image to fill `in-use`, `scale`, `size-reference`, `swatch`, `texture` of the product, `ingredient-or-material` presented as own sourcing, or `result-or-context` results. LAW, RESEARCH.
Rationale: these jobs are how the shopper judges the real product (Baymard in-scale, human model, health and beauty research cited in `image-jobs-by-page-type.md`).
Check: every `generated` slot's Role/purpose job is `context`, a backdrop, a texture fill, a decoration or an icon set.

## Sources

- Google Merchant product data spec (IPTC) https://support.google.com/merchants/answer/7052112 ; promotional overlays https://support.google.com/merchants/answer/6101131
- Shopify Theme Store requirements https://shopify.dev/docs/storefronts/themes/store/requirements ; Shopify Magic media https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic/media-generation
- FTC consumer reviews and testimonials rule https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials ; Q&A https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers ; Federal Register https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-465-trade-regulation-rule-use-consumer-reviews-testimonials-final-rule ; health products guidance https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance
- ASCI draft AI labelling guidelines https://www.ascionline.in/wp-content/uploads/2026/05/asci-ai-labelling-guidelines.pdf ; coverage https://www.thehindubusinessline.com/info-tech/asci-proposes-risk-based-approach-for-responsible-labelling-on-ads-made-with-ai/article70969237.ece
- EU AI Act Art. 50 quick facts https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems ; Orrick summary https://www.orrick.com/en/insights/2026/08/eu-ai-act-transparency-obligations-for-ai-generated-content-article-50
- ASA before/after https://www.asa.org.uk/advice-online/before-and-after-photos.html ; production techniques https://www.asa.org.uk/advice-online/cosmetics-the-use-of-production-techniques.html
- Meta AI labels https://www.facebook.com/business/help/1010479435004531 ; newsroom https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/
- W3C images tutorial https://www.w3.org/WAI/tutorials/images/ ; alt decision tree https://www.w3.org/WAI/tutorials/images/decision-tree/
- NN/g AI-generated images https://www.nngroup.com/articles/ai-generated-images/ ; Nosto trust ranking https://www.nosto.com/blog/new-research-brands-prefer-ugc-for-diversity/
- Secondary (verify before legal reliance): Craftshift on Shopify AI disclosure https://craftshift.com/disclose-ai-generated-product-images-shopify-2026/
