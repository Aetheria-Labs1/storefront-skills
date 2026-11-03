# Source authoring

The compiler owns acceptance of source. House requirements are in
`references/design-rules.md`; CSS is owned by
`references/authoring/css-and-styling.md`. This file owns markup mechanics,
not another style policy or island-selection table.

## Source inputs

Author one source value and pass it directly to MCP. Pass structured `head`,
optional `scripts` and any page-wide `theme_css` separately from the HTML.
`references/source-artifact-workflow.md` owns the direct-input contract and
persisted version evidence; no HTML or CSS file is created.

## Section identity

A section starts at `<!-- section: kebab-case-id -->` and continues to the
next delimiter. Use one matching `<section id="kebab-case-id">` per delimiter.
Ids come from `references/page-types/_checklist-format.md`, including its
suffix convention. Keep ids stable across patches; renaming can break
anchors and version history. Announcement, header, footer and navigation are
ordinary source sections in the declared order, not a hidden renderer shell.

## Island markup

Resolve interactive decisions through
`references/workflows/island-selection-workflow.md`. For the chosen island,
use `<lx-island name="...">` with one readable `application/json` child
containing the props confirmed by its current schema. Use the live schema's
authoring example rather than a static prop map.

Allowed source attributes are `name`, `hydrate`, `class`, `id`, `style`,
and `headless` where supported. Read the hydration default and headless
contract live. A different island's defaults or hooks are not evidence.
Source uses `hydrate`; `data-island`, `data-props` and `data-hydrate` are
compiled renderer markers and are not hand-authored source.

A fallback is one `data-lx-island-fallback` child alongside the JSON child.
It contains readable static information, not a competing purchase handler.
Supported headless behavior is different from fallback content: fetch the
current required hooks, preserve their state contract, and test the result.
Navigation hydration hooks likewise come from the selected live schema.

Cart V2 is enabled by default. Cart behavior comes from the effective
published profile, not a head flag or authored cart section. Required
singleton roles and linked purchase state are resolved in the island-selection
owner.

## Native content

Use semantic HTML for content that does not need an island: disclosures,
comparison tables, static statistics, linked logos and product navigation.
Preserve native keyboard/focus behavior. A radio group needs real labels;
a table needs meaningful headers and an appropriate caption. House A11 owns
control sizing. Native markup is not a license to recreate cart logic.

## Head and external code

- `head.title` contains the real title; approved font stylesheet URLs belong
  in structured `head.fonts`, not CSS imports or section link tags.
- `scripts[]` is for approved integrations and analytics. Animation engines
  use the managed loaders described in `references/animation-system.md`.
- Keep JSON and JSON-LD scripts in their supported HTML locations. Never
  escape a whole section into an HTML string; valid HTML entities in text
  and attribute values remain ordinary HTML.
- Custom motion uses `application/lexsis-motion` under the house budget.
  Follow the managed API contract rather than copying raw timers, global
  DOM access, observers, storage, networking or programmatic clicks into JS.
- Plain top-level section script is compatibility behavior, not a route
  around the compiler's managed-code checks.
- Custom cart, batch add, multiple-product, and guided-selling controls use
  the documented `lx:cart:add-items` event from `section`. Keep the initiating
  element under `data-lx-control`, bind it through the lifecycle API, and
  listen for renderer response events on the same section. Do not create
  hidden commerce islands or drive their controls with `.click()`.

## Section script policy

The compiler and validator enforce these rules. Plan around them before
writing JS:

- **No `window.location`.** Navigate with `lifecycle.navigate(url)`. It allows
  same-origin paths and https URLs without credentials, and returns `false`
  for anything else.
- **No raw observers.** Use `lifecycle.observeMutations` and
  `lifecycle.observeVisibility`. These cannot target nodes inside an island;
  react to island events instead (for example `lx:quiz:result`, or
  `lx:hydrated` once an island mounts).
- **Buttons need a binding in their own section.** A `<button>` must have a
  click listener in the same section's JS, or a registered behaviour. A
  button with `data-lx-open-modal="<key>"` is bound by the Modal runtime, so
  it can open a pop-up that lives in another section.
- **`#hash` links** to an id not on the page are a warning, not an error, so
  you can add a link before the shared section that owns the id is synced.

### Lifecycle API

Section JS receives `section` (the root element) and `lifecycle`. Everything
registered through `lifecycle` is cleaned up with the section.

| Member | Use |
|---|---|
| `root` | The section element. |
| `query(sel)`, `queryAll(sel)` | Find elements in the section. Island internals are excluded. |
| `on(target, type, listener, opts?)` | Add an event listener on the section, its children, `window` or `document`. Returns an unsubscribe function. |
| `timeout(fn, ms)`, `interval(fn, ms)`, `frame(fn)`, `loop(fn, {fps})` | Managed timers. |
| `observeVisibility(targets, cb, opts?)` | Managed `IntersectionObserver`. |
| `observeMutations(target, cb, opts?)` | Managed `MutationObserver`, outside islands only. |
| `navigate(url)` | Navigate with the allow-list above. |
| `cart`, `onCart(cb)` | Cart snapshot and change subscription. |
| `forms.schema(key)`, `forms.submit(key, data, {consent})` | Forms-dashboard forms. `submit` never throws; check `ok`. |
| `store.session`, `store.local`, `store.onChange(cb)` | Store-wide key/value storage (`local` takes `{ttlDays}`). |
| `guard(fn)` | Wrap a callback in the section's error and CPU budget. |
| `addCleanup(fn)`, `setVisible(bool)` | Teardown hook; reveal-state control. |

## Working examples

Each block below compiles cleanly against the current compiler and live
island schemas (checked in CI). Copy the mechanics, not the copy or ids.
Replace placeholder product, variant and image values with resolved catalog
data; never ship them.

A custom control needs `data-lx-control` plus a `click` listener bound
through `lifecycle.query` or `section.querySelector`. An unregistered
`data-behavior` name, a non-click listener alone, or any `document.*` /
`window.*` lookup fails compilation by design.

```html lexsis-example
<!-- section: ingredients -->
<section id="ingredients" class="px-4 py-12">
  <h2 class="text-2xl font-semibold">What's inside</h2>
  <button type="button" data-lx-control="ingredients-toggle" aria-expanded="false" class="min-h-[48px] underline">Show full list</button>
  <ul data-ingredients hidden class="mt-4 list-disc pl-5"><li>Coconut oil</li></ul>
  <script>
    const toggle = lifecycle.query('[data-lx-control="ingredients-toggle"]');
    toggle.addEventListener("click", () => {
      const list = section.querySelector("[data-ingredients]");
      list.hidden = !list.hidden;
      toggle.setAttribute("aria-expanded", String(!list.hidden));
    });
  </script>
</section>
```

A vertical offer selector is `QuantityBreaks` with `variant: "list"` (stacked
rows, smallest quantity first). Set `showCta: false` with `emitEvents: true`
when a BuyBox owns the add-to-cart button. Prices are labels; a repeated-unit
discount also needs a cart-profile promotion (`promotionRef`).

```html lexsis-example
<!-- section: offer -->
<section id="offer" class="px-4 py-12">
  <h2 class="text-2xl font-semibold">Choose your pack</h2>
  <lx-island name="QuantityBreaks">
    <script type="application/json">{"variant":"list","variantId":"gid://shopify/ProductVariant/1","currency":"INR","tiers":[{"quantity":1,"price":"₹349","perUnit":"₹349 each"},{"quantity":2,"price":"₹649","perUnit":"₹325 each","badge":"Most picked"}]}</script>
  </lx-island>
</section>
```

A responsive product gallery uses `ProductGallery`: `layout` sets desktop
(here a vertical thumbnail rail on the left), `mobileLayout: "swipe"` sets a
swipe rail below `md`. Give every image real `alt` text.

```html lexsis-example
<!-- section: gallery -->
<section id="gallery" class="px-4 py-8">
  <h2 class="sr-only">Product photos</h2>
  <lx-island name="ProductGallery">
    <script type="application/json">{"layout":"vertical","thumbPosition":"left","mobileLayout":"swipe","navigation":"arrows","media":[{"type":"image","src":"https://cdn.shopify.com/s/files/1/0000/0001/files/oil-front.jpg","alt":"Baby oil bottle, front"},{"type":"image","src":"https://cdn.shopify.com/s/files/1/0000/0001/files/oil-back.jpg","alt":"Baby oil bottle, ingredients label"}]}</script>
  </lx-island>
</section>
```

## Compile handoff

Write complete source, then follow `references/generation-protocol.md` for
exact-input compilation, repair, draft creation or versioned editing. A clean
compile does not prove visual quality. Hosted design review and production
readiness follow `references/qa-recipe.md`.
