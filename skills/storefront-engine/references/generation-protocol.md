# Generation Protocol — How Pages Are Built

> This is the canonical reference for how AI agents generate storefront pages using the Lexsis AI MCP. All operational skills reference this protocol.

> **Compiled runtime reference:** any `data-island` or `data-props` snippets in
> storage-format examples below are renderer output, not page source. New pages
> use `<lx-island>` with a JSON script child as defined in `source-format.md`.

---

## MCP Workflow (Correct Order)

```
1. Read the selected store/theme from `work/storefront/setup/setup.json`
2. Read its saved brand design and exact theme CSS
3. Read current products, variants, assets, permissions, and island schemas
4. Require a valid page plan and a completed design asset decision, or record
   explicit skips
5. Promote the approved canonical source with final production assets
6. lexsis_pages → compile
7. lexsis_page_create → create draft
8. Host-agent responsive and commerce verification
```

Setup provides slow-changing design context. Commerce, assets, schemas,
permissions, analytics, and remote versions are always read live.

> **Brand kit ↔ design.md precedence**: exact tokens normally come from the
> saved theme, while design.md supplies style philosophy and component guidance.
> Before authoring, compare any explicit `NEVER`, `must`, or `non-negotiable`
> design rule with the matching token. If they directly contradict each other,
> return `THEME_CONTEXT_CONFLICT` with both values and stop using that property
> until the theme or guide is corrected. Never silently choose a
> property-by-property winner or invent a blended rule.

> **Documentation precedence**: live MCP contracts win over bundled docs. For
> islands, use `vibe://schema/island/{name}` (or `lexsis_design` action
> `island_schema`) first, bundled
> `references/islands/{slug}/schema.json` second, and prose/layout examples
> last. Never merge prop shapes from different versions.

> **Authoring format**: write pages in the HTML-native **source format** (`source-format.md`) — plain HTML sections delimited by `<!-- section: id -->`, islands as `<lx-island name>` with a JSON `<script>` child. The compiler produces VibePage JSON and does all escaping.

> **Local source**: follow `source-artifact-workflow.md`.
> `lexsis-source.html` is the canonical editable visual and production
> artifact. It is dry-run compiled into an interactive local preview during
> `/design-page`, then promoted unchanged by `/generate`.

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
- Compiled visual source runs in the reusable local island preview shell
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
- Reviews → configured review source or public reviews endpoint; never invent
  reviewers, ratings, locations, or counts
- Brand tokens → `lexsis_brand` action `brand_kit` or `lexsis_brand.get_theme`

### Locale and Market Rules

- Derive currency, tax language, shipping promises, and payment methods from
  the selected store. Do not default every page to USD or to India.
- For India storefronts, format INR with `₹`, use pincode-aware delivery
  language, and mention GST, COD, or UPI only when store data confirms them.
- Localize names, units, dates, and cities without fabricating regional proof.

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
If visual QA fails, update local source, compile the complete page, patch only
changed sections with `expected_version`, update the manifest, then repeat QA.
