# Design Rules

House rules for every generated page. They override generated brand `design.md`
guidance and brand-kit preview blueprints. Record every override in
`page plan` under "Overrides of brand design.md".

Loaded by `/plan-page` (Design direction block), `/design-page` (Design Direction
Gate and hosted review) and `/optimize` (Scorecard).
Review the persisted MCP source and hosted draft. No local QA script or
page-file workflow is required.

## Precedence

```text
house rules (storefront-engine/references/design-rules.md)
  > merchant-stated brand rules (voice_md, banned_phrases, explicit owner notes in brand-design.md)
    > brand-kit token VALUES (colours, fonts, radii, spacing)
      > generated design.md guidance (intent, component patterns, do/don't)
        > brand-kit preview blueprint and island presets (illustrative only)
```

Rules for applying it:

1. A lower layer may narrow a higher layer (pick one of the allowed icon sets) but never widen it (re-enable emoji).
2. Token values win over design.md prose for values, except where the value fails WCAG AA against its documented pairing; then return `THEME_CONTEXT_CONFLICT` with both values. Conflicts are raised for values only, never for style guidance.
3. "Mandated by the brand guide" (the ALL-CAPS exception in N5) means merchant-stated only. Anything the generator inferred from screenshots is tagged `[observed]` and cannot unlock an exception.

## 2. Design rules for generated storefront pages

Format per rule: imperative sentence, rationale and hosted/MCP acceptance
check. Inspect the persisted source through MCP and the actual hosted DOM,
styles and interactions; never inject diagnostic code into section source.

### 2.1 NEVER

N1. Never use emoji by default, and never as icons: not in tickers, trust strips, badges, buttons, alt text, island JSON props or CSS `content`. Emoji may appear in copy only when the user explicitly insists; record it in `page plan` under "Design direction > Emoji in copy" with the merchant's wording, and keep every occurrence inside running text. When the page needs icons and no inline SVG set fits, generate a monochrome SVG icon set (one stroke, one size); never substitute emoji.
Rationale: glyphs render differently per OS vendor, ignore `currentColor` and stroke weight, are announced by Unicode name to screen readers, and are the most recognised marker of AI-generated pages (Miller et al. 2018; uxskill).
Check (hosted/MCP): Inspect visible copy, alt text, props and CSS content for emoji. None may be icons; any copy-only exception must match the merchant's recorded wording.

N2. Never change the background from section to section. The page has one background, `--lx-bg-color`, from below the navbar to above the footer. Allowed exceptions, exhaustively: the announcement bar, the navbar, the footer, and at most one full-bleed moment that `page plan` names under "Design direction > Bold moment". A `<section>` or any full-width wrapper painted `--lx-bg-surface`, `--lx-surface-alt` or `--lx-secondary-color` is a band and fails, even if it is white.
Rationale: bands are a template's way of faking structure; separation belongs to spacing, type scale and hairlines (NN/g grouping; Stellae). Alternating fills are also the reason the rejected page read as five stacked templates.
Check (hosted/MCP): At each viewport, inspect full-width backgrounds. Only chrome and the single plan-named full-bleed exception may differ from the page background.

N3. Never use emoji, images or mixed libraries as icons. Icons are one inline SVG set, one stroke weight, `stroke="currentColor"`, `fill="none"`, one size per context, `aria-hidden="true"` with a visible text label. Or no icons.
Rationale: two stroke languages on one screen is a tell; icons that garnish headings are skipped by readers (uxskill icons).
Check (hosted/MCP): Inspect rendered icons and persisted markup: one SVG set, one stroke weight, currentColor, no image icons, hidden decorative SVGs and visible labels.

N4. Never use more than two type families. A non-Latin script gets one matching family declared with `[lang]`; it does not count.
Rationale: one display face plus one workhorse is the ceiling for coherence (frontend-design; Shopify Theme Store "Consistent typography").
Check (hosted/MCP): Inspect computed font families and loaded font stylesheets. At most two families plus the declared non-Latin family.

N5. Never set eyebrow labels in ALL-CAPS unless a merchant-stated brand rule (not a generator-observed one) requires it, and then at most one per three sections.
Rationale: the tracked-out caps eyebrow above every heading is the highest-frequency AI tell (designer-skill avoid-ai-slop; frontend-design).
Check (hosted/MCP): Inspect eyebrow labels. No uppercase without a merchant-stated rule; an authorized exception appears at most once per three sections.

N6. Never accent a single word or phrase inside a headline with colour, italic, weight or underline.
Rationale: the one-word accent is a default treatment, not a decision (frontend-design).
Check (hosted/MCP): Inspect each headline's child spans and computed styles. No word-level accent treatment.

N7. Never use gradient washes, glow shadows, shimmer, pulse, float, animated backgrounds, or `hover:scale` / `hover:-translate` / `hover:scale-1xx` on cards, buttons or images. The only permitted gradient is a black-to-transparent overlay on a photograph for text legibility inside the plan-named bold moment.
Rationale: gradient + hover-lift is the SaaS-card kit that reads as generated regardless of brand (Sailop; frontend-design).
Check (hosted/MCP): Inspect source and rendered effects at rest and on hover. No banned effects; only the plan-named photographic legibility overlay may use a gradient.

N8. Never wrap plain text in a card. A card (`--lx-bg-surface`, border, or shadow with radius) surrounds a distinct object only: a product, a proof artefact with an image, a table, a form, a quoted review. Paragraphs, lists and FAQs sit on the page background.
Rationale: identical rounded cards chop content into interchangeable units and signal that nothing is more important than anything else (uxskill tells; NN/g common region "use sparingly").
Check (hosted/MCP): At desktop and mobile, count cards containing only paragraphs/lists/FAQs: zero. Every card surrounds a permitted distinct object.

N9. Never render discount or status pills in ALL-CAPS or with percentages ("31% OFF", "BEST VALUE", "MOST POPULAR", "NEW ARRIVALS") unless the merchant runs a named sale recorded in the plan's confirmed claims. Compare-at price is struck-through text only.
Rationale: the OFF pill and the highlighted middle tier are stock conversion-template chrome; Baymard's guidance is to show the price and compare-at clearly, not to shout.
Check (hosted/MCP): Inspect offer/status treatments. No prohibited pills; any named-sale exception is evidenced in confirmed claims and prices follow the offer ledger.

N10. Never add motion that is not answering a user action, except one orchestrated moment named in the plan. No fade-up per section, no stagger, no counters, no parallax, no marquee ticker unless the announcement bar's own island provides it. Custom motion must follow `animation-system.md` and use `application/lexsis-motion`, not raw observers, timers, or global DOM access.
Rationale: scattered entrance effects are the generic default; one moment lands, ten do not (frontend-design; Sailop).
Check (hosted/MCP): Inspect motion blocks and hosted behavior with reduced motion enabled and disabled. Non-interaction motion is limited to the single plan-named moment; no raw observers, timers or global DOM recipes are authored.

N11. Never show proof you cannot source: star glyphs, review counts, customer counts, "Only N left", countdowns, "as seen in" logos. Every number in a proof section traces to "Claims confirmed" in the plan.
Rationale: fabricated proof destroys trust and is itself a tell (five gold stars + round avatar + italic quote). `references/proof/reviews-sourcing.md` owns reviewer and quotation evidence.
Check (hosted/MCP): List every visible proof numeral, count, logo and testimonial. Match each to confirmed evidence and its proof-ledger row.

N12. Never append `U+2192` or `U+00BB` to link and button text, join meta strings with middle dots, or place an icon in a rounded tile above a heading (icon-tile-stack).
Rationale: template chrome that appears whatever the subject (frontend-design; designer-skill).
Check (hosted/MCP): Inspect link/button labels and heading ornaments. No U+2192 or U+00BB suffixes, middle-dot meta chains or icon-tile headings.

N13. Never mix radii on the same object type or use one radius on everything. Declare a radius scale by object type and use only those tokens.
Rationale: uniform `rounded-2xl` on cards, buttons, inputs and images is the absence of a system (Sailop "rounded-2xl on everything").
Check (hosted/MCP): Compare computed radii by object type to the declared radius tokens; no stray values or universal radius.

N14. Never hardcode off-brand hex or Tailwind default colours. Colours come from `--lx-*` tokens or the plan's named palette.
Rationale: default colours such as `#667eea`, `#764ba2`, `#8b5cf6`, `#f9fafb`, and `text-yellow-400` mark a page as templated rather than merchant-specific (uxskill tells).
Check (hosted/MCP): Compare computed colors and source values to the selected theme and plan palette; no off-brand defaults.

### 2.2 ALWAYS

A1. Always write the Design direction block in `page plan` before any HTML: palette of 4 to 6 named hex with roles; type roles, families and one modular ratio; layout concept in one sentence plus an ASCII wireframe at 1280 and 390; alignment rule; icon decision; the one bold moment; the background rule with its single named exception or "none"; motion decision; the generic-default check with at least three concrete differences; the list of brand-design.md lines being overridden.
Rationale: the plan-review-build-critique loop is what stops the model averaging toward the centre of its training data (frontend-design).
Check (hosted/MCP): The plan contains all ten Design direction fields, with no empty or TBD value, before source authoring.

A2. Always separate sections with a spacing scale and, where a break is needed, one 1px hairline in `--lx-border-color`. Use one 8-point scale; section padding comes from at most two pairs (e.g. 64/96 and 40/56 mobile/desktop).
Rationale: proximity and whitespace carry grouping; a line is a subtle, universally understood divider; colour is emotional and should be spent on pacing, not plumbing (NN/g; Stellae; Tubik).
Check (hosted/MCP): Measure section spacing at mobile and desktop: one 8-point scale, at most two padding pairs and only the specified hairline where needed.

A3. Always build hierarchy with a single modular type scale (one ratio, 1.2 to 1.333 for commerce), no more than three sizes visible on one screen, one `<h1>`, one `<h2>` per section, headings 1.1 to 1.2 line-height, body 1.5 to 1.7.
Rationale: three sizes give hierarchy without noise; NN/g and accessibility.build converge on this.
Check (hosted/MCP): Inspect heading count, computed sizes and line heights against the declared ratio. One h1, one h2 per section and no more than three sizes per screen.

A4. Always keep body measure between 45 and 80 characters at every viewport; give serif body 0.05 more line-height than sans. Constrain text containers with `max-width` in `ch` (60 to 70ch), not px.
Rationale: WCAG 1.4.8 caps body at 80 characters; legibility research centres on 45 to 75 (Butterick 45 to 90).
Check (hosted/MCP): Inspect body measure at each viewport: 45 to 80 characters, 60 to 70ch containers, and the required serif line-height adjustment.

A5. Always record one icon decision in the plan and, if icons exist, ship them as one inline SVG set at one size and one stroke, with the text label always visible.
Rationale: see N3.
Check (hosted/MCP): Match the rendered SVG set and visible labels to the plan's icon decision and N3.

A6. Always declare a radius scale by object type in `theme_css` (`--r-control`, `--r-card`, `--r-media`, `--r-pill`) and use only those tokens.
Rationale: the relationship between radii is the design.
Check (hosted/MCP): Inspect effective theme CSS and rendered radii: every object uses its declared --r-control, --r-card, --r-media or --r-pill token.

A7. Always meet WCAG 2.2 AA: 4.5:1 for text under 24px (18.67px bold), 3:1 for large text and for UI component boundaries, including muted text on the page background, accent on any tint, and button text on button fill.
Rationale: W3C 1.4.3 and 1.4.11; the RudraSetu guide itself flags #D52600 on #FBE9E6 as borderline.
Check (hosted/MCP): Measure actual foreground/background pairs, including muted text and buttons over imagery: at least 4.5:1 for normal text and 3:1 for large text and component boundaries.

A8. Always compose the PDP buy section to Baymard and Shopify requirements: untruncated title, price and compare-at, unit price if applicable, variant options as buttons, quantity, add-to-cart, a shipping and returns line, all within the first viewport on desktop and within 1.5 viewports at 390px; product media takes 50 to 60 percent of desktop width.
Rationale: users decide on the PDP; hidden price or delivery cost is a top abandonment cause (Baymard PDP research; Shopify Theme Store product page requirements).
Check (hosted/MCP): On the hosted PDP, verify all required buying controls within one desktop viewport and 1.5 mobile viewports at 390px, with media at 50 to 60 percent of desktop width.

A9. Always spend boldness once. Name the single memorable element in the plan; every other element is quiet: page background, body weight, hairlines, sentence case.
Rationale: one element can be remembered; the mirror test, remove one accessory (frontend-design; Chanel).
Check (hosted/MCP): The desktop and mobile squint test isolates the one plan-named bold element, not several competing accessories.

A10. For production-ready work, always run the hosted design review at 390 and 1280 before recording design approval. Fast drafts return `DRAFT_CREATED` first and may leave this review pending.
Rationale: the real renderer catches banding, hierarchy, hydration, and media problems without maintaining a second preview runtime.
Check (hosted/MCP): Record hosted preview URL, tested version and screenshots at 390 and 1280 with no blocking failure before design approval.

A11. Always ship the quality floor without announcing it: `:focus-visible` styles, `prefers-reduced-motion` handling, 48px minimum tap targets, alt text on product media, `lang` attributes on non-Latin text.
Check (hosted/MCP): Test keyboard focus, reduced motion, all 48px tap targets, media alternatives and language attributes on the hosted draft.

A12. Always write copy as design content: sentence case, active voice, the CTA says what happens ("Add to cart", not "Shop Now U+2192"), no placeholder or invented copy, brand voice from `voice_md` or the merchant.
Check (hosted/MCP): Read rendered copy and controls against the plan and brand voice. No generic action labels, placeholder content or invented facts.

## Tells (fail the squint test)

Cream page + high-contrast serif + terracotta accent as the only idea; identical rounded cards with one radius and one grey shadow; tracked-out ALL-CAPS eyebrow above every heading; meta strings joined with middle dots; `WORD  -  fragment` labels; `U+2192` appended to links and buttons; icon in a rounded tile above every heading; discount pills and "MOST POPULAR" ribbons; gradient washes; fade-up on every section; five gold stars with a round avatar and an italic quote; a monospace face for small labels; near-black `#0B0B0B` standing in for black.

Source audit: internal design-rules research (2026-09-05).
