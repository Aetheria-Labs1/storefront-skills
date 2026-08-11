---
name: browser-analyze
description: Use Codex Browser to analyze a URL for design extraction, CRO evidence, or competitor research. Use when a task provides a reference or storefront URL.
---

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
