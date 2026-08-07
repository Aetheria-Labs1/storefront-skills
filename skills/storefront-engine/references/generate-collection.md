# Collection / Category Page Generation

> Reference: `vibe://docs/generation-guide` | `vibe://skills/generation-protocol`
> **Workflow:** See `generation-protocol.md` for Phases 1-5 execution (context gathering, HTML generation, validation, publishing). This doc covers page-type-specific patterns only.

Generate browsable product listing pages. Grid-focused with EditorialProductGrid island. Quick-add buttons add +15% add-to-cart from grid. Consistent card aspect ratios prevent layout shift. Mid-grid promotional cards every 6-8 products drive AOV.

## Triggers

"collection page", "category page", "product grid", "shop all", "PLP", "product listing"

## CRO-Backed Section Ordering

```
1. Navbar/SiteHeader   — full navigation + breadcrumb (REQUIRED island)
2. Hero Banner         — collection title + description (max 300px desktop, 200px mobile)
3. Filter/Sort Bar     — collapsible sidebar desktop, bottom sheet mobile
4. Product Grid        — EditorialProductGrid island (the star of the page)
5. Mid-Grid Promo      — promotional card every 6-8 products
6. Social Proof        — compact trust bar below grid
7. Newsletter          — compact single-line signup
8. Footer              — full nav + payment icons (REQUIRED island)
```

## Page-Specific Context Calls

After the standard 4 context calls, also fetch:
```
get_navigation          → navbar/footer links, collection hierarchy, breadcrumb
list_products           → all products in target collection (titles, prices, images, variants, tags)
```

Critical extractions from `list_products`:
- Product count (determines pagination: "Load More" at 12+ products)
- Available filter dimensions: price range, product type, color, size, tags
- Variant data per product (for color swatches on cards)
- Sale/compare-at prices (for badge display)

## Page-Specific Rules

- Grid is the STAR — hero banner stays short (max 300px desktop, 200px mobile)
- Tighter section padding than other page types: `py-8 md:py-12`
- Consistent card aspect ratios (1:1 or 3:4) with `object-fit: cover`
- Product titles truncated to 2 lines max (prevent layout break)
- Price always visible on card (never hidden behind interaction)

## Required Islands

| Island | Placement | Props Source |
|--------|-----------|-------------|
| **SiteHeader** (REQUIRED) | Section 1 | `get_navigation` → links[], logo |
| **EditorialProductGrid** (REQUIRED) | Section 4 | `list_products` → products array |
| **Footer** (REQUIRED) | Section 8 | `get_navigation` → footer links |

```html
<!-- EditorialProductGrid -->
<div data-island="EditorialProductGrid" data-props='{"products":[{"id":"p1","title":"...","price":"$29.99","compareAtPrice":"$39.99","image":"...","secondImage":"...","variants":[{"color":"Black","swatch":"#000"},{"color":"White","swatch":"#fff"}],"badge":"Sale","quickAdd":true}],"columns":{"mobile":2,"tablet":3,"desktop":4},"quickAddEnabled":true,"promoCard":{"position":7,"title":"Buy 2, Get 1 Free","image":"...","href":"/collections/bundles"}}'></div>
```

Use `vibe://schema/island/EditorialProductGrid` for exact prop shape.

## Responsive Grid Columns

| Viewport | Columns | Card Min Width | Gap |
|----------|---------|----------------|-----|
| Mobile (< 640px) | 2 | ~160px | 12px |
| Tablet (640-1024px) | 3 | ~200px | 16px |
| Desktop (> 1024px) | 4 | ~280px | 20px |

## Product Card Anatomy

Every card MUST include:
1. **Image** — consistent aspect ratio (3:4 recommended), `object-fit: cover`
2. **Hover image** — second product image on hover (desktop only)
3. **Title** — truncated to 2 lines, `--lx-font-heading`
4. **Price** — always visible; if on sale: `<s>$39.99</s> $29.99` in accent color
5. **Color swatches** — small dots if product has color variants (max 5 visible + "+3")
6. **Quick-add button** — appears on hover (desktop) or always visible (mobile)
7. **Badge** — "New", "Sale", "Bestseller" positioned top-left

### Quick-Add Behavior (+15% add-to-cart from grid)
- Single-variant products: "Add to Cart" button adds directly
- Multi-variant products: "Choose Options" links to PDP
- On success: "Added!" micro-feedback animation (checkmark morph, 300ms)
- Never interrupt browsing with full-page redirects

## Mid-Grid Promotional Card

Insert after every 6-8 products (spans full grid width):
- Brand accent color background (`--lx-accent-color`)
- Promotional message: bundle deal, free shipping threshold, seasonal sale
- Single CTA button with contrasting color
- Different visual weight from product cards (clearly promotional, not confusable)

Example placements:
- Position 7: "Buy 2, Get 1 Free" bundle promo
- Position 14: "Free shipping on orders over $75" threshold nudge
- Position 21: "Subscribe & Save 20%" for consumables

## Filtering UX

### Desktop — Collapsible Sidebar
- Left sidebar (240px width) with filter groups
- Each group expandable/collapsible (accordion pattern)
- Active filters shown as removable chips above grid
- "Clear All" link when filters active
- Product count updates: "Showing 12 of 48 products"

### Mobile — Bottom Sheet
- "Filter" button in sticky bar triggers bottom sheet modal
- Full-screen overlay with filter groups
- "Apply Filters (12)" button shows result count
- "Clear" link in sheet header
- Sort dropdown: separate from filters, always accessible

## Verification Checklist

- [ ] Grid renders with correct column count per breakpoint
- [ ] All product images same aspect ratio (no layout jank)
- [ ] Prices visible on every card (including sale strikethrough)
- [ ] Quick-add buttons functional (hover on desktop, visible on mobile)
- [ ] Color swatches display correctly (not overflowing card)
- [ ] Mid-grid promo card visually distinct from product cards
- [ ] Filter bar sticky on scroll (desktop)
- [ ] Breadcrumb: Home > Collections > [Name] correct
- [ ] Mobile: 2-col grid, no horizontal overflow
- [ ] Brand colors via `--lx-*` variables applied

## Collection-Specific CRO Data

| Tactic | Impact | Source |
|--------|--------|--------|
| Quick-add buttons on grid | +15% add-to-cart | Shopify 2026 |
| Consistent card aspect ratios | Prevents CLS (must be <= 0.1) | Web.dev |
| Price visible on card | Table stakes (hidden price = lost sale) | Baymard |
| "Added!" micro-feedback | Peak-end rule — reward moment | Material Design 3 |
| Mid-grid promo card | AOV lift via threshold/bundle nudge | Marine Layer pattern |
| Hover second image | +engagement, reduces PDP bounce rate | Fashion industry std |
| 2-col mobile grid | Optimal for thumb browsing | Apple HIG (48px targets) |
| Short hero (< 300px) | Grid is the star — don't bury it | Baymard |
| Breadcrumb navigation | Reduces bounce, aids discovery | NNGroup |
| Load More (vs pagination) | Lower friction continuation | Infinite scroll without losing context |

## Section CSS Pattern

```html
<!-- Tighter padding for collection pages — grid density matters -->
<section id="collection-grid" class="py-8 md:py-12 px-4" style="background: var(--lx-bg-color);">
  <div class="max-w-7xl mx-auto">
    <!-- Grid content -->
  </div>
</section>
```
