# Design Assets & Brand Management

Manage visual assets (search, generate, edit) and brand identity (kit, themes).

## Asset Pipeline (Priority Order)

Always follow this order — never generate when existing assets work:

### 1. Ask, then browse or search
```
lexsis_asset_library(action: "search", args: { query: "", mode: "tags", theme_id: "<theme uuid>", limit: 48 })   // browse; opens the asset picker in UI hosts
lexsis_asset_library(action: "search", args: { query: "lifestyle woman skincare", theme_id: "<theme uuid>" })   // search when the user declines to pick
```
Returns existing brand assets (product shots, lifestyle, textures, SVGs).
`theme_id` is required. In UI hosts the picker multi-selects across pages and
returns a `Design asset selection:` message with `asset_ids` and
`selection_order`; wait for it before picking yourself. Tag browsing uses the
vision vocabulary: `banner`, `lifestyle`, `social-proof`, `logo`,
`product-shot`, `hero`, `flat-lay`, `before-after`.

### 2. Generate If Needed
```
lexsis_drafts(action: "asset_generate", args: {
  prompt: "Minimalist skincare flatlay on marble surface, soft morning light",
  style: "photography",        // photography | illustration | 3d_render | editorial | abstract
  purpose: "hero_bg",          // hero_bg | product_lifestyle | texture_fill | decorative_element | section_bg | card_bg | pattern_tile | product_composite
  aspect: "landscape",         // landscape | portrait | square
  quality: "medium",           // low | medium | high
  brand_colors: ["#1a1a1a", "#f5f5dc"]
})
```

### 3. Composite With References
```
lexsis_drafts(action: "asset_generate", args: {
  reference_images: ["https://cdn.example.com/asset_123.png", "https://cdn.example.com/asset_456.png"],
  prompt: "Place product bottle on the lifestyle background, natural lighting match",
  style: "photography",
  purpose: "product_composite"
})
```

### 4. Verify
```
lexsis_assets.view(asset_id)
```
Visual verification before using in page.

## Style Selection Guide

| Brand Tone | Style |
|-----------|-------|
| Luxury/Premium | `photography` or `editorial` |
| Playful/Fun | `illustration` or `3d_render` |
| Tech/Modern | `abstract` or `3d_render` |
| Natural/Organic | `photography` |
| Artistic/Creative | `editorial` or `illustration` |

## Purpose → Aspect Ratio

| Purpose | Aspect | Typical Use |
|---------|--------|-------------|
| hero_bg | landscape | Full-width hero backgrounds |
| product_lifestyle | portrait/square | Product in context |
| card_bg | square | Grid cards, thumbnails |
| section_bg | landscape | Section backgrounds |
| icon | square | Small decorative elements |
| texture | square | Repeating patterns, overlays |

## Brand Kit Management

### Read Brand Identity
```
lexsis_brand(action: "brand_kit", args: {})
```
Returns: logo, fonts (heading/body), colors (primary/secondary/accent), border radius, spacing scale, brand voice.

### List Available Themes
```
lexsis_brand.list_themes()
```
Returns: theme IDs, names, which is default.

### Update Theme
```
lexsis_drafts.theme_update(theme_id, {
  fonts: { heading: "Inter", body: "Inter" },
  colors: { primary: "#000", accent: "#ff6b00" },
  border_radius: "8px"
})
```

## Design References

To extract design tokens from a reference URL, the agent should screenshot the site and analyze the visual design (palette, fonts, spacing, tone) directly.

## Cost Control

- `low` quality: fast, cheap — use for textures, backgrounds, placeholders
- `medium` quality: default — use for most section images
- `high` quality: expensive — use only for hero images and key product shots
- Budget: ~3-5 generated assets per page maximum
- Always `lexsis_asset_library` action `search` first to avoid unnecessary generation
