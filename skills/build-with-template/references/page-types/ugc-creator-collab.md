# UGC creator collab

A co-branded page where one creator's content is both the hero and the proof. The visitor arrives from that creator's Reel, TikTok, YouTube description, link in bio or whitelisted ad, trusts the creator more than the brand, and must buy the creator's pick with the creator's discount already applied. The brand supplies the product, the policy facts and the rights paperwork; the creator supplies the voice.

## Identify it

Signals in the brief:
- A named creator, influencer, affiliate or ambassador; "collab", "x [name]", "code SARAH20", "creator drop", or a programme with many partners.
- Traffic is tiktok, instagram, influencer or affiliate links; the ad is a Spark or whitelisted creator post.
- The merchant has creator video and a rights agreement, or is about to sign one.

Near neighbours:
- `video-sales-page`: choose it when one long video carries the pitch; this type is many short clips and one creator's voice.
- `ad-landing-page`: choose it when the creator is a supporting testimonial, not the frame.
- `offer-page`: choose it when the discount is the message and the creator is only the code.
- `lookbook-shop-the-look`: choose it when the page is editorial imagery across many looks without a creator narrator.

Landing page tone for creator traffic: `references/traffic-source-tiktok.md` (UGC screenshot hero, native aesthetic). Rights, disclosure and display rules: `references/proof/ugc-rights-and-display.md`. This file holds the contract.

## Variants

- **Single-product creator page.** One hero product, the creator's clip, their quote, a kit as an optional add-on.
- **Creator picks (3 to 6 products).** `shop-the-look` cards, each with one line in the creator's words ("why I use this"); one CTA per card counts toward the CTA ceiling, so keep the primary CTA on the hero product and the cards on `next-step` links, or cap picks at two cards with buttons.
- **Creator kit.** A partner-curated bundle ("Sarah's kit") with savings math from the offer ledger; partner-curated bundles drove +67% AOV at Cozy Earth (OPERATOR, vendor case, https://creatorcommerce.shop/brand-case-studies/cozy-earth).

## Anatomy

1. `hero` mandatory. The creator's own clip (9:16, click to play or a muted captioned loop) or their photo; creator name and one-line personal welcome in their words ("Hey, it is Sarah, these are the three I actually use"); brand logo lockup; "Paid partnership" or "Ad" label in frame; the auto-applied discount stated as a fact ("Your 15% is applied at checkout"); one CTA.
2. `product-spotlight` mandatory. The hero product with price, variant, shipping and returns line, the creator's quote about it, and add-to-cart.
3. `ugc-grid` mandatory. The post that sent the visitor plus three to six more creator clips or stills, synced from the platform where rights allow; handle visible on each; captions on video; disclosure label in frame for the whole brand segment.
4. `shop-the-look` conditional: the creator picked three to six products. One creator sentence per card.
5. `routine` or `usage` recommended. How the creator uses it: steps, time of day, frequency, in their words.
6. `reviews` or `review-summary` recommended. Brand proof beside the creator's: rating with count, or two verbatim customer quotes; the creator is the primary proof, but at least one non-creator proof is mandatory (research block 14).
7. `offer` conditional: a creator kit or bundle exists. Savings math from the ledger; never a code to type.
8. `faq` recommended. Shipping, returns, "is this the same product Sarah uses", how the discount applies.
9. `shipping-returns` recommended when not already in the spotlight.
10. `closing-cta` mandatory. Same action; the creator's sign-off line above it.

Forbidden: `header`, `product-grid` (a catalogue dump loses the creator frame), `cross-sell` (the picks are the relationship), `countdown`, `stock-indicator`, `email-capture`, `sms-capture`, `quiz`, `related-reads`. One creator per page. Index length 6 to 9; research agrees.

## Workflow

Assets first: the creator's own content is the hero and the proof, so nothing is planned until the clips, their rights and their disclosure are in the ledger (`references/proof/ugc-rights-and-display.md`). Every module is creator media plus a few words, the product's real identity image, and the brand's policy facts; nothing is padded with stock, studio shots or generated people. Each Media line runs the loop in `references/workflows/section-asset-workflow.md` (sourcing: `references/assets/asset-sourcing-sequence.md`; video: `references/assets/video-rules.md`; ALLOW, ASK and NEVER: `references/assets/generation-policy.md`). Each Island line names the island and its decision inputs per `references/workflows/island-selection-workflow.md`, with the catalog from `lexsis_design.islands` and the variant and props resolved live from `lexsis_design.island_schema`.

Ask rule, used by every Media line below: tell the merchant what is missing (job, aspect, count), offer upload via `lexsis_asset_upload.upload` or MCP generation when the purpose is feasible under `references/assets/generation-policy.md`, and skip or merge the section only if the merchant chooses. In fast-draft, proceed with the closest existing asset or leave the slot `planned`, and list every missing asset in the plan and the draft summary. Creator media is the exception: `imagery.video` is required, so without one rights-cleared creator clip or still the build returns blocked with the reason and the import offer.

### Context reads
1. `lexsis_catalog.get` for the hero product and each pick: `identity` image per product, variant axes (the creator's variant is pre-selected where known; BuyBox variants carry no image, so colour-with-image needs VariantSwatches), price and compare-at (the creator discount is a ledger row with the list price as basis, `references/offers/offer-types.md`), selling plans (ignored: subscribe-save is a misfit), inventory (a real drop cap only), `included-items` media for a kit.
2. `lexsis_campaigns.creatives`, `analyze` and `frames` for the post or whitelisted ad that sends the click: the hook line the welcome repeats (`references/copy/message-match.md`), the offer in the caption, the frame that becomes the hero poster, paid or gifted status.
3. Rights first: for every creator asset a `P` ledger row with scoped written rights naming "website", handle, paid or gifted flag, music cleared, consent date; `lexsis_asset_library.search` with `theme_id`, `mode: "tags"` `social-proof` and `kind: "video"` for clips already imported with rights, then `lexsis_asset_import.import` of the creator's original files (never a screenshot) once the row exists.
4. `lexsis_catalog.reviews_status`, `reviews` (`product_id`, `has_media: true`): the non-creator proof band per `references/proof/reviews-sourcing.md`; creator content never enters the review average.
5. `lexsis_brand.context` and `brand_kit` (`theme_id`): tokens, logo lockup, shipping and returns facts, the disclosure wording for the market (US "Paid partnership", India an ASCI label, UK "Ad"). Skip `navigation`; nav is none.
6. `lexsis_asset_library.search` tag `product-shot` for the spotlight and picks. `lexsis_workspace.credits` is not needed; nothing on this page is generated.

### Section by section
Open every candidate with `lexsis_assets.view` and run the section fit review in section 1b of `references/workflows/section-asset-workflow.md` before use; view the clips or stills for one section together so the set reads as one shoot, and view a generated backdrop the same way after it returns. For creator media the viewing also confirms that the creator is the person the rights row names, that the product is visible and identifiable in the frame, that the clip is natively vertical rather than a letterboxed landscape crop, and that any burned-in caption or on-screen text is legible and does not duplicate the page headline.

**`hero`**
- Purpose: the creator's clip or portrait, their handle and disclosure label in frame, a one-line welcome in their words, the discount stated as a fact, one CTA.
- Media: yes; `ugc` as `video-poster` from the creator's 9:16 clip (a real frame with the creator and the product), or `ugc-screenshot` when the click came from a static post; 4:5 or 9:16. Search: the sending post's original via `lexsis_campaigns.frames` and `lexsis_asset_import.import` with the `P` row, then library `social-proof` with a `P` row. Nothing found: ask rule naming the rights row and the original file; generation is never feasible for people or UGC (GN3, GN9); the type is blocked until the merchant supplies it. No-go: a studio packshot, stock imagery, a second creator, autoplay with sound, urgency of any kind. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used. While viewing the clip, check that the disclosure label is in frame and that the `P` row matches this file. Viewing confirms the creator matches the rights row, the product is identifiable in frame, the clip is natively vertical, and any burned-in caption is legible and does not repeat the headline.
- Island: `VideoPlayer` for the clip, click to play with the poster, captions supplied with the media object; a muted captioned loop of 6 to 15 seconds only when the plan names it as the single motion moment with a pause control (N10). The disclosure label and handle are HTML over the frame. The CTA is an anchor to the spotlight. Resolve variant and props from `lexsis_design.island_schema`.
- Copy: welcome at most 25 words, verbatim and approved by the creator; "Your 15% is applied at checkout" with the free-shipping threshold; "Paid partnership" or "Ad" exactly as the market permits; no "obsessed" or "must-have" unless the creator said it (`references/anti-patterns/copy-anti-patterns.md`).
- Decide with: the `P` row status; `lexsis_campaigns.analyze` hook and offer; the offer ledger row.

**`product-spotlight`**
- Purpose: the hero product with price, variant, shipping and returns line, the creator's quote about it, add-to-cart.
- Media: yes; the `identity` image from catalog media (the one place a brand packshot belongs), plus one creator still of the product in use where rights exist. Nothing found for identity: ask rule; no generation is feasible (GP11). View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: `BuyBox`, one per page, its form decided by the variant count and axes, badges off, the applied discount in its label; `VariantSwatches` when colour variants carry images and to pre-select the creator's variant. `DeliveryEstimate` for the dispatch cutoff when `shipping-returns` is not a separate section (India pincode copy is static HTML). `StickyBar` bound to the spotlight, appearing after the hero CTA scrolls out with the discount fact in its label; it has no variant sync, so it carries a variant only when one is pre-selected and otherwise links back to the spotlight. Resolve variant and props from `lexsis_design.island_schema`; presets `buybox/default-light`, `deliveryestimate/inline-quiet`, `stickybar/product-light`.
- Copy: `add-to-cart` ("Add to cart, 15% applied"); list price struck only with the ledger basis; the creator's quote at most 30 words, verbatim.
- Decide with: variant axes and images; the percent-off or fixed-off ledger row and its auto-apply mechanic (never a code to type).

**`ugc-grid`**
- Purpose: the post that sent the visitor plus three to six more creator clips or stills, handle on each, disclosure for the whole brand segment.
- Media: yes; `ugc` clips at 9:16 native with captions and real poster frames, or stills at 1:1 or 4:5, uniform per grid, crop only, original grading; each item with its own `P` row and music cleared. Search: library `social-proof` with `kind: "video"` and `P` rows, then `lexsis_asset_import.import` of the creator's originals with consent. Fewer than four items: ask rule naming the count and the rights record each item needs; generation is never feasible (GN9); a smaller grid or none only on the merchant's call. No-go: brand-shot "UGC-style" content labelled as creator content, platform-licensed music kept in a hosted clip, a carousel. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used. View the tiles together as one set and check the disclosure label and the `P` row for each while viewing. Viewing confirms the creator matches the rights row, the product is identifiable in frame, the clip is natively vertical, and any burned-in caption is legible and does not repeat the headline.
- Island: `ShoppableVideoFeed` for three or more clips, posters on every item, click to play, sound off until tapped, creator name and caption shown, the hero product tagged; native `<video>` tiles for one or two clips; a static grid for stills. Resolve variant and props from `lexsis_design.island_schema`.
- Copy: handle visible on each tile; the disclosure label in frame; captions on video.
- Decide with: clip count and `P` rows; the UGC row in `references/assets/video-rules.md` (20 to 40 seconds, 9:16).

**`shop-the-look`** (conditional: the creator picked three to six products)
- Purpose: one card per pick with one line in the creator's words.
- Media: yes; one catalog `identity` image per pick via `lexsis_catalog.get`; a creator still with the pick in use where rights exist. Nothing found: ask rule; no generation is feasible. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used. Viewing confirms the creator matches the rights row, the product is identifiable in frame, the clip is natively vertical, and any burned-in caption is legible and does not repeat the headline.
- Island: `QuickAdd` on at most two cards (the CTA ceiling), links to the PDPs on the rest; alternatively the picks are tagged inside the `ShoppableVideoFeed` items. No `ProductCarousel` below four picks, and its entry animation off if used (N10). Resolve variant and props from `lexsis_design.island_schema`.
- Copy: `fab` on the card; the creator's sentence at most 30 words, verbatim; "Shop <name>'s picks" only for this variant.
- Decide with: pick count; the CTA ceiling of 2 to 3.

**`routine`** or **`usage`**
- Purpose: how the creator uses it: steps, time of day, frequency, in their words.
- Media: yes; `sequence` of three to five creator stills or one creator clip showing the routine, each with a `P` row. Search: library `social-proof`, then the creator's originals imported with consent. Nothing found: ask rule; generation is never feasible; the routine collapses into the hero clip's caption only if the merchant chooses. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used. Check the `P` row for each still or clip while viewing. Viewing confirms the creator matches the rights row, the product is identifiable in frame, the clip is natively vertical, and any burned-in caption is legible and does not repeat the headline.
- Island: `none` for stills; `VideoPlayer` for one routine clip, click to play; resolve variant and props from `lexsis_design.island_schema`.
- Copy: `bab` in the creator's voice; at most 120 words; step text in HTML.
- Decide with: what the creator actually filmed; `P` rows.

**`reviews`** or **`review-summary`**
- Purpose: the mandatory non-creator proof beside the creator's voice.
- Media: `review-with-media` cards from `reviews` with `has_media: true`; avatars real or CSS initials, never generated. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: by band per `references/proof/reviews-sourcing.md`. B0 and B1: no review module; `guarantee` plus `certification` supply the non-creator proof and the plan records it. B2: `ReviewCarousel` bound to the product id showing three to six media reviews, autoplay off (its default is on, N10); preset `reviewcarousel/grid-flat`. B3 and B4: a media grid of six to twelve, or `ReviewList` with media on. Creator content is never mixed in. Resolve variant and props from `lexsis_design.island_schema`.
- Copy: verbatim, dated, attributed as stored; the rating with n only at B2 or higher.
- Decide with: `reviews_status` band; `has_media` count.

**`offer`** (conditional: a creator kit or bundle exists)
- Purpose: the kit with savings math from the ledger, never a code.
- Media: yes; `included-items` flat lay of every shipped component from catalog media or merchant upload. Nothing found: ask rule; generation is never feasible for contents (`image-jobs-by-page-type.md` section 7, GP13); the kit ships as a list with component identity images meanwhile. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: when the kit is the hero product the spotlight `BuyBox` sells it; otherwise a card with `QuickAdd` or a link, since the page carries one BuyBox; resolve variant and props from `lexsis_design.island_schema`.
- Copy: "$87 separately, $59 as a set, save $28" from the ledger (`references/offers/offer-types.md`); "Add <name>'s kit".
- Decide with: the bundle ledger row and component prices from `lexsis_catalog.get`.

**`faq`**
- Purpose: shipping, returns, "is this the same product <name> uses", how the discount applies.
- Media: no.
- Island: `none`; native `<details>` and `<summary>` (the FAQ island is deprecated).
- Copy: answers at most 60 words; second person for brand policy lines.
- Decide with: policy URLs; the discount mechanic in the ledger.

**`shipping-returns`** (recommended when not already in the spotlight)
- Purpose: the policy facts in full.
- Media: no.
- Island: `DeliveryEstimate` for the cutoff line when shipping is domestic and predictable, `none` otherwise; resolve variant and props from `lexsis_design.island_schema`.
- Copy: days, scope and friction stated; policy URL.
- Decide with: `lexsis_brand.context` policy facts.

**`closing-cta`**
- Purpose: the same action; the creator's sign-off line above it.
- Media: optional reuse of the hero poster or spotlight identity slot; no new job.
- Island: `none`; the CTA anchors to the spotlight.
- Copy: the creator's sign-off verbatim, at most 25 words; the same CTA text as the spotlight.
- Decide with: the creator-approved copy record.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | `identity` for the spotlight and picks, `included-items` for a kit | nothing creator-shaped; catalog media never fills a UGC slot | reuse for spotlight and cards only |
| asset library | creator clips and stills already imported with `P` rows (`social-proof`), `product-shot` | the sending post's original, rights rows for older clips | ask the merchant for the rights row and original file; import with `lexsis_asset_import.import` after the written yes; no generation |
| ad creatives | the whitelisted or Spark post: hero poster, hook line, stated offer | anything the creator did not film | `lexsis_campaigns.frames` for the poster; the creator's consent must name the website, not only ads |
| generation | nothing; a `texture_fill` at most | creator, customers, product, results, logos, text | never; ask the merchant to import creator media instead |

With only one rights-cleared creator clip and the catalog identity image the page still ships: hero (the clip), spotlight, a one-item grid or none, faq, shipping and returns, closing; `shop-the-look`, `routine`, `offer` and the review module are listed as missing assets with the import offer and leave the page only on the merchant's decision, and the non-creator proof is `guarantee` plus `certification`. Without any rights-cleared creator media the type is blocked. Generated assets: zero on this type. Nothing is used sight unseen: every asset in this table is opened with `lexsis_assets.view` and passes the section 1b fit review before it is assigned.

## Above the fold (390px)

Visible, in order:
1. Brand and creator lockup (logo not clickable).
2. Creator clip or portrait, 9:16 or 4:5, with the disclosure label visible in frame and the creator's handle.
3. One-line welcome in the creator's words, at most 25 words.
4. Discount line as fact ("15% off is already applied") with the free-shipping threshold.
5. Primary CTA, full width, 48px minimum.

The first screen must read as a continuation of the post that sent the click: same face, same hook, same product (OPERATOR, TikTok landing-page guidance via `references/traffic-source-tiktok.md`). Must not appear: a code to type, a countdown, a stock count, a second creator, stock imagery, a studio packshot hero, press logos, an email popup, autoplay with sound.

## Proof

Density: 3 to 5 modules (index; research places creator pages at medium density with the creator voice as the primary proof, the index asks for more because the brand is cold to this visitor).

| Kind | Where | Minimum evidence |
|---|---|---|
| `creator-video` | `hero`, `ugc-grid` | asset id, scoped written rights that name "website" (organic consent does not cover the site or ads), creator handle, paid or gifted disclosure flag, platform-licensed music stripped or relicensed (LAW: platform terms; FTC material connection) |
| `ugc-photo` or `ugc-video` | `ugc-grid` | rights record per item; source labelled; never presented as "customer reviews" when it is creator content |
| `review-summary` or `review-quote` | `reviews`, `product-spotlight` | API count and average at 5 or more reviews; verbatim dated quotes; the non-creator proof that is mandatory |
| `policy-fact` or `guarantee` | `product-spotlight`, under every CTA | policy URL, exact terms |
| `expert-quote` | only when the creator holds the credential | credential verifiable, connection disclosed |

Rights and disclosure are mandatory, not optional (LAW): US "#ad" or "Paid partnership" clear and conspicuous, superimposed on video, in the same language as the content (FTC Endorsement Guides, https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking); India one of ASCI's permitted labels, on screen at least 3 seconds for video up to 15 seconds, a third of the duration for 15 seconds to 2 minutes, the whole brand segment beyond that (https://www.ascionline.in/social/wp-content/uploads/2025/04/ASCI-Influencer-Guidelines.pdf); UK "Ad" per ASA and CMA. Free product is a material connection everywhere. Creator withdraws consent: remove from every surface within 30 days (GDPR) or 45 days (CCPA). Templates and the request script: `references/proof/ugc-rights-and-display.md`.

Placement: creator proof in the top 20% and again at 40 to 60%; brand proof at 60 to 80% beside the spotlight or reviews; policy fact under every CTA. Forbidden kinds: `social-proof-popup`, `live-viewer-count`, `press-logo-unlinked`. Zero brand reviews: `references/proof/reviews-sourcing.md` tiers 4 and 5; the non-creator proof becomes `guarantee` plus `certification`; the plan records it.

## Offer and CTA

- CTA count: 2 to 3 (index; research allows 2 to 4). Hero, product spotlight, closing; one destination.
- First CTA: hero (`first_after_section: 0`).
- Sticky: optional, recommended by the creator-commerce vendors (CreatorCommerce lists it as mandatory; that is a vendor claim). When used: appears after the hero CTA scrolls out, discount fact in the label ("Add to cart, 15% applied"), one button.
- Copy pattern: `add-to-cart` for the hero product ("Add to cart", "Add Sarah's pick"); `shop-collection` only for the picks variant ("Shop Sarah's picks"). The creator's phrasing may sit as microcopy, not as the button text (design-rules A12).
- Price reveal: on the spotlight card, immediately; the discounted price shown with the list price struck only when the ledger holds the basis.
- Discount mechanics: auto-applied through the link, never a code to type. Cozy Earth's co-branded pages with auto-applied discounts reported +214% conversion and +67% AOV against generic pages (OPERATOR, vendor case, https://creatorcommerce.shop/brand-case-studies/cozy-earth); codes leak, blur attribution and lose the story. Single-use codes only as an anti-leak fallback (Aspire SecureCodes, https://www.aspire.io/creatorstores). The discount is one `percent-off` or `fixed-off` ledger row confirmed by the merchant.
- Offer fit: `none`, `percent-off` or `fixed-off` as the auto-applied creator discount, `gwp`, `free-shipping`, `bundle` (creator kit), `first-order` (when the creator audience is new to the brand), `trial-sample`, `limited-edition` (a real capped drop), `bnpl` on higher-ticket picks.
- Offer misfit: `bogo`, `tiered-volume`, `bundle-decoy`, `subscribe-save`, `referral`, `loyalty`, `cashback`, `mystery`, `pre-order-price`, `price-lock`, `flash-sale`, `clearance`, `gift-card`, `student-military`, `charity`. `references/offers/offer-types.md` governs.
- Urgency: `verified-only` and never in the hero. A real drop cap ("Edition of 500, counter stops at the cap") is the only urgency that fits a collab; no timers.

## Imagery

Required jobs: `ugc`, `identity`, `in-use`. Strongly recommended: `detail`, `scale`, `included-items` for a kit, `founder-or-team` for the creator portrait.
- Hero: `video-poster` from the creator's clip (a real frame with the creator and the product), or `ugc-screenshot` when the click came from a static post. Never a studio hero.
- Balance: creator content 60 to 80% of all media; brand packshots only on the spotlight and cards; consistent with the creator's aesthetic, not the brand's studio look (research block 14).
- Video: required. 9:16 native, captions burned in or toggleable, click to play or muted loop with a pause control, creator handle and disclosure label in frame, poster from the video, platform music stripped or licensed, `preload="none"`.
- Minimum images: 5 (hero frame, spotlight identity, three UGC tiles).
- Slots the plan must create: hero clip and poster; spotlight identity image; UGC grid of four to eight tiles (1:1 or 4:5, uniform, original grading, crop only); one card image per pick; kit flat lay when a kit exists. Employee or agency content shot "UGC-style" is lifestyle, not UGC, and is never labelled as customer or creator content (LAW, FTC insider rule).

## Copy

- Framework: `hook-story-offer` in the creator's first-person voice; `bab` in the creator's words for the routine; `fab` on product cards.
- Headline by awareness: problem-aware leads with the creator's own problem ("I stopped waking up puffy. Here is what changed"); solution-aware leads with the creator's result and the product ("The sheets Sarah actually sleeps on, 15% applied").
- Message match: the hero clip is the post that sent the click or the same creative; the welcome line repeats the post's hook; the offer equals the offer in the caption or ad (`references/copy/message-match.md`).
- Creator words: verbatim and approved by the creator; never written by the brand and presented as theirs (LAW: endorsements reflect the endorser's honest opinion and experience, FTC 16 CFR 255). Edits limited to trimming.
- Reading level: grade 6 to 8; short lines; the creator's register, including imperfect grammar, stays.
- Length ceilings: welcome 25 words; hero clip 20 to 40 seconds; per-product creator quote 30 words; routine 120 words; FAQ answer 60; total 300 to 700 words.
- Vocabulary: first person for the creator, second person for the brand's policy lines; no blacklist words; no "obsessed", "viral" or "must-have" unless the creator said it; disclosure words exactly as the jurisdiction permits ("Ad", "Paid partnership", "Sponsored"); sentence case.

## Never

- Never render creator content without a scoped, recorded rights agreement that names the website.
- Never omit the paid or gifted disclosure, or hide it in hashtags, alt text or the footer.
- Never make the visitor type a code; the discount is applied by the link.
- Never put more than one creator on a page.
- Never use stock imagery or a studio packshot as the hero.
- Never label brand-shot "UGC-style" content as creator or customer content.
- Never present creator content as customer reviews or mix it into a review average.
- Never keep platform-licensed music in a clip hosted on the page.
- Never autoplay with sound.
- Never show a countdown, stock count or viewer count, and never any urgency in the hero.
- Never send creator traffic to a generic homepage or PDP with a code (research block 14 top mistake).
- Never write the creator's quote for them.

## Examples

- Cozy Earth co-branded creator funnels across 600 or more creators: creator hero, auto-applied discount, creator-curated kits; +214% conversion and +67% AOV reported by the vendor (https://creatorcommerce.shop/brand-case-studies/cozy-earth).
- Hello Face "Real results": every result labelled with product, duration and frequency, a consent and unedited disclaimer at the top, a video UGC grid with handles, an FAQ answering "are these real?" (https://hellofaceglobal.com/real-results/). The labelling and consent pattern applies to every UGC tile here.
- Crocs x Kai Cenat creator storefront and Superfiliate coPages that sync creator posts to the page (https://d2c-times.com/is-superfiliate-the-creative-infrastructure-dtc-has-been-waiting-for-2/ ; https://sproutsocial.com/insights/creator-storefronts/).

## Checklist

```json
{
  "page_type": "ugc-creator-collab",
  "aliases": ["creator page", "co-branded landing page", "coPage", "creator storefront", "influencer landing page", "affiliate landing page", "ambassador page"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["problem-aware", "solution-aware"],
  "traffic": ["tiktok", "instagram", "influencer", "affiliate"],
  "sections": { "min": 6, "max": 9 },
  "mandatory_sections": ["hero", "product-spotlight", "ugc-grid", "closing-cta"],
  "recommended_sections": [["routine", "usage"], ["reviews", "review-summary"], "shop-the-look", "faq", "shipping-returns"],
  "forbidden_sections": ["header", "product-grid", "cross-sell", "countdown", "stock-indicator", "email-capture", "sms-capture", "quiz", "related-reads"],
  "nav": "none",
  "price_above_fold": "optional",
  "cta": { "min": 2, "max": 3, "first_after_section": 0, "sticky": "optional", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 3, "max_modules": 5, "required_kinds": ["creator-video", "policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["ugc", "identity", "in-use"], "hero": "video-poster", "video": "required", "min_images": 5 },
  "copy_framework": ["hook-story-offer", "bab", "fab"],
  "offer_compat": { "allowed": ["none", "percent-off", "fixed-off", "gwp", "free-shipping", "bundle", "first-order", "trial-sample", "limited-edition", "bnpl"], "forbidden": ["bogo", "tiered-volume", "bundle-decoy", "subscribe-save", "referral", "loyalty", "cashback", "mystery", "pre-order-price", "price-lock", "flash-sale", "clearance", "gift-card", "student-military", "charity"] },
  "urgency": "verified-only"
}
```

## Sources

- https://creatorcommerce.shop/brand-case-studies/cozy-earth
- https://creatorcommerce.shop/brand-blog/tiktok-shop-product-fit
- https://www.aspire.io/creatorstores
- https://d2c-times.com/is-superfiliate-the-creative-infrastructure-dtc-has-been-waiting-for-2/
- https://sproutsocial.com/insights/creator-storefronts/
- https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
- https://www.ascionline.in/social/wp-content/uploads/2025/04/ASCI-Influencer-Guidelines.pdf
- https://help.instagram.com/581066165581870/
- https://www.nosto.com/wp-content/uploads/2019/02/Stackla-Consumer-Marketer-Data-Report-2019_FINAL.pdf
- https://www.bazaarvoice.com/press/sei-2022-press-release/
- https://www.yotpo.com/blog/increase-conversion-rate-ecommerce/
- https://ads.tiktok.com/resources/help/article/ad-review-checklist-landing-page?lang=en
- https://hellofaceglobal.com/real-results/
