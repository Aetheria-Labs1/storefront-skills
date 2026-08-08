<!-- GENERATED from skills/ by scripts/build-distributions.py — DO NOT EDIT.
     storefront-skills v5.1.3 · 13 skills · 49 island schemas -->

# Lexsis Storefront Skills — Knowledge Base

## Workflows

---

# Skill: analyze-page

> Analyze a reference webpage into a reproducible Lexsis design brief. Use for competitor or inspiration URLs; not for an existing-page CRO audit.

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
   - `<lx-island>` for interactive elements (valid props from schema)
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
    <!-- Source-format HTML with Tailwind + --lx-* vars + islands -->
    <lx-island name="BuyBox">
      <script type="application/json">
        { "productId": "{{PRODUCT_ID}}", "variant": "expanded", "ctaText": "{{CTA_TEXT}}" }
      </script>
    </lx-island>
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

---

# Skill: asset-prep

> Source and prepare visual assets for a storefront page — search the brand library first, then generate, import, or pull from external MCPs (video, stock, research imagery). Also answers to its old name, asset-pipeline. Run after /plan-page; produces the asset manifest generation consumes.

> **Inputs:** Approved page plan (from `/plan-page` workflow)
> **Outputs:** Asset manifest (URLs + purposes + section mapping)
> **When to load:** After page plan is approved, before HTML generation.

---

## Decision Tree

```
Need an image or video for a section?
│
├─ search_design_library({ query }) → found good match?
│  ├─ YES → use it (free, on-brand)
│  └─ NO ↓
│
├─ Product shot needed?
│  ├─ YES → use real images from list_products (NEVER generate fake products)
│  └─ NO ↓
│
├─ What type of asset?
│  ├─ Static image (background, lifestyle, texture, composite)
│  │  └─ generate_asset or edit_asset (built-in, costs credits)
│  │
│  ├─ Video (hero, demo, UGC-style)
│  │  └─ External MCP: HiggsField / Runway / Kling
│  │
│  ├─ Reference/mood imagery (competitor screenshots, inspiration)
│  │  └─ External MCP: Exa (web_search_exa)
│  │
│  ├─ Stock photography (realistic, non-AI look needed)
│  │  └─ External MCP: Unsplash / Pexels
│  │
│  └─ Specialized illustration (custom style beyond built-in)
│     └─ External MCP: OpenArt
│
└─ After sourcing → import_asset({ url, purpose, tags }) to persist in library
```

---

## Built-In Tools (Lexsis AI MCP)

| Tool | What it does | Cost |
|------|-------------|------|
| `search_design_library` | Search existing brand assets | Free |
| `generate_asset` | AI image generation (photography, illustration, 3d, editorial, abstract, texture) | Credits |
| `edit_asset` | Composite, inpaint, or style-transfer existing images | Credits |
| `view_asset` | Visually verify a generated/edited asset before using | Free |
| `import_asset` | Bring an external URL (or base64) into the design library for reuse. Call with **no arguments** to open an upload picker so the user can supply their own file — use that when they want to add their own logo/photo and you have no URL for it | Free |

**Always `search_design_library` first.** Existing assets are free and already brand-consistent.

See `design-enrichment.md` for detailed prompt patterns, style selection guide, compositing recipes, and HTML placement patterns.

---

## External MCPs (Detected at Runtime)

These tools are available when the user has the corresponding MCP installed. Check availability before suggesting.

### Exa — Image Research & Reference

```
web_search_exa({ query: "skincare brand hero photography editorial style" })
```

Use for: mood boards, competitor visual research, finding reference imagery to brief `generate_asset` more precisely, sourcing real lifestyle photos.

**Flow:** Exa search → find reference URL → `import_asset({ url })` to persist → use in page.

### HiggsField / Runway / Kling — Video Generation

Use when: TikTok traffic source, fashion/luxury vertical, product demo needed, brand has no existing video content.

**Flow:**
1. Generate video via external MCP (short clip, 3-8 seconds)
2. `extract_video_frames` → pull best frame as thumbnail
3. Use video URL in HeroMedia island or `<video>` tag
4. Set click-to-play (NEVER autoplay — costs 7% CVR)

**Video placement patterns:**
- Hero: click-to-play with compelling thumbnail image
- Product demo: inline player after benefits section
- Social proof: UGC-style video carousel
- Background: muted loop, heavily dimmed (luxury only)

### OpenArt — Specialized AI Illustration

Use when: `generate_asset(style: "illustration")` doesn't provide enough control over style, need specific artistic direction, or brand has a custom illustration language.

### Unsplash / Pexels — Stock Photography

Use when: brand has no library assets, AI generation looks too synthetic, need real-world photography (locations, hands, diverse models).

---

## Feeding External Assets Into Pages

All external assets MUST be persisted before use:

```
1. Source asset via external MCP → get URL
2. import_asset({ url, purpose: "hero_bg", tags: ["lifestyle", "summer"] })
   → returns { asset_id, url, width, height }
3. Use returned URL in page HTML (same as built-in assets)
```

This ensures: the asset is stored in the brand's library, available for reuse, and won't break if the external source goes down.

---

## Per-Page-Type Asset Budget

| Page Type | Hero (high) | Section BGs (medium) | Lifestyle (medium) | Video | Total assets |
|-----------|-------------|---------------------|--------------------|----|------|
| PDP | 1 | 0-1 | 1 | 0-1 | 2-4 |
| Landing | 1 | 2-3 | 0-1 | 0-1 | 3-5 |
| Homepage | 1 | 1 | 0 | 0 | 2 |
| Editorial | 1 | 3-4 | 2-3 | 0-1 | 6-9 |
| Collection | 0-1 | 0 | 0 | 0 | 0-1 |
| Bundle | 1 | 1 | 0 | 0 | 2-3 |

**Rules:**
- Check `get_credits_balance` before any generation
- Use `quality: "medium"` default; `"high"` only for hero images
- Products have their own Shopify images — never generate product shots

---

## Video in Pages

### When Video Converts Better
- TikTok/Reels traffic (video-native audience)
- Fashion/beauty (texture, movement, try-on)
- Luxury (cinematic brand storytelling)
- Product demos (85% say video convinced them to buy)

### Technical Integration
```html
<!-- Click-to-play video hero (use HeroMedia island) -->
<lx-island name="HeroMedia">
  <script type="application/json">
    { "media": { "type": "video", "src": "VIDEO_URL", "poster": "THUMBNAIL_URL", "autoplay": false } }
  </script>
</lx-island>

<!-- Inline video (no island needed for simple playback) -->
<video class="w-full rounded-xl" poster="THUMBNAIL_URL" controls playsinline>
  <source src="VIDEO_URL" type="video/mp4" />
</video>
```

### Anti-Patterns
- NEVER autoplay video (-7% CVR)
- NEVER use video as only hero content (needs fallback image)
- NEVER serve uncompressed video (use CDN URL from import_asset)

---

## Asset Manifest (Output Format)

After sourcing all assets, produce this manifest to hand to `/generate`:

```
Section: hero
  - URL: https://cdn.trylexsis.com/assets/abc123.jpg
  - Purpose: hero_bg
  - Source: generated (quality: high)

Section: social-proof
  - URL: https://cdn.trylexsis.com/assets/def456.mp4
  - Purpose: testimonial_video
  - Source: external (HiggsField)
  - Thumbnail: https://cdn.trylexsis.com/assets/def456-thumb.jpg

Section: benefits
  - URL: https://cdn.trylexsis.com/assets/ghi789.jpg
  - Purpose: lifestyle_shot
  - Source: library (existing)
```

The generation workflow uses these URLs directly in `<img src="">` and island props.

---

## Cost Control

1. `search_design_library` first — always (free)
2. `get_credits_balance` before expensive operations
3. Prefer `quality: "medium"` — reserve `"high"` for hero only
4. External MCP assets → `import_asset` to avoid re-fetching
5. CSS gradients/solid colors for sections that don't need imagery
6. Reuse: one hero image can serve as dimmed background for 2-3 sections

---

# Skill: browser-analyze

> Use Codex Browser to analyze a URL for design extraction, CRO evidence, or competitor research. Use when a task provides a reference or storefront URL.

# Browser-Powered Page Analysis

Use Codex Browser to deeply analyze web pages before generating or optimizing storefronts.

## When to Use

- User says "remix this", "build like this", "analyze this page"
- User provides a competitor URL or reference site
- User wants CRO audit of their own page
- User wants design tokens extracted from a live site

---

## Workflow

### Step 1 — Navigate and Capture

Use Codex Browser to:
1. Open the target URL
2. Take a full-page screenshot (desktop viewport)
3. Resize to mobile (375px width) and screenshot again
4. Note the page title, meta description, and any structured data

### Step 2 — DOM Inspection

Use Codex Browser to run read-only JavaScript inspection:

```js
// Extract structural data
({
  headings: [...document.querySelectorAll('h1,h2,h3')].map(h => ({ tag: h.tagName, text: h.textContent.trim() })),
  ctas: [...document.querySelectorAll('button, a[class*="btn"], a[class*="cta"], [data-action]')].map(el => ({ text: el.textContent.trim(), href: el.href || '', classes: el.className })),
  images: [...document.querySelectorAll('img')].slice(0, 20).map(img => ({ src: img.src, alt: img.alt, width: img.naturalWidth })),
  colors: getComputedStyle(document.body).backgroundColor,
  fonts: getComputedStyle(document.body).fontFamily,
  sections: [...document.querySelectorAll('section, [class*="section"], main > div')].length
})
```

From this data, identify:
- Section count and heading hierarchy
- CTA buttons (text, color, position relative to fold)
- Color palette from computed styles
- Font families in use
- Image sources and alt text quality
- Interactive elements (carousels, tabs, accordions, video players)

### Step 3 — Conversion Analysis (12-Point Audit)

Score each 0-10 based on screenshots + DOM data:

| # | Dimension | Key Question |
|---|-----------|-------------|
| 1 | Above-the-Fold | CTA visible without scroll? Hero compelling? |
| 2 | Message-Match | Headline aligned with likely traffic source? |
| 3 | CTA Quality | Benefit-driven copy? Adequate contrast? Single primary? |
| 4 | Social Proof | Stars/testimonials/logos present? Well-placed? |
| 5 | Trust Signals | Shipping/returns/guarantees visible? |
| 6 | Urgency/Scarcity | Real or manufactured? Appropriate for vertical? |
| 7 | Price Psychology | Anchoring? Payment splitting? Bundle breaks? |
| 8 | Product Positioning | Benefits-led? Lifestyle context? Differentiation? |
| 9 | Mobile UX | 48px tap targets? 16px fonts? Sticky CTA? |
| 10 | Section Ordering | AIDA-compliant? FAQ before CTA? |
| 11 | Page Speed | Image formats? LCP candidate? Render-blocking? |
| 12 | Anti-Patterns | Autoplay? Carousel hero? Nav on LP? Competing CTAs? |

### Step 4 — Design Token Extraction

Compile from visual inspection + computed styles:

```json
{
  "primary_color": "#...",
  "secondary_color": "#...",
  "background": "#...",
  "surface": "#...",
  "text_color": "#...",
  "font_heading": "...",
  "font_body": "...",
  "border_radius": "...px",
  "spacing_unit": "...px"
}
```

### Step 5 — Output PAGE_ANALYSIS

Output this structured block:

```json
{
  "source_url": "https://...",
  "page_type": "pdp|landing|collection|homepage|editorial",
  "vertical": "beauty|supplements|fashion|food|luxury|home|tech",
  "sections_found": [
    { "type": "hero", "has_cta": true, "above_fold": true },
    { "type": "social-proof", "subtype": "logo-bar" },
    ...
  ],
  "design_tokens": {
    "primary_color": "#...",
    "font_heading": "...",
    "font_body": "...",
    "border_radius": "8px",
    "spacing": "comfortable|tight|generous"
  },
  "conversion_score": 72,
  "strengths": [
    "Strong hero with benefit-driven headline",
    "Trust badges visible above fold"
  ],
  "weaknesses": [
    { "dimension": "mobile-ux", "issue": "CTA below fold on mobile", "impact": "critical" },
    { "dimension": "social-proof", "issue": "No testimonials with real names", "impact": "high" }
  ],
  "recommended_remix": {
    "sections": ["hero", "trust-bar", "benefits", "testimonials", "product-showcase", "faq", "cta"],
    "tactics": ["sticky-cta", "real-testimonials", "benefit-before-feature"],
    "avoid": ["autoplay", "carousel-hero", "generic-stock"]
  }
}
```

Then proceed to page generation using this analysis as context.

---

## Fallback (No @Browser Available)

If @Browser is not available or not enabled:
1. Use `extract_brand_design({ url })` from Lexsis AI MCP for server-side screenshot + token extraction
2. Note limitations: no DOM access, no mobile viewport test, no interaction detection
3. Suggest: "Enable the Browser plugin in Codex settings for deeper page analysis (DOM inspection, mobile testing, interaction detection)."

---

## Reference Data

### Conversion Benchmarks
| Metric | Average | Top 20% | Top 10% |
|--------|---------|---------|---------|
| All Shopify | 1.4% | >3.2% | >4.7% |
| Mobile | 1.2% | — | >3.9% |
| Landing pages (2026) | 3.5-5.2% | — | — |

### Critical Multipliers
- Sticky CTA + above-fold CTA: +12% CVR
- Real testimonials with names: +22% CVR
- Autoplay video: -7% CVR
- Personalized CTAs: +202% vs default
- 1s speed improvement: +2% CVR

### Anti-Patterns to Detect
- Autoplay video (loses 7% CVR)
- Rotating carousels (banner blindness)
- Navigation links on landing pages (exit opportunities)
- Multiple competing CTAs per viewport
- Generic stock photography
- CTA below mobile fold without sticky alternative

---

# Skill: cart

> Inspect, assign, and edit Cart V2 profiles, including offers, shipping goals, subscriptions, responsive behavior, and scoped custom CSS.

# Configure Cart Profiles

Use this workflow for Cart V2 configuration and page targeting.

## Architecture

- A generated page declares only `head.use_cart_v2: true`.
- Never add `DrawerShell`, `CartLines`, or cart HTML to page sections.
- The renderer injects the resolved published profile after page sections.
- Resolution order is page assignment, campaign assignment, store default,
  then legacy fallback.
- Page titles and SEO metadata never select a cart.
- Draft profile edits do not affect shoppers until the merchant publishes.
- Assignment changes and profile publish/rollback operations automatically
  refresh affected published Shopify pages after the database commit.

## MCP Surface

Use only these cart tools:

1. `get_cart_profile`
2. `set_cart_profile`
3. `edit_cart`

Profile creation, duplication, publishing, rollback, defaults, campaign
targeting, history, and archival remain in the Lexsis app.

## Workflow

### 1. Inspect

Call `get_cart_profile` before making changes.

- Pass `page_id` to inspect the effective profile and resolution source.
- Pass `cart_profile_id` to inspect an editable draft.
- Pass `store_id` alone to list available profiles.

Do not assume that the store default is the page's effective cart.

### 2. Assign when requested

Call `set_cart_profile` with `page_id` and a published `cart_profile_id`.

Pass `cart_profile_id: null` to remove the page assignment. This restores
campaign, default, or legacy fallback resolution.

### 3. Edit the draft

Call `edit_cart` with a partial patch. The same tool handles:

- `cart_mode`
- `layout_schema`
- `cart_rules`
- `commerce_config`
- `custom_css`

Use `commerce_config` for free shipping, selling-plan presentation, offers,
checkout behavior, currency, and `cart_style`. Nested objects merge with the
existing draft. Arrays such as `offer_slots` replace the existing array.

Example:

```json
{
  "cart_profile_id": "PROFILE_UUID",
  "change_note": "Campaign cart treatment",
  "patch": {
    "commerce_config": {
      "free_shipping_threshold": 7500,
      "free_shipping_celebration": true,
      "cart_style": {
        "width": "440px",
        "responsive": {
          "mobile": "bottom-sheet"
        },
        "line_spacing": "comfortable"
      }
    },
    "custom_css": "[data-part=\"checkout\"] { font-weight: 600; }"
  }
}
```

`edit_cart` never publishes. Tell the merchant to review and publish in the
Lexsis app when the response reports unpublished changes.

## Offers

Offer placements are:

- `header`
- `after_line`
- `after_lines`
- `before_checkout`

Use Shopify product GIDs. Manual offers require recommended product IDs.
Shopify-powered offers use `RELATED` or `COMPLEMENTARY` recommendation intent.

Do not fabricate products, prices, currencies, or selling plans. Subscription
purchase options appear only for products with real Shopify selling plans.

## Trigger Communication

All cart triggers use `cart:open`.

1. Add-to-cart actions emit `cart:open` immediately.
2. The hydrator bridges DOM `cart:open` events to the cart event bus.
3. The injected `DrawerShell` listens for the event and opens.
4. Child cart islands hydrate on first open.
5. The cart confirms or rolls back the optimistic line.

The header cart button uses the same event. Custom page code may dispatch:

```js
document.dispatchEvent(new CustomEvent("cart:open"))
```

The trigger never needs the profile ID. Profile resolution happens before
hydration.

## Styling

Page `theme_css` provides brand defaults. Cart profile design settings and
`custom_css` provide cart-only overrides.

Custom CSS is sanitized, scoped to the profile cart root, and published with
the profile snapshot. External imports, external URLs, script escapes, and
unbalanced rules are rejected.

## Verification

After assignment or editing:

1. Call `get_cart_profile` with the page ID.
2. Confirm `resolution_source` and profile identity.
3. Preview add-to-cart and header cart triggers.
4. Check desktop and mobile modes.
5. Confirm offers use real products and subscriptions appear only when
   selling plans exist.
6. Confirm draft changes remain non-live until published.

Read `storefront-engine/references/cart-composition.md` and
`storefront-engine/references/cart-v2-management.md` for the detailed contract.

---

# Skill: experiment

> Set up A/B tests, personalization variants, and monitor experiment results — hypothesis-driven testing with statistical significance tracking

# Run Storefront Experiment

Set up A/B tests, personalization variants, and monitor experiment results — hypothesis-driven testing with statistical significance tracking

## Context

- **conversion-psychology**: > When to load: ALWAYS. Read before generating any ecommerce page.

## Workflow

# Storefront Analytics & Experiments

Access page performance data and manage A/B experiments.

## Analytics Tools

### Page-Level Deep Dive
```
get_page_analytics(page_id)
```
Returns: CVR, bounce rate, time on page, traffic sources, device split, top-performing sections.

### Time Series Trends
```
get_analytics_timeseries({ metric: "conversions", period: "daily", range: "30d" })
```
Returns: daily/weekly trends for hits, conversions, revenue, AOV.

### Revenue Attribution
```
get_attribution({ page_id? })
```
Returns: ROAS by channel, revenue per page, top campaigns driving conversions.

## A/B Testing Flow

### 1. Create Experiment
```
create_ab_test({
  page_id: "...",
  variants: [{ blueprint_id: "...", weight: 50 }, { blueprint_id: "...", weight: 50 }]
})
```

### 2. Monitor Results
```
get_experiment_results(experiment_id)
```
Returns: CVR per variant, statistical significance (mSPRT), sample sizes, winner recommendation.

### 3. Scale Winner
```
scale_winner(experiment_id, { variant_id: "..." })
```
Scales winning variant to 100% traffic, marks experiment complete.

## Best Practices

- Wait for statistical significance before scaling winner
- Minimum ~1000 visitors per variant for reliable results
- Check device split — a variant may win on mobile but lose on desktop
- Use `get_attribution` to understand which traffic sources convert best
- Compare page analytics before/after changes to measure impact


# Personalization Variant (Persona-Specific Page Versions)

Create targeted page variants adapting messaging, imagery, social proof, and CTAs to each audience segment's motivations and objections.

## Prerequisites

- Base page exists (the page to personalize from)
- Personas defined or user describes target audiences
- Brand kit available (shared across all variants)

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Load Personas and Base Page

```
list_personas()
```

Review available audience segments. If none exist, define inline: name, demographics, pain points, motivations, objections, buying stage, tone preference.

```
get_page(page_id)
get_page_content(page_id)
```

Understand current structure, copy, and section types. This is the default variant.

### Step 3 — Plan Persona Adaptations

For each selected persona, identify what changes (ordered by conversion impact):

| Priority | Element | Personalization Strategy |
|----------|---------|--------------------------|
| 1 | Hero headline + subheadline | Tone shift: urgent for deal-seekers, aspirational for status-seekers (+202% CVR) |
| 2 | Hero image | Demographic match: age, lifestyle, environment |
| 3 | Social proof selection | Relevant testimonials matching persona's concern |
| 4 | CTA text | Motivation match: savings-focused vs quality-focused vs speed-focused |
| 5 | Section ordering | Pain-first for problem-aware, solution-first for solution-aware |

Not everything changes. Keep brand identity (colors, fonts, logo) consistent across all variants.

### Step 4 — Source Persona-Matched Assets

For each persona:
```
search_design_library({ query: "<persona-relevant imagery>" })
```

Find images reflecting the persona's world. Generate if needed:
```
generate_asset({ prompt: "...", demographic: "<persona context>" })
```

### Step 5 — Create Each Variant

For each persona:
```
create_page_variation(page_id, {
  name: "<persona_name> variant",
  changes: {
    sections: [
      { section_id: "hero", html: "...", css: "..." },
      { section_id: "social-proof", html: "..." },
      { section_id: "cta-block", html: "..." }
    ]
  }
})
```

All variants use the same `--lx-*` CSS variables (brand stays consistent). Only content, imagery, and tone change.

Islands remain identical across variants -- only the surrounding copy/imagery adapts.
When a prop change is part of the experiment, edit source-format markup:
```html
<lx-island name="BuyBox">
  <script type="application/json">
    { "product": { "title": "...", "price": "$29.99", "variants": [] } }
  </script>
</lx-island>
```

### Step 6 — Validate All Variants

For each variant:
```
check_page_integrity({ page_id: variant_page_id, archetype })
```

Ensure all render correctly, islands work, mobile intact.

### Step 7 — Visual Verification (Each Variant)

Use Codex Browser to open every variant preview, capture desktop and mobile screenshots, and inspect the rendered result. If Browser is unavailable, provide the preview URLs and state that visual verification remains manual.

Checklist (per variant):
- [ ] Headline tone matches persona (urgent vs aspirational vs analytical)
- [ ] Hero image reflects persona demographic
- [ ] CTA language aligns with persona motivation
- [ ] Social proof relevant to persona's concerns
- [ ] Brand identity consistent (`--lx-*` variables unchanged)
- [ ] Mobile layout intact
- [ ] Islands hydrated correctly

### Step 8 — (Optional) Set Up Persona-Targeted Experiment

```
create_ab_test({
  page_id: base_page_id,
  variants: [
    { page_id: variant_a_id, weight: 33, targeting: { persona: "deal-seekers" } },
    { page_id: variant_b_id, weight: 33, targeting: { persona: "quality-seekers" } },
    { page_id: base_page_id, weight: 34, targeting: { default: true } }
  ]
})
```

Traffic routes to matching persona variant based on UTM/audience signals.

## Decision Points

| Question | Decision |
|----------|----------|
| Which personas? | Top 2-3 highest-value segments (by revenue or volume) |
| What to personalize? | Headlines + hero image + CTA = highest impact; start there |
| Full rewrite or selective? | Selective: 3-5 elements max per variant to isolate impact |
| Auto-assign or manual? | Auto if UTM/referrer identifies segment; manual for broad traffic |
| How many variants? | 2-4 max -- more variants need more traffic for significance |

## Quality Gates

- Each variant feels genuinely tailored (not just a headline swap)
- Imagery matches persona demographic and psychographic profile
- CTA language aligns with persona motivation
- Social proof relevant to persona (industry-matched, use-case-matched)
- All variants share same `--lx-*` brand identity
- Each variant passes `check_page_integrity` independently
- Tone consistent within each variant (headline tone = body copy tone)
- Structural integrity maintained (no broken sections or islands)


# A/B Test Variant (Hypothesis-Driven Experiment)

Clone an existing page, apply a single focused change based on a clear hypothesis, launch a controlled experiment, and monitor for statistical significance via mSPRT.

## Prerequisites

- Target page exists and is published (needs traffic)
- Sufficient traffic (minimum 200 daily visitors, recommend 500+)
- Clear metric to optimize (CVR, AOV, bounce rate, scroll depth)

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
```

These two calls ALWAYS run first. No exceptions.

### Step 2 — Load Current Page and Baseline

```
get_page(page_id)
get_page_analytics(page_id)
```

Record baseline performance:
- Conversion rate (primary metric)
- Bounce rate, average time on page
- Scroll depth, CTA click-through
- Revenue per visitor

This is the control to beat.

### Step 3 — Formulate Hypothesis

Structure: "Changing **[element]** from **[current]** to **[proposed]** will improve **[metric]** by **[estimated %]** because **[reason based on user behavior]**."

Document the hypothesis BEFORE creating the variant. Not post-hoc.

Common high-impact tests (ordered by typical lift):
1. Hero headline copy (+5-15% CVR)
2. CTA button color/text (+3-10% CTR)
3. Social proof placement (+5-22% depending on type)
4. Hero image: lifestyle vs product-focused (+8-12%)
5. Section ordering: problem-first vs solution-first (+3-7%)
6. Price anchoring: was/now vs % off (+4-8%)

### Step 4 — Create the Variant

```
duplicate_page(page_id)
```

Creates exact copy. Then apply the SINGLE focused change:
```
update_section_from_source({ page_id: variant_page_id, section_id, source })
```

RULE: ONE change per test. Multiple changes make attribution impossible.

All styling via `--lx-*` CSS variables. Islands remain unchanged unless the
test specifically targets island props:
```html
<lx-island name="BuyBox">
  <script type="application/json">
    { "product": { "title": "...", "price": "$29.99", "variants": [] } }
  </script>
</lx-island>
```

### Step 5 — Validate Variant

```
check_page_integrity({ page_id: variant_page_id, archetype })
```

Ensure variant renders correctly, all islands work, mobile intact.

### Step 6 — Visual Verification

Use Codex Browser to open the variant preview, capture desktop and mobile screenshots, and inspect the rendered result. If Browser is unavailable, provide the preview URL and state that visual verification remains manual.

Checklist:
- [ ] The ONE change is clearly visible
- [ ] Everything else identical to control
- [ ] Mobile layout intact
- [ ] Islands hydrated correctly
- [ ] No unintended side effects (broken spacing, color bleed)

### Step 7 — Launch Experiment

```
create_ab_test({
  page_id: page_id,
  hypothesis: "Changing [X] will improve [metric] because [reason]",
  variants: [
    { page_id: page_id, weight: 50, name: "Control (A)" },
    { page_id: variant_page_id, weight: 50, name: "Variant (B)" }
  ],
  primary_metric: "conversion_rate",
  minimum_sample: 1000
})
```

50/50 split is standard. 80/20 only for high-traffic pages testing risky changes.

### Step 8 — Monitor Results

```
get_experiment_results(experiment_id)
```

Returns: CVR per variant with confidence intervals, statistical significance (mSPRT), sample size, winner recommendation, secondary metrics.

RULES:
- NEVER call a winner before mSPRT reports `significant: true`
- Minimum 1000 visitors per variant for evaluation
- Check device split (variant may win mobile, lose desktop)
- Monitor secondary metrics (winning CVR but tanking AOV is not a win)

### Step 9 — Scale Winner

Only when `significant: true`:
```
scale_winner(experiment_id, winning_variant_id)
```

Routes 100% traffic to winner. Marks experiment complete.

If no winner after 2000+ visitors per variant: the change has no meaningful impact. Stop test, formulate bolder hypothesis.

## Decision Points

| Question | Decision |
|----------|----------|
| What to test first? | Highest impact, lowest effort: headline > CTA > hero > layout |
| Traffic split? | 50/50 default; 80/20 for high-traffic + risky changes |
| When to check? | After 500+ visitors per variant; avoid daily peeking |
| When to stop? | Significant result OR >3000 visitors/variant with no signal |
| Variant loses? | Document learning, revert to control, new hypothesis |
| Multiple tests? | Only on DIFFERENT pages; never two tests on same page |

## Quality Gates

- ONE change per test (scientific rigor -- isolate the variable)
- Hypothesis documented BEFORE variant creation
- Minimum 1000 visitors per variant before evaluating
- Statistical significance required (mSPRT p<0.05) before declaring winner
- Both variants pass `check_page_integrity`
- Control remains untouched for test duration
- Secondary metrics monitored alongside primary
- Learning documented regardless of outcome (losses teach as much as wins)
- Wait for mSPRT -- never call early based on gut feeling

---

# Skill: generate

> Generate a complete Shopify storefront page — auto-detects page type (landing, PDP, collection, homepage, editorial, listicle, bundle) and applies conversion-optimized patterns

# Generate Storefront Page

Generate a complete Shopify storefront page — auto-detects page type (landing, PDP, collection, homepage, editorial, listicle, bundle) and applies conversion-optimized patterns

## Context

- **storefront-craft**: Load this skill first on any storefront page generation task.
- **workflow-orchestration**: Load after `craft-guide`. Defines optimal tool sequences, parallelization rules, and flow selection.
- **conversion-psychology**: > When to load: ALWAYS. Read before generating any ecommerce page.
- **island-patterns**: How to properly embed, wrap, and combine React islands in vibe-code HTML sections. Load when using commerce or engagement islands.

## Workflow

> **STOP — Planning Required First**
> Before running any generation phase, execute the Page Planning workflow (Phase 1 from storefront-engine).
> Assess what the user has told you, ask clarifying questions if < 4 signals are present, generate a section plan, and get user approval.
> Do NOT proceed to Phase 2 until a page plan is confirmed by the user.
> Exception: If user explicitly says "skip planning" or "just build it".

# Storefront Page Generation

Generate high-quality Shopify storefront pages using the Lexsis AI MCP tools.

> **Prerequisites**: Read `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`, and `vibe://skills/source-format` first — they define the source authoring format, CSS variable system, island integration, and visual verification step.

## Generation Flow (Two-Phase)

### Phase 2 — Context Gathering (run ALL in parallel)

```
get_workspace_details    → workspace ID
get_connected_stores     → store domain
get_brand_kit            → logo, fonts, colors, voice, border radius
get_design_md            → brand brief + design philosophy + don'ts
list_products            → product catalog (for commerce islands)
get_navigation           → navbar/footer links
search_design_library    → existing brand assets (hero images, lifestyle shots)
```

All 7 calls can run in parallel. Wait for all before proceeding.

### Phase 3 — Asset Preparation

Decision tree per section:
1. `search_design_library` — check existing assets FIRST (always)
2. `generate_asset` — only if library has nothing suitable
3. `edit_asset` — composite/modify if needed
4. `view_asset` — verify result before using in page

Budget: 3-5 generated assets per page max. Existing assets = free.

### Phase 4a — Draft Source HTML

Author the page in **source format** (see `vibe://skills/source-format`) — plain HTML, never JSON-escaped:
- Sections delimited by `<!-- section: id -->` comments
- Islands as `<lx-island name="BuyBox"><script type="application/json">{...props}</script></lx-island>` — use `vibe://schema/island/{name}` for exact prop shapes
- Section CSS in a `<style>` block, section JS in a `<script>` block per section
- Generate `theme_css` with `compile_theme` (WCAG-checked, from brand kit colors)
- Focus on visual design: layout, typography, color, spacing, imagery; animations via `data-behavior="gsap-*"` presets or shared keyframes
- Write real copy naturally (apostrophes/quotes are fine — never escape anything; never Lorem Ipsum)
- Use asset URLs from Phase 3 in `<img>` tags

### Phase 4b — Compile & Fix

```
compile_page_source(source, head, theme_css, scripts)   → compiled page + issues
```

Fix reported issues in the source and re-compile. Common issues: duplicate section IDs, invalid island names, malformed props JSON, missing headless hooks, external scripts in section HTML.

### Phase 5 — Publish + Visual Verify

```
create_page_from_source(source, head, theme_css, scripts, slug, archetype, publish=false)  → preview_url
```

**Visual verification is REQUIRED before marking complete:**

| Environment | How to Verify |
|-------------|--------------|
| Codex Browser | Open `preview_url`, capture desktop and mobile screenshots, then review them |
| No Browser | Provide `preview_url` and state that visual verification remains manual |

**Checklist:**
- [ ] Hero visible above fold (headline + CTA without scrolling)
- [ ] Brand colors applied (not default purple)
- [ ] Fonts loaded (not system fallback)
- [ ] Images rendering (not broken/placeholder)
- [ ] Mobile layout correct (375px viewport, no horizontal scroll)
- [ ] Islands hydrated (BuyBox shows product data, not empty div)
- [ ] CTA contrast ≥ 4.5:1

If issues → `update_section_from_source` (one section per call) → re-screenshot.
When satisfied, return the draft preview. Call `publish_page(page_id)` only after the user explicitly approves a live publish.

## Page Type Templates

**Product Landing (PDP)** — 8-10 sections:
Hero (split) → Gallery → BuyBox → Benefits → Ingredients/Specs → Reviews → Related Products → FAQ → Sticky CTA → Footer

**Campaign Landing** — 10 sections:
Hero → Problem/Pain → Solution → Key Benefits → Social Proof → How It Works → Comparison → Offer/Pricing → FAQ → CTA

**Homepage** — 7-8 sections:
Hero → Featured Products → Brand Story → Categories → Testimonials → Newsletter → Trust Bar → Footer

**Collection** — 6 sections:
Hero Banner → Filter/Sort → Product Grid → Promo Card → Social Proof → Footer

## Quality Bar

- Mobile-first (375px viewport — test this)
- All brand colors via `--lx-*` CSS variables (never hardcoded hex in HTML)
- Proper heading hierarchy (single h1 in hero, h2 per section, h3 for sub-items)
- Islands for ALL commerce interactions (add-to-cart, checkout, cart drawer)
- All images from asset tools (never external URLs unless Shopify CDN)
- No fetch/XHR, eval, localStorage, @import, duplicate IDs
- Hero headline ≤ 8 words, visible without scrolling
- Use shared keyframes (fadeUp, fadeIn, scaleIn) — don't define new @keyframes unless truly unique

## Ad-to-Page Flow

When converting an ad creative to a landing page:
1. `get_ad_creatives` — get creative metadata
2. `analyze_ad_creative` — extract headline, claims, colors, tone, CTA
3. `match_persona_to_ad` — identify target audience
4. Continue with Phases 1-5 using extracted context
5. Ensure "scent continuity" — ad headline ≈ page hero headline

---

# Skill: optimize

> CRO-optimize an existing page — analyzes conversion weaknesses and applies fixes (redesign sections, add trust signals, fix CTAs, improve mobile UX)

# Optimize Storefront Page

CRO-optimize an existing page — analyzes conversion weaknesses and applies fixes (redesign sections, add trust signals, fix CTAs, improve mobile UX)

## Context

- **cro-research**: > Compiled from Baymard Institute, Unbounce, Shopify, CXL, Conversion Rate Experts, Nielsen Norman Group, Littledata, HubSpot, Optimizely, Wordstream, and Awwwards analysis. Data points sourced 2024-2026.
- **conversion-psychology**: > When to load: ALWAYS. Read before generating any ecommerce page.

## Workflow

# Storefront Page Editing

Edit existing pages using section-level operations.

## Edit Flow

1. `find_page` — locate the target page
2. `get_page_source` and `inspect_page_sections` — read current source and structure
3. Make section-level source changes
4. `update_section_from_source` — compiles and preflights before saving
5. `check_page_integrity` — verify the completed page

## Operations

### Update/Replace a Section

```
update_section_from_source({ page_id, section_id, source })
```
- Replaces the compiled section from one source-format section
- Auto-bumps page version
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
update_section_from_source({ page_id, source, position })
```
- Position: "before:{section_id}" or "after:{section_id}" or index number
- Must include full section HTML

### Remove a Section

```
remove_page_section(page_id, section_id)
```
- Irreversible — confirm with user first
- Auto-bumps version

### Reorder Sections

```
move_page_section(page_id, section_id, new_position)
```
- Position is 0-indexed
- All other sections shift accordingly

## Best Practices

- Always `get_page` first to understand current structure
- Reference section IDs from the page data (don't guess)
- After all edits, run `check_page_integrity` before telling the user it is done
- For multi-section changes, batch them (each call bumps version)
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout


# Page Redesign (Modernize/Refresh Existing Page)

Visually refresh an existing page using performance data to preserve what works and redesign what does not.

## Prerequisites

- Target page exists (published or draft)
- Brand kit up to date (may have changed since page creation)
- Page analytics available for performance-informed decisions

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
get_design_md()                  → brand brief, design philosophy, constraints
```

These four calls ALWAYS run first. No exceptions.

### Step 2 — Locate and Inspect Target Page

```
find_page({ query: "page name or slug" })
```
Or:
```
list_pages({ status: "published" })
```

Then load full page data:
```
get_page(page_id)
inspect_page_sections(page_id)
```

Understand: section count, section types, content blocks, current `--lx-*` variables, islands in use.

### Step 3 — Analyze Performance

```
get_page_analytics(page_id)
```

Categorize each section:
- **KEEP** — high CVR, proven copy, minor visual polish only
- **REDESIGN** — same content, new layout/styling
- **REPLACE** — low-performing, rebuild approach
- **REMOVE** — adds friction, no conversion value

Key rule: NEVER redesign sections that are converting well. Analytics data overrides aesthetic preferences.

### Step 4 — Apply Section-by-Section Updates

For each section to change:
```
update_section_from_source({ page_id, section_id, source })
```

For reordering (if scroll-depth data suggests better flow):
```
move_page_section(page_id, section_id, new_position)
```

All updated sections must use `--lx-*` CSS variables from current brand kit. No hardcoded colors or fonts.

### Step 5 — Validate

```
check_page_integrity({ page_id, archetype })
```

Ensure no broken islands, valid HTML structure, responsive layout intact.

### Step 6 — Show Before/After

```
diff_page_versions(page_id, { from: previous_version, to: current_version })
```

Present structural diff to user for approval before publishing.

### Step 7 — Load Preview and Verify Visually

```
get_page(page_id)
```

Use the returned `preview_url`.

Use Codex Browser to open `preview_url`, capture desktop and mobile screenshots, and inspect the rendered result. If Browser is unavailable, provide the preview URL and state that visual verification remains manual.

Checklist:
- [ ] Brand colors applied (current kit, not old defaults)
- [ ] Fonts loading correctly (not system fallback)
- [ ] High-CVR sections unchanged in structure
- [ ] Mobile layout intact or improved
- [ ] All islands still functional (cart, forms)
- [ ] Section spacing consistent
- [ ] No horizontal scroll on mobile

If issues found: `update_section_from_source` to fix, then re-verify.

### Step 8 — Go Live (User Confirms)

Only after user approves:
```
publish_page(page_id)
```

If redesign later hurts metrics: `rollback_page_version(page_id, version_id)` is available.

## Decision Points

| Question | Decision |
|----------|----------|
| Full rebuild or section-by-section? | >70% sections changing = full rebuild is faster |
| Keep copy or rewrite? | Keep unless analytics show messaging problems |
| Preserve section order? | Yes, unless scroll-depth shows clear drop-off pattern |
| Same section types or new? | Prefer new layouts for freshness; same types if copy fits |
| A/B test old vs new? | Recommend if page has >500 daily visitors |

## Quality Gates

- URL/slug PRESERVED (never change -- breaks SEO and ad links)
- Page title and meta description preserved unless explicitly requested
- High-CVR sections retain their copy and core structure
- New design matches current brand kit (`--lx-*` variables)
- Mobile responsiveness maintained or improved
- All existing islands remain functional
- Version history intact (rollback available)
- Page passes `check_page_integrity` with zero errors

---

# Skill: plan-page

> Plan a storefront page before generation. Use to gather requirements and create an approved section, animation, and visual-rhythm blueprint.

# Plan Storefront Page

Plan a storefront page before generation — gathers requirements, designs section layout, animations, and visual rhythm.

## Context

- **storefront-craft**: Load this skill first on any storefront page generation task.
- **conversion-psychology**: Read before planning any ecommerce page.

## Workflow

# Page Planning Workflow

> This produces a structured page blueprint. Run it standalone, or use it as Phase 1 before `$generate`.

## Step 1 — Assess What's Known

Score the user's input:

| Signal | Check |
|--------|-------|
| Page type (landing, PDP, homepage, collection, editorial, listicle, bundle) | stated? |
| Target audience / persona | described? |
| Products or collection to feature | named? |
| Traffic source (Meta, Google, TikTok, email, organic) | mentioned? |
| Conversion goal (purchase, signup, browse) | clear? |
| Reference URL or ad creative | provided? |
| Tone/style preference | specified? |

- **4+ signals present** → proceed to Step 3 (auto-plan)
- **< 4 signals** → proceed to Step 2 (ask questions)

## Step 2 — Adaptive Discovery

Ask ONLY questions whose answers are missing. Never ask more than 4 at once.

**Tier 1 (always ask if missing):**
1. "What type of page?" (landing / PDP / homepage / collection / editorial)
2. "Who is this for?" (audience: demographics + pain point)
3. "What should visitors do?" (single conversion goal)

**Tier 2 (ask if Tier 1 reveals complexity):**
4. "Where does traffic come from?" (impacts visual density + social proof weight)
5. "Any sections you specifically want?" (hero style, FAQ, comparison table, etc.)
6. "Should this feel bold/energetic or minimal/premium?" (visual approach)
7. "Any animations or scroll effects?" (parallax, reveal-on-scroll, sticky elements)

**Follow-up triggers:**
- Multiple products mentioned → "Which is the hero product? Are others cross-sells or equals?"
- Health/beauty vertical → "Do you have clinical data or certifications to feature?"
- Ad creative provided → "Should the page match the ad's exact style, or just the message?"

## Step 3 — Generate Page Plan

Use MCP tools to gather brand context:
```
get_brand_kit        → colors, fonts, voice, spacing
get_design_md        → brand philosophy + don'ts
list_products        → available product data
get_navigation       → navbar/footer links
```

Then produce a structured plan covering:

**A. Section Sequence** (ordered list)
For each section:
- Section ID + type (e.g. `hero-split`, `social-proof-bar`, `features-grid`)
- Purpose (what it communicates / why it's here in this position)
- Key content (headline direction, imagery type, specific products)
- Island requirement (if interactive: BuyBox, FAQ, ReviewCarousel, etc.)
- Animation (fade-up, parallax, sticky, reveal, none)

**B. Visual Rhythm**
- Spacing pattern (tight-loose-tight, progressive relaxation, etc.)
- Color temperature flow (hero warm → middle neutral → CTA warm)
- Typography hierarchy (display → heading → body sizes)

**C. Inter-Section Communication**
- Narrative thread (how sections connect logically)
- CTA placement strategy (where and how many)
- Social proof distribution (where trust signals appear and why)
- Scroll incentives (what makes user keep scrolling)

**D. Technical Requirements**
- Islands needed (exact list)
- Custom animations (scroll-triggered reveals, parallax, sticky)
- Asset requirements (hero image, lifestyle shots, textures, icons)

## Step 4 — Present Plan for Approval

Show the plan to the user in this format:

```
📋 Page Plan: [Page Type] for [Audience]

Goal: [Conversion goal]
Sections: [N] | Islands: [list] | Style: [visual approach]

Section Layout:
1. [hero-split] — Hook headline + product image + primary CTA
   Animation: fade-up on load
2. [trust-bar] — Star rating + press logos + "X customers served"
   Animation: none (instant credibility)
3. [problem-solution] — Pain → product as answer (emotional)
   Animation: reveal on scroll
...

Visual Flow: [spacing + color temperature description]
CTA Strategy: [where + how many]

Proceed with this plan? (Or tell me what to change)
```

Wait for user confirmation. If user suggests changes, update plan and re-present.

## Step 5 — Next Steps

Once approved, the user can:
- Run `$generate` — carry the plan forward as the binding blueprint
- Or hand off the plan to any generation flow

The plan becomes BINDING for generation:
- Phase 2 context gathering targets the plan's requirements
- Phase 3 asset generation follows the plan's imagery needs
- Phase 4 HTML generation follows the plan's section sequence EXACTLY
- Section purposes from the plan guide the copywriting
- Animation choices from the plan guide the JS/CSS

---

# Skill: publish

> QA a storefront page, create a draft preview, and publish live only after explicit user approval.

# Publish Storefront Page

QA a storefront page, validate structure and rendering, create a draft preview, and publish live only after explicit user approval.

## Context

- **qa-recipe**: compile source, create a draft, run integrity checks, then verify in a browser

## Workflow

# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. `compile_page_source` — compile and validate the generated source
2. `create_page_from_source` — create a draft preview first
   - `publish: false` → preview URL only (not live on store)
3. Confirm the user explicitly wants a live publish before `publish_page`.

## Operations

### Draft Preview (New Page)
```
compile_page_source({ source, head, theme_css, scripts })
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
```
Returns: page_id and preview_url

### Preview (Draft)
```
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
```
Returns: preview_url (not visible to store visitors)

### Publish Live (Explicit Approval Required)
```
publish_page(page_id)
```
Only call this after the user explicitly says to publish live. Makes a draft page live.

### Unpublish
```
unpublish_page(page_id)
```
Takes page offline but preserves it in DB.

### Duplicate
```
duplicate_page(page_id, { title: "New Title" })
```
Creates a copy — useful for A/B test variants.

### Create Experiment Variant
```
create_page_variation(page_id, { changes: {...} })
```
Creates variant for A/B testing.

## Prerequisites

- Store must be connected (`get_connected_stores`)
- Brand kit should exist for proper theming

## Post-Publish

After publishing, the page is served via:
- Shopify store (native page)
- pages.lexsis.app (standalone via edge worker)
- Custom domain (if tracking domain configured)

---

# Skill: remix

> Rebuild a competitor page or ad creative adapted to your brand — extracts structure and conversion patterns, regenerates with your products and design tokens

# Remix Storefront Page

Rebuild a competitor page or ad creative adapted to your brand — extracts structure and conversion patterns, regenerates with your products and design tokens

## Context

- **storefront-craft**: Load this skill first on any storefront page generation task.
- **visual-craft**: Techniques for making vibe-code pages look premium. Load when polishing visual quality.

## Workflow

# Ad Creative to Landing Page

Generate a high-converting landing page from an ad creative with full scent continuity (headline, palette, CTA, tone match from click to page).

## Prerequisites

- At least one ad creative synced (Meta/Google/TikTok)
- Store connected and brand kit configured

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Identify and Analyze the Ad

```
get_ad_creatives({ store_id, status: "active" })
```

Present available creatives (thumbnail + headline + spend). User picks one, or use highest-spend active creative.

```
analyze_ad_creative({ creative_id })
```

Extracts: headline, subheadline, claims, color_palette, tone, cta_text, target_audience, urgency_signals, imagery_style.

### Step 3 — Match Persona and Source Assets

```
match_persona_to_ad({ creative_id })
```

Maps to persona: demographics, pain points, motivations, objections, buying stage. Determines page tone.

```
search_design_library({ query: "<product/topic from ad>" })
```

Find product shots and lifestyle images matching the ad aesthetic. Use `generate_asset` if library insufficient.

### Step 4 — Two-Phase Page Generation

**Phase 4a — Raw HTML + Tailwind (no islands)**

Generate full page as HTML + Tailwind. Scent continuity rules:
- Hero headline = ad headline (semantic match, max 2-word variation)
- `--lx-accent-color` set to ad's dominant color
- CTA text matches or escalates the ad CTA
- First fold answers the same promise the ad made
- Zero navigation links (single CTA focus)

Structure: Hero > Problem/Agitation > Solution > Social Proof > Features > CTA repeat > FAQ

Mark interactive placeholders: `<div data-placeholder="BuyBox" class="..."></div>`

Use `--lx-*` CSS variables in `theme_css` for all brand colors and fonts.

**Phase 4b — Island Mapping**

Replace placeholders with hydrated islands:
```html
<lx-island name="BuyBox">
  <script type="application/json">
    { "product": { "title": "...", "price": "$29.99", "variants": [] } }
  </script>
</lx-island>
```

Use `get_island_schema` for exact prop shapes.

### Step 5 — Validate and Publish Draft

```
compile_page_source({ source, head, theme_css, scripts })
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
```

Always publish as draft first. Returns `preview_url`.

### Step 6 — Visual Verification

Use Codex Browser to open `preview_url`, capture desktop and mobile screenshots, and inspect the rendered result. If Browser is unavailable, provide the preview URL and state that visual verification remains manual.

Checklist:
- [ ] Hero headline matches ad headline (scent continuity)
- [ ] Brand colors applied via `--lx-*` variables (not defaults)
- [ ] Single CTA focus (no nav leakage)
- [ ] Mobile layout not broken (stack, readable text)
- [ ] Islands hydrated (BuyBox shows product data)
- [ ] Social proof section present

If issues found: `update_section_from_source` to fix, then re-verify.

## Decision Points

| Question | Decision |
|----------|----------|
| Which ad? | Ask user, or highest-spend active creative |
| Which product? | Extract from ad analysis (primary product) |
| Draft or live? | Always draft first -- user confirms |
| Long or short? | Video ad = longer storytelling; static = concise |
| Include pricing? | Only if ad mentions price/discount explicitly |

## Quality Gates

- Hero headline >=80% semantic similarity to ad headline
- Color palette matches ad dominant colors (set via `--lx-accent-color`)
- Single primary CTA throughout (no competing actions)
- Mobile-first layout (most ad traffic is mobile)
- No navigation links that leak traffic from conversion
- Ad urgency signals carried through (countdown, limited stock, etc.)
- Page passes `compile_page_source` with zero errors


# Competitor Remix (Rebuild from Reference URL)

Capture a competitor page, decompose its structure, and rebuild it using the user's own brand identity, copy, and products. NEVER copy content -- only structural inspiration.

## Prerequisites

- User provides a reference URL
- Store connected and brand kit configured
- User's own product/content available to replace competitor's

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Capture Reference Design

```
capture_design_source({ url })
```

Screenshots the page and extracts structural layout data.

The agent should analyze the screenshot to extract the competitor's design DNA: color palette, typography, spacing rhythm, border radius, shadow depth, image treatment style, overall aesthetic (minimal, bold, editorial, etc.).

### Step 3 — Decompose into Section Map

Analyze captured page into numbered section breakdown:
```
1. Full-bleed hero — product centered, headline overlay, gradient wash
2. Trust badge row — 4 icons with micro-labels, centered
3. Split feature section — image left, text right, 50/50
4. Testimonial carousel — 3 cards, star ratings, photos
5. Product grid — 3 columns, hover zoom
6. FAQ accordion — 6 items, expandable
7. Final CTA — full-width, contrasting background
```

For each: note layout pattern, content type, approximate proportions, interactive elements.

### Step 4 — Map to Lexsis Capabilities

For each competitor section:
- Island available? Use `get_island_schema(island_name)` for prop shapes
- Static HTML+Tailwind section? (most common)
- Requires custom interactivity? Flag for JS sandbox

### Step 5 — Source User's Own Assets

```
search_design_library({ query: "<relevant product/category>" })
list_products({ limit: 10 })
```

Replace ALL competitor imagery with user's own assets. Generate new if needed:
```
generate_asset({ prompt: "...", style_reference: "brand_kit" })
```

CRITICAL: NEVER reference, hotlink, or reuse competitor images/copy/logos.

### Step 6 — Two-Phase Generation

**Phase 4a — Raw HTML + Tailwind (no islands)**

For each section from the decomposition:
- **Structure**: Keep competitor's layout pattern (grid, split, stacked)
- **Brand**: Replace ALL colors/fonts/spacing with user's `--lx-*` variables
- **Content**: Write original copy serving user's value proposition
- **Images**: User's own assets exclusively
- **CTAs**: Aligned with user's conversion goals

Set all brand tokens in `theme_css`:
```css
:root { --lx-accent-color: #...; --lx-font-heading: '...', serif; }
```

Mark interactive placeholders: `<div data-placeholder="BuyBox" class="..."></div>`

**Phase 4b — Island Mapping**

Replace placeholders with hydrated islands:
```html
<lx-island name="BuyBox">
  <script type="application/json">
    { "product": { "title": "...", "price": "$29.99", "variants": [] } }
  </script>
</lx-island>
<lx-island name="FAQ">
  <script type="application/json">
    { "items": [{ "question": "...", "answer": "..." }] }
  </script>
</lx-island>
```

### Step 7 — Validate and Publish Draft

```
compile_page_source({ source, head, theme_css, scripts })
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
```

Returns `preview_url`.

### Step 8 — Visual Verification

Use Codex Browser to open `preview_url`, capture desktop and mobile screenshots, and compare the rendered result with the reference structure. If Browser is unavailable, provide the preview URL and state that visual verification remains manual.

Checklist:
- [ ] ZERO competitor content carried over (no copy, images, logos)
- [ ] All colors from user's `--lx-*` variables (not competitor palette)
- [ ] Structural similarity recognizable but not pixel-perfect
- [ ] User's brand fonts loading (not system fallback)
- [ ] Mobile layout works independently
- [ ] Islands hydrated with user's own product data
- [ ] Original copy serves user's value proposition

If issues found: `update_section_from_source` to fix, then re-verify.

## Decision Points

| Question | Decision |
|----------|----------|
| Keep exact structure or adapt? | Adapt: remove irrelevant sections, add where user has more to say |
| Which sections to skip? | Competitor-specific (their awards, team), navigation that does not fit |
| How close to follow? | Structural only -- proportions, flow, section types |
| Interactive elements? | Map to available islands; static equivalent if no island exists |

## Quality Gates

- ZERO competitor content (copy, images, logos, brand marks)
- Page uses exclusively user's `--lx-*` CSS variables
- All images are user's own or freshly generated
- All product references from user's own catalog
- Copy is original, serving user's value proposition
- Mobile layout independent (do not assume competitor's responsive approach)
- Page passes `compile_page_source` with zero errors

---

# Skill: search-docs

> Search Lexsis storefront documentation — islands, skills, conversion patterns, verticals, workflows, tools, and troubleshooting. Use when you need to look up how something works before generating or editing.

# Search Lexsis Documentation

Search documentation, skill knowledge, island patterns, and industry guidance via the MCP.

## When to Use

- Before generating: look up island props, variant names, content schemas
- For vertical/industry patterns: "beauty hero patterns", "supplements trust signals"
- For conversion techniques: "urgency patterns", "social proof placement"
- For workflow steps: "how to publish", "A/B test setup"
- For troubleshooting: "island not rendering", "publish fails"
- When unsure which island to use for a UI pattern

## Workflow

1. Call `search_docs` with the user's query (or your own lookup query)
2. If results reference a skill by name, read it via `vibe://skills/{skillName}` resource for full content
3. If results reference an island, read `vibe://catalog/islands/{name}` for schema + props + variants
4. Synthesize relevant findings — don't dump raw results, extract what's actionable

## Tool Usage

### Primary search
```json
{ "name": "search_docs", "arguments": { "query": "<search terms>", "limit": 5 } }
```

### Narrow by category
Use `category` to focus results:
- `islands` — interactive component schemas, props, variants
- `tools` — MCP tool documentation and parameters
- `recipes` — end-to-end workflows (ad-to-page, A/B testing, brand setup)
- `vibe-page` — page schema, theming, animations, publishing
- `skills` — conversion psychology, craft guide, generation protocols, verticals
- `verticals` — industry-specific patterns (beauty, supplements, fashion, food, home, luxury)
- `troubleshooting` — common issues and fixes
- `getting-started` — setup, auth, quickstart
- `resources` — MCP resources reference

### Deep-read a skill
Read resource URI: `vibe://skills/{skillName}`
Returns full markdown content of the skill file.

Available skills: craft-guide, conversion-psychology, generation-protocol, workflow-orchestration, island-patterns, visual-craft, premium-patterns, animation-system, design-enrichment, qa-recipe, vertical-beauty, vertical-fashion, vertical-food, vertical-home, vertical-luxury, vertical-supplements, cart-composition, cart-v2-management

### Deep-read an island
Read resource URI: `vibe://catalog/islands/{islandName}`
Returns schema with all props, variants, and usage hints.

## Examples

| User asks | Search call | Follow-up |
|-----------|------------|-----------|
| "How does BuyBox work?" | `search_docs({ query: "BuyBox", category: "islands" })` | Read `vibe://catalog/islands/BuyBox` |
| "Beauty landing page patterns" | `search_docs({ query: "beauty landing page", category: "verticals" })` | Read `vibe://skills/vertical-beauty` |
| "Countdown urgency techniques" | `search_docs({ query: "countdown urgency scarcity" })` | — |
| "Publishing workflow" | `search_docs({ query: "publish page workflow", category: "recipes" })` | Read `vibe://skills/publishing` |
| "What islands handle reviews?" | `search_docs({ query: "reviews testimonials", category: "islands" })` | Read `vibe://catalog/islands/ReviewCarousel` |

## Tips

- Use specific terms, not vague questions — "BuyBox variant swatches" not "how to show products"
- Combine category filter with query for best results
- If search returns nothing, try broader terms or drop the category filter
- Skill resources contain full implementation guides — always read them when referenced

---

# Skill: storefront-engine

> Orchestrator for Lexsis AI storefront page generation. Routes broad or multi-step requests to the right workflow (generate, optimize, remix, experiment, cart, publish), sequences MCP tools, and loads reference knowledge on demand. Prefer a focused workflow skill when one clearly matches.

# Storefront Engine — Workflow Orchestration

The routing and orchestration layer for Lexsis AI storefront operations. Use it for broad requests that span several workflows or when no focused skill is a clear match.

## How This Works

1. **Focused skills** handle generate, optimize, remix, experiments, Cart V2, publishing, CRO analysis, and page building. Select one when its scope matches.
2. **Reference files** in `references/` contain deep knowledge — load ONLY what the selected workflow needs, never all at once.
3. **Island schemas** in `references/islands/{name}/schema.json` — full prop types, parts, examples, anti-patterns.
4. For URL analysis, use a browser tool when available (see `browser-analyze`); otherwise use Lexsis server-side design extraction.

All page work follows one contiguous sequence: **Phase 1 Plan → Phase 2 Context → Phase 3 Assets → Phase 4 Build → Phase 5 Ship.**

---

## Phase 1: Page Planning (MANDATORY)

> Do NOT skip this phase. Do NOT proceed to Flow Selection until a plan is approved.
> Skip ONLY if: user is editing an existing page, a CRO_BLUEPRINT is already provided, or user explicitly says "skip planning" / "just build it".

### Step 1 — Assess What's Known

Score the user's input:

| Signal | Check |
|--------|-------|
| Page type (landing, PDP, homepage, collection, editorial, listicle, bundle) | stated? |
| Target audience / persona | described? |
| Products or collection to feature | named? |
| Traffic source (Meta, Google, TikTok, email, organic) | mentioned? |
| Conversion goal (purchase, signup, browse) | clear? |
| Reference URL or ad creative | provided? |
| Tone/style preference | specified? |

- **4+ signals present** → proceed to Step 3 (auto-plan)
- **< 4 signals** → proceed to Step 2 (ask questions)

### Step 2 — Adaptive Discovery

Ask ONLY questions whose answers are missing. Never ask more than 4 at once.

**Tier 1 (always ask if missing):**
1. "What type of page?" (landing / PDP / homepage / collection / editorial)
2. "Who is this for?" (audience: demographics + pain point)
3. "What should visitors do?" (single conversion goal)

**Tier 2 (ask if Tier 1 reveals complexity):**
4. "Where does traffic come from?" (impacts visual density + social proof weight)
5. "Any sections you specifically want?" (hero style, FAQ, comparison table, etc.)
6. "Should this feel bold/energetic or minimal/premium?" (visual approach)
7. "Any animations or scroll effects?" (parallax, reveal-on-scroll, sticky elements)

**Follow-up triggers:**
- Multiple products mentioned → "Which is the hero product? Are others cross-sells or equals?"
- Health/beauty vertical → "Do you have clinical data or certifications to feature?"
- Ad creative provided → "Should the page match the ad's exact style, or just the message?"

### Step 3 — Generate Page Plan

Produce a structured plan covering:

**A. Section Sequence** (ordered list) — for each section: section ID + type, purpose, key content, island requirement, animation.

**B. Visual Rhythm** — spacing pattern, color temperature flow, typography hierarchy.

**C. Inter-Section Communication** — narrative thread, CTA placement strategy, social proof distribution, scroll incentives.

**D. Technical Requirements** — islands needed (exact list), custom animations, asset requirements.

### Step 4 — Present Plan for Approval

```
📋 Page Plan: [Page Type] for [Audience]

Goal: [Conversion goal]
Sections: [N] | Islands: [list] | Style: [visual approach]

Section Layout:
1. [hero-split] — Hook headline + product image + primary CTA
   Animation: fade-up on load
2. [trust-bar] — Star rating + press logos + "X customers served"
   Animation: none (instant credibility)
...

Visual Flow: [spacing + color temperature description]
CTA Strategy: [where + how many]

Proceed with this plan? (Or tell me what to change)
```

Wait for user confirmation. If the user suggests changes, update the plan and re-present.

### Step 5 — Hand Off

Once approved, the plan is the binding blueprint: Phase 2 context gathering targets its requirements, Phase 3 assets follow its imagery needs, Phase 4 HTML follows its section sequence EXACTLY.

---

## Flow Selection

```
What did the user provide?
│
├─ Ad creative (image URLs / screenshot)
│  → AD-TO-PAGE FLOW (analyze creative → extract style → generate matched page)
│
├─ Reference URL (competitor / inspiration)
│  → DESIGN-FIRST FLOW (browser screenshots URL → extract tokens → use as theme → generate)
│
├─ Brand brief only (name, industry, tone)
│  → STANDARD FLOW (Phases 1-5)
│
├─ Existing page (wants edits)
│  → EDIT FLOW (read page → modify sections → validate → write)
│
├─ Product focus (PDP, collection)
│  → PRODUCT FLOW (list_products first → build around real product data)
│
└─ Multiple inputs (ad + products + brand)
   → STANDARD FLOW with enriched context
```

---

## Standard Flow

### Phase 2: Context Gathering ✅ ALL PARALLEL

Fire simultaneously — no dependencies:

```
┌─ get_storefront_skills({ brief, page_type })    → system prompt + island catalog + schema
├─ get_design_md()                                 → brand voice/guidelines
├─ list_products(limit: 10)                        → product catalog (names, images, prices)
├─ search_design_library({ query: "hero" })        → existing brand assets
├─ get_navigation()                                → nav links (check `status` — if not_synced/empty, ask the user)
└─ get_connected_stores()                          → store_id (for publish later)
```

### Phase 3: Asset Preparation ✅ PARALLEL PER SECTION

Full multi-source strategy (library → generate → import → external MCPs): see the `asset-prep` skill or `references/asset-prep.md`.

Decision tree per image:
1. `search_design_library` first — if the brand has relevant assets, USE THEM
2. No match → `generate_asset` (write your own descriptive prompt)
3. Product-on-background → `edit_asset` with product image + background
4. Transparent overlay → `generate_asset` with `transparent: true`
5. User has their own file → `import_asset` with no arguments (opens an upload picker)

Collect all image URLs before Phase 4.

### Phase 4: Build (Agent writes source-format HTML)

1. Generate `theme_css` with `compile_theme` (brand tokens → WCAG-checked CSS vars)
2. Write each section as plain HTML (Tailwind classes + CSS vars), delimited by `<!-- section: id -->`
3. Place `<lx-island name="X">` elements (props as a JSON `<script>` child) where interactive commerce is needed — see `references/source-format.md`
4. Embed asset URLs directly in `<img src="...">` and `background-image`
5. Add a section `<style>` block only for custom keyframes/animations (or use `data-behavior="gsap-*"` presets)
6. Add a section `<script>` block only for custom scroll/DOM work

Sub-steps (see `references/generation-protocol.md`): **4a — draft source HTML** (structure, copy, islands in place), then **4b — compile & fix** (`compile_page_source` reports issues; fix and re-compile).

### Phase 5: Validate + Ship ❌ SEQUENTIAL

```
compile_page_source({ source, head, theme_css, scripts })  → compiled page + issues; fix and re-compile
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })  → draft + preview URL
```

Report the preview URL. Call `publish_page` ONLY after the user explicitly says to go live.

---

## Ad-to-Page Flow

```
Phase 2: analyze_ad_creative({ image_urls }) + get_storefront_skills + list_products
Phase 3: use ad creative images directly; generate_asset / edit_asset for the rest
Phase 4-5: Standard Flow
```

## Design-First Flow (Reference URL)

```
Phase 2: browser screenshots URL → extracted palette/fonts/spacing + get_storefront_skills + list_products
Phase 3-5: Standard Flow, with extracted tokens as the theme_css base
```

## Edit Flow (Safe Iteration)

```
1. find_page({ query })                                   → locate page
2. get_page_source({ page_id })                           → read round-trip source
3. inspect_page_sections({ page_id })                     → inspect current sections
4. update_section_from_source({ page_id, source })        → compile, preflight, commit
5. check_page_integrity({ page_id, archetype })           → structural QA
6. [Optional] diff_page_versions / rollback_page_version
```

**Key rules:** source updates preflight before writing; run integrity after all edits; rollback creates a forward version, preserving history.

---

## Reference Files

Load with `Read references/{name}.md` when you need specific knowledge. Do NOT load all at once.

### Knowledge (domain expertise)
- **generation-protocol.md** — Page generation rules, constraints, quality gates, Phase 4a/4b detail
- **cro-research.md** — Conversion rate optimization research and data (2026)
- **storefront-craft.md** — Load FIRST on any page generation task. Core craft principles.
- **workflow-orchestration.md** — Tool sequences, parallelization, flow selection
- **conversion-psychology.md** — AIDA framework → section order mapping
- **visual-craft.md** — Premium visual techniques. Load when polishing quality.
- **island-patterns.md** — How to embed, wrap, and combine React islands
- **premium-patterns.md** — Copy-and-adapt HTML+Tailwind patterns for high-converting sections
- **animation-system.md** — CSS-only + IntersectionObserver animations. No framer-motion.
- **design-enrichment.md** — generate_asset, edit_asset, view_asset prompt patterns
- **asset-prep.md** — Multi-source asset strategy (library, generation, import, external MCPs)
- **qa-recipe.md** — Validation, integrity checks, screenshot QA workflow
- **reference-pdp-remix.md** — PDP reference site patterns and adaptation

### Verticals
vertical-beauty, vertical-supplements, vertical-fashion, vertical-food, vertical-home, vertical-luxury

### Traffic Sources
traffic-source-meta, traffic-source-google, traffic-source-tiktok

### Island Reference
- **islands/_contract.md** — Rules ALL island wrappers must follow
- **islands/{name}/schema.json** — Full props, variants, examples, anti-patterns (one per island)
- **islands/{name}/layouts/*.json** — Pre-built renderer-compatible section templates

### Operational (workflow procedures)
page-generation, design-assets, publishing, page-editing, analytics, generate-pdp, generate-landing-page, generate-homepage, generate-collection, generate-listicle, generate-bundle-page, generate-editorial, ad-to-page, page-redesign, competitor-remix, personalization-variant, ab-test-variant, section-library, cart-composition, cart-v2-management

---

## Reference Knowledge

---

# Storefront Craft Guide — Start Here

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then run `compile_page_source`.

Load this skill first on any storefront page generation task.

---

## Architecture: Vibe-Code

Pages are **raw HTML + Tailwind CSS + CSS custom properties + React islands**. No component JSON. No blueprint system. The AI generates HTML directly.

**VibePage schema:**
```json
{
  "head": { "title": "Page Title", "fonts": ["https://fonts.googleapis.com/..."] },
  "theme_css": ":root { --lx-accent-color: #4F46E5; ... }",
  "sections": [
    { "id": "hero", "html": "<section class='...'>...</section>", "css": ".custom { ... }", "js": "// vanilla JS" }
  ]
}
```

**Islands** = interactive React components hydrated at `data-island` markers in HTML:
```html
<div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart"}'></div>
```

---

## Skills Map

| Skill | Purpose | Load when... |
|---|---|---|
| `craft-guide` | This file — architecture, flow, quality bar | Always first |
| `workflow-orchestration` | Tool sequencing, parallelization, flow selection | Always — load after craft-guide |
| `conversion-psychology` | Universal persuasion: pricing, urgency, trust, CTA psychology | Always — load for any ecommerce page |
| `animation-system` | CSS animations, scroll-reveal, headline effects | Adding motion to sections |
| `visual-craft` | Typography, spacing, color, micro-interactions | Polishing visual quality |
| `design-enrichment` | AI image generation + compositing pipeline | Need custom images/textures |
| `premium-patterns` | Proven high-converting section patterns in HTML | Building hero, trust, CTA sections |
| `island-patterns` | Per-island wrapper HTML + combination recipes | Using commerce/engagement islands |
| **Verticals** | | |
| `vertical-beauty` | Beauty/skincare: ingredient storytelling, before/after, editorial | Beauty, skincare, haircare, fragrance |
| `vertical-supplements` | Supplements: dark mode, clinical proof, comparison, urgency | Vitamins, protein, nootropics, fitness |
| `vertical-fashion` | Fashion: editorial layouts, lookbook grids, dramatic type | Clothing, shoes, accessories, streetwear |
| `vertical-food` | Food/bev: sensory photography, warm palettes, subscription | Food, coffee, snacks, meal kits |
| `vertical-luxury` | Luxury: restraint, whitespace, minimal sections, quiet CTAs | Jewelry, watches, designer, AOV>$300 |
| `vertical-home` | Home: room context, dimensions, material stories | Furniture, decor, candles, textiles |
| **Traffic Sources** | | |
| `traffic-source-meta` | Meta ads: message match, mobile-first, trust stacking | Facebook/Instagram ad landing pages |
| `traffic-source-google` | Google: intent matching, info density, CompareTable, FAQ | Google Ads/SEO landing pages |
| `traffic-source-tiktok` | TikTok: 3-sec hook, video-first, UGC aesthetic, 6-8 sections | TikTok/Reels/Shorts traffic |
| **Workflows** | | |
| `reference-pdp-remix` | Competitor PDP deconstruction and rebuild | Rebuilding a reference URL for your brand |

---

## Generation Flow (Overview)

```
1. get_storefront_skills({ brief, page_type }) → system prompt, island catalog, schema
2. [Optional] search_design_library() → find existing brand assets
3. [Optional] generate_asset(prompt, style, purpose) → get image URLs
4. Agent authors source-format HTML with `<lx-island>` components
5. compile_page_source({ source, head, theme_css, scripts }) → compile + validation
6. create_page_from_source({ source, head, theme_css, scripts, slug, publish: false }) → persist as draft, returns preview URL
7. publish_page({ page_id }) → go live (ONLY after the user explicitly approves)
```

---

## CSS Variables (Brand Theming)

All sections use these CSS custom properties (set in `theme_css`):

| Variable | Purpose |
|---|---|
| `--lx-accent-color` | Primary brand/CTA color |
| `--lx-accent-color-hover` | Hover state |
| `--lx-text-color` | Primary text |
| `--lx-text-muted` | Secondary text |
| `--lx-bg-color` | Page background |
| `--lx-bg-surface` | Card/section background |
| `--lx-border-color` | Borders and dividers |
| `--lx-font-heading` | Heading font family |
| `--lx-font-body` | Body font family |

Use via `style="color: var(--lx-accent-color)"` or `style="font-family: var(--lx-font-heading)"`.

---

## Quality Bar

**Great page:**
- Mobile-first (works at 375px, enhances at lg:)
- Uses CSS vars for all brand colors/fonts (no hardcoded hex)
- Proper heading hierarchy (h1 → h2 → h3)
- Islands for all interactive commerce (BuyBox, Cart, Reviews)
- Generated/library images — no broken placeholder URLs in production
- Smooth scroll reveal on key sections
- Trust signals near purchase points
- Sticky add-to-cart on PDP

**Mediocre page:**
- Hardcoded colors instead of CSS vars
- Desktop-only layout
- Missing islands (raw HTML buttons instead of BuyBox)
- placeholder.co images shipped to production
- No animations or visual rhythm
- Trust badges missing

---

## Anti-Patterns (NEVER do these)

1. **No `fetch()` or XHR in section JS** — blocked by hydrator security
2. **No `eval()`, `localStorage`, `WebSocket`** — blocked
3. **No `@import` in section CSS** — blocked
4. **No external `url()` in CSS** — only inline gradients/colors
5. **No duplicate section IDs** — each must be unique kebab-case
6. **No `<script src="...">` in HTML** — use section `js` field for vanilla JS
7. **No framework code** — no React/Vue/Angular in section HTML (islands handle interactivity)
8. **Don't fake commerce** — always use BuyBox island for add-to-cart, never a plain button

---

## Section ID Naming

Use descriptive kebab-case: `hero`, `product-gallery`, `social-proof`, `ingredients`, `faq`, `sticky-cta`, `trust-badges`, `footer`. Never `section-1`, `section-2`.

---

## Island Rules

- `data-props` must be valid JSON in single-quoted attribute
- Only use valid island names (26 total — call `get_island_catalog` to see them)
- One `BuyBox` per page (multiple breaks cart state)
- Cart: `head.use_cart_v2: true` on every commerce page (`CartDrawer` V1 deprecated — never author a cart section)
- `StickyBar` needs `triggerOffset` — distance in px before it appears
- `ReviewCarousel` can use custom reviews array OR fetch from Shopify via productId

---

## Tailwind Usage

- CDN included in renderer — all utility classes available
- Use responsive prefixes: `sm:`, `md:`, `lg:`, `xl:`
- Prefer utilities over custom CSS (only use section `css` for keyframes/animations)
- Use `clamp()` for fluid typography: `text-[clamp(2rem,5vw,4rem)]`
- Container: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`

---

## Image Strategy

1. **Always check `search_design_library` first** — brand's uploaded assets are free and on-brand
2. **Use `list_products` for product images** — never generate fake product shots
3. **`generate_asset` for custom imagery** — hero backgrounds, lifestyle contexts, textures
4. **`edit_asset` for composites** — product-on-background, texture overlays
5. **Place URLs directly in HTML** — `<img src="${url}" />` or inline `style="background-image: url(...)"`
6. **Load `design-enrichment` skill** for full asset generation pipeline details
7. **For video, reference imagery, or external AI tools** → see `asset-pipeline.md` for multi-source strategy

---

# Generation Protocol — How Pages Are Built

> This is the canonical reference for how AI agents generate storefront pages using the Lexsis AI MCP. All operational skills reference this protocol.

> **Compiled runtime reference:** any `data-island` or `data-props` snippets in
> storage-format examples below are renderer output, not page source. New pages
> use `<lx-island>` with a JSON script child as defined in `source-format.md`.

---

## MCP Workflow (Correct Order)

```
1. get_workspace_details      → workspace ID, plan tier
2. get_connected_stores       → store domain, Shopify data
3. get_brand_kit              → logo, fonts, colors, voice, border radius
4. get_design_md              → brand brief, design philosophy, don'ts
5. [page-type specific tools] → products, navigation, ad creatives, etc.
6. compile_theme              → WCAG-checked --lx-* theme_css from brand colors
7. Generate page (two-phase, SOURCE FORMAT — see source-format.md)
8. compile_page_source        → dry-run compile + validation issues
9. create_page_from_source    → persists page, returns preview_url
10. Visual verification       → screenshot and verify
```

Steps 1-4 are ALWAYS run first. They establish context. Steps 5+ vary by skill.

> **Brand kit ↔ design.md precedence**: when the two disagree, **exact tokens (colors, fonts, radius, spacing values) come from the brand kit**; **style philosophy, component guidance, and explicit don'ts come from design.md**. Conflict on a token → use the kit's value, applied within design.md's don'ts. Don't stall trying to reconcile them.

> **Authoring format**: write pages in the HTML-native **source format** (`source-format.md`) — plain HTML sections delimited by `<!-- section: id -->`, islands as `<lx-island name>` with a JSON `<script>` child. The compiler produces VibePage JSON and does all escaping.

> **Templates**: search before drafting. Retrieve templates you intend to edit
> with `get_section_template({ ids })`. Each returned `source` is ready for
> editing and compiling. `format: "compiled_reference"` is renderer output and cannot be passed directly to
> source-authoring tools.

---

## Two-Phase Generation (Fast Iteration Pattern)

### Phase 4a — Draft Source HTML

Generate the FULL page as source-format HTML first:
- Plain HTML + Tailwind, sections delimited by `<!-- section: id -->`
- Focus on layout, visual hierarchy, spacing, typography
- Write all copy naturally — apostrophes/quotes need no escaping
- Set all colors via `--lx-*` CSS variables (from `compile_theme`)
- Mobile-first responsive; shared keyframes or `data-behavior="gsap-*"` presets for animation
- Islands go in directly as `<lx-island name="BuyBox">` with a JSON `<script>` child — use `get_island_schema({island_name})` for exact prop shapes

### Phase 4b — Compile & Fix

Run `compile_page_source { source, head, theme_css, scripts }`:
- Returns the compiled VibePage + compile issues + publish validation
- Fix reported issues in the source (unknown islands, bad props, missing hooks) and re-compile
- When clean, `create_page_from_source` persists it (the agent-authored source is stored too, retrievable via `get_page_source` for later edits)

### Why Two-Phase?
- Source HTML renders in any browser preview — fast visual feedback
- Compile is instant and deterministic — validation before anything persists
- Separates design decisions from data-wiring decisions
- Escaping failures are impossible: the compiler, not the model, writes `data-props`

---

## VibePage JSON Structure (storage format — compiler output)

> You do not write this by hand. The source-format compiler produces it as the storage and rendering format.

```json
{
  "head": {
    "title": "Page Title — Brand Name",
    "fonts": ["https://fonts.googleapis.com/css2?family=..."],
    "use_cart_v2": true
  },
  "theme_css": ":root { --lx-accent-color: #4F46E5; --lx-font-heading: 'Playfair Display', serif; }",
  "sections": [
    { "id": "hero", "html": "<section>...</section>", "css": "...", "js": "..." }
  ]
}
```

### Rules
- **Tailwind CSS** in HTML class attributes (renderer includes Tailwind CDN)
- **CSS Variables** (`--lx-*`) for all brand colors/fonts — set in `theme_css` (generate with `compile_theme`)
- **Islands** compile to `data-island="Name"` + `data-props='JSON'` attributes (in source format, write `<lx-island>` instead)
- **Section IDs** must be unique, kebab-case: "hero", "social-proof", "faq"
- **Section JS** is sandboxed — no fetch/XHR/eval/localStorage. Only DOM manipulation + IntersectionObserver. Runs after immediate islands mount; `lx:hydrated` / `lx:islands-ready` events signal island readiness
- **Shared keyframes** already loaded: fadeUp, fadeIn, scaleIn, slideInLeft, slideInRight, marquee, float, shimmer, wordFade, pulseRing. GSAP presets via `data-behavior="gsap-reveal|gsap-parallax|gsap-pin|gsap-marquee-scroll"`
- **No @import, no external URLs in CSS**; external JS libs go in `scripts[]`, never section HTML

### Available CSS Variables (override in theme_css)
| Variable | Default | Purpose |
|----------|---------|---------|
| `--lx-accent-color` | #5055aa | Primary CTA color |
| `--lx-accent-color-hover` | #4045aa | Hover state |
| `--lx-text-color` | #1a1a2e | Primary text |
| `--lx-text-muted` | #6b7280 | Secondary text |
| `--lx-bg-color` | #ffffff | Page background |
| `--lx-bg-surface` | #ffffff | Card backgrounds |
| `--lx-border-color` | #e5e7eb | Borders/dividers |
| `--lx-font-heading` | system-ui | Heading font |
| `--lx-font-body` | system-ui | Body font |
| `--lx-surface-alt` | #f9fafb | Alternating section bg |
| `--lx-lavender` | #c9b8e8 | Secondary accent |
| `--lx-teal` | #5bc8c0 | Tertiary accent |

---

## Visual Verification (Critical Step)

After `create_page_from_source` returns a `preview_url`, ALWAYS verify visually.

### For Claude Code (Playwright MCP)

Install: https://playwright.dev/docs/getting-started-mcp

Add to Claude Code MCP config:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Then:
```
1. browser_navigate → preview_url
2. browser_take_screenshot({fullPage: true}) → full page capture
3. Review: layout, spacing, mobile responsiveness, broken images
4. If issues found → `update_section_from_source({ page_id, source })` → re-verify
```

### For Codex (Built-in Browser)

Use the built-in browser tool to open the preview URL and visually inspect.

### For Cursor / Other IDEs

If no browser tool available, instruct user:
- "Preview URL: {url} — open in browser to verify"
- Suggest mobile viewport check (375px width)

### Installation Reference

Playwright MCP docs: https://playwright.dev/docs/getting-started-mcp

### What to Check
- [ ] Hero section visible above fold (no scroll needed for headline + CTA)
- [ ] Brand colors applied (not default purple)
- [ ] Fonts loading (not system fallback)
- [ ] Images rendering (not broken placeholders)
- [ ] Mobile layout not broken (stack columns, readable text)
- [ ] Islands hydrated (BuyBox shows product, not empty div)
- [ ] CTA buttons have proper contrast (WCAG AA: 4.5:1 min)
- [ ] No horizontal scroll on mobile
- [ ] Section spacing consistent (not cramped or overly spaced)

---

## Island Integration Reference

Islands are React components that hydrate client-side. They handle interactive commerce functionality.

### How to Embed
```html
<div data-island="IslandName" data-props='{"key": "value"}'></div>
```

### Key Islands by Use Case

| Need | Island | Key Props |
|------|--------|-----------|
| Add to cart | BuyBox | product.title, product.price, product.variants |
| Product images | ProductGallery | images[], layout |
| Cart drawer | DrawerShell | Contains CartLines + CartCheckoutButton |
| Reviews | ReviewCarousel | provider, productId |
| FAQ accordion | FAQ | items[{question, answer}] |
| Email capture | EmailCapture | provider, listId |
| Announcement | AnnouncementBar | message, link, dismissible |
| Navigation | Navbar / SiteHeader | links[], logo |
| Footer | Footer | links[], social[], newsletter |
| Product grid | EditorialProductGrid | products[], columns |
| Trust badges | TrustBadgeBar | badges[{icon, text}] |
| Social proof popup | SocialProofPopup | provider, delay |

### Prop Data Sources
- Product data → `get_product(product_id)` or `list_products`
- Navigation → `get_navigation`
- Reviews → configured in store (no manual data needed)
- Brand tokens → `get_brand_kit`

---

## Deprecated Tools (DO NOT USE)

These tools appeared in older skill versions but are no longer available:

| Removed | Replacement |
|---------|-------------|
| `get_theme_json` | `get_brand_kit` (includes theme data) |
| `provision_store` | Handle via onboarding flow, not page generation |
| `extract_brand_design` / `capture_design_source` / `list_design_sources` | No replacement — no MCP tool for reference-URL design extraction currently exists |
| `search_section_templates` returning `html`/`css`/`js` inline | Search is metadata-only now; call `get_section_template({ ids })` for compile-ready source |

`get_island_catalog` and `get_island_schema` remain active tools — use them for island discovery and schema lookups, alongside the `vibe://catalog/islands` resource.

---

## Quality Gates (Before Publishing)

1. **compile_page_source** — compile and validate source before creating a page
2. **check_page_integrity** — archetype-specific rules (recommended)
3. **Visual verification** — browser screenshot (required for final delivery)

If `compile_page_source` fails → fix source errors → re-compile.
If `check_page_integrity` warns → assess if acceptable → proceed or fix.
If visual check fails → `update_section_from_source` → re-screenshot.

---

# Source Format — HTML-Native Page Authoring (V2)

> **This is the preferred way to author pages.** Write plain HTML with `<lx-island>` elements; the `compile_page_source` / `create_page_from_source` tools compile it to VibePage JSON deterministically. Never hand-write `data-island` / `data-props` attributes or escape HTML into JSON strings — the compiler does all escaping for you.

## Why this format exists

The old path (VibePage JSON with HTML in strings and JSON inside `data-props='...'` attributes) forced triple escaping and caused the top agent failure classes: entity-escaped markup rendering as literal text, apostrophes in copy breaking props, giant-blob page updates. In source format those failures are impossible by construction.

## The format

```html
<!-- section: hero -->
<section class="py-12 md:py-16 lg:py-20" style="background-color: var(--lx-bg-color)">
  <h1 class="text-4xl md:text-5xl font-bold" style="font-family: var(--lx-font-heading)">
    Don't miss the "Summer Drop"
  </h1>

  <lx-island name="CountdownTimer" hydrate="visible">
    <script type="application/json">
      { "endDate": "2026-09-01T00:00:00Z", "variant": "flip" }
    </script>
  </lx-island>
</section>

<style>
  /* becomes section.css — scope selectors to this section */
  .hero-glow { box-shadow: 0 0 40px var(--lx-accent-color); }
</style>

<script>
  /* becomes section.js — sandboxed; `section` is bound to this section's element */
  section.querySelectorAll('.hero-glow').forEach(el => el.classList.add('ready'));
</script>

<!-- section: faq -->
<section class="py-12">
  <lx-island name="FAQ">
    <script type="application/json">
      { "items": [{ "q": "Can't I return it?", "a": "Yes — 30 days, no questions asked." }] }
    </script>
  </lx-island>
</section>
```

### Rules

1. **Sections** are delimited by `<!-- section: kebab-case-id -->` comments. Ids must be unique.
2. **Islands** are `<lx-island name="IslandName">` with props as a `<script type="application/json">` child. Write natural copy — apostrophes, quotes, em-dashes are all fine; no escaping needed.
3. **`<lx-island>` attributes**: `name` (required), `hydrate` (`immediate|visible|idle|interaction`), `headless` (headless mode — see below), plus `class`/`id`/`style` which pass through to the compiled element.
4. **Section CSS** goes in a top-level `<style>` block; **section JS** in a top-level `<script>` block (multiple blocks are concatenated). `application/json` / `ld+json` scripts stay in the HTML.
5. **External libraries** (GSAP etc.) do NOT go in section HTML — pass them via the `scripts` param of the compile tools.
6. **`head`, `theme_css`, `scripts`** are structured tool params, not part of the source. Generate `theme_css` with `compile_theme` (WCAG-checked palette from brand colors) instead of writing it by hand.

### Tool workflow

```
get_brand_kit → compile_theme { accent, bg, fonts... } → theme_css
draft source HTML (whole page)
compile_page_source { source, head, theme_css, scripts }   ← dry-run: compiled page + issues
fix any issues, then:
create_page_from_source { source, head, theme_css, scripts, slug, publish }
edits: update_section_from_source { page_id, source }      ← one section per call
round-trip: get_page_source { page_id } → edit → update_section_from_source
```

`update_section_from_source` compiles ONE section (delimiter optional — pass `section_id` if absent) and upserts it. Prefer it over whole-page rewrites: smaller payloads, no blob races.

## Starting From a Template

Search the section library before writing a section from scratch. When you pick
a template, request editable source:

```text
get_section_template({ ids: ["template-id"] })
```

The response's `source` is one complete source-format section: a delimiter,
`<lx-island>` markup, and the template CSS/JS. Tailor it, then run
`compile_page_source`.

`format: "compiled_reference"` is renderer output containing
`data-island` / `data-props`. It is useful for inspection but must never be
given to source-authoring tools.

## Headless islands (fully custom markup)

For maximum design freedom, add `headless` and author the island's internals yourself; behavior attaches to `data-lx-*` hooks. Currently supported: **BuyBox** (plus the long-standing Navbar/Footer/SiteHeader hydration modes — see island-patterns.md).

```html
<lx-island name="BuyBox" headless>
  <script type="application/json">
    { "product": { "title": "Serum", "price": "$49.00", "variants": [
      { "id": "v1", "title": "30ml", "price": "$49.00", "available": true },
      { "id": "v2", "title": "50ml", "price": "$69.00", "available": true }
    ] } }
  </script>

  <p class="text-3xl font-bold" data-lx-buybox="price">$49.00</p>
  <div class="flex gap-2">
    <button data-lx-buybox="variant-option" data-variant-id="v1" class="px-4 py-2 border rounded-full">30ml</button>
    <button data-lx-buybox="variant-option" data-variant-id="v2" class="px-4 py-2 border rounded-full">50ml</button>
  </div>
  <div class="flex items-center gap-3">
    <button data-lx-buybox="qty-dec">−</button>
    <span data-lx-buybox="qty">1</span>
    <button data-lx-buybox="qty-inc">+</button>
  </div>
  <button data-lx-buybox="add" class="w-full py-4 rounded-full text-white"
          style="background: var(--lx-accent-color)">Add to Cart</button>
  <p data-lx-buybox="error" class="text-red-600 text-sm">Couldn't add — try again.</p>
</lx-island>
```

### BuyBox hooks

| Hook | Required | Behavior |
|---|---|---|
| `add` | **yes** | add-to-cart trigger; gets `lx-adding` / `lx-added` classes |
| `price` | recommended | text kept in sync with selected variant/plan |
| `compare-price` | no | compare-at price; hidden when none |
| `variant-option` | no | one per variant, needs `data-variant-id="v1"`; gets `lx-selected` / `lx-disabled` |
| `qty` / `qty-inc` / `qty-dec` | no | quantity display (or `<input>`) + stepper |
| `stock` | no | availability text; override via `data-in-stock-text` / `data-out-of-stock-text` |
| `error` | no | revealed when add-to-cart fails |

Style the state classes in section CSS: `.lx-selected { ... }`, `.lx-adding { opacity: .6 }`, `.lx-disabled { pointer-events: none; opacity: .4 }`.

## Animations

### Presets (no JS needed) — `data-behavior`

```html
<section data-behavior="gsap-reveal" data-config='{"targets":".card","y":40,"stagger":0.1}'>
<div data-behavior="gsap-parallax" data-config='{"speed":0.3}'>
<section data-behavior="gsap-pin" data-config='{"stepDuration":0.5}'>  <!-- children: [data-pin-step] -->
<div data-behavior="gsap-marquee-scroll" data-config='{"distance":-200}'>
```

Presets lazy-load GSAP from CDN themselves and respect `prefers-reduced-motion`. Also available (CSS-driven, pre-existing): `scroll-reveal`, `accordion`, `horizontal-scroll`, `content-slider`, `sticky-reveal`.

### Custom GSAP in section JS

Load the library via the `scripts` param, then write timelines in the section `<script>`:

```json
"scripts": [
  { "src": "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js", "position": "body-end" },
  { "src": "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js", "position": "body-end" }
]
```

The compiler warns (`missing_animation_lib`) if section JS references gsap without either a scripts entry or a `gsap-*` preset on the page. Section JS runs after immediate islands mount; for work that depends on a deferred island, listen for its `lx:hydrated` event (bubbles, `detail.island`) or the document-level `lx:islands-ready`.

## What NOT to do

```html
<!-- ❌ hand-written island markers (old format — compiler rejects raw usage in source) -->
<div data-island="FAQ" data-props='{"items":[...]}'></div>

<!-- ❌ escaped HTML — never escape anything -->
&lt;section&gt;...&lt;/section&gt;

<!-- ❌ external scripts in section HTML — use the scripts param -->
<script src="https://cdn.example.com/lib.js"></script>
```

---

# Workflow Orchestration — Execution Engine

Load after `craft-guide`. Defines optimal tool sequences, parallelization rules, and flow selection.

---

## Flow Selection

```
What did the user provide?
│
├─ Ad creative (image URLs / screenshot)
│  → AD-TO-PAGE FLOW (analyze creative → extract style → generate matched page)
│
├─ Reference URL (competitor / inspiration)
│  → DESIGN-FIRST FLOW (agent screenshots URL → extracts tokens → uses as theme → generate)
│
├─ Brand brief only (name, industry, tone)
│  → STANDARD FLOW (context → assets → generate → validate → write)
│
├─ Existing page (wants edits)
│  → EDIT FLOW (read page → modify sections → validate → write)
│
├─ Product focus (PDP, collection)
│  → PRODUCT FLOW (list_products first → build around real product data)
│
└─ Multiple inputs (ad + products + brand)
   → STANDARD FLOW with enriched context
```

---

## Standard Flow (5 Phases)

See `generation-protocol.md` for the full Phases 1-5 execution protocol (context gathering, asset preparation, HTML generation, validation, publishing + visual verification).

---

## Ad-to-Page Flow

```
Phase 2: Context
├─ analyze_ad_creative({ image_urls, ad_format })  → visual signals, CTA, headline
├─ get_storefront_skills({ brief from ad analysis, page_type: "landing" })
└─ list_products()

Phase 3: Assets
├─ Use ad creative images directly where appropriate
├─ generate_asset for additional sections (testimonial bg, trust section bg)
└─ edit_asset to adapt ad images (crop, extend, composite)

Phase 4-4: Same as Standard Flow
```

---

## Design-First Flow (Reference URL)

```
Phase 2:
├─ Agent screenshots URL               → extracted palette, fonts, spacing, tone
├─ get_storefront_skills(brief)
└─ list_products()

Phase 3: Use extracted tokens as theme_css base
Phase 4-4: Same as Standard Flow
```

---

## Edit Flow (Safe Iteration)

```
1. find_page({ query })                              → locate page by handle/title/UUID
2. get_page_source({ page_id })                      → read round-trip source when available
3. inspect_page_sections({ page_id })                → inspect current compiled sections
4. Identify which sections to modify
5. update_section_from_source({ page_id, source })   → compile, preflight, commit
6. check_page_integrity({ page_id, archetype })           → structural QA pass
7. [Optional] diff_page_versions({ page_id, version_a, version_b })  → review all changes
8. [If broken] rollback_page_version({ page_id, target_version })    → revert to prior version
```

**Key rules:**
- `update_section_from_source` compiles and runs the full-page preflight before it writes
- Run `check_page_integrity` after all edits complete — catches archetype violations (e.g. PDP without BuyBox)
- Use `diff_page_versions` to verify your changes look correct before publishing
- Use `rollback_page_version` if integrity check fails — creates a new forward version, preserves history

---

## Duplication Flow (Idempotent)

```
1. find_page({ query })                                     → locate source page
2. duplicate_page({ page_id, handle, idempotency_key })     → safe clone (retries won't create extras)
3. Edit sections on the duplicate (use Edit Flow above)
4. check_page_integrity({ page_id, archetype })             → final QA
```

**Idempotency key:** Pass a deterministic string (e.g. `"${handle}-v2-from-${source_handle}"`) so that retrying the same operation returns the existing duplicate instead of creating another.

---

## Parallelization Rules

| Can parallelize | Cannot parallelize |
|---|---|
| All Phase 2 context calls | Phase 3 needs Phase 2 results (brand_colors for asset gen) |
| Multiple generate_asset calls | validate must complete before write |
| Asset gen for different sections | edit_asset needs source image URLs first |

---

## Cost Control

- `search_design_library` before `generate_asset` — existing assets are free
- Use `quality: "medium"` for most assets, `"high"` only for hero images
- One hero image + one lifestyle shot usually enough for a PDP
- Landing pages: hero + 2-3 section backgrounds max
- Skip asset gen for sections using solid color/gradient backgrounds

---

## Page Type Defaults

### PDP Sections (6-8)
```
hero (product gallery + buybox) → trust-badges → benefits → ingredients → reviews → faq → sticky-cta → cart-drawer
```

### Landing Page Sections (7-10)
```
hero → trust-bar → problem/solution → features → before-after → testimonials → pricing → faq → cta → exit-intent
```

### Homepage Sections (5-7)
```
hero → featured-products → brand-story → social-proof → collections → newsletter → footer
```

### Collection Sections (4-6)
```
collection-header → filters → product-grid → featured-pick → trust-bar → newsletter
```

---

## Credit Costs

Always call `get_credits_balance` before expensive operations. If balance is 0, inform the user before proceeding.

| Tool | Cost | Notes |
|------|------|-------|
| `generate_asset` | credits | AI image generation |
| `edit_asset` | credits | AI image editing/compositing |
| `create_page_from_source` | credits | Page generation (only on publish, not drafts) |
| `create_page_variation` | credits | A/B variant creation (requires Pro plan) |
| `create_ab_test` | credits | Experiment setup (requires Pro plan) |
| `update_section_from_source` | credits | Section regeneration |
| `compile_page_source` | FREE | Always validate before publishing |
| `check_page_integrity` | FREE | Structure/accessibility check |
| All read/list/get tools | FREE | No cost for browsing data |

**Preflight pattern:**
```
get_credits_balance → check cost → warn if insufficient → proceed or abort
```

Source-format pages persisted via `create_page_from_source` still cost credits (the write action, not the compiler, bills). Draft previews (`publish: false`) also consume credits.

---

# Conversion Psychology — Storefront Design Intelligence

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then run `compile_page_source`.

> When to load: ALWAYS. Read before generating any ecommerce page.

## The Conversion Stack (AIDA → Sections)

Map the AIDA framework to section order. Each stage requires specific psychology and placement.

### Short Page (5-7 sections) — Impulse / Low-consideration products

1. **Attention (1 section)**: Hero section
   - High-contrast gradient or bold product image
   - Benefit-driven headline (6-10 words)
   - `font-size: clamp(2.5rem, 5vw, 3.5rem)` for headline
   - Sticky CTA bar for persistent action

2. **Interest (2 sections)**: Value props + social proof stats
   - 3 icon-driven benefits max
   - Numbers: customer count, star rating, review count
   - `py-8 md:py-12` spacing

3. **Desire (2 sections)**: Reviews + transformation proof
   - Star-first review display, 3-6 reviews
   - Before/after images or testimonial carousel
   - `data-island="ReviewCarousel"` for dynamic trust

4. **Action (2 sections)**: CTA + footer
   - Urgency element (countdown or inventory indicator)
   - First-person CTA copy: "Get MY [benefit]"
   - `data-island="CountdownTimer"` or `data-island="InventoryIndicator"`

### Medium Page (8-12 sections) — Considered purchase / New-to-brand

1. **Attention (1)**: Hero with video or interactive media
2. **Interest (3)**: Value props → logo carousel → stats
   - Logo carousel = trust transfer from known brands
   - Neutral background between hero and body
3. **Desire (5)**: Feature grid → testimonials → before/after → reviews → comparison table
   - 3-6 features with icons
   - Transformation proof with `data-island="BeforeAfter"`
   - Compare you vs. 2 alternatives (3 columns max)
4. **Action (3)**: FAQ → CTA → footer
   - Preemptive objection handling (5-8 questions)
   - `data-island="EmailCapture"` for fence-sitters
   - `data-island="FAQ"` for progressive disclosure

### Long Page (12-16 sections) — High-ticket / Complex products

1. **Attention (2)**: Hero + announcement bar
   - Free shipping threshold / promo in bar
2. **Interest (4)**: Value props → logo carousel → stats → press mentions
   - Layer authority progressively: claims → endorsements → proof
3. **Desire (7)**: Feature showcase → testimonials → case study → feature grid → reviews → comparison → risk reversal
   - Hero feature with `data-island="VideoPlayer"`
   - Full customer journey (problem → solution → result)
   - Guarantee + return policy badge-driven
4. **Action (3)**: FAQ → dual CTA → footer
   - Dual CTA: buy now / learn more
   - `data-island="BundleBuilder"` for upsells

**Section Order Rules:**
- Never reviews before value props (prove value before social proof)
- FAQ immediately before final CTA (remove last objection)
- Stats or logo carousel within first 3 sections for trust anchoring
- Footer always last (consistency signal)

---

## Above-the-Fold Rules

What MUST be visible without scroll (< 900px viewport height). Violating this kills 40%+ of conversions.

### PDP (Product Detail Page)

**Mandatory visible elements:**
- Product image (left 50-60% width, min 600px tall)
- Product title (max 2 lines)
- Price + compare_at_price (if discounted)
- Star rating + review count (clickable to reviews)
- Primary CTA button
- 1-2 trust badges (free shipping, guarantee)

**HTML pattern:**
```html
<section class="grid md:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 py-8">
  <div class="relative">
    <img src="/product.jpg" alt="Product" class="w-full h-auto rounded-lg" />
  </div>
  <div class="flex flex-col justify-center space-y-6">
    <h1 class="text-4xl md:text-5xl font-bold leading-tight" style="color:var(--lx-text-color)">
      Premium Product Name
    </h1>
    <p class="text-lg md:text-xl opacity-80">One-line benefit promise that resonates</p>
    <div class="flex items-baseline gap-3">
      <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$89.00</span>
      <span class="text-lg line-through opacity-40">$129.00</span>
      <span class="text-xs font-semibold px-2 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">31% OFF</span>
    </div>
    <div class="flex items-center gap-2">
      <div class="flex">
        <span class="text-yellow-400">★★★★★</span>
      </div>
      <span class="text-sm opacity-70">(2,847 reviews)</span>
    </div>
    <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart — Free Shipping","showQuantity":true}'></div>
    <div class="flex gap-4 pt-4">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🚚</span>
        <span class="text-sm">Free Shipping</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-2xl">💯</span>
        <span class="text-sm">Money-Back Guarantee</span>
      </div>
    </div>
  </div>
</section>
```

### Landing Page (paid traffic)

**Mandatory visible:**
- Headline with specific benefit (not generic)
- Subline addressing pain point
- Hero image/video showing product in use
- Primary CTA (above fold)
- 1 trust signal (review stars or customer count)

**HTML pattern:**
```html
<section class="relative min-h-screen flex items-center justify-center text-center px-4 py-20" style="background:linear-gradient(135deg, #667eea 0%, #764ba2 100%)">
  <div class="max-w-4xl mx-auto space-y-8">
    <h1 class="text-5xl md:text-7xl font-extrabold leading-none text-white">
      Get Flawless Skin in 30 Days
    </h1>
    <p class="text-xl md:text-2xl text-white/90">
      Without harsh chemicals or expensive treatments. Guaranteed.
    </p>
    <button class="px-10 py-5 text-xl font-bold rounded-lg transition-transform hover:scale-105" style="background:white;color:var(--lx-accent-color)">
      Start MY Transformation
    </button>
    <p class="text-white/80 text-sm">Join 47,000+ customers who transformed their skin</p>
  </div>
  <div data-island="CountdownTimer" data-props='{"endDate":"2026-06-30T23:59:59Z","message":"Offer ends in:","urgencyThreshold":3600}'></div>
  <div data-island="SocialProofPopup" data-props='{"displayDuration":5000,"interval":15000,"maxPopups":3}'></div>
</section>
```

### Collection Page

**Mandatory visible:**
- Category headline + product count
- Filter bar (collapsible on mobile)
- First 4-6 products (2x3 grid desktop, 2 columns mobile)
- Sort dropdown
- Trust signal (delivery promise or return policy)

**Layout rule:** First product fold < 600px from top on desktop, < 800px on mobile.

---

## Price Psychology Patterns

### Anchoring (strikethrough + current)

Show original price crossed out. Minimum 20% discount to be credible, optimal 30-40%.

```html
<div class="flex items-baseline gap-3">
  <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$79.99</span>
  <span class="text-lg line-through opacity-40">$119.99</span>
  <span class="text-xs font-semibold px-2 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">33% OFF</span>
</div>
<p class="text-sm mt-2 opacity-70">Save $40 today</p>
```

### Charm Pricing

End prices in .97, .95, or .99. Never .00 for mid-market ($50-$300). Use .00 only for premium ($500+).

**Examples:**
- Low-ticket (<$50): $29.97, $14.99
- Mid-ticket ($50-$300): $129.95, $79.97
- High-ticket ($300+): $999.00, $1,500.00

### Bundle Pricing (quantity breaks)

Show per-unit savings, not just total discount.

```html
<div class="grid md:grid-cols-3 gap-4">
  <div class="p-6 border rounded-lg" style="border-color:var(--lx-border-color)">
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 1</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$59.99</p>
      <p class="text-sm opacity-70">$59.99 each</p>
      <button class="w-full px-4 py-2 mt-4 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
  <div class="p-6 border-2 rounded-lg relative transform scale-105" style="border-color:var(--lx-accent-color);box-shadow:0 20px 60px rgba(102,126,234,0.2)">
    <span class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 text-xs font-semibold rounded-full text-white" style="background:var(--lx-accent-color)">BEST VALUE</span>
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 3</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$119.99</p>
      <p class="text-sm opacity-70">$40.00 each — Save $60</p>
      <button class="w-full px-4 py-3 mt-4 rounded font-bold text-white" style="background:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
  <div class="p-6 border rounded-lg" style="border-color:var(--lx-border-color)">
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 2</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$99.99</p>
      <p class="text-sm opacity-70">$50.00 each — Save $20</p>
      <button class="w-full px-4 py-2 mt-4 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
</div>
```

### Payment Splitting (Afterpay/Klarna)

Show "or 4 payments of $X" beneath price. Increases conversion 20-30% for $100+ items.

```html
<div class="space-y-2">
  <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$159.99</p>
  <p class="text-sm opacity-70">or 4 interest-free payments of $40.00 with <strong>Afterpay</strong></p>
</div>
```

### Decoy Pricing (3-tier)

Always show 3 options. Middle option is the target, positioned as "most popular".

```html
<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <h3 class="text-2xl font-bold mb-2">Basic</h3>
    <p class="text-4xl font-bold mb-4" style="color:var(--lx-text-color)">$49.99</p>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature A</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature B</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
      Get Started
    </button>
  </div>
  <div class="p-8 rounded-lg relative transform scale-105" style="border:3px solid var(--lx-accent-color);box-shadow:0 20px 60px rgba(0,0,0,0.2)">
    <span class="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 text-sm font-semibold rounded-full text-white" style="background:var(--lx-accent-color)">MOST POPULAR</span>
    <h3 class="text-2xl font-bold mb-2">Pro</h3>
    <div class="flex items-baseline gap-2 mb-4">
      <p class="text-4xl font-bold" style="color:var(--lx-text-color)">$89.99</p>
      <p class="text-lg line-through opacity-40">$129.99</p>
    </div>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature A</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature B</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature C</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature D</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded font-bold text-white" style="background:var(--lx-accent-color)">
      Start Pro Trial
    </button>
  </div>
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <h3 class="text-2xl font-bold mb-2">Premium</h3>
    <p class="text-4xl font-bold mb-4" style="color:var(--lx-text-color)">$149.99</p>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Everything in Pro</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature E</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature F</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Priority Support</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
      Go Premium
    </button>
  </div>
</div>
```

---

## Social Proof Hierarchy

Rank order by persuasive power (highest to lowest). Use this sequence in sections.

### 1. Numbers (stats bar)

Raw metrics. Most credible when specific and large.

```html
<section class="py-16 px-4" style="background:var(--lx-bg-surface)">
  <div class="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-6xl mx-auto text-center">
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">247,000+</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Happy Customers</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">4.8/5.0</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Average Rating</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">12,000+</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">5-Star Reviews</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">94%</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Would Recommend</p>
    </div>
  </div>
</section>
```

**When to use:** First 3 sections. Anchor trust before storytelling.

### 2. Faces (testimonial cards)

Photos + quotes. Most effective for emotional products (beauty, wellness, lifestyle).

```html
<section class="py-16 px-4">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="color:var(--lx-text-color)">What Our Customers Say</h2>
    <div class="grid md:grid-cols-3 gap-8">
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface)">
        <div class="flex items-center gap-4 mb-4">
          <img src="/testimonials/sarah.jpg" alt="Sarah M." class="w-20 h-20 rounded-full" style="border:4px solid var(--lx-accent-color)" />
          <div>
            <p class="font-bold">Sarah M.</p>
            <p class="text-sm opacity-70">Verified Buyer</p>
            <div class="flex text-yellow-400">★★★★★</div>
          </div>
        </div>
        <p class="text-lg italic leading-relaxed opacity-90">
          "This completely changed how I approach skincare. I saw results in just 2 weeks."
        </p>
      </div>
      <!-- Repeat for more testimonials -->
    </div>
  </div>
</section>
```

**When to use:** After interest stage, before feature deep-dive. 3-6 testimonials max per section.

### 3. Logos (logo carousel)

Trust transfer from known brands. Works for B2B, press mentions, "as seen on".

```html
<section class="py-12 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto">
    <p class="text-center text-sm uppercase tracking-wide mb-8 opacity-70">Trusted by Leading Brands</p>
    <div class="flex justify-center items-center gap-12 flex-wrap">
      <img src="/logos/forbes.svg" alt="Forbes" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
      <img src="/logos/techcrunch.svg" alt="TechCrunch" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
      <img src="/logos/wsj.svg" alt="Wall Street Journal" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
    </div>
  </div>
</section>
```

**When to use:** Section 2-3. Before testimonials, after value props.

### 4. Quotes (review list)

Text-only reviews. Lowest impact but high volume works (10+ reviews).

```html
<section class="py-16 px-4">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="color:var(--lx-text-color)">12,000+ 5-Star Reviews</h2>
    <div data-island="ReviewCarousel" data-props='{"autoplay":true,"reviewsPerView":3,"reviews":[{"rating":5,"text":"Exceeded expectations. Results were visible in days. Highly recommend.","author":"John D.","verified":true,"date":"2026-06-15"}]}'></div>
  </div>
</section>
```

**When to use:** Mid-page (sections 5-8). Pile-on after testimonials for reinforcement.

---

## Urgency & Scarcity

Three types. Each requires different implementation and psychology.

### 1. Real Scarcity (Inventory)

Only use if actually tracking inventory. False scarcity destroys brand trust.

```html
<div class="inline-flex items-center gap-2 px-4 py-2 rounded" style="background:#fff3cd;color:#856404">
  <span class="font-semibold">⚠️ Only 7 left in stock</span>
</div>
<div data-island="InventoryIndicator" data-props='{"threshold":10,"lowStockMessage":"Only {count} left in stock","outOfStockMessage":"Sold out — join waitlist"}'></div>
```

**When to use:** High-demand products, limited editions, seasonal items.

### 2. Deadline (Countdown)

Time-limited offers. Must have real expiration.

```html
<div class="sticky top-0 z-50 py-3 px-4 text-center text-white font-semibold text-sm" style="background:#c9302c">
  🔥 Summer Sale: 30% Off Ends in
  <div data-island="CountdownTimer" data-props='{"endDate":"2026-06-30T23:59:59Z","message":"","urgencyThreshold":3600}'></div>
  <a href="#shop" class="ml-4 underline">Shop Now</a>
</div>
```

**When to use:** Flash sales, product launches, abandoned cart recovery.

### 3. Exclusivity (Limited Access)

Member-only, waitlist, invite-only framing.

```html
<section class="py-20 px-4 text-center" style="background:var(--lx-bg-surface)">
  <div class="max-w-2xl mx-auto space-y-6">
    <h2 class="text-4xl font-bold" style="color:var(--lx-text-color)">Join the Waitlist</h2>
    <p class="text-lg opacity-80">Limited to 500 founding members. Next batch ships August 2026.</p>
    <div class="inline-block px-4 py-2 rounded-full text-sm font-semibold" style="background:#f0f0f0">
      127 spots remaining
    </div>
    <div data-island="EmailCapture" data-props='{"placeholder":"Enter your email","buttonText":"Reserve Your Spot"}'></div>
  </div>
</section>
```

**When to use:** Pre-launch, beta access, VIP tiers.

### Anti-Patterns (Fake Urgency)

| ❌ Don't | Why | ✅ Do |
|----------|-----|-------|
| Evergreen countdowns (timer resets on refresh) | Users notice, trust tanks | Use real sale end dates, or remove timer |
| "Only 2 left!" for digital products | Obvious lie | Use enrollment caps ("Only 50 spots in this cohort") |
| "Sale ends tonight" every night | Cried wolf effect | Run real weekly/monthly sales with calendar |
| SocialProofPopup with fake names | "John from New York just bought" on loop | Only use if pulling real order events from API |

---

## Cognitive Load Management

Max 3 choices per section. More options = decision paralysis = abandonment.

### Feature Grid (3 features, not 7)

**Good (3 features):**
```html
<section class="py-16 px-4">
  <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
    <div class="text-center space-y-4">
      <span class="text-5xl">⚡</span>
      <h3 class="text-xl font-bold">Fast Results</h3>
      <p class="opacity-80">See improvements in 7 days or less</p>
    </div>
    <div class="text-center space-y-4">
      <span class="text-5xl">🛡️</span>
      <h3 class="text-xl font-bold">Risk-Free</h3>
      <p class="opacity-80">60-day money-back guarantee</p>
    </div>
    <div class="text-center space-y-4">
      <span class="text-5xl">❤️</span>
      <h3 class="text-xl font-bold">Love It</h3>
      <p class="opacity-80">Join 47,000+ happy customers</p>
    </div>
  </div>
</section>
```

**If you have 6+ features:** Split into 2 sections (benefits vs. technical specs).

### CompareTable (3 columns max, 5-8 rows)

```html
<div data-island="CompareTable" data-props='{"columns":[{"name":"Competitor A","highlight":false},{"name":"You","highlight":true},{"name":"Competitor B","highlight":false}],"rows":[{"feature":"Feature 1","values":["❌","✅","❌"]},{"feature":"Feature 2","values":["✅","✅","❌"]},{"feature":"Feature 3","values":["❌","✅","✅"]}]}'></div>
```

### Progressive Disclosure (Tabs/FAQ)

Use islands for deep info. Don't dump paragraphs.

```html
<div data-island="Tabs" data-props='{"tabs":[{"label":"How It Works","content":"..."},{"label":"Ingredients","content":"..."},{"label":"Shipping","content":"..."}]}'></div>
<div data-island="FAQ" data-props='{"items":[{"question":"How long does shipping take?","answer":"2-3 business days."}]}'></div>
```

---

## Trust Escalation Ladder

Move visitors from low-commitment → high-commitment actions. Don't ask for the sale immediately.

### Sequence:

1. **Browse encouragement** (no commitment)
   - Hero: "Explore our collection"
   - Value props: "See why 47,000+ customers love us"

2. **Email capture** (small commitment)
   - Offer: "Get 10% off your first order"
   - Placement: Section 3-5
   - `data-island="EmailCapture"`

3. **Cart confidence** (medium commitment)
   - `data-island="BuyBox"` with "Add to Cart"
   - Show: trust badges, free shipping, easy returns

4. **Purchase trigger** (high commitment)
   - Final CTA: "Complete your order"
   - Add: `data-island="CountdownTimer"` or `data-island="InventoryIndicator"`
   - Show: risk reversal (guarantee)

---

## CTA Psychology

Button copy is conversion science. Every word matters.

### First-Person Labels

**Bad (second-person):**
- "Get Started"
- "Buy Now"
- "Download the Guide"

**Good (first-person):**
- "Start MY Free Trial"
- "Add to MY Cart"
- "Send ME the Guide"

**Why it works:** First-person creates ownership before purchase.

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Start MY Transformation
</button>
```

### Benefit-Driven Copy

**Bad (action-only):**
- "Submit"
- "Continue"
- "Next"

**Good (action + benefit):**
- "Get My Discount"
- "Unlock Free Shipping"
- "Claim My Spot"

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Claim My 30% Off
</button>
```

### Contrast Principle

CTA button must have 4.5:1 contrast ratio against background (WCAG AA). Use high-chroma colors.

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg shadow-lg transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white;box-shadow:0 4px 12px rgba(102,126,234,0.4)">
  Add to Cart
</button>
```

**Color pairs (high contrast):**
- Blue CTA on white: `#667eea` / `#ffffff`
- Red CTA on dark: `#c9302c` / `#1a1a1a`
- Green CTA on light: `#28a745` / `#f9fafb`

### Button Hierarchy

**Primary (main action):**
```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Buy Now — $89
</button>
```

**Secondary (alternative action):**
```html
<button class="px-6 py-3 rounded-lg" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
  Learn More
</button>
```

**Ghost (low-commitment):**
```html
<button class="px-6 py-3 rounded-lg hover:bg-opacity-10" style="color:var(--lx-accent-color)">
  View Details
</button>
```

**Link (minimal friction):**
```html
<a href="#learn-more" class="underline" style="color:var(--lx-accent-color)">
  Learn More
</a>
```

### Dual CTA (high + low commitment)

Offer high-commitment + low-commitment options.

```html
<div class="flex gap-4 justify-center">
  <button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
    Buy Now — $89
  </button>
  <button class="px-6 py-3 rounded-lg" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
    Learn More
  </button>
</div>
```

**When to use:** High-ticket products ($300+), complex products needing education.

---

## Visual Hierarchy for Conversion

Eye-flow patterns direct attention to CTAs.

### Focal Points (element styles)

Use scale, color, and whitespace to create hierarchy.

**Headline (most important):**
```html
<h1 class="text-5xl md:text-7xl font-extrabold leading-tight mb-4" style="color:var(--lx-text-color)">
  Transform Your Skin in 30 Days
</h1>
```

**Subline (secondary):**
```html
<p class="text-xl md:text-2xl leading-relaxed mb-8" style="color:var(--lx-text-muted)">
  Clinically proven formula with visible results in just 2 weeks
</p>
```

**CTA (action):**
```html
<button class="px-10 py-5 text-xl font-bold rounded-lg shadow-2xl transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white;box-shadow:0 8px 24px rgba(102,126,234,0.5)">
  Get Started
</button>
```

### Whitespace for Emphasis

Surround CTAs with empty space (min 2rem padding).

```html
<section class="py-20 px-4">
  <!-- CTA content -->
</section>
```

---

## Anti-Patterns (Conversion Killers)

| ❌ | Why | ✅ |
|----|-----|-----|
| Generic headlines ("Welcome to Our Store") | No hook, no benefit | "Get [Specific Benefit] in [Timeframe]" |
| Hidden prices ("Contact for Pricing") | Friction, distrust | Show price upfront (even if high) |
| Walls of text (5-paragraph descriptions) | Cognitive overload | Bullet points, max 3 benefits |
| Too many CTAs (3+ above fold) | Decision paralysis | 1 primary CTA, 1 optional secondary |
| Tiny mobile buttons (40px tap target) | Poor UX, missed clicks | 48px minimum (py-3 or py-4) |
| Auto-playing video with sound | Annoys users | Muted autoplay, click to unmute |
| No trust signals above fold | Credibility gap | Add star rating or customer count near CTA |
| Fake urgency (evergreen countdown) | Trust erosion | Real sale end dates or remove timer |
| Cluttered forms (8-field email capture) | Abandonment | Email only with `data-island="EmailCapture"` |
| Slow load times (5+ second hero load) | Bounce rate spike | Optimize images, lazy-load below fold |
| No mobile optimization (desktop-only) | Poor mobile UX | Responsive spacing, clamp() font sizes |
| Unclear value prop ("We're the best") | Generic, meaningless | "Save 10 hours/week with automated [task]" |
| No risk reversal (no guarantee) | Fear of loss | Risk reversal section before final CTA |
| Dead-end pages (no next step) | Lost momentum | Every section ends with CTA or link |
| Inconsistent branding (5 button styles) | Unprofessional | Consistent colors via CSS vars |

---

## Complete Page Recipes

### Recipe 1: Lead Gen (Email Capture)

**Goal:** Maximize email signups for nurture sequence.

**VibePage structure (abbreviated):**
```json
{
  "head": {
    "title": "Get the Ultimate Skincare Guide",
    "fonts": ["https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap"]
  },
  "theme_css": ":root { --lx-accent-color: #667eea; --lx-text-color: #1a1a1a; --lx-bg-color: #ffffff; --lx-bg-surface: #f9fafb; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class='py-20 px-4 text-center' style='background:linear-gradient(135deg, #667eea 0%, #764ba2 100%)'><div class='max-w-3xl mx-auto space-y-6'><h1 class='text-5xl md:text-6xl font-extrabold text-white'>Get the Flawless Skin Guide</h1><p class='text-xl text-white/90'>Learn how to achieve radiant skin in 30 days. Free download.</p><div data-island='EmailCapture' data-props='{\"placeholder\":\"Enter your email\",\"buttonText\":\"Send Me the Guide\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "value-props",
      "html": "<section class='py-16 px-4'><div class='grid md:grid-cols-3 gap-8 max-w-5xl mx-auto'><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>Science-Backed Methods</h3><p class='opacity-80'>Proven techniques from dermatologists</p></div><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>Natural Ingredients</h3><p class='opacity-80'>No harsh chemicals or side effects</p></div><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>30-Day Results</h3><p class='opacity-80'>See visible improvements in one month</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "stats",
      "html": "<section class='py-12 px-4' style='background:var(--lx-bg-surface)'><div class='grid grid-cols-2 gap-8 max-w-4xl mx-auto text-center'><div><p class='text-5xl font-extrabold' style='color:var(--lx-accent-color)'>47,000+</p><p class='text-sm uppercase mt-2 opacity-70'>Downloads</p></div><div><p class='text-5xl font-extrabold' style='color:var(--lx-accent-color)'>4.9/5</p><p class='text-sm uppercase mt-2 opacity-70'>Rating</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta",
      "html": "<section class='py-20 px-4 text-center'><div class='max-w-2xl mx-auto space-y-6'><h2 class='text-4xl font-bold' style='color:var(--lx-text-color)'>Ready to Get Started?</h2><div data-island='EmailCapture' data-props='{\"placeholder\":\"Enter your email\",\"buttonText\":\"Download Now — It\\'s Free\"}'></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

### Recipe 2: Direct Purchase (Low-ticket <$100)

**Goal:** Impulse buy, minimal friction.

**VibePage structure (abbreviated):**
```json
{
  "sections": [
    {
      "id": "hero",
      "html": "<section class='grid md:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 py-8'><div><img src='/product.jpg' class='w-full rounded-lg'/></div><div class='flex flex-col justify-center space-y-6'><h1 class='text-5xl font-bold' style='color:var(--lx-text-color)'>Premium Serum</h1><p class='text-xl opacity-80'>Transform your skin in 30 days</p><div class='flex items-baseline gap-3'><span class='text-3xl font-bold' style='color:var(--lx-text-color)'>$79.99</span><span class='text-lg line-through opacity-40'>$119.99</span><span class='text-xs font-semibold px-2 py-1 rounded-full text-white' style='background:var(--lx-accent-color)'>33% OFF</span></div><div data-island='BuyBox' data-props='{\"productId\":\"gid://shopify/Product/123\",\"ctaText\":\"Add to Cart — Free Shipping\"}'></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

### Recipe 3: High-AOV ($500+)

**Goal:** Build trust for expensive purchase.

**VibePage structure (abbreviated):**
```json
{
  "sections": [
    {
      "id": "hero",
      "html": "<section class='relative min-h-screen flex items-center justify-center px-4' style='background:url(/hero.jpg) center/cover'><div class='max-w-3xl text-center space-y-6 text-white'><h1 class='text-6xl font-extrabold'>Enterprise CRM Platform</h1><p class='text-2xl'>Trusted by Fortune 500 companies</p><button class='px-8 py-4 text-lg font-bold rounded-lg' style='background:white;color:var(--lx-accent-color)'>Schedule a Demo</button></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "logos",
      "html": "<section class='py-12 px-4' style='background:var(--lx-bg-surface)'><p class='text-center text-sm uppercase tracking-wide mb-8 opacity-70'>Trusted by Industry Leaders</p><div class='flex justify-center gap-12 flex-wrap'><img src='/logos/company1.svg' class='h-10 opacity-60'/><img src='/logos/company2.svg' class='h-10 opacity-60'/><img src='/logos/company3.svg' class='h-10 opacity-60'/></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

**End of conversion-psychology.md**

---

# Island Patterns — Wrapper HTML & Combination Recipes

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then run `compile_page_source`.

How to properly embed, wrap, and combine React islands in vibe-code HTML sections. Load when using commerce or engagement islands.

---

## Island Embedding Rules

1. `data-island` attribute = exact island name (case-sensitive)
2. `data-props` = valid JSON in **single-quoted** attribute value
3. One `BuyBox` per page (multiple breaks cart state)
4. Cart: set `head.use_cart_v2: true` on every commerce page — never author a cart section (`CartDrawer` is deprecated V1)
5. Islands hydrate client-side — surrounding HTML renders immediately (SSR)
6. Never put islands inside other islands
7. Always wrap in a containing section with proper spacing

---

## Commerce Islands

### BuyBox — Primary Purchase Action

**Always pair with surrounding context (title, price are in the BuyBox island itself):**

```html
<section class="px-4 sm:px-6 lg:px-8 py-8">
  <div class="max-w-2xl mx-auto">
    <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart"}'></div>
  </div>
</section>
```

**PDP layout — Gallery + BuyBox side by side:**

```html
<section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-16">
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">
    <!-- Left: Gallery -->
    <div data-island="ProductGallery" data-props='{"productId":"gid://shopify/Product/123","layout":"grid","enableZoom":true}'></div>
    <!-- Right: BuyBox -->
    <div class="lg:sticky lg:top-24 lg:self-start">
      <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart"}'></div>
    </div>
  </div>
</section>
```

### Cart — V2 is the default (CartDrawer V1 is DEPRECATED)

Set `head.use_cart_v2: true` on every commerce page. The renderer injects the resolved published cart profile separately, so **never author a cart section in the page**. Use `get_cart_profile`, `set_cart_profile`, and `edit_cart` for MCP cart work. Full composition guide: load the `cart-composition` reference.

```jsonc
{ "head": { "title": "...", "use_cart_v2": true } }   // that's the whole cart setup
```

Legacy note: `CartDrawer` (V1) exists only on old pages that predate Cart V2. Don't add it to new pages; when editing a legacy page, prefer migrating it (remove CartDrawer, set the flag).

### StickyBar — Scroll-triggered Bottom CTA

```html
<section>
  <div data-island="StickyBar" data-props='{"productId":"gid://shopify/Product/123","showPrice":true,"triggerOffset":600}'></div>
</section>
```

`triggerOffset`: px from top before bar appears. Set to ~height of hero + BuyBox section.

### QuantityBreaks — Volume Discounts

Place directly below or beside BuyBox:

```html
<section class="px-4 sm:px-6 lg:px-8 pb-6">
  <div class="max-w-2xl mx-auto">
    <div data-island="QuantityBreaks" data-props='{"productId":"gid://shopify/Product/123","tiers":[{"qty":2,"discount":10,"label":"Buy 2 Save 10%"},{"qty":3,"discount":15,"label":"Buy 3 Save 15%"},{"qty":5,"discount":20,"label":"Buy 5 Save 20%"}]}'></div>
  </div>
</section>
```

### ProductCarousel — Cross-sells / Related

```html
<section class="py-12 lg:py-20 px-4 sm:px-6 lg:px-8" style="background:var(--lx-bg-surface)">
  <div class="max-w-7xl mx-auto">
    <h2 class="text-center font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.25rem,2.5vw,2rem)">
      You May Also Like
    </h2>
    <div data-island="ProductCarousel" data-props='{"productIds":["gid://shopify/Product/1","gid://shopify/Product/2","gid://shopify/Product/3","gid://shopify/Product/4"],"columns":4,"showQuickAdd":true}'></div>
  </div>
</section>
```

### ProductGallery — Image Gallery with Zoom

```html
<div data-island="ProductGallery" data-props='{"productId":"gid://shopify/Product/123","layout":"grid","enableZoom":true}'></div>
```

Layout options: `"grid"` (thumbnails below), `"stack"` (vertical scroll), `"carousel"` (swipe).

---

## Social Proof Islands

### ReviewCarousel — Customer Reviews

**With custom reviews (no Shopify fetch):**

```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-10">
      <p class="text-xs uppercase tracking-[0.2em] mb-2" style="color:var(--lx-accent-color)">Testimonials</p>
      <h2 class="font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">Loved by Thousands</h2>
    </div>
    <div data-island="ReviewCarousel" data-props='{"reviews":[{"author":"Priya M.","rating":5,"text":"Amazing results in just one week!","date":"2026-05-01"},{"author":"Ananya R.","rating":5,"text":"Best serum I have ever used.","date":"2026-04-15"},{"author":"Kavita S.","rating":4,"text":"Great for sensitive skin.","date":"2026-03-20"}],"autoPlay":true}'></div>
  </div>
</section>
```

**With Shopify product reviews (auto-fetch):**

```html
<div data-island="ReviewCarousel" data-props='{"productId":"gid://shopify/Product/123","autoPlay":true}'></div>
```

### TrustBadgeBar — Trust Signals

```html
<section class="py-4 border-y" style="border-color:var(--lx-border-color)">
  <div data-island="TrustBadgeBar" data-props='{"badges":[{"icon":"shield","label":"Secure Checkout"},{"icon":"truck","label":"Free Shipping"},{"icon":"refresh","label":"Easy Returns"},{"icon":"award","label":"Premium Quality"}]}'></div>
</section>
```

Available icons: `shield`, `truck`, `refresh`, `award`, `check`, `lock`, `heart`, `star`, `clock`, `leaf`.

### SocialProofPopup — Recent Activity Toasts

Place once (invisible section):

```html
<section class="hidden">
  <div data-island="SocialProofPopup" data-props='{"messages":[{"text":"Sarah from Mumbai just purchased","delay":3000},{"text":"Rohit from Delhi added to cart","delay":5000},{"text":"12 people viewing this now","delay":8000}],"position":"bottom-left","interval":8000}'></div>
</section>
```

---

## Content Islands

### FAQ — Accordion Questions

```html
<section class="py-12 lg:py-20 px-4">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-center font-bold mb-10" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">
      Frequently Asked Questions
    </h2>
    <div data-island="FAQ" data-props='{"items":[{"question":"How do I use this product?","answer":"Apply 2-3 drops to clean skin morning and night."},{"question":"Is it suitable for sensitive skin?","answer":"Yes, dermatologist tested and hypoallergenic."},{"question":"When will I see results?","answer":"Most customers see improvement within 1-2 weeks."},{"question":"What is your return policy?","answer":"30-day hassle-free returns, no questions asked."}],"style":"accordion","openFirst":true}'></div>
  </div>
</section>
```

### Tabs — Tabbed Content

```html
<section class="py-12 px-4">
  <div class="max-w-4xl mx-auto">
    <div data-island="Tabs" data-props='{"tabs":[{"label":"Details","content":"<p>Full product details and specifications.</p>"},{"label":"Ingredients","content":"<ul><li>Hyaluronic Acid</li><li>Niacinamide 5%</li><li>Ceramides</li></ul>"},{"label":"How to Use","content":"<ol><li>Cleanse face</li><li>Apply 2-3 drops</li><li>Follow with moisturizer</li></ol>"}],"style":"underline"}'></div>
  </div>
</section>
```

Style options: `"underline"`, `"pills"`, `"bordered"`.

### BeforeAfter — Comparison Slider

```html
<section class="py-12 lg:py-20 px-4">
  <div class="max-w-2xl mx-auto text-center">
    <h2 class="font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">
      Real Results
    </h2>
    <div data-island="BeforeAfter" data-props='{"before":{"src":"BEFORE_IMAGE_URL","label":"Day 1"},"after":{"src":"AFTER_IMAGE_URL","label":"Day 30"}}'></div>
  </div>
</section>
```

---

## Engagement Islands

### IngredientExplorer — Interactive Ingredients

```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-4xl mx-auto">
    <div class="text-center mb-10">
      <p class="text-xs uppercase tracking-[0.2em] mb-2" style="color:var(--lx-accent-color)">Transparency</p>
      <h2 class="font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">What's Inside</h2>
    </div>
    <div data-island="IngredientExplorer" data-props='{"ingredients":[{"name":"Hyaluronic Acid","description":"Multi-molecular weight complex","benefit":"Deep multi-layer hydration"},{"name":"Niacinamide 5%","description":"Vitamin B3 derivative","benefit":"Minimizes pores, evens tone"},{"name":"Ceramide Complex","description":"Skin-identical lipids","benefit":"Repairs moisture barrier"}],"layout":"interactive"}'></div>
  </div>
</section>
```

### CompareTable — Product Comparison

```html
<section class="py-12 lg:py-20 px-4">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-center font-bold mb-10" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">
      Why We're Different
    </h2>
    <div data-island="CompareTable" data-props='{"products":[{"name":"Our Serum","features":{"Clean Ingredients":true,"Dermat Tested":true,"No Parabens":true,"Under ₹1500":true}},{"name":"Brand X","features":{"Clean Ingredients":false,"Dermat Tested":true,"No Parabens":false,"Under ₹1500":false}},{"name":"Brand Y","features":{"Clean Ingredients":true,"Dermat Tested":false,"No Parabens":true,"Under ₹1500":true}}],"features":["Clean Ingredients","Dermat Tested","No Parabens","Under ₹1500"],"highlightIndex":0}'></div>
  </div>
</section>
```

### EmailCapture — Lead Capture

```html
<section class="py-12 lg:py-16 px-4" style="background:var(--lx-accent-color)">
  <div class="max-w-xl mx-auto text-center">
    <h2 class="text-white text-2xl font-bold mb-2" style="font-family:var(--lx-font-heading)">Join the Club</h2>
    <p class="text-white/70 text-sm mb-6">Get 10% off your first order + early access to new launches.</p>
    <div data-island="EmailCapture" data-props='{"placeholder":"Enter your email","buttonText":"Get 10% Off","incentive":"10% off your first order","style":"inline"}'></div>
  </div>
</section>
```

### ExitIntent — Last-Chance Popup

Place once (invisible):

```html
<section class="hidden">
  <div data-island="ExitIntent" data-props='{"headline":"Wait! Don't leave empty-handed","body":"Use code EXIT15 for 15% off your first order","ctaText":"Claim My Discount","showOnMobile":true}'></div>
</section>
```

---

## Common Combinations

### PDP Core (minimum viable PDP)

```
1. ProductGallery + BuyBox (side-by-side on desktop)
2. TrustBadgeBar (immediately below)
3. Tabs (details/ingredients/usage)
4. ReviewCarousel
5. StickyBar (scroll-triggered)
6. head.use_cart_v2: true (cart injected — no section needed)
```

### Landing Page Core

```
1. Hero section (HTML, no island)
2. TrustBadgeBar
3. Benefits section (HTML grid)
4. BeforeAfter or IngredientExplorer
5. ReviewCarousel
6. EmailCapture or BuyBox
7. FAQ
8. ExitIntent (hidden)
```

### Collection Page

```
1. Collection header (HTML)
2. ProductCarousel (featured picks)
3. Product grid with QuickAdd per card
4. TrustBadgeBar
5. EmailCapture (footer)
```

---

## Data-Props Formatting Rules

1. **Single quotes** around attribute value: `data-props='...'`
2. **Double quotes** inside JSON: `{"key":"value"}`
3. **No apostrophes** in text values — use `'` or rephrase
4. **No line breaks** in data-props — must be one line
5. **Numbers without quotes**: `{"qty":2,"discount":10}`
6. **Booleans without quotes**: `{"autoPlay":true}`
7. **Arrays**: `{"items":[{...},{...}]}`

### Escaping gotchas

```html
<!-- WRONG: apostrophe breaks parsing -->
<div data-props='{"text":"Don't miss out"}'></div>

<!-- RIGHT: avoid apostrophes -->
<div data-props='{"text":"Do not miss out"}'></div>

<!-- RIGHT: use HTML entity in surrounding HTML, not in props -->
```

---

## PDP Template Recipes

### DTC Beauty PDP

```
ProductGallery (vertical, listenForVariant:true)
├── VariantSwatches (color, image type)
├── SubscriptionToggle
├── BuyBox (listenForEvents:true, showVariantSelector:false)
├── DeliveryEstimate (variant:"inline")
├── TrustBadgeBar (compact)
├── PaymentOptions (variant:"inline", listenForEvents:true)
├── InventoryIndicator (variant:"badge", listenForEvents:true)
├── Tabs (underline)
├── ReviewCarousel
├── BundleBuilder (layout:"horizontal")
├── ProductCarousel ("You may also like")
├── StickyBar
└── SocialProofPopup    # cart: head.use_cart_v2: true (injected)
```

### Fashion/Apparel PDP

```
ProductGallery (layout:"grid", listenForVariant:true)
├── VariantSwatches (color, image) + VariantSwatches (type:"size_grid", axis mode)
├── OptionResolver (productId)
├── SizeGuide
├── BuyBox (variant:"expanded", listenForEvents:true, showVariantSelector:false)
├── InventoryIndicator (variant:"text", listenForEvents:true)
├── DeliveryEstimate (variant:"card")
├── Tabs (style:"underline")
├── ReviewCarousel
├── BundleBuilder (title:"Complete the look", layout:"stacked")
├── ProductCarousel
├── StickyBar
└── ExitIntent          # cart: head.use_cart_v2: true (injected)
```

### Supplements/Wellness PDP

```
ProductGallery (vertical)
├── VariantSwatches (flat, image type for flavors)
├── QuantityBreaks
├── SubscriptionToggle
├── BuyBox (listenForEvents:true)
├── PaymentOptions (variant:"expandable")
├── TrustBadgeBar (badges: GMP, vegan, lab-tested)
├── IngredientExplorer (layout:"interactive")
├── FAQ (style:"accordion")
├── ReviewCarousel
├── CompareTable (vs competitors)
├── BundleBuilder (title:"Stack for results")
├── StickyBar
└── CountdownTimer      # cart: head.use_cart_v2: true (injected) (style:"simple", inline with price)
```

### Personalized Product PDP (Gifts/Jewelry)

```
ProductGallery (layout:"grid")
├── VariantSwatches (type:"text")
├── BuyBox (variant:"expanded", listenForEvents:true)
├── DeliveryEstimate (variant:"banner")
├── PaymentOptions (variant:"inline")
├── Tabs
├── ReviewCarousel
├── ProductCarousel ("Complete the gift set")
└── StickyBar            # cart: head.use_cart_v2: true (injected)
```

### Island Communication on PDP

Key event flows for PDP islands:
- VariantSwatches → (variant:changed) → BuyBox, ProductGallery, InventoryIndicator, PaymentOptions
- OptionResolver → (variant:changed) → all listeners above (for multi-axis products)
- SubscriptionToggle → (subscription:changed) → BuyBox
- BundleBuilder → (bundle:add) → cart drawer (Cart V2, injected)
- InventoryIndicator → (inventory:updated) → StickyBar, BuyBox

Always set `listenForEvents:true` on listener islands when they co-exist with emitters.

---

## New PDP Islands (v2)

### ProductHero — Split-Layout PDP Hero

Premium split-hero for PDPs. Media pane on one side, BuyBox on the other.

```html
<div data-island="ProductHero" data-props='{"images":[{"url":"/product-1.jpg","objectFit":"contain","objectPosition":"center"},{"url":"/product-2.jpg","objectFit":"cover"}],"layout":"splitLeft","thumbnails":"rail","thumbnailPosition":"left","navigation":"floatingArrows","transition":"fade","listenForVariant":true}'></div>
```

**Layout options:** `splitLeft` (media left 60%), `splitRight`, `fullHeight`, `stacked`
**ALWAYS PAIR WITH:** BuyBox in the adjacent grid cell. Use CSS grid in the containing HTML section to create the split.

### EditorialProductGrid — Related Products + Bundle

Mixed-type grid with center feature card for bundles or highlighted products.

```html
<div data-island="EditorialProductGrid" data-props='{"products":[{"id":"123","title":"Product A","price":"$29","image":"/a.jpg"},{"id":"456","title":"Product B","price":"$35","image":"/b.jpg"}],"featureCard":{"title":"Save 20%","subtitle":"Bundle & save","type":"bundle","cta":"Add Bundle"},"layout":"tripleCenter","showQuickAdd":true}'></div>
```

**Layout options:** `tripleCenter` (product | feature | product), `dualSide`, `quad`

### PDPInfoCards — Product Detail Cards

Information cards for product specs, taste profiles, pairings, certifications.

```html
<div data-island="PDPInfoCards" data-props='{"cards":[{"title":"Taste Profile","icon":"palette","items":["Bright citrus","Smooth finish","Medium body"]},{"title":"Pairs With","icon":"wine","items":["Dark chocolate","Aged cheese","Fresh berries"]}],"variant":"dashed","columns":2,"badgeRow":[{"icon":"leaf","label":"Organic"},{"icon":"shield","label":"Lab Tested"}]}'></div>
```

**Variant options:** `bordered`, `dashed`, `filled`, `minimal`
**ALWAYS PAIR WITH:** Place below ProductHero/BuyBox section, above reviews.

---

## Navigation Islands — Hydration Mode (Preferred)

Navigation islands (Navbar, Footer, SiteHeader) support **hydration mode**: you generate ANY HTML/CSS, then place `data-lx-*` tags on functional elements. The island attaches behavior (cart state, mobile toggle, newsletter) without touching your design.

### Why Hydration Mode?

- Complete design freedom — any layout, any CSS
- Only 2-5 behavior props (vs 15+ style props in legacy mode)
- Cart state auto-syncs — no prop management
- Publish validator enforces required tags — can't ship broken nav

### Navbar — Hydration Mode

**Required tags:** `data-lx-nav="root|cart-trigger|cart-count|mobile-trigger|mobile-panel"`

**Behavior props:** `sticky` (bool), `cartMode` ("drawer"|"link"), `transparent` (bool)

```html
<div data-island="Navbar" data-props='{"sticky":true,"cartMode":"drawer"}'>
  <nav data-lx-nav="root" class="fixed top-0 w-full z-50 bg-white/95 backdrop-blur border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-6 flex items-center justify-between h-16">
      <a href="/" data-lx-nav="logo">
        <img src="{{brand_logo}}" class="h-8" alt="{{brand_name}}" />
      </a>
      <nav class="hidden lg:flex items-center gap-8">
        <a href="/collections" data-lx-nav="link" class="text-sm font-medium">Shop</a>
        <a href="/about" data-lx-nav="link" class="text-sm font-medium">About</a>
      </nav>
      <div class="flex items-center gap-4">
        <button data-lx-nav="cart-trigger" class="relative p-2">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4zM3 6h18M16 10a4 4 0 01-8 0"/>
          </svg>
          <span data-lx-nav="cart-count" class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-black text-white text-[10px] flex items-center justify-center" style="display:none"></span>
        </button>
        <button data-lx-nav="mobile-trigger" class="lg:hidden p-2">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 12h18M3 6h18M3 18h18"/>
          </svg>
        </button>
      </div>
    </div>
    <div data-lx-nav="mobile-panel" class="hidden lg:hidden border-t px-6 py-4">
      <a href="/collections" class="block py-3 text-sm font-medium">Shop</a>
      <a href="/about" class="block py-3 text-sm font-medium">About</a>
    </div>
  </nav>
</div>
```

**CSS requirement** (include in section CSS):
```css
[data-lx-nav="mobile-panel"] { display: none; }
[data-lx-nav="mobile-panel"].lx-open { display: block; }
```

**Dropdowns (optional):**
```html
<div class="relative">
  <a href="/shop" data-lx-nav="dropdown-trigger">Shop ▾</a>
  <div data-lx-nav="dropdown-panel" class="absolute top-full mt-2 bg-white shadow-lg rounded-lg p-4">
    <a href="/collections/new" class="block py-2 text-sm">New Arrivals</a>
  </div>
</div>
```

**Hide cart (no cart-trigger/cart-count needed):**
```html
<div data-island="Navbar" data-props='{"sticky":true,"hideCart":true}'>
```

### Footer — Hydration Mode

**Required tags:** `data-lx-footer="root"`  
**Optional tags:** `newsletter-form`, `newsletter-input`, `newsletter-success`, `year`

```html
<div data-island="Footer" data-props='{"newsletterEndpoint":"https://api.example.com/subscribe"}'>
  <footer data-lx-footer="root" class="bg-gray-950 text-gray-300 py-16 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12">
      <div>
        <img src="{{brand_logo}}" class="h-8 mb-4 invert" alt="{{brand_name}}" />
        <p class="text-sm text-gray-400">{{brand_tagline}}</p>
      </div>
      <div>
        <h4 class="text-white font-semibold text-sm mb-4">Shop</h4>
        <a href="/collections" class="block text-sm py-1.5 text-gray-400 hover:text-white">All Products</a>
      </div>
      <div>
        <h4 class="text-white font-semibold text-sm mb-4">Newsletter</h4>
        <form data-lx-footer="newsletter-form" class="flex">
          <input data-lx-footer="newsletter-input" type="email" placeholder="your@email.com" class="flex-1 px-3 py-2 bg-gray-900 border border-gray-700 text-sm text-white rounded-l" />
          <button type="submit" class="px-4 py-2 bg-white text-black text-sm font-medium rounded-r">→</button>
        </form>
        <p data-lx-footer="newsletter-success" style="display:none" class="text-sm text-green-400 mt-2"></p>
      </div>
    </div>
    <div class="max-w-7xl mx-auto mt-10 pt-6 border-t border-gray-800 text-sm text-gray-500">
      © <span data-lx-footer="year"></span> All rights reserved.
    </div>
  </footer>
</div>
```

### SiteHeader — Hydration Mode

Combines announcement + navbar. Uses BOTH `data-lx-header` and `data-lx-nav` tags.

**Required tags:** `data-lx-header="root"` + same nav tags as Navbar

```html
<div data-island="SiteHeader" data-props='{"sticky":true,"cartMode":"drawer","messages":["Free shipping over $75","New summer collection"],"dismissible":true}'>
  <header data-lx-header="root" class="fixed top-0 w-full z-50">
    <div data-lx-header="announcement" class="bg-black text-white text-center py-2 text-xs relative">
      <span data-lx-header="announcement-text">Free shipping over $75</span>
      <button data-lx-header="announcement-dismiss" class="absolute right-3 top-1/2 -translate-y-1/2">✕</button>
    </div>
    <nav class="bg-white border-b">
      <!-- Same data-lx-nav tags as Navbar example above -->
    </nav>
  </header>
</div>
```

### Tag Reference

| Tag | Islands | Behavior |
|-----|---------|----------|
| `data-lx-nav="root"` | Navbar, SiteHeader | Sticky/scroll attaches here |
| `data-lx-nav="cart-trigger"` | Navbar, SiteHeader | Click → open cart drawer or navigate |
| `data-lx-nav="cart-count"` | Navbar, SiteHeader | textContent auto-updated from $cartLines |
| `data-lx-nav="mobile-trigger"` | Navbar, SiteHeader | Click toggles mobile-panel .lx-open class |
| `data-lx-nav="mobile-panel"` | Navbar, SiteHeader | Toggle target for mobile menu |
| `data-lx-nav="dropdown-trigger"` | Navbar, SiteHeader | Hover shows dropdown-panel |
| `data-lx-nav="dropdown-panel"` | Navbar, SiteHeader | Shown/hidden on hover (same parent) |
| `data-lx-footer="root"` | Footer | Root element |
| `data-lx-footer="newsletter-form"` | Footer | Form submit → POST endpoint |
| `data-lx-footer="newsletter-input"` | Footer | Email input |
| `data-lx-footer="newsletter-success"` | Footer | Shown after successful submit |
| `data-lx-footer="year"` | Footer | textContent = current year |
| `data-lx-header="root"` | SiteHeader | Root + spacer via ResizeObserver |
| `data-lx-header="announcement"` | SiteHeader | Hidden on dismiss |
| `data-lx-header="announcement-text"` | SiteHeader | Rotates through messages[] |
| `data-lx-header="announcement-dismiss"` | SiteHeader | Click hides + persists to sessionStorage |

### Validation (Publish Blocks If Missing)

The publish validator enforces required tags when hydration mode detected:
- Navbar/SiteHeader: `root` + `cart-trigger` + `cart-count` + `mobile-trigger` + `mobile-panel`
- Footer: `root`
- Cart tags skipped if `hideCart: true` in props

---

# Style Packs — Named `data-part` CSS Bundles

> Pre-tested visual treatments for rendered-mode islands. Pick ONE pack per page and paste its island overrides into the relevant sections' `<style>` blocks. Packs only touch visual properties (radius, borders, shadows, typography case/tracking) via `[data-part]` selectors and `--lx-*` variables — never layout. For fully custom island markup use headless mode instead (source-format.md).

## Choosing

| Pack | Feel | Best for |
|---|---|---|
| `editorial` | serif confidence, hairline rules, generous air | premium skincare, fashion, coffee |
| `soft-luxury` | pill shapes, soft shadows, muted warmth | beauty, wellness, jewelry |
| `brutalist` | hard edges, thick borders, high contrast | streetwear, drops, gen-z brands |
| `playful` | big radii, bouncy hovers, chunky buttons | kids, snacks, novelty, pets |
| `minimal` | flat, monochrome, quiet CTAs | tech accessories, tools, minimal brands |

## editorial

```css
[data-part="cta"] { border-radius: 0; text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.85rem; padding: 1.1rem 2.5rem; }
[data-part="variant-btn"] { border-radius: 0; border-width: 1px; text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.75rem; }
[data-part="heading"] { font-family: var(--lx-font-heading); font-weight: 400; letter-spacing: -0.01em; }
[data-part="item"] { border: none; border-bottom: 1px solid var(--lx-border-color); border-radius: 0; }
[data-part="badge"] { border-radius: 0; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.65rem; }
```

## soft-luxury

```css
[data-part="cta"] { border-radius: 9999px; box-shadow: 0 8px 24px color-mix(in srgb, var(--lx-accent-color) 35%, transparent); padding: 1rem 2.75rem; }
[data-part="variant-btn"] { border-radius: 9999px; border-color: var(--lx-border-color); }
[data-part="item"] { border-radius: 1.25rem; border: 1px solid var(--lx-border-color); box-shadow: 0 2px 12px rgb(0 0 0 / 0.04); }
[data-part="badge"] { border-radius: 9999px; }
[data-part="trust-badges"] { opacity: 0.75; }
```

## brutalist

```css
[data-part="cta"] { border-radius: 0; border: 3px solid var(--lx-text-color); box-shadow: 4px 4px 0 var(--lx-text-color); text-transform: uppercase; font-weight: 800; }
[data-part="cta"]:hover { transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--lx-text-color); }
[data-part="variant-btn"] { border-radius: 0; border: 2px solid var(--lx-text-color); font-weight: 700; }
[data-part="item"] { border: 2px solid var(--lx-text-color); border-radius: 0; box-shadow: 4px 4px 0 var(--lx-border-color); }
[data-part="badge"] { border-radius: 0; border: 2px solid var(--lx-text-color); font-weight: 800; }
```

## playful

```css
[data-part="cta"] { border-radius: 1.25rem; font-weight: 800; padding: 1.1rem 2.5rem; transition: transform 150ms ease; }
[data-part="cta"]:hover { transform: scale(1.04) rotate(-1deg); }
[data-part="variant-btn"] { border-radius: 1rem; border-width: 2px; font-weight: 700; }
[data-part="item"] { border-radius: 1.5rem; border: 2px solid var(--lx-border-color); }
[data-part="badge"] { border-radius: 9999px; font-weight: 800; }
```

## minimal

```css
[data-part="cta"] { border-radius: 0.375rem; box-shadow: none; font-weight: 500; }
[data-part="variant-btn"] { border-radius: 0.375rem; border-color: var(--lx-border-color); font-weight: 400; }
[data-part="item"] { border: none; border-radius: 0.5rem; background: var(--lx-surface-alt); box-shadow: none; }
[data-part="badge"] { border-radius: 0.25rem; font-weight: 500; }
[data-part="trust-badges"] { filter: grayscale(1); opacity: 0.6; }
```

## Rules

1. One pack per page — mixing packs is the #1 way to make a page look broken.
2. Scope to a section if two islands need different treatments: `#hero [data-part="cta"] { ... }`.
3. Packs compose with `compile_theme` output — they reference `--lx-*` variables, never hardcode colors.
4. Check the island's `schema.json` `parts` array before targeting a part name (`get_island_schema`).

---

# Asset Pipeline — Multi-Source Visual Strategy

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then run `compile_page_source`.

> **Inputs:** Approved page plan (from `/plan-page` workflow)
> **Outputs:** Asset manifest (URLs + purposes + section mapping)
> **When to load:** After page plan is approved, before HTML generation.

---

## Decision Tree

```
Need an image or video for a section?
│
├─ search_design_library({ query }) → found good match?
│  ├─ YES → use it (free, on-brand)
│  └─ NO ↓
│
├─ Product shot needed?
│  ├─ YES → use real images from list_products (NEVER generate fake products)
│  └─ NO ↓
│
├─ What type of asset?
│  ├─ Static image (background, lifestyle, texture, composite)
│  │  └─ generate_asset or edit_asset (built-in, costs credits)
│  │
│  ├─ Video (hero, demo, UGC-style)
│  │  └─ External MCP: HiggsField / Runway / Kling
│  │
│  ├─ Reference/mood imagery (competitor screenshots, inspiration)
│  │  └─ External MCP: Exa (web_search_exa)
│  │
│  ├─ Stock photography (realistic, non-AI look needed)
│  │  └─ External MCP: Unsplash / Pexels
│  │
│  └─ Specialized illustration (custom style beyond built-in)
│     └─ External MCP: OpenArt
│
└─ After sourcing → import_asset({ url, purpose, tags }) to persist in library
```

---

## Built-In Tools (Lexsis AI MCP)

| Tool | What it does | Cost |
|------|-------------|------|
| `search_design_library` | Search existing brand assets | Free |
| `generate_asset` | AI image generation (photography, illustration, 3d, editorial, abstract, texture) | Credits |
| `edit_asset` | Composite, inpaint, or style-transfer existing images | Credits |
| `view_asset` | Visually verify a generated/edited asset before using | Free |
| `import_asset` | Bring an external URL (or base64) into the design library for reuse. Call with **no arguments** to open an upload picker so the user can supply their own file — use that when they want to add their own logo/photo and you have no URL for it | Free |

**Always `search_design_library` first.** Existing assets are free and already brand-consistent.

See `design-enrichment.md` for detailed prompt patterns, style selection guide, compositing recipes, and HTML placement patterns.

---

## External MCPs (Detected at Runtime)

These tools are available when the user has the corresponding MCP installed. Check availability before suggesting.

### Exa — Image Research & Reference

```
web_search_exa({ query: "skincare brand hero photography editorial style" })
```

Use for: mood boards, competitor visual research, finding reference imagery to brief `generate_asset` more precisely, sourcing real lifestyle photos.

**Flow:** Exa search → find reference URL → `import_asset({ url })` to persist → use in page.

### HiggsField / Runway / Kling — Video Generation

Use when: TikTok traffic source, fashion/luxury vertical, product demo needed, brand has no existing video content.

**Flow:**
1. Generate video via external MCP (short clip, 3-8 seconds)
2. `extract_video_frames` → pull best frame as thumbnail
3. Use video URL in HeroMedia island or `<video>` tag
4. Set click-to-play (NEVER autoplay — costs 7% CVR)

**Video placement patterns:**
- Hero: click-to-play with compelling thumbnail image
- Product demo: inline player after benefits section
- Social proof: UGC-style video carousel
- Background: muted loop, heavily dimmed (luxury only)

### OpenArt — Specialized AI Illustration

Use when: `generate_asset(style: "illustration")` doesn't provide enough control over style, need specific artistic direction, or brand has a custom illustration language.

### Unsplash / Pexels — Stock Photography

Use when: brand has no library assets, AI generation looks too synthetic, need real-world photography (locations, hands, diverse models).

---

## Feeding External Assets Into Pages

All external assets MUST be persisted before use:

```
1. Source asset via external MCP → get URL
2. import_asset({ url, purpose: "hero_bg", tags: ["lifestyle", "summer"] })
   → returns { asset_id, url, width, height }
3. Use returned URL in page HTML (same as built-in assets)
```

This ensures: the asset is stored in the brand's library, available for reuse, and won't break if the external source goes down.

---

## Per-Page-Type Asset Budget

| Page Type | Hero (high) | Section BGs (medium) | Lifestyle (medium) | Video | Total assets |
|-----------|-------------|---------------------|--------------------|----|------|
| PDP | 1 | 0-1 | 1 | 0-1 | 2-4 |
| Landing | 1 | 2-3 | 0-1 | 0-1 | 3-5 |
| Homepage | 1 | 1 | 0 | 0 | 2 |
| Editorial | 1 | 3-4 | 2-3 | 0-1 | 6-9 |
| Collection | 0-1 | 0 | 0 | 0 | 0-1 |
| Bundle | 1 | 1 | 0 | 0 | 2-3 |

**Rules:**
- Check `get_credits_balance` before any generation
- Use `quality: "medium"` default; `"high"` only for hero images
- Products have their own Shopify images — never generate product shots

---

## Video in Pages

### When Video Converts Better
- TikTok/Reels traffic (video-native audience)
- Fashion/beauty (texture, movement, try-on)
- Luxury (cinematic brand storytelling)
- Product demos (85% say video convinced them to buy)

### Technical Integration
```html
<!-- Click-to-play video hero (use HeroMedia island) -->
<div data-island="HeroMedia" data-props='{"media":{"type":"video","src":"VIDEO_URL","poster":"THUMBNAIL_URL","autoplay":false}}'></div>

<!-- Inline video (no island needed for simple playback) -->
<video class="w-full rounded-xl" poster="THUMBNAIL_URL" controls playsinline>
  <source src="VIDEO_URL" type="video/mp4" />
</video>
```

### Anti-Patterns
- NEVER autoplay video (-7% CVR)
- NEVER use video as only hero content (needs fallback image)
- NEVER serve uncompressed video (use CDN URL from import_asset)

---

## Asset Manifest (Output Format)

After sourcing all assets, produce this manifest to hand to `/generate`:

```
Section: hero
  - URL: https://cdn.trylexsis.com/assets/abc123.jpg
  - Purpose: hero_bg
  - Source: generated (quality: high)

Section: social-proof
  - URL: https://cdn.trylexsis.com/assets/def456.mp4
  - Purpose: testimonial_video
  - Source: external (HiggsField)
  - Thumbnail: https://cdn.trylexsis.com/assets/def456-thumb.jpg

Section: benefits
  - URL: https://cdn.trylexsis.com/assets/ghi789.jpg
  - Purpose: lifestyle_shot
  - Source: library (existing)
```

The generation workflow uses these URLs directly in `<img src="">` and island props.

---

## Cost Control

1. `search_design_library` first — always (free)
2. `get_credits_balance` before expensive operations
3. Prefer `quality: "medium"` — reserve `"high"` for hero only
4. External MCP assets → `import_asset` to avoid re-fetching
5. CSS gradients/solid colors for sections that don't need imagery
6. Reuse: one hero image can serve as dimmed background for 2-3 sections

---

# Before Showing Draft to Merchant — QA Recipe

## Pre-flight Checklist

1. **Compile and validate source** — call `compile_page_source` with `source`, `head`, `theme_css`, and `scripts`
2. **Save as draft** — call `create_page_from_source` with `publish: false`
3. **Check integrity** — call `check_page_integrity` with the page's archetype

## Browser QA (if available)

### Viewports to test:
- Mobile: 390×844 (iPhone 14)
- Desktop: 1440×900

### Check for:
- [ ] No horizontal overflow at any viewport
- [ ] All images load (no broken/gray placeholders)
- [ ] Hero section visible above fold on both viewports
- [ ] Text readable without zooming on mobile
- [ ] Interactive islands respond to clicks (FAQ accordion, BuyBox variant selection)
- [ ] No console errors blocking render

## Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Gray product cards | Missing `image`/`media` in product data | Add image URLs or use `productIds` for auto-fetch |
| FAQ items don't toggle | Missing island hydration script | Ensure page includes island runtime |
| 401 on publish | Using API key auth | Endpoint supports X-API-Key — ensure key is valid |
| Images too large/slow | Using original Shopify CDN URLs | Append `&width=800` to resize |

## Draft vs Live

- `publish: false` → draft at `/v/{slug}?shop={domain}&preview=1`
- `publish: true` → live page, edge-cached, visible to shoppers
- Always draft first, QA, then publish

---

# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. `compile_page_source` — compile and validate the generated source
2. `create_page_from_source` — persist the initial draft
   - `publish: false` → preview URL only (not live on store)
3. `publish_page` — go live only after explicit approval

## Operations

### Create Draft (New Page)
```
compile_page_source({ source, head, theme_css, scripts })
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
```
Returns: page_id, page_url, preview_url

### Preview (Draft)
```
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
```
Returns: preview_url (not visible to store visitors)

### Publish Existing Page
```
publish_page(page_id)
```
Makes a draft page live.

### Unpublish
```
unpublish_page(page_id)
```
Takes page offline but preserves it in DB.

### Duplicate
```
duplicate_page(page_id, { title: "New Title" })
```
Creates a copy — useful for A/B test variants.

### Create Experiment Variant
```
create_page_variation(page_id, { changes: {...} })
```
Creates variant for A/B testing.

## Prerequisites

- Store must be connected (`get_connected_stores`)
- Brand kit should exist for proper theming

## Post-Publish

After publishing, the page is served via:
- Shopify store (native page)
- pages.lexsis.app (standalone via edge worker)
- Custom domain (if tracking domain configured)

---

# Storefront Page Generation

> **Full workflow:** See `generation-protocol.md` for Phases 1-5 execution (context gathering, HTML generation, validation, publishing, visual verification).

This file covers quick-reference patterns for generation.

---

## Template-First Rule

Always search `search_section_templates` before generating sections from scratch. It returns metadata only — fetch markup for the ids you pick with `get_section_template`:

```
search_section_templates({ query: "hero with video background for fashion", section: "hero", industry: "fashion", mood: "editorial" })
get_section_template({ ids: ["<chosen id from results>"] })
```

- If a matching template is found (score > 0.7): USE IT. Its returned `source`
  contains the section markup, CSS, and JS ready to tailor with brand-specific
  copy/images, then pass to
  `compile_page_source`.
- If no match: generate from scratch in Phase 4.

Templates are conversion-proven, pixel-perfect, and faster than custom generation.
Use `format: "compiled_reference"` only to inspect renderer output; never paste its
`data-island` / `data-props` markup into source-authoring tools.

For a full page, check `search_page_kits` before assembling sections one at a time — it returns curated multi-section groupings that already share one palette/vertical:

```
search_page_kits({ query: "clinical supplements PDP", page_type: "pdp", industry: "supplements" })
```

---

## Page Type Section Defaults

**Product Landing (PDP)** — 8-10 sections:
Hero (split) → Gallery → BuyBox → Benefits → Ingredients/Specs → Reviews → Related Products → FAQ → Sticky CTA → Footer

**Campaign Landing** — 10 sections:
Hero → Problem/Pain → Solution → Key Benefits → Social Proof → How It Works → Comparison → Offer/Pricing → FAQ → CTA

**Homepage** — 7-8 sections:
Hero → Featured Products → Brand Story → Categories → Testimonials → Newsletter → Trust Bar → Footer

**Collection** — 6 sections:
Hero Banner → Filter/Sort → Product Grid → Promo Card → Social Proof → Footer

**Editorial** — 6-8 sections:
Full-Bleed Hero → Intro Copy → Shoppable Gallery → Content Block → Product Spotlight → Related Reads → Footer

**Listicle** — 7-9 sections:
Hero + TOC → Methodology → Numbered Items → Comparison Table → Verdict → FAQ → CTA

**Bundle** — 6-8 sections:
Hero + Savings Hook → Step Progress → Product Selection → Social Proof → FAQ → Sticky Summary

---

# Storefront Page Editing

Edit existing pages using section-level operations.

## Edit Flow

1. `find_page` — locate the target page
2. `get_page_source` and `inspect_page_sections` — read source and structure
3. Edit exactly one source-format section
4. `update_section_from_source` — compile, preflight, and save
5. `check_page_integrity` — verify the completed page

## Operations

### Update/Replace a Section

```
update_section_from_source({ page_id, section_id, source })
```
- Replaces the compiled section from source-format HTML
- Auto-bumps page version
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
update_section_from_source({ page_id, source, position })
```
- Position: "before:{section_id}" or "after:{section_id}" or index number
- Must include full section HTML

### Remove a Section

```
remove_page_section(page_id, section_id)
```
- Irreversible — confirm with user first
- Auto-bumps version

### Reorder Sections

```
move_page_section(page_id, section_id, new_position)
```
- Position is 0-indexed
- All other sections shift accordingly

## Best Practices

- Always `get_page` first to understand current structure
- Reference section IDs from the page data (don't guess)
- After editing, run `check_page_integrity` before telling the user it is done
- For multi-section changes, batch them (each call bumps version)
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout
