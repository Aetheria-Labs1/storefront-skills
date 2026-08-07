# Design Enrichment — AI Image Generation & Compositing

How to use `generate_asset`, `edit_asset`, and `view_asset` tools to create custom images for page sections. Load when a page needs custom imagery beyond what's in the design library.

---

## Decision Tree: Generate vs Reuse

```
Need an image for a section?
│
├─ search_design_library({ query: "hero lifestyle skincare" })
│  ├─ Found good match → USE IT (free, brand-consistent)
│  └─ No match or poor quality → GENERATE
│
├─ Product shot needed?
│  ├─ list_products() has product images → USE EXISTING
│  └─ Need product-on-background composite → edit_asset()
│
└─ Custom background/texture/lifestyle → generate_asset()
```

**Rule: Always `search_design_library` first.** Only generate when library has nothing suitable.

---

## Pipeline: Generate → Verify → Use

### Step 1: Generate Image (write your own descriptive prompt)

```
generate_asset({
  prompt: "soft editorial product photography, dewy botanicals with morning light, cream linen backdrop, green and white accent tones, shallow depth of field, natural diffused lighting, 4K commercial quality",
  style: "photography",
  purpose: "hero_bg",
  aspect: "landscape",
  quality: "high",
  brand_colors: ["#2D5016", "#FEFDFB", "#F5F0EB"],
  brand_tone: "clinical yet warm"
})
→ Returns { asset_id, url, width, height }
```

### Step 2: Verify (optional — use view_asset to visually inspect)

```
view_asset(asset_id) → base64 image you can see directly
```

### Step 3: Use URL in HTML

```html
<section class="relative min-h-[70vh]">
  <img src="THE_RETURNED_URL" alt="Hero background" class="absolute inset-0 w-full h-full object-cover" />
  <div class="relative z-10 ...">Content on top</div>
</section>
```

---

## Style Selection Guide

| Brand Tone | `style` param | Notes |
|---|---|---|
| Luxury/Premium | `photography` or `editorial` | High-end studio quality, dramatic lighting |
| Playful/Bold | `illustration` or `3d_render` | Vibrant, stylized, fun |
| Clinical/Minimal | `photography` | Clean, white backgrounds, precise |
| Earthy/Organic | `photography` or `lifestyle` | Natural light, textures, warmth |
| Tech/Modern | `3d_render` or `abstract` | Geometric, gradients, futuristic |
| Fashion | `editorial` | Editorial spreads, high contrast |

---

## Purpose Mapping

| Section Type | `purpose` param | `aspect` | Notes |
|---|---|---|---|
| Hero full-width | `hero_bg` | `landscape` | Wide, dramatic |
| Hero split (image half) | `product_lifestyle` | `portrait` or `square` | Product in context |
| Section background | `section_bg` | `landscape` | Subtle, not distracting |
| Product on background | `product_composite` | `square` | Use edit_asset |
| Card/feature image | `card_bg` | `square` | Small, tight crop |
| Texture/pattern | `texture_fill` | `square` | Tileable, subtle |
| Floating decoration | `decorative_element` | `square` | Transparent PNG |
| Flat lay composition | `product_lifestyle` | `landscape` | Multiple items arranged |

---

## Compositing with edit_asset

### Product on Lifestyle Background

```
// First: generate a background
generate_asset({
  prompt: "Marble countertop with soft morning light, botanical shadows",
  style: "photography",
  purpose: "product_composite",
  aspect: "square"
})
→ bg_url

// Then: composite product onto it
edit_asset({
  source_images: [product_image_url, bg_url],
  prompt: "Place the product bottle centered on the marble surface, natural shadows, studio lighting",
  aspect: "square",
  quality: "high"
})
→ final composited image
```

### Transparent PNG Overlays

```
generate_asset({
  prompt: "Abstract botanical leaf shapes, minimal line art",
  style: "illustration",
  purpose: "decorative_element",
  transparent: true,
  brand_colors: ["#2D5016"]
})
```

Use as decorative overlay:
```html
<img src="TRANSPARENT_URL" class="absolute top-0 right-0 w-32 opacity-20 pointer-events-none" />
```

### Texture Overlay

```
generate_asset({
  prompt: "Subtle paper grain texture, off-white, organic feel",
  style: "texture",
  purpose: "texture_fill",
  aspect: "square",
  quality: "low"
})
```

Use as background:
```html
<section style="background-image: url('TEXTURE_URL'); background-size: 300px; background-repeat: repeat;">
```

Wait — **no external URLs in CSS `url()`**. Use inline style on an element instead:

```html
<div class="absolute inset-0 opacity-5" style="background-image: url('TEXTURE_URL'); background-size: 300px; background-repeat: repeat;"></div>
```

---

## Placing Images in HTML

### Hero Background

```html
<section class="relative min-h-[70vh] flex items-center overflow-hidden">
  <img src="URL" alt="" class="absolute inset-0 w-full h-full object-cover" aria-hidden="true" />
  <div class="absolute inset-0 bg-gradient-to-r from-black/60 to-transparent"></div>
  <div class="relative z-10 max-w-7xl mx-auto px-6">
    <h1 class="text-white text-5xl font-bold">...</h1>
  </div>
</section>
```

### Product Image (contained)

```html
<div class="aspect-square rounded-2xl overflow-hidden" style="background:var(--lx-bg-surface)">
  <img src="URL" alt="Product Name" class="w-full h-full object-contain p-8" />
</div>
```

### Card with Image

```html
<div class="rounded-xl overflow-hidden shadow-sm border" style="border-color:var(--lx-border-color)">
  <img src="URL" alt="..." class="w-full aspect-[4/3] object-cover" />
  <div class="p-5">
    <h3 class="font-semibold">Card Title</h3>
  </div>
</div>
```

### Background with Overlay

```html
<section class="relative py-20">
  <img src="URL" alt="" class="absolute inset-0 w-full h-full object-cover opacity-20" aria-hidden="true" />
  <div class="relative z-10 max-w-4xl mx-auto text-center px-6">
    Content on top of subtle background
  </div>
</section>
```

---

## Cost Control

| Quality | Cost | Use for |
|---|---|---|
| `low` | Cheap | Textures, patterns, decorative elements |
| `medium` | Moderate | Card images, section backgrounds, secondary visuals |
| `high` | Expensive | Hero images, primary product shots, key visuals |

**Budget per page type:**
- PDP: 1 high (hero) + 1-2 medium (lifestyle) = 2-3 assets
- Landing: 1 high (hero) + 2-3 medium (section bgs) = 3-4 assets
- Homepage: 1 high (hero) + 1 medium (brand story) = 2 assets
- Collection: 0-1 medium (header) — products have their own images

---

## Common Prompt Patterns

### Hero Backgrounds
- "Soft gradient background with subtle botanical shadows, [brand_color] tones, editorial feel"
- "Abstract geometric shapes with smooth gradient, modern minimal, [brand_colors]"
- "Lifestyle flat lay with [product_category] items, overhead shot, clean styling"

### Section Backgrounds
- "Subtle watercolor wash, [brand_color] tint, very light opacity"
- "Clean linen texture, off-white, natural fiber detail"
- "Soft bokeh light circles on dark background"

### Product Composites
- "Product on [surface], natural window light, soft shadows"
- "Hands holding product, [skin_tone], clean background"
- "Product arranged with [complementary items], editorial styling"

### Decorative Elements
- "Minimal line art [motif], single stroke, [brand_color]"
- "Abstract blob shape, organic form, [brand_color], transparent background"
- "Small icon illustration of [concept], flat design, [brand_color]"

---

## Anti-Patterns

1. **Don't generate when library has it** — waste of cost and time
2. **Don't use `url()` in section CSS** — blocked by validator. Use `<img>` or inline `style` attribute
3. **Don't generate product shots** — always use real product images from `list_products`
4. **Don't over-generate** — 2-4 assets per page max. Use CSS gradients/colors for the rest
5. **Don't use `quality: "high"` for everything** — reserve for hero/primary images only
6. **Don't forget alt text** — decorative images get `alt="" aria-hidden="true"`, meaningful ones get descriptive alt

---

## Beyond Built-In Tools

For video generation, reference imagery research, stock photography, or specialized AI illustration via external MCPs (Exa, HiggsField, OpenArt, etc.), see `asset-pipeline.md`.
