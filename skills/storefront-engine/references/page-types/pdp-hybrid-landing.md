# PDP hybrid landing

A product page's buy mechanics (gallery, buy box with variants, shipping line, reviews with distribution) wearing a landing page's discipline: no store navigation, an ad-matched headline, one goal. The visitor arrives from a paid click that already did some convincing, knows the category or the product, and needs to choose a variant and add to cart without leaving.

## Identify it

Signals in the brief:
- "Product page but for ads", "PDP with a story on top", "landing page that feels like a product page".
- One product with three or more variants (shade, size, flavour, tier) or a gallery that decides the sale.
- Traffic is meta with a demo or testimonial ad, or google-shopping where the feed image and price must match the page.
- Awareness solution-aware to product-aware; the ad or feed already named the product.

Near neighbours:
- `pdp`: choose it when traffic is organic, brand search, email or in-store navigation; the visitor expects the full store around the product.
- `ad-landing-page`: choose it when the product has one or two variants and the story matters more than the gallery.
- `retargeting-warm`: choose it when the visitor already viewed this product; objections before buy mechanics.
- `bundle-kit`: choose it when the value is the set rather than the product.

Baymard-grade buy-box requirements are house rule A8 in `references/design-rules.md`; the full PDP recipe is `references/generate-pdp.md`; Google Shopping feed matching is `references/traffic-source-google.md`. This file holds the contract.

## Variants

- **Search-intent PDP (google-shopping).** Slot 1 of the gallery is the feed image; title, price, currency and availability match the feed; correct variant pre-selected from the URL; Product and Offer JSON-LD in the initial HTML (LAW-adjacent: Merchant Center landing page policy, https://support.google.com/merchants/answer/4752265?hl=en). No message-match band; the product title is the H1.
- **Listicle-topped hybrid (Jones Road pattern).** Five short numbered reasons between the message-match band and the buy box, then the full PDP (https://www.jonesroadbeauty.com/pages/foundation-stick-performance). Reasons are `list-item` sections and count toward the section ceiling.

## Anatomy

1. `hero` mandatory. A compact message-match band, 120 to 220px on mobile: H1 restates the ad promise (not the product name), subhead names mechanism or outcome, `review-summary` when 5 or more reviews exist. No CTA here; the buy box follows immediately. For the search-intent variant this band collapses into the product title.
2. `gallery` mandatory. 5 to 8 images: identity, in-scale, in-hand or on-model, detail, variation per selected variant, ingredient or spec label where the vertical needs it; thumbnails visible, pinch zoom on mobile. 42% of users try to judge size from images (RESEARCH, Baymard, https://baymard.com/blog/current-state-ecommerce-product-page-ux).
3. `buy-box` mandatory. Untruncated title, rating and count, price and compare-at (ledger basis only), a two to four sentence story or mechanism block directly under the title, variant options as buttons with a one-line fit sentence per option where it helps (Jones Road shades, Wakefit tiers), quantity, add-to-cart, shipping and returns line, guarantee, payment options. Subscription toggle pre-selected only for consumables with cancellation terms beside it.
4. `trust-bar` recommended. Policy facts under the CTA; 13 of 15 PDPs in the teardowns carry trust chips here.
5. `benefits` mandatory. Three to six outcome-led items with a number, material, time or test each.
6. `mechanism` or `how-it-works` recommended. Why it works, with a diagram where one exists (Seed ViaCap pattern).
7. `ingredients`, `specs` or `materials` conditional: supplements, skincare, food, apparel fabric, electronics. Facts panel image for supplements (Baymard); supplier provenance where verified (Minimalist names Merck).
8. `before-after` conditional: substantiated, same subject and framing, consented, category permitted (`references/proof/before-after-and-claims.md`).
9. `expert-endorsement` recommended. Named person, credential line, written approval, connection disclosed.
10. `comparison` recommended. Us versus the category or intra-range tiers "right below the main description" (OPERATOR, RISE DTC, https://daily.risedtc.com/p/the-us-vs-them-comparison-chart).
11. `ugc-grid` recommended. 6 to 12 rights-cleared tiles; 67% of sites lack it and users seek unfiltered images (RESEARCH, Baymard, https://baymard.com/blog/integrate-social-media-visuals-on-product-page).
12. `reviews` mandatory. Distribution bars as filters at 20 or more reviews, photo reviews navigable, at least one critical review reachable without filtering (RESEARCH, Baymard, https://baymard.com/blog/allow-navigation-across-reviews-from-reviewer-images).
13. `cross-sell` conditional: a named relationship only ("Complete the routine", "Refill the stack"), two to three items with the fit reason beside each, below `reviews`, never before the buy box (`references/consumer-behavior-cro.md`).
14. `faq` recommended. Five to eight collapsed, objection-phrased ("Will it feel heavy or cakey?").
15. `closing-cta` mandatory. Repeats the add-to-cart with the guarantee; last-word quote above it.

Forbidden: `header` (logo only, not clickable), `product-grid`, `related-reads`, `email-capture`, `sms-capture`, `quiz`. Horizontal tab layouts that hide content fail Baymard's layout guidance and are not used. Index length 8 to 11; research allows 8 to 12; the index governs, so the listicle-topped variant caps reasons at three.

## Workflow

Assets first: the gallery is the sale on this type, so every gallery job is mapped before a word of copy exists, and every lower section gets a real image or is put to the merchant. Each Media line runs the loop in `references/workflows/section-asset-workflow.md` (sourcing: `references/assets/asset-sourcing-sequence.md`; jobs and vertical minimums: `references/assets/image-jobs-by-page-type.md` and `references/assets/imagery-by-vertical.md`, the higher number wins; ALLOW, ASK and NEVER: `references/assets/generation-policy.md`). Each Island line names the island and its decision inputs per `references/workflows/island-selection-workflow.md`; the catalog comes from `lexsis_design.islands` and the variant and props are resolved live from `lexsis_design.island_schema`.

Ask rule, used by every Media line below: tell the merchant what is missing (job, aspect, count), offer upload via `lexsis_asset_upload.upload` or MCP generation when the purpose is feasible under `references/assets/generation-policy.md`, and skip or merge the section only if the merchant chooses. In fast-draft, proceed with the closest existing asset or leave the slot `planned`, and list every missing asset in the plan and the draft summary.

### Context reads
1. `lexsis_catalog.get` with the product id: every media item mapped to a job (`identity`, `detail`, `scale`, `in-use`, `variation`, `included-items`, `label-or-facts-panel`), the current order, per-variant image mapping (a `variation` slot per variant that lacks one), variant axes and count (BuyBox variants carry no image, so colour-with-image needs VariantSwatches), price and compare-at (ledger basis), selling plans (a subscribe-save toggle only for consumables with cancellation terms, `references/offers/offer-types.md`), inventory (a stock line only from live data), and the exact title the feed uses.
2. Traffic source. Meta: `lexsis_campaigns.creatives`, `analyze` and `frames` give the H1 promise and the creative that becomes gallery slot one (`references/copy/message-match.md`). Google Shopping: no creative; the feed image, title, price and availability govern slot one and the H1 (`references/traffic-source-google.md`).
3. `lexsis_catalog.reviews_status`, `review_collections` (active), `reviews` (`product_id`, `limit: 100`, then per-star and `has_media`): band, distribution eligibility at 20 or more, one review of 3 stars or lower reachable, variant purchased where stored (`references/proof/reviews-sourcing.md`). `reviews_search` per benefit and objection.
4. `lexsis_brand.context` and `brand_kit` (`theme_id`): tokens, voice, policy facts, certifications and any expert endorsement records for the ledger. Skip `navigation`; nav is none.
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`: `product-shot`, `lifestyle`, `flat-lay`, `social-proof`, `before-after`, `logo`; then semantic per missing job. Count against the vertical gallery minimum before slots are created; view candidates with `lexsis_assets.view`.
6. `lexsis_workspace.credits` only if a `context` or backdrop slot remains open. The hero is a packshot type, so any generation sits below the fold and needs the ASK line in `generation-policy.md` section 4.

### Section by section
**`hero`**
- Purpose: a 120 to 220px message-match band: H1 restates the ad promise, one subhead, `review-summary`; no CTA, no image of its own.
- Media: no. The first gallery image directly below is the hero image; a band image would push price and add-to-cart below y=1266 at 390px. Search-intent variant: the band collapses into the product title.
- Island: `none`.
- Copy: H1 at most 10 words with 60% token overlap with the ad (`references/copy/message-match.md`); subhead one line; average plus n at band B2 or higher, "n reviews" at B1; no blacklist words (`references/anti-patterns/copy-anti-patterns.md`).
- Decide with: `lexsis_campaigns.analyze` for meta traffic; the feed title for Shopping traffic; the review band.

**`gallery`**
- Purpose: five to eight images that let the shopper judge identity, size, use, detail and their own variant.
- Media: yes; `identity` at slot one (the feed packshot for Shopping traffic; the ad creative at slot one and the packshot at slot two for meta traffic), then `scale`, `in-use` or on-model, `detail`, `variation` per selected variant, `label-or-facts-panel` or `ingredient-or-material` where the vertical needs it, a demo video at slot two or three with a real poster (`references/assets/video-rules.md`). Search: catalog media, then library `product-shot` and `lifestyle`, then semantic per job, then merchant or supplier upload. Nothing found below the vertical minimum: ask rule naming each missing job and count; no generation is feasible in the gallery (GP11, GN12); the gallery ships with verified images only, no placeholder. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used. The ad creative at slot one is the clean original, not the exported ad with baked-in text, and its SKU, variant and angle are confirmed by eye against the feed or creative; view the gallery candidates together so they read as one shoot. `lexsis_asset_library.search` with `mode: "ocr"` flags library candidates that carry baked-in text before they are viewed.
- Island: `ProductGallery`, or `ProductHero` in a split layout beside the buy box for fashion, furniture and premium goods where media should take 50 to 60% of desktop width; decide layout, thumbnails, mobile behaviour and lightbox from the image count, the vertical and whether colour variants carry images (variant sync on when VariantSwatches is present); autoplay and transitions off unless the plan names the motion moment (N10). Resolve variant and props from `lexsis_design.island_schema`; presets `productgallery/rail-bottom-light`, `productgallery/rail-left-editorial`, `producthero/split-rail-light`.
- Copy: alt per slot from the slot template in `references/assets/slot-spec.md`; thumbnails all visible up to 10 to 14, then an explicit "+N".
- Decide with: image count against the vertical minimum; variant image mapping; traffic source.

**`buy-box`**
- Purpose: untruncated title, rating and count, price and compare-at, a two to four sentence story block, variant buttons with a fit sentence, quantity, add-to-cart, shipping and returns line, guarantee, payment options.
- Media: the gallery above supplies it; `swatch` images per colour variant from catalog media or library (flat CSS chips only beside a real swatch). Nothing found: ask rule; no generation is feasible for swatches. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: `BuyBox`, one per page; decide its form from the variant count and axes and whether the page has its own icon set. `VariantSwatches` when colour or shade variants carry images (the fit sentence per option is HTML beside it). `DeliveryEstimate` for the dispatch cutoff (India pincode copy is static HTML). `InventoryIndicator` only when bound to live inventory. `StickyBar` bound to the buy section when the page runs past three viewports; it has no variant sync, so it carries a variant only when one is pre-selected and otherwise links back to the buy box. Resolve variant and props from `lexsis_design.island_schema`; presets `buybox/default-light`, `deliveryestimate/inline-quiet`, `inventoryindicator/text-quiet`, `stickybar/product-light`.
- Copy: `bab` intro at most 60 words; "Add to cart" or "Add to bag" for fashion and beauty; per-serving or per-day line only when arithmetically true; subscribe-save copy shows renewal price and cancellation terms beside the toggle (`references/offers/offer-types.md`).
- Decide with: variant axes and images, selling plans, inventory, offer ledger rows, page length.

**`trust-bar`**
- Purpose: policy facts under the add-to-cart.
- Media: no photography; payment or certification marks only as issuer artwork with a ledger row (`references/proof/press-and-media-mentions.md` for any press). Nothing found: ask rule; generation is not feasible for badges (GN5). Any logo or mark is still opened with `lexsis_assets.view` before use.
- Island: `none`; a static HTML row (Marquee is deprecated).
- Copy: three or four facts, at most six words each.
- Decide with: policy URLs and certification rows in the ledger.

**`benefits`**
- Purpose: three to six outcomes with a number, material, time or test.
- Media: yes; one image per benefit with the product present (`detail`, `in-use`, `scale`, `included-items`), reusing gallery images at a different crop only once. Search: catalog media, then library `product-shot` and `lifestyle`, then semantic, then merchant upload. Nothing found for a benefit: ask rule; feasible purpose `product_composite` for a `context` benefit only; a benefit merges only on the merchant's choice. No-go: icon tiles, emoji, generated in-use. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: `none`.
- Copy: `fab`; subhead at most 8 words; body at most 25 words.
- Decide with: the job map; one slot per benefit.

**`mechanism`** or **`how-it-works`**
- Purpose: why it works, with a diagram where one exists.
- Media: yes; `diagram` as authored inline SVG with numbers in HTML, or `sequence` of real step photos. Search: catalog media, then library, then merchant or supplier upload, then author the SVG. Nothing found: ask rule; generation is not feasible for steps or a raster diagram; the authored SVG carries the section meanwhile. No-go: stock lab imagery, three icon tiles. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: `none`; `VideoPlayer` only when a real 45 to 90 second demo exists and is not already in the gallery, click to play with a real poster; resolve variant and props from `lexsis_design.island_schema`.
- Copy: three steps, at most 25 words each; study n and design disclosed beside any statistic.
- Decide with: `test-data` ledger rows; catalog coverage of `sequence`.

**`ingredients`**, **`specs`** or **`materials`** (conditional: supplements, skincare, food, apparel, electronics)
- Purpose: what it is made of, as facts.
- Media: yes; `label-or-facts-panel` as a legible real photo (1600px or more) with the same figures in HTML, or `ingredient-or-material` flat lay, or a `detail` macro of fabric or ports. Search: catalog media, then library `flat-lay` and `product-shot`, then supplier upload with a licence. Nothing found: ask rule; generation is not feasible (GN6, GN11); the panel is an HTML table meanwhile. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: `none`; the table is HTML (Tabs is deprecated and horizontal tabs are forbidden on this type).
- Copy: every number in HTML matches the label; supplier provenance only where verified.
- Decide with: the vertical row in `imagery-by-vertical.md`; ledger rows.

**`before-after`** (conditional: substantiated, consented, category permitted)
- Purpose: a genuine result pair for a results objection.
- Media: yes; a verified `before-after` ledger row with the same subject, crop and lighting, interval stated in HTML. Search: library tag `before-after` with a `P` row, then merchant upload with consent on file. Nothing found: ask rule, naming the consent and substantiation the pair needs; generation is never feasible (GN4); the section exists only with a verified row and never in the hero. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: `BeforeAfter` when both images share one aspect ratio, static side-by-side otherwise; resolve variant and props from `lexsis_design.island_schema`.
- Copy: "Before" and "After" with the interval; "Individual results vary" where the category requires it.
- Decide with: `references/proof/before-after-and-claims.md`; the `P` row status.

**`expert-endorsement`**
- Purpose: a named person with a credential and disclosed connection.
- Media: yes; `founder-or-team` portrait of the named expert (real, consented) from the library or merchant upload. Nothing found: ask rule; generation is never feasible for people (GN3); the quote runs with the credential line as text meanwhile. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: `none`.
- Copy: quote at most 60 words; name, credential, connection disclosed.
- Decide with: the `expert-quote` ledger row with written approval.

**`comparison`**
- Purpose: us versus the category, or the merchant's own tiers, right below the description.
- Media: one `comparison-visual` of our attribute physically; the alternative is an inline SVG silhouette. Search: catalog `detail` or `scale`, then library, then merchant upload. Nothing found: ask rule; generation is not feasible (GN8); the table stands with our identity image in the header meanwhile. No-go: competitor photos, tick grids without a concession row. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: `none`; a static HTML table.
- Copy: four to six rows, cells at most 6 words.
- Decide with: `test-data` rows per cell.

**`ugc-grid`**
- Purpose: six to twelve rights-cleared customer tiles, uniform aspect, handles visible.
- Media: yes; `ugc` from `reviews` with `has_media: true` and library `social-proof`, each with a `P` row; crop only, original grading (`references/proof/ugc-rights-and-display.md`). Fewer than six: ask rule naming the count and the rights record each tile needs; generation is never feasible (GN9); a smaller grid or none only on the merchant's call. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: `none` for a static grid of stills; `ShoppableVideoFeed` when the tiles are 9:16 clips with the product tagged, posters on every item; resolve variant and props from `lexsis_design.island_schema`.
- Copy: "Customer photos" label; first name or handle when permitted.
- Decide with: `has_media` count; UGC ledger rows.

**`reviews`**
- Purpose: the full module with distribution and filters, one critical review reachable.
- Media: photo reviews navigable (`review-with-media`); avatars real or CSS initials, never generated. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: by band per `references/proof/reviews-sourcing.md`. B1: static cards. B2: `ReviewCarousel` bound to the product id or an active collection, autoplay off (its default is on, N10); preset `reviewcarousel/grid-flat`. B3 and B4: `ReviewList` with sort and filters, media on, totals from the API total, layout decided by whether the store holds demographics; no rating filter on the list. Resolve variant and props from `lexsis_design.island_schema`. B0: `guarantee`, `certifications` and product evidence replace it and the omission is recorded.
- Copy: verbatim, dated, variant purchased where stored; one 3-star or lower visible by default at 20 or more.
- Decide with: `reviews_status`, per-star counts, `has_media`.

**`cross-sell`** (conditional: a named relationship, below `reviews`)
- Purpose: two or three items that complete the routine, each with its fit reason.
- Media: yes; one catalog `identity` image per item via `lexsis_catalog.get`. Nothing found: ask rule; no generation is feasible for identity. View every candidate with `lexsis_assets.view` and run the fit review in `references/workflows/section-asset-workflow.md` section 1b (subject, crop, quiet zone for the copy, consistency with neighbouring slots, palette, no baked-in text or watermark) before it is used.
- Island: `QuickAdd` per card when the page runs cart v2 and the items need a variant picker, links to the PDPs otherwise; `ProductCarousel` only at four or more items, entry animation off unless the plan names it (N10). Resolve variant and props from `lexsis_design.island_schema`.
- Copy: the relationship named ("Complete the routine"); one fit sentence per item.
- Decide with: catalog relationships the merchant confirms.

**`faq`**
- Purpose: five to eight objection-phrased questions, collapsed.
- Media: no.
- Island: `none`; native `<details>` and `<summary>` (the FAQ island is deprecated).
- Copy: answers at most 60 words; "Will it feel heavy or cakey?" phrasing.
- Decide with: `reviews_search` on objection topics.

**`closing-cta`**
- Purpose: repeat add-to-cart with the guarantee; last-word quote above.
- Media: optional reuse of a verified `in-use` slot; no new job, no generation.
- Island: `none`; the CTA anchors to the buy box.
- Copy: same verb and object as the buy box.
- Decide with: the last-word `review-quote` row.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media (N images) | `identity`, `variation`, `detail`, often `label-or-facts-panel` | `scale`, on-model `in-use`, `included-items`, a variant image for every variant | ask the merchant to upload (identity-bound, no generation); the gallery ships with verified images only and the vertical minimum is recorded as unmet |
| asset library | `product-shot`, `lifestyle`, `social-proof` with rights, `before-after` with a `P` row | in-use of this exact variant | tag search, then semantic; view before assigning; UGC only with a `P` row |
| ad creatives | gallery slot one for meta traffic, the H1 promise | anything below the gallery | import the brand-owned frame with `lexsis_asset_import.import`; Shopping traffic uses the feed image instead |
| generation | `product_composite` for a `context` benefit, `texture_fill`; backdrops only below the fold and only after the ASK line for packshot heroes | product, people, results, labels, logos, text | never; ask the merchant to upload instead |

With only a packshot and one variant image the page still ships as gallery, buy box, trust bar, benefits around the packshot, reviews at any band above B0, faq and closing; `mechanism`, `ingredients`, `before-after`, `expert-endorsement`, `comparison`, `ugc-grid` and `cross-sell` are listed as missing assets with the upload offer and leave the page only on the merchant's decision. Generated assets: at most four per page, usually zero on this type. Nothing is used sight unseen: every asset in this table is opened with `lexsis_assets.view` and passes the section 1b fit review before it is assigned.

## Above the fold (390px)

Visible, in order:
1. Logo (not clickable).
2. Message-match H1, at most 10 words, and a one-line subhead.
3. `review-summary` (average plus n) or "n reviews" text.
4. First gallery image (4:5 or 1:1) with visible thumbnail cues; for google-shopping traffic this is the feed packshot, for meta traffic the ad creative with the packshot at slot 2.
5. Product title and price with compare-at.

Within 1.5 viewports (price and add-to-cart above y=1266px at 390px, per design-rules A8): variant buttons, quantity, add-to-cart, shipping and returns line. On desktop the buy section fits the first viewport and media takes 50 to 60% of the width.

Must not appear: a hero CTA that competes with add-to-cart, a countdown, a stock count, a promo bar stack (one `announcement` at most), an email popup, a carousel that hides the price, autoplay video with sound, a second product.

## Proof

Density: 2 to 4 modules (index). Research minimum for a PDP: star summary near the title, a reviews module with distribution and filters, a policy fact at add-to-cart (internal teardown audit, 2026-09-10).

| Kind | Where | Minimum evidence |
|---|---|---|
| `review-summary` | `hero` band and `buy-box` | 5 or more reviews for an average with n; count only at 1 to 4; distribution at 20 or more |
| `review-list` or `review-with-media` | `reviews` | verbatim, dated, attribution as stored, variant purchased where stored ("Reviewing: Carbon"); one 3-star or lower reachable |
| `policy-fact` or `guarantee` | `buy-box`, `trust-bar` | policy page URL, exact terms |
| `ugc-photo` | `ugc-grid` | rights record, handle |
| `expert-quote` | `expert-endorsement` | named, credential, approval, connection disclosed |
| `test-data` or `certification` | beside the claim in `mechanism` or `ingredients` | report or issuer on file; study n and design disclosed (AG1 pattern) |

Placement: PDPs front-load a number (rating in the top 20%) and back-load the evidence (full widget at 80 to 100%) in 12 of 15 teardowns; keep one inline quote beside the strongest benefit at 40 to 60% so the middle is not proof-free. Forbidden kinds: `social-proof-popup`, `live-viewer-count`, `press-logo-unlinked`. Cart-velocity lines ("21,100 added this week") render only from a live binding, never static.

Zero reviews: `references/proof/reviews-sourcing.md` tiers 4 and 5. Replace `reviews` with `guarantee`, `certifications` and product evidence; record the omission. A considered purchase with no proof at all (Mokobara teardown) is the failure to avoid, so the substitutes are mandatory when reviews are absent.

## Offer and CTA

- CTA count: 2 to 3. Add-to-cart in the buy box; a repeat after `reviews` when the page exceeds three viewports; the closing CTA. Same verb and object every time. A sticky bar is chrome and does not count.
- First CTA: the buy box, section 3 (`first_after_section: 2`). The message-match band carries no button.
- Sticky: optional, recommended when the page runs past three viewports. Appears only after the buy box scrolls out, 56 to 64px, carries thumbnail, price, selected variant, one button; opens the real variant picker when none is chosen; never auto-adds a default variant (OPERATOR, https://revenueflows.ai/blog/do-sticky-add-to-cart-buttons-increase-shopify-conversion-rate). Short pages under three viewports gain little.
- Copy pattern: `add-to-cart` ("Add to cart", "Add to bag" for fashion and beauty), price in the label where space allows. Express pay buttons may sit beside it; no "Buy now" text button.
- Price reveal: immediately, in the buy box, tax-inclusive wording per market; per-serving or per-day line when arithmetically true (Huel "$2.65 per meal", https://huel.com/products/huel-black-edition).
- Offer fit: `none`, `free-shipping`, `gwp`, `bundle` (below the buy box with savings math), `subscribe-save` (toggle with cancellation terms), `first-order`. `percent-off` and `fixed-off` only with a verified compare-at basis; `bogo` and `tiered-volume` for consumables with a `quantity-breaks` section (offer-types OF4); `bnpl` on goods over about $80 or 3,000 rupees; `cashback` for India bank offers; `limited-edition` when the edition cap is documented.
- Offer misfit: `flash-sale` and `clearance` belong to `sale-clearance-flash`; `referral`, `loyalty`, `gift-card`, `student-military`, `mystery`, `pre-order-price`, `price-lock`, `bundle-decoy` and `charity` change the page's job. The table in `references/offers/offer-types.md` governs.
- Urgency: `verified-only`. Dispatch cutoff between price and add-to-cart is the default; a countdown only bound to `offer.endsAt` in the final 48 hours; a stock line only from live inventory. Never in the message-match band.

## Imagery

Required jobs: `identity`, `detail`, `scale`, `in-use`, `variation` (when variants exist). Strongly recommended: `ugc`, `included-items`, `ingredient-or-material` or `label-or-facts-panel` by vertical, `sequence` for how-to.
- Hero: `packshot` at gallery slot 1 for google-shopping traffic (feed match); meta traffic swaps slot 1 to the ad creative (`product-in-context` or `product-in-hand`) and keeps the packshot at slot 2. Video sits at gallery slot 2 or 3 with a poster and play badge, never autoplay with sound (RESEARCH, Baymard, https://baymard.com/blog/embedding-product-page-videos).
- Balance: by vertical from `references/assets/image-jobs-by-page-type.md`; default supplements 50:35:15 studio to lifestyle to UGC, beauty 35:45:20, apparel 30:50:20.
- Video: optional; 45 to 90 seconds demo, captions, click to play.
- Minimum images: 5 (6 beauty plus one per shade shown on skin, 7 home and electronics, 8 apparel).
- Slots the plan must create: gallery of 5 to 8 with the jobs above; variant images that swap on selection; mechanism `diagram` where a mechanism section exists; UGC grid of 6 to 12 when rights exist; comparison visual when a `comparison` section exists. Never generate a replacement identity image when verified Shopify media exists.

## Copy

- Framework: `bab` for the two to four sentence hybrid intro under the title; `fab` for the description, bullets and specs; `4ps` for the below-fold argument (promise, picture, proof, push).
- Headline by awareness: solution-aware leads with result plus mechanism ("Foundation coverage without the foundation feel"); product-aware leads with product plus strongest verified claim or the ad's promise verbatim. Search-intent variant: the product title is the H1, in the feed's words.
- Message match (mandatory for meta traffic): H1 shares the ad headline's promise (60% token overlap or the identical claim rephrased no longer); same variant in slot 1 of the gallery; same offer; same CTA verb (`references/copy/message-match.md`). For google-shopping traffic the match is to the feed: title, image, price, availability.
- Reading level: grade 6 to 8. Subtitle may carry the two or three decision specs ("42 hours playback, ENx, 5-minute charge"); each spec verified.
- Length ceilings: H1 10 words; intro block 60 words; each benefit 25 words; description 150 words before disclosure; each FAQ answer 60; total 500 to 1,200 words excluding reviews.
- Vocabulary: variant options carry a fit sentence in plain words ("for fair to medium skin tones"); routine duration stated where results take time ("start alternate days, then daily after two weeks"); no blacklist words; sentence case; product names keep brand casing.

## Never

- Never render store navigation, a mega menu, search or footer link columns.
- Never place price or add-to-cart below y=1266px at 390px or below the first viewport on desktop.
- Never show two different star averages on one page (Jones Road hybrid shows 4.88 in the hero and 4.61 in the module).
- Never auto-add a default variant from a sticky bar.
- Never hide benefits, ingredients or reviews behind horizontal tabs.
- Never stack more than one announcement bar or more than one code offer.
- Never place a cross-sell strip before the reviews module or without a named relationship.
- Never show a compare-at price without a ledger basis, or a discount pill in ALL-CAPS (design-rules N9).
- Never show a countdown or stock count in the message-match band or the gallery.
- Never let the message-match band carry its own CTA.
- Never show an average with fewer than 5 reviews or a distribution with fewer than 20.
- Never use a hero video as the LCP element or autoplay with sound.

## Examples

- Jones Road "Your Skin Foundation Stick" performance page: benefit headline with a press quote strip, five short reasons, then a full embedded buy box with 30 shades each carrying a fit sentence, objection-phrased FAQ (https://www.jonesroadbeauty.com/pages/foundation-stick-performance).
- Seed DS-01: one-sentence claim, price, subscription microcopy, "Start now", guarantee line all above the fold; mechanism diagram; us-versus-category table; FAQ that answers "do I have to subscribe" head-on (https://seed.com/daily-synbiotic).
- Wakefit ShapeSense Ortho: gallery with trial, shipping and warranty badges, 454k ratings beside the title, four tiers each with a one-line who-it-is-for, size-confirmation nudge under add-to-cart (https://www.wakefit.co/mattress/orthopaedic-memory-foam-mattress/WOMFM72366).

## Checklist

```json
{
  "page_type": "pdp-hybrid-landing",
  "aliases": ["hybrid PDP", "PDP landing page", "product page for ads", "search-intent PDP", "feed landing page"],
  "funnel_stage": ["mof"],
  "awareness": ["solution-aware", "product-aware"],
  "traffic": ["meta", "google-shopping"],
  "sections": { "min": 8, "max": 11 },
  "mandatory_sections": ["hero", "gallery", "buy-box", "benefits", "reviews", "closing-cta"],
  "recommended_sections": ["trust-bar", ["mechanism", "how-it-works"], ["ingredients", "specs", "materials"], "expert-endorsement", "comparison", "ugc-grid", "faq"],
  "forbidden_sections": ["header", "product-grid", "related-reads", "email-capture", "sms-capture", "quiz"],
  "nav": "none",
  "price_above_fold": "required",
  "cta": { "min": 2, "max": 3, "first_after_section": 2, "sticky": "optional", "copy_pattern": "add-to-cart" },
  "proof": { "min_modules": 2, "max_modules": 4, "required_kinds": ["review-summary", "policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["identity", "detail", "scale", "in-use", "variation"], "hero": "packshot", "video": "optional", "min_images": 5 },
  "copy_framework": ["bab", "fab", "4ps"],
  "offer_compat": { "allowed": ["none", "free-shipping", "gwp", "bundle", "subscribe-save", "first-order", "percent-off", "fixed-off", "bogo", "tiered-volume", "bnpl", "cashback", "limited-edition"], "forbidden": ["bundle-decoy", "referral", "loyalty", "mystery", "pre-order-price", "price-lock", "flash-sale", "clearance", "gift-card", "student-military", "charity"] },
  "urgency": "verified-only"
}
```

## Sources

- https://baymard.com/research/product-page
- https://baymard.com/blog/current-state-ecommerce-product-page-ux
- https://baymard.com/blog/user-ratings-distribution-summary
- https://baymard.com/blog/allow-navigation-across-reviews-from-reviewer-images
- https://baymard.com/blog/integrate-social-media-visuals-on-product-page
- https://baymard.com/blog/embedding-product-page-videos
- https://support.google.com/merchants/answer/4752265?hl=en
- https://support.google.com/merchants/answer/7331077?hl=en
- https://daily.risedtc.com/p/the-us-vs-them-comparison-chart
- https://revenueflows.ai/blog/do-sticky-add-to-cart-buttons-increase-shopify-conversion-rate
- https://zerglo.com/us/blog/pdp-conversion-subscriptions
- https://www.replo.app/use-case/skincare-pdp
- https://www.jonesroadbeauty.com/pages/foundation-stick-performance
- https://seed.com/daily-synbiotic
- https://huel.com/products/huel-black-edition
- https://www.wakefit.co/mattress/orthopaedic-memory-foam-mattress/WOMFM72366
