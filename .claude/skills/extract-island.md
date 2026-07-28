---
description: Analyze a specific component on any webpage and output a renderer-compatible island layout JSON. Use when reverse-engineering a hero, FAQ, nav, product card, or any UI component into a reusable Lexsis layout.
allowed-tools: mcp__playwright__*
---

# /extract-island

Extract a single component from a live webpage and produce a layout JSON compatible with the Lexsis vibe renderer.

## When to Use

- Reverse-engineering a competitor's hero section, navigation, or product card
- Creating a new layout variant for an existing island (e.g., a new BuyBox arrangement)
- Capturing design inspiration from any website as a reusable template
- Contributing new layouts to the storefront-skills repo via PR

## Output Format

The output MUST match this exact structure (same as `reference/islands/{name}/layouts/*.json`):

```json
{
  "id": "{island-kebab}-{variant-slug}",
  "html": "<section ...>...</section>",
  "css": "",
  "js": ""
}
```

## Renderer Compatibility Rules

These rules are NON-NEGOTIABLE. Violating any produces broken output:

1. **`--lx-*` CSS variables** for ALL colors, fonts, spacing that should be themeable:
   - `var(--lx-color-primary)`, `var(--lx-color-accent)`, `var(--lx-bg-surface)`
   - `var(--lx-font-heading)`, `var(--lx-font-body)`
   - `var(--lx-text-color)`, `var(--lx-text-muted)`, `var(--lx-border-color)`
   - `var(--lx-radius)`, `var(--lx-shadow)`

2. **`data-island` must reference a REAL island** from our 47-island catalog:
   - Commerce: `BuyBox`, `QuickAdd`, `ProductCard`, `ProductCarousel`, `ProductHero`, `ProductGallery`, `CartDrawer`, `DrawerShell`, `CartLines`, `CartCheckoutButton`, `CartSummary`, `CartProgressBar`, `CartDiscountInput`, `CartCrossSell`, `ProceedToCart`, `QuantityBreaks`, `SubscriptionToggle`
   - Navigation: `Navbar`, `MobileMenu`, `Footer`, `SiteHeader`, `AnnouncementBar`
   - Engagement: `FAQ`, `ReviewCarousel`, `CountdownTimer`, `SocialProofPopup`, `Tabs`, `EmailCapture`, `BackToTop`, `WishlistButton`
   - Media: `HeroMedia`, `ProductGallery`, `VideoPlayer`, `ImageZoom`, `BeforeAfter`, `MediaCarousel`
   - Layout: `Modal`, `StickyBar`, `CompareTable`, `BundleBuilder`, `EditorialProductGrid`
   - Info: `DeliveryEstimate`, `InventoryIndicator`, `PaymentOptions`, `PDPInfoCards`, `SizeGuide`, `TrustBadgeBar`, `VariantSwatches`, `IngredientExplorer`, `OptionResolver`

3. **`data-props` must match the island's schema** — read `reference/islands/{name}/schema.json` for valid props, types, and required fields. Never invent props that don't exist.

4. **`{{PLACEHOLDER}}` for content slots** — dynamic content uses double-brace placeholders:
   - `{{PRODUCT_ID}}`, `{{HEADLINE}}`, `{{CTA_TEXT}}`, `{{IMAGE_SRC}}`
   - Never hardcode product-specific content

5. **Tailwind CSS** for all structural layout (grid, flex, spacing, responsive breakpoints)

6. **Responsive**: mobile-first, use `sm:`, `md:`, `lg:` breakpoints

7. **No external JS** — interactive behavior comes from islands only, not custom scripts

## Workflow

### Step 1: Navigate and capture
```
browser_navigate → {url}
browser_take_screenshot (full page)
browser_snapshot (accessibility tree)
```

### Step 2: Identify the target component
User tells you which component to extract ("the hero", "that FAQ section", "the sticky cart bar").
Find it in the DOM snapshot.

### Step 3: Deep analysis
For the target component, analyze:
- **Structure**: semantic HTML elements, nesting depth, grid/flex layout
- **Styling**: colors, typography, spacing, borders, shadows, animations
- **Responsive**: how it collapses/stacks on mobile
- **Interactive parts**: accordions, carousels, popovers, add-to-cart → map to islands
- **Content slots**: what's dynamic vs decorative

### Step 4: Map to Lexsis islands
For each interactive element found:
1. Identify closest matching island from the catalog above
2. Read its `schema.json` to get valid props
3. Construct valid `data-props` JSON using only documented props
4. If no island matches, use pure HTML (static rendering)

### Step 5: Output layout JSON
Produce the final JSON with:
- `id`: descriptive slug (e.g., `hero-split-video-left`)
- `html`: complete section HTML using --lx-* vars + Tailwind + data-island markers
- `css`: empty string (Tailwind handles styling)
- `js`: empty string (islands handle interactivity)

## Example Output

```json
{
  "id": "hero-split-video-left",
  "html": "<section class=\"grid grid-cols-1 lg:grid-cols-5 min-h-[80vh] overflow-hidden\"><div class=\"lg:col-span-3 relative\"><video autoplay muted loop playsinline class=\"absolute inset-0 w-full h-full object-cover\"><source src=\"{{VIDEO_SRC}}\" type=\"video/mp4\" /></video></div><div class=\"lg:col-span-2 flex flex-col justify-center px-8 lg:px-12 py-16\" style=\"background-color: var(--lx-bg-surface)\"><h1 class=\"text-4xl lg:text-5xl font-bold leading-tight\" style=\"font-family: var(--lx-font-heading); color: var(--lx-text-color)\">{{HEADLINE}}</h1><p class=\"mt-4 text-lg\" style=\"color: var(--lx-text-muted)\">{{SUBHEAD}}</p><div class=\"mt-8\"><div data-island=\"BuyBox\" data-props='{\"productId\":\"{{PRODUCT_ID}}\",\"ctaText\":\"{{CTA_TEXT}}\",\"variant\":\"compact\"}'></div></div></div></section>",
  "css": "",
  "js": ""
}
```

## Contributing the Layout

After extracting, the user can PR the layout into the repo:

```
plugins/lexsis-storefront-skills/
  skills/storefront-engine/reference/islands/{island-name}/layouts/{variant-slug}.json
```

The filename becomes the layout identifier used by generation skills.
