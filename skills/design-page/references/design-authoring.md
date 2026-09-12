# Lexsis Page Authoring

Use this guide only after `PLAN_APPROVED` and `ASSETS_READY`.

## Precedence

1. Merchant rules and verified legal constraints.
2. Approved page plan and visual decisions.
3. Selected theme tokens and exact `design.md`.
4. Lexsis house authoring rules below.
5. Template source as a starting structure.

If theme values conflict with approved merchant rules or make required text
fail accessible contrast, stop with the conflicting values. Do not silently
invent replacement brand tokens.

## Composition

- Preserve the plan's section order and consumer decision jobs.
- Use one page background system and one planned bold moment.
- Prefer deliberate grids, editorial compositions, and useful whitespace over
  repeated generic cards, pills, icon tiles, and decorative bands.
- Recompose hierarchy for 390 rather than shrinking the desktop layout.
- Keep one clear primary action on single-goal pages.
- Use motion only for the approved state, sequence, or emphasis.
- Use approved concepts as visual evidence, not page media.

## Templates and Sections

- `page-kit`: resolve the approved kit with
  `lexsis_template_library.get_kit`, then fetch only its selected section
  source through `lexsis_design.get_section`.
- `sections`: fetch only the approved section ids.
- saved merchant section: use `lexsis_template_library.get_mine` for its
  approved id.
- `custom`: author the planned layout directly.

Template source may be adapted to the approved content and design. It does not
override section order, final copy, proof, offers, assets, or responsive intent.

## Islands

Use ordinary semantic HTML for static content. Use `<lx-island>` only for a
planned interaction supported by the current renderer.

1. Read `lexsis_design.islands`.
2. Select the smallest island that fulfils the planned behaviour.
3. Read `lexsis_design.island_schema` for that island.
4. Follow its current source example, required hooks, props, hydration, and
   supported headless mode.
5. Keep props schema-valid and bind current product, variant, review, or
   collection ids.

Do not fetch every schema, imitate deprecated components, duplicate managed
cart state, or add custom global event handlers where the island contract
already owns the behaviour.

## Source and CSS

- Author one complete editable source value with stable section ids.
- Keep section-specific CSS beside its section.
- Put shared page-wide tokens, typography, backgrounds, accessibility, and
  responsive rules in `theme_css`.
- Use Lexsis theme variables for brand values.
- Use compiler-supported Tailwind utilities only; there is no runtime
  Tailwind CDN.
- Keep JavaScript limited to behaviour that is not already managed by an
  island.
- Include visible focus, keyboard operation, reduced-motion handling, and
  48px authored tap targets.
- Avoid emoji as interface icons. Use supported icons, inline SVG, or CSS.
- Header, announcement, navigation, main content, and footer appear once in
  source order.

## Copy, Proof, and Offers

- Place approved customer-facing copy verbatim.
- A wording change, new claim, new CTA, or new policy statement returns to
  `/plan-page`.
- Render only approved claim rows and their approved safe treatments.
- Render quotations verbatim with stored attribution.
- Ratings, review counts, prices, compare-at prices, stock, urgency, delivery,
  guarantees, and offer terms come from approved rows and refreshed live data.
- Review components use current product or collection ids and real totals.
- Press, certification, payment, and partner marks use only the verified
  production bindings.

## Production Assets

Use only rows from the `ASSETS_READY` binding table.

- Keep product and variant identity exact.
- Apply the recorded desktop/mobile crop and focal point.
- Use descriptive alt text for informative media and empty alt for decorative
  media.
- Preload the hero; lazy-load below-fold images.
- Video is click-to-play or an approved muted loop, with a real poster,
  captions, and controls.
- Never use a concept URL, transient output, placeholder, filename guess, or
  unbound library asset.

If a bound asset is inaccessible, unsuitable in the actual layout, or fails
identity/rights requirements, return the slot to `/plan-assets`.

## Compile Contract

Compile complete source, head, `theme_css`, scripts, bindings, and runtime
dependencies together. Repair source from compiler findings. A clean compile
id can create one unpublished draft. Compile ids and direct source are
mutually exclusive page-creation input modes.
