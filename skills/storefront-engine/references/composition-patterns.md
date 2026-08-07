# Composition Patterns

Concrete HTML patterns for building pages with composable primitives.

---

## Product Card (custom HTML + primitives)

```html
<div class="product-card" data-scope="product:{{handle}}">
  <a href="/products/{{handle}}" class="product-card__link">
    <div class="product-card__media">
      <div data-island="MediaCarousel" data-hydrate="visible" data-props='{
        "media": [{"src":"{{image1}}","alt":"{{title}}"},{"src":"{{image2}}","alt":"{{title}} alt"}],
        "hoverAdvance": true,
        "showDots": true,
        "aspect": "3:4",
        "transition": "fade"
      }'></div>
    </div>
    <div class="product-card__info">
      <h3 class="product-card__title">{{title}}</h3>
      <p class="product-card__price">{{price}}</p>
    </div>
  </a>
  <div class="product-card__action">
    <div data-island="QuickAdd" data-hydrate="interaction" data-props='{
      "product": {"title":"{{title}}","variants":[{"id":"{{variantId}}","title":"Default","price":"{{price}}","available":true}],"image":"{{image1}}"},
      "render": "icon",
      "iconSize": 36
    }'></div>
  </div>
</div>
```

**CSS for card:**
```css
.product-card { position: relative; }
.product-card__link { text-decoration: none; color: inherit; }
.product-card__media { border-radius: 0.5rem; overflow: hidden; }
.product-card__info { padding: 0.75rem 0; }
.product-card__title { font-size: 0.875rem; font-weight: 500; margin: 0; }
.product-card__price { font-size: 0.8125rem; color: #6b7280; margin: 0.25rem 0 0; }
.product-card__action { position: absolute; bottom: 4.5rem; right: 0.75rem; z-index: 5; }
```

---

## Product Grid (CSS Grid + cards)

```html
<div class="product-grid" data-behavior="scroll-reveal" data-config='{"stagger":80}'>
  <!-- Repeat product-card pattern for each product -->
  <div class="product-card" data-reveal-item data-scope="product:{{handle1}}">...</div>
  <div class="product-card" data-reveal-item data-scope="product:{{handle2}}">...</div>
  <div class="product-card" data-reveal-item data-scope="product:{{handle3}}">...</div>
  <div class="product-card" data-reveal-item data-scope="product:{{handle4}}">...</div>
</div>
```

**CSS:**
```css
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 14rem), 1fr));
  gap: 1.5rem;
}
.product-grid [data-reveal-item] {
  opacity: 0; transform: translateY(1rem);
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.product-grid [data-reveal-item][data-visible="true"] {
  opacity: 1; transform: translateY(0);
}
```

---

## Product Carousel (horizontal scroll + cards)

```html
<div data-behavior="horizontal-scroll">
  <div class="carousel-header">
    <h2>You May Also Like</h2>
    <div class="carousel-nav">
      <button data-scroll-prev aria-label="Previous">←</button>
      <button data-scroll-next aria-label="Next">→</button>
    </div>
  </div>
  <div data-scroller class="carousel-track">
    <div class="carousel-card" data-scope="product:{{handle1}}">
      <div data-island="MediaCarousel" data-hydrate="visible" data-props='{...}'></div>
      <h3>{{title}}</h3>
      <p>{{price}}</p>
      <div data-island="QuickAdd" data-hydrate="interaction" data-props='{...}'></div>
    </div>
    <!-- more cards -->
  </div>
</div>
```

**CSS:**
```css
.carousel-track {
  display: flex; gap: 1rem;
  overflow-x: auto; scroll-snap-type: x mandatory;
  scrollbar-width: none;
}
.carousel-track::-webkit-scrollbar { display: none; }
.carousel-card {
  flex: 0 0 calc(33.333% - 0.667rem);
  scroll-snap-align: start;
  min-width: 0;
}
@media (max-width: 768px) { .carousel-card { flex: 0 0 75%; } }
```

---

## Accordion / FAQ (behavior, no React)

```html
<div data-behavior="accordion" data-config='{"mode":"single"}'>
  <div data-accordion-item>
    <button data-accordion-trigger aria-expanded="false">
      <span>What is your return policy?</span>
      <svg class="accordion-icon" width="16" height="16" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div data-accordion-content data-state="closed">
      <p>We offer 30-day returns on all products...</p>
    </div>
  </div>
  <div data-accordion-item>
    <button data-accordion-trigger aria-expanded="false">
      <span>How long does shipping take?</span>
      <svg class="accordion-icon" width="16" height="16" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div data-accordion-content data-state="closed">
      <p>Standard shipping takes 3-5 business days...</p>
    </div>
  </div>
</div>
```

**CSS:**
```css
[data-accordion-trigger] {
  width: 100%; display: flex; justify-content: space-between; align-items: center;
  padding: 1rem 0; border: none; background: none; cursor: pointer;
  font-size: 1rem; font-weight: 500; text-align: left;
  border-bottom: 1px solid var(--lx-border-color, #e5e7eb);
}
[data-accordion-trigger] .accordion-icon {
  transition: transform 0.2s;
}
[data-accordion-trigger][aria-expanded="true"] .accordion-icon {
  transform: rotate(180deg);
}
[data-accordion-content] {
  display: grid; grid-template-rows: 0fr;
  transition: grid-template-rows 0.3s ease;
}
[data-accordion-content][data-state="open"] {
  grid-template-rows: 1fr;
}
[data-accordion-content] > * {
  overflow: hidden;
}
```

---

## Scroll-Reveal Section

```html
<section data-behavior="scroll-reveal" data-config='{"animation":"fade-up","stagger":100}'>
  <div data-reveal-item class="feature-card">Feature 1</div>
  <div data-reveal-item class="feature-card">Feature 2</div>
  <div data-reveal-item class="feature-card">Feature 3</div>
</section>
```

**CSS:**
```css
[data-reveal-item] {
  opacity: 0; transform: translateY(1.5rem);
  transition: opacity 0.5s ease, transform 0.5s ease;
}
[data-reveal-item][data-visible="true"] {
  opacity: 1; transform: translateY(0);
}
```

---

## Variant Selector + QuickAdd Composition

For cards that need variant selection before add-to-cart:

```html
<div data-scope="product:{{handle}}">
  <div data-island="VariantSelector" data-props='{
    "product": {
      "variants": [...],
      "options": [{"name":"Size","values":["S","M","L"]}]
    },
    "render": "buttons"
  }'></div>
  <div data-island="QuickAdd" data-props='{
    "product": {"title":"...","variants":[...]},
    "render": "button"
  }'></div>
</div>
```

The `data-scope` ensures VariantSelector's `variant:changed` emission only reaches the QuickAdd within the same scope.

---

## Countdown (Headless Mode)

```html
<div class="sale-timer" data-island="CountdownTimer" data-props='{
  "endDate": "2026-12-31T23:59:59Z",
  "style": "headless",
  "expiredAction": "hide"
}'></div>
```

**CSS (you control all styling):**
```css
.sale-timer { display: flex; gap: 0.5rem; font-family: monospace; }
.sale-timer [data-part="days"],
.sale-timer [data-part="hours"],
.sale-timer [data-part="minutes"],
.sale-timer [data-part="seconds"] {
  background: #1a1a2e; color: #fff;
  padding: 0.5rem; border-radius: 0.25rem;
  font-size: 1.5rem; font-weight: 700;
  min-width: 2.5rem; text-align: center;
}
```

---

## Hero: Infinite Scrolling Background Images (CSS-only)

```html
<section class="hero-scroll">
  <div class="hero-scroll__media">
    <div class="hero-scroll__track">
      <!-- Duplicate all slides for seamless loop -->
      <div class="hero-scroll__slide"><img src="..." alt=""></div>
      <div class="hero-scroll__slide"><img src="..." alt=""></div>
      <!-- ...duplicated set... -->
      <div class="hero-scroll__slide"><img src="..." alt="" aria-hidden="true"></div>
      <div class="hero-scroll__slide"><img src="..." alt="" aria-hidden="true"></div>
    </div>
  </div>
  <div class="hero-scroll__content">
    <h1>Heading</h1>
    <p>Subtitle</p>
    <a href="#">CTA</a>
  </div>
</section>
```

**CSS:**
```css
.hero-scroll { position: relative; min-height: 100svh; overflow: hidden; }
.hero-scroll__media { position: absolute; inset: 0; display: flex; overflow: hidden; }
.hero-scroll__track { display: flex; height: 100%; flex-shrink: 0; animation: scrollTrack 50s infinite linear; }
.hero-scroll__slide { flex-shrink: 0; width: calc(100vw - 10rem); height: 100%; }
.hero-scroll__slide img { width: 100%; height: 100%; object-fit: cover; }
.hero-scroll__content { position: relative; z-index: 3; /* overlay text */ }
@keyframes scrollTrack { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
```

---

## Hero: SVG Curved Ribbon Text (CSS-only)

```html
<section class="hero-ribbon">
  <div class="hero-ribbon__content"><!-- heading + CTA --></div>
  <div class="hero-ribbon__ribbons">
    <svg viewBox="0 0 1048 594" fill="none">
      <path id="curve-left" d="M0.597656 50.92...1046.43 565.235" stroke="none" stroke-width="60"></path>
      <text x="-1048">
        <textPath href="#curve-left">Repeated text content...</textPath>
        <animate attributeName="x" from="-1048" to="0" dur="10s" repeatCount="indefinite" calcMode="linear"></animate>
      </text>
    </svg>
  </div>
</section>
```

Two SVGs in a 2-col grid create crossed ribbon effect. Text flows along Bezier curves with `<animate>`. Speed via `dur` attribute.

---

## Hero: Deck Card Slider (minimal JS)

```html
<section class="hero-deck">
  <div class="hero-deck__track">
    <div class="hero-deck__item" data-id="0">
      <div class="hero-deck__image"><img src="..."></div>
      <div class="hero-deck__content"><p class="hero-deck__title">Title</p></div>
    </div>
    <!-- more items... -->
  </div>
  <div class="hero-deck__buttons">
    <button class="hero-deck__prev">←</button>
    <button class="hero-deck__next">→</button>
  </div>
</section>
```

**CSS (nth-child positioning):**
```css
.hero-deck__item { position: absolute; width: 200px; height: 300px; top: 50%; transform: translateY(-50%); transition: all .5s; }
.hero-deck__item:nth-child(1), .hero-deck__item:nth-child(2) { top: 0; left: 0; width: 100%; height: 100%; }
.hero-deck__item:nth-child(2) .hero-deck__content { display: block; }
.hero-deck__item:nth-child(3) { left: 55%; }
.hero-deck__item:nth-child(4) { left: calc(55% + 220px); }
.hero-deck__item:nth-child(n+6) { opacity: 0; }
```

**JS (DOM rotation):**
```js
next.onclick = () => track.appendChild(track.firstElementChild);
prev.onclick = () => track.prepend(track.lastElementChild);
```

---

## Hero: Organic Blob Shape (SVG clip-path)

```html
<svg width="0" height="0" aria-hidden="true">
  <defs>
    <clipPath id="hero-blob" clipPathUnits="objectBoundingBox">
      <path d="M0.875,1 H0.124 C0.121,0.999..."></path>
    </clipPath>
  </defs>
</svg>
<div style="clip-path: url(#hero-blob); -webkit-clip-path: url(#hero-blob); min-height: 95vh;">
  <img src="..." style="width:100%;height:100%;object-fit:cover">
  <div class="content-overlay"><!-- heading + CTA --></div>
</div>
```

See `reference/blob-shapes.md` for 6 preset shapes categorized by mood.
