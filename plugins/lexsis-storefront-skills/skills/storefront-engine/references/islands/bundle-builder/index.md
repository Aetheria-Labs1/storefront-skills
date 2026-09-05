# Bundle Builder — Island Directory

Interactive bundle creation island for product bundles with tiered discounts.

## Files

| File | Purpose |
|------|---------|
| `layouts/step-based.json` | Full section with step progress (Choose, Review, Checkout) |
| `layouts/horizontal.json` | Single row: product grid + bundle summary sidebar |
| `layouts/compact.json` | Inline bundle widget for embedding in PDP as upsell |

## Quick Reference

- **Variants**: horizontal, stacked
- **Required prop**: `productIds` (JSON array of Shopify GIDs)
- **Schema**: `vibe://schema/island/BundleBuilder`
- **Layouts**: `vibe://islands/bundle-builder/layouts/{name}`
- **Contract**: follows `_contract.md`

## Composition

- Pair with: BuyBox (on PDP for upsell), TrustBadgeBar, ProductGallery
- Step-based layout is a standalone section (full-width, dedicated page area)
- Horizontal layout works as mid-page section between product details and reviews
- Compact layout embeds inline within other sections (e.g., below BuyBox)
- Discount tier display should be visible before user starts selecting products
- Template vars: `{{PRODUCT_IDS}}` (JSON array), `{{DISCOUNT_TIERS}}` (JSON), `{{CTA_TEXT}}`
