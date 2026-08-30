# Reference PDP Remix — Competitor Deconstruction Workflow

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

> When to load: User provides a competitor/reference URL and wants to rebuild the same PDP structure for their brand.

---

## Phase 3: Capture

1. Screenshot the reference URL (or user provides screenshots)
2. Identify visual sections top-to-bottom — number each band
3. Extract design tokens: colors, fonts, spacing rhythm, border treatments
4. Note the overall aesthetic: editorial, clinical, playful, luxury, minimal

**Output:** Numbered section list with descriptions:
```
1. Split hero — product media left, buy panel right
2. Info cards row — 2 cards with bullet lists
3. Editorial product grid — 3 products + center bundle
4. Trust/certification badges
5. Footer with newsletter
```

---

## Phase 4: Decompose — Section → Island Mapping

Map each section to an island or HTML-only section:

| Reference Pattern | Lexsis Island | Notes |
|---|---|---|
| Split hero (media + buy panel) | `ProductHero` + `BuyBox` | Use `layout: "splitLeft"` or `"splitRight"` |
| Standard gallery + buy below | `ProductGallery` + `BuyBox` | Stacked layout |
| Related products grid | `EditorialProductGrid` | Use `featureCard` for bundle offers |
| Product carousel | `ProductCarousel` | Horizontal scrolling |
| Bundle builder | `BundleBuilder` | With discount badge |
| Info/detail cards | `PDPInfoCards` | Taste profile, pairs-with, etc. |
| Trust badges row | `TrustBadgeBar` | Icons + labels |
| Review section | `ReviewCarousel` | Star ratings + text |
| FAQ accordion | `FAQ` | Collapsible sections |
| Sticky add-to-cart | `StickyCart` | Appears on scroll |
| Newsletter footer | `Footer` | Use `layout: "editorialGrid"` with `newsletter` prop |
| Size guide modal | `SizeGuide` | Triggered by link |
| Variant swatches | `VariantSwatches` | Color/size selection |

**If no island matches:** Build as HTML-only section in the VibePage JSON. Document the gap.

---

## Phase 5: Adapt

For each mapped section:

1. **Swap brand tokens** — Replace competitor colors/fonts with user's brand kit
2. **Swap product data** — Replace competitor products with user's catalog
   - Call `lexsis_catalog.list` to get real product data (images, prices, handles)
3. **Swap copy tone** — Rewrite headlines/body in user's brand voice
   - Reference `lexsis_design.guide` for tone guidelines
4. **Swap imagery** — Replace competitor photos with user's assets
   - Call `lexsis_asset_library` action `search` first (prefer existing)
   - Call `lexsis_drafts` action `asset_generate` only if library has nothing suitable

---

## Phase 5: Build

Tool sequence:

```
┌─ lexsis_workspace.get      → workspace context
├─ lexsis_brand.brand_kit              → colors, fonts, logo
├─ lexsis_design.guide              → brand voice
├─ lexsis_catalog.list(limit: 10)   → product catalog
└─ lexsis_asset_library.search      → existing assets
     ↓
For each section needing custom imagery:
  ├─ lexsis_asset_library(action: "search", args: { query: "..." })
  └─ lexsis_drafts(action: "asset_generate", args: { ... })  ← costs credits
     ↓
Assemble source-format HTML:
  - sections delimited by `<!-- section: id -->`
  - `<lx-island>` elements for interactive components
  - `theme_css` passed as a structured tool argument
     ↓
lexsis_pages.compile            ← FREE
     ↓
lexsis_page_create(action: "create", args: { source, head, theme_css, scripts, slug, publish: false })  ← costs credits (preview first)
```

---

## Phase 5: QA — Visual Comparison

Checklist against reference:

- [ ] Same number of sections (or intentional omissions documented)
- [ ] Hero layout matches (split/stacked/fullHeight)
- [ ] Typography hierarchy preserved (heading sizes, weights)
- [ ] Spacing rhythm similar (section padding, element gaps)
- [ ] Color contrast maintained (dark-on-light or light-on-dark)
- [ ] Mobile stacking order makes sense
- [ ] All islands hydrate (no missing data-props)
- [ ] Product data is real (not placeholder)
- [ ] CTAs are actionable (not dead links)
- [ ] Images are brand-appropriate (not competitor's)

**Gap report format:**
```
## Gaps (reference features not yet supported)

| Section | Reference Has | Current Status | Workaround |
|---------|--------------|----------------|------------|
| Hero | 360° product spin | Not available | Use multi-image gallery with zoom transition |
| Footer | Animated newsletter | Static input | HTML-only animation in section js |
```

---

## Common Premium PDP Structures

### Luxury/Editorial PDP (6-8 sections)
```
├── ProductHero (splitLeft, fullHeight, floatingArrows)
├── BuyBox (expanded variant)
├── PDPInfoCards (2 cards: craftsmanship + materials)
├── HTML section: editorial brand story (full-bleed imagery)
├── ReviewCarousel (3-5 curated reviews)
├── EditorialProductGrid (related + bundle center card)
├── TrustBadgeBar (certifications)
└── Footer (editorialGrid + newsletter)
```

### DTC/Performance PDP (8-12 sections)
```
├── ProductGallery (horizontal, autoplay) + BuyBox (default)
├── TrustBadgeBar (shipping, returns, guarantee)
├── HTML section: benefits grid (icons + copy)
├── PDPInfoCards (ingredients/specs)
├── ReviewCarousel (high-count, star-first)
├── FAQ
├── ProductCarousel (related products)
├── BundleBuilder (frequently bought together)
├── StickyCart
└── Footer (newsletterSplit)
```

### Fashion/Apparel PDP (6-10 sections)
```
├── ProductHero (splitRight, thumbnailRail) + BuyBox + VariantSwatches
├── SizeGuide
├── HTML section: lookbook (full-bleed editorial images)
├── ReviewCarousel
├── ProductCarousel (complete the look)
├── EditorialProductGrid (styling suggestions)
└── Footer (columns)
```

---

## Credit Awareness

Before starting a remix build:
- Call `lexsis_workspace` action `credits` to check available credits
- `lexsis_drafts` action `asset_generate` and `lexsis_page_create` action `create` cost credits
- `lexsis_pages` action `compile` and all read tools are FREE
- If balance is 0: inform user, suggest using existing library assets only, or upgrading plan
