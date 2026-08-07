---
name: analyze-page
description: Analyze a reference webpage into a reproducible Lexsis design brief. Use for competitor or inspiration URLs; not for an existing-page CRO audit.
---

# Analyze Storefront Page

Deeply analyze a full webpage and produce a comprehensive design reference document — section by section, with reproducible HTML patterns, island mappings, and design tokens.

## When to Use

- User shares a URL and wants to "make something like this"
- Analyzing a competitor's page structure before generation
- Extracting design system tokens from an existing site
- Understanding a page's conversion strategy and section rhythm
- Creating a design brief for `$generate` to follow

## Auto-Trigger

This skill also activates when the user shares a URL with intent phrases:
- "use this as reference"
- "make something like this"
- "analyze this page"
- "recreate this layout"
- "I like this design"
- "similar to this"

## Workflow

### Step 1: Full-page capture
```
browser_navigate → {url}
browser_take_screenshot (full page)
browser_snapshot (full accessibility tree)
```

### Step 2: Classify page type
Determine which category:
- **PDP** — product detail (gallery, BuyBox, reviews, related products)
- **Landing** — campaign/post-click (single CTA, no nav, urgency, social proof)
- **Collection** — product grid with filters, category navigation
- **Homepage** — multi-CTA, navigation, hero, collections grid, brand story
- **Editorial** — long-form content, shoppable moments, magazine layout
- **Other** — blog, about, custom

### Step 3: Extract global design tokens
From computed styles and visual inspection:
- **Colors**: primary, accent, background, surface, text, muted, border
- **Typography**: heading font, body font, sizes, weights
- **Spacing**: section padding, content gaps, element margins
- **Shape**: border radius, shadow style
- **Motion**: animation patterns (fade, slide, parallax)

### Step 4: Section-by-section analysis
Scroll through the page. For EACH distinct section:

1. **Identify type** — map to nearest `lx_*` section type:
   - `lx_hero`, `lx_hero_split`, `lx_hero_video`
   - `lx_promo_top_bar`, `lx_ticker`
   - `lx_value_props`, `lx_features`, `lx_features_grid`
   - `lx_benefits`, `lx_how_it_works`, `lx_steps`
   - `lx_testimonials`, `lx_reviews`, `lx_social_proof`
   - `lx_press`, `lx_logos`
   - `lx_faq`, `lx_pricing`, `lx_bundles`, `lx_comparison`
   - `lx_cta`, `lx_cta_band`, `lx_sticky_cta`, `lx_urgency`
   - `lx_gallery`, `lx_video`, `lx_stats`, `lx_guarantee`
   - `lx_content`, `lx_layout`

2. **Extract full HTML pattern** — reproducible structure using:
   - Tailwind classes for layout
   - `--lx-*` CSS vars for theming
   - `data-island` for interactive elements (valid props from schema)
   - `{{PLACEHOLDER}}` for dynamic content

3. **Islands used** — list which islands appear, with their variant/props

4. **Responsive behavior** — how it adapts (stacks, hides, reflows)

5. **Animation/interaction** — scroll triggers, hover effects, transitions

### Step 5: Conversion strategy analysis
Identify:
- CTA frequency and placement pattern
- Social proof positioning relative to purchase decision
- Urgency/scarcity tactics used
- Trust signal locations
- Information hierarchy (what's above fold vs below)
- Mobile-specific conversion elements (sticky bars, etc.)

## Output Format

Print the following markdown inline (DO NOT save to file):

```markdown
# Page Reference: {page_title}

## Classification
- **Type**: {PDP | Landing | Collection | Homepage | Editorial}
- **URL**: {url}
- **Platform**: {Shopify | Custom | WordPress | Webflow | ...}
- **Sections**: {count}

## Design System (global tokens)
| Token | Value |
|-------|-------|
| Primary | {hex} |
| Accent | {hex} |
| Background | {hex} |
| Surface | {hex} |
| Text | {hex} |
| Text muted | {hex} |
| Border | {hex} |
| Heading font | {font-family} |
| Body font | {font-family} |
| Section spacing | {px} desktop / {px} mobile |
| Border radius | {px} |
| Shadow | {css value} |

## Section 1: {descriptive name}
**Maps to**: `lx_{type}`
**Islands**: [{IslandName}(variant), ...]

\```html
<section class="py-20 px-4 lg:px-8" style="background-color: var(--lx-bg-surface)">
  <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
    <!-- Full reproducible HTML with Tailwind + --lx-* vars + data-island markers -->
    <div data-island="BuyBox" data-props='{"productId":"{{PRODUCT_ID}}","variant":"expanded","ctaText":"{{CTA_TEXT}}"}'></div>
  </div>
</section>
\```

**Responsive**: Stacks vertically below lg, image full-width on mobile
**Animation**: Fade-in on scroll (IntersectionObserver, 200ms delay)

---

## Section 2: {name}
...repeat for ALL sections...

---

## Conversion Strategy
- **CTA pattern**: {description — frequency, placement, style}
- **Social proof**: {where placed, what type}
- **Urgency**: {countdown, stock indicators, limited offers}
- **Trust signals**: {guarantees, badges, certifications}
- **Mobile optimization**: {sticky bars, simplified layout, thumb-friendly CTAs}

## Replication Notes
Key patterns to preserve when generating a similar page:
- {section rhythm / ordering pattern}
- {whitespace and breathing room strategy}
- {visual weight distribution}
- {progressive disclosure of information}
```

## Tips for Best Results

- Take multiple screenshots if page is very long (scroll + capture)
- Use `browser_evaluate` to extract computed CSS values for accurate tokens
- Check viewport at both desktop (1440px) and mobile (390px) widths
- For Shopify stores, note which islands map to native Shopify features vs custom

## Island Reference

When mapping interactive elements, consult `reference/islands/{name}/schema.json` for:
- Valid prop names and types
- Required vs optional props
- Available variants
- Anti-patterns to avoid
- Composition rules (which islands pair together)
