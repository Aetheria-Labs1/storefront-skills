# Product Grid & Cards — Custom HTML Pattern

CSS grid of product cards. Replaces EditorialProductGrid and ProductCard islands.
No hydration needed for static display. For add-to-cart, place QuickAdd islands inside cards.

## Single Product Card

```html
<div style="display:flex; flex-direction:column; gap:0.75rem">
  <div style="aspect-ratio:3/4; overflow:hidden; border-radius:0.5rem; background:#f9fafb">
    <img src="https://cdn.shopify.com/..." alt="Product Name" style="width:100%; height:100%; object-fit:cover" />
  </div>
  <div>
    <h3 style="font-size:0.875rem; font-weight:500; margin:0">Product Name</h3>
    <p style="font-size:0.875rem; color:#6b7280; margin:0.25rem 0 0">$49.00</p>
  </div>
</div>
```

## Responsive Grid (2-col mobile, 4-col desktop)

```html
<div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(min(100%,12rem),1fr)); gap:1.5rem">
  <!-- product cards here -->
</div>
```

## With Multi-Image Hover (CSS-only)

For product cards with image swap on hover (shows second image):

```html
<div class="product-card" style="position:relative; aspect-ratio:3/4; overflow:hidden; border-radius:0.5rem">
  <img class="img-primary" src="https://cdn.shopify.com/.../front.jpg" alt="Product" style="width:100%; height:100%; object-fit:cover; transition:opacity 0.3s" />
  <img class="img-hover" src="https://cdn.shopify.com/.../back.jpg" alt="" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; transition:opacity 0.3s" />
</div>
```

CSS (in section css field):
```css
.product-card:hover .img-primary { opacity: 0; }
.product-card:hover .img-hover { opacity: 1; }
```

## With Multi-Image Carousel (section JS)

For a proper multi-image carousel within a card (auto-advance or swipe):

```html
<div class="card-carousel" data-images='["img1.jpg","img2.jpg","img3.jpg"]' style="position:relative; aspect-ratio:3/4; overflow:hidden; border-radius:0.5rem">
  <img class="carousel-img" src="img1.jpg" alt="Product" style="width:100%; height:100%; object-fit:cover; transition:opacity 0.4s" />
  <div class="carousel-dots" style="position:absolute; bottom:0.5rem; left:50%; transform:translateX(-50%); display:flex; gap:0.25rem">
    <span style="width:6px; height:6px; border-radius:50%; background:#fff; opacity:1"></span>
    <span style="width:6px; height:6px; border-radius:50%; background:#fff; opacity:0.5"></span>
    <span style="width:6px; height:6px; border-radius:50%; background:#fff; opacity:0.5"></span>
  </div>
</div>
```

JS (in section js field):
```js
section.querySelectorAll('.card-carousel').forEach(carousel => {
  const images = JSON.parse(carousel.dataset.images);
  const img = carousel.querySelector('.carousel-img');
  const dots = carousel.querySelectorAll('.carousel-dots span');
  let idx = 0;
  carousel.addEventListener('mouseenter', () => {
    const timer = setInterval(() => {
      idx = (idx + 1) % images.length;
      img.src = images[idx];
      dots.forEach((d, i) => d.style.opacity = i === idx ? '1' : '0.5');
    }, 1200);
    carousel._timer = timer;
  });
  carousel.addEventListener('mouseleave', () => {
    clearInterval(carousel._timer);
    idx = 0;
    img.src = images[0];
    dots.forEach((d, i) => d.style.opacity = i === 0 ? '1' : '0.5');
  });
});
```

## With QuickAdd (interactive add-to-cart)

Place a QuickAdd island inside the card. Use `render:"icon"` for a floating cart button, or `render:"button"` for full-width. Set `data-hydrate="interaction"` to defer hydration until user hovers.

```html
<div style="display:flex; flex-direction:column; gap:0.75rem; position:relative" data-scope="product:wireless-headphones">
  <div style="aspect-ratio:3/4; overflow:hidden; border-radius:0.5rem">
    <div data-island="MediaCarousel" data-hydrate="visible" data-props='{"media":[{"src":"https://cdn.shopify.com/product-front.jpg","alt":"Front"},{"src":"https://cdn.shopify.com/product-back.jpg","alt":"Back"}],"hoverAdvance":true,"showDots":true,"aspect":"3:4"}'></div>
  </div>
  <h3 style="font-size:0.875rem; font-weight:500; margin:0">Product Name</h3>
  <p style="font-size:0.875rem; color:#6b7280; margin:0">$49.00</p>
  <div style="position:absolute; bottom:5rem; right:0.75rem; z-index:5">
    <div data-island="QuickAdd" data-hydrate="interaction" data-props='{"product":{"title":"Product Name","variants":[{"id":"gid://shopify/ProductVariant/123","title":"Default","price":"$49.00","available":true}],"image":"https://cdn.shopify.com/product-front.jpg"},"render":"icon","iconSize":36}'></div>
  </div>
</div>
```

**Key points:**
- `data-scope="product:{{handle}}"` isolates variant events per card
- `MediaCarousel` with `data-hydrate="visible"` loads only when scrolled into view
- `QuickAdd` with `data-hydrate="interaction"` loads only on hover/click
- `render:"icon"` gives a small floating button instead of full-width

## "Buy Together" / Upsell Grid

```html
<div style="display:flex; gap:1rem; align-items:center; padding:1.5rem; border:1px solid #e5e7eb; border-radius:0.75rem">
  <!-- Main product -->
  <div style="flex:1; text-align:center">
    <img src="..." alt="Main" style="width:80px; height:80px; object-fit:cover; border-radius:0.5rem" />
    <div style="font-size:0.75rem; margin-top:0.5rem">Main Product</div>
  </div>
  <span style="font-size:1.5rem; color:#6b7280">+</span>
  <!-- Upsell -->
  <div style="flex:1; text-align:center">
    <img src="..." alt="Upsell" style="width:80px; height:80px; object-fit:cover; border-radius:0.5rem" />
    <div style="font-size:0.75rem; margin-top:0.5rem">Complement Product</div>
  </div>
  <span style="font-size:1.5rem; color:#6b7280">=</span>
  <!-- Bundle price -->
  <div style="flex:1; text-align:center">
    <div style="font-size:1.25rem; font-weight:700">$79</div>
    <div style="font-size:0.75rem; color:#10b981">Save $20</div>
    <div data-island="QuickAdd" data-props='{"variantId":"gid://shopify/ProductVariant/bundle123","label":"Add Both"}'></div>
  </div>
</div>
```
