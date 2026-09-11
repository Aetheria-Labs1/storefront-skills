# Slot spec

Technical and content specification per asset slot role: aspect, minimum
source resolution, weight budget, format, loading rule, content rules,
allowed source types and alt-text template. `/design-page` applies it to every
`<img>`, `<picture>` and `<video>` it writes; `/generate` fails production QA
on a hero that violates SS1. Job coverage is in
`references/assets/image-jobs-by-page-type.md`, sourcing in
`references/assets/asset-sourcing-sequence.md`, generation limits in
`references/assets/generation-policy.md`, video in
`references/assets/video-rules.md`. Text over images and overlays follow N7
and A7 in `references/design-rules.md`.

Weights are house budgets (HEURISTIC) anchored to the Web Almanac: the median
largest image on a mobile page is 135 KB, the 75th percentile 404 KB, and 8%
of pages ship an LCP image over 1 MB https://almanac.httparchive.org/en/2024/media ,
https://almanac.httparchive.org/en/2024/performance . Minimum resolutions
follow Shopify (2048 x 2048 recommended for square product images; upload cap
5000 x 5000, 25 MP, 20 MB) https://help.shopify.com/en/manual/products/product-media/product-media-types
and Amazon (1600 px longest side for zoom) https://sellercentral.amazon.com/help/hub/reference/external/G1881 .

## 1. Technical spec

`Plan role` is the Role/purpose value written in the plan's Asset slots
table. "Preload" means `<link rel="preload" as="image">` or an `<img>` in the
initial HTML with `fetchpriority="high"`; "lazy" means `loading="lazy"
decoding="async"`.

| Slot role | Plan role | Aspect | Min source px | Max KB mobile / desktop | Format | Loading |
|---|---|---|---|---|---|---|
| `hero-image` | `product_media` | 16:9 or 21:9 desktop full-bleed; 4:5 desktop split; 4:5 or 9:16 mobile art-directed | 1920 wide desktop (2400 preferred); 1080 x 1350 or 1080 x 1920 mobile | 200 / 350 | AVIF or WebP, JPEG fallback | preload, `fetchpriority="high"`, never lazy, never in a carousel |
| `hero-backdrop` | `hero_bg` | 16:9 plus portrait crop | 1536 wide (generator ceiling; acceptable because the image carries no product detail) | 200 / 250 | AVIF or WebP | as `hero-image` when it is the largest element |
| `hero-video-poster` | `product_media` or `proof` | matches the video: 16:9 or 9:16 | 1280 wide or 1080 x 1920 | 150 / 200 | AVIF or WebP, JPEG fallback | preload, `fetchpriority="high"`; the video itself `preload="none"` |
| `gallery-main` | `product_media` | 1:1 (Shopify default) or 4:5 | 1600 short side (2048 preferred) | 250 / 300 | AVIF or WebP | first image `fetchpriority="high"` on `pdp` types; others lazy |
| `gallery-thumb` | derived from `gallery-main` | 1:1 | 160 display, served from the main image `srcset` | 30 | as main | lazy |
| `lifestyle-inset` | `product_media` (in-use or context) | 3:2, 4:5 or 16:9 | 1600 wide | 200 / 250 | AVIF or WebP | lazy |
| `feature-image` | `product_media` or `product_composite` | 1:1 or 4:5 | 1200 | 150 / 180 | AVIF or WebP | lazy |
| `section-background` | `section_bg` | 21:9 or 16:9 | 1920 wide (1536 when generated) | 180 / 200 | AVIF or WebP | lazy unless above the fold; bold moment only |
| `product-card` | `product_media` | 1:1 or 4:5, uniform per grid | 800 short side (1200 preferred) | 60 / 80 | AVIF or WebP | lazy; first row above the fold may use `fetchpriority="auto"` |
| `review-avatar` | `proof` | 1:1 | 200 (display 40 to 96) | 20 | WebP or CSS initials | lazy |
| `ugc-tile-square` | `proof` (ugc) | 1:1 or 4:5, uniform per grid | 800 | 60 / 80 | AVIF or WebP | lazy |
| `ugc-tile-vertical` | `proof` (ugc video) | 9:16 | poster 1080 x 1920; video 1080 x 1920 | poster 120; video 8000 | poster WebP; video H.264 MP4, optional WebM or AV1 | poster lazy; video `preload="none"`, click to play |
| `press-logo` | `proof` (press-logo-linked) | as supplied, height-normalised 24 to 32 px display | vector | 10 | SVG, or PNG monochrome at 2x | lazy; inside `<a href>` |
| `badge` | `proof` (certification) | 1:1 or as issued, 48 to 64 px display | vector | 10 | SVG or PNG monochrome at 2x | lazy |
| `before-after-pair` | `proof` (before-after) | 1:1 each, identical crop | 1200 | 180 / 200 each | AVIF or WebP | lazy |
| `diagram` | `product_media` (diagram) | any | inline SVG; raster fallback 1600 wide | 120 / 150 | SVG; PNG or WebP fallback | lazy |
| `swatch` | `product_media` (swatch) | 1:1 | 400 (display 24 to 64) | 20 | WebP, or CSS colour from catalog hex | lazy |
| `size-chart-image` | `product_media` (size-reference) | any | HTML table preferred; raster fallback 1600 wide | 150 / 200 | PNG or WebP | lazy |
| `founder-photo` | `proof` (founder-note) | 4:5 or 1:1 | 1200 | 120 / 150 | AVIF or WebP | lazy |
| `og-social-image` | `product_media` | 1.91:1 | 1200 x 630 | 300 | JPEG or PNG (widest crawler support) | `<meta property="og:image">` only; not in the body |
| `texture-tile` | `texture_fill` or `pattern_tile` | 1:1 seamless | 512 | 60 | WebP or PNG | inline `style` background on a `div`; lazy by nature |
| `decorative-element` | `decorative_element` | any | vector | 8 SVG; 40 transparent PNG | SVG preferred | lazy; `aria-hidden="true"` |
| `icon` | not a slot (`icon_set` only when authored) | 1:1, 24 px grid | vector | 4 each | inline SVG | inline |

## 2. Content and sourcing

Allowed sources use the step names from `asset-sourcing-sequence.md`:
shopify, library, merchant-upload, supplier, stock, generated (purpose in
brackets). Alt templates use `{}` fields; keep alt under 125 characters; never
begin with "image of", "photo of" or "picture of".

| Slot role | Content rules | Allowed sources | Alt template |
|---|---|---|---|
| `hero-image` | Same SKU, variant and angle family as the ad; product legible within one second; a quiet zone for HTML headline and CTA; a face looks toward the copy or product; one static image | shopify, library, merchant-upload; stock only as a backdrop with a real cut-out composited; generated[hero_bg] backdrop only | "{Product} {variant} {in use or on surface}, {one-line scene}" |
| `hero-backdrop` | No people, products, text or logos; low detail under the text; passes 4.5:1 with the single overlay | library, stock, generated[hero_bg] | `alt=""` |
| `hero-video-poster` | A real frame showing the product and, where present, a face or hands; never an auto-selected dark frame; play control drawn in HTML | derived from the video; shopify; library | as the hero image |
| `gallery-main` | Job order: identity, in-use, detail, scale, variation, included-items; consistent background within the identity set; zoomable; swaps on variant selection | shopify, library, merchant-upload, supplier | "{Product} {variant}, {job: front view / close-up of X / shown at scale with Y}" |
| `gallery-thumb` | All visible up to 10 to 14, then an explicit "+N"; video thumbs carry a play badge | derived | "Image {n} of {N}: {short job}" |
| `lifestyle-inset` | Real product legible; real people only when they are not presented as customers (or the slot cites a UGC ledger row); consistent grading across the set | shopify, library, merchant-upload; stock only without the product and without customer implication; generated[product_composite] over a real cut-out for `context` | "{Person or scene} using {product} {where}" |
| `feature-image` | One image per benefit; the product present; text in HTML | shopify, library, generated[product_composite] | "{Product} showing {feature}" |
| `section-background` | Carries no information; low luminance variance; only in the bold moment | library, stock, generated[section_bg] | `alt=""` |
| `product-card` | Identity image; same background, crop scale and orientation across the grid | shopify, library | "{Product} {variant}" |
| `review-avatar` | A real reviewer photo with consent, or CSS initials; never stock or generated faces | library (with ledger row), CSS initials | "{First name}" or `alt=""` when the name is adjacent |
| `ugc-tile-square` | Rights-cleared; crop only; original grading; caption with first name or handle when permitted; the grid is labelled as customer content | library (UGC with ledger row) | "Customer photo: {product} {context}" |
| `ugc-tile-vertical` | Native 9:16; captions; disclosure when gifted or paid; 20 to 40 s | library (UGC with ledger row) | poster: "Customer video: {topic}" |
| `press-logo` | Only outlets that covered the brand; monochrome; one height; wrapped in a link to the article | library (outlet-supplied or licensed) | "{Outlet}" (the link's accessible name) |
| `badge` | Real certification marks only, issuer artwork, issuer text beside the mark | library (issuer artwork) | "{Certification name}" |
| `before-after-pair` | Genuine, same lighting, angle and framing; unretouched; consent and substantiation on file; interval and "individual result" in HTML; never in the hero | library only, with a `verified` ledger row | "Before: {state}. After {interval}: {state}" |
| `diagram` | Numbers, units and labels in HTML or SVG `<text>`; palette colours; no photoreal rendering | authored inline SVG, merchant-upload, library, supplier | short alt plus the full data in adjacent HTML |
| `swatch` | Real swatch per variant; shade on skin for colour cosmetics; flat chips may be CSS from the catalog hex | shopify, library, merchant-upload, supplier | "{Shade or colour name}" or "{Shade} on {skin tone}" |
| `size-chart-image` | HTML table first; image only when the merchant supplies a chart that cannot be transcribed | merchant-upload, library | "Size chart for {product}; measurements listed below" |
| `founder-photo` | Real, named, in context (workshop, kitchen, lab) | library, merchant-upload | "{Name}, {role} at {brand}" |
| `og-social-image` | Real product plus wordmark; text allowed here only, because it never renders in the page | shopify, library | n/a (meta tag) |
| `texture-tile` | Abstract, tileable, no objects | generated[texture_fill or pattern_tile], stock | `alt=""` |
| `decorative-element` | Palette-limited vector; static; at most two per page | generated[decorative_element], library | `alt=""` |
| `icon` | One inline SVG set; one stroke; `currentColor`; `aria-hidden="true"` with a visible label | authored, library icon set | n/a |

## 3. LCP and loading rules

1. The hero is the LCP element on almost every page type; keep LCP under
   2.5 s at the 75th percentile https://web.dev/articles/lcp .
2. Put the hero `<img>` (or a `<link rel="preload" as="image">`) in the
   initial HTML so the preload scanner finds it. Client-injected or
   `data-src` heroes cause resource-load delay: the median poor-LCP page
   waits 1.3 s before even requesting its LCP image, four times its download
   time https://web.dev/blog/common-misconceptions-lcp .
3. `fetchpriority="high"` on the hero and on at most one other image; Google
   Flights cut LCP from 2.6 s to 1.9 s with this alone
   https://web.dev/articles/fetch-priority .
4. Never `loading="lazy"` on the hero https://developer.chrome.com/docs/performance/insights/lcp-discovery .
5. No hero carousel; if a legacy one exists, slides 2 and later get
   `fetchpriority="low"` https://web.dev/articles/fetch-priority .
6. Weights per section 1. Context: 73% of mobile pages have an image as LCP
   and the median mobile home page carries 900 KB of images
   https://almanac.httparchive.org/en/2024/performance ,
   https://almanac.httparchive.org/en/2024/page-weight .
7. AVIF is about 50% smaller than JPEG and WebP 25 to 35% smaller; serve them
   with a JPEG fallback through `<picture type>` https://web.dev/articles/choose-the-right-image-format .
   Shopify's CDN negotiates format automatically for uploaded media and
   accepts `width=` on the URL for `srcset` renditions
   https://help.shopify.com/en/manual/products/product-media/product-media-types .
   Where the asset host does not transform, import the mobile crop as its
   own asset.
8. `srcset` widths 360, 768, 1080, 1440, 1920 (and 2400 for full-bleed
   heroes) with a `sizes` attribute matching the layout
   https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images .
9. `width` and `height` on every `<img>` and `<source>` (or a CSS
   `aspect-ratio`) to stop layout shift https://web.dev/learn/images/prescriptive .
10. Everything below the first viewport is `loading="lazy"
    decoding="async"`.

## 4. Markup pattern

```html
<!-- hero: art-directed, preloaded, one static image -->
<picture>
  <source media="(max-width: 767px)" type="image/avif" srcset="{mobile}?width=1080&format=avif 1080w" width="1080" height="1350">
  <source media="(max-width: 767px)" srcset="{mobile}?width=1080 1080w" width="1080" height="1350">
  <source type="image/avif" srcset="{desktop}?width=1440&format=avif 1440w, {desktop}?width=1920&format=avif 1920w, {desktop}?width=2400&format=avif 2400w" sizes="100vw">
  <img src="{desktop}?width=1920" srcset="{desktop}?width=1440 1440w, {desktop}?width=1920 1920w, {desktop}?width=2400 2400w" sizes="100vw"
       width="1920" height="1080" fetchpriority="high" decoding="async"
       alt="{Product} {variant} on a linen table, morning light" style="object-position: 60% 40%">
</picture>

<!-- below the fold -->
<img src="{url}?width=800" srcset="{url}?width=800 800w, {url}?width=1200 1200w" sizes="(min-width: 1024px) 33vw, 50vw"
     width="1200" height="1500" loading="lazy" decoding="async" alt="{Product} shown at scale in hand">
```

## 5. Alt text rules

| Case | Rule | Source |
|---|---|---|
| Informative image | Describe what a blind shopper needs: product, variant, what the frame shows (angle, in use, scale). Under 125 characters. No "image of". No keyword lists | https://www.w3.org/WAI/tutorials/images/decision-tree/ |
| Decorative image (backdrop, texture, decoration) | `alt=""`, `aria-hidden="true"`, or a CSS or inline-style background | same |
| Complex image (diagram, size chart) | Short alt plus the full data as adjacent HTML text or table | same |
| Linked image (press logo, product card) | The alt is the link's purpose: outlet name or product name | same |
| Text in image (never planned) | If a merchant-supplied image contains text, repeat the text in HTML and describe it in alt | WCAG 1.4.5 https://www.w3.org/WAI/tutorials/images/ |
| Product media | Alt is mandatory (A11 in `references/design-rules.md`) | house |

## 6. Rules

`$W` is the page workspace.

SS1. Render the hero as a real `<img>` in the initial HTML with `fetchpriority="high"` and without `loading="lazy"`; at most two `fetchpriority="high"` images per page. RESEARCH.
Rationale: resource-load delay is the largest LCP cost https://web.dev/blog/common-misconceptions-lcp ; https://web.dev/articles/fetch-priority .
Check: `perl -0ne 'print scalar(() = /fetchpriority="high"/g), "\n"' $W/lexsis-source.html` prints 1 or 2; `perl -0ne 'print scalar(() = /section: hero.*?<img[^>]*loading="lazy"/gs), "\n"'` prints 0.

SS2. Give every `<img>` and `<source>` explicit `width` and `height` or a CSS `aspect-ratio`. RESEARCH.
Rationale: prevents layout shift https://web.dev/learn/images/prescriptive .
Check: `perl -ne 'print if /<img(?![^>]*width=)/' $W/lexsis-source.html | wc -l` prints 0.

SS3. Lazy-load everything below the first viewport with `loading="lazy" decoding="async"`. RESEARCH.
Rationale: below-fold images compete with the LCP image for bandwidth https://web.dev/articles/optimize-lcp .
Check: `grep -c '<img' $W/lexsis-source.html` minus `grep -c 'loading="lazy"'` equals the number of `fetchpriority="high"` images plus first-row product cards, and no more.

SS4. Serve AVIF or WebP with a fallback, through `<picture type>` or a CDN that negotiates format. RESEARCH.
Rationale: 25 to 50% smaller than JPEG https://web.dev/articles/choose-the-right-image-format .
Check: `grep -cE 'type="image/(avif|webp)"|format=(avif|webp)' $W/lexsis-source.html` is at least 1, or every image host is `cdn.shopify.com`.

SS5. Stay inside the weight budget per slot. HEURISTIC anchored to RESEARCH.
Rationale: median largest mobile image 135 KB; 8% of pages ship over 1 MB https://almanac.httparchive.org/en/2024/media .
Check: `curl -sI "<url>" | grep -i content-length` per slot rendition is at or under the budget; record the hero value in `qa-report.md`.

SS6. Give the mobile hero its own portrait crop with the product enlarged; never a scaled-down landscape. RESEARCH.
Rationale: scaled heroes shrink the product and push the CTA down https://www.nngroup.com/articles/big-pictures-small-screens/ ; art direction is what `<picture media>` exists for https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images .
Check: the hero `<picture>` has a `<source media="(max-width: 767px)">` whose `height` exceeds its `width`.

SS7. Write alt text under 125 characters from the slot template; decorative slots get `alt=""`; never "image of". LAW.
Rationale: W3C alt decision tree https://www.w3.org/WAI/tutorials/images/decision-tree/ .
Check: `perl -ne 'print if /alt="[^"]{126,}"/' $W/lexsis-source.html | wc -l` prints 0; `grep -ciE 'alt="(image|photo|picture) of' $W/lexsis-source.html` prints 0; every `<img>` inside a `hero_bg`, `section_bg`, `texture_fill` or `decorative_element` slot has `alt=""`.

SS8. Keep text off the image pixels; overlay HTML text with the one permitted legibility overlay and meet 4.5:1 (3:1 for large text) against the worst-case region at 390 and 1280. LAW, RESEARCH.
Rationale: WCAG 1.4.3 and 1.4.5; https://www.nngroup.com/articles/text-over-images/ ; N7 and A7 in `references/design-rules.md`.
Check: the N7 grep in `design-rules.md` returns only the plan-named overlay; hosted screenshots at 390 and 1280 show the headline on the quiet zone (yes/no in `qa-report.md`).

SS9. Use one static hero; never a carousel; never `fetchpriority="high"` on anything but the hero and the first gallery image. RESEARCH.
Rationale: carousel engagement about 1% and mostly slide 1 https://erikrunyon.com/2013/01/carousel-interaction-stats/ ; extra slides compete for LCP bandwidth https://web.dev/articles/fetch-priority .
Check: IJ8 grep in `image-jobs-by-page-type.md`; SS1 count.

SS10. Keep one aspect ratio per grid (product cards, UGC tiles, feature images). RESEARCH.
Rationale: mixed ratios break scanning and comparison https://www.nngroup.com/articles/product-photos-listing-pages/ .
Check: within one grid section, `grep -oE 'width="[0-9]+" height="[0-9]+"'` yields a single width:height ratio.

SS11. Set a focal point (`object-position` or the host's focal parameter) on every cover-cropped image. OPERATOR.
Rationale: responsive crops otherwise cut the product https://help.shopify.com/en/manual/online-store/images/theme-images .
Check: every `<img>` with `object-cover` or `object-fit: cover` also carries `object-position` or a focal URL parameter.

SS12. Ship one `og:image` at 1200 x 630 showing the real product. OPERATOR.
Rationale: link previews are the only place text-in-image is acceptable, and crawlers read the meta tag, not the body.
Check: `grep -c 'property="og:image"' $W/lexsis-source.html` is 1; the file's dimensions via `sips -g pixelWidth -g pixelHeight` are 1200 x 630.

SS13. Use real reviewer photos with consent or CSS initials for avatars; never stock or generated faces. LAW.
Rationale: 16 CFR 465 fake-testimonial rule https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers ; `references/proof/proof-ledger.md`.
Check: every `review-avatar` slot's Source decision is `library` with a ledger id, or the avatar is a CSS initials mark.

SS14. Never upscale product imagery to reach a minimum; drop the slot or ask the merchant. LAW.
Rationale: Google disapproves upscaled or thumbnail-sized product images https://support.google.com/merchants/answer/7052112 .
Check: import response `width`/`height` meets the slot minimum from the original file, not from a resized copy.

## Sources

- web.dev LCP https://web.dev/articles/lcp ; optimize LCP https://web.dev/articles/optimize-lcp ; fetch priority https://web.dev/articles/fetch-priority ; LCP misconceptions https://web.dev/blog/common-misconceptions-lcp ; image formats https://web.dev/articles/choose-the-right-image-format ; prescriptive syntaxes https://web.dev/learn/images/prescriptive
- Chrome LCP request discovery https://developer.chrome.com/docs/performance/insights/lcp-discovery
- Web Almanac 2024 media https://almanac.httparchive.org/en/2024/media ; performance https://almanac.httparchive.org/en/2024/performance ; page weight https://almanac.httparchive.org/en/2024/page-weight
- MDN responsive images https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images ; image formats https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types
- Shopify media types https://help.shopify.com/en/manual/products/product-media/product-media-types ; theme images and focal points https://help.shopify.com/en/manual/online-store/images/theme-images ; image sizes https://www.shopify.com/blog/image-sizes
- Amazon image guide https://sellercentral.amazon.com/help/hub/reference/external/G1881 ; Google Merchant spec https://support.google.com/merchants/answer/7052112
- W3C alt decision tree https://www.w3.org/WAI/tutorials/images/decision-tree/ ; images tutorial https://www.w3.org/WAI/tutorials/images/
- NN/g text over images https://www.nngroup.com/articles/text-over-images/ ; big pictures small screens https://www.nngroup.com/articles/big-pictures-small-screens/ ; listing photos https://www.nngroup.com/articles/product-photos-listing-pages/
- Erik Runyon carousel stats https://erikrunyon.com/2013/01/carousel-interaction-stats/
- FTC consumer reviews rule Q&A https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers
