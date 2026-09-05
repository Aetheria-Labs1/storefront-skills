# Bundle Builder — Island Directory

Interactive bundle creation island for product bundles with tiered discounts.

## Quick Reference

- **Variants**: horizontal, stacked
- **Required prop**: `productIds` (JSON array of Shopify GIDs)
- **Schema**: `vibe://schema/island/BundleBuilder`
- **Contract**: follows `_contract.md`

## Composition

- Pair with: BuyBox (on PDP for upsell), TrustBadgeBar, ProductGallery
- Step-based layout is a standalone section (full-width, dedicated page area)
- Horizontal layout works as mid-page section between product details and reviews
- Compact layout embeds inline within other sections (e.g., below BuyBox)
- Discount tier display should be visible before user starts selecting products
- Template vars: `{{PRODUCT_IDS}}` (JSON array), `{{DISCOUNT_TIERS}}` (JSON), `{{CTA_TEXT}}`
