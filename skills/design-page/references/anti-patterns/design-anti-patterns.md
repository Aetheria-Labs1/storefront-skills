# Design anti-patterns

The cluster of visual defaults that marks a page as generated. Any one tell
is defensible; three or more on one page is the fingerprint. This file
extends `references/design-rules.md`: tells that N1 to N14 and A1 to A12
already forbid are listed by id in section 1 and not restated. Section 2
adds the tells the house rules do not cover, each with a check. `/plan-page`
uses the list for the "Generic-default check"; `/design-page` uses it in the
hosted review; `design_lint.py` runs the static greps.

Why it happens: models emit the statistical mode of their training data.
Tailwind's tutorial palette (indigo-500) and its three-column feature grid
dominated 2019 to 2024 web code, so "buttons are indigo, features come in
threes" is the default. Vendor scan data (Sailop, indicative): blue-600
primary in about 34 percent of AI-generated sites, indigo about 22 percent,
blue-to-purple gradient in 41 percent of gradient users, Inter in 47 percent.
https://sailop.com/blog/ai-slop-encyclopedia ; https://booplex.com/blog/what-is-ai-design-slop ; https://github.com/Ferousco-dev/anti-slop-design

Cluster rule (DA0, FAIL, OPERATOR): each tell below is WARN alone. Count
every DA tell plus every design-rules tell present on the page; a total of
three or more fails the page regardless of brand. `$W` is the page
workspace.

## 1. Tells already enforced by design-rules

| Tell | Rule id | Do not restate; run the rule's check |
|---|---|---|
| Emoji as icons or bullets | N1 | |
| Alternating section background bands | N2 | |
| Mixed icon libraries, images as icons | N3 | |
| More than two type families | N4 | |
| Tracked-out ALL-CAPS eyebrow above every heading | N5 | |
| One accented word inside a headline | N6 | |
| Gradient washes, glow shadows, shimmer, pulse, hover-lift, hover-scale | N7 | |
| Cards around plain text | N8 | |
| Discount pills, "MOST POPULAR" ribbons | N9 | |
| Fade-up per section, stagger, counters, parallax, marquee | N10 | |
| Unsourced stars, counts, "as seen in" logos | N11 | |
| Arrows on buttons, middle-dot meta strings, icon-in-rounded-tile above headings | N12 | |
| One radius on everything or mixed radii per object type | N13 | |
| Off-brand hex and Tailwind default colour classes (#667eea, #764ba2, #8b5cf6, #f9fafb, #6366f1, #7c3aed, text-yellow/gray/slate/purple/indigo) | N14 | |
| Body measure over 80 characters | A4 | |
| Text under 4.5:1, CTA text on brand pastel | A7 | |
| Stock CTA copy "Shop Now / Get Started / Learn More / Buy Now" | A12 | |

## 2. Additional tells

| Id | Tell | Why it reads generated | Rule | Tag | Check |
|---|---|---|---|---|---|
| DA1 | Indigo, violet, purple or fuchsia palette; blue-to-purple gradient; cyan accent on a dark ground | Tailwind's default accent and the 2023 to 2024 SaaS hero kit; N14 lists a few hex values, this widens it to the whole hue band | Palette comes from the brand kit or the plan's named palette. If the brand kit has no purple, the page has no purple. | RESEARCH | `grep -ciE '\b(indigo|violet|purple|fuchsia)-[3-7]00\b|#(6d28d9|5b21b6|a855f7|9333ea|c026d3|2563eb|22d3ee)\b|from-(blue|indigo|violet)-[0-9]+[^"]*to-(purple|violet|fuchsia|pink)-[0-9]+' $W/lexsis-source.html $W/page-theme.css` is 0 unless the hex is in the plan's palette table |
| DA2 | Inter, or system-ui alone, as the only typeface | The most frequent generated pairing (47 percent in the Sailop sample) | Typeface from the brand kit; if none, a distinct display plus text pairing with the rationale in the plan's Type roles line. | RESEARCH | `grep -oiE "family=[A-Za-z+]+|font-family:\s*[^;]+" $W/page-theme.css | sort -u` contains a face other than Inter, system-ui, ui-sans-serif, Arial |
| DA3 | Three-column icon-feature grid (icon, h3, two-line p, times three) | The tutorial features section; readers skip garnish icons (uxskill) | Features as product photos, an annotated image, a comparison table or prose with numbers. If a grid is unavoidable, vary the column count and lead with an image. | RESEARCH | script in section 3 `iconTrios` is 0 |
| DA4 | Glassmorphism: `backdrop-filter: blur` plus translucent white plus 1 px border | 2021 to 2024 dribbble default | Blur only when a sticky header sits over imagery. No glass cards. | OPERATOR | `grep -cE 'backdrop-filter:\s*blur|backdrop-blur' $W/lexsis-source.html $W/page-theme.css` at most 1, and only on the header |
| DA5 | Two equal-weight buttons in the hero ("Get started" and "Learn more") | SaaS hero kit; also fails CA4 | One filled CTA; an optional text link with a specific object ("See the ingredients"). | RESEARCH | `document.querySelectorAll('[data-section=hero] button, [data-section=hero] a.btn').length <= 1` counting filled buttons; the second control, if any, is an underlined `<a>` |
| DA6 | Fake browser or phone mockup framing a physical product | Software-template habit applied to goods | Show the product. Mockups only when the product is an app or a screen. | OPERATOR | `grep -ciE 'browser-mockup|device-frame|phone-mockup|window-dots' $W/lexsis-source.html` is 0 unless the catalog item is software |
| DA7 | Testimonial trio: three cards, round avatars, five stars each, equal-length quotes, "First L." attribution | The template proof block; also fails N11 when unsourced | Real ledger quotes with varied length and format: one long, several short, one screenshot; attribution exactly as stored; no stock avatars. | RESEARCH | script in section 3 `equalTestimonials` is 0; `grep -c 'rounded-full' <testimonial section>` is 0 unless the avatar is a real customer photo in the ledger |
| DA8 | "Trusted by 10,000+ customers" caption over a logo strip | Round invented number plus logos without links; lint P2 and P3 cover the logos | Counts only from a ledger row, rounded down with "over"; logos only as linked press rows with the caption "Press" or "In the press". | LAW, OPERATOR | `grep -ciE 'trusted by [0-9,]+\+?|loved by [0-9,]+\+?|join [0-9,]+\+? (happy|satisfied)' $T` is 0 unless the number is in the ledger |
| DA9 | Sparkles, rocket, lightning-bolt or "magic wand" icons | Generic "AI" iconography; meaningless for goods | Icon set excludes them. | OPERATOR | `grep -ciE 'sparkles|lucide-rocket|lucide-zap|icon-bolt|wand' $W/lexsis-source.html` is 0 |
| DA10 | Checkmark lists in more than one section | The universal "benefits" filler | At most one checklist per page, and only for inclusions or a comparison. | OPERATOR | count of `<ul>` whose items start with a check SVG or "check" class is at most 1 |
| DA11 | Stats trio "99% / 24/7 / 10k+" | Round or non-metric numbers signal invention; N11 covers sourcing | Numbers are exact, sourced, and never "24/7"; at most one stats row with a footnoted source per figure. | LAW, OPERATOR | `grep -cE '\b(99|100)%|24/7|\b10k\+|\b10,000\+' $T` is 0 unless each is a ledger row |
| DA12 | Decorative blur orbs, radial "glow" blobs, grid-dot or noise backgrounds | Background filler that says nothing about the product | None. The organic clip-path treatments in `references/blob-shapes.md` are allowed only on an image, only when the plan names them as the bold moment. | OPERATOR | `grep -cE 'blur-(2xl|3xl)|bg-grid|bg-dot|radial-gradient' $W/lexsis-source.html $W/page-theme.css` is 0; `clip-path: url(#blob` appears at most once and matches the plan |
| DA13 | Everything centred | Centred long text is hard to scan; the centred stack is the template default | Hero and bodies left-aligned at 390; centre only short headline-plus-CTA stacks; at most half of sections centred. | RESEARCH | `[...document.querySelectorAll('p')].filter(p => getComputedStyle(p).textAlign === 'center' && p.getBoundingClientRect().height > parseFloat(getComputedStyle(p).lineHeight) * 1.5).length === 0` |
| DA14 | Identical section rhythm: adjacent sections with the same skeleton (h2, p, three children, button) | Repetition is the layout equivalent of the rule of three | No two adjacent sections share a layout skeleton; vary with a full-bleed image, a table, a single large quote, an ingredient callout, a founder note. | OPERATOR | script in section 3 `adjacentSame` is 0 |
| DA15 | Generic stock or AI-rendered people, floating 3D objects | See CA6 and the generation policy NEVER list | Product, packaging, real customers with rights, studio shots. | RESEARCH | every people image is a ledger UGC row or merchant asset |
| DA16 | Hero carousel | CA1 | One static hero. | RESEARCH | CA1 check |
| DA17 | Gradient text (`background-clip: text`) | N7 forbids gradients in general; this names the text variant explicitly | Solid colour for all text. | OPERATOR | `grep -cE 'background-clip:\s*text|-webkit-text-fill-color:\s*transparent|bg-clip-text' $W/lexsis-source.html $W/page-theme.css` is 0 |
| DA18 | Dark hero with neon accents, then a light body | Two moods glued together; also breaks N2 unless the dark hero is the named bold moment | One mode per page; a dark section only as the plan's bold moment or for a dark brand. | OPERATOR | N2 browser check lists at most one non-page background between nav and footer |
| DA19 | `transition: all`; scroll-reveal classes on more than three elements | Blanket motion is the default; N10 covers unplanned motion | No `transition-all`; reveal only in the plan's one moment. | OPERATOR | `grep -cE 'transition:\s*all|transition-all' $W/lexsis-source.html $W/page-theme.css` is 0; `grep -cE 'data-aos|animate-fade-up|reveal-on-scroll' $W/lexsis-source.html` is 0 |
| DA20 | Centred section header stack on every section: eyebrow, h2, `max-w-2xl mx-auto` paragraph | The single most repeated Tailwind section opener | Section openers vary: a left-aligned h2 alone, an h2 with a figure, a table caption, a pull quote. | OPERATOR | `grep -cE 'max-w-(xl|2xl|3xl) mx-auto text-center' $W/lexsis-source.html` at most 1 |
| DA21 | Pill badge above the h1 ("New", "v2.0", "AI-powered", "Now shipping") | Product-launch SaaS chrome; N9 covers discount pills | No hero badge. A dated news line ("Back in stock 12 Sep") is plain text from the offer ledger. | OPERATOR | hero section contains no `rounded-full` element with under 25 characters of text above the h1 |
| DA22 | Cinematic overlay hero: full-bleed stock photo, dark overlay, centred white headline, repeated as section openers | One legibility overlay is permitted (N7); repeating it is a template | At most one image-with-overlay moment per page, named in the plan. | OPERATOR | `grep -cE 'bg-black/[0-9]+|rgba\(0, ?0, ?0, ?0\.[3-7]' $W/lexsis-source.html $W/page-theme.css` at most 1 |
| DA23 | Default greys as the palette: #0B0B0B or #111827 text, #6b7280 muted, #f9fafb surface | Tailwind gray-900/500/50; N14 lists #f9fafb only | Text, muted and surface tints are derived from the brand palette; near-black is a named hex in the plan. | OPERATOR | `grep -ciE '#0b0b0b|#111827|#0f172a|#6b7280|#9ca3af|#f3f4f6|#e5e7eb' $W/lexsis-source.html $W/page-theme.css` is 0 |
| DA24 | Bento grid of mixed-span rounded cards | 2024 SaaS layout with no commerce job | Product grids follow `references/product-grid.md`; no decorative bento. | OPERATOR | `grep -cE 'col-span-[2-3][^"]*row-span-[2-3]' $W/lexsis-source.html` is 0 |
| DA25 | Uniform `shadow-lg`/`shadow-xl` on every card | Depth as decoration | Shadows only on floating UI (sticky bar, dialog, dropdown); cards use a hairline or none (N8). | OPERATOR | `grep -cE 'shadow-(lg|xl|2xl)' $W/lexsis-source.html` at most 2, none inside a section that is not chrome |
| DA26 | Five gold stars with a rating but no count, or stars as decoration in the hero | Proof-ledger display rule 3: stars only beside a numeric average and count | As the ledger rule. | LAW | lint P4 |

## 3. Scoring script

```bash
# Count DA tells (static). Add browser results for DA5, DA13, DA18, and the design-rules tells found by design_lint.py.
S=$W/lexsis-source.html; C=$W/page-theme.css; T=$W/copy.txt
tells=0
hit(){ n=$(eval "$1"); [ "${n:-0}" -gt "${2:-0}" ] && { echo "DA$3 $n"; tells=$((tells+1)); }; }
hit "grep -ciE '\b(indigo|violet|purple|fuchsia)-[3-7]00\b|from-(blue|indigo|violet)-[0-9]+[^\"]*to-(purple|violet|fuchsia|pink)' $S $C | awk -F: '{s+=\$NF} END{print s}'" 0 1
hit "grep -cE 'backdrop-filter:\s*blur|backdrop-blur' $S $C | awk -F: '{s+=\$NF} END{print s}'" 1 4
hit "grep -ciE 'browser-mockup|device-frame|phone-mockup' $S" 0 6
hit "grep -ciE 'trusted by [0-9,]+\+?|loved by [0-9,]+\+?' $T" 0 8
hit "grep -ciE 'sparkles|lucide-rocket|lucide-zap|icon-bolt' $S" 0 9
hit "grep -cE '\b(99|100)%|24/7|\b10k\+' $T" 0 11
hit "grep -cE 'blur-(2xl|3xl)|bg-grid|bg-dot|radial-gradient' $S $C | awk -F: '{s+=\$NF} END{print s}'" 0 12
hit "grep -cE 'background-clip:\s*text|bg-clip-text' $S $C | awk -F: '{s+=\$NF} END{print s}'" 0 17
hit "grep -cE 'transition:\s*all|transition-all' $S $C | awk -F: '{s+=\$NF} END{print s}'" 0 19
hit "grep -cE 'max-w-(xl|2xl|3xl) mx-auto text-center' $S" 1 20
hit "grep -cE 'bg-black/[0-9]+' $S" 1 22
hit "grep -ciE '#0b0b0b|#111827|#0f172a|#6b7280|#f3f4f6|#e5e7eb' $S $C | awk -F: '{s+=\$NF} END{print s}'" 0 23
hit "grep -cE 'col-span-[2-3][^\"]*row-span-[2-3]' $S" 0 24
hit "grep -cE 'shadow-(lg|xl|2xl)' $S" 2 25
echo "static DA tells: $tells  (add design_lint FAIL count and browser tells; total >= 3 fails DA0)"
```

```python
# DA3 iconTrios, DA7 equalTestimonials, DA14 adjacentSame (bs4 over lexsis-source.html)
from bs4 import BeautifulSoup; import re, sys
s = BeautifulSoup(open(sys.argv[1]), 'html.parser')
iconTrios = sum(1 for g in s.select('[class*="grid-cols-3"]') if len(g.find_all(recursive=False)) == 3 and all(k.find('svg') and k.find(['h3','h4']) and k.find('p') for k in g.find_all(recursive=False)))
def L(q): return len(q.get_text(' ', strip=True).split())
equalTestimonials = 0
for sec in s.select('[data-section*="review"],[data-section*="testimonial"]'):
    qs = [L(q) for q in sec.select('blockquote,[data-part=quote]')]
    if len(qs) >= 3 and max(qs) - min(qs) <= 0.1 * max(qs): equalTestimonials += 1
sig = lambda sec: tuple(c.name for c in sec.find_all(['h2','h3','ul','img','button','table','blockquote','figure'], limit=8))
secs = s.select('[data-section]'); adjacentSame = sum(1 for a, b in zip(secs, secs[1:]) if sig(a) == sig(b))
print({'DA3': iconTrios, 'DA7': equalTestimonials, 'DA14': adjacentSame})   # all 0
```

## 4. What to do instead

| Instead of | Use |
|---|---|
| Icon-trio features | one annotated product photo with three callouts, or a two-column spec table |
| Testimonial trio | one long ledger quote beside the claim it supports; a short list of three verbatim lines of different length elsewhere |
| Stats trio | one exact number with its source in a footnote, or nothing |
| Glass card, blur orb, gradient | the page background, a hairline, and the product image |
| Two-button hero | one filled CTA and one underlined text link naming a specific section |
| Centred header stack | left-aligned h2 with the figure or table it introduces |
| Cinematic overlay hero | the product on the page background at 55 percent width, headline beside it |

## 5. Lint alignment

`design_lint.py` covers the section 1 tells. Adopt these static greps as WARN each, and a `DA0` FAIL when the sum of DA WARNs and N/A FAILs is three or more:

```python
DA1  = r"\b(indigo|violet|purple|fuchsia)-[3-7]00\b|#(6d28d9|5b21b6|a855f7|9333ea|c026d3|2563eb|22d3ee)\b|from-(blue|indigo|violet)-\d+[^\"]*to-(purple|violet|fuchsia|pink)-\d+"
DA2  = "font families other than Inter/system-ui/ui-sans-serif/Arial in page-theme.css == 0"   # invert: WARN when none
DA4  = r"backdrop-filter:\s*blur|backdrop-blur"            # allow 1
DA6  = r"browser-mockup|device-frame|phone-mockup|window-dots"
DA8  = r"trusted by [0-9,]+\+?|loved by [0-9,]+\+?|join [0-9,]+\+? (happy|satisfied)"
DA9  = r"sparkles|lucide-rocket|lucide-zap|icon-bolt|wand"
DA11 = r"\b(99|100)%|24/7|\b10k\+|\b10,000\+"              # unless in plan claims
DA12 = r"blur-(2xl|3xl)|bg-grid|bg-dot|radial-gradient"
DA17 = r"background-clip:\s*text|-webkit-text-fill-color:\s*transparent|bg-clip-text"
DA19 = r"transition:\s*all|transition-all|data-aos|animate-fade-up|reveal-on-scroll"
DA20 = r"max-w-(xl|2xl|3xl) mx-auto text-center"          # allow 1
DA22 = r"bg-black/[0-9]+|rgba\(0, ?0, ?0, ?0\.[3-7]"         # allow 1
DA23 = r"#0b0b0b|#111827|#0f172a|#6b7280|#9ca3af|#f3f4f6|#e5e7eb"
DA24 = r"col-span-[2-3][^\"]*row-span-[2-3]"
DA25 = r"shadow-(lg|xl|2xl)"                                # allow 2
```

Browser and bs4 checks (DA3, DA5, DA7, DA13, DA14, DA18) are recorded in `qa-report.md` and counted toward DA0 by hand.
