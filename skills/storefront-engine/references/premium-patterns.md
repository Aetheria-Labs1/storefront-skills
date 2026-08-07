# Premium Patterns — High-Converting Section Templates

Copy-and-adapt HTML+Tailwind patterns for common high-converting sections. Load when building hero, trust, CTA, or social proof sections.

---

## Hero Patterns

### Centered Hero (universal)

```html
<section class="relative min-h-[80vh] flex items-center justify-center text-center px-4 overflow-hidden" style="background:var(--lx-bg-color)">
  <div class="max-w-3xl mx-auto space-y-6">
    <p class="text-xs uppercase tracking-[0.2em] font-medium" style="color:var(--lx-accent-color)">Eyebrow Text</p>
    <h1 class="font-bold leading-[1.1] tracking-tight" style="font-family:var(--lx-font-heading);font-size:clamp(2.5rem,6vw,4.5rem)">
      Your Hero Headline Here
    </h1>
    <p class="text-lg lg:text-xl max-w-xl mx-auto" style="color:var(--lx-text-color);opacity:0.7">
      Supporting copy that reinforces the headline and builds desire.
    </p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center pt-4">
      <a href="#buy" class="px-8 py-4 rounded-lg font-semibold text-sm transition-all hover:scale-[1.02] hover:shadow-lg" style="background:var(--lx-accent-color);color:white">
        Primary CTA
      </a>
      <a href="#learn" class="px-8 py-4 rounded-lg font-semibold text-sm border-2 transition-all hover:scale-[1.02]" style="border-color:var(--lx-accent-color);color:var(--lx-accent-color)">
        Secondary CTA
      </a>
    </div>
  </div>
</section>
```

### Split Hero (image + text)

```html
<section class="grid grid-cols-1 lg:grid-cols-2 min-h-[80vh]">
  <div class="flex items-center px-6 lg:px-16 py-16 lg:py-0 order-2 lg:order-1">
    <div class="space-y-6 max-w-lg">
      <p class="text-xs uppercase tracking-[0.2em] font-medium" style="color:var(--lx-accent-color)">Category</p>
      <h1 class="font-bold leading-[1.1]" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3.5rem)">
        Headline
      </h1>
      <p class="text-base lg:text-lg leading-relaxed" style="color:var(--lx-text-color);opacity:0.7">
        Body copy here.
      </p>
      <button class="px-8 py-4 rounded-lg font-semibold transition-all hover:shadow-lg" style="background:var(--lx-accent-color);color:white">
        Shop Now
      </button>
    </div>
  </div>
  <div class="relative order-1 lg:order-2 min-h-[50vh] lg:min-h-full">
    <img src="IMAGE_URL" alt="Hero" class="absolute inset-0 w-full h-full object-cover" />
  </div>
</section>
```

### Full-Bleed Image Hero

```html
<section class="relative min-h-[90vh] flex items-center overflow-hidden">
  <img src="IMAGE_URL" alt="" class="absolute inset-0 w-full h-full object-cover" aria-hidden="true" />
  <div class="absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-transparent"></div>
  <div class="relative z-10 max-w-7xl mx-auto px-6 lg:px-16">
    <div class="max-w-xl space-y-6 text-white">
      <h1 class="font-bold leading-[1.05]" style="font-family:var(--lx-font-heading);font-size:clamp(2.5rem,5vw,4rem)">
        Bold Statement
      </h1>
      <p class="text-lg opacity-90">Supporting text on dark overlay.</p>
      <button class="px-8 py-4 rounded-lg font-semibold bg-white text-black transition-all hover:scale-[1.02]">
        Explore
      </button>
    </div>
  </div>
</section>
```

---

## Trust Bar Patterns

### Horizontal Icons + Text

```html
<section class="py-6 border-y" style="border-color:var(--lx-border-color);background:var(--lx-bg-surface)">
  <div class="max-w-5xl mx-auto px-4 flex flex-wrap justify-center gap-8 lg:gap-12">
    <div class="flex items-center gap-2">
      <svg class="w-5 h-5 flex-shrink-0" style="color:var(--lx-accent-color)" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 13l4 4L19 7"/></svg>
      <span class="text-sm font-medium" style="color:var(--lx-text-color)">Dermatologist Tested</span>
    </div>
    <div class="flex items-center gap-2">
      <svg class="w-5 h-5 flex-shrink-0" style="color:var(--lx-accent-color)" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
      <span class="text-sm font-medium" style="color:var(--lx-text-color)">Free Shipping Over ₹999</span>
    </div>
    <div class="flex items-center gap-2">
      <svg class="w-5 h-5 flex-shrink-0" style="color:var(--lx-accent-color)" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
      <span class="text-sm font-medium" style="color:var(--lx-text-color)">30-Day Easy Returns</span>
    </div>
    <div class="flex items-center gap-2">
      <svg class="w-5 h-5 flex-shrink-0" style="color:var(--lx-accent-color)" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
      <span class="text-sm font-medium" style="color:var(--lx-text-color)">100% Secure Payment</span>
    </div>
  </div>
</section>
```

---

## Social Proof Patterns

### Rating Summary Bar

```html
<div class="flex items-center gap-3 py-4">
  <div class="flex">
    <!-- 5 filled stars -->
    <svg class="w-5 h-5" style="color:var(--lx-accent-color)" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
    <!-- repeat 4 more times -->
  </div>
  <span class="text-sm font-semibold" style="color:var(--lx-text-color)">4.9</span>
  <span class="text-sm" style="color:var(--lx-text-color);opacity:0.6">Based on 2,847 reviews</span>
</div>
```

### Testimonial Card Grid

```html
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-center font-bold mb-12" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.5rem)">
      What Our Customers Say
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- Card -->
      <div class="bg-white rounded-xl p-6 shadow-sm">
        <div class="flex gap-1 mb-3">
          <!-- 5 stars SVG -->
        </div>
        <p class="text-sm leading-relaxed mb-4" style="color:var(--lx-text-color);opacity:0.8">
          "Review text here. Keep it authentic and specific."
        </p>
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-full bg-gray-200 flex items-center justify-center text-xs font-bold">PM</div>
          <div>
            <p class="text-sm font-medium">Priya M.</p>
            <p class="text-xs opacity-50">Verified Buyer</p>
          </div>
        </div>
      </div>
      <!-- Repeat cards -->
    </div>
  </div>
</section>
```

---

## CTA Patterns

### Sticky Bottom Bar (mobile)

```html
<section class="fixed bottom-0 left-0 right-0 z-50 lg:hidden p-4 border-t bg-white/95 backdrop-blur-sm" style="border-color:var(--lx-border-color)">
  <div class="flex items-center justify-between gap-3">
    <div>
      <p class="text-sm font-bold">₹1,299</p>
      <p class="text-xs opacity-50 line-through">₹1,799</p>
    </div>
    <button class="flex-1 py-3 rounded-lg font-semibold text-sm" style="background:var(--lx-accent-color);color:white">
      Add to Cart
    </button>
  </div>
</section>
```

### Urgency CTA Section

```html
<section class="py-12 px-4 text-center" style="background:var(--lx-accent-color)">
  <div class="max-w-2xl mx-auto space-y-4">
    <p class="text-white/80 text-sm font-medium uppercase tracking-wider">Limited Time Offer</p>
    <h2 class="text-white text-3xl lg:text-4xl font-bold" style="font-family:var(--lx-font-heading)">
      Get 20% Off Today Only
    </h2>
    <p class="text-white/70 text-lg">Use code WELCOME20 at checkout</p>
    <button class="mt-4 px-10 py-4 bg-white rounded-lg font-bold text-sm transition-all hover:scale-[1.02] hover:shadow-xl" style="color:var(--lx-accent-color)">
      Shop Now →
    </button>
  </div>
</section>
```

---

## Pricing Patterns

### Price with Discount

```html
<div class="flex items-baseline gap-3">
  <span class="text-3xl font-bold" style="color:var(--lx-text-color)">₹1,299</span>
  <span class="text-lg line-through opacity-40">₹1,799</span>
  <span class="text-xs font-semibold px-2 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">28% OFF</span>
</div>
```

### Bundle Pricing

```html
<div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
  <div class="border rounded-xl p-5 text-center" style="border-color:var(--lx-border-color)">
    <p class="text-sm font-medium mb-1">1 Bottle</p>
    <p class="text-2xl font-bold">₹1,299</p>
    <p class="text-xs opacity-50">₹1,299/unit</p>
  </div>
  <div class="border-2 rounded-xl p-5 text-center relative" style="border-color:var(--lx-accent-color)">
    <span class="absolute -top-3 left-1/2 -translate-x-1/2 text-[10px] font-bold px-3 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">MOST POPULAR</span>
    <p class="text-sm font-medium mb-1">2 Bottles</p>
    <p class="text-2xl font-bold">₹2,199</p>
    <p class="text-xs opacity-50">₹1,099/unit • Save 15%</p>
  </div>
  <div class="border rounded-xl p-5 text-center" style="border-color:var(--lx-border-color)">
    <p class="text-sm font-medium mb-1">3 Bottles</p>
    <p class="text-2xl font-bold">₹2,999</p>
    <p class="text-xs opacity-50">₹999/unit • Save 23%</p>
  </div>
</div>
```

---

## Features/Benefits Pattern

### Icon Grid

```html
<section class="py-16 lg:py-24 px-4">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-12">
      <p class="text-xs uppercase tracking-[0.2em] mb-3" style="color:var(--lx-accent-color)">Why Choose Us</p>
      <h2 class="font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.5rem)">Benefits That Matter</h2>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
      <div class="text-center space-y-3">
        <div class="w-12 h-12 mx-auto rounded-xl flex items-center justify-center" style="background:var(--lx-bg-surface)">
          <svg class="w-6 h-6" style="color:var(--lx-accent-color)" fill="none" stroke="currentColor" viewBox="0 0 24 24">...</svg>
        </div>
        <h3 class="font-semibold">Benefit Title</h3>
        <p class="text-sm leading-relaxed" style="opacity:0.7">Short description of this benefit.</p>
      </div>
      <!-- Repeat 5 more -->
    </div>
  </div>
</section>
```

---

## Navigation Pattern

### Transparent → Solid on Scroll

HTML:
```html
<nav class="fixed top-0 left-0 right-0 z-50 transition-all duration-300 nav-transparent" id="main-nav">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
    <a href="/" class="text-lg font-bold" style="font-family:var(--lx-font-heading)">Brand</a>
    <div class="hidden md:flex items-center gap-6">
      <a href="#" class="text-sm font-medium opacity-80 hover:opacity-100 transition-opacity">Shop</a>
      <a href="#" class="text-sm font-medium opacity-80 hover:opacity-100 transition-opacity">About</a>
      <a href="#" class="text-sm font-medium opacity-80 hover:opacity-100 transition-opacity">Reviews</a>
    </div>
    <button class="p-2">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
    </button>
  </div>
</nav>
```

CSS:
```css
.nav-transparent { background: transparent; }
.nav-solid { background: var(--lx-bg-color); box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
```

JS:
```javascript
(function() {
  var nav = document.getElementById('main-nav');
  if (!nav) return;
  window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
      nav.classList.remove('nav-transparent');
      nav.classList.add('nav-solid');
    } else {
      nav.classList.remove('nav-solid');
      nav.classList.add('nav-transparent');
    }
  }, { passive: true });
})();
```
