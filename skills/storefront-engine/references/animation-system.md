# Animation System — Vibe-Code Reference

CSS-only and vanilla JS animations for storefront pages. No framer-motion, no React — pure CSS keyframes + IntersectionObserver for scroll triggers.

---

## When to Animate vs Not

**Animate:**
- Hero headline on premium/editorial/bold brands
- Section entrances on scroll (fade-up, slide-in)
- Background gradients on dark/vibrant brands
- Stats/numbers counting up
- Floating decorative elements

**Don't animate:**
- Clinical/minimal brands (medical, simple skincare) → zero or subtle only
- Product images → never animate product shots
- More than 3 animated sections per page → overwhelming
- Text that needs to be read immediately (pricing, CTA copy)

---

## Section CSS: Keyframe Animations

Place in section `css` field. Scoped per section.

### Fade In Up (most common entrance)

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

### Stagger Children

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

Use section `js` field. IntersectionObserver fires animation on scroll.

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

### Gradient Text Shift

```css
@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.gradient-text {
  background: linear-gradient(90deg, var(--lx-accent-color), #8b5cf6, var(--lx-accent-color));
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradientShift 4s ease infinite;
}
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

## Background Animations

### Gradient Shift (hero/CTA backgrounds)

```css
@keyframes bgShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.animated-bg {
  background: linear-gradient(135deg, var(--lx-accent-color), var(--lx-bg-surface), var(--lx-accent-color));
  background-size: 400% 400%;
  animation: bgShift 8s ease infinite;
}
```

### Floating Elements (decorative)

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

### Parallax (scroll-based offset)

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

### Button Hover
```html
<button class="transition-all duration-200 hover:scale-[1.02] hover:shadow-lg active:scale-[0.98]" style="background:var(--lx-accent-color)">
  Shop Now
</button>
```

### Card Hover Lift
```html
<div class="transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">Card</div>
```

### Image Hover Zoom
```html
<div class="overflow-hidden rounded-xl">
  <img class="transition-transform duration-500 hover:scale-110" src="..." />
</div>
```

---

## Brand Tone → Animation Mapping

| Tone | Level | Recommended |
|---|---|---|
| Luxury/Premium | Subtle, slow | Fade-in-up (0.8s), text-reveal, gradient-text |
| Playful/Bold | Energetic | Stagger, scale-in, floating elements, gradient-shift |
| Clinical/Minimal | Near-zero | Simple fade (0.4s) only |
| Editorial | Refined | Word-by-word, slide-left/right, underline-draw |
| Earthy/Organic | Gentle | Slow fade (1s), parallax, float |
| Tech/DTC | Snappy | Fast stagger (0.08s delay), scale-in |

---

## Performance Rules

1. Only animate `transform` and `opacity` — never `width`, `height`, `margin`
2. Add `will-change: transform` to heavily animated elements
3. Max 10 keyframe animations per page
4. Accessibility — always include:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
5. Scroll observers: `{ passive: true }` and `threshold: 0.15`
