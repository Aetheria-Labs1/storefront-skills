# Source Format — HTML-Native Page Authoring (V2)

> House rules in `storefront-engine/references/design-rules.md` override every example below.
> Examples show structure and copy intent; their styling (gradients, hover transforms,
> uppercase labels, pills, emoji, section fills) is illustrative and must not be copied.
> Where an example conflicts with a house rule, the rule wins.

> **This is the preferred way to author pages.** Write plain HTML with
> `<lx-island>` elements; `lexsis_pages` action `compile` and
> `lexsis_page_create` action `create` compile it deterministically. Never
> hand-write `data-island` / `data-props` or escape HTML into JSON strings.

For durable page work, store this format in `lexsis-source.html` and follow
`source-artifact-workflow.md`. The design workflow authors that same file,
dry-run compiles it with `page-theme.css`, and hydrates the compiled result
through the exported island preview runtime.

## Why this format exists

The old path (VibePage JSON with HTML in strings and JSON inside `data-props='...'` attributes) forced triple escaping and caused the top agent failure classes: entity-escaped markup rendering as literal text, apostrophes in copy breaking props, giant-blob page updates. In source format those failures are impossible by construction.

## The format

```html
<!-- section: hero -->
<section class="py-12 md:py-16 lg:py-20" style="background-color: var(--lx-bg-color)">
  <h1 class="text-4xl md:text-5xl font-bold" style="font-family: var(--lx-font-heading)">
    Don't miss the "Summer Drop"
  </h1>

  <lx-island name="CountdownTimer" hydrate="visible">
    <script type="application/json">
      { "endDate": "2026-09-15T00:00:00Z", "style": "flip" }
    </script>
  </lx-island>
</section>

<style>
  /* becomes section.css — scope selectors to this section */
  .hero-lede { max-width: 62ch; }
</style>

<script
  type="application/lexsis-motion"
  data-motion-id="hero-entrance"
  data-capabilities="waapi"
  data-mode="entrance"
  data-importance="decorative"
  data-reduced-motion="static"
>
({ dom, waapi }) => {
  const lede = dom.query(".hero-lede");
  if (!lede) return;
  waapi.animate(lede, [
    { opacity: 0.25, transform: "translateY(18px)" },
    { opacity: 1, transform: "translateY(0)" }
  ], { duration: 600, fill: "both" });
}
</script>

<!-- section: faq -->
<section class="py-12">
  <details>
    <summary>Can I return it?</summary>
    <p>Yes — 30 days, no questions asked.</p>
  </details>
</section>
```

### Rules

1. **Sections** are delimited by `<!-- section: kebab-case-id -->` comments. Ids must be unique.
2. **Islands** are `<lx-island name="IslandName">` with props as a `<script type="application/json">` child. Write natural copy — apostrophes, quotes, em-dashes are all fine; no escaping needed.
3. **`<lx-island>` attributes**: `name` (required), `hydrate` (`immediate|visible|idle|interaction`), `headless` (headless mode — see below), plus `class`/`id`/`style` which pass through to the compiled element.
4. **Section CSS** goes in a top-level `<style>` block. New custom animation
   goes in `<script type="application/lexsis-motion">`. Plain top-level
   `<script>` remains compatibility section JS. `application/json` / `ld+json`
   scripts stay in the HTML.
5. **External libraries** do not go in section HTML. Approved analytics and
   integrations use `scripts`; GSAP, Three.js, Lottie, and Rive use managed
   motion loaders instead.
6. **`head`, `theme_css`, `scripts`** are structured tool arguments. Save the
   selected theme and approved page-wide additions in `page-theme.css`, then
   pass that file's exact contents as `theme_css`.
7. Tailwind classes compile into one `compiled_page_css` artifact. Fix every
   missing candidate; do not add Tailwind CDN or a separate generated sheet.

### Tool workflow

```
lexsis_brand → list_themes/get_theme → theme_css
draft source HTML (whole page)
lexsis_pages { action: "compile", args: { source, head, theme_css, scripts } }
fix any issues, then:
lexsis_page_create { action: "create", args: { source, head, theme_css, scripts, slug, publish: false } }
edits: lexsis_drafts → page_update_section or page_patch
round-trip: lexsis_pages → source/section_source → lexsis_drafts
```

`page_update_section` compiles one section and upserts it. `page_patch` batches
related localized changes into one version. Pass `expected_version`.

## Starting From a Template

Search the section library before writing a section from scratch. When you pick
a template, request editable source:

```text
lexsis_design({ action: "get_section", args: { ids: ["template-id"] } })
```

The response's `source` is one complete source-format section: a delimiter,
`<lx-island>` markup, and the template CSS/JS. Tailor it, then run
`lexsis_pages` action `compile`.

`format: "compiled_reference"` is renderer output containing
`data-island` / `data-props`. It is useful for inspection but must never be
given to source-authoring tools.

## Headless islands (fully custom markup)

For maximum design freedom, add `headless` and author the island's internals yourself; behavior attaches to `data-lx-*` hooks. Currently supported: **BuyBox** (plus the long-standing Navbar/Footer/SiteHeader hydration modes — see island-patterns.md).

```html
<lx-island name="BuyBox" headless>
  <script type="application/json">
    { "product": { "title": "Serum", "price": "$49.00", "variants": [
      { "id": "v1", "title": "30ml", "price": "$49.00", "available": true },
      { "id": "v2", "title": "50ml", "price": "$69.00", "available": true }
    ] } }
  </script>

  <p class="text-3xl font-bold" data-lx-buybox="price">$49.00</p>
  <div class="flex gap-2">
    <button data-lx-buybox="variant-option" data-variant-id="v1" class="px-4 py-2 border rounded-full">30ml</button>
    <button data-lx-buybox="variant-option" data-variant-id="v2" class="px-4 py-2 border rounded-full">50ml</button>
  </div>
  <div class="flex items-center gap-3">
    <button data-lx-buybox="qty-dec">−</button>
    <span data-lx-buybox="qty">1</span>
    <button data-lx-buybox="qty-inc">+</button>
  </div>
  <button data-lx-buybox="add" class="w-full py-4 rounded-full text-white"
          style="background: var(--lx-accent-color)">Add to Cart</button>
  <p data-lx-buybox="error" class="text-red-600 text-sm">Couldn't add — try again.</p>
</lx-island>
```

### BuyBox hooks

| Hook | Required | Behavior |
|---|---|---|
| `add` | **yes** | add-to-cart trigger; gets `lx-adding` / `lx-added` classes |
| `price` | recommended | text kept in sync with selected variant/plan |
| `compare-price` | no | compare-at price; hidden when none |
| `variant-option` | no | one per variant, needs `data-variant-id="v1"`; gets `lx-selected` / `lx-disabled` |
| `qty` / `qty-inc` / `qty-dec` | no | quantity display (or `<input>`) + stepper |
| `stock` | no | availability text; override via `data-in-stock-text` / `data-out-of-stock-text` |
| `error` | no | revealed when add-to-cart fails |

Style the state classes in section CSS: `.lx-selected { ... }`, `.lx-adding { opacity: .6 }`, `.lx-disabled { pointer-events: none; opacity: .4 }`.

## Animations

Read `animation-system.md` before authoring any plan-named custom motion.

### Presets — `data-behavior`

```html
<section data-behavior="gsap-reveal" data-config='{"targets":".card","y":40,"stagger":0.1}'>
<div data-behavior="gsap-parallax" data-config='{"speed":0.3}'>
<section data-behavior="gsap-pin" data-config='{"stepDuration":0.5}'>  <!-- children: [data-pin-step] -->
<div data-behavior="gsap-marquee-scroll" data-config='{"distance":-200}'>
```

Presets use the renderer-owned pinned GSAP loader and respect reduced motion.
Also available (CSS-driven, pre-existing): `scroll-reveal`, `accordion`,
`horizontal-scroll`, `content-slider`, and `sticky-reveal`.

### Custom managed motion

Use `<script type="application/lexsis-motion">` for custom WAAPI, GSAP, SVG,
Canvas 2D, WebGL, Three.js, Lottie, Rive, video, pointer, scroll, or runtime
event work. Declare capabilities and use managed timers, observers, loops,
assets, and engine loaders. Do not add animation libraries through `scripts`.

The MCP compiler extracts managed motion into `section.motion[]`, validates the
AST and performance budgets, and round-trips it through source reads and page
patches. Plain section JS remains only for compatibility behavior.

## What NOT to do

```html
<!-- Don't: hand-written island markers (old format — compiler rejects raw usage in source) -->
<div data-island="FAQ" data-props='{"items":[...]}'></div>

<!-- Don't: escaped HTML — never escape anything -->
&lt;section&gt;...&lt;/section&gt;

<!-- Don't: external scripts in section HTML — use the scripts param -->
<script src="https://cdn.example.com/lib.js"></script>
```
