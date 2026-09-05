# Island Presets

Named, pre-validated prop and CSS presets for the active Lexsis islands. A preset id is a
design-intent token the plan may name (`Preset: buybox/compact-dark`); `/design-page`
applies it verbatim and records any deviation as `presetOverrides` in the manifest.
Every preset respects `storefront-engine/references/design-rules.md`: no emoji, no gradients, transparent island
surfaces on the single page background, no icon glyphs unless the page has no other
icon set, no motion effects. Verified against island schema 5.1.0 on 2026-09-05; when
`island_schema` reports a different version, re-verify before use.

## 2. Per-island reference

### 2.1 SiteHeader

Compound announcement bar + navbar. Category navigation. Hydrate default `immediate`. Variants: none. Headless: no (but supports *hydration mode*: author your own `<header>` markup with `data-lx-header="root|announcement|announcement-text|announcement-dismiss"` and `data-lx-nav="root|cart-trigger|cart-count|mobile-trigger|mobile-panel|link|logo"` as the child of `<lx-island>`; props then only carry behavior). Max 1 per page, first section; never combine with a separate Navbar.

UI-controlling props (schema v5.1.0):

| Prop | Type | Values / default | Effect |
|---|---|---|---|
| `sticky` | boolean | - | header pins to top |
| `transparent` | boolean | - | no nav background until scroll (hero overlap) |
| `offsetTop` | string | CSS length | top offset when sticky |
| `cartMode` | enum | `drawer` \| `link` | cart icon opens drawer or navigates to `cartUrl` |
| `hideCart` | boolean | - | removes cart trigger |
| `dismissible` / `rotateInterval` | boolean / number | top-level, hydration mode only | announcement close button, rotation ms |
| `announcement.backgroundColor`, `.textColor` | string | hex or `var(--lx-*)` | announcement bar paint (allowed exception to one-background rule) |
| `announcement.speed` | number | ms; keep >= 4000 | rotation speed |
| `announcement.dismissible` | boolean | - | close button |
| `navbar.transparent` | boolean | - | same as top-level for legacy mode |
| `navbar.style` | object | `bgColor, textColor, accentColor, logoHeight, height, borderBottom, fontFamily, fontSize, fontWeight, padding, maxWidth, dropdownBg, dropdownTextColor, mobileBg, mobileTextColor` (all string) | full nav paint and type; schema types these as `?object`, examples pass strings |
| `navbar.hideCart` | boolean | - | - |

Data props: `announcement.messages[]` (string, keep < 60 chars), `announcement.link`, `navbar.logo{src|text, alt, url}` (use `text` wordmark when no logo asset), `navbar.links[{label,url,children[]}]`, `navbar.cta{label,url}`, `navbar.cartCount` (omit; auto-synced), `cartUrl`, `messages[]` (hydration mode).

CSS vars declared: `--lx-accent-color` only. `--lx-header-*`, `--lx-nav-*` from the earlier capture: unconfirmed, not in schema.
Parts: `announcement, announcement-dismiss, announcement-text, cart-badge, cart-trigger, cta, dropdown, dropdown-item, link, links, logo, mobile-link, mobile-panel, mobile-trigger, nav, root`.
Fallback: hydration-mode markup *is* the fallback; for legacy (props-only) mode give a plain `<header>` with logo link and 3-5 `<a>` links as the `data-lx-island-fallback` child.
Gotchas: `navbar.style.*` values must be strings even though schema prints `?object`. Announcement paint is the only place a non-page background is allowed besides footer. Do not set `cartCount`.

### 2.2 Navbar

Nav only (use when no announcement, or when announcement should scroll away). Hydrate `immediate`. Variants: none. Hydration mode as above with `data-lx-nav` tags. Must be a direct page child, not inside a section wrapper, for sticky to work.

UI-controlling props: `sticky`, `transparent`, `offsetTop`, `cartMode` (`drawer|link`), `hideCart`, `style{bgColor, textColor, accentColor, logoHeight, height, borderBottom, fontFamily, fontSize, fontWeight, padding, maxWidth, dropdownBg, dropdownTextColor, mobileBg, mobileTextColor}`, `cart{icon: cart|bag|basket, svg, image, label, badgeColor}`.
Data props: `logo{src|html, alt, url}` (required), `links[{label,url,children[]}]` (required), `cta{label,url}`, `cartUrl`, `cartCount` (omit).
CSS vars: `--lx-accent-color`. Parts: `cart-badge, cart-trigger, cta, dropdown, dropdown-item, link, links, logo, mobile-link, mobile-panel, mobile-trigger, root`.
Fallback: plain `<nav>` with logo and links.
Gotchas: `cart.svg` lets you supply the page's single inline SVG set icon (house rule: one stroke weight, `currentColor`); prefer it over `cart.icon` when the page already uses custom SVGs. `logo.html` accepts an inline SVG wordmark.

### 2.3 AnnouncementBar

Standalone rotating message strip. Hydrate `immediate`. Variants: none (earlier capture's `default|gradient|ticker|minimal` do not exist; a gradient would also break house rules). Max 1 per page; pair with Navbar, never with SiteHeader.

UI-controlling props: `backgroundColor` (string), `textColor` (string), `sticky` (boolean, default false), `dismissible` (boolean, default false; only meaningful with `sticky`), `speed` (number ms, default 4000, keep >= 4000).
Data props: `messages[]` (required, string), `link` (string, whole bar becomes a link).
CSS vars: `--lx-accent-color`. Parts: `close-btn, icon, link, root, text`.
Fallback: one `<p>` with the first message.
Gotchas: the `icon` part exists but no prop controls it; hide it with `[data-part="icon"]{display:none}` when the page has no icon set. Text must be emoji-free (house rule and validator check).

### 2.4 ProductGallery

PDP media gallery (thumbnail rails, grids, collage, masonry; image + video; lightbox; variant sync). Category commerce. Hydrate `immediate`. Headless: no. Variants = `layout` values.

UI-controlling props:

| Prop | Type | Values / default | Effect |
|---|---|---|---|
| `layout` | enum | `horizontal` (default) \| `vertical` \| `stacked` \| `grid` \| `collageLeft` \| `collageRight` \| `twoColumn` \| `masonry` | desktop arrangement |
| `mobileLayout` | enum | `stacked` \| `swipe` | always set explicitly for grid/collage/masonry |
| `thumbPosition` | enum | `left` \| `right` \| `bottom` \| `top` | rail placement for horizontal/vertical |
| `transition` | enum | `none` \| `slide` \| `fade` (default) \| `zoom` \| `kenBurns` | avoid kenBurns (motion) |
| `objectFit` | enum | `cover` (default) \| `contain` | contain for packshots on white |
| `maxHeight` | string | CSS length | caps main media |
| `enableLightbox` | boolean | - | adds `open-lightbox` control |
| `autoplay` / `interval` | boolean / number | false / 4000 | avoid on PDP |

Data props: `media[]` (current; `images[]` is deprecated and kept as an alias; item `{src|url, alt, type: image|video, poster, mobileSrc, srcSet, sizes, fit, objectPosition, sources[], provider}`), `listenForVariant` (boolean; needs a VariantSwatches emitter).

CSS vars (declared, long list; the useful subset): `--lx-product-gallery-bg, -border, -radius, -gap, -mobile-gap, -mobile-peek, -mobile-ratio, -columns, -tile-ratio, -featured-ratio, -stacked-ratio, -masonry-tall-ratio, -masonry-wide-ratio, -focus-width, -focus-offset, -open-bg, -open-color, -open-shadow`; `--lx-media-carousel-arrow-{bg,border,color,hover-bg,offset,radius,shadow,size}`, `--lx-media-carousel-dot-{color,active-color,active-scale,gap,offset,shadow,size}`, `--lx-media-carousel-{bg,duration,ease,fit,radius,placeholder}`; `--lx-media-lightbox-{backdrop,close-*,control-*,max-width,max-height,media-bg,padding,mobile-padding,z-index}`; `--lx-video-*` and `--lx-shoppable-*` (video tiles only); `--lx-accent-color, --lx-bg-surface, --lx-text-color`.
Parts (useful subset): `root, viewport, track, slide, main-media, media, image, video, thumbnail-strip, thumbnail, grid, grid-item, controls, previous, next, dots, dot, open-lightbox, lightbox, lightbox-close, lightbox-content, adaptive-video-*`.
Fallback: first image as `<img>` at the gallery aspect ratio.
Gotchas: the compile validator accepts `media` or legacy `images`; each item needs `src` (or `url`). Presets use `media`.

### 2.5 ProductHero

Large hero gallery for split PDP layouts (media 50-60 percent of viewport beside BuyBox). Category commerce. Hydrate `visible` (design QA must scroll it into view). Headless: no. Variants = `layout`.

UI-controlling props:

| Prop | Type | Values / default |
|---|---|---|
| `layout` | enum | `stacked` \| `splitLeft` (default) \| `splitRight` \| `fullHeight` |
| `thumbnails` | enum | `none` \| `rail` (default) \| `dots` |
| `thumbnailPosition` | enum | `left` (default) \| `right` \| `bottom` (no `top`) |
| `navigation` | enum | `none` \| `arrows` \| `floatingArrows` (default) |
| `aspectRatio` | string | `3:4` default; `1:1`, `4:5` |
| `maxHeight` | string | `85vh` default |
| `transition` | enum | `none` \| `slide` \| `fade` (default) \| `zoom` \| `kenBurns` |
| `showIndicators` | boolean | - |
| `autoplay`, `interval`, `hoverAdvance` | boolean, number, boolean | false, 4000, false |
| `className` | string | passes through to root |

Data props: `images[]` (required; `{url, alt, type, poster, objectFit, objectPosition}`; note key is `url` here, `src` in ProductGallery), `listenForVariant`.
CSS vars: `--lx-hero-bg, --lx-hero-radius, --lx-hero-thumb-radius, --lx-hero-thumb-size, --lx-hero-thumb-gap, --lx-hero-arrow-bg, --lx-hero-arrow-size, --lx-hero-arrow-offset, --lx-hero-transition-duration, --lx-accent-color, --lx-border-color` (schema also lists a stray `--lx-hero-` prefix entry).
Parts: `root, media-pane, slide, thumbnail-rail, thumbnail, nav-prev, nav-next, dot`.
Fallback: first image `<img>` with the chosen aspect ratio.
Gotchas: default `85vh` pushes BuyBox below the fold on mobile; presets cap at `560px`-`640px`. Set `--lx-hero-bg: transparent`. Confirmed working styling pattern: `#id{--lx-accent-color:...;--lx-hero-radius:12px;--lx-hero-thumb-radius:10px}` and `#id [data-part="thumbnail"]{...}`.

### 2.6 BuyBox

Primary purchase UI: price, variant buttons, quantity, add-to-cart, optional trust badges, notify-me. Category commerce. Hydrate `immediate`. Headless: **yes** (hooks `add` required; `price, compare-price, variant-option[data-variant-id], qty, qty-inc, qty-dec, stock, error`; state classes `lx-selected lx-disabled lx-adding lx-added`). Max 1 per page. Requires `head.use_cart_v2: true` for cart feedback.

UI-controlling props:

| Prop | Type | Values / default | Effect |
|---|---|---|---|
| `variant` | enum | `default` \| `compact` \| `expanded` | compact drops qty and variant selector (single-variant only); expanded adds trust badges block |
| `showPrice` | boolean | true | hide when the section renders its own price |
| `showVariantSelector` | boolean | true | set false when VariantSwatches is used |
| `showTrustBadges` | boolean | - | badges row; default icons are the island's own set (see gotcha) |
| `buttonStyle` | object | `{borderRadius, padding, fontSize}` strings | CTA shape without CSS |
| `animate` | boolean \| string | true | add-to-cart feedback motion |
| `ctaText` | string | - | button label |

Data props: `product{title, price, compareAtPrice, variants[{id,title,price,available}]}` (required; `id` is the Shopify variant GID), `listenForEvents` (boolean, pair with VariantSwatches). `productId` shown in `index.md` and old layouts is **not** in the v5.1 schema.
CSS vars: `--lx-accent-color` only. Parts: `root, cta, variants, variant-btn, qty, qty-btn, trust-badges, notify`.
Fallback: static price `<p>` plus a disabled-looking `<a>` to `/products/{{product.handle}}`; never a working custom button.
Gotchas: `showTrustBadges` icons are not controllable by prop; if the page has no icon set or a different SVG set, set `showTrustBadges:false` (house rule: one icon style). Earlier capture's variants `standard|full-width|split|minimal` do not exist. Do not duplicate title/price outside the island unless `showPrice:false`.

### 2.7 StickyBar

Bottom-fixed CTA re-surfacing add-to-cart (product mode) or a collection link (collection mode). Category commerce. Hydrate `immediate`. Variants: none. Headless: no. Place after the BuyBox section.

UI-controlling props: `showAfter` (string CSS selector, e.g. `"#buy"`, or number px; **always set**), `animate` (boolean | string, default true; `false` for quiet pages), `cta` (string, default "Add to Cart").
Data props: `product{title, price, compareAtPrice?, image?, variantId}` (variantId required in product mode) **or** `collection{label, url, subtitle?, image?}`.
CSS vars: `--lx-accent-color, --lx-text-color`. Parts: `root, bar, cta, product-image, product-info, product-price, product-title`.
Fallback: none needed (bar is hidden until scroll); an empty child is fine.
Gotchas: no bar background prop; the bar paints its own surface (accepted: it is fixed chrome, not a section). Style `[data-part="bar"]` for border-top/shadow removal. Omit `product.image` for a text-only bar.

### 2.8 ProductCarousel

Horizontal product-card rail ("You may also like"). Category commerce. Hydrate `immediate`. Variants: none; card look via `cardVariant`. Headless: no. Needs 4+ products; `showQuickAdd` requires cart v2.

UI-controlling props:

| Prop | Type | Values | Effect |
|---|---|---|---|
| `cardVariant` | enum | `default` \| `compact` \| `compactRows` | card density; compactRows renders a list |
| `mediaTransition` | enum | `none` \| `slide` \| `fade` \| `zoom` \| `kenBurns` | card image swap on hover-advance |
| `hoverAdvance` / `hoverAdvanceMode` / `hoverInterval` | boolean / `next`\|`cycle` / number | cycles card media on hover; off for quiet pages |
| `showQuickAdd`, `showWishlist`, `showLearnMore`, `showQuickView` | boolean | - | card actions; each adds a button (icon buttons use the island's icon set) |
| `animate` | boolean \| string | - | staggered fade-up on entry |
| `columns` | number | - | ignored in carousel context per anti-pattern note; unconfirmed effect |
| `title` | string | - | heading rendered by island (`heading`/`title` parts) |

Data props: `products[{id, handle, title, subtitle?, price, compareAtPrice?, badge?, image? | media[]?, variants[]?}]` (required).
CSS vars: same media-carousel/featured-media/video family as ProductGallery plus `--lx-surface-alt, --lx-text-muted, --lx-border-color, --lx-bg-surface, --lx-accent-color, --lx-text-color`. No dedicated card radius/border var; use parts.
Parts (useful): `root, heading, title, track, viewport, slide, card-wrapper, image, badge, price, compare-price, quick-add, nav-prev, nav-next, dots, dot, row, row-image, row-title, row-price, row-subtitle, row-list, media-placeholder`.
Fallback: 4 static cards (`<a>` + `<img>` + title + price) in a 2/4 grid.
Gotchas: omit `title` and render the section h2 yourself to keep heading hierarchy in the wrapper (contract: h2 owned by section). `showWishlist`/`showQuickView` add icon buttons in the island's own icon style; leave off when the page uses its own SVG set.

### 2.9 Footer

Site footer: link columns, logo, tagline, social, newsletter, copyright. Category navigation. Hydrate `immediate`. Variants: none; layout via `style.layout`. Hydration mode: author your own `<footer data-lx-footer="root">` with optional `newsletter-form`, `newsletter-input`, `newsletter-success`, `year` tags. Max 1, last section. Footer may paint its own background (house-rule exception).

UI-controlling props:

| Prop | Type | Values |
|---|---|---|
| `style.layout` | enum | `simple` \| `centered` \| `columns` \| `editorialGrid` \| `newsletterSplit` |
| `style.bgColor, textColor, linkColor, linkHoverColor, headingColor, accentColor, borderColor` | string | colors |
| `style.fontFamily, fontSize, padding, maxWidth, logoHeight, logoFilter` | string | type, spacing, logo treatment (`logoFilter: "invert(1)"` for dark footers) |
| `borderStyle` | enum | `none` \| `solid` \| `dashed` (top rule) |
| `tileLayout` | boolean | social links as tiles (`social-tiles` part) |

Data props: `columns[{heading?, links[{label,url}]}]`, `links[]` (simple layout), `logo{src, alt}`, `tagline`, `copyright`, `socialLinks[{platform, url, icon?}]`, `newsletter{heading, placeholder, buttonText}`, `successMessage`.
CSS vars: `--lx-accent-color`. Parts: `root, columns, nav-rows, newsletter, social-tiles`.
Fallback: hydration-mode markup, or a `<footer>` with links and copyright.
Gotchas: social icons are the island's own glyphs; `socialLinks[].icon` accepts a string (URL or inline SVG; unconfirmed which). If the page has no icon set, prefer text social links via `columns` and omit `socialLinks`. Old `layouts/compact.json` uses `style.variant`/`style.inline`/`newsletter.enabled`, none of which exist in v5.1.

### 2.10 ReviewCarousel

Rotating or grid review showcase with stars, verified flag, avatars, optional media. Category social_proof. Hydrate `visible`. Headless: no. Two data modes: static `reviews[]` (wins if non-empty) or fetch (`collectionId` or `productIds` + filters; the page supplies the endpoint at runtime, never write `reviewsEndpoint`). Mid-page or after product details, never first. Needs 3+ real reviews; never fabricate.

UI-controlling props:

| Prop | Type | Values / default | Effect |
|---|---|---|---|
| `variant` | enum | `default` \| `compact` \| `minimal` \| `grid` (default `default`) | default = one card carousel; compact = short strip; minimal = quote-only (short bodies only); grid = all at once |
| `autoplay` | boolean | true | set false for grid and for quiet pages |
| `interval` | number | 5000, keep >= 4000 | - |
| `pageSize` | number | 10, max 20 | fetch mode count |

Data props: `reviews[{id?, author, rating, title?, body, date?, verified?, avatar?, helpful_count?, media[]?}]` (static, only real reviews from `lexsis_catalog.reviews`), or fetch mode `collectionId` (an active collection from the plan's Proof sources line) or `productIds[]`, plus `reviewSnapshotId`, `minRating`, `sort` (`recent|highest|most_helpful`). Omit `reviewsEndpoint`.
CSS vars: `--lx-accent-color` (avatar bg, active dot), `--lx-text-color` (author). Parts: `root, card, avatar, author, body, title, date, verified, media-preview, nav-prev, nav-next, dots, dot, load-more`.
Fallback: 3 static blockquotes with author lines.
Gotchas: stars and the verified check are island glyphs (not controllable); acceptable as the page's single icon set only if the rest of the page uses no other icons, otherwise hide `[data-part="verified"]` and rely on the "Verified" text. `index.md` mentions `card-grid` on `--lx-surface-alt` backgrounds; house rules forbid that, so cards sit on the page background with a hairline border. `card` default may carry a shadow; flatten via `[data-part="card"]{box-shadow:none;border:1px solid var(--lx-border-color)}`.

### 2.11 InventoryIndicator

Low-stock urgency: "Only X left" pill, progress bar, or inline text. Category commerce. Hydrate `immediate`. Headless: no. Auto-hides above `lowStockThreshold`; can listen for `variant:changed`.

UI-controlling props: `variant` (`badge` default | `bar` | `text`), `showExactCount` (boolean, default true), `lowStockThreshold` (number, default 5; controls when it appears), `urgentThreshold` (number, default 3; colour escalation).
Data props: `variantId`, `quantity` (number; static preview value), `listenForEvents` (boolean, default false).
CSS vars: `--lx-inventory-urgent-color`, `--lx-inventory-low-color`, `--lx-inventory-ok-color` (state colours; fall back to the island defaults). Parts: `root, dot, message, bar-track, bar-fill`.
Fallback: none; the island hides itself when stock is high, so an empty child is correct.
Gotchas: set the three state vars in the section `<style>` when the brand palette has no red. Do not use for pre-order products.

### 2.12 DeliveryEstimate

"Order within Xh, arrives by <date>" line with optional free-shipping threshold. Category commerce. Hydrate `immediate`. Headless: no. Countdown updates each minute; returns nothing after cutoff.

UI-controlling props: `variant` (`inline` default | `card` | `banner`), `showCountdown` (boolean, default true).
Data props: `estimatedDays` (number, default 4), `cutoffHour` (number 0-23, default 14; store timezone, unconfirmed), `freeShippingThreshold` (number, minor units per example `5000`; unconfirmed currency handling).
CSS vars: `--lx-accent-color, --lx-text-color`. Parts: `root, icon, text, date`.
Fallback: one `<p>` "Ships in {{shipping.days}} business days".
Gotchas: `card` and `banner` variants paint their own surface, which violates the one-background rule; presets use `inline` only, or `card` with `[data-part="root"]{background:transparent;border:1px solid var(--lx-border-color)}`. The `icon` part is an island glyph; hide it when the page has no icon set. Keep it out of pages with international or variable shipping.

#### Shared notes for section 2

- **Fallback child.** `design-page/references/island-preview.md` asks for a direct `data-lx-island-fallback` child inside `<lx-island>`; `build_page_preview.py` does not reference that attribute, so its runtime handling is unconfirmed. Keep fallback markup simple, class-free or Tailwind-only (every class must compile), and free of interactive controls that could be mistaken for the island.
- **`animate` type.** Schema shows `boolean|boolean|string|string|string` for BuyBox, StickyBar, ProductCarousel; accepted string values are undocumented. Presets use booleans only.
- **Manifest evidence per island** (from `validate_page_workspace.py`): `{sectionId, name, schemaVersion, lifecycleStatus:"active", mode:"native"|"headless", previewMode:"hydrated"|"fallback"}`, in source order.

## 3. Presets

Conventions: id is `<island-lowercase>/<intent>-<tone>`. Each preset is `props` (goes verbatim into the `<script type="application/json">`) plus optional `css` (goes into the section `<style>`, scoped by the island wrapper id `{{id}}`). Placeholders `{{...}}` are replaced by `/design-page` from catalog, brand and plan data. Colour strings use `var(--lx-*)` tokens; island `style.*` props are applied as inline styles so `var()` resolves (confirmed for hex, expected for `var()`; verify on first compile). Tones: `light` = page background, dark text; `dark` = inverted strip (`--lx-text-color` bg); `quiet` = no motion, no chrome; `editorial` = square corners, hairlines, letterspaced caps.

### 3.1 SiteHeader

**siteheader/sticky-light** - default PDP/landing header: inverted announcement strip, white nav with hairline. Use when the plan has an announcement message.
```json
{"props":{"sticky":true,"cartMode":"drawer","announcement":{"messages":["{{announcement.message_1}}","{{announcement.message_2}}"],"speed":5000,"dismissible":false,"backgroundColor":"var(--lx-text-color)","textColor":"var(--lx-bg-color)"},"navbar":{"logo":{"src":"{{brand.logo_url}}","alt":"{{brand.name}}","url":"/"},"links":"{{nav.links}}","style":{"bgColor":"var(--lx-bg-color)","textColor":"var(--lx-text-color)","accentColor":"var(--lx-accent-color)","height":"64px","logoHeight":"28px","maxWidth":"1280px","fontFamily":"var(--lx-font-body)","fontSize":"14px","fontWeight":"500","borderBottom":"1px solid var(--lx-border-color)","dropdownBg":"var(--lx-bg-color)","dropdownTextColor":"var(--lx-text-color)","mobileBg":"var(--lx-bg-color)","mobileTextColor":"var(--lx-text-color)"}}}}
```

**siteheader/transparent-dark** - nav floats over the plan's single full-bleed hero, text light, no announcement. Use only when the section directly below is that full-bleed moment.
```json
{"props":{"sticky":true,"transparent":true,"cartMode":"drawer","navbar":{"logo":{"src":"{{brand.logo_url_light}}","alt":"{{brand.name}}","url":"/"},"links":"{{nav.links}}","transparent":true,"style":{"textColor":"#ffffff","accentColor":"#ffffff","height":"72px","logoHeight":"28px","maxWidth":"1280px","fontSize":"14px","fontWeight":"500","borderBottom":"none","mobileBg":"var(--lx-text-color)","mobileTextColor":"var(--lx-bg-color)"}}}}
```

**siteheader/minimal-light** - non-sticky, no announcement, one CTA. Use for campaign landing pages with a single conversion goal.
```json
{"props":{"sticky":false,"cartMode":"link","cartUrl":"/cart","navbar":{"logo":{"text":"{{brand.name}}","url":"/"},"links":[{"label":"Shop","url":"{{nav.shop_url}}"}],"cta":{"label":"{{cta.text}}","url":"#buy"},"style":{"bgColor":"var(--lx-bg-color)","textColor":"var(--lx-text-color)","accentColor":"var(--lx-accent-color)","height":"72px","fontSize":"14px","fontWeight":"400","borderBottom":"none","maxWidth":"1280px"}}}}
```
```css
#{{id}} [data-part="cta"]{border-radius:var(--lx-radius,8px);padding:10px 18px}
```

### 3.2 Navbar

**navbar/sticky-light** - same look as siteheader/sticky-light without the strip. Use when no announcement, or when pairing with `announcementbar/*` that should scroll away.
```json
{"props":{"sticky":true,"cartMode":"drawer","logo":{"src":"{{brand.logo_url}}","alt":"{{brand.name}}","url":"/"},"links":"{{nav.links}}","cart":{"icon":"bag"},"style":{"bgColor":"var(--lx-bg-color)","textColor":"var(--lx-text-color)","accentColor":"var(--lx-accent-color)","height":"64px","logoHeight":"28px","maxWidth":"1280px","fontSize":"14px","fontWeight":"500","borderBottom":"1px solid var(--lx-border-color)","dropdownBg":"var(--lx-bg-color)","dropdownTextColor":"var(--lx-text-color)","mobileBg":"var(--lx-bg-color)","mobileTextColor":"var(--lx-text-color)"}}}
```

**navbar/transparent-dark** - light text over the hero, CTA pill. Use only above the plan's full-bleed moment.
```json
{"props":{"sticky":true,"transparent":true,"cartMode":"drawer","logo":{"src":"{{brand.logo_url_light}}","alt":"{{brand.name}}","url":"/"},"links":"{{nav.links}}","cta":{"label":"{{cta.text}}","url":"#buy"},"cart":{"icon":"bag","badgeColor":"#ffffff"},"style":{"textColor":"#ffffff","accentColor":"#ffffff","height":"72px","logoHeight":"28px","borderBottom":"none","mobileBg":"var(--lx-text-color)","mobileTextColor":"var(--lx-bg-color)"}}}
```
```css
#{{id}} [data-part="cta"]{background:#ffffff;color:var(--lx-text-color);border-radius:9999px;padding:10px 18px}
```

### 3.3 AnnouncementBar

**announcementbar/static-dark** - one message, inverted strip, no controls. Use for shipping or guarantee line.
```json
{"props":{"messages":["{{announcement.message_1}}"],"backgroundColor":"var(--lx-text-color)","textColor":"var(--lx-bg-color)","dismissible":false,"sticky":false}}
```
```css
#{{id}} [data-part="icon"]{display:none}
#{{id}} [data-part="text"]{font-size:13px;letter-spacing:.02em}
```

**announcementbar/rotating-accent** - 2-3 rotating promo lines on the accent colour. Use during a campaign window; pair with `navbar/sticky-light`.
```json
{"props":{"messages":["{{announcement.message_1}}","{{announcement.message_2}}","{{announcement.message_3}}"],"speed":5000,"backgroundColor":"var(--lx-accent-color)","textColor":"#ffffff","link":"{{announcement.url}}","dismissible":false,"sticky":false}}
```
```css
#{{id}} [data-part="icon"]{display:none}
```


### 3.4 ProductGallery

Shared flat-chrome CSS used by all three (flatten arrows, dots, no island surface):
```css
#{{id}}{--lx-product-gallery-bg:transparent;--lx-media-carousel-bg:transparent;--lx-media-carousel-arrow-bg:var(--lx-bg-color);--lx-media-carousel-arrow-border:1px solid var(--lx-border-color);--lx-media-carousel-arrow-color:var(--lx-text-color);--lx-media-carousel-arrow-hover-bg:var(--lx-bg-color);--lx-media-carousel-arrow-shadow:none;--lx-media-carousel-arrow-radius:9999px;--lx-media-carousel-arrow-size:40px;--lx-media-carousel-dot-color:var(--lx-border-color);--lx-media-carousel-dot-active-color:var(--lx-text-color);--lx-media-carousel-dot-active-scale:1;--lx-media-carousel-dot-shadow:none;--lx-product-gallery-focus-width:2px;--lx-media-lightbox-backdrop:rgba(0,0,0,.92);--lx-media-lightbox-close-bg:transparent;--lx-media-lightbox-close-border:1px solid rgba(255,255,255,.4);--lx-media-lightbox-close-color:#ffffff}
```

**productgallery/rail-bottom-light** - main image with thumbnail strip below, rounded, lightbox. Default PDP gallery.
```json
{"props":{"media":"{{product.media}}","layout":"horizontal","thumbPosition":"bottom","mobileLayout":"swipe","transition":"fade","objectFit":"cover","enableLightbox":true,"autoplay":false,"listenForVariant":false}}
```
```css
#{{id}}{--lx-product-gallery-radius:var(--lx-radius,12px);--lx-product-gallery-gap:12px;--lx-product-gallery-mobile-ratio:1/1}
#{{id}} [data-part="thumbnail"]{border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,8px)}
```

**productgallery/rail-left-editorial** - vertical rail on the left, square corners, `contain` for packshots, no transition. Use for fashion or premium goods with studio imagery.
```json
{"props":{"media":"{{product.media}}","layout":"vertical","thumbPosition":"left","mobileLayout":"swipe","transition":"none","objectFit":"contain","enableLightbox":true,"autoplay":false}}
```
```css
#{{id}}{--lx-product-gallery-radius:0;--lx-media-carousel-radius:0;--lx-media-carousel-arrow-radius:0;--lx-product-gallery-gap:16px;--lx-product-gallery-border:1px solid var(--lx-border-color)}
#{{id}} [data-part="thumbnail"]{border-radius:0;border:1px solid transparent}
```

**productgallery/stacked-quiet** - all images stacked full-width on desktop, swipe rail on mobile, no lightbox, no motion. Use for long-scroll editorial PDPs where the BuyBox is sticky beside the media.
```json
{"props":{"media":"{{product.media}}","layout":"stacked","mobileLayout":"swipe","transition":"none","objectFit":"cover","enableLightbox":false,"autoplay":false}}
```
```css
#{{id}}{--lx-product-gallery-radius:var(--lx-radius,8px);--lx-product-gallery-gap:8px;--lx-product-gallery-stacked-ratio:4/5;--lx-product-gallery-mobile-peek:24px}
```

### 3.5 ProductHero

**producthero/split-rail-light** - hero beside BuyBox, thumbnails under the image, arrows inside frame, capped height. Default premium PDP.
```json
{"props":{"images":"{{product.hero_images}}","layout":"splitLeft","thumbnails":"rail","thumbnailPosition":"bottom","navigation":"arrows","aspectRatio":"4:5","maxHeight":"640px","transition":"fade","autoplay":false,"hoverAdvance":false}}
```
```css
#{{id}}{--lx-hero-bg:transparent;--lx-hero-radius:var(--lx-radius,12px);--lx-hero-thumb-radius:var(--lx-radius,8px);--lx-hero-thumb-size:64px;--lx-hero-thumb-gap:8px;--lx-hero-arrow-bg:var(--lx-bg-color);--lx-hero-arrow-size:40px;--lx-hero-arrow-offset:12px;--lx-hero-transition-duration:300ms}
#{{id}} [data-part="thumbnail"]{border:1px solid var(--lx-border-color)}
```

**producthero/stacked-dots-quiet** - square image, dots only, no arrows, mobile-first. Use when the product has 2-4 images and the page is copy-led.
```json
{"props":{"images":"{{product.hero_images}}","layout":"stacked","thumbnails":"dots","navigation":"none","showIndicators":true,"aspectRatio":"1:1","maxHeight":"560px","transition":"fade","autoplay":false,"hoverAdvance":false}}
```
```css
#{{id}}{--lx-hero-bg:transparent;--lx-hero-radius:var(--lx-radius,12px);--lx-hero-transition-duration:250ms}
#{{id}} [data-part="dot"]{background:var(--lx-border-color)}
```

**producthero/fullheight-sharp-dark** - full-height, square corners, floating arrows on dark chips, no thumbnails. Use only as the plan's one full-bleed moment (pairs with `siteheader/transparent-dark`).
```json
{"props":{"images":"{{product.hero_images}}","layout":"fullHeight","thumbnails":"none","navigation":"floatingArrows","aspectRatio":"3:4","maxHeight":"85vh","transition":"slide","autoplay":false,"hoverAdvance":false}}
```
```css
#{{id}}{--lx-hero-bg:var(--lx-text-color);--lx-hero-radius:0;--lx-hero-arrow-bg:rgba(0,0,0,.6);--lx-hero-arrow-size:44px;--lx-hero-arrow-offset:16px;--lx-hero-transition-duration:400ms}
```

### 3.6 BuyBox

Data block shared by all BuyBox presets: `"product":{"title":"{{product.title}}","price":"{{product.price}}","compareAtPrice":"{{product.compare_at_price}}","variants":"{{product.variants}}"}` where `{{product.variants}}` expands to `[{"id":"gid://shopify/ProductVariant/...","title":"...","price":"...","available":true}]`.

**buybox/default-light** - variant buttons, quantity, accent CTA with the page radius, no trust badges (page owns its icons). Default PDP.
```json
{"props":{"product":"{{product}}","variant":"default","ctaText":"{{cta.text}}","showPrice":true,"showVariantSelector":true,"showTrustBadges":false,"animate":true,"buttonStyle":{"borderRadius":"var(--lx-radius,8px)","padding":"16px 24px","fontSize":"15px"}}}
```
```css
#{{id}} [data-part="variant-btn"]{border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,8px);background:transparent;color:var(--lx-text-color)}
#{{id}} [data-part="qty"],#{{id}} [data-part="qty-btn"]{border-color:var(--lx-border-color);border-radius:var(--lx-radius,8px)}
```

**buybox/compact-dark** - single-variant product, no quantity, black square CTA with letterspaced label. Use in bundles, upsell rows, or sticky sidebars.
```json
{"props":{"product":"{{product}}","variant":"compact","ctaText":"{{cta.text}}","showPrice":true,"showTrustBadges":false,"animate":false,"buttonStyle":{"borderRadius":"0","padding":"18px 28px","fontSize":"13px"}}}
```
```css
#{{id}} [data-part="cta"]{background:var(--lx-text-color);color:var(--lx-bg-color);text-transform:uppercase;letter-spacing:.08em;font-weight:600}
```

**buybox/expanded-editorial** - expanded layout, pill CTA and pill variant buttons; trust badges on only when the page has no other icon set. Use for premium PDPs with a long BuyBox column.
```json
{"props":{"product":"{{product}}","variant":"expanded","ctaText":"{{cta.text}}","showPrice":true,"showVariantSelector":true,"showTrustBadges":"{{page.icon_set == 'none'}}","animate":true,"buttonStyle":{"borderRadius":"9999px","padding":"18px 32px","fontSize":"15px"}}}
```
```css
#{{id}} [data-part="variant-btn"]{border-radius:9999px;border:1px solid var(--lx-border-color);background:transparent;padding:8px 16px;font-size:13px}
#{{id}} [data-part="trust-badges"]{opacity:.8;font-size:13px}
```

### 3.7 StickyBar

**stickybar/product-light** - page-coloured bar, hairline top, accent CTA, appears after the BuyBox section. Default PDP.
```json
{"props":{"product":{"title":"{{product.title}}","price":"{{product.price}}","compareAtPrice":"{{product.compare_at_price}}","image":"{{product.image_thumb}}","variantId":"{{product.default_variant_id}}"},"cta":"{{cta.text}}","showAfter":"#{{sections.buybox.id}}","animate":true}}
```
```css
#{{id}} [data-part="bar"]{background:var(--lx-bg-color);color:var(--lx-text-color);border-top:1px solid var(--lx-border-color);box-shadow:none}
#{{id}} [data-part="cta"]{border-radius:var(--lx-radius,8px)}
#{{id}} [data-part="product-image"]{border-radius:var(--lx-radius,6px)}
```

**stickybar/product-dark** - inverted bar, no image, no animation. Use on quiet or editorial pages.
```json
{"props":{"product":{"title":"{{product.title}}","price":"{{product.price}}","variantId":"{{product.default_variant_id}}"},"cta":"{{cta.text}}","showAfter":"#{{sections.buybox.id}}","animate":false}}
```
```css
#{{id}} [data-part="bar"]{background:var(--lx-text-color);color:var(--lx-bg-color);box-shadow:none}
#{{id}} [data-part="cta"]{background:var(--lx-bg-color);color:var(--lx-text-color);border-radius:0}
#{{id}} [data-part="product-price"]{color:var(--lx-bg-color);opacity:.8}
```

**stickybar/collection-light** - collection/campaign destination instead of add-to-cart. Use on listicle, gift-guide and collection landers.
```json
{"props":{"collection":{"label":"{{collection.cta_label}}","url":"{{collection.url}}","subtitle":"{{collection.subtitle}}"},"showAfter":"#{{sections.first_content.id}}","animate":true}}
```
```css
#{{id}} [data-part="bar"]{background:var(--lx-bg-color);border-top:1px solid var(--lx-border-color);box-shadow:none}
```

### 3.8 ProductCarousel

Shared flat-chrome CSS (same arrow/dot variables as the gallery):
```css
#{{id}}{--lx-media-carousel-arrow-bg:var(--lx-bg-color);--lx-media-carousel-arrow-border:1px solid var(--lx-border-color);--lx-media-carousel-arrow-color:var(--lx-text-color);--lx-media-carousel-arrow-shadow:none;--lx-media-carousel-arrow-radius:9999px;--lx-media-carousel-dot-color:var(--lx-border-color);--lx-media-carousel-dot-active-color:var(--lx-text-color);--lx-media-carousel-dot-shadow:none;--lx-media-carousel-radius:var(--lx-radius,8px)}
#{{id}} [data-part="card-wrapper"]{background:transparent;border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,8px);box-shadow:none;transition:none}
#{{id}} [data-part="badge"]{border-radius:var(--lx-radius,4px);background:var(--lx-text-color);color:var(--lx-bg-color)}
```

**productcarousel/cards-quiet** - plain cards, no actions, no hover media, no entry animation; section owns the h2. Default "You may also like".
```json
{"props":{"products":"{{related.products}}","cardVariant":"default","showQuickAdd":false,"showLearnMore":false,"showWishlist":false,"showQuickView":false,"hoverAdvance":false,"mediaTransition":"none","animate":false}}
```

**productcarousel/cards-quickadd-light** - adds the quick-add button (requires `head.use_cart_v2:true`), fade media swap, entry fade. Use on collection and bundle pages.
```json
{"props":{"products":"{{related.products}}","cardVariant":"default","showQuickAdd":true,"showLearnMore":false,"showWishlist":false,"showQuickView":false,"hoverAdvance":false,"mediaTransition":"fade","animate":true}}
```
```css
#{{id}} [data-part="quick-add"]{border-radius:var(--lx-radius,8px);background:var(--lx-accent-color);color:#ffffff}
```

**productcarousel/rows-compact** - list rows (image, title, price) for sidebars and "complete the set". Use with 3-5 products.
```json
{"props":{"products":"{{related.products}}","cardVariant":"compactRows","showQuickAdd":false,"showLearnMore":false,"hoverAdvance":false,"mediaTransition":"none","animate":false}}
```
```css
#{{id}} [data-part="row"]{border-bottom:1px solid var(--lx-border-color);padding:12px 0}
#{{id}} [data-part="row-image"]{border-radius:var(--lx-radius,6px)}
```

### 3.9 Footer

**footer/columns-dark** - inverted footer, 3-4 link columns, text social links (no glyphs), no newsletter. Default.
```json
{"props":{"logo":{"src":"{{brand.logo_url}}","alt":"{{brand.name}}"},"tagline":"{{brand.tagline}}","columns":"{{footer.columns}}","copyright":"{{brand.copyright}}","borderStyle":"none","tileLayout":false,"style":{"layout":"columns","bgColor":"var(--lx-text-color)","textColor":"var(--lx-bg-color)","linkColor":"var(--lx-bg-color)","linkHoverColor":"var(--lx-accent-color)","headingColor":"var(--lx-bg-color)","accentColor":"var(--lx-accent-color)","borderColor":"rgba(255,255,255,.15)","fontFamily":"var(--lx-font-body)","fontSize":"14px","padding":"64px 0 32px","maxWidth":"1280px","logoHeight":"24px","logoFilter":"invert(1)"}}}
```

**footer/simple-light** - one row of links, hairline top, page background. Use on campaign landers.
```json
{"props":{"logo":{"src":"{{brand.logo_url}}","alt":"{{brand.name}}"},"links":"{{footer.links}}","copyright":"{{brand.copyright}}","borderStyle":"solid","style":{"layout":"simple","bgColor":"var(--lx-bg-color)","textColor":"var(--lx-text-muted)","linkColor":"var(--lx-text-color)","linkHoverColor":"var(--lx-accent-color)","borderColor":"var(--lx-border-color)","fontSize":"13px","padding":"32px 0","maxWidth":"1280px","logoHeight":"20px"}}}
```

**footer/newsletter-split-light** - newsletter on one side, columns on the other, page background with hairline. Use when the plan names email capture as a goal and no EmailCapture island is on the page.
```json
{"props":{"logo":{"src":"{{brand.logo_url}}","alt":"{{brand.name}}"},"columns":"{{footer.columns}}","newsletter":{"heading":"{{newsletter.heading}}","placeholder":"Email address","buttonText":"Subscribe"},"successMessage":"Thanks, you are on the list.","copyright":"{{brand.copyright}}","borderStyle":"solid","style":{"layout":"newsletterSplit","bgColor":"var(--lx-bg-color)","textColor":"var(--lx-text-color)","linkColor":"var(--lx-text-color)","linkHoverColor":"var(--lx-accent-color)","headingColor":"var(--lx-text-color)","accentColor":"var(--lx-accent-color)","borderColor":"var(--lx-border-color)","fontSize":"14px","padding":"64px 0 32px","maxWidth":"1280px","logoHeight":"24px"}}}
```
```css
#{{id}} [data-part="newsletter"] input{border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,8px);background:transparent}
#{{id}} [data-part="newsletter"] button{border-radius:var(--lx-radius,8px)}
```

### 3.10 ReviewCarousel

Shared flat card CSS:
```css
#{{id}} [data-part="card"]{background:transparent;border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,12px);box-shadow:none}
#{{id}} [data-part="nav-prev"],#{{id}} [data-part="nav-next"]{background:var(--lx-bg-color);border:1px solid var(--lx-border-color);color:var(--lx-text-color);box-shadow:none}
#{{id}} [data-part="dot"]{background:var(--lx-border-color)}
```

**reviewcarousel/grid-flat** - all reviews visible, no motion. Default when 3-6 reviews.
```json
{"props":{"collectionId":"{{reviews.collection_id}}","minRating":4,"pageSize":8,"variant":"grid","autoplay":false}}
```

**reviewcarousel/single-quiet** - one card at a time, manual arrows, no autoplay. Use when review bodies are long.
```json
{"props":{"collectionId":"{{reviews.collection_id}}","minRating":4,"pageSize":6,"variant":"default","autoplay":false,"interval":6000}}
```

**reviewcarousel/strip-compact** - short strip of one-line reviews with slow rotation. Use near the BuyBox as a proof line, bodies under 60 chars.
```json
{"props":{"collectionId":"{{reviews.collection_id}}","minRating":4,"pageSize":6,"variant":"compact","autoplay":true,"interval":6000}}
```
```css
#{{id}} [data-part="verified"]{display:none}
```

### 3.11 InventoryIndicator

**inventoryindicator/text-quiet** - inline sentence under the price, shows only below 10 units. Default.
```json
{"props":{"variantId":"{{product.default_variant_id}}","quantity":"{{product.inventory_quantity}}","variant":"text","showExactCount":true,"lowStockThreshold":10,"urgentThreshold":3,"listenForEvents":true}}
```
```css
#{{id}} [data-part="message"]{color:var(--lx-text-muted);font-size:13px}
#{{id}} [data-part="dot"]{background:var(--lx-accent-color)}
```

**inventoryindicator/bar-accent** - thin progress bar in the accent colour. Use for drops and limited runs.
```json
{"props":{"variantId":"{{product.default_variant_id}}","quantity":"{{product.inventory_quantity}}","variant":"bar","showExactCount":true,"lowStockThreshold":25,"urgentThreshold":5,"listenForEvents":true}}
```
```css
#{{id}} [data-part="bar-track"]{background:var(--lx-border-color);height:4px;border-radius:9999px}
#{{id}} [data-part="bar-fill"]{background:var(--lx-accent-color);border-radius:9999px}
```

**inventoryindicator/badge-outline** - outlined pill, no exact count. Use when stock numbers should stay private.
```json
{"props":{"variantId":"{{product.default_variant_id}}","quantity":"{{product.inventory_quantity}}","variant":"badge","showExactCount":false,"lowStockThreshold":5,"urgentThreshold":2,"listenForEvents":true}}
```
```css
#{{id}} [data-part="root"]{background:transparent;border:1px solid var(--lx-border-color);color:var(--lx-text-color);border-radius:9999px;padding:4px 10px;font-size:12px}
```

### 3.12 DeliveryEstimate

**deliveryestimate/inline-quiet** - one muted line, no icon, countdown on. Default under the BuyBox CTA.
```json
{"props":{"variant":"inline","estimatedDays":"{{shipping.days}}","cutoffHour":"{{shipping.cutoff_hour}}","showCountdown":true}}
```
```css
#{{id}} [data-part="icon"]{display:none}
#{{id}} [data-part="text"]{color:var(--lx-text-muted);font-size:13px}
#{{id}} [data-part="date"]{color:var(--lx-text-color);font-weight:600}
```

**deliveryestimate/card-outline** - card variant with its surface removed, hairline border, free-shipping threshold. Use in a "shipping and returns" block.
```json
{"props":{"variant":"card","estimatedDays":"{{shipping.days}}","cutoffHour":"{{shipping.cutoff_hour}}","showCountdown":true,"freeShippingThreshold":"{{shipping.free_threshold_minor}}"}}
```
```css
#{{id}} [data-part="root"]{background:transparent;border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,12px);box-shadow:none}
#{{id}} [data-part="icon"]{display:none}
```

`banner` variant intentionally has no preset: it paints a full-width surface, which breaks the one-background rule.

## 4. Preset system proposal

Goal: a plan says `BuyBox: preset buybox/compact-dark`; design applies exact props and CSS; compile and the validator can prove it. Smallest change that does this: one reference file, one line in `page-plan.md` per section, one field per manifest island. No new tool, no runtime change.

### 4.1 File location and shape

`skills/storefront-engine/references/island-presets.md` (loaded by `/plan-page` for `Preset:` ids and by `/design-page` next to `design-rules.md`). One `##` per island, one `###` per preset id, each with a single fenced `json` block containing the whole preset entry (props + css + metadata). Markdown keeps it human-reviewable; the fenced block is machine-extractable with the same regex the validator already uses for `<script type="application/json">`.

Optionally mirror as `skills/design-page/assets/island-presets.json` (array of entries) if a script needs to load it; generate it from the `.md`, do not hand-maintain two copies.

### 4.2 Preset entry schema (minimal JSON Schema)

```json
{"$schema":"https://json-schema.org/draft/2020-12/schema","title":"LexsisIslandPreset","type":"object","required":["id","island","schemaVersion","props"],"additionalProperties":false,
 "properties":{
  "id":{"type":"string","pattern":"^[a-z]+/[a-z0-9]+(-[a-z0-9]+)+$","description":"<island-lowercase>/<intent>-<tone>"},
  "island":{"type":"string","description":"Exact runtime island name, e.g. BuyBox"},
  "schemaVersion":{"type":"string","description":"island_schema version the preset was verified against, e.g. 5.1.0"},
  "hydrate":{"type":"string","enum":["immediate","visible","idle","interaction"]},
  "mode":{"type":"string","enum":["native","headless"],"default":"native"},
  "props":{"type":"object","description":"Verbatim island props; string values may contain {{placeholders}}"},
  "css":{"type":"string","description":"Section CSS scoped with #{{id}}; only [data-part] selectors and --lx-* variables"},
  "requires":{"type":"object","properties":{"cartV2":{"type":"boolean"},"iconSet":{"type":"string","enum":["none","page"]},"fullBleedMoment":{"type":"boolean"},"minItems":{"type":"integer"}}},
  "placeholders":{"type":"array","items":{"type":"string"},"description":"Every {{token}} used, so design can check bindings"},
  "use":{"type":"string","description":"One line: when to pick it"},
  "houseRules":{"type":"array","items":{"type":"string"},"description":"Rules this preset was checked against: no-emoji, no-gradient, one-background, one-icon-set, no-motion-effects"}
 }}
```

Example entry:
```json
{"id":"buybox/compact-dark","island":"BuyBox","schemaVersion":"5.1.0","hydrate":"immediate","mode":"native","props":{"product":"{{product}}","variant":"compact","ctaText":"{{cta.text}}","showTrustBadges":false,"animate":false,"buttonStyle":{"borderRadius":"0","padding":"18px 28px","fontSize":"13px"}},"css":"#{{id}} [data-part=\"cta\"]{background:var(--lx-text-color);color:var(--lx-bg-color);text-transform:uppercase;letter-spacing:.08em}","requires":{"cartV2":true},"placeholders":["product","cta.text"],"use":"Single-variant product in bundles, upsell rows, sticky sidebars.","houseRules":["no-emoji","no-gradient","one-background","one-icon-set","no-motion-effects"]}
```

### 4.3 How `/plan-page` selects

`plan-page/SKILL.md` today forbids island names and props in the plan. Keep that for props, relax it for preset ids: a preset id is a *design intent token*, not implementation. Add one optional line per section in `page-plan.md`:

```text
## Sections
3. Buy
   Purpose: convert; primary CTA.
   Preset: buybox/compact-dark, stickybar/product-dark
```

Rules: ids must exist in `island-presets.md`; the plan lists at most one preset per island role; the plan's "Design direction" block names the tone once (`light`, `dark`, `quiet`, `editorial`) and every chosen preset's tone must match it or be listed as an explicit exception. Header and footer presets are picked in the "Design direction" block, not per section.

### 4.4 How `/design-page` applies and overrides

1. Read `island-presets.md`; for each `Preset:` line resolve the entry. Unknown id = stop and ask (return `PRESET_NOT_FOUND`).
2. Check `requires`: `cartV2` -> `head.use_cart_v2:true`; `iconSet:"none"` -> the page uses no other icons; `fullBleedMoment` -> the plan names one; `minItems` -> enough products/reviews. Fail = pick the sibling preset with the same intent or return `PRESET_REQUIREMENT_UNMET`.
3. Emit `<lx-island name="{{island}}" id="{{sectionId}}-{{islandLower}}" hydrate="{{hydrate}}">` with `props` after placeholder substitution, and append `css` (with `#{{id}}` substituted) to that section's `<style>`.
4. Overrides: a section may add `Preset override:` lines in the plan or the designer may deviate; every deviation is recorded in the manifest as `islands[].presetOverrides` (JSON merge patch against the preset props) and in `page-plan.md` under "Design direction". No silent edits to preset props.
5. Never edit a preset in place for one page; add a new id if a new look is needed.

### 4.5 How compile validates

- `lexsis_pages compile` remains the authority for prop shape; presets are pre-validated once per `schemaVersion`, so a compile error on a preset-applied island means either an override or a schema drift. Log the island `version` from `island_schema` and fail fast when it differs from `preset.schemaVersion`.
- Extend `validate_page_workspace.py` (design phase) with three cheap checks: (a) every `islands[].preset` id exists in the preset file; (b) props in source equal preset props after substitution plus recorded `presetOverrides` (deep-equal after removing `{{...}}`-bound keys); (c) preset `css` text is present in the section's `<style>`. Emit `island_preset_mismatch` as a blocking finding in `SOURCE_PHASES`.
- House-rule checks already in `design-rules.md` (emoji grep, distinct backgrounds) run unchanged; presets are pre-checked against them, and `houseRules` records which.

### 4.6 Manifest

`islands[]` already carries `{sectionId, name, schemaVersion, lifecycleStatus, mode, previewMode}`. Add:

```json
{"sectionId":"buy","name":"BuyBox","schemaVersion":"5.1.0","lifecycleStatus":"active","mode":"native","previewMode":"hydrated","preset":"buybox/compact-dark","presetOverrides":{"ctaText":"Add to bag"}}
```

`preset` is a string or `null` (custom composition, rationale in `page-plan.md`). `presetOverrides` omitted when empty. `design.stylePack` stays; a preset set is not a style pack, but when a page uses presets of a single tone, record `design.presetTone`.

Source: `work/research/lexsis-island-presets.md`.
