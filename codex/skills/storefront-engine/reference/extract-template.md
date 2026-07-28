---
name: extract-template
description: Analyze any webpage URL, identify each visual section, and create pixel-perfect template JSONs for the section library. Maps page regions to island components and generates ready-to-render section templates.
trigger: extract template, analyze this page for templates, create template from, templatize this page, extract sections from
---

# Extract Template from URL

Analyze a live webpage and decompose it into reusable section templates for the Lexsis storefront template library.

## Prerequisites

- Playwright MCP must be available (for page loading and screenshots)
- Island schemas at `storefront-skills/reference/islands/` (for component mapping)
- Template registry at `services/storefront-renderer/public/templates/registry.json`

## Workflow

### Phase 1: Page Load & Analysis

1. Navigate to the target URL using Playwright (`browser_navigate`)
2. Take a full-page screenshot for visual reference (`browser_take_screenshot`)
3. Get page snapshot to understand DOM structure (`browser_snapshot`)
4. Identify distinct visual sections by looking for:
   - `<section>`, `<header>`, `<footer>` elements
   - Major background color/image transitions
   - Full-width containers with significant vertical padding
   - Semantic groupings (hero, product details, reviews, FAQ, etc.)

### Phase 2: Section Classification

For each identified section, determine:
- **Type**: hero | buy-box | social-proof | trust | reviews | faq | product-info | interactive | navigation | countdown | footer | announcement
- **Islands needed**: Which islands from the registry can render this pattern
- **Content**: Extract actual text, images, prices, product data from the section
- **Layout**: Grid structure, alignment, responsive hints

Reference island schemas at `storefront-skills/reference/islands/{name}/schema.json` to understand what each island supports.

### Phase 3: Template Generation

For each section, generate a template JSON following this schema:

```json
{
  "id": "{section-type}-{descriptor}-{source-brand}",
  "name": "Human-Readable Name",
  "description": "One-line description of what this section does",
  "industries": ["beauty", "supplements"],
  "section": "hero",
  "useCase": "trust-driven",
  "mood": "clinical",
  "tags": ["relevant", "tags"],
  "thumbnail": "/templates/thumbs/{id}.png",
  "islands_used": ["ProductHero", "BuyBox"],
  "props_used": { "ProductHero": { "layout": "splitLeft" } },
  "theme": {
    "palette": { "bg": "#...", "accent": "#...", "text": "#...", "surface": "#...", "border": "#..." },
    "fonts": { "display": "Font Name", "body": "Font Name" }
  },
  "section": {
    "id": "section-id",
    "html": "<section ...>full HTML with data-island and data-props attributes</section>",
    "css": "",
    "js": ""
  }
}
```

### Phase 4: HTML Construction Rules

When building the section HTML:
1. Use Tailwind CSS classes for layout and spacing
2. Use `--lx-*` CSS custom properties for colors/fonts (not hardcoded colors)
3. Include `data-island="IslandName"` and `data-props='...'` for interactive components
4. Hardcode all content (text, images, prices) — no template variables
5. Keep images as their original URLs from the source page
6. Match the visual layout as closely as possible (pixel-perfect intent)

### Phase 5: File Output

1. Write each template JSON to `services/storefront-renderer/public/templates/sections/{section-type}/{id}.json`
2. Update `services/storefront-renderer/public/templates/registry.json` — add new entries to the `templates` array
3. If any section pattern can't be represented by existing islands, log to `services/storefront-renderer/ISLAND_GAPS.md`

### Phase 6: Report

Output a summary table:
| # | Section | Type | Islands | Status |
|---|---------|------|---------|--------|
| 1 | Hero banner | hero | ProductHero | ✓ Created |
| 2 | Reviews grid | reviews | ReviewCarousel | ✓ Created |
| 3 | Custom 3D viewer | interactive | — | ⚠ Gap logged |

## Industry Detection

Detect the industry from the page content/products:
- beauty/skincare: serums, creams, ingredients lists, before/after
- fashion: clothing, sizes, lookbook imagery
- supplements: capsules, dosage, clinical claims, certifications
- food: recipes, nutrition facts, flavors
- home: furniture, room scenes, dimensions
- tech: specs, comparison tables, compatibility

## Tips

- Focus on SECTIONS, not individual components — a section is a full-width block
- Each section should be self-contained (renderable on its own)
- Prefer islands over raw HTML where the pattern matches
- If a section is purely decorative (no interaction needed), use static HTML only (islands_used: [])
- Extract actual brand colors from the page for the theme palette
