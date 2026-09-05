# Design Rules

House rules for every generated page. They override generated brand `design.md`
guidance and brand-kit preview blueprints. Record every override in
`page-plan.md` under "Overrides of brand design.md".

Loaded by `/plan-page` (Design direction block), `/design-page` (Design Direction
Gate and Self-Critique Gate), `/generate` (Production Gate) and `/optimize`.
`design-page/scripts/design_lint.py <workspace>` runs the static checks and prints
the results table.

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

Format per rule: imperative sentence; rationale; a check the agent can run. Checks are written for macOS (BSD grep has no `-P`; use `perl -CSD`). `$W` is the page workspace, e.g. `work/visual-pages/<handle>`. Browser checks run in the preview via the browser tool's evaluate call.

### 2.1 NEVER

N1. Never use emoji by default, and never as icons: not in tickers, trust strips, badges, buttons, alt text, island JSON props or CSS `content`. Emoji may appear in copy only when the user explicitly insists; record it in `page-plan.md` under "Design direction › Emoji in copy" with the merchant's wording, and keep every occurrence inside running text. When the page needs icons and no inline SVG set fits, generate a monochrome SVG icon set (one stroke, one size); never substitute emoji.
Rationale: glyphs render differently per OS vendor, ignore `currentColor` and stroke weight, are announced by Unicode name to screen readers, and are the most recognised marker of AI-generated pages (Miller et al. 2018; uxskill).
Check:
```bash
perl -CSD -ne 'while(/([\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}\x{2B00}-\x{2BFF}\x{2300}-\x{23FF}\x{1F1E6}-\x{1F1FF}\x{FE0F}\x{200D}\x{203C}\x{2049}])/g){print "$ARGV:$.: $1\n"}' $W/lexsis-source.html $W/page-theme.css | wc -l   # 0, unless page-plan.md records "Emoji in copy: allowed"; then every hit must be inside copy, none as an icon
```

N2. Never change the background from section to section. The page has one background, `--lx-bg-color`, from below the navbar to above the footer. Allowed exceptions, exhaustively: the announcement bar, the navbar, the footer, and at most one full-bleed moment that `page-plan.md` names under "Design direction › Bold moment". A `<section>` or any full-width wrapper painted `--lx-bg-surface`, `--lx-surface-alt` or `--lx-secondary-color` is a band and fails, even if it is white.
Rationale: bands are a template's way of faking structure; separation belongs to spacing, type scale and hairlines (NN/g grouping; Stellae). Alternating fills are also the reason the rejected page read as five stacked templates.
Check (browser):
```js
(() => { const body = getComputedStyle(document.body).backgroundColor, vw = document.documentElement.clientWidth;
  return [...document.querySelectorAll('body *')].filter(el => { const cs = getComputedStyle(el);
    return cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== body && el.getBoundingClientRect().width >= vw - 2 && el.getBoundingClientRect().height > 40; })
    .map(el => ({ el: el.id || el.className || el.tagName, bg: getComputedStyle(el).backgroundColor })); })()
```
Pass when the list contains only announcement, nav, footer elements and at most one element whose id matches the plan's bold moment.

N3. Never use emoji, images or mixed libraries as icons. Icons are one inline SVG set, one stroke weight, `stroke="currentColor"`, `fill="none"`, one size per context, `aria-hidden="true"` with a visible text label. Or no icons.
Rationale: two stroke languages on one screen is a tell; icons that garnish headings are skipped by readers (uxskill icons).
Check:
```bash
grep -o 'stroke-width="[^"]*"' $W/lexsis-source.html | sort -u | wc -l   # 0 or 1
grep -c '<img[^>]*class="[^"]*icon' $W/lexsis-source.html                 # 0
```

N4. Never use more than two type families. A non-Latin script gets one matching family declared with `[lang]`; it does not count.
Rationale: one display face plus one workhorse is the ceiling for coherence (frontend-design; Shopify Theme Store "Consistent typography").
Check:
```bash
grep -oE "family=[A-Za-z+]+" $W/page-theme.css | sort -u | wc -l          # <= 3 including the [lang] family
```

N5. Never set eyebrow labels in ALL-CAPS unless a merchant-stated brand rule (not a generator-observed one) requires it, and then at most one per three sections.
Rationale: the tracked-out caps eyebrow above every heading is the highest-frequency AI tell (designer-skill avoid-ai-slop; frontend-design).
Check:
```bash
grep -cE 'uppercase|text-transform:\s*uppercase' $W/lexsis-source.html $W/page-theme.css   # 0, or <= ceil(sections/3) with a stated rule
```

N6. Never accent a single word or phrase inside a headline with colour, italic, weight or underline.
Rationale: the one-word accent is a default treatment, not a decision (frontend-design).
Check:
```bash
perl -0ne 'print scalar(() = /<h[1-3][^>]*>[^<]*<(span|em|strong|i|b|mark)/g), "\n"' $W/lexsis-source.html   # 0
```

N7. Never use gradient washes, glow shadows, shimmer, pulse, float, animated backgrounds, or `hover:scale` / `hover:-translate` / `hover:scale-1xx` on cards, buttons or images. The only permitted gradient is a black-to-transparent overlay on a photograph for text legibility inside the plan-named bold moment.
Rationale: gradient + hover-lift is the SaaS-card kit that reads as generated regardless of brand (Sailop; frontend-design).
Check:
```bash
grep -nE 'gradient\(|bg-gradient|shimmer|animate-pulse|pulseRing|float-|hover:scale|hover:-translate|scale\(1\.[0-9]|box-shadow:\s*0 0 ' $W/lexsis-source.html $W/page-theme.css | wc -l   # 0, or only the plan-named overlay
```

N8. Never wrap plain text in a card. A card (`--lx-bg-surface`, border, or shadow with radius) surrounds a distinct object only: a product, a proof artefact with an image, a table, a form, a quoted review. Paragraphs, lists and FAQs sit on the page background.
Rationale: identical rounded cards chop content into interchangeable units and signal that nothing is more important than anything else (uxskill tells; NN/g common region "use sparingly").
Check: for each element matching `\.rs-card|bg-surface|rounded-[a-z0-9]+.*shadow`, confirm it contains `<img`, `<table`, `<form`, `<blockquote` or a price. Manual pass on the 1280 screenshot; count cards that contain only text; must be 0.

N9. Never render discount or status pills in ALL-CAPS or with percentages ("31% OFF", "BEST VALUE", "MOST POPULAR", "NEW ARRIVALS") unless the merchant runs a named sale recorded in the plan's confirmed claims. Compare-at price is struck-through text only.
Rationale: the OFF pill and the highlighted middle tier are stock conversion-template chrome; Baymard's guidance is to show the price and compare-at clearly, not to shout.
Check:
```bash
grep -nE '\b[0-9]{1,2}% ?OFF\b|BEST VALUE|MOST POPULAR|LIMITED TIME|NEW ARRIVAL' $W/lexsis-source.html | wc -l   # 0
```

N10. Never add motion that is not answering a user action, except one orchestrated moment named in the plan. No fade-up per section, no stagger, no counters, no parallax, no marquee ticker unless the announcement bar's own island provides it.
Rationale: scattered entrance effects are the generic default; one moment lands, ten do not (frontend-design; Sailop).
Check:
```bash
grep -cE 'data-reveal|IntersectionObserver|@keyframes|animation:' $W/lexsis-source.html $W/page-theme.css   # 0, or exactly the plan-named moment
grep -c 'prefers-reduced-motion' $W/page-theme.css   # 1 if any animation exists
```

N11. Never show proof you cannot source: star glyphs, review counts, customer counts, "Only N left", countdowns, "as seen in" logos. Every number in a proof section traces to "Claims confirmed" in the plan.
Rationale: fabricated proof destroys trust and is itself a tell (five gold stars + round avatar + italic quote). The engine's own `generate-pdp.md` line 64 already says never invent reviewers.
Check: list every numeral in sections tagged proof/trust/reviews; each must appear in `page-plan.md` under confirmed claims.

N12. Never append `→` or `»` to link and button text, join meta strings with middle dots, or place an icon in a rounded tile above a heading (icon-tile-stack).
Rationale: template chrome that appears whatever the subject (frontend-design; designer-skill).
Check:
```bash
grep -cE '(→|&rarr;|»)\s*</(a|button)' $W/lexsis-source.html   # 0
grep -cE 'w-1[0-6] h-1[0-6][^"]*rounded' $W/lexsis-source.html   # 0
```

N13. Never mix radii on the same object type or use one radius on everything. Declare a radius scale by object type and use only those tokens.
Rationale: uniform `rounded-2xl` on cards, buttons, inputs and images is the absence of a system (Sailop "rounded-2xl on everything").
Check:
```bash
grep -ohE 'border-radius:\s*[^;]+|rounded(-[a-z0-9\[\]]+)?' $W/lexsis-source.html $W/page-theme.css | sort | uniq -c | sort -rn   # <= 4 distinct values, each mapped to a type in page-theme.css comments
```

N14. Never hardcode off-brand hex or Tailwind default colours. Colours come from `--lx-*` tokens or the plan's named palette.
Rationale: `#667eea`, `#764ba2`, `#8b5cf6`, `#f9fafb`, `text-yellow-400` appear throughout the engine references and mark a page as templated (uxskill tells).
Check:
```bash
grep -nEi '#667eea|#764ba2|#8b5cf6|#f9fafb|#6366f1|#7c3aed|text-(yellow|gray|slate|purple|indigo)-[0-9]' $W/lexsis-source.html $W/page-theme.css | wc -l   # 0
```

### 2.2 ALWAYS

A1. Always write the Design direction block in `page-plan.md` before any HTML: palette of 4 to 6 named hex with roles; type roles, families and one modular ratio; layout concept in one sentence plus an ASCII wireframe at 1280 and 390; alignment rule; icon decision; the one bold moment; the background rule with its single named exception or "none"; motion decision; the generic-default check with at least three concrete differences; the list of brand-design.md lines being overridden.
Rationale: the plan-review-build-critique loop is what stops the model averaging toward the centre of its training data (frontend-design).
Check: `grep -c '^\*\*' page-plan.md` under "## Design direction" returns all 10 field labels from the template in section 3.1; none is empty or "TBD".

A2. Always separate sections with a spacing scale and, where a break is needed, one 1px hairline in `--lx-border-color`. Use one 8-point scale; section padding comes from at most two pairs (e.g. 64/96 and 40/56 mobile/desktop).
Rationale: proximity and whitespace carry grouping; a line is a subtle, universally understood divider; colour is emotional and should be spent on pacing, not plumbing (NN/g; Stellae; Tubik).
Check: `grep -oE 'padding:\s*[0-9]+px' $W/page-theme.css | sort -u` yields values from the 8-pt scale only; `grep -c 'border-top: 1px solid var(--lx-border-color)'` is the only divider mechanism.

A3. Always build hierarchy with a single modular type scale (one ratio, 1.2 to 1.333 for commerce), no more than three sizes visible on one screen, one `<h1>`, one `<h2>` per section, headings 1.1 to 1.2 line-height, body 1.5 to 1.7.
Rationale: three sizes give hierarchy without noise; NN/g and accessibility.build converge on this.
Check: `grep -c '<h1' $W/lexsis-source.html` is 1; every `font-size` in `page-theme.css` is a step of the declared ratio (list them: `grep -oE 'font-size:\s*[^;]+' | sort -u`).

A4. Always keep body measure between 45 and 80 characters at every viewport; give serif body 0.05 more line-height than sans. Constrain text containers with `max-width` in `ch` (60 to 70ch), not px.
Rationale: WCAG 1.4.8 caps body at 80 characters; legibility research centres on 45 to 75 (Butterick 45 to 90).
Check (browser, 1280):
```js
(() => [...document.querySelectorAll('p, li, figcaption')].map(p => ({ t: p.textContent.trim().slice(0,40), cpl: Math.round(p.getBoundingClientRect().width / (parseFloat(getComputedStyle(p).fontSize) * 0.5)) })).filter(x => x.cpl > 80))()   // []
```

A5. Always record one icon decision in the plan and, if icons exist, ship them as one inline SVG set at one size and one stroke, with the text label always visible.
Rationale: see N3. Check: as N3, plus `grep -c 'aria-hidden="true"'` equals the SVG count.

A6. Always declare a radius scale by object type in `page-theme.css` (`--r-control`, `--r-card`, `--r-media`, `--r-pill`) and use only those tokens.
Rationale: the relationship between radii is the design. Check: `grep -c 'border-radius: var(--r-' $W/page-theme.css $W/lexsis-source.html` equals the total count of `border-radius` declarations.

A7. Always meet WCAG 2.2 AA: 4.5:1 for text under 24px (18.67px bold), 3:1 for large text and for UI component boundaries, including muted text on the page background, accent on any tint, and button text on button fill.
Rationale: W3C 1.4.3 and 1.4.11; the RudraSetu guide itself flags #D52600 on #FBE9E6 as borderline.
Check:
```bash
python3 - <<'PY'
def L(h):
    r,g,b=[int(h.lstrip('#')[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def ratio(a,b):
    x,y=sorted([L(a),L(b)],reverse=True); return round((x+0.05)/(y+0.05),2)
pairs={'text/page':('#1F1D24','#F5F0E6'),'muted/page':('#6B6560','#F5F0E6'),'accent/page':('#D52600','#F5F0E6'),'accent/tint':('#D52600','#FBE9E6'),'cream/charcoal btn':('#F5F0E6','#1F1D24'),'cream/maroon bar':('#F5F0E6','#8B1A00')}
for k,(a,b) in pairs.items(): print(k, ratio(a,b))
PY
```
Every text pair >= 4.5, every large-text or component pair >= 3.

A8. Always compose the PDP buy section to Baymard and Shopify requirements: untruncated title, price and compare-at, unit price if applicable, variant options as buttons, quantity, add-to-cart, a shipping and returns line, all within the first viewport on desktop and within 1.5 viewports at 390px; product media takes 50 to 60 percent of desktop width.
Rationale: users decide on the PDP; hidden price or delivery cost is a top abandonment cause (Baymard PDP research; Shopify Theme Store product page requirements).
Check: at 390 screenshot, price and add-to-cart appear above y = 1266px; at 1280, both appear above y = 800px.

A9. Always spend boldness once. Name the single memorable element in the plan; every other element is quiet: page background, body weight, hairlines, sentence case.
Rationale: one element can be remembered; the mirror test, remove one accessory (frontend-design; Chanel).
Check: the 1280 screenshot has exactly one element that a squint test isolates; it matches the plan's bold moment.

A10. Always run the self-critique gate (section 3.2) with screenshots at 390 and 1280 and write `design-critique.md` before showing any preview path.
Rationale: a picture catches what grep cannot: banding, hierarchy, an eye that lands in the wrong place.
Check: `$W/design-critique.md` exists, has a results table with no FAIL, and references two screenshot files.

A11. Always ship the quality floor without announcing it: `:focus-visible` styles, `prefers-reduced-motion` handling, 48px minimum tap targets, alt text on product media, `lang` attributes on non-Latin text.
Check: `grep -c ':focus-visible' $W/page-theme.css` >= 1; `grep -c 'prefers-reduced-motion'` >= 1 when animation exists; `grep -c 'lang="'` >= 1 when Devanagari is present.

A12. Always write copy as design content: sentence case, active voice, the CTA says what happens ("Add to cart", not "Shop Now →"), no placeholder or invented copy, brand voice from `voice_md` or the merchant.
Check: `grep -cE '>(Shop Now|Get Started|Learn More|Buy Now)\s*(→)?<' $W/lexsis-source.html` is 0; no "lorem".


## Tells (fail the squint test)

Cream page + high-contrast serif + terracotta accent as the only idea; identical rounded cards with one radius and one grey shadow; tracked-out ALL-CAPS eyebrow above every heading; meta strings joined with middle dots; `WORD — fragment` labels; `→` appended to links and buttons; icon in a rounded tile above every heading; discount pills and "MOST POPULAR" ribbons; gradient washes; fade-up on every section; five gold stars with a round avatar and an italic quote; a monospace face for small labels; near-black `#0B0B0B` standing in for black.

Source audit: `work/research/lexsis-design-rules.md` (2026-09-05).
