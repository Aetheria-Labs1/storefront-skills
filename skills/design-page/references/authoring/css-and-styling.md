# CSS and styling

How a Lexsis page is styled, and how to decide where a rule goes. Read this
before writing the first class attribute. It is the styling layer under
`references/workflows/section-asset-workflow.md` (which media a section gets)
and `references/workflows/island-selection-workflow.md` (which island a
section gets). House rules in `references/design-rules.md` outrank everything
here, and `lexsis_pages` action `compile` outranks every document: it decides
whether a class, a rule or a module is legal.

Two facts set the shape of the file. Tailwind is compiled at build time from
the classes present in your source, with no runtime CDN, so a class the
compiler cannot generate is a blocking error rather than a silent no-op. And
section CSS is appended after the generated utilities, so it can quietly defeat
them, which makes it powerful and makes it the wrong default.

## 1. The cascade you are writing into

Compiled CSS lands in exactly this order
(`references/lexsis-design-capabilities.md`):

```text
1. theme CSS                        page-theme.css, passed as theme_css
2. generated Tailwind utilities     compiled from the classes in your source
3. section CSS in page order        each section's <style> block, top to bottom
```

The renderer has already supplied its reset, base typography, smooth
scrolling, and the shared keyframes `fadeUp`, `fadeIn`, `scaleIn`,
`slideInLeft`, `slideInRight`, `marquee`, `float`, `shimmer`, `wordFade`,
`pulseRing`. You never ship a second reset and never redefine those names.

| Layer | Owns | Never holds |
|---|---|---|
| Theme CSS (`page-theme.css`) | `--lx-*` token values, the radius scale (`--r-control`, `--r-card`, `--r-media`, `--r-pill`), the type scale, `:focus-visible`, one `prefers-reduced-motion` block, page-wide `@font-face` if any | per-section layout, one-off component rules, anything only one section reads |
| Generated utilities | all layout, spacing, sizing, flex, grid, responsive behaviour, state variants | nothing you author directly; you author the classes |
| Section CSS (`<style>` in the section) | one scoped component's geometry, `data-part` overrides for that section's islands, one scoped keyframe, `@supports` and container-query fallbacks, print and RTL adjustments | page layout, tokens, global element selectors, a second grid system |

Putting layout in section CSS fights the utilities you already wrote.
`md:grid-cols-3` is one class on one element; `.benefits > div { width:
33.333% }` is invisible from the markup, survives the breakpoint change you
make later, and wins on equal specificity because it ships last, so the bug
looks like Tailwind not working.

Check: for every rule in a section `<style>` block, name which of the five
allowed jobs in section 3 it does. A rule with no job is a utility you have
not written yet.

## 2. Tailwind is the default

Layout, spacing, sizing, flex and grid, responsive behaviour, application of
the type scale, and state variants are all utility classes. Author mobile
first: the unprefixed class is the small screen, and `sm:`, `md:`, `lg:`,
`xl:` add upward. Never write a max-width prefix chain to undo a desktop
default. Section 8 shows a whole section written this way.

Rules that keep the compile clean:

1. **Every class is a real utility.** `section-pad-lg`, `wrapper-xl` and
   `grid-3up` are not; the compiler reports them and the page has no padding,
   wrapper or grid until you fix them. The one exception is a class you define
   in the same section's CSS for a job section 3 allows, and it is a hook, not
   a layout system.
2. **No arbitrary value the config cannot produce.** `max-w-[62ch]` is fine
   because it resolves to a plain CSS value; a class needing a config key that
   does not exist never resolves.
3. **No dynamic class-name construction.** Classes are literal text in source;
   one built at runtime, or living only in island props, is never scanned.
4. **Spacing comes from one 8-point scale** and section padding from at most
   two pairs, per `references/design-rules.md` A2. Pick the pair once and
   repeat it; do not tune each section.
5. **Type sizes are steps of one modular ratio** (A3), at most three visible
   on a screen, one `<h1>` per page and one `<h2>` per section.
6. **State variants are utilities too**: `hover:`, `focus-visible:`, and the
   `data-` and `aria-` attribute variants the config enables. N7 bans the
   specific hover effects `hover:scale`, `hover:-translate` and
   `hover:scale-1xx` on cards, buttons and images; a hover state changes colour
   or border colour.

Check: grep your source for class tokens that are not in the compiler's
report. `validation_errors` and `missing_candidates` from
`lexsis_pages` action `compile` are the authoritative list, and
`missing_candidates` must be empty before you create the draft.

## 3. When section CSS is justified

This is a closed list. Anything not on it is a utility.

**a. Geometry utilities cannot express.** A named grid template, a clip path,
an aspect-driven collage.

```css
/* section: lookbook */
#lookbook .lookbook-grid {
  display: grid;
  grid-template-areas: "wide wide tall" "detail scale tall";
  grid-template-columns: 1fr 1fr 1.2fr;
  gap: 1.5rem;
}
#lookbook [data-tile="wide"] { grid-area: wide; }
```

**b. An island's `data-part` hooks.** Section 5 covers this in full.

**c. One scoped keyframe, and its reduced-motion pair, for the plan's single
motion moment.** Named after the section, never a shared keyframe name.

```css
@keyframes hero-rule-draw { from { transform: scaleX(0) } to { transform: scaleX(1) } }
#hero .hero-rule { transform-origin: left; animation: hero-rule-draw 700ms ease both; }
@media (prefers-reduced-motion: reduce) {
  #hero .hero-rule { animation: none; transform: none; }
}
```

**d. An `@supports` or container-query fallback.**

```css
#gift-grid .gift-tiles { display: grid; grid-template-columns: repeat(2, 1fr); container-type: inline-size; }
@container (min-width: 40rem) { #gift-grid .gift-tiles { grid-template-columns: repeat(4, 1fr); } }
```

**e. A print or RTL adjustment**, scoped the same way:
`#specs [dir="rtl"] .spec-row { text-align: right }`. Two rules bind all five:

- **Always scope by the section id.** `#hero .hero-rule`, never `.hero-rule`
  alone, never a bare element selector such as `section { padding: 96px 0 }`,
  never a utility-class selector such as `.grid { gap: 2rem }`. Every section's
  CSS ships in one stylesheet, so an unscoped rule reaches the whole page.
- **Never a second global layout system.** Section CSS that defines containers,
  column widths, breakpoint media queries or vertical rhythm has rebuilt
  Tailwind badly; delete it and write classes.

## 4. Tokens, never raw values

Brand colour, type, surfaces, borders and radii come from `--lx-*` tokens the
theme compiler produced and contrast-checked. The set
(`references/lexsis-design-capabilities.md`):

```text
--lx-accent-color        --lx-bg-color        --lx-text-color     --lx-border-color
--lx-accent-color-hover  --lx-bg-surface      --lx-text-muted
--lx-accent-soft         --lx-surface-alt
optional: --lx-font-heading   --lx-font-body   --lx-radius
```

`--lx-bg-color` is the page background, and by N2 the only one from below the
navbar to above the footer. `--lx-bg-surface` and `--lx-surface-alt` are
component tints (a card, a chip, a selected state), never a section fill.
`--lx-text-muted` is the muted pairing the compiler checked; dimming
`--lx-text-color` with `opacity` is not the same thing and drops below A7.

How to reach a token:

| Situation | Write |
|---|---|
| Colour or font on an element | `style="background-color: var(--lx-accent-color)"`, `style="font-family: var(--lx-font-heading)"` |
| Inside section CSS | `border: 1px solid var(--lx-border-color)` |
| Radius | `border-radius: var(--r-card)` (or `--r-control`, `--r-media`, `--r-pill`) |

Rules:

1. **No off-brand hex and no Tailwind default palette classes** (N14). The
   named offenders the checks look for are `#667eea`, `#764ba2`, `#8b5cf6`,
   `#f9fafb`, `#6366f1`, `#7c3aed`, and `text-yellow-*`, `text-gray-*`,
   `text-slate-*`, `text-purple-*`, `text-indigo-*`.
2. **Never redefine a `--lx-*` token inside a section.** A section that sets
   `--lx-accent-color` has forked the brand for everything below it in the
   cascade. Set island-specific variables instead (section 5).
3. **A page-level token override belongs in `page-theme.css`**, inside
   `:root`, once, with a comment naming why. That file also declares the radius
   scale with its object-type mapping (A6, N13), four values or fewer, and
   lists the type scale so the ratio is auditable. One radius on everything is
   the absence of a system; five is noise.

## 5. Styling islands correctly

An island owns its internals. You get two contact surfaces, both listed in its
schema (`lexsis_design` action `island_schema` live, or the bundled
`references/islands/<slug>/schema.json`): `parts`, the `data-part` values you
may select, and `css_vars`, the custom properties the island reads. Prefer a
`css_vars` value over a rule: a variable is the island's own API and survives a
version bump, while a rule is a bet on internal structure.

Real example, `ProductGallery`, whose schema declares
`--lx-product-gallery-gap`, `--lx-product-gallery-radius`,
`--lx-product-gallery-columns` and `--lx-product-gallery-tile-ratio` in
`css_vars`, and `thumbnail`, `thumbnail-strip`, `main-media` and
`open-lightbox` in `parts`.

```css
/* section: gallery */
#gallery [data-part="root"] {
  --lx-product-gallery-gap: 0.75rem;
  --lx-product-gallery-radius: var(--r-media);
}
#gallery [data-part="thumbnail"] { border: 1px solid var(--lx-border-color); }
#gallery [data-part="open-lightbox"] { border-radius: var(--r-control); }
```

Second real example, `BuyBox`. Its schema declares parts `root`, `cta`,
`variants`, `variant-btn`, `qty`, `qty-btn`, `trust-badges`, `notify`, and
`--lx-accent-color` as its only `css_var`.

```css
#buy [data-part="cta"] { border-radius: var(--r-control); }
#buy [data-part="variant-btn"] { border: 1px solid var(--lx-border-color); border-radius: var(--r-control); background: transparent; color: var(--lx-text-color); }
#buy [data-part="qty"], #buy [data-part="qty-btn"] { border-color: var(--lx-border-color); }
```

Rules:

1. **Only `[data-part="x"]` selectors**, and only the parts the schema lists.
   Class names inside an island change between versions; a part name is a
   contract. Never select an island's internal DOM by tag path or class.
2. **Always scope by section id.** `cta`, `root`, `item`, `heading`, `link`
   and `badge` repeat across islands. `#buy [data-part="cta"]` is a rule;
   `[data-part="cta"]` is a page-wide accident.
3. **Visual properties only.** Colour, border, radius, typography, and the
   island's own spacing variables. `display`, `position`, `float`,
   `grid-template`, or a width on `[data-part="root"]` breaks the responsive
   behaviour the island ships, and the compile will not catch it.
4. **No `!important` and no id beyond the section scope.** Section CSS already
   wins at equal specificity because it is last. A rule that is not landing
   means the selector is wrong, or you are fighting an inline style the island
   sets from a prop, in which case the prop is the fix.
5. **A preset's CSS is applied verbatim.** `references/island-presets.md` ships
   each preset as props plus scoped CSS in the `#{{id}} [data-part=...]` form.
   Substitute the section id, paste it into that section's `<style>`, and do
   not rewrite it. Every deviation, in props or CSS, is recorded as
   `islands[].presetOverrides` in `page-manifest.json` as a JSON merge patch
   (`null` removes a preset prop) and named in `page-plan.md`.
6. **Hide, do not fight.** Some islands expose a part no prop controls, for
   example `AnnouncementBar`'s `icon`. With no icon set on the page, the move
   is `#promo [data-part="icon"] { display: none }`, not a competing glyph.

## 6. Responsive and accessible by construction

Mobile first, in prefix order. The prefixes in use are `sm:`, `md:`, `lg:`
and occasionally `xl:`; the compiler's Tailwind config owns their pixel values,
so never restate them as hardcoded media queries. The hosted review runs at
390px and 1280px in `/design-page` and adds 768px in `/generate`; those three
widths are what your class chain has to read correctly at.

Floors, all reachable with utilities:

| Floor | Value | Source |
|---|---|---|
| Tap target, any control | 24 x 24 CSS px | WCAG 2.2 SC 2.5.8, `references/anti-patterns/mobile-anti-patterns.md` MA11 |
| Tap target, close, swatch, quantity | 44 x 44 | MA11 |
| Tap target, primary CTA | 48 x 48 | `references/design-rules.md` A11 |
| Body text on mobile | never below `text-sm` | `references/islands/_contract.md` |
| Body measure | 45 to 80 characters at every width, constrained in `ch` | A4 |
| Text contrast | 4.5:1 under 24px, 3:1 for large text and component boundaries | A7 |

```html
<a href="#buy" class="inline-flex min-h-[48px] items-center px-6 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2"
   style="background-color: var(--lx-accent-color)">Add to cart</a>
<p class="max-w-[68ch] leading-relaxed" style="color: var(--lx-text-muted)">...</p>
```

`:focus-visible` and the one `prefers-reduced-motion` block live in
`page-theme.css` so they apply once. A section adds a reduced-motion rule only
when it owns the plan's motion moment (section 3c). Measure is
`max-w-[NNch]`, never a pixel width, which is wrong at the next type scale.

## 7. What never appears

| Never | Why |
|---|---|
| Runtime Tailwind CDN, `<link>` or `<script>` to `cdn.tailwindcss.com` | Tailwind is compiled; the CDN is a second, unversioned stylesheet |
| `@import`, or any external URL in CSS, including a font stylesheet | rejected; fonts are a structured `head.fonts` argument, not an import |
| `<script src>` in section HTML | approved integrations go in page `scripts[]`; GSAP, Three.js, Lottie and Rive use managed motion loaders |
| Inline `style` for anything a token or utility covers | it is unreviewable and unscoped; the narrow exception is a one-off computed value such as `style="object-position: 60% 40%"` for an asset focal point, required by `references/assets/slot-spec.md` SS11 |
| `!important` | section CSS is already last in the cascade |
| ID selectors beyond the section scope | specificity escalation nobody can unwind |
| A second reset or base-typography block | the renderer already shipped one |
| Global element selectors in section CSS (`section`, `h2`, `p`, `img`), or unscoped `@keyframes` | they leak to every section, and keyframe names collide |
| Hardcoded pixel media queries duplicating Tailwind's breakpoints | two sources of truth for one layout |
| Gradient washes, glow shadows, `shimmer`, `animate-pulse`, `pulseRing`, `float`, animated backgrounds | N7; the only permitted gradient is a black-to-transparent legibility overlay inside the plan-named bold moment |
| `hover:scale`, `hover:-translate`, `hover:scale-1xx`, `transform: scale(1.0x)` on cards, buttons, images | N7; hover changes colour or border colour |
| A section or full-width wrapper painted `--lx-bg-surface`, `--lx-surface-alt` or `--lx-secondary-color` | N2; one page background |
| Off-brand hex or Tailwind palette colour classes | N14 |

## 8. One section, badly and correctly

Badly:

```html
<!-- section: benefits -->
<section class="benefit-band section-pad-lg">
  <link rel="stylesheet" href="https://cdn.tailwindcss.com/3.4.16/tailwind.min.css">
  <div class="wrapper-xl grid-3up">
    <div class="benefit-card"><h3>Cold pressed</h3><p>Pressed the day it ships.</p></div>
  </div>
</section>
<style>
  @import url("https://fonts.googleapis.com/css2?family=Inter");
  section { padding: 96px 0; }
  .benefit-band { background: linear-gradient(180deg, #f9fafb, #ffffff); }
  .benefit-card { border-radius: 16px; box-shadow: 0 0 24px rgba(102, 126, 234, .35); color: #667eea; }
  .benefit-card:hover { transform: translateY(-4px) scale(1.02); }
</style>
```

Correctly:

```html
<!-- section: benefits -->
<section id="benefits" class="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
  <div class="mx-auto max-w-6xl">
    <h2 class="text-2xl md:text-3xl lg:text-4xl" style="font-family: var(--lx-font-heading)">
      Why it works
    </h2>
    <ul class="mt-8 grid grid-cols-1 gap-8 md:grid-cols-3 md:gap-10">
      <li class="max-w-[62ch]">
        <h3 class="text-lg">Cold pressed</h3>
        <p class="mt-2 leading-relaxed" style="color: var(--lx-text-muted)">Pressed the day it ships.</p>
      </li>
    </ul>
  </div>
</section>
```

Line by line:

| Change | Why |
|---|---|
| Removed the Tailwind `<link>` and the `@import` | there is no runtime CDN, `@import` is rejected, and fonts belong in `head.fonts` |
| `benefit-band section-pad-lg` to `px-4 py-16 sm:px-6 lg:px-8 lg:py-24` | invented classes are blocking compile errors; padding now comes from the scale (A2) |
| `wrapper-xl grid-3up` to `mx-auto max-w-6xl` plus `grid grid-cols-1 gap-8 md:grid-cols-3` | mobile first, layout in utilities, no hidden second grid |
| Deleted the whole `<style>` block | nothing in it did one of the five jobs in section 3, and `section { padding }` reached every section on the page |
| Dropped the gradient, the glow shadow and the hover lift | N7; hover changes colour or border colour |
| `#667eea` and `#f9fafb` to `--lx-text-muted` on the page background | N14, and the token pairing is contrast-checked |
| `<div class="benefit-card">` to `<li>` with no card, plus `max-w-[62ch]` | N8 keeps plain text on the page background; A4 sets measure in `ch` |

## 9. Debugging the compile

`lexsis_pages` action `compile` returns the compiled page plus
`validation_errors` and publish validation. Treat `validation_errors` as the
work list and `missing_candidates` as a hard gate: it must be empty before
`lexsis_page_create` action `create`.

Common causes, in the order worth checking:

1. **Unknown utility class.** An invented name, a typo, a class that exists
   only as a string inside island props, or an arbitrary value the config
   cannot produce. Fix the class; never add a CDN or a hand-written rule.
2. **Unknown island.** A misspelled `name`, or a deprecated one. The bundled
   schemas mark `BackToTop`, `Carousel`, `CartDrawer`, `Countdown`, `FAQ`,
   `Marquee`, `StatCards` and `Tabs` deprecated, each with a replacement.
3. **Invalid props.** Shape drift between a bundled example and the live
   schema. Fetch that one island's schema and copy from `authoring.examples`.
4. **Missing required hook.** A headless island without it. `BuyBox` headless
   requires `data-lx-buybox="add"`.
5. **Motion module rejected.** A `motion_*`, `unmanaged_*` or capability error.
   The compiler rejects `window`, `document`, `fetch`, storage, raw timers, raw
   animation frames, raw observers, dynamic imports, programmatic `.click()`,
   island-internal access, unbounded loops, and undeclared capabilities. See
   `references/animation-system.md`.
6. **`missing_candidates` not empty.** Every entry is a class the page asked
   for and the compiler could not produce. Resolve all of them.

Repair order: classes first, because they are mechanical and cheap; then
islands and props, fetching a full schema only for an island an error names;
then motion; then recompile. Loop until blocking errors are clear, save the
clean response and input hashes in `compile-artifact.json`, and create with
`publish:false`.

The compiler is the authority on what is legal, not on what looks right. A
clean compile proves contract safety and nothing about hierarchy, banding,
crops, contrast in context, or whether the page reads as one design. The hosted
draft at 390px and 1280px settles that, and
`design-page/scripts/design_lint.py <workspace>` runs the static house-rule
checks.

## Precedence over older craft docs

Several older docs in this folder predate the compiler contract and the house
rules. Where any of them disagrees with this file or
`references/design-rules.md`, this file and the rules win, and each of those
docs now carries a correction note at the point of the outdated guidance. You
do not need to remember which: follow the rules, and treat a code example as
illustrative until it agrees with them.
