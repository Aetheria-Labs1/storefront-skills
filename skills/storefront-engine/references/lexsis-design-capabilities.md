# Lexsis Page Design Capabilities

Use this contract when designing, preparing assets, generating, or
structurally optimizing a Lexsis page. `/plan-page` does not load island or
implementation guidance.

## Theme and Brand Context

Select exactly one saved store/theme pair for a page.

- Use the saved `brand-design.md` for voice, art direction, component guidance,
  and explicit design don'ts.
- Use `lexsis_brand` action `get_theme` for the current complete theme when a
  live refresh is required.
- Use `lexsis_brand` action `compile_theme` when theme CSS must be derived from
  brand inputs.
- Exact theme tokens win over prose when values conflict.
- Never combine design files or CSS from multiple themes on one page.

The theme compiler provides WCAG-checked `--lx-*` variables including:

- `--lx-accent-color`
- `--lx-accent-color-hover`
- `--lx-accent-soft`
- `--lx-bg-color`
- `--lx-bg-surface`
- `--lx-surface-alt`
- `--lx-text-color`
- `--lx-text-muted`
- `--lx-border-color`
- optional `--lx-font-heading`, `--lx-font-body`, and `--lx-radius`

Use tokens for brand colors, typography, surfaces, borders, and radii. Avoid
hard-coded brand values inside sections.

## Tailwind and CSS

Lexsis compiles page classes with Tailwind at compile time. There is no runtime
Tailwind CDN.

- Use Tailwind utilities for layout, spacing, sizing, and responsive behavior.
- Work mobile-first, then enhance with responsive prefixes.
- Missing Tailwind utilities are blocking compiler errors unless the class is
  explicitly defined in theme or section CSS.
- Use section CSS only for intentional, scoped components or behavior.
- Do not recreate the page layout as a second CSS system.

Compiled CSS order is:

1. theme CSS
2. generated Tailwind utilities
3. section CSS in page order

Section CSS can override earlier rules at equal specificity. Keep global
tokens and page-wide rules in theme CSS, and scope section overrides by
section ID.

The renderer already supplies its reset, base typography, smooth scrolling,
and shared keyframes:

`fadeUp`, `fadeIn`, `scaleIn`, `slideInLeft`, `slideInRight`, `marquee`,
`float`, `shimmer`, `wordFade`, and `pulseRing`.

## Template-First Composition

Before custom composition:

1. Discover `lexsis_template_library` actions `search_page_kits` and
   `search_sections`.
2. Search page kits using page type, archetype, objective, industry, and mood.
3. Treat a page kit as a coherent list of section-template IDs. There is no
   single page-kit instantiation action.
4. Fetch selected section source through `lexsis_design` action `get_section`,
   at most three IDs per call.
5. Adapt the returned source to the selected theme, plan, products, copy, and
   assets.

Template search returns metadata, not editable markup. `get_section` returns
authoring source with section delimiters, `<lx-island>` markup, and section
CSS/JS.

If the host renders an interactive template picker, wait for the user's
selection. Custom composition is allowed only after recording the evaluated
templates and why none fit.

## Islands

For every interactive element:

1. Discover `lexsis_design` actions `islands` and `island_schema`.
2. Use `islands` for selection guidance.
3. Resolve the exact selected schema.
4. Confirm lifecycle status is active.
5. Use the current required props and a supported native variant.
6. Style supported `data-part` hooks listed by the schema.
7. Use headless mode only when native variants cannot satisfy the approved
   design and every required hook is implemented.

Author islands as `<lx-island>` with one readable `application/json` child.
Never hand-author compiled `data-island` or `data-props` markup.

If the catalogue marks an island deprecated or superseded, follow its
replacement guidance. The replacement may be another island or supported
native HTML/CSS such as `<details>`; do not force a deprecated island into the
page.

Do not replace BuyBox or another commerce island with a custom button.

## Visual Preview

The design-stage source is compiled without saving. The local preview uses the
compiled markup and exported Lexsis island runtime.

- Use real compiled islands when schema-valid preview data exists.
- Shoppable video, galleries, accordions, and similar islands should run in
  the preview when their media and props are valid.
- A static fallback is permitted only for the affected island when it cannot
  compile or lacks safe preview data.
- Local interaction demonstrates presentation; hosted-draft QA certifies real
  product resolution, cart behavior, checkout-related behavior, and remote
  integrations.

Inspect 390px and 1280px during design. `/generate` adds 768px and hosted QA.

## Asset Roles

Template results do not expose a separate media-slot schema. Derive required
roles, aspect ratios, and crop guidance from the selected section source,
approved layout, and island schema.

Use live Shopify media for product identity. Visually verify creator and
product imagery. Temporary placeholders are visual-stage inputs only.

## Compact Manifest Evidence

Record the design decision:

```json
{
  "template": {
    "mode": "page-kit",
    "pageKitId": "kit-slug",
    "sectionTemplateIds": ["hero-slug", "buy-box-slug"]
  },
  "design": {
    "stylePack": "editorial",
    "compiledStyleManifest": null
  }
}
```

`template.mode` is `page-kit`, `sections`, or `custom`. Keep selection reasons
and evaluated alternatives in `page-plan.md`, not the manifest. After
compilation, store the returned style manifest under
`design.compiledStyleManifest`.

`stylePack` is the selected named pack, `custom` for an intentional scoped
treatment, or `existing-page` when adopting and preserving a remote page's
current design.
