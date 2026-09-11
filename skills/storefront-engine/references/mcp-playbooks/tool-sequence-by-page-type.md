# Extra MCP Calls by Page Type

`tool-sequence-by-stage.md` is the base sequence. Each page type adds the
calls below, in the stage where they belong. Ids refer to
`references/page-types/<file>.md`.

| Page type | Plan-stage additions | Design-stage additions | Skip |
|---|---|---|---|
| `ad-landing-page` | `lexsis_campaigns.creatives` U+2192 `.analyze` (or view the creative) U+2192 `.match_persona`; `lexsis_catalog.reviews_search` with the ad's main claim | `lexsis_design.island_schema` for BuyBox, StickyBar, ReviewCarousel; FAQ as native details | `lexsis_brand.navigation` (no nav) |
| `pdp` | `lexsis_catalog.get` with every variant; `lexsis_catalog.reviews` per product with `has_media: true` | schemas for ProductGallery, BuyBox or ProductHero, VariantSwatches, SizeGuide, ReviewList or ReviewCarousel, StickyBar, DeliveryEstimate; FAQ as native details | `lexsis_campaigns.*` unless ad-driven |
| `pdp-hybrid-landing` | as `ad-landing-page` plus `pdp` | as `pdp` | nav |
| `advertorial` | `lexsis_campaigns.analyze`; `lexsis_catalog.reviews_search` for each narrative claim; `lexsis_campaigns.personas` | one BuyBox or a linked offer bridge only; no gallery island | StickyBar in the first half, CountdownTimer |
| `listicle` | `lexsis_catalog.list` for every featured product; `lexsis_brand.navigation` for internal links | QuickAdd or ProductCarousel per item; comparison table and FAQ as static HTML | countdown |
| `comparison-us-vs-them` | `lexsis_catalog.get` for spec facts; merchant-confirmed competitor facts with source URLs | static comparison table; BuyBox | competitor logos or product photos |
| `quiz-funnel` | `lexsis_capture.funnel_templates` U+2192 `.funnel_template`; `lexsis_capture.form_schemas` | `lexsis_drafts.funnel_create` U+2192 `lexsis_capture.validate_funnel` U+2192 `.preview_funnel`; FunnelRuntime island | BuyBox above the quiz |
| `bundle-kit` | `lexsis_catalog.get` for each component; verified bundle price and savings math | BundleBuilder or QuantityBreaks, PlanSelector, BuyBox | percent-off pills |
| `offer-page` | offer ledger items confirmed with the merchant; `lexsis_cart.get` for discount behaviour | BuyBox with the offer, CartDiscountInput only if a code is required, CountdownTimer only with a verified end | reset timers |
| `sale-clearance-flash` | verified end date and stock; `lexsis_catalog.list` filtered to sale items | product grid composition (`references/product-grid.md`) with compare-at, CountdownTimer (verified), InventoryIndicator (verified) | fabricated stock counts |
| `seasonal-gifting` | delivery cutoffs and gift options confirmed; `lexsis_catalog.list` for the gift set | product grid or ProductCarousel by recipient or price band, DeliveryEstimate, gift-note field via cart profile | countdown without a real cutoff |
| `launch-waitlist-preorder` | `lexsis_capture.form_schemas`; ship date and pre-order terms confirmed | EmailCapture (waitlist), BuyBox only when pre-order is live | reviews for a product with none (use founder note, test data) |
| `restock` | `lexsis_catalog.get` inventory; past review data | BuyBox, ReviewCarousel, InventoryIndicator (verified) | urgency copy beyond real stock |
| `subscription` | `lexsis_catalog.get` selling plans; cancellation terms confirmed | SubscriptionToggle, PlanSelector; FAQ as native details with the cancellation answer first | hidden recurring terms |
| `ugc-creator-collab` | `lexsis_campaigns.creatives` for the creator's content; usage rights confirmed | ShoppableVideoFeed or VideoPlayer, ReviewCarousel, BuyBox | studio imagery in the hero |
| `video-sales-page` | video asset in the library; transcript for captions | VideoPlayer (click-to-play, captions), BuyBox after the video; FAQ as native details | autoplay with sound |
| `brand-story-founder` | `lexsis_brand.brand_kit` voice; founder facts confirmed | EmailCapture, ProductCarousel at the end | discounts, countdowns |
| `ingredient-science` | ingredient facts, studies with URLs, certifications confirmed | IngredientExplorer, BuyBox; tabs and FAQ as static HTML | unsupported clinical claims |
| `collection-landing` | `lexsis_catalog.list` for the collection; `lexsis_brand.navigation` | product grid with QuickAdd, filter UI, EmailCapture | hero taller than one screen |
| `homepage` | `lexsis_brand.navigation`; `lexsis_catalog.list` best sellers; `lexsis_catalog.reviews` | SiteHeader or Navbar, FeaturedCollectionStage, ProductCarousel, ReviewCarousel, EmailCapture, Footer | ad-style urgency |
| `lookbook-shop-the-look` | `lexsis_catalog.get` per look item | GalleryLightbox, QuickAdd, ProductCarousel | walls of text |
| `gift-guide` | recipient personas; price bands; delivery cutoffs | product grid per band, CSS tabs by recipient, DeliveryEstimate | one undifferentiated grid |
| `lead-capture-giveaway` | `lexsis_capture.form_schemas`; incentive and terms confirmed | EmailCapture, Modal only as exit intent | popups within 10 seconds |
| `referral-loyalty-vip` | programme terms confirmed | EmailCapture or a FunnelRuntime form; tier table as static HTML | invented member counts |
| `retargeting-warm` | analytics: `lexsis_analytics.page` for the source page; objection list | BuyBox early, native-details FAQ early, ReviewCarousel | re-explaining the product |
| `thank-you-post-purchase` | `lexsis_catalog.get` for cross-sell; delivery expectations | ProductCarousel with a named relationship, EmailCapture for referral | full navigation |
| `faq-support-led` | policies and answers confirmed | native details FAQ groups, CSS tabs, DeliveryEstimate | hard-sell CTA blocks |
| `trial-sample` | trial terms, shipping fee, conversion terms confirmed | BuyBox for the trial SKU; native-details FAQ with "what happens after" first | hidden auto-renew |
| `wholesale-b2b` | MOQ, pricing tiers, lead times confirmed | EmailCapture or FunnelRuntime form; specs as CSS tabs; downloadable line sheet | consumer urgency |

Rules:

1. Add only the rows for the type recorded in `page.pageType`.
2. Every "confirmed" item is a `## Offer ledger` or `## Proof ledger` row in
   `page plan` before design begins.
3. When a listed island's schema says `deprecated`, use its replacement.
