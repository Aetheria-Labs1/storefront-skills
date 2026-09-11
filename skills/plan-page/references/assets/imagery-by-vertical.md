# Imagery by vertical

The asset layer per vertical: which image jobs the vertical adds to the page
type's requirements, the default hero, on-body and scale rules, swatch and
texture rules, facts-panel legibility, before/after pointers, size-inclusive
rules, what generic templates miss, and anti-patterns. The design layer
(section sequences, tone, module choices) lives in `references/vertical-*.md`
for beauty, fashion, food, home, luxury and supplements; electronics,
jewellery, pets and baby have no design-layer file yet, so this file plus the
page type file govern them. The page type fixes the base jobs
(`references/assets/image-jobs-by-page-type.md`); the vertical raises them.
Studio, lifestyle and UGC shares are in section 6 of that file and are not
repeated here.

Tags: LAW, RESEARCH, OPERATOR, HEURISTIC as defined in
`references/assets/image-jobs-by-page-type.md`. Teardown evidence is from
internal teardown audit, 2026-09-10 (OPERATOR).

## 0. Vertical index

| Vertical | Design layer | Gallery min | Default PDP hero | Added required jobs |
|---|---|---|---|---|
| Beauty | `references/vertical-beauty.md` | 6 + 1 per shade on skin | `packshot` with selected shade | `swatch`, `texture`, `in-use` (applied), `label-or-facts-panel` (INCI) |
| Supplements | `references/vertical-supplements.md` | 5 | `packshot` | `label-or-facts-panel`, `scale` (serving), `sequence` (routine), `included-items` (kits) |
| Fashion | `references/vertical-fashion.md` | 8 to 12 | `packshot` on model | `size-reference`, `detail`, `variation`, `in-use` (movement) |
| Food and beverage | `references/vertical-food.md` | 5 | `packshot` or `product-in-context` (plated) | `scale` (serving), `ingredient-or-material`, `label-or-facts-panel` (nutrition) |
| Home and furniture | `references/vertical-home.md` | 8 | `product-in-context` (room at scale) | `scale`, `diagram` (dimensions), `texture`, `variation` (finish) |
| Electronics | none | 7 | `packshot` | `detail` (ports), `included-items`, `scale` (in hand) |
| Jewellery | none (use `vertical-luxury.md` for tone) | 6 | `packshot` macro | `detail`, `scale` (on body), `swatch` (metal, stone) |
| Pets | none | 6 | `in-use` (animal using it) | `scale` (vs breed), `detail` (material), `included-items` |
| Baby | none | 6 | `in-use` (caregiver, correct use) | `scale` (vs age), `label-or-facts-panel` (safety), `sequence` (assembly, washing) |
| Luxury | `references/vertical-luxury.md` | 6 | `packshot` with whitespace | `detail` (craft macro), `packaging`, `texture` |

## 1. Beauty

| Item | Rule |
|---|---|
| Required jobs | `identity`, `texture` (formula macro), `swatch` (whole shade range side by side on diverse skin tones), `in-use` (applied on the intended area, one human-model image per shade on a matching skin tone), `variation` (gallery swaps on shade), `label-or-facts-panel` (INCI as HTML). RESEARCH https://baymard.com/blog/health-and-beauty-ux-research |
| Hero | `packshot` with the selected shade on `pdp`; `product-in-hand` or `editorial-lifestyle` on landing types; a face may look at camera (the face is the canvas, IJ11 exception) |
| On-body and scale | Applied product on skin, hair or nails; arm swatch strip; texture smear on a neutral surface under even light. OPERATOR: Sharma "see the texture on skin, with bright lights" https://sharmabrands.com/blogs/newsletter/7-biggest-landing-page-mistakes |
| Swatch and shade | One real swatch per shade; shade-finder result must show the same shade image as the PDP; never a generated skin tone; flat CSS chips allowed only next to the real swatch image |
| Facts panel | Full INCI list as HTML text; a label photo is supplementary and zoomable |
| Before/after | Only through `references/proof/before-after-and-claims.md`: same-session lighting, no retouching in product-relevant areas, signed and dated consent, evidence on file; CAP treats retouched "after" images as misleading even with a disclaimer https://www.asa.org.uk/advice-online/cosmetics-the-use-of-production-techniques.html . Never in the hero. Never generated |
| Size-inclusive | Shade range shown across the full tone range the product sells; models across skin tones and ages when the range is marketed as inclusive |
| Templates miss | A one-line skin-tone fit sentence per shade in the selector (Jones Road: 15 shades each with "for fair to medium skin tones"); how-to steps with inline video; press quotes as text rather than logos. Jones Road's own PDP had zero lifestyle imagery in extracted alt text, the gap this file's `in-use` requirement closes |
| Anti-patterns | Shade list rendered twice; two different star ratings on one page; "Results" image sections with no labels, interval or consent line (Mamaearth); lash inserts or extensions beyond what the product achieves; clinical props; generated skin |

## 2. Supplements

| Item | Rule |
|---|---|
| Required jobs | `identity`, `label-or-facts-panel` (Supplement Facts legible: HTML text preferred, or a real photo at 1600 px or more, zoomable), `scale` (scoop or serving in hand), `texture` (mixing or powder-into-water shot), `sequence` (routine: when, how much), `included-items` for kits and welcome boxes. LAW: 21 CFR 101.36 https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-101/subpart-C/section-101.36 |
| Hero | `packshot` with the facts panel one click away; `product-in-context` (routine) on subscription pages |
| On-body and scale | Serving size in hand or against a glass; capsule beside a coin; never a body transformation |
| Swatch and texture | Powder, gummy or capsule macro; the mixed drink as consumed |
| Facts panel | Every number the page quotes (mg, CFU, servings) appears in HTML and matches the label photo; footnote the study design and n when a stat is shown (AG1: "third-party, single-arm study, 35 adults") |
| Before/after | Forbidden as imagery; results are text claims in the proof ledger with substantiation. FTC expects randomised controlled trials for health claims and judges the net impression of all images https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance |
| Size-inclusive | Hands and routines across ages and skin tones where real media exists; no "fit" imagery implying body outcomes |
| Templates miss | Formula or strain table with mg or percentages (Seed, The Whole Truth ingredient % chart); a mechanism diagram with numbers in HTML (Seed ViaCap); lab-test results as a dated pass/fail modal (Salt of the Earth); welcome kit photographed as included items rather than as a discount |
| Anti-patterns | Lab coats, stethoscopes, anatomy diagrams implying treatment; "clinically proven" badges without a ledger row; generated doctors (ASCI prohibited tier https://www.ascionline.in/wp-content/uploads/2026/05/asci-ai-labelling-guidelines.pdf ); a 3.9 rating leading the hero; two conflicting review counts on one page (Create, Sun Powder) |

## 3. Fashion

| Item | Rule |
|---|---|
| Required jobs | `identity` (on model, front, back, side), `in-use` (movement), `detail` (fabric, stitching, hardware), `size-reference` (model height and size worn in HTML), `variation` (every colour photographed), `texture` (fabric macro), `swatch` (fabric or colour). RESEARCH https://baymard.com/blog/human-model ; 5 to 15 thumbnails https://baymard.com/blog/secondary-hover-information |
| Hero | `packshot` on model for `pdp`; `editorial-lifestyle` for lookbook and landing types; restraint and whitespace for premium lines (Speero: smaller images and whitespace raised perceived value of a dress shirt) https://speero.com/post/how-product-image-size-impacts-value-perception-original-research |
| On-body and scale | On-model is mandatory for anything worn; state "Model is 5'9" wearing size M" in HTML beside the gallery; flat lay as a secondary identity image |
| Swatch and texture | One swatch per colourway; fabric macro at the drape point |
| Facts panel | Fabric composition and care as HTML (Snitch shows composition %); size chart as an HTML table, never only an image |
| Before/after | Not applicable; "fit" claims are review quotes in the ledger |
| Size-inclusive | Multiple body sizes and skin tones where the range is inclusive; the size-run shown matches sizes actually sold; sold-out sizes shown inline in the selector, not hidden |
| Templates miss | Model height plus size worn line (Snitch); sold-out sizes inline; UGC of fit ("how does it fit them, do I relate") lifted engaged-shopper conversion 20% at UNTUCKit https://www.yotpo.com/case-studies/untuckit/ ; 32% more likely to buy clothing modelled by a fellow customer https://www.yotpo.com/blog/visual-reviews/ |
| Anti-patterns | Only cut-outs for worn products; a size chart as an image alone; three rotating promo bars above the gallery; mixed aspect ratios in the product grid; nine on-model shots and no size guide (Snitch) |

## 4. Food and beverage

| Item | Rule |
|---|---|
| Required jobs | `identity` (pack front), `label-or-facts-panel` (pack back, nutrition panel legible or as HTML), `scale` (serving: bowl in hand, glass on table), `ingredient-or-material` (flat lay), `context` (occasion), `in-use` (pour, plate, steam) |
| Hero | `packshot` for search and Shopping traffic; `product-in-context` (plated or poured) for social traffic; appetising food is a "magnetic" image feature http://ptgmedia.pearsoncmg.com/images/9780321498366/excerpts/eyetrackwebu_06to226.pdf |
| On-body and scale | Portion beside a hand or standard tableware; pack beside a known object for multi-packs |
| Swatch and texture | Flavour tiles with real product, not colour blocks alone; texture macro (crumb, pour, foam) |
| Facts panel | Nutrition per serving as an HTML table; ingredient percentages where the merchant declares them (The Whole Truth); allergens in text |
| Before/after | Not applicable |
| Size-inclusive | Not applicable; show hands and tables across the market's households |
| Templates miss | Origin, yield and preservative chip row as the hero spec line (Sleepy Owl: "100% Arabica, 3 cups per pack, from Chikmagalur"); tasting notes on collection cards (Blue Tokai); a short muted pour or sizzle loop, since food and beverage videos under one minute have the highest engagement (Wistia 2026, see `video-rules.md`) |
| Anti-patterns | Generated food or ingredients (GN11 in `generation-policy.md`); a subscription collection with no hero image and no headline (Blue Tokai); stock "hands and coffee" scenes; steam or gloss added in retouching that changes what ships |

## 5. Home and furniture

| Item | Rule |
|---|---|
| Required jobs | `identity` (cut-out), `context` (room at true scale with a person or standard object), `scale`, `diagram` (dimensions with numbers in HTML), `texture` (material macro), `variation` (finish or colour), `included-items` and `sequence` (assembly). RESEARCH: 28 to 37% of sites miss in-scale https://baymard.com/blog/in-scale-product-images ; https://baymard.com/blog/furniture-and-home-decor-ux-research |
| Hero | `product-in-context` at true scale for `pdp` and landing; `grid` for collections |
| On-body and scale | A person or a standard object (chair, door, bed frame) in the room shot; a dimension diagram beside the gallery; a size-confirmation nudge under add to cart (Wakefit "confirm size fits your bed") |
| Swatch and texture | Finish swatches as real photos; fabric or wood macro |
| Facts panel | Dimensions, weight, materials, care as an HTML spec table; layer or construction diagram with labels in HTML (Endy layers and height rows) |
| Before/after | Not applicable |
| Size-inclusive | Rooms and bodies across the market; no single "showroom" body type |
| Templates miss | Tier or model comparison with a "who it's for" line per tier (Wakefit, Endy "most loved by"); trial nights and warranty years photographed as label or certificate where they exist; 3D or AR when available (shoppers 44% more likely to add to cart after 3D interaction, self-selected) https://www.shopify.com/ca/case-studies/rebecca-minkoff ; customer photo and video gallery with variant tags (Wakefit, Ridge "Reviewing: [variant]") |
| Anti-patterns | Cut-outs only; a listicle with no image of the actual product set (Miracle sheets); dimension numbers baked into an image; three overlapping price offers crowding the gallery |

## 6. Electronics

| Item | Rule |
|---|---|
| Required jobs | `identity` on neutral, `detail` (ports, connectors, mounts: the compatibility question), `scale` (in hand or on desk), `included-items` (in-box flat lay), `in-use`, `diagram` when a feature needs explaining. RESEARCH: "what's included" +30.5% CVR, n=12,412 https://www.processcreative.com.au/blog/a-b-testing-does-showing-whats-in-the-box-actually-lift-conversions |
| Hero | `packshot`, large; larger images raise perceived value for spec goods (Speero, above) |
| On-body and scale | In-hand or on-ear or on-desk; a reference object for accessories |
| Swatch and texture | Colour variants each photographed (Ridge: 55 colour cards, each with its own image); surface finish macro |
| Facts panel | Spec table as HTML (boAt: 16 rows); screens show real UI, never a placeholder screen; feature callouts as HTML over the image, not baked in |
| Before/after | Not applicable; performance claims are ledger rows with test data |
| Size-inclusive | Hands and ears across the market where real media exists |
| Templates miss | Hotspot image with numbered callouts in HTML (Ridge); per-attachment photo with caption (Bombay Shaving Company: five heads captioned); quantified-benefit headers beside a feature image ("5 min charge = 75 min play", boAt); subtitle carrying the two or three decision specs |
| Anti-patterns | Feature banners with specs baked into the image; a hero giveaway banner outranking the product; duplicated feature rows; two conflicting country-of-origin statements beside the gallery |

## 7. Jewellery

| Item | Rule |
|---|---|
| Required jobs | `identity` (macro on neutral, true colour), `scale` (on neck, wrist, ear or hand across skin tones; coin or ruler for small pieces), `detail` (clasp, setting, hallmark), `swatch` (metal and stone options), `packaging` and `gift-presentation` (box). RESEARCH https://baymard.com/blog/human-model |
| Hero | `packshot` macro with whitespace; `product-in-context` on body for landing types |
| On-body and scale | Every piece on a body part; chain lengths shown on a torso with the length in HTML; ring sizes as an HTML guide |
| Swatch and texture | Metal finish and stone colour as real macro swatches; never a rendered stone standing in for the real one |
| Facts panel | Metal, carat, stone, weight, dimensions as HTML; certification with issuer as a ledger row (`references/proof/trust-badges-certifications.md`) |
| Before/after | Not applicable |
| Size-inclusive | Skin tones and hand or neck sizes across the market; stacking shots show real combinations sold |
| Templates miss | No jewellery page is in the teardown set; apply Baymard human-model and in-scale research and the luxury restraint rule (fewer, larger, more margin) |
| Anti-patterns | Macro only, no on-body; rendered or generated stones and metals (GN1); colour-shifted metals from non-sRGB files; gift boxes shown that do not ship |

## 8. Pets

| Item | Rule |
|---|---|
| Required jobs | `in-use` (the animal actually using the product), `scale` (against a recognisable breed size or a hand), `detail` (material, seams, safety), `included-items`, `identity`, `ugc` when rights exist (photos are critical in pets https://www.bazaarvoice.com/wp-content/themes/bazaarvoice/_sei-2019/static/downloads/BV19-SEI-Main-NA-Final.pdf ) |
| Hero | `in-use` with the animal for `pdp` and landing; `packshot` for search traffic |
| On-body and scale | Breed named in alt or caption ("shown on a 25 kg Labrador"); size guide as an HTML table by weight and breed |
| Swatch and texture | Fabric, chew material, coating macro |
| Facts panel | Ingredients and feeding guide as HTML for food; material and washing as HTML for gear |
| Before/after | Forbidden as imagery for health or behaviour outcomes (GN4) |
| Size-inclusive | Breeds and sizes the product actually fits |
| Templates miss | Launch pages that sell the roadmap must still show the real prototype; Klassy Pet's reservation page had no product imagery at all, its weakest point |
| Anti-patterns | Generated animals presented as customers' pets (GN3 and GN9); unsafe use depicted (GN10); stock "happy dog" without the product |

## 9. Baby

| Item | Rule |
|---|---|
| Required jobs | `in-use` (caregiver and child in correct, safe use), `scale` (relative to the child's age band), `label-or-facts-panel` (safety and certification marks as a real label photo or HTML text), `included-items`, `sequence` (assembly, washing, installation), `identity` |
| Hero | `in-use` with correct use for `pdp` and landing; `packshot` for gear on search traffic |
| On-body and scale | Age band in HTML beside the image ("shown with a 6-month-old"); harness or fit points visible |
| Swatch and texture | Fabric and material macro; colour variants photographed |
| Facts panel | Certifications with issuer and number as ledger rows; never generated badges (GN5); age and weight limits as HTML |
| Before/after | Forbidden (GN4); developmental or health outcomes are not imagery |
| Size-inclusive | Families and caregivers across the market where real media exists |
| Templates miss | No baby page is in the teardown set; apply the safety and certification rules above and the home vertical's assembly sequence pattern |
| Anti-patterns | Synthetic children or caregivers under any label (ASCI prohibited tier; GN3); depictions of unsafe use even in "lifestyle" shots (car seat without harness, crib with soft bedding); generated certification marks |

## 10. Luxury

| Item | Rule |
|---|---|
| Required jobs | `identity` with generous margin, `detail` (craft macro: stitching, engraving, weave), `texture`, `packaging` (unboxing), `in-use` (one editorial look), `variation` |
| Hero | `packshot` with whitespace or one `editorial-lifestyle` look; never a grid or a busy scene. RESEARCH: whitespace raised perceived value for experience goods https://speero.com/post/how-product-image-size-impacts-value-perception-original-research |
| On-body and scale | One on-body image per worn piece; scale shown quietly (a hand, a shoulder), not a ruler |
| Swatch and texture | Material macro on neutral; leather, metal and fabric swatches as real photos |
| Facts panel | Provenance, materials and care as HTML; certificates with issuer as ledger rows |
| Before/after | Not applicable |
| Size-inclusive | As fashion where the product is worn |
| Templates miss | Warranty or repair programme photographed as an artefact (Ridge "Built for Life", Mokobara "CTRL+Z coverage" expander); a feature carousel is acceptable below the fold only, never as the hero (Mokobara's 8-slide feature carousel sits mid-page) |
| Anti-patterns | Discount pills or percent-off chrome near imagery (N9 in `references/design-rules.md`); more than 5% UGC share; generated backdrops with glow or gradient (N7); hover-scale on product images (N7) |

## 11. Rules

Checks use persisted MCP source and the hosted draft.

IV1. Show the whole shade range on diverse skin tones and one applied image per shade for colour cosmetics; bind the gallery to the shade selector. RESEARCH.
Rationale: Baymard health and beauty guidelines on arm swatches, human models per shade and applied makeup https://baymard.com/blog/health-and-beauty-ux-research .
Check: `swatch` slot count is at least the shade count, or one swatch-strip slot exists; the `variant-picker` island binds to the gallery (yes/no in `QA record`).

IV2. Render every regulated label (supplement facts, nutrition, INCI, safety limits) as HTML text and keep any label photo legible at 1600 px or more. LAW.
Rationale: 21 CFR 101.36 https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-101/subpart-C/section-101.36 ; WCAG 1.4.5 images of text https://www.w3.org/WAI/tutorials/images/ .

IV3. Put a model height and size worn line in HTML beside every on-model fashion gallery, and photograph every colourway. RESEARCH.
Rationale: fit is the top uncertainty for worn goods https://baymard.com/blog/human-model .

IV4. Never generate food, ingredients or formula; photograph the real serving at scale. LAW.
Rationale: GN11 in `generation-policy.md`; net-impression deception https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance .
Check: no manifest entry with `generated: true` on a food page has a `sectionId` of `gallery`, `ingredients`, `product-hero` or `benefits`.

IV5. Give every home and furniture product a room shot at true scale and a dimension diagram with numbers in HTML. RESEARCH.
Rationale: 28 to 37% of sites miss in-scale imagery https://baymard.com/blog/in-scale-product-images .

IV6. Photograph ports, connectors and the box contents for electronics; show real UI on screens. RESEARCH.
Rationale: compatibility is Baymard's first image type; box contents lifted conversion 30.5% https://www.processcreative.com.au/blog/a-b-testing-does-showing-whats-in-the-box-actually-lift-conversions .
Check: a `detail` slot whose alt names a port, connector or mount, and an `included-items` slot, both `verified`.

IV7. Show every jewellery piece on a body part across skin tones and give small pieces a coin or ruler reference. RESEARCH.
Rationale: Baymard human model and in-scale research (above).
Check: each jewellery product has a slot whose alt names neck, wrist, ear, hand or finger, and small pieces have a `scale` slot.

IV8. Show pet products in use by a real animal with the breed or weight stated; never a generated animal as a customer's pet. LAW, RESEARCH.
Rationale: GN3 and GN9 in `generation-policy.md`; photos are critical in pets (Bazaarvoice SEI 2019, above).
Check: the `in-use` slot alt names an animal and the caption or alt states breed or weight; no `generated: true` entry on a pets page contains an animal word in alt.

IV9. Show baby products in correct, safe use with a caregiver; never synthetic children; never unsafe depictions. LAW.
Rationale: ASCI prohibited tier covers unsafe situations and fabricated people regardless of label https://www.ascionline.in/wp-content/uploads/2026/05/asci-ai-labelling-guidelines.pdf .

IV10. Use fewer, larger, whitespace-framed images for luxury and keep UGC to a curated minimum. RESEARCH.
Rationale: whitespace raised perceived value for experience goods https://speero.com/post/how-product-image-size-impacts-value-perception-original-research .
Check: image count is at or near the gallery minimum (6) and no product grid on the page exceeds three columns at 1280.

IV11. Route every before/after through the proof ledger and its file; none in the hero, none generated, none without interval and consent. LAW.
Rationale: `references/proof/before-after-and-claims.md`; ASA https://www.asa.org.uk/advice-online/before-and-after-photos.html .
Check: every `before-after` section cites a `P[0-9]+` id with status `verified`; the IJ13 acceptance rule from `image-jobs-by-page-type.md` passes.

IV12. Match the vertical's added required jobs on top of the page type's row before the asset question is asked. OPERATOR.
Rationale: the type fixes anatomy, the vertical fixes which modules fill the slots (`references/page-types/_index.md` section 8).
Check: the plan's "Gallery jobs" line lists each job from this file's section 0 row for the vertical as covered or as a created slot.

## Sources

- Baymard: health and beauty https://baymard.com/blog/health-and-beauty-ux-research ; human model https://baymard.com/blog/human-model ; in-scale https://baymard.com/blog/in-scale-product-images ; furniture and home decor https://baymard.com/blog/furniture-and-home-decor-ux-research ; thumbnails https://baymard.com/blog/secondary-hover-information
- Speero/CXL image size and perceived value https://speero.com/post/how-product-image-size-impacts-value-perception-original-research
- Process Creative what's included test https://www.processcreative.com.au/blog/a-b-testing-does-showing-whats-in-the-box-actually-lift-conversions
- Yotpo UNTUCKit https://www.yotpo.com/case-studies/untuckit/ ; visual reviews https://www.yotpo.com/blog/visual-reviews/
- Shopify and Rebecca Minkoff 3D/AR https://www.shopify.com/ca/case-studies/rebecca-minkoff
- Bazaarvoice SEI 2019 https://www.bazaarvoice.com/wp-content/themes/bazaarvoice/_sei-2019/static/downloads/BV19-SEI-Main-NA-Final.pdf
- NN/g eyetracking excerpt http://ptgmedia.pearsoncmg.com/images/9780321498366/excerpts/eyetrackwebu_06to226.pdf
- Sharma Brands https://sharmabrands.com/blogs/newsletter/7-biggest-landing-page-mistakes
- Regulation: 21 CFR 101.36 https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-101/subpart-C/section-101.36 ; FTC health products guidance https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance ; ASA production techniques https://www.asa.org.uk/advice-online/cosmetics-the-use-of-production-techniques.html ; ASA before/after https://www.asa.org.uk/advice-online/before-and-after-photos.html ; ASCI draft AI labelling https://www.ascionline.in/wp-content/uploads/2026/05/asci-ai-labelling-guidelines.pdf ; W3C images https://www.w3.org/WAI/tutorials/images/
