# Source authoring

How to write the page source itself so it compiles and renders correctly the
first time. The styling half is `references/authoring/css-and-styling.md`; the
format contract is `references/source-format.md`; house rules are
`references/design-rules.md`. Where an older example in this folder disagrees
with the compiler, the compiler wins.

You are writing one file, `lexsis-source.html`, as plain HTML. The compiler
turns it into the stored page and does every piece of escaping. You never
hand-write `data-island`, `data-props`, or an escaped entity.

## 1. The page workspace

```text
work/campaigns/<campaign-slug>/pages/<page-handle>/
├── page-plan.md            hand-written, by /plan-page
├── page-manifest.json      hand-written state ledger, grown per stage
├── lexsis-source.html      hand-written, the canonical page source
├── page-theme.css          hand-written, global tokens and page-wide rules
├── compile-artifact.json   generated: the clean compile response and hashes
├── qa-report.md            hand-written, by /generate
└── assets/
```

`lexsis-source.html` and `page-theme.css` are the only editable design inputs.
Everything else is either state or generated. `references/page-files.md` and
`references/source-artifact-workflow.md` own the manifest shape, the hash
fields and the edit-and-sync loop; do not restate them here, and do not commit
a compiled page as if it were source.

`head`, `theme_css` and `scripts` are not in the HTML file. They are structured
arguments you pass to `lexsis_pages` action `compile` and
`lexsis_page_create` action `create`. `theme_css` is the exact contents of
`page-theme.css`.

## 2. Section delimiters and ids

A section starts at a comment and runs to the next one:

```html
<!-- section: hero -->
<section id="hero" class="px-4 py-16 sm:px-6 lg:px-8">
  ...
</section>

<!-- section: reviews -->
<section id="reviews" class="px-4 py-16 sm:px-6 lg:px-8">
  ...
</section>
```

Rules:

1. **Ids come from the canonical vocabulary** in
   `references/page-types/_checklist-format.md`. Use a listed id, or a listed
   id with a suffix (`reviews-skin-type` satisfies `reviews`). Do not invent a
   name; add a new id only by adding it to that file.
2. **Kebab-case, unique on the page.** The compiler rejects a duplicate.
3. **One `<section id="...">` per delimiter**, with the element id matching
   the delimiter id. That is what makes section CSS scopable
   (`#hero .hero-rule`) and what island presets substitute into their
   `#{{id}} [data-part=...]` selectors.
4. **Stable across edits.** Edits are applied as section patches:
   `lexsis_drafts` action `page_update_section` compiles and upserts one
   section, and `page_patch` batches related changes, both with
   `expected_version`. A renamed id reads as a delete plus an insert, loses
   the section's version history, and breaks any `showAfter` selector or
   in-page anchor pointing at it. Rename only when the section's job actually
   changed.
5. **Announcement, header, nav and footer are ordinary sections** in source
   order. The renderer injects no hidden shell around them
   (`references/lexsis-mcp-contract.md`). Source order is the page order.

## 3. Authoring islands

One element, one JSON child:

```html
<lx-island name="ReviewCarousel" hydrate="visible">
  <script type="application/json">
    { "collectionId": "...", "minRating": 4, "pageSize": 12, "autoplay": false }
  </script>
</lx-island>
```

`autoplay: false` is not redundant: this island's schema defaults it to `true`,
and N10 allows motion only at the plan's single named moment. Several islands
ship motion on, so read the defaults rather than assuming off.

Rules:

1. **`<lx-island name="X">` with one `application/json` script child.** Write
   the JSON readably. Apostrophes, quotes and dashes in copy need no escaping,
   because the compiler writes `data-props`, not you.
2. **Never hand-write compiled markup.** `data-island` and `data-props` are
   renderer output. `lexsis_design` action `get_section` returning
   `format: "compiled_reference"` is for inspection only and must never be fed
   back to a source-authoring tool.
3. **Props are resolved live from the schema**, per
   `references/workflows/island-selection-workflow.md`. Copy shapes from the
   schema's `authoring.examples`, not from memory or from a prose example. Set
   only props a decision in the plan justifies; everything else stays at its
   default. Sibling islands name the same field differently, so a shape that
   worked for one gallery is not proof for another.
4. **Allowed attributes are `name`, `hydrate`, `class`, `id`, `style`**, plus
   `headless` where the schema supports it. `class`, `id` and `style` pass
   through to the compiled element.
5. **Hydration comes from the schema's `defaultHydrate`** unless a preset says
   otherwise. Read the value from the schema; never infer it from the island's
   job. Across the 47 active bundled contracts there are only four groups, and
   `immediate` is the overwhelming default:

   | `defaultHydrate` | Islands |
   |---|---|
   | `immediate` (36) | AnnouncementBar, BeforeAfter, BundleBuilder, BuyBox, CartCheckoutButton, CartCrossSell, CartDiscountInput, CountdownTimer, DeliveryEstimate, DrawerShell, EmailCapture, Footer, FunnelRuntime, HeroMedia, ImageZoom, IngredientExplorer, InventoryIndicator, MobileMenu, Modal, Navbar, OptionResolver, PaymentOptions, PlanSelector, ProceedToCart, ProductCarousel, **ProductGallery**, QuantityBreaks, ShoppableVideoFeed, SiteHeader, SizeGuide, StickyBar, SubscriptionToggle, VariantSelector, VariantSwatches, VideoPlayer, WishlistButton |
   | `visible` (6) | FeaturedCollectionStage, MediaCarousel, ProductHero, ReviewCarousel, ReviewList, SocialProofPopup (never used) |
   | `idle` (4) | CartLines, CartProgressBar, CartSummary, GalleryLightbox |
   | `interaction` (1) | QuickAdd |

   `ProductGallery` is bold because it is the one most often assumed to be
   `visible`: it is `immediate`, since a lazily hydrated gallery is the page's
   largest contentful paint.
6. **Fallback content is one `data-lx-island-fallback` child** of the
   `<lx-island>`, a sibling of the JSON script, showing readable content until
   the island hydrates (`references/island-presets.md`). Keep it simple,
   Tailwind-only so every class compiles, and free of interactive controls that
   could be mistaken for the island: a static price and a link to the product
   page, never a working custom button. Never replace `BuyBox` or another
   commerce island with a hand-built button. Custom internals are a different
   mechanism: only `BuyBox` sets `authoring.headless.supported`, with hooks
   `add` (required), `price`, `compare-price`, `variant-option`, `qty`,
   `qty-inc`, `qty-dec`, `stock` and `error`. Separately the navigation islands
   accept authored markup through hydration hooks: `data-lx-header` and
   `data-lx-nav` on SiteHeader, `data-lx-nav` on Navbar and MobileMenu,
   `data-lx-footer` on Footer.
7. **One-instance rules bind.** One purchase form, header island, footer,
   sticky bar, lightbox, auto-triggered overlay, announcement bar and option
   resolver per page. `SiteHeader`, or `Navbar` plus `AnnouncementBar`, never
   both.
8. **Cart is configuration, not a section.** Set `head.use_cart_v2: true` on
   every commerce page and never author a cart section; the renderer injects
   the published cart profile.
9. **Headless mode only when a native variant cannot satisfy the approved
   design**, and only with every required hook present. `BuyBox` headless
   requires `data-lx-buybox="add"` and offers `price`, `compare-price`,
   `variant-option` (with `data-variant-id`), `qty`, `qty-inc`, `qty-dec`,
   `stock`, `error`. Style its state classes `lx-selected`, `lx-disabled`,
   `lx-adding`, `lx-added` in the section CSS.

## 4. Static HTML first

An island is justified only when the section needs cart or variant state, live
catalogue data, media behaviour, an overlay, or a form that posts. Everything
else is HTML you write, and several islands that used to cover these jobs are
now deprecated with HTML named as the replacement.

| Job | Write | Why not an island |
|---|---|---|
| Accordion, FAQ | `<details>` with `<summary>` | `FAQ` is deprecated; its replacement is native markup |
| Tabs | radio inputs plus labels, or `<details>` | `Tabs` is deprecated |
| Stat figures | `<dl>` with `<dt>`/`<dd>`, or `<figure>` | `StatCards` is deprecated; ledger numbers only, no count-up |
| Logo row | `<ul>` of `<a>` wrapping monochrome `<img>` or inline SVG, one height | `Marquee` is deprecated; an unlinked press logo is not rendered at all |
| Comparison table | `<table>` with `<th scope>` | no island covers it |
| Product grid | your own card markup in a utility grid | keeps the grid in utilities |
| Back to top | `<a href="#top">` with CSS `scroll-behavior` | `BackToTop` is deprecated |
| Generic slider | CSS `scroll-snap` | `Carousel` is deprecated in favour of scroll-snap or a specialised island |

Keep them accessible: `<details>` and `<summary>` give you the disclosure
semantics for free, so do not add `role` or `aria-expanded` on top. A radio-tab
set needs a real `<label for>` per input and a visible `:focus-visible` ring. A
table needs `<th scope="col">` or `scope="row"`, and a caption when the
comparison is not obvious from the heading above it. Every control clears the
tap-target floors in `references/authoring/css-and-styling.md` section 6.

Re-check `deprecated` in the live catalogue each build. If the live catalogue
shows an island active that the bundled schema calls deprecated, the live
catalogue wins.

## 5. Head, fonts and scripts

Passed as structured arguments, never as markup in the HTML file:

```json
{
  "head": {
    "title": "Cold-pressed vitamin C serum - Aurelia",
    "fonts": ["https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600&display=swap"],
    "use_cart_v2": true
  }
}
```

- **`head.title`** is the real page title, sentence case, brand at the end.
- **`head.fonts`** holds complete HTTPS stylesheet URLs, or nothing at all if
  the design is an intentional system stack. Never `@import` a font in CSS and
  never `<link>` one in section HTML. At most two families (N4); a non-Latin
  script may add one matching family declared with `[lang]`.
- **`head.use_cart_v2: true`** on every commerce page.
- **`scripts[]`** is for approved analytics and integrations only. GSAP,
  Three.js, Lottie and Rive are never loaded here; they have managed loaders
  (`references/animation-system.md`). No `<script src>` in section HTML.

## 6. Copy and content in source

Copy is design content, not filler added later. Write it as you write the
markup.

- **Sentence case** for headings, buttons and labels. No ALL-CAPS eyebrow
  unless a merchant-stated brand rule requires it, and then at most one per
  three sections (N5).
- **No escaping.** Write `Don't miss the "Summer Drop"` directly, in markup and
  inside island JSON. Escaped entities in source are a bug, not caution.
- **CTA names the action.** "Add to cart", not "Shop Now". No `→` or `»`
  appended to link or button text (N12).
- **Alt text** follows `references/assets/slot-spec.md`: under 125 characters,
  describing what a blind shopper needs, never "image of"; `alt=""` for
  decorative backdrops and textures; product media always has alt (A11).
- **`lang` attributes** on any non-Latin run of text, with the matching family
  declared for that `[lang]`.
- **No invented proof.** Every numeral in a proof section traces to the plan's
  confirmed claims (N11), and reviews are verbatim from the ledger.
- **No emoji** anywhere, including island JSON props and CSS `content` (N1).
- Read `references/anti-patterns/copy-anti-patterns.md` before writing
  headings and controls; its vocabulary and structure lists are what
  `design_lint.py` C1 to C4 check.

## 7. Motion

The plan names at most one motion moment for the whole page (N10). Author it as
a managed module in the same section as its markup:

```html
<script
  type="application/lexsis-motion"
  data-motion-id="hero-rule"
  data-capabilities="waapi"
  data-mode="entrance"
  data-importance="decorative"
  data-reduced-motion="static"
>
({ dom, waapi }) => {
  const rule = dom.query(".hero-rule");
  if (!rule) return;
  waapi.animate(rule, [{ transform: "scaleX(0)" }, { transform: "scaleX(1)" }],
    { duration: 700, fill: "both" });
}
</script>
```

The body is one function expression. Declare every capability the code uses;
undeclared capability APIs are removed from the runtime context. Read
`references/animation-system.md` before writing one.

Everything that is not that single moment is a CSS transition on hover, focus,
or an open/closed state, and content stays visible by default so a failed
module never leaves a blank section. Common reveal, parallax, pin and marquee
behaviour has renderer-owned presets (`data-behavior="gsap-reveal"` and
siblings) that respect reduced motion; use one rather than writing a module.

## 8. Section JS

A plain top-level `<script>` in a section is compatibility-only, and it is
lifecycle-wrapped. It cannot use global DOM queries, unmanaged observers or
loops, raw timers, programmatic `.click()`, `fetch`, `eval`, or browser
storage.

The rule that follows: if a behaviour needs global DOM access, an observer, a
timer, or an animation frame, it is a managed motion module or an island, not
section JS. Body-scroll locking, wheel hijacking and `setTimeout` recipes in
older craft docs are all in that category.

## 9. The compile and repair loop

1. Write a **rough but complete** page: every planned section, real delimiters,
   real copy, minimal island props from the schema examples. Complete beats
   polished, because the compiler reports across the whole page at once.
2. Call `lexsis_pages` action `compile` with `source`, `head`, `theme_css` and
   `scripts`. It returns the compiled page plus `validation_errors` and publish
   validation.
3. Work `validation_errors` as a list. Fetch a **full island schema only for an
   island an error names**, or when a required behaviour is genuinely unclear.
   Do not pre-fetch every schema.
4. Fix the source, preserving the planned composition, and recompile until
   blocking errors are clear and `missing_candidates` is empty. Repair order
   and the common causes are in
   `references/authoring/css-and-styling.md` section 9.
5. Save the clean response and its input hashes in `compile-artifact.json`.
6. Call `lexsis_page_create` action `create` with the same fields and
   `publish: false`. Record the page id, version, preview URL and hashes. One
   draft per page: if the manifest already has a page id, patch that draft
   instead of creating a second one.
7. Review the hosted draft at 390px and 1280px. A clean compile proves contract
   safety, not that the page looks right.

## 10. Checklist before you compile

Run this over your own source. Every line is checkable by reading the file.

1. Every section has a `<!-- section: id -->` delimiter and one matching
   `<section id="...">`.
2. Every id is in the canonical vocabulary, kebab-case, unique, and unchanged
   from the last version unless the section's job changed.
3. Section order matches the plan, with announcement, header, nav and footer as
   ordinary sections in place.
4. No `data-island`, no `data-props`, no escaped HTML entities anywhere.
5. Every `<lx-island>` has exactly one `application/json` child, and its props
   match the schema you actually read this session.
6. Every `hydrate` value is the schema's `defaultHydrate` or a preset's.
7. No deprecated island: `BackToTop`, `Carousel`, `CartDrawer`, `Countdown`,
   `FAQ`, `Marquee`, `StatCards`, `Tabs`.
8. One purchase form, one header island, one footer, one announcement bar, one
   sticky bar, one lightbox; `head.use_cart_v2` set and no cart section.
9. Every class is a real Tailwind utility, written mobile first.
10. Every `<style>` rule is scoped by its section id and does one of the five
    jobs in `references/authoring/css-and-styling.md` section 3.
11. No `@import`, no `<script src>`, no Tailwind CDN, no `!important`.
12. Colours, fonts and radii read `--lx-*` or the declared radius tokens; no
    off-brand hex, no Tailwind palette classes.
13. At most one `application/lexsis-motion` module, matching the plan's moment,
    with its capabilities declared; no raw observers, timers or frames.
14. Every `<img>` has alt (or `alt=""` when decorative), `width` and `height`,
    `loading="lazy"` below the fold, and the hero preloaded, not lazy.
15. Every numeral in a proof section appears in the plan's confirmed claims.
16. No emoji, no ALL-CAPS eyebrows beyond the allowance, no `→` on links or
    buttons, no "Shop Now".
17. One `<h1>`; one `<h2>` per section.
18. Text containers are constrained in `ch`, and primary CTAs clear 48px.

## Conflicts found

1. `references/primitives-guide.md` writes islands as `data-island` with
   `data-hydrate`, which is compiled output. Source format is `<lx-island>`
   with `hydrate`. The same file lists `Countdown` as a live island, while its
   schema marks it deprecated in favour of `CountdownTimer`, and routes
   accordions to `data-behavior="accordion"`, while
   `references/workflows/island-selection-workflow.md` routes `faq` to native
   `<details>`.
2. `references/composition-patterns.md` shows compiled `data-island` and
   `data-props` markup in its carousel example, and puts `→` and `←` in button
   text, which N12 forbids. Its section CSS also uses unscoped attribute
   selectors; scope them by section id.
3. `references/scroll-patterns.md` recommends raw `wheel` listeners,
   `setTimeout`, and setting `document.body.style.overflow`. Section JS cannot
   do any of those; that work is a managed motion module or an island.
4. `references/islands/_contract.md` still names islands that are not in the
   catalogue (`TrustBadgeBar`, `PDPInfoCards`, `CompareTable`) and instructs
   alternating section backgrounds plus a default `fadeUp` entrance, which N2
   and N10 forbid. Treat those blocks as static HTML and follow the house
   rules.
