# GalleryLightbox — Island Directory

Event-driven fullscreen lightbox with scroll-snap viewer and thumbnail sidebar. One instance per page serves all galleries.

## Files

| File | Purpose |
|------|---------|
| `layouts/lookbook-grid.json` | 4-col tight grid triggering lightbox on click |
| `layouts/mosaic-strip.json` | 8-col dense mosaic with grayscale hover |
| `layouts/rounded-card.json` | 3-col grid inside pastel gradient card wrapper |

## Quick Reference

- **Variants**: none (single behavior, styled via CSS vars)
- **Required props**: none (event-driven)
- **Schema**: `vibe://schema/island/GalleryLightbox`
- **Layouts**: `vibe://islands/gallery-lightbox/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Event Bus Pattern

Unlike most islands that receive data via props, GalleryLightbox uses DOM events:

```js
// Open from any script or island
document.dispatchEvent(new CustomEvent('lx:lightbox:open', {
  detail: {
    images: [{src: '/img1-large.jpg', alt: 'Alt'}, ...],
    startIndex: 2
  }
}));

// Listen for close
document.addEventListener('lx:lightbox:close', () => { /* ... */ });
```

## Composition

- Mount once at page level (bottom of section HTML)
- Any gallery grid fires `lx:lightbox:open` via inline JS or from another island
- Pairs with: lookbook grids, UGC sections, product detail pages, blog image grids
- Never mount multiple instances — one handles all triggers
