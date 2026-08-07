# Generation Protocol — How Pages Are Built

> This is the canonical reference for how AI agents generate storefront pages using the Lexsis AI MCP. All operational skills reference this protocol.

---

## MCP Workflow (Correct Order)

```
1. get_workspace_details      → workspace ID, plan tier
2. get_connected_stores       → store domain, Shopify data
3. get_brand_kit              → logo, fonts, colors, voice, border radius
4. get_design_md              → brand brief, design philosophy, don'ts
5. [page-type specific tools] → products, navigation, ad creatives, etc.
6. Generate page (two-phase)
7. validate_vibe_page         → structural/safety check
8. publish_vibe_page          → returns preview_url
9. Visual verification        → screenshot and verify
```

Steps 1-4 are ALWAYS run first. They establish context. Steps 5+ vary by skill.

---

## Two-Phase Generation (Fast Iteration Pattern)

### Phase 4a — Raw HTML + Tailwind (No Islands)

Generate the FULL page as plain HTML + Tailwind CSS first:
- Focus on layout, visual hierarchy, spacing, typography
- Use placeholder `<div>` elements where islands will go (mark with `data-placeholder="BuyBox"`)
- Write all copy, set all colors via `--lx-*` CSS variables
- Ensure mobile-first responsive design
- Apply shared keyframes for animations (fadeUp, fadeIn, scaleIn, etc.)

This phase is fast to iterate on — pure HTML renders instantly.

### Phase 4b — Island Mapping

Replace placeholder divs with actual island markers:
```html
<!-- Phase 4a placeholder -->
<div data-placeholder="BuyBox" class="...">Buy button goes here</div>

<!-- Phase 4b final -->
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
```

Use `get_island_schema({island_name})` resource (`vibe://schema/island/{name}`) to get exact prop shapes.

### Why Two-Phase?
- HTML renders in any browser preview — fast visual feedback
- Island hydration requires the renderer — slower feedback loop
- Separates design decisions from data-wiring decisions
- Easier to iterate on layout without breaking island props

---

## VibePage JSON Structure

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
- **CSS Variables** (`--lx-*`) for all brand colors/fonts — set in `theme_css`
- **Islands** via `data-island="Name"` + `data-props='JSON'` attributes
- **Section IDs** must be unique, kebab-case: "hero", "social-proof", "faq"
- **Section JS** is sandboxed — no fetch/XHR/eval/localStorage. Only DOM manipulation + IntersectionObserver
- **Shared keyframes** already loaded: fadeUp, fadeIn, scaleIn, slideInLeft, slideInRight, marquee, float, shimmer, wordFade, pulseRing
- **No @import, no external URLs in CSS**, no inline `<style>` or `<script>` tags in HTML

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

After `publish_vibe_page` returns a `preview_url`, ALWAYS verify visually.

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
4. If issues found → update_page_section to fix → re-verify
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
| `search_section_templates` returning `html`/`css`/`js` inline | Search is metadata-only now; call `get_section_template({ ids })` for markup |

`get_island_catalog` and `get_island_schema` remain active tools — use them for island discovery and schema lookups, alongside the `vibe://catalog/islands` resource.

---

## Quality Gates (Before Publishing)

1. **validate_vibe_page** — structural validation (required)
2. **check_page_integrity** — archetype-specific rules (recommended)
3. **Visual verification** — browser screenshot (required for final delivery)

If `validate_vibe_page` fails → fix errors → re-validate.
If `check_page_integrity` warns → assess if acceptable → proceed or fix.
If visual check fails → `update_page_section` → re-screenshot.
