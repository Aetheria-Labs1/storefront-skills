# CSS and styling

The compiler accepts or rejects CSS and utilities. House visual and
accessibility rules live in `references/design-rules.md`; do not weaken
them through a theme, template, preset or component default.

## 1. Cascade and ownership

The cascade is theme CSS, generated Tailwind utilities, then section CSS in
page order. The renderer supplies its reset and base styles; do not duplicate
them. The page-wide `theme_css` value owns theme tokens, the plan's radius/type scales,
page-wide focus styles and reduced-motion handling. Literal utility classes
own layout, spacing, sizing, responsive behavior and state styling.
Section CSS is exceptional and always scoped to its section id.

## 2. Utilities first

Author mobile first using literal classes supported by the compiler. Do not
construct class names at runtime, add a Tailwind CDN, or invent unconfigured
utilities. Resolve every `missing_candidates` entry rather than assuming it
will render. The house rules own the spacing/type scales and permitted
state feedback; this file does not define another set of values.

## 3. Section CSS jobs

Use section CSS only for geometry utilities cannot express, visual overrides
of schema-declared parts/variables, the plan's named motion, a feature-query
fallback, or a scoped print/RTL adjustment. Complex named-grid geometry can
need CSS; ordinary columns and breakpoints remain utilities.

Every selector begins with the section id. Scope each selector in a comma
list separately. Keyframes have unique section-qualified names. Never add
page-global element selectors, a second container system, or `!important`.
Tokens belong in the theme; do not redefine brand variables inside sections.

## 4. Tokens and contrast

Use the theme's verified `--lx-*` values and plan-declared object radius
tokens. `--lx-text-muted` is the secondary text pairing; opacity on primary
text is not a substitute for a contrast-checked color. A7 owns contrast.
N2 owns surfaces and its exhaustive exceptions. N7 owns effects; no accent
glow is allowed under the name of a neutral shadow.

An inline reference to a theme token is valid, as is an approved image focal
point. Do not use inline styles to rebuild layout already covered by
utilities. A page-level token override belongs in `theme_css` and must
still satisfy the house requirements and binding rules.

## 5. Island styling

Discover `parts` and `css_vars` from `lexsis_design.island_schema` for the
selected component. Prefer its supported CSS variables for geometry; use
scoped part selectors for visual properties. Do not assume another island
has the same parts. Do not target implementation classes or override an
island's internal layout with `display`, positioning or a new grid.

After the live schema confirms the part, a visual override can be:

```css
#buy-box [data-part="cta"] { border-radius: var(--r-control); }
```

A saved preset label is visual intent, not frozen configuration. Resolve the
actual props and styling now; record the result and any intentional departure
in the workspace. Do not paste a static per-island prop or hydration table.

## 6. Responsive and accessible implementation

Follow A3/A4/A7/A11 for type, measure, contrast and interaction sizing.
A11's 48px minimum governs every authored tap target; external 24px or 44px
floors do not reduce it. Review at the workflow's specified widths, including
390px and 1280px for hosted design approval. Use native scrolling rather than
clipping content or intercepting input. Preserve visible keyboard focus.

## 7. Motion and repair

N10 owns the motion budget. `references/animation-system.md` owns managed
motion syntax and runtime APIs. A shared renderer animation is not permission
to deploy a banned effect. Static content remains visible when motion fails.

When styling fails: check source syntax, the compiler's missing utilities,
selector scope, live schema parts and CSS variables, then cascade order.
Fix the owning layer rather than escalating specificity or patching compiled
output. Recompile the exact inputs and inspect the hosted result.
