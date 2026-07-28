# Asset Pipeline — Multi-Source Visual Strategy

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
| `import_asset` | Bring an external URL into the design library for reuse | Free |

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
