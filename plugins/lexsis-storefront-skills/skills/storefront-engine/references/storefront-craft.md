# Storefront Craft Guide — Start Here

> House rules in `storefront-engine/references/design-rules.md` override every example below.
> Examples show structure and copy intent; their styling (gradients, hover transforms,
> uppercase labels, pills, emoji, section fills) is illustrative and must not be copied.
> Where an example conflicts with a house rule, the rule wins.

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

Load this skill first on any storefront page generation task.

---

## Architecture: Vibe-Code

Pages are **source-format HTML + compiled Tailwind CSS + CSS custom properties
+ React islands**. No component JSON. The AI generates readable HTML directly
and Lexsis compiles it.

**Authoring source:**
```html
<!-- section: hero -->
<section id="hero">
  <lx-island name="BuyBox">
    <script type="application/json">
      {
        "product": {
          "title": "Product name",
          "variants": []
        }
      }
    </script>
  </lx-island>
</section>
```

The compiler produces VibePage storage JSON and hydrated `data-island`
markers. Do not write that compiled representation by hand.

---

## Skills Map

| Skill | Purpose | Load when... |
|---|---|---|
| `craft-guide` | This file — architecture, flow, quality bar | Always first |
| `workflow-orchestration` | Tool sequencing, parallelization, flow selection | Always — load after craft-guide |
| `conversion-psychology` | Universal persuasion: pricing, urgency, trust, CTA psychology | Always — load for any ecommerce page |
| `animation-system` | CSS animations, scroll-reveal, headline effects | Only when the plan names one motion moment |
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
| `--lx-bg-surface` | Card background (never a section background) |
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
- Zero emoji, one page background, one icon set, one bold moment
- Trust signals near purchase points
- Sticky add-to-cart on PDP

**Mediocre page:**
- Hardcoded colors instead of CSS vars
- Desktop-only layout
- Missing islands (raw HTML buttons instead of BuyBox)
- placeholder.co images shipped to production
- Emoji as icons, alternating section fills, mixed icon sets, scattered motion
- Trust badges missing

---

## Anti-Patterns (NEVER do these)

1. **No `fetch()` or XHR in section JS** — blocked by hydrator security
2. **No `eval()`, `localStorage`, `WebSocket`** — blocked
3. **No `@import` in section CSS** — blocked
4. **No external `url()` in CSS** — only inline colors via `--lx-*` tokens
5. **No duplicate section IDs** — each must be unique kebab-case
6. **No `<script src="...">` in HTML** — use section `js` field for vanilla JS
7. **No framework code** — no React/Vue/Angular in section HTML (islands handle interactivity)
8. **Don't fake commerce** — always use BuyBox island for add-to-cart, never a plain button

---

## Section ID Naming

Use descriptive kebab-case: `hero`, `product-gallery`, `social-proof`, `ingredients`, `faq`, `sticky-cta`, `trust-badges`, `footer`. Never `section-1`, `section-2`.

---

## Island Rules

- Author props in the `<lx-island>` JSON script child; the compiler writes
  `data-props`
- Use the live island catalogue and exact selected schema; do not rely on a
  fixed island count
- Follow lifecycle replacement guidance for deprecated or superseded islands
- One `BuyBox` per page (multiple breaks cart state)
- Cart: `head.use_cart_v2: true` on every commerce page (`CartDrawer` V1 deprecated — never author a cart section)
- `StickyBar` needs `triggerOffset` — distance in px before it appears
- `ReviewCarousel` can use custom reviews array OR fetch from Shopify via productId

---

## Tailwind Usage

- Lexsis compiles referenced utilities into one immutable page CSS artifact;
  there is no runtime Tailwind CDN
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
