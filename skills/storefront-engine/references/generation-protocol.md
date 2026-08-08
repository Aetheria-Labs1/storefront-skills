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
6. compile_theme              → WCAG-checked --lx-* theme_css from brand colors
7. Generate page (two-phase, SOURCE FORMAT — see source-format.md)
8. compile_page_source        → dry-run compile + validation issues
9. create_page_from_source    → persists page, returns preview_url
10. Visual verification       → screenshot and verify
```

Steps 1-4 are ALWAYS run first. They establish context. Steps 5+ vary by skill.

> **Brand kit ↔ design.md precedence**: when the two disagree, **exact tokens (colors, fonts, radius, spacing values) come from the brand kit**; **style philosophy, component guidance, and explicit don'ts come from design.md**. Conflict on a token → use the kit's value, applied within design.md's don'ts. Don't stall trying to reconcile them.

> **Authoring format**: write pages in the HTML-native **source format** (`source-format.md`) — plain HTML sections delimited by `<!-- section: id -->`, islands as `<lx-island name>` with a JSON `<script>` child. The compiler produces VibePage JSON and does all escaping.

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
| `search_section_templates` returning `html`/`css`/`js` inline | Search is metadata-only now; call `get_section_template({ ids })` for markup |

`get_island_catalog` and `get_island_schema` remain active tools — use them for island discovery and schema lookups, alongside the `vibe://catalog/islands` resource.

---

## Quality Gates (Before Publishing)

1. **compile_page_source** — compile and validate source before creating a page
2. **check_page_integrity** — archetype-specific rules (recommended)
3. **Visual verification** — browser screenshot (required for final delivery)

If `compile_page_source` fails → fix source errors → re-compile.
If `check_page_integrity` warns → assess if acceptable → proceed or fix.
If visual check fails → `update_section_from_source` → re-screenshot.
