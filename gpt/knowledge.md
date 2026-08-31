<!-- GENERATED from skills/ by scripts/build-distributions.py — DO NOT EDIT.
     storefront-skills v5.4.0 · 14 skills · 54 island schemas -->

# Lexsis Storefront Skills — Knowledge Base

## Workflows

---

# Skill: analyze-page

> Analyze a reference webpage into a brand-safe structural brief. Use for competitor or inspiration URLs before visual-page; do not generate page source or production assets here.

# Analyze Storefront Page

Own structural analysis of a reference page. Do not write replacement HTML,
generate assets, create a page, or publish. `visual-page` owns the new-page
workflow after this brief is ready.

## Workflow

1. Capture the URL with `browser-analyze` when Browser is available.
2. Classify the page: PDP, landing, homepage, collection, editorial, or other.
3. Extract:
   - global design tokens and visual rhythm
   - section order, proportions, and responsive behavior
   - CTA, trust, urgency, and social-proof placement
   - interaction patterns and candidate Lexsis islands
4. Separate reusable structure from protected source material.
5. Output `VISUAL_PAGE_INPUT`:

```text
Source URL: [...]
Page type: [...]
Design direction: [...]
Section map: [...]
Responsive behavior: [...]
Conversion patterns: [...]
Candidate islands: [...]
Do not carry forward: [copy, logos, product imagery, claims, testimonials]
```

## Safety

- Use the source only for hierarchy, composition, and interaction patterns.
- Do not copy text, logos, images, product claims, pricing, reviews, or brand
  marks.
- Do not write source-format HTML in this skill.

## Optional Follow-Up

This skill can end after producing `VISUAL_PAGE_INPUT`. When the user wants a
new brand-owned page from that brief, `visual-page` can use it as input.

---

# Skill: asset-prep

> Source and prepare visual assets for a storefront page — search the brand library first, then generate, import, or pull from external MCPs (video, stock, research imagery). Also answers to its old name, asset-pipeline. Run after /plan-page; produces the asset manifest generation consumes.

> **Inputs:** Approved page plan, optionally with a `visual-page` layout brief
> **Outputs:** Asset manifest (URLs + purposes + section mapping)
> **When to load:** After page plan is approved, before HTML generation.

---

## Decision Tree

```
Need an image or video for a section?
│
├─ lexsis_asset_library({ action: "search", args: { query, workspace_id } })
│  → found good match?
│  ├─ YES → use it (free, on-brand)
│  └─ NO ↓
│
├─ Product shot needed?
│  ├─ YES → use real images from lexsis_catalog action list/get
│  └─ NO ↓
│
├─ What type of asset?
│  ├─ Static image (background, lifestyle, texture, composite)
│  │  └─ lexsis_drafts action asset_generate
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
└─ After sourcing → lexsis_asset_upload action import
   with { url, purpose, tags, workspace_id }
```

---

## Built-In Tools (Lexsis AI MCP)

| Tool | What it does | Cost |
|------|-------------|------|
| `lexsis_asset_library` → `search` | Search workspace assets | Free |
| `lexsis_drafts` → `asset_generate` | Generate, composite, inpaint, or restyle | Credits |
| `lexsis_assets` → `view` | Visually verify an asset | Free |
| `lexsis_asset_upload` → `import` | Import URL, base64, conversation attachments, or open the upload picker | Free |

Always search first. Pass `workspace_id` explicitly for multi-workspace
accounts. Automatic selection is allowed only with one active workspace.

When a `visual-page` layout concept is supplied, use it only for composition,
crop, and visual-rhythm guidance. It is not a production asset. Source final
media through the library, Shopify product data, generation, or import.

See `design-enrichment.md` for detailed prompt patterns, style selection guide, compositing recipes, and HTML placement patterns.

---

## External MCPs (Detected at Runtime)

These tools are available when the user has the corresponding MCP installed. Check availability before suggesting.

### Exa — Image Research & Reference

```
web_search_exa({ query: "skincare brand hero photography editorial style" })
```

Use for: mood boards, competitor visual research, finding reference imagery to
brief `lexsis_drafts` action `asset_generate`, and sourcing real lifestyle
photos.

**Flow:** Exa search → find reference URL → `lexsis_asset_upload` action
`import` → use the returned permanent URL.

### HiggsField / Runway / Kling — Video Generation

Use when: TikTok traffic source, fashion/luxury vertical, product demo needed, brand has no existing video content.

**Flow:**
1. Generate video via external MCP (short clip, 3-8 seconds)
2. `lexsis_campaigns.frames` → pull best frame as thumbnail
3. Use video URL in HeroMedia island or `<video>` tag
4. Set click-to-play (NEVER autoplay — costs 7% CVR)

**Video placement patterns:**
- Hero: click-to-play with compelling thumbnail image
- Product demo: inline player after benefits section
- Social proof: UGC-style video carousel
- Background: muted loop, heavily dimmed (luxury only)

### OpenArt — Specialized AI Illustration

Use when `lexsis_drafts` action `asset_generate` with illustration styling does
not provide enough control, or the brand has a custom illustration language.

### Unsplash / Pexels — Stock Photography

Use when: brand has no library assets, AI generation looks too synthetic, need real-world photography (locations, hands, diverse models).

---

## Feeding External Assets Into Pages

All external assets MUST be persisted before use:

```
1. Source asset via external MCP → get URL
2. lexsis_asset_upload({
     action: "import",
     args: {
       url,
       purpose: "hero_bg",
       tags: ["lifestyle", "summer"],
       workspace_id
     }
   })
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
- Check `lexsis_workspace` action `credits` before generation
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
- NEVER serve uncompressed video; use the permanent imported CDN URL

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

1. `lexsis_asset_library` action `search` first
2. `lexsis_workspace` action `credits` before expensive operations
3. Prefer `quality: "medium"` — reserve `"high"` for hero only
4. External MCP assets → `lexsis_asset_upload` action `import`
5. CSS gradients/solid colors for sections that don't need imagery
6. Reuse: one hero image can serve as dimmed background for 2-3 sections

## Optional Follow-Up

This skill can end after returning `ASSET_MANIFEST`. `generate` can consume the
manifest with an approved page plan and optional visual layout brief when the
user asks for a draft.

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

Return `PAGE_ANALYSIS_INPUT`. Do not generate source HTML or page assets here.

---

## Fallback (No @Browser Available)

If @Browser is not available or not enabled:
1. Ask for screenshots or use any user-supplied visual reference.
2. Note the limitation: no DOM access, mobile viewport test, or interaction detection.
3. Hand the available evidence to `analyze-page` or `remix`.

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

## Optional Follow-Up

This skill can end after returning `PAGE_ANALYSIS_INPUT`. That evidence can
later inform `analyze-page`, `remix`, or `optimize` if the user requests one
of those outcomes.

---

# Skill: cart

> Inspect, assign, and edit cart profiles, including offers, shipping goals, subscriptions, responsive behavior, and scoped custom CSS.

# Configure Cart Profiles

Use this workflow for cart profile configuration and page targeting.

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

1. `lexsis_cart.get`
2. `lexsis_drafts.cart_set`
3. `lexsis_drafts.cart_edit`

Profile creation, duplication, publishing, rollback, defaults, campaign
targeting, history, and archival remain in the Lexsis app.

## Workflow

### 1. Inspect

Call `lexsis_cart.get` before making changes.

- Pass `page_id` to inspect the effective profile and resolution source.
- Pass `cart_profile_id` to inspect an editable draft.
- Pass `store_id` alone to list available profiles.

Do not assume that the store default is the page's effective cart.

### 2. Assign when requested

Call `lexsis_drafts.cart_set` with `page_id` and a published `cart_profile_id`.

Pass `cart_profile_id: null` to remove the page assignment. This restores
campaign, default, or legacy fallback resolution.

### 3. Edit the draft

Call `lexsis_drafts.cart_edit` with a partial patch. The same tool handles:

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

`lexsis_drafts.cart_edit` never publishes. Tell the merchant to review and publish in the
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

1. Call `lexsis_cart.get` with the page ID.
2. Confirm `resolution_source` and profile identity.
3. Preview add-to-cart and header cart triggers.
4. Check desktop and mobile modes.
5. Confirm offers use real products and subscriptions appear only when
   selling plans exist.
6. Confirm draft changes remain non-live until published.

Read `storefront-engine/references/cart-composition.md` and
the cart profile management reference for the detailed contract.

## Optional Follow-Up

This skill is complete when the cart profile is reviewed in the Lexsis app. If
the user separately requests page integration, `generate` can use the confirmed
profile requirements.

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
lexsis_analytics({ action: "page", args: { page_id } })
```
Returns: CVR, bounce rate, time on page, traffic sources, device split, top-performing sections.

### Time Series Trends
```
lexsis_analytics({ action: "timeseries", args: { metric: "conversions", period: "daily", range: "30d" } })
```
Returns: daily/weekly trends for hits, conversions, revenue, AOV.

### Revenue Attribution
```
lexsis_analytics({ action: "attribution", args: { page_id? } })
```
Returns: ROAS by channel, revenue per page, top campaigns driving conversions.

## A/B Testing Flow

### 1. Create Experiment
```
lexsis_drafts({
  action: "experiment_create",
  args: {
    page_id: "...",
    variants: [{ blueprint_id: "...", weight: 50 }, { blueprint_id: "...", weight: 50 }]
  }
})
```

### 2. Monitor Results
```
lexsis_analytics({ action: "experiment", args: { experiment_id } })
```
Returns: CVR per variant, statistical significance (mSPRT), sample sizes, winner recommendation.

### 3. Scale Winner
```
lexsis_live_ops({ action: "scale_winner", args: { experiment_id, variant_id: "..." } })
```
Scales winning variant to 100% traffic, marks experiment complete.

## Best Practices

- Wait for statistical significance before scaling winner
- Minimum ~1000 visitors per variant for reliable results
- Check device split — a variant may win on mobile but lose on desktop
- Use `lexsis_analytics.attribution` to understand which traffic sources convert best
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
lexsis_workspace → get/stores
lexsis_brand → brand_kit/list_themes/get_theme
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Load Personas and Base Page

```
lexsis_campaigns({ action: "personas", args: { workspace_id } })
```

Review available audience segments. If none exist, define inline: name, demographics, pain points, motivations, objections, buying stage, tone preference.

```
lexsis_pages({ action: "get", args: { page_id } })
lexsis_pages({ action: "content", args: { page_id } })
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
lexsis_asset_library({ action: "search", args: { query: "<persona-relevant imagery>", workspace_id } })
```

Find images reflecting the persona's world. Generate if needed:
```
lexsis_drafts({ action: "asset_generate", args: { prompt: "...", demographic: "<persona context>", workspace_id } })
```

### Step 5 — Create Each Variant

For each persona:
```
lexsis_drafts({
  action: "page_variation",
  args: {
    page_id,
    name: "<persona_name> variant",
    changes: {
      sections: [
        { section_id: "hero", html: "...", css: "..." },
        { section_id: "social-proof", html: "..." },
        { section_id: "cta-block", html: "..." }
      ]
    }
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
lexsis_pages({ action: "integrity", args: { page_id: variant_page_id, archetype } })
```

Ensure all render correctly, islands work, mobile intact.

### Step 7 — Visual Verification (Each Variant)

Use the host agent's browser capability at 390px, 768px, and 1280px for every
variant. Lexsis does not create shared browser sessions. If browser access is
unavailable, provide the preview URLs and state that visual QA remains.

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
lexsis_drafts({
  action: "experiment_create",
  args: {
    page_id: base_page_id,
    variants: [
      { page_id: variant_a_id, weight: 33, targeting: { persona: "deal-seekers" } },
      { page_id: variant_b_id, weight: 33, targeting: { persona: "quality-seekers" } },
      { page_id: base_page_id, weight: 34, targeting: { default: true } }
    ]
  }
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
- Each variant passes `lexsis_pages` action `integrity` independently
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
lexsis_workspace → get/stores
```

These two calls ALWAYS run first. No exceptions.

### Step 2 — Load Current Page and Baseline

```
lexsis_pages({ action: "get", args: { page_id } })
lexsis_analytics({ action: "page", args: { page_id } })
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
lexsis_drafts({ action: "page_duplicate", args: { page_id } })
```

Creates exact copy. Then apply the SINGLE focused change:
```
lexsis_drafts({
  action: "page_update_section",
  args: { page_id: variant_page_id, section_id, source, expected_version }
})
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
lexsis_pages({ action: "integrity", args: { page_id: variant_page_id, archetype } })
```

Ensure variant renders correctly, all islands work, mobile intact.

### Step 6 — Visual Verification

Use the host agent's browser capability at 390px, 768px, and 1280px. If it is
unavailable, provide the preview URL and state that visual QA remains.

Checklist:
- [ ] The ONE change is clearly visible
- [ ] Everything else identical to control
- [ ] Mobile layout intact
- [ ] Islands hydrated correctly
- [ ] No unintended side effects (broken spacing, color bleed)

### Step 7 — Launch Experiment

```
lexsis_drafts({
  action: "experiment_create",
  args: {
    page_id: page_id,
    hypothesis: "Changing [X] will improve [metric] because [reason]",
    variants: [
      { page_id: page_id, weight: 50, name: "Control (A)" },
      { page_id: variant_page_id, weight: 50, name: "Variant (B)" }
    ],
    primary_metric: "conversion_rate",
    minimum_sample: 1000
  }
})
```

50/50 split is standard. 80/20 only for high-traffic pages testing risky changes.

### Step 8 — Monitor Results

```
lexsis_analytics({ action: "experiment", args: { experiment_id } })
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
lexsis_live_ops({ action: "scale_winner", args: { experiment_id, variant_id: winning_variant_id } })
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
- Both variants pass `lexsis_pages` action `integrity`
- Control remains untouched for test duration
- Secondary metrics monitored alongside primary
- Learning documented regardless of outcome (losses teach as much as wins)
- Wait for mSPRT -- never call early based on gut feeling

## Optional Follow-Up

This skill can end with a documented winner or learning. `optimize` can use
that evidence for a later page improvement when the user requests one.

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

When invoked by `visual-page`, use its approved plan, final asset manifest, and
layout brief as the binding inputs. Recreate the approved composition with
source-format HTML and valid islands; never embed the visual layout reference as
page media.

# Storefront Page Generation

Generate high-quality Shopify storefront pages using the Lexsis AI MCP tools.

> **Prerequisites**: Read `vibe://docs/generation-guide`, `vibe://skills/generation-protocol`, and `vibe://skills/source-format` first — they define the source authoring format, CSS variable system, island integration, and visual verification step.

## Generation Flow (Two-Phase)

### Phase 2 — Context Gathering (run ALL in parallel)

```
lexsis_workspace → get       → workspace context
lexsis_workspace → stores    → store ID and domain
lexsis_brand → brand_kit     → logo, fonts, colors, voice, border radius
lexsis_brand → list_themes   → available themes
lexsis_brand → get_theme     → complete selected theme + theme_css
lexsis_design → guide        → design philosophy + don'ts
lexsis_catalog → list        → product catalog
lexsis_asset_library → search → existing brand assets
```

Run independent reads in parallel. If more than one workspace or store is
available, select explicitly. If no valid theme exists in the selected
workspace, stop and report the configuration error—never borrow another
workspace's theme.

### Phase 3 — Asset Preparation

Decision tree per section:
1. `lexsis_asset_library` action `search` — check existing assets first
2. `lexsis_drafts` action `asset_generate` — only if no suitable match exists
3. Add `reference_images` to edit or composite
4. `lexsis_assets` action `view` — verify before page use

Budget: 3-5 generated assets per page max. Existing assets = free.

### Phase 4a — Draft Source HTML

Author the page in **source format** (see `vibe://skills/source-format`) — plain HTML, never JSON-escaped:
- Sections delimited by `<!-- section: id -->` comments
- Islands as `<lx-island name="BuyBox"><script type="application/json">{...props}</script></lx-island>` — use `vibe://schema/island/{name}` for exact prop shapes
- Section CSS in a `<style>` block, section JS in a `<script>` block per section
- Use `theme_css` returned by `lexsis_brand` action `get_theme`, or generate it
  with action `compile_theme` when intentionally authoring a new palette
- Focus on visual design: layout, typography, color, spacing, imagery; animations via `data-behavior="gsap-*"` presets or shared keyframes
- Write real copy naturally (apostrophes/quotes are fine — never escape anything; never Lorem Ipsum)
- Use asset URLs from Phase 3 in `<img>` tags

### Phase 4b — Compile & Fix

```
lexsis_pages({
  action: "compile",
  args: { source, head, theme_css, scripts }
}) → compiled page + issues + compiled_page_css
```

Fix reported issues and recompile. `missing_candidates` must be empty: Tailwind
is compiled once into `compiled_page_css`; do not add a runtime Tailwind CDN or
separate page stylesheet.

### Phase 5 — Publish + Visual Verify

```
lexsis_page_create({
  action: "create",
  args: {
    source, head, theme_css, scripts, slug, archetype,
    workspace_id, store_id, theme_id,
    inherit_header: true, inherit_footer: true,
    publish: false
  }
}) → preview_url
```

**Visual verification is REQUIRED before marking complete:**

Use the host agent's own browser capability. The Lexsis MCP does not create or
pool Playwright sessions. Verify 390px, 768px, and 1280px; use screenshots when
available and computed styles/DOM geometry when they are not.

**Checklist:**
- [ ] Hero visible above fold (headline + CTA without scrolling)
- [ ] Brand colors applied (not default purple)
- [ ] Fonts loaded (not system fallback)
- [ ] Images rendering (not broken/placeholder)
- [ ] Layout correct at 390px, 768px, and 1280px with no horizontal scroll
- [ ] Islands hydrated (BuyBox shows product data, not empty div)
- [ ] CTA contrast ≥ 4.5:1

If issues, use `lexsis_drafts` action `page_update_section` or `page_patch`,
then repeat QA. Return the draft preview. Call `lexsis_live_ops` action
`publish` only after explicit approval.

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

- Mobile-first (test 390px, 768px, and 1280px)
- All brand colors via `--lx-*` CSS variables (never hardcoded hex in HTML)
- Proper heading hierarchy (single h1 in hero, h2 per section, h3 for sub-items)
- Islands for ALL commerce interactions (add-to-cart, checkout, cart drawer)
- All images from asset tools (never external URLs unless Shopify CDN)
- No fetch/XHR, eval, localStorage, @import, duplicate IDs
- Hero headline ≤ 8 words, visible without scrolling
- Use shared keyframes (fadeUp, fadeIn, scaleIn) — don't define new @keyframes unless truly unique

## Scope Boundary

Do not analyze ads, screenshots, competitor URLs, or reference pages here.
`browser-analyze`, `analyze-page`, and `remix` create the safe source brief;
`visual-page` owns the resulting layout concept and approval.

## Optional Follow-Up

This skill can end after source compilation, draft creation, and visual QA
produce `DRAFT_READY`. `publish` is available only when the user explicitly
asks to make that draft live.

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

1. `lexsis_pages` action `find`
2. `lexsis_pages` actions `edit_context`, `source`, and `inspect`
3. Make section-level source changes
4. `lexsis_drafts` action `page_update_section` or `page_patch`
5. `lexsis_pages` actions `diff` and `integrity`

## Operations

### Update/Replace a Section

```
lexsis_drafts({ action: "page_update_section", args: { page_id, section_id, source, expected_version } })
```
- Replaces the compiled section from one source-format section
- Auto-bumps page version
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
lexsis_drafts({ action: "page_update_section", args: { page_id, source, position, expected_version } })
```
- Position: "before:{section_id}" or "after:{section_id}" or index number
- Must include full section HTML

### Remove a Section

```
lexsis_drafts({ action: "page_remove_section", args: { page_id, section_id, expected_version } })
```
- Creates a reversible new page version
- Auto-bumps version

### Reorder Sections

```
lexsis_drafts({ action: "page_move_section", args: { page_id, section_id, position, expected_version } })
```
- Position is 0-indexed
- All other sections shift accordingly

## Best Practices

- Always read `edit_context` before writing
- Reference section IDs from the page data (don't guess)
- After edits, run `diff` and `integrity`
- Batch related changes with `page_patch` so they create one version
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
lexsis_workspace → get/stores
lexsis_brand → brand_kit/list_themes/get_theme
lexsis_design → guide
```

These four calls ALWAYS run first. No exceptions.

### Step 2 — Locate and Inspect Target Page

```
lexsis_pages({ action: "find", args: { query: "page name or slug" } })
```
Or:
```
lexsis_pages({ action: "list", args: { status: "published" } })
```

Then load full page data:
```
lexsis_pages({ action: "get", args: { page_id } })
lexsis_pages({ action: "inspect", args: { page_id } })
```

Understand: section count, section types, content blocks, current `--lx-*` variables, islands in use.

### Step 3 — Analyze Performance

```
lexsis_analytics({ action: "page", args: { page_id } })
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
lexsis_drafts({ action: "page_update_section", args: { page_id, section_id, source, expected_version } })
```

For reordering (if scroll-depth data suggests better flow):
```
lexsis_drafts({ action: "page_move_section", args: { page_id, section_id, position, expected_version } })
```

All updated sections must use `--lx-*` CSS variables from current brand kit. No hardcoded colors or fonts.

### Step 5 — Validate

```
lexsis_pages({ action: "integrity", args: { page_id, archetype } })
```

Ensure no broken islands, valid HTML structure, responsive layout intact.

### Step 6 — Show Before/After

```
lexsis_pages({ action: "diff", args: { page_id, version_a: previous_version, version_b: current_version } })
```

Present structural diff to user for approval before publishing.

### Step 7 — Load Preview and Verify Visually

```
lexsis_pages({ action: "get", args: { page_id } })
```

Use the returned `preview_url`.

Use the host agent's browser capability at 390px, 768px, and 1280px. Lexsis
does not create a shared browser session. If unavailable, provide the preview
URL and state that visual verification remains.

Checklist:
- [ ] Brand colors applied (current kit, not old defaults)
- [ ] Fonts loading correctly (not system fallback)
- [ ] High-CVR sections unchanged in structure
- [ ] Mobile layout intact or improved
- [ ] All islands still functional (cart, forms)
- [ ] Section spacing consistent
- [ ] No horizontal scroll on mobile

If issues are found, patch through `lexsis_drafts`, then re-verify.

### Step 8 — Go Live (User Confirms)

Only after user approves:
```
lexsis_live_ops({ action: "publish", args: { page_id } })
```

If redesign later hurts metrics: `lexsis_live_ops.rollback(page_id, version_id)` is available.

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
- Page passes `lexsis_pages` action `integrity` with zero errors

## Optional Follow-Up

This skill can end with a validated page update. `publish` is available for an
explicit release request, while `experiment` can use a testable hypothesis
when the user wants a controlled comparison.

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
lexsis_brand → brand_kit/get_theme → colors, fonts, voice, spacing
lexsis_design → guide              → brand philosophy + don'ts
lexsis_catalog → list              → available product data
lexsis_brand → navigation          → navbar/footer links
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

### Embedded Use by `visual-page`

When `visual-page` calls this workflow, produce the same plan as
`PLAN_DRAFT` and do not ask for approval yet. `visual-page` creates a visual
layout reference with `lexsis_drafts` action `asset_generate` and presents it
plus the plan as one
approval decision.

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

When run directly, wait for user confirmation. If user suggests changes, update
the plan and re-present.

## Step 5 — Next Steps

Once approved, the user can:
- Run `$generate` — carry the plan forward as the binding blueprint
- Or use the plan with any generation flow

The plan becomes BINDING for generation:
- Phase 2 context gathering targets the plan's requirements
- Phase 3 asset generation follows the plan's imagery needs
- Phase 4 HTML generation follows the plan's section sequence EXACTLY
- Section purposes from the plan guide the copywriting
- Animation choices from the plan guide the JS/CSS

## Optional Follow-Up

This skill can end with an approved plan. `visual-page` can use it for a
visual-first concept, or `asset-prep` and `generate` can use it when the user
wants to continue directly to a draft.

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

1. Require a `DRAFT_READY` page from `generate` or a validated update from
   `optimize`.
2. Read `lexsis_pages` action `edit_context` and confirm
   `has_unpublished_changes` when promoting an edited published page.
3. Confirm the preview has passed QA at 390px, 768px, and 1280px using the host
   agent's browser capability.
4. Confirm the user explicitly wants a live release.

## Operations

### Ready Draft Requirement

`generate` creates and validates draft previews. Do not recreate source or
compile it here. Require the page ID, preview URL, and completed visual QA
before release.

### Publish Live (Explicit Approval Required)
```json
{
  "name": "lexsis_live_ops",
  "arguments": {
    "action": "publish",
    "args": { "page_id": "page-uuid" }
  }
}
```
Only call this after explicit approval. A successful publish promotes the
reviewed current version to the immutable public `published_version_id`.
Failure preserves the previous live version.

### Unpublish
```
lexsis_live_ops({ action: "unpublish", args: { page_id } })
```
Takes page offline but preserves it in DB.

### Duplicate
```
lexsis_drafts({ action: "page_duplicate", args: { page_id, title: "New Title" } })
```
Creates a copy — useful for A/B test variants.

### Create Experiment Variant
```
lexsis_drafts({ action: "page_variation", args: { page_id, changes: {...} } })
```
Creates variant for A/B testing.

## Prerequisites

- Resolve the store with `lexsis_workspace` action `stores`
- `lexsis_brand` action `list_themes` must return a valid selected/default theme
- Run `lexsis_pages` action `integrity` before publishing

## Post-Publish

After publishing, the page is served via:
- Shopify store (native page)
- pages.lexsis.app (standalone via edge worker)
- Custom domain (if tracking domain configured)

## Optional Follow-Up

This skill ends after release. Later, `experiment` can test a focused variant
or `optimize` can address performance evidence when the user requests it.

---

# Skill: remix

> Convert a competitor page, inspiration site, or ad creative into a brand-safe visual reference brief. Use when a user wants to adapt a reference; hand the brief to visual-page instead of building the page here.

# Remix Reference Into a Brief

Own reference interpretation only. Do not generate page source, production
assets, drafts, or live pages. `visual-page` owns the new-page workflow.

## Inputs

- competitor or inspiration URL
- screenshot or ad creative
- user's product, page goal, and brand direction

## Workflow

1. Capture the source with `browser-analyze` when a URL is available.
2. For ads, call `lexsis_campaigns.analyze` and `lexsis_campaigns.match_persona`.
3. Extract only reusable design signals:
   - page type and section order
   - hierarchy, grids, proportions, whitespace, and motion
   - CTA and trust-signal placement
   - responsive behavior
   - candidate Lexsis islands
4. Exclude competitor copy, product claims, logos, imagery, testimonials,
   pricing, and proprietary marks.
5. Output `VISUAL_PAGE_INPUT`:

```text
Source type: [URL | screenshot | ad]
Page type: [landing | PDP | homepage | collection | editorial]
Audience and conversion goal: [...]
Safe composition cues: [...]
Section map: [...]
Mobile behavior: [...]
Candidate islands: [...]
Avoid: [competitor-specific content and patterns]
```

## Non-Negotiable Safety

- Recreate structure and visual intent, never protected content.
- Use the user's own brand kit, products, claims, assets, and copy.
- Do not hotlink or import competitor images into production media.

## Optional Follow-Up

This skill can end after returning `VISUAL_PAGE_INPUT`. `visual-page` can use
that brief when the user wants a visual layout reference and brand-owned draft.

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

1. Call `lexsis_support` with action `search_docs` and the user's query (or your own lookup query)
2. If results include a resource URI, read that exact URI for full content.
3. If results reference an island, read `vibe://catalog/islands/{name}` for selection guidance. Once selected, read `vibe://schema/island/{name}` for exact props and source-format markup.
4. Synthesize relevant findings — don't dump raw results, extract what's actionable

## Tool Usage

### Primary search
```json
{
  "name": "lexsis_support",
  "arguments": {
    "action": "search_docs",
    "args": { "query": "<search terms>", "limit": 5 }
  }
}
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

### Deep-read a result
Use only a resource URI returned by `lexsis_support` action `search_docs`. Do not invent a resource
name or rely on a hard-coded catalog: the search result is the authoritative
availability check.

### Deep-read an island
Read resource URI: `vibe://catalog/islands/{islandName}`
Returns selection guidance, variants, behavior, and styling surface. Then read
`vibe://schema/island/{islandName}` for the exact prop contract and
`<lx-island>` source example.

## Examples

| User asks | Search call | Follow-up |
|-----------|------------|-----------|
| "How does BuyBox work?" | `lexsis_support.search_docs({ query: "BuyBox", category: "islands" })` | Read `vibe://catalog/islands/BuyBox` |
| "Beauty landing page patterns" | `lexsis_support.search_docs({ query: "beauty landing page", category: "verticals" })` | Read the returned resource URI |
| "Countdown urgency techniques" | `lexsis_support.search_docs({ query: "countdown urgency scarcity" })` | — |
| "Publishing workflow" | `lexsis_support.search_docs({ query: "publish page workflow", category: "recipes" })` | Read the returned resource URI |
| "What islands handle reviews?" | `lexsis_support.search_docs({ query: "reviews testimonials", category: "islands" })` | Read `vibe://catalog/islands/ReviewCarousel` |

## Tips

- Use specific terms, not vague questions — "BuyBox variant swatches" not "how to show products"
- Combine category filter with query for best results
- If search returns nothing, try broader terms or drop the category filter
- Skill resources contain full implementation guides — always read them when referenced

## Optional Follow-Up

This skill can end after returning the concise answer. Its findings can inform
any workflow the user explicitly chooses, including `visual-page`, `plan-page`,
`asset-prep`, `generate`, `optimize`, `experiment`, `cart`, or `publish`.

---

# Skill: storefront-engine

> Route a storefront request to the one Lexsis workflow that owns it. Use for broad or ambiguous requests spanning visual page creation, reference analysis, assets, generation, optimization, experiments, cart configuration, or publishing.

# Storefront Engine

This is the router. It does not build pages, generate assets, edit pages, or
publish. Select one owning skill and pass it only the context it needs.

Read `references/workflow-handoffs.md` for optional workflow connections.

Reference files use compact `router.action(...)` notation. Execute that as the
named consolidated MCP router with `{"action": "action", "args": {...}}`.
Never call a former one-tool-per-operation name directly.

## Routing

| User intent | Owning skill |
|---|---|
| New page from a brief, product, ad, screenshot, URL, or mixed input | `visual-page` |
| Text-only section and conversion plan, without visual concept generation | `plan-page` |
| Analyze a reference URL into a safe structural brief | `analyze-page` |
| Capture a URL with Browser before analysis | `browser-analyze` |
| Prepare final page assets | `asset-prep` |
| Build an approved plan and asset manifest into a draft | `generate` |
| Improve an existing page using performance evidence | `optimize` |
| Create or monitor a controlled experiment | `experiment` |
| Configure cart profiles | `cart` |
| QA a ready draft and release it live | `publish` |
| Search a schema, workflow, or troubleshooting answer | `search-docs` |
| Extract a reusable island layout for maintainers | `extract-island` |

## Routing Rules

1. Use `visual-page` for every new page request unless the user explicitly
   asks for planning only.
2. Send a reference URL through `browser-analyze` or `analyze-page` before
   `visual-page`; do not make `visual-page` rediscover the same evidence.
3. Do not call `generate` until the plan is approved and `asset-prep` returns
   the final asset manifest.
4. Do not call `publish` until a draft has passed visual QA and the user
   explicitly asks to go live.
5. Do not use `remix` to build a page. It produces a brand-safe reference
   brief for `visual-page`.

## Completion

This router is complete after selecting a workflow. The selected skill can run
independently; do not require a chain merely because a related workflow exists.

---

# Skill: visual-page

> Turn a storefront brief, product, ad, screenshot, reference URL, or mixed input into an approved visual layout brief and a draft Shopify page. Use when a user wants a new page designed visually before it is built.

# Visual Page Builder

Use this workflow for new page generation when the user wants a visual layout
before source HTML is written. It orchestrates `plan-page`, `asset-prep`, and
`generate`; do not duplicate their detailed rules.

Read `storefront-engine/references/visual-layout-workflow.md` before starting.

## Inputs

Accept any combination of:

- a plain-language brief, target audience, traffic source, or conversion goal
- a product or collection
- a brand direction or existing design assets
- an ad creative, screenshot, or reference URL

Route inputs before creating a layout:

| Input | First action |
|---|---|
| Reference URL or screenshot | Load `browser-analyze` or `analyze-page` |
| Ad creative | `lexsis_campaigns.analyze`, then `lexsis_campaigns.match_persona` |
| Product or collection | `lexsis_catalog` action `list` and use real Shopify imagery |
| Brief only | Run the embedded `plan-page` assessment |
| Existing page edit | Use the edit flow, not this skill |

Never reuse competitor copy, logos, product images, or brand marks. Reference
inputs are for composition, hierarchy, and interaction patterns only.

## Phase 1: Draft Plan and Layout

1. Gather the minimum missing requirements with the `plan-page` assessment.
2. Gather brand context through `lexsis_brand`, `lexsis_design`,
   `lexsis_catalog`, and `lexsis_asset_library`.
3. Create an internal `PLAN_DRAFT`: section order, conversion goal, visual
   rhythm, asset needs, and required islands.
4. Call `lexsis_workspace` action `credits` and `lexsis_assets` action
   `capabilities`.
5. Generate a layout reference with `lexsis_drafts` action `asset_generate`.
6. Call `lexsis_assets` action `view` to inspect it. Translate the concept into a layout brief:
   desktop composition, mobile stacking, section proportions, CTA positions,
   image placement, and island mapping.
7. Present the layout concept and the plan together. Wait for approval before
   producing final assets or page source.

Use only `lexsis_drafts` action `asset_generate` for layout-reference creation.
Do not assume a provider or model. Call `lexsis_assets` action `capabilities` when
the brief requires a specific quality, cost, reference-image, size, or output
format decision.

The concept prompt must say it is a storefront composition study, not a final
page. Use generic placeholder copy where text treatment matters. The concept
is not a production page image and must not be embedded in the final page.

## Approval Format

Present one decision point:

```text
Visual Page Plan: [page type]

Goal: [conversion goal]
Layout: [concept asset URL]
Sections: [ordered section list]
Visual rhythm: [composition, palette, spacing]
Commerce: [islands]
Production assets needed: [list]

Proceed to prepare final assets and create a draft preview?
```

## Phase 2: Build the Draft

After approval:

1. Hand the approved plan and layout brief to `asset-prep`.
2. Hand the final asset manifest, plan, and layout brief to `generate`.
3. `generate` compiles source-format HTML and creates a draft preview only.
4. Inspect desktop and mobile screenshots against the approved layout.
5. Fix material composition, overflow, asset, or island failures before
   returning the preview.

Never call `lexsis_live_ops` action `publish` unless the user separately
approves a live publish.

## Optional Follow-Up

After approval, this workflow may use `asset-prep` and `generate` to create a
draft. It may also end after returning the approved plan and layout brief when
the user wants to continue later.

---

## Reference Knowledge

---

# Storefront Craft Guide — Start Here

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

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
1. lexsis_discover({ query: "page creation" }) → authoritative action schemas
2. [Optional] lexsis_asset_library({ action: "search", args: {...} }) → find existing brand assets
3. [Optional] lexsis_drafts({ action: "asset_generate", args: {...} }) → get image URLs
4. Agent authors source-format HTML with `<lx-island>` components
5. lexsis_pages({ action: "compile", args: { source, head, theme_css, scripts } }) → compile + validation
6. lexsis_page_create({ action: "create", args: { source, head, theme_css, scripts, slug, publish: false } }) → persist as draft, returns preview URL
7. lexsis_live_ops({ action: "publish", args: { page_id } }) → go live (ONLY after the user explicitly approves)
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
- Only use valid island names (26 total — call `lexsis_design.islands` to see them)
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

1. **Always check `lexsis_asset_library` action `search` first** — brand's uploaded assets are free and on-brand
2. **Use `lexsis_catalog.list` for product images** — never generate fake product shots
3. **`lexsis_drafts` action `asset_generate` for custom imagery** — hero backgrounds, lifestyle contexts, textures
4. **`lexsis_drafts` action `asset_generate` with `reference_images` for composites** — product-on-background, texture overlays
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
1. lexsis_workspace → get/stores
2. lexsis_brand → brand_kit/lexsis_brand.list_themes/lexsis_brand.get_theme
3. lexsis_design → guide
4. [page-type routers] → catalog, navigation, campaigns, assets
5. Require a valid selected/default theme in the chosen workspace
7. Generate page (two-phase, SOURCE FORMAT — see source-format.md)
8. lexsis_pages → compile
9. lexsis_page_create → create draft
10. Host-agent visual verification
```

Steps 1-4 are ALWAYS run first. They establish context. Steps 5+ vary by skill.

> **Brand kit ↔ design.md precedence**: when the two disagree, **exact tokens (colors, fonts, radius, spacing values) come from the brand kit**; **style philosophy, component guidance, and explicit don'ts come from design.md**. Conflict on a token → use the kit's value, applied within design.md's don'ts. Don't stall trying to reconcile them.

> **Authoring format**: write pages in the HTML-native **source format** (`source-format.md`) — plain HTML sections delimited by `<!-- section: id -->`, islands as `<lx-island name>` with a JSON `<script>` child. The compiler produces VibePage JSON and does all escaping.

> **Templates**: search before drafting. Retrieve templates you intend to edit
> with `lexsis_design` action `get_section`. Each returned `source` is ready for
> editing and compiling. `format: "compiled_reference"` is renderer output and cannot be passed directly to
> source-authoring tools.

---

## Two-Phase Generation (Fast Iteration Pattern)

### Phase 4a — Draft Source HTML

Generate the FULL page as source-format HTML first:
- Plain HTML + Tailwind, sections delimited by `<!-- section: id -->`
- Focus on layout, visual hierarchy, spacing, typography
- Write all copy naturally — apostrophes/quotes need no escaping
- Set all colors via `--lx-*` CSS variables (from `lexsis_brand.compile_theme`)
- Mobile-first responsive; shared keyframes or `data-behavior="gsap-*"` presets for animation
- Islands go in directly as `<lx-island name="BuyBox">` with a JSON `<script>` child — use `lexsis_design` action `island_schema` for exact prop shapes

### Phase 4b — Compile & Fix

Run `lexsis_pages` action `compile`:
- Returns the compiled VibePage + compile issues + publish validation
- Fix reported issues in the source (unknown islands, bad props, missing hooks) and re-compile
- Require `missing_candidates` to be empty
- When clean, `lexsis_page_create` action `create` persists a draft; retrieve
  source later with `lexsis_pages` action `source`

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
- **Tailwind CSS** in HTML class attributes. The compiler emits one
  deterministic `compiled_page_css`; there is no runtime Tailwind CDN.
- **CSS Variables** (`--lx-*`) for all brand colors/fonts — set in `theme_css` (generate with `lexsis_brand.compile_theme`)
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

After `lexsis_page_create` returns a `preview_url`, always verify visually.
Use the calling agent's browser capability; Lexsis does not create a shared
Playwright session or browser pool.

Test 390px, 768px, and 1280px. Use screenshots when available. Otherwise use
computed styles, DOM bounds, scroll dimensions, image completeness, hover
state, and console inspection. If the host has no browser capability, return
the preview URL and state that visual QA remains.

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
<lx-island name="IslandName">
  <script type="application/json">{ "key": "value" }</script>
</lx-island>
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
- Product data → `lexsis_catalog` action `get` or `list`
- Navigation → `lexsis_brand` action `navigation`
- Reviews → configured in store (no manual data needed)
- Brand tokens → `lexsis_brand` action `brand_kit` or `lexsis_brand.get_theme`

---

## Deprecated Tools (DO NOT USE)

These tools appeared in older skill versions but are no longer available:

| Removed | Replacement |
|---------|-------------|
| `get_theme_json` | `lexsis_brand` action `brand_kit` (includes theme data) |
| `provision_store` | Handle via onboarding flow, not page generation |
| `extract_brand_design` / `capture_design_source` / `list_design_sources` | No replacement — no MCP tool for reference-URL design extraction currently exists |
| `lexsis_template_library.search_sections` returning `html`/`css`/`js` inline | Search is metadata-only now; call `lexsis_design.get_section({ ids })` for compile-ready source |

`lexsis_design.islands` and `lexsis_design.island_schema` remain active tools — use them for island discovery and schema lookups, alongside the `vibe://catalog/islands` resource.

---

## Quality Gates (Before Publishing)

1. `lexsis_pages` action `compile`
2. `lexsis_pages` action `integrity`
3. Host-agent visual verification

If compile fails, fix source and retry. If integrity warns, assess and fix.
If visual QA fails, use `lexsis_drafts` action `page_update_section` or
`page_patch`, then repeat QA.

---

# Source Format — HTML-Native Page Authoring (V2)

> **This is the preferred way to author pages.** Write plain HTML with
> `<lx-island>` elements; `lexsis_pages` action `compile` and
> `lexsis_page_create` action `create` compile it deterministically. Never
> hand-write `data-island` / `data-props` or escape HTML into JSON strings.

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
5. **External libraries** do not go in section HTML—pass them through `scripts`.
6. **`head`, `theme_css`, `scripts`** are structured tool arguments. Prefer
   `theme_css` from `lexsis_brand` action `lexsis_brand.get_theme`.
7. Tailwind classes compile into one `compiled_page_css` artifact. Fix every
   missing candidate; do not add Tailwind CDN or a separate generated sheet.

### Tool workflow

```
lexsis_brand → list_themes/get_theme → theme_css
draft source HTML (whole page)
lexsis_pages { action: "compile", args: { source, head, theme_css, scripts } }
fix any issues, then:
lexsis_page_create { action: "create", args: { source, head, theme_css, scripts, slug, publish: false } }
edits: lexsis_drafts → page_update_section or page_patch
round-trip: lexsis_pages → source/section_source → lexsis_drafts
```

`page_update_section` compiles one section and upserts it. `page_patch` batches
related localized changes into one version. Pass `expected_version`.

## Starting From a Template

Search the section library before writing a section from scratch. When you pick
a template, request editable source:

```text
lexsis_design({ action: "get_section", args: { ids: ["template-id"] } })
```

The response's `source` is one complete source-format section: a delimiter,
`<lx-island>` markup, and the template CSS/JS. Tailor it, then run
`lexsis_pages` action `compile`.

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
│  → PRODUCT FLOW (lexsis_catalog.list first → build around real product data)
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
├─ lexsis_campaigns.analyze({ image_urls, ad_format })  → visual signals, CTA, headline
├─ get_storefront_skills({ brief from ad analysis, page_type: "landing" })
└─ lexsis_catalog.list()

Phase 3: Assets
├─ Use ad creative images directly where appropriate
├─ lexsis_drafts.asset_generate for additional sections (testimonial bg, trust section bg)
└─ lexsis_drafts.asset_generate with reference_images to adapt ad images (crop, extend, composite)

Phase 4-4: Same as Standard Flow
```

---

## Design-First Flow (Reference URL)

```
Phase 2:
├─ Agent screenshots URL               → extracted palette, fonts, spacing, tone
├─ get_storefront_skills(brief)
└─ lexsis_catalog.list()

Phase 3: Use extracted tokens as theme_css base
Phase 4-4: Same as Standard Flow
```

---

## Edit Flow (Safe Iteration)

```
1. lexsis_pages.find({ query })                              → locate page by handle/title/UUID
2. lexsis_pages.edit_context({ page_id })                 → resolve store/workspace + current version
3. lexsis_pages.source({ page_id })                       → read round-trip source when available
4. lexsis_pages.inspect({ page_id })                 → inspect current compiled sections
5. Identify which sections to modify
6. lexsis_drafts.page_update_section({ page_id, source, expected_version }) → compile, preflight, commit
7. lexsis_pages.integrity({ page_id, archetype })       → structural QA pass
8. [Optional] lexsis_pages.diff({ page_id, version_a, version_b })  → review all changes
9. [If broken] lexsis_live_ops.rollback({ page_id, target_version })    → revert to prior version
```

**Key rules:**
- `lexsis_drafts.page_update_section` compiles and runs the full-page preflight before it writes
- Existing page writes derive store/workspace from `page_id`; omit redundant `store_id`
- A `version_conflict` means another write landed first; re-read and rebase
- Run `lexsis_pages.integrity` after all edits complete — catches archetype violations (e.g. PDP without BuyBox)
- Use `lexsis_pages.diff` to verify your changes look correct before publishing
- Use `lexsis_live_ops.rollback` if integrity check fails — creates a new forward version, preserves history

---

## Duplication Flow (Idempotent)

```
1. lexsis_pages.find({ query })                                     → locate source page
2. lexsis_drafts.page_duplicate({ page_id, handle, idempotency_key })     → safe clone (retries won't create extras)
3. Edit sections on the duplicate (use Edit Flow above)
4. lexsis_pages.integrity({ page_id, archetype })             → final QA
```

**Idempotency key:** Pass a deterministic string (e.g. `"${handle}-v2-from-${source_handle}"`) so that retrying the same operation returns the existing duplicate instead of creating another.

---

## Parallelization Rules

| Can parallelize | Cannot parallelize |
|---|---|
| All Phase 2 context calls | Phase 3 needs Phase 2 results (brand_colors for asset gen) |
| Multiple lexsis_drafts.asset_generate calls | validate must complete before write |
| Asset generation for different sections | Reference-based generation needs source image URLs first |

---

## Cost Control

- `lexsis_asset_library` action `search` before `lexsis_drafts` action `asset_generate` — existing assets are free
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

Always call `lexsis_workspace` with action `credits` before expensive
operations. If balance is 0, inform the user before proceeding.

| Tool | Cost | Notes |
|------|------|-------|
| `lexsis_drafts` → `asset_generate` | credits | AI image generation, editing, and compositing |
| `lexsis_page_create` → `create` | credits | Draft page generation |
| `lexsis_drafts` → `page_variation` | credits | A/B variant creation (requires Pro plan) |
| `lexsis_drafts` → `experiment_create` | credits | Experiment setup (requires Pro plan) |
| `lexsis_drafts` → `page_update_section` | credits | Section regeneration |
| `lexsis_pages` → `compile` | FREE | Always validate before creating or publishing |
| `lexsis_pages` → `integrity` | FREE | Structure/accessibility check |
| All read/list/get tools | FREE | No cost for browsing data |

**Preflight pattern:**
```
lexsis_workspace(credits) → check cost → warn if insufficient → proceed or abort
```

Source-format pages persisted through `lexsis_page_create` still cost credits
(the write action, not the compiler, bills). Draft previews also consume
credits.

---

# Conversion Psychology — Storefront Design Intelligence

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

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

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

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

Set `head.use_cart_v2: true` on every commerce page. The renderer injects the resolved published cart profile separately, so **never author a cart section in the page**. Use `lexsis_cart.get`, `lexsis_drafts.cart_set`, and `lexsis_drafts.cart_edit` for MCP cart work. Full composition guide: load the `cart-composition` reference.

```jsonc
{ "head": { "title": "...", "use_cart_v2": true } }   // that's the whole cart setup
```

Legacy note: `CartDrawer` (V1) exists only on old pages that predate cart profiles. Don't add it to new pages; when editing a legacy page, prefer migrating it (remove CartDrawer, set the flag).

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
- BundleBuilder → (bundle:add) → cart drawer (injected cart profile)
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
3. Packs compose with `lexsis_brand.compile_theme` output — they reference `--lx-*` variables, never hardcode colors.
4. Check the island's `schema.json` `parts` array before targeting a part name (`lexsis_design.island_schema`).

---

# Asset Pipeline — Multi-Source Visual Strategy

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

> **Inputs:** Approved page plan (from `/plan-page` workflow)
> **Outputs:** Asset manifest (URLs + purposes + section mapping)
> **When to load:** After page plan is approved, before HTML generation.

---

## Decision Tree

```
Need an image or video for a section?
│
├─ lexsis_asset_library({ action: "search", args: { query, workspace_id } })
│  → found good match?
│  ├─ YES → use it (free, on-brand)
│  └─ NO ↓
│
├─ Product shot needed?
│  ├─ YES → use real images from lexsis_catalog action list/get
│  └─ NO ↓
│
├─ What type of asset?
│  ├─ Static image (background, lifestyle, texture, composite)
│  │  └─ lexsis_drafts action asset_generate
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
└─ After sourcing → lexsis_asset_upload action import
```

---

## Built-In Tools (Lexsis AI MCP)

| Tool | What it does | Cost |
|------|-------------|------|
| `lexsis_asset_library` → `search` | Search workspace assets | Free |
| `lexsis_drafts` → `asset_generate` | Generate, composite, inpaint, or restyle | Credits |
| `lexsis_assets` → `view` | Verify an asset | Free |
| `lexsis_asset_upload` → `import` | Import URL, base64, attachments, or use upload picker | Free |

Always search first. Pass `workspace_id` explicitly when multiple workspaces
are available.

See `design-enrichment.md` for detailed prompt patterns, style selection guide, compositing recipes, and HTML placement patterns.

---

## External MCPs (Detected at Runtime)

These tools are available when the user has the corresponding MCP installed. Check availability before suggesting.

### Exa — Image Research & Reference

```
web_search_exa({ query: "skincare brand hero photography editorial style" })
```

Use for: mood boards, competitor visual research, finding reference imagery to brief `lexsis_drafts` action `asset_generate` more precisely, sourcing real lifestyle photos.

**Flow:** Exa search → find URL → `lexsis_asset_upload` action `import` → use
the returned permanent URL.

### HiggsField / Runway / Kling — Video Generation

Use when: TikTok traffic source, fashion/luxury vertical, product demo needed, brand has no existing video content.

**Flow:**
1. Generate video via external MCP (short clip, 3-8 seconds)
2. `lexsis_campaigns.frames` → pull best frame as thumbnail
3. Use video URL in HeroMedia island or `<video>` tag
4. Set click-to-play (NEVER autoplay — costs 7% CVR)

**Video placement patterns:**
- Hero: click-to-play with compelling thumbnail image
- Product demo: inline player after benefits section
- Social proof: UGC-style video carousel
- Background: muted loop, heavily dimmed (luxury only)

### OpenArt — Specialized AI Illustration

Use when: `lexsis_drafts(action: "asset_generate", args: style: "illustration")` doesn't provide enough control over style, need specific artistic direction, or brand has a custom illustration language.

### Unsplash / Pexels — Stock Photography

Use when: brand has no library assets, AI generation looks too synthetic, need real-world photography (locations, hands, diverse models).

---

## Feeding External Assets Into Pages

All external assets MUST be persisted before use:

```
1. Source asset via external MCP → get URL
2. lexsis_asset_upload({
     action: "import",
     args: { url, purpose: "hero_bg", tags: ["lifestyle", "summer"], workspace_id }
   })
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
- Check `lexsis_workspace` action `credits` before generation
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
<!-- Click-to-play video hero -->
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
- NEVER serve uncompressed video; use the imported CDN URL

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

1. `lexsis_asset_library` action `search` first
2. `lexsis_workspace` action `credits` before expensive operations
3. Prefer `quality: "medium"` — reserve `"high"` for hero only
4. External MCP assets → `lexsis_asset_upload` action `import`
5. CSS gradients/solid colors for sections that don't need imagery
6. Reuse: one hero image can serve as dimmed background for 2-3 sections

---

# Before Showing Draft to Merchant — QA Recipe

## Pre-flight Checklist

1. **Compile and validate source** — `lexsis_pages` action `compile`
2. **Save as draft** — `lexsis_page_create` action `create` with `publish:false`
3. **Check integrity** — `lexsis_pages` action `integrity`

## Browser QA (if available)

### Viewports to test:
- Mobile: 390px
- Tablet: 768px
- Desktop: 1280px

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
| 401 on publish | OAuth session expired or revoked | Reconnect the MCP and complete browser OAuth |
| Insufficient scope on publish | Connection has Read or Build access | Reauthorize with Publish access after user approval |
| Images too large/slow | Using original Shopify CDN URLs | Append `&width=800` to resize |

## Draft vs Live

- `publish: false` → draft at `/v/{slug}?shop={domain}&preview=1`
- `lexsis_page_create` is draft-only and rejects `publish:true`
- Publish later with `lexsis_live_ops` action `publish` after explicit approval
- Draft edits do not replace the public `published_version_id`

---

# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. `lexsis_pages` action `compile`
2. `lexsis_page_create` action `create` with `publish:false`
3. `lexsis_pages` action `integrity`
4. Host-agent browser QA at 390px, 768px, and 1280px
5. `lexsis_live_ops` action `publish` after explicit approval

## Operations

### Create Draft (New Page)
```
lexsis_pages({ action: "compile", args: { source, head, theme_css, scripts } })
lexsis_page_create({ action: "create", args: { source, head, theme_css, scripts, slug, publish: false } })
```
Returns: page_id, page_url, preview_url

### Preview (Draft)
```
lexsis_page_create({ action: "create", args: { source, head, theme_css, scripts, slug, publish: false } })
```
Returns: preview_url (not visible to store visitors)

### Publish Existing Page
```
lexsis_live_ops({ action: "publish", args: { page_id } })
```
Promotes the exact reviewed version to `published_version_id`.

### Unpublish
```
lexsis_live_ops({ action: "unpublish", args: { page_id } })
```
Takes page offline but preserves it in DB.

### Duplicate
```
lexsis_drafts({ action: "page_duplicate", args: { page_id, title: "New Title" } })
```
Creates a copy — useful for A/B test variants.

### Create Experiment Variant
```
lexsis_drafts({ action: "page_variation", args: { page_id, changes: {...} } })
```
Creates variant for A/B testing.

## Prerequisites

- Resolve a connected store with `lexsis_workspace` action `stores`
- Require a valid selected/default theme from `lexsis_brand`

Edits to a published page remain draft-only until publish succeeds. A failed
republish keeps the prior public version live.

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

Always search `lexsis_template_library.search_sections` before generating sections from scratch. It returns metadata only — fetch markup for the ids you pick with `lexsis_design.get_section`:

```
lexsis_template_library.search_sections({ query: "hero with video background for fashion", section: "hero", industry: "fashion", mood: "editorial" })
lexsis_design.get_section({ ids: ["<chosen id from results>"] })
```

- If a matching template is found (score > 0.7): USE IT. Its returned `source`
  contains the section markup, CSS, and JS ready to tailor with brand-specific
  copy/images, then pass to
  `lexsis_pages` action `compile`.
- If no match: generate from scratch in Phase 4.

Templates are conversion-proven, pixel-perfect, and faster than custom generation.
Use `format: "compiled_reference"` only to inspect renderer output; never paste its
`data-island` / `data-props` markup into source-authoring tools.

For a full page, check `lexsis_template_library.search_page_kits` before assembling sections one at a time — it returns curated multi-section groupings that already share one palette/vertical:

```
lexsis_template_library.search_page_kits({ query: "clinical supplements PDP", page_type: "pdp", industry: "supplements" })
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

1. `lexsis_pages` action `find`
2. `lexsis_pages` action `edit_context`
3. `lexsis_pages` actions `section_source`, `source`, or `inspect`
4. Edit exactly one source-format section
5. `lexsis_drafts` action `page_update_section` or `page_patch`
6. `lexsis_pages` actions `diff` and `integrity`

For existing pages, `page_id` is authoritative. Do not require the user to
reselect a workspace or pass `store_id`; an optional store ID is only an
assertion. Service-token store/workspace scopes remain authorization boundaries.

## Operations

### Update/Replace a Section

```
lexsis_drafts({
  action: "page_update_section",
  args: { page_id, section_id, source, expected_version }
})
```
- Replaces the compiled section from source-format HTML
- Auto-bumps page version
- Returns `version_conflict` if another edit landed first
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
lexsis_drafts({
  action: "page_update_section",
  args: { page_id, source, position, expected_version }
})
```
- Position: "before:{section_id}" or "after:{section_id}" or index number
- Must include full section HTML

### Remove a Section

```
lexsis_drafts({ action: "page_remove_section", args: { page_id, section_id, expected_version } })
```
- Creates a reversible new page version
- Auto-bumps version

### Reorder Sections

```
lexsis_drafts({ action: "page_move_section", args: { page_id, section_id, position, expected_version } })
```
- Position is 0-indexed
- All other sections shift accordingly

## Best Practices

- Always call `lexsis_pages` action `edit_context` before a write
- Re-read context/source and rebase when an edit returns `version_conflict`
- Reference section IDs from the page data (don't guess)
- After editing, run `diff` and `integrity`
- Batch related multi-section changes with `page_patch` so they create one version
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout

Minor edits use this workflow directly. They do not repeat the new-page planning
workflow; the existing page retains its approved plan.

For published pages, `current_version` can advance while the live renderer
remains pinned to `published_version_id`. Publish only after QA.

---

# Visual Layout Workflow

Use this reference with the `visual-page` skill. It converts mixed page inputs
into a visual concept, an approved page plan, and a valid source-format draft.

## Layout Concept Contract

The concept is an internal visual brief. It communicates:

- section order and relative heights
- hero composition and focal point
- grid, split, and card proportions
- image placement and treatment
- color temperature and whitespace rhythm
- CTA hierarchy and likely island placement
- desktop composition and mobile stacking intent

It does not provide final copy, production imagery, product facts, or valid
island props. Use brand data, Shopify product data, and the island schemas for
those.

## Generate the Layout Reference

Call `lexsis_drafts` action `asset_generate` to create the visual reference. The workflow is
provider-neutral: do not hardcode a provider or model here.

Call `lexsis_assets.capabilities` only when the request needs a deliberate
quality, cost, reference-image, size, output-format, or transparency choice.
Record the returned asset ID in the working brief, but do not use the layout
reference as final page media.

## Prompt Template

```text
Create a desktop ecommerce [PAGE TYPE] composition study for [AUDIENCE].

Goal: [CONVERSION GOAL].
Brand direction: [BRAND TONE, PALETTE, TYPOGRAPHY].
Section order: [SECTION PLAN].
Use [PRODUCT / EXISTING ASSET] only as visual reference.
Show clear hierarchy, whitespace, CTA placement, image zones, card/grid
proportions, and mobile-friendly stacking intent.
This is a layout concept, not a final website. Use generic placeholder copy;
do not reproduce competitor branding, logos, copy, or imagery.
```

Use `16:9`, `2K`, and PNG by default. Use reference images only when they are
tenant-owned assets, user-supplied assets, or safe visual references.

## Concept to Source Mapping

After `lexsis_assets.view`, write a concise layout brief before running `asset-prep`:

| Concept signal | Source-format implementation |
|---|---|
| Full-bleed hero | Semantic `<section>` with responsive image and overlay |
| Split hero | Grid that stacks below `lg` |
| Product purchase area | `BuyBox` with real product data |
| Repeated cards | CSS grid with stable media aspect ratios |
| Reviews / FAQs / tabs | Valid matching island with schema-derived props |
| Pinned conversion action | `StickyBar` only when the page type and product support it |

Do not copy pixels literally. Preserve visual intent while obeying the brand
kit, accessibility rules, content hierarchy, source format, and island
contracts.

## Approval and QA

Show the concept and plan in one approval response. After approval, compare the
draft preview at desktop and 375px mobile widths:

- hero headline and CTA are visible above the fold
- layouts stack without horizontal overflow
- real product data and final assets replaced placeholders
- no concept image is embedded in the page
- islands hydrate and page compilation has zero errors
- composition still matches the approved visual rhythm

---

# Optional Workflow Connections

Each skill owns one outcome and can run independently. The connections below
describe reusable outputs, not mandatory sequencing.

| Skill | Owns | Output | May inform |
|---|---|---|---|
| `storefront-engine` | Routing only | Selected workflow | One owner from this table |
| `browser-analyze` | Browser capture and raw evidence | `PAGE_ANALYSIS_INPUT` | `analyze-page`, `remix`, or `optimize` |
| `analyze-page` | Reference page structural analysis | `VISUAL_PAGE_INPUT` | `visual-page` |
| `remix` | Brand-safe reference/ad adaptation brief | `VISUAL_PAGE_INPUT` | `visual-page` |
| `plan-page` | Standalone approved content and section plan | `PAGE_PLAN` | `asset-prep` or `visual-page` |
| `visual-page` | New-page visual layout concept and single approval | approved plan + layout brief | `asset-prep` |
| `asset-prep` | Final production asset sourcing | `ASSET_MANIFEST` | `generate` |
| `generate` | Source-format page, compile, draft preview, visual QA | `DRAFT_READY` | `publish` |
| `publish` | Live release or lifecycle action | live status | `experiment` or `optimize` |
| `optimize` | Existing-page, performance-led improvements | validated page update | `publish` or `experiment` |
| `experiment` | Controlled variants and result evaluation | winner or learning | `optimize` |
| `cart` | Cart profile configuration | reviewed cart profile | `generate` only if page integration changes |
| `search-docs` | Documentation lookup | answer and selected workflow | matching owner |
| `extract-island` | Maintainer reusable island layout | contribution-ready layout | maintainer review |

## Connection Rules

1. Pass compact named artifacts, not a second copy of upstream instructions.
2. Preserve tenant-scoped asset and product identifiers.
3. A layout concept is composition guidance only, never final page media.
4. A `DRAFT_READY` page is not live. Only `publish` can release it after
   explicit user approval.
5. Stop after the requested outcome. Follow a connection only when the user
   asks for the downstream outcome.
