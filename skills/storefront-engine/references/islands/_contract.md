# Island Design Contract

Rules every island wrapper MUST follow. Violations = visual clashing between sections.

---

## Spacing

| Context | Class | Value |
|---------|-------|-------|
| Section wrapper vertical | `py-12 md:py-16 lg:py-20` | 48/64/80px |
| Between islands in same section | `space-y-6` or `gap-8` | 24/32px |
| Section heading to content | `mb-8 md:mb-12` | 32/48px |

Islands don't add outer margin. Wrapper controls position.

## Container Widths

| Island Type | Max Width | Class |
|-------------|-----------|-------|
| Full-bleed (hero, gallery bg) | none | `w-full` |
| Commerce (BuyBox, grid, cards) | 7xl (80rem) | `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8` |
| Content (FAQ, text, email) | 3xl (48rem) | `max-w-3xl mx-auto px-4` |
| Navigation (nav, footer) | full | `w-full` (internal max-w-7xl) |
| Narrow content (testimonial quote) | 2xl (42rem) | `max-w-2xl mx-auto px-4` |

## Background Rhythm

```
Section 1 (hero):     --lx-bg-color or full-bleed image
Section 2:            --lx-surface-alt
Section 3:            --lx-bg-color
Section 4:            --lx-surface-alt
...alternate...
```

- Never 3+ consecutive sections with same background
- Hero always uses `--lx-bg-color` or image (never surface-alt)
- CTA banner sections: `--lx-accent-color` bg with white text (exception to alternating rule)

Apply via inline style: `style="background-color: var(--lx-surface-alt)"`

## Typography Hierarchy

| Level | Owner | Class | Font |
|-------|-------|-------|------|
| h1 | Hero section ONLY | `text-4xl md:text-5xl lg:text-6xl font-bold` | `--lx-font-heading` |
| h2 | Section headings | `text-2xl md:text-3xl lg:text-4xl font-bold` | `--lx-font-heading` |
| h3+ | Inside islands | Controlled by island — DO NOT OVERRIDE | — |

- One h1 per page (in hero)
- Section h2: centered by default (`text-center`), left-aligned in split layouts
- Supporting text below h2: `text-lg` + `--lx-text-muted` + `max-w-2xl mx-auto`
- Never set font-family in wrapper HTML — use CSS variables only

## Color Constraints

| Element | Allowed Colors |
|---------|---------------|
| Wrapper background | `--lx-bg-color`, `--lx-surface-alt`, transparent, or image |
| Text | `--lx-text-color` (primary), `--lx-text-muted` (secondary) |
| CTA buttons | `--lx-accent-color` bg + white text |
| Borders/dividers | `--lx-border-color` |
| Accent highlights | `--lx-accent-color` (links, badges, active states ONLY) |

NEVER use `--lx-accent-color` as a section background (except CTA banner sections).

## Responsive Rules

- Mobile-first: default styles = mobile, enhance with `sm:` → `md:` → `lg:`
- Grid layouts: `grid-cols-1 lg:grid-cols-2` (stack on mobile)
- Sticky elements: only above lg (`lg:sticky lg:top-24`)
- Full-bleed images: `aspect-[16/9] md:aspect-auto` (constrain mobile, natural desktop)
- Touch targets: min 44x44px on mobile
- Font sizes never below `text-sm` (14px) on mobile

## Animation Rules

- Use ONLY shared keyframes: `fadeUp`, `fadeIn`, `scaleIn`, `slideInLeft`, `slideInRight`
- Entrance timing: `animation: fadeUp 0.6s ease both`
- Stagger: `animation-delay: calc(var(--i, 0) * 100ms)` with `--i` set per item
- Never animate island internals — only wrapper/surrounding static HTML
- Reduce motion: animations should be subtle (< 20px translation, < 0.5s duration)

## Composition Rules

- Max 1 `BuyBox` per page
- Max 1 `DrawerShell` / `CartDrawer` per page (in hidden section)
- Max 1 `Navbar` / `SiteHeader` per page (first section)
- Max 1 `Footer` per page (last section)
- `TrustBadgeBar`: place within 1 scroll (200px) of primary CTA
- `StickyBar`: triggers when BuyBox scrolls out of viewport — place after BuyBox section
- `ReviewCarousel`: mid-page or after product details (never first section)

## Template Variables in Layout JSONs

Layouts use `{{VARIABLE}}` placeholders. Agent replaces before pasting:

| Variable | Source | Example |
|----------|--------|---------|
| `{{PRODUCT_ID}}` | `get_product` or `list_products` | `gid://shopify/Product/12345` |
| `{{PRODUCT_TITLE}}` | product.title | `Hydrating Serum` |
| `{{PRODUCT_PRICE}}` | product.price | `$29.99` |
| `{{BRAND_NAME}}` | `get_brand_kit` → name | `Glow Labs` |
| `{{CTA_TEXT}}` | page-type or industry skill | `Add to Cart` |
| `{{IMAGE_URL}}` | `search_design_library` or `generate_asset` | `https://cdn...` |
| `{{STORE_DOMAIN}}` | `get_connected_stores` | `mystore.myshopify.com` |

## Custom Styling via `data-part`

Islands expose internal elements through `data-part` attributes for CSS targeting without breaking encapsulation.

### How it works

Every island renders internal elements with `data-part="name"` attributes. You target them in the section's wrapping HTML using CSS attribute selectors:

```html
<section class="py-16">
  <style>
    /* Target the CTA button inside BuyBox */
    [data-part="cta"] {
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Target variant buttons */
    [data-part="variant-btn"] {
      border-radius: var(--lx-radius);
      border-color: var(--lx-border-color);
    }

    /* Target the trust badges row */
    [data-part="trust-badges"] {
      justify-content: flex-start;
    }
  </style>

  <div data-island="BuyBox" data-props='{"productId":"{{PRODUCT_ID}}"}'></div>
</section>
```

### Rules

1. **Only use `[data-part="x"]` selectors** — never target island internals by class name (classes can change between versions)
2. **Scope with section wrapper** — if multiple islands share part names, scope:
   ```css
   .hero-section [data-part="cta"] { ... }
   ```
3. **Only override visual properties** — colors, borders, radius, spacing, typography. Never override layout/positioning (breaks responsive behavior)
4. **Use `--lx-*` variables in overrides** — keeps theming consistent:
   ```css
   [data-part="cta"] {
     background-color: var(--lx-color-primary);
     color: white;
   }
   ```
5. **Check `schema.json`** for available parts — each island's `schema.json` has a `"parts"` array listing all targetable elements

### Common parts across islands

| Part name | Meaning | Found in |
|-----------|---------|----------|
| `root` | Island outer container | Nearly all islands |
| `cta` | Primary action button | BuyBox, StickyBar, EmailCapture, Navbar |
| `heading` | Section/island title | FAQ, CartCrossSell, CompareTable |
| `item` | Repeated list item | ProductCarousel, ReviewCarousel, CartCrossSell |
| `link` | Navigation link | Navbar, Footer, MobileMenu |
| `logo` | Brand logo element | Navbar, Footer, SiteHeader |
| `badge` | Count/status badge | Navbar (cart-badge), InventoryIndicator |

### What NOT to do

```html
<!-- ❌ WRONG: targeting by className (fragile) -->
<style>.buy-box-root .MuiButton-root { ... }</style>

<!-- ❌ WRONG: overriding layout (breaks responsive) -->
<style>[data-part="root"] { display: block !important; }</style>

<!-- ❌ WRONG: hardcoded colors (breaks theming) -->
<style>[data-part="cta"] { background: #ff6b00; }</style>

<!-- ✅ CORRECT: visual-only override with CSS vars -->
<style>[data-part="cta"] { background: var(--lx-accent-color); border-radius: 9999px; }</style>
```

### Finding available parts

1. Check `reference/islands/{name}/schema.json` → `"parts"` array
2. Or use `get_island_schema` MCP tool → returns parts list
3. Each part name describes the element's role, not its HTML tag
