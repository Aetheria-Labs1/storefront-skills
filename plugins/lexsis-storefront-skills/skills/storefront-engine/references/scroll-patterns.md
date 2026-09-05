# Scroll Patterns — Known Issues & Workarounds

## scroll-snap + Programmatic Scroll Conflict

`scrollBy()` and `scrollTo()` silently fail when `scroll-snap-type: x mandatory` is active.
This is browser spec behavior (Chrome 120+, Safari 17+). The browser refuses partial scrolls
that don't land exactly on a snap point.

### Symptoms
- `container.scrollBy({ left: 100 })` does nothing
- Smooth scroll animations freeze or jump
- Horizontal gallery scroll-jacking breaks

### Fix: Disable snap during programmatic scroll

```css
.gallery-container {
  scroll-snap-type: x mandatory; /* works for user scroll */
}
.gallery-container.scrolling {
  scroll-snap-type: none; /* disable during programmatic scroll */
}
```

```js
function scrollGallery(container, amount) {
  container.classList.add('scrolling');
  container.scrollBy({ left: amount, behavior: 'smooth' });
  setTimeout(() => container.classList.remove('scrolling'), 500);
}
```

### Alternative: Use `proximity` instead of `mandatory`

`scroll-snap-type: x proximity` allows partial scrolls. Snap points are "suggestions"
rather than hard stops. Often better UX for galleries.

## Horizontal Gallery Scroll-Jacking

For immersive galleries (Brunello Cucinelli-style horizontal scroll):

### Pattern

```html
<div class="gallery-wrapper" style="overflow:hidden; height:100vh; position:relative">
  <div class="gallery-track" style="display:flex; height:100%; transition:transform 0.5s ease">
    <!-- slides -->
  </div>
</div>
```

```js
let currentSlide = 0;
const track = section.querySelector('.gallery-track');
const slideCount = track.children.length;

section.querySelector('.gallery-wrapper').addEventListener('wheel', (e) => {
  e.preventDefault();
  if (e.deltaY > 30 && currentSlide < slideCount - 1) currentSlide++;
  if (e.deltaY < -30 && currentSlide > 0) currentSlide--;
  track.style.transform = `translateX(-${currentSlide * 100}%)`;
}, { passive: false });
```

### Rules
- MUST lock body overflow (`document.body.style.overflow = 'hidden'`) during gallery
- MUST provide exit: auto-release to vertical scroll at last slide
- MUST show progress indicator (dots, fraction, or progress bar)
- AVOID on mobile — conflicts with native swipe, pull-to-refresh
- AVOID without clear visual affordance that horizontal scroll exists

## Smooth Scroll + Snap Points Together

If you need both smooth programmatic scroll AND snap points:
1. Remove snap from the programmatic container
2. Use CSS `scroll-behavior: smooth` on a parent that has snap
3. Or use Web Animations API (`element.animate()`) instead of scrollBy — bypasses snap
