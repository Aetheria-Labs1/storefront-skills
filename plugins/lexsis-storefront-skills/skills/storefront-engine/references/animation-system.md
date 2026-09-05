# Animation System — Vibe-Code Reference

> House rules in `storefront-engine/references/design-rules.md` override every example below.
> Examples show structure and copy intent; their styling (gradients, hover transforms,
> uppercase labels, pills, emoji, section fills) is illustrative and must not be copied.
> Where an example conflicts with a house rule, the rule wins.

CSS-only and vanilla JS animations for storefront pages. No framer-motion, no React — pure CSS keyframes + IntersectionObserver for scroll triggers.

---

## When to Animate vs Not

**Animate nothing unless the plan names one moment.** Motion that answers a user action (hover colour, focus, open/close) is always fine. Everything below is reference for that single plan-named moment, never a default.

**Don't animate:**
- Section entrances by default → no fade-up on every section, no stagger on every grid
- Backgrounds → no colour shift, no floating decorative elements, no counters
- Clinical/minimal, luxury and earthy brands → zero, or one slow fade
- Product images → never animate product shots
- Text that needs to be read immediately (pricing, CTA copy)

---

## Section CSS: Keyframe Animations

Place in section `css` field. Scoped per section.

### Fade In Up (never by default; at most one orchestrated moment per page, named in the plan)

```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up {
  animation: fadeInUp 0.6s ease-out forwards;
  opacity: 0;
}
```

### Slide In Left/Right

```css
@keyframes slideInLeft {
  from { opacity: 0; transform: translateX(-40px); }
  to { opacity: 1; transform: translateX(0); }
}
@keyframes slideInRight {
  from { opacity: 0; transform: translateX(40px); }
  to { opacity: 1; transform: translateX(0); }
}
.slide-left { animation: slideInLeft 0.7s ease-out forwards; opacity: 0; }
.slide-right { animation: slideInRight 0.7s ease-out forwards; opacity: 0; }
```

### Scale In (cards, badges)

```css
@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
}
.scale-in { animation: scaleIn 0.5s ease-out forwards; opacity: 0; }
```

### Stagger Children (never by default; only inside the one plan-named moment)

```css
.stagger > * { opacity: 0; animation: fadeInUp 0.5s ease-out forwards; }
.stagger > *:nth-child(1) { animation-delay: 0s; }
.stagger > *:nth-child(2) { animation-delay: 0.1s; }
.stagger > *:nth-child(3) { animation-delay: 0.2s; }
.stagger > *:nth-child(4) { animation-delay: 0.3s; }
.stagger > *:nth-child(5) { animation-delay: 0.4s; }
.stagger > *:nth-child(6) { animation-delay: 0.5s; }
```

---

## Scroll-Triggered Reveal (Section JS)

Never by default; at most one orchestrated moment per page, named in the plan. Do not put `[data-reveal]` on every section. Use section `js` field. IntersectionObserver fires animation on scroll.

```javascript
(function() {
  var els = document.querySelectorAll('[data-section-id="SECTION_ID"] [data-reveal]');
  if (!els.length) return;
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  els.forEach(function(el) { observer.observe(el); });
})();
```

Pair with CSS:
```css
[data-reveal] { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }
[data-reveal].revealed { opacity: 1; transform: translateY(0); }
[data-reveal]:nth-child(2) { transition-delay: 0.1s; }
[data-reveal]:nth-child(3) { transition-delay: 0.2s; }
```

HTML: `<div data-reveal>Content appears on scroll</div>`

**Important:** Replace `SECTION_ID` with the actual section id in the JS.

---

## Headline Effects (CSS-only)

### Word-by-Word Fade

```css
@keyframes wordFade {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}
.headline-word { display: inline-block; opacity: 0; animation: wordFade 0.4s ease-out forwards; }
.headline-word:nth-child(1) { animation-delay: 0.0s; }
.headline-word:nth-child(2) { animation-delay: 0.12s; }
.headline-word:nth-child(3) { animation-delay: 0.24s; }
.headline-word:nth-child(4) { animation-delay: 0.36s; }
.headline-word:nth-child(5) { animation-delay: 0.48s; }
```

HTML: Wrap each word in `<span class="headline-word">Word</span>`

### Text Reveal (clip-path)

```css
@keyframes textReveal {
  from { clip-path: inset(0 100% 0 0); }
  to { clip-path: inset(0 0% 0 0); }
}
.text-reveal { animation: textReveal 0.8s ease-out forwards; }
```

### Underline Draw

```css
@keyframes drawUnderline {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
.highlight-word { position: relative; display: inline-block; }
.highlight-word::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 3px;
  background: var(--lx-accent-color);
  transform-origin: left;
  animation: drawUnderline 0.6s ease-out 0.3s forwards;
  transform: scaleX(0);
}
```

---

## Background & Decorative Motion (never by default)

### Floating Elements (decorative — never by default)

```css
@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  33% { transform: translateY(-15px) rotate(3deg); }
  66% { transform: translateY(-8px) rotate(-2deg); }
}
.float-1 { animation: float 6s ease-in-out infinite; }
.float-2 { animation: float 8s ease-in-out infinite; animation-delay: -2s; }
.float-3 { animation: float 7s ease-in-out infinite; animation-delay: -4s; }
```

### Parallax (only on a plan-named full-bleed image)

Section JS:
```javascript
(function() {
  var section = document.querySelector('[data-section-id="SECTION_ID"]');
  var bg = section && section.querySelector('.parallax-bg');
  if (!bg) return;
  function onScroll() {
    var rect = section.getBoundingClientRect();
    var speed = 0.3;
    bg.style.transform = 'translateY(' + (rect.top * speed) + 'px)';
  }
  window.addEventListener('scroll', onScroll, { passive: true });
})();
```

---

## Micro-Interactions (Tailwind transitions)

Hover states change colour, underline or border-colour only. No transforms (no scale, no translate, no lift, no glow).

### Button Hover
```html
<button class="transition-colors duration-200 hover:bg-[var(--lx-accent-color-hover)]" style="background:var(--lx-accent-color)">
  Shop now
</button>
```

### Card Hover
```html
<div class="border transition-colors duration-300 hover:border-[var(--lx-accent-color)]" style="border-color:var(--lx-border-color)">Card</div>
```

### Image Hover
```html
<div class="overflow-hidden rounded-xl">
  <img class="transition-opacity duration-300 hover:opacity-90" src="..." />
</div>
```

---

## Brand Tone → Animation Mapping

| Tone | Level | Recommended |
|---|---|---|
| Luxury/Premium | None or one slow fade | Fade-in (0.8s) on the one plan-named moment, or nothing |
| Playful/Bold | One moment | Stagger or scale-in on the one plan-named moment |
| Clinical/Minimal | Near-zero | Simple fade (0.4s) only, or nothing |
| Editorial | Refined | Word-by-word or underline-draw on the headline only |
| Earthy/Organic | None or one slow fade | Slow fade (1s) on the one plan-named moment, or nothing |
| Tech/DTC | One moment | Fast stagger (0.08s delay) on the one plan-named moment |

---

## Performance Rules

1. Only animate `transform` and `opacity` — never `width`, `height`, `margin`
2. Add `will-change: transform` to heavily animated elements
3. Max 10 keyframe animations per page
4. Accessibility — mandatory in `page-theme.css` whenever any animation exists:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
5. Scroll observers: `{ passive: true }` and `threshold: 0.15`
