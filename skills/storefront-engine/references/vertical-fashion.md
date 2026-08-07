# Fashion & Apparel — Storefront Blueprint Design Intelligence

> **When to load**: Product vertical is fashion, clothing, apparel, shoes, accessories, streetwear, athleisure, or basics. Auto-loads via `vibe://skills/vertical-fashion`.

## The Fashion Page Philosophy

Fashion pages sell **aspiration and identity**, not fabric specs. The page IS the lookbook. Every section should answer **"who will I become wearing this?"**

**Design must feel:**
- **Curated** — every element intentional, nothing generic
- **Editorial** — magazine spread quality, not catalog listing
- **Image-forward** — photography carries the narrative, design stays minimal to let imagery breathe

The photography does 80% of the work. Your job is to frame it perfectly and get out of the way.

---

## VibePage Architecture

Fashion pages are **raw HTML + Tailwind CSS + CSS custom properties + React islands**. NOT JSON schema.

**VibePage structure:**
```json
{
  "head": {
    "title": "...",
    "meta": [...]
  },
  "theme_css": ":root { --lx-accent-color: #000; ... }",
  "sections": [
    {
      "id": "hero",
      "html": "<section>...</section>",
      "css": "",
      "js": ""
    }
  ]
}
```

**CSS Variables:**
- `var(--lx-accent-color)` — Brand accent
- `var(--lx-text-color)` — Primary text
- `var(--lx-text-muted)` — Secondary text
- `var(--lx-bg-color)` — Page background
- `var(--lx-bg-surface)` — Card/surface background
- `var(--lx-border-color)` — Borders
- `var(--lx-font-heading)` — Heading font family
- `var(--lx-font-body)` — Body font family

**Available Islands:**
- `BuyBox` — Add to cart, variant selection
- `ProductGallery` — Multi-image viewer with zoom
- `VariantSwatches` — Color/size/style selector
- `SizeGuide` — Drawer with measurements
- `ReviewCarousel` — Customer reviews with photos
- `ProductCarousel` — Horizontal product scroller
- `VideoPlayer` — Video embed with controls
- `ImageZoom` — Detail inspection overlay
- `FAQ` — Collapsible Q&A
- `EmailCapture` — Newsletter signup
- `StickyBar` — Floating CTA bar
- `TrustBadgeBar` — Payment/shipping badges

**Tailwind Conventions:**
- All utility classes available
- Responsive: `sm:`, `md:`, `lg:`
- Container: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`

---

## Section Sequences (by page type)

### Single Product PDP (8-10 sections)

**Editorial approach**: Tell the product story through imagery first, utility second.

```
1. Editorial hero (full-bleed on-model shot)
   WHY: First impression = aspiration. Show product styled on body.

2. ProductGallery island (4-6 angles)
   WHY: Fashion buyers need fit, drape, texture visible. Build confidence.

3. BuyBox + VariantSwatches
   WHY: Conversion moment. Clean, uncluttered.

4. Product details (materials, care, sizing)
   WHY: Utility specs. Keep minimal.

5. Styling grid (outfit compositions)
   WHY: Show versatility. "3 ways to wear it." Drives AOV.

6. ProductCarousel ("Complete the Look")
   WHY: Cross-sell through styling, not generic "related."

7. SizeGuide island (drawer trigger)
   WHY: Reduce returns. Include model measurements.

8. ReviewCarousel (UGC-heavy, customer photos)
   WHY: Social proof. Real people wearing > star ratings.

9. Final CTA (minimal, single action)
   WHY: Final conversion nudge. Keep understated.

10. Newsletter (optional: "Get styling tips")
    WHY: Build community. Fashion wins on relationship.
```

**WHY this order**: Emotion first (hero, gallery, styling), then rational (details, reviews), then convert.

---

### Collection / Drop Page (10-12 sections)

**Lookbook-first storytelling**: This is a campaign, not a product list.

```
1. Campaign hero (full-bleed model shot + drop name)
2. Split editorial (campaign image + manifesto text)
3. Lookbook grid (8-12 tiles, mixed sizes)
4. Featured pieces (asymmetric bento layout)
5. Value props ("Sustainably Made" / "Limited Edition")
6. VideoPlayer (campaign film)
7. Stats (if relevant: "200 pieces only")
8. Social proof (UGC grid)
9. ProductCarousel ("Shop Collection")
10. Newsletter ("Be first for Drop 05")
```

---

### Lookbook / Editorial (6-8 sections)

**Image-heavy, minimal text**: Magazine pacing.

```
1. Full-bleed hero (1-2 word headline)
2. Lookbook grid (12-16 tiles, uniform aspect ratio)
3. Typographic break (pull quote)
4. Editorial split (model + detail)
5. Video (campaign film)
6. Social proof (press mentions)
7. Understated CTA ("View Collection")
```

---

### Sale / Seasonal Campaign (8-10 sections)

**Urgency + editorial quality.**

```
1. Sale hero ("End of Season / Up to 50% Off")
2. Countdown timer (if time-bound)
3. Sale grid (8-12 items, price badges)
4. Featured picks (hero items at deep discounts)
5. Value props ("Free Shipping" / "Easy Returns")
6. Stats ("1,200+ sold this weekend")
7. ProductCarousel ("Selling Fast")
8. Reviews (customer photos)
9. Bold CTA ("Shop Sale")
10. Newsletter ("Be first for next sale")
```

---

## Island HTML Patterns

### ProductGallery + VariantSwatches + SizeGuide Stack

**Full PDP product section:**

```html
<section class="py-16 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
      
      <!-- Left: Gallery -->
      <div>
        <div data-island="ProductGallery" data-props='{
          "images": [
            {"url": "/hero-editorial.jpg", "alt": "Model wearing product"},
            {"url": "/front-flat.jpg", "alt": "Front view"},
            {"url": "/back-flat.jpg", "alt": "Back view"},
            {"url": "/detail-texture.jpg", "alt": "Fabric detail"},
            {"url": "/styled-context.jpg", "alt": "Styled with accessories"}
          ],
          "layout": "editorial",
          "zoom": true,
          "aspectRatio": "3:4"
        }'></div>
      </div>

      <!-- Right: BuyBox -->
      <div class="flex flex-col gap-8">
        <div>
          <p class="text-xs uppercase tracking-widest text-gray-500 mb-3">Organic Cotton</p>
          <h1 class="text-4xl sm:text-5xl font-light mb-4" style="font-family: var(--lx-font-heading);">
            The Relaxed Tee
          </h1>
          <p class="text-base text-gray-600 mb-6">Soft, pre-washed, made to last.</p>
          <p class="text-2xl font-semibold mb-8">$48</p>
        </div>

        <!-- Color Swatches -->
        <div>
          <p class="text-sm font-medium mb-3">Color</p>
          <div data-island="VariantSwatches" data-props='{
            "type": "color",
            "display": "swatch",
            "size": "lg",
            "showLabel": true
          }'></div>
        </div>

        <!-- Size Selection -->
        <div>
          <div class="flex items-center justify-between mb-3">
            <p class="text-sm font-medium">Size</p>
            <button class="text-sm underline" onclick="openSizeGuide()">Size Guide</button>
          </div>
          <div data-island="VariantSwatches" data-props='{
            "type": "size",
            "display": "button",
            "size": "md"
          }'></div>
        </div>

        <!-- Add to Cart -->
        <div data-island="BuyBox" data-props='{
          "showPrice": false,
          "showQuantity": true,
          "ctaText": "Add to Bag"
        }'></div>

        <!-- Product Details -->
        <div class="border-t pt-6">
          <details class="group">
            <summary class="flex items-center justify-between cursor-pointer text-sm font-medium mb-2">
              Material
              <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </summary>
            <p class="text-sm text-gray-600 mt-2">100% organic cotton. GOTS certified.</p>
          </details>
        </div>

        <div class="border-t pt-6">
          <details class="group">
            <summary class="flex items-center justify-between cursor-pointer text-sm font-medium mb-2">
              Fit & Care
              <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </summary>
            <p class="text-sm text-gray-600 mt-2">Relaxed fit. True to size. Model is 5'10", wearing M.</p>
            <p class="text-sm text-gray-600 mt-2">Machine wash cold. Hang dry.</p>
          </details>
        </div>
      </div>

    </div>
  </div>

  <!-- Size Guide Drawer Island -->
  <div data-island="SizeGuide" data-props='{
    "measurements": [
      {"size": "XS", "chest": "32-34\"", "waist": "24-26\"", "hip": "34-36\""},
      {"size": "S", "chest": "34-36\"", "waist": "26-28\"", "hip": "36-38\""},
      {"size": "M", "chest": "38-40\"", "waist": "30-32\"", "hip": "40-42\""},
      {"size": "L", "chest": "42-44\"", "waist": "34-36\"", "hip": "44-46\""}
    ],
    "fitDescription": "Relaxed fit. Size down for fitted look.",
    "modelStats": "Model is 5'\''10\" (178cm), wearing size M."
  }'></div>
</section>
```

---

### ProductCarousel for Cross-Sell

**"Complete the Look" carousel:**

```html
<section class="py-16 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-light mb-8" style="font-family: var(--lx-font-heading);">
      Complete the Look
    </h2>
    
    <div data-island="ProductCarousel" data-props='{
      "products": [
        {"id": "prod_123", "title": "Wide Leg Cargo", "price": "$98", "image": "/cargo.jpg"},
        {"id": "prod_124", "title": "Canvas Sneaker", "price": "$68", "image": "/sneaker.jpg"},
        {"id": "prod_125", "title": "Canvas Tote", "price": "$38", "image": "/tote.jpg"}
      ],
      "layout": "scroll",
      "ctaStyle": "quickAdd",
      "showBadges": true
    }'></div>
  </div>
</section>
```

---

### VideoPlayer for Campaign Films

```html
<section class="py-24 bg-black">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-4xl font-light text-white mb-12 text-center">
      Drop 04 Campaign Film
    </h2>
    
    <div data-island="VideoPlayer" data-props='{
      "url": "/campaign-film-drop-04.mp4",
      "poster": "/campaign-hero.jpg",
      "autoplay": false,
      "muted": true,
      "controls": true,
      "aspectRatio": "16:9"
    }'></div>
  </div>
</section>
```

---

## Typography

**DRAMATIC size contrast = editorial feel.**

### Hero Headlines (Full-Bleed Sections)

```html
<section class="relative h-screen flex items-center justify-center">
  <img src="/hero-editorial.jpg" alt="New Season" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-black/20"></div>
  
  <div class="relative z-10 text-center text-white px-4">
    <p class="text-xs uppercase tracking-widest mb-4 opacity-80">Spring 2026</p>
    <h1 class="font-light leading-none" 
        style="font-size: clamp(3rem, 8vw, 7.5rem); 
               letter-spacing: -0.02em;
               max-width: 16ch;
               margin: 0 auto;">
      New Season
    </h1>
  </div>
</section>
```

**Key values:**
- Hero: `clamp(3rem, 8vw, 7.5rem)` = 48px–120px
- Font weight: `300` (ultra-light)
- Letter-spacing: `-0.02em` (tight)
- Line height: `1.0` (compact)
- Max-width: `16ch` (forces dramatic line breaks)

---

### Eyebrows (Collection Names, Seasons)

```html
<p class="text-xs uppercase font-medium tracking-widest text-gray-500 mb-3" 
   style="letter-spacing: 0.15em;">
  Spring 2026
</p>
```

**Examples:**
- "SPRING 2026"
- "COLLAB / ARTIST NAME"
- "LIMITED EDITION"

---

### Section Headings

```html
<h2 class="font-normal mb-8" 
    style="font-size: clamp(1.75rem, 4vw, 3rem); 
           letter-spacing: -0.01em;
           font-family: var(--lx-font-heading);">
  Complete the Look
</h2>
```

Keep 2-4 words max. Let products speak.

---

### Body Text (Rare Usage)

```html
<p class="text-base leading-relaxed text-gray-600" 
   style="max-width: 60ch;">
  100% organic cotton. Pre-washed. Made in Portugal.
</p>
```

**Use only for:**
- Materials
- Care instructions
- Fit descriptions

---

## Color & Backgrounds

**Monochrome is king. Black + white + ONE accent.**

### Streetwear (Dark Mode)

```html
<section class="py-24 bg-[#0a0a0a] text-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-5xl font-extrabold uppercase mb-8">Drop 04</h2>
    <p class="text-base text-white/70">Limited edition. 200 pieces only.</p>
  </div>
</section>
```

CSS vars:
```css
:root {
  --lx-bg-color: #0a0a0a;
  --lx-text-color: #ffffff;
  --lx-accent-color: #ff6b00;
}
```

---

### Premium Basics (Clean White)

```html
<section class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-4xl font-light text-black mb-8">Essential Tee</h2>
    <p class="text-base text-gray-600">Soft, timeless, made to last.</p>
  </div>
</section>
```

CSS vars:
```css
:root {
  --lx-bg-color: #ffffff;
  --lx-text-color: #0a0a0a;
  --lx-text-muted: rgba(0,0,0,0.6);
}
```

---

### Editorial (High Contrast B&W Photography)

```html
<section class="relative h-screen">
  <img src="/hero-bw.jpg" alt="Editorial" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-gradient-to-b from-black/30 to-black/60"></div>
  
  <div class="relative z-10 h-full flex items-center justify-center text-white">
    <h1 class="text-6xl sm:text-8xl font-light">New Season</h1>
  </div>
</section>
```

---

## Hero Patterns

### Full-Bleed Editorial Hero

```html
<section class="relative h-screen flex items-center">
  <img src="/hero-on-model.jpg" alt="Editorial hero" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-black/30"></div>
  
  <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
    <div class="max-w-2xl">
      <p class="text-xs uppercase tracking-widest text-white/80 mb-4">Organic Cotton</p>
      <h1 class="text-white font-light leading-none mb-6" 
          style="font-size: clamp(3rem, 8vw, 7rem);">
        The Relaxed Tee
      </h1>
      <p class="text-lg text-white/90 mb-8">Soft, pre-washed, made to last.</p>
      <button class="bg-white text-black px-8 py-4 text-sm font-medium uppercase tracking-wide hover:bg-gray-100 transition">
        Shop Now
      </button>
    </div>
  </div>
</section>
```

---

### Split Lookbook Hero

```html
<section class="min-h-screen bg-white">
  <div class="grid grid-cols-1 lg:grid-cols-2 min-h-screen">
    
    <!-- Left: Image -->
    <div class="relative h-[60vh] lg:h-screen">
      <img src="/lookbook-split.jpg" alt="Lookbook" class="absolute inset-0 w-full h-full object-cover" />
    </div>

    <!-- Right: Text -->
    <div class="flex items-center justify-center p-8 lg:p-16">
      <div class="max-w-md">
        <p class="text-xs uppercase tracking-widest text-gray-500 mb-4">Spring 2026</p>
        <h1 class="text-5xl sm:text-6xl font-light mb-6">Made for Movement</h1>
        <p class="text-base text-gray-600 mb-8 leading-relaxed">
          Relaxed silhouettes. Premium materials. Designed in Los Angeles for the way you live.
        </p>
        <a href="/collection" class="inline-block border-b-2 border-black text-sm uppercase tracking-wide pb-1 hover:opacity-70 transition">
          Explore Collection
        </a>
      </div>
    </div>

  </div>
</section>
```

---

## Lookbook Grid (Asymmetric)

**Editorial-style asymmetric grid with CSS Grid:**

```html
<section class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-4xl font-light mb-12">3 Ways to Wear It</h2>
    
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- Large hero tile (2x2) -->
      <div class="col-span-2 row-span-2 relative aspect-[3/4] overflow-hidden group">
        <img src="/styled-1.jpg" alt="Casual look" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
      </div>

      <!-- Medium tile (1x2) -->
      <div class="col-span-1 row-span-2 relative aspect-[3/4] overflow-hidden group">
        <img src="/styled-2.jpg" alt="Layered look" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      </div>

      <!-- Small tile (1x1) -->
      <div class="col-span-1 row-span-1 relative aspect-square overflow-hidden group">
        <img src="/styled-3.jpg" alt="Dressed up" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      </div>

      <!-- Small tile (1x1) -->
      <div class="col-span-1 row-span-1 relative aspect-square overflow-hidden group">
        <img src="/styled-4.jpg" alt="Detail shot" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      </div>
    </div>
  </div>
</section>
```

**Grid size mapping:**
- Large: `col-span-2 row-span-2` (2x2)
- Medium: `col-span-1 row-span-2` (1x2)
- Small: `col-span-1 row-span-1` (1x1)

**Hover effects** (via CSS):
- `group-hover:scale-105` — Zoom
- `group-hover:brightness-110` — Shimmer
- Ken Burns: `transition-transform duration-700`

---

## Social Proof / Reviews

**UGC-first, with customer measurements:**

```html
<section class="py-24 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-4xl font-light mb-4">What Customers Are Wearing</h2>
    <p class="text-base text-gray-600 mb-12">Real people, real fit feedback.</p>

    <div data-island="ReviewCarousel" data-props='{
      "displayMode": "ugc_gallery",
      "items": [
        {
          "customerName": "Alex M.",
          "customerStats": "5'\''8\", 145lbs, size M",
          "rating": 5,
          "reviewText": "Perfect fit. True to size. Fabric is so soft—ordering more colors.",
          "customerPhoto": "/ugc-customer-1.jpg",
          "verifiedPurchase": true,
          "sizeRating": "true_to_size",
          "styleTags": ["casual", "everyday"]
        },
        {
          "customerName": "Sarah J.",
          "customerStats": "5'\''6\", 130lbs, size S",
          "rating": 5,
          "reviewText": "Love the relaxed fit. Great for layering.",
          "customerPhoto": "/ugc-customer-2.jpg",
          "verifiedPurchase": true,
          "sizeRating": "true_to_size"
        }
      ],
      "filters": ["sizeRating", "styleTags"],
      "sortBy": "photosFirst"
    }'></div>

    <!-- Size Rating Summary -->
    <div class="mt-12 max-w-md mx-auto">
      <p class="text-sm font-medium mb-4">Fit Rating</p>
      <div class="space-y-2">
        <div class="flex items-center gap-3">
          <span class="text-xs text-gray-600 w-24">Runs Small</span>
          <div class="flex-1 bg-gray-200 h-2 rounded-full">
            <div class="bg-gray-800 h-2 rounded-full" style="width: 10%;"></div>
          </div>
          <span class="text-xs text-gray-600">10%</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-xs text-gray-600 w-24">True to Size</span>
          <div class="flex-1 bg-gray-200 h-2 rounded-full">
            <div class="bg-gray-800 h-2 rounded-full" style="width: 85%;"></div>
          </div>
          <span class="text-xs text-gray-600">85%</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-xs text-gray-600 w-24">Runs Large</span>
          <div class="flex-1 bg-gray-200 h-2 rounded-full">
            <div class="bg-gray-800 h-2 rounded-full" style="width: 5%;"></div>
          </div>
          <span class="text-xs text-gray-600">5%</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

**WHY**: Customer body stats + photos = trust. Aggregate fit data reduces returns.

---

## Anti-Patterns (Fashion Page Killers)

### 1. Product-on-white-only (No Lifestyle)
**Bad**: Only flat-lay white-background shots.  
**Fix**: Lead with on-model editorial. Flat-lays secondary.

### 2. Stock Photos
**Bad**: Generic stock models.  
**Fix**: Custom or AI-generated brand-consistent imagery.

### 3. Centered Symmetric Layouts
**Bad**: Every section centered, equal columns.  
**Fix**: Asymmetric grids, off-center text, varied sizes.

### 4. Too Much Text
**Bad**: Long paragraphs explaining product story.  
**Fix**: 1-3 word headlines. Let imagery carry narrative.

### 5. Corporate Typography
**Bad**: Arial, same size everywhere.  
**Fix**: Dramatic size contrast. Ultra-light heroes (300 weight).

### 6. Equal-Column Product Grids
**Bad**: 4-column grid, all same size.  
**Fix**: Asymmetric lookbook grids. Mixed sizes.

### 7. Generic "Shop Now" CTAs
**Bad**: Every CTA says "Shop Now."  
**Fix**: "Shop [Collection]", "Add to Bag", "View Lookbook."

### 8. Ignoring Mobile Aspect Ratios
**Bad**: 16:9 landscape heroes that crop poorly.  
**Fix**: Portrait aspect ratios (3:4, 4:5). Test mobile.

### 9. Size Chart as Afterthought
**Bad**: Size chart buried in footer.  
**Fix**: SizeGuide island link prominent near BuyBox.

### 10. No Model Measurements
**Bad**: Product photos with no fit context.  
**Fix**: Always include: "Model is 5'10", wearing M."

### 11. Overuse of Urgency (Non-Sale)
**Bad**: Countdown timers on regular PDPs.  
**Fix**: Use urgency only for real sales/drops.

### 12. No UGC / Customer Photos
**Bad**: Only professional brand photos in reviews.  
**Fix**: ReviewCarousel with UGC. Prioritize customer photos.

---

## Complete Fashion PDP Blueprint

**Full VibePage JSON for a premium fashion PDP:**

```json
{
  "head": {
    "title": "The Relaxed Tee — Organic Cotton",
    "meta": [
      {"name": "description", "content": "Soft, pre-washed, made to last."}
    ]
  },
  "theme_css": ":root { --lx-accent-color: #0a0a0a; --lx-text-color: #0a0a0a; --lx-text-muted: rgba(0,0,0,0.6); --lx-bg-color: #ffffff; --lx-font-heading: 'Inter', sans-serif; --lx-font-body: 'Inter', sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative h-screen flex items-center\"><img src=\"/hero-editorial.jpg\" alt=\"The Relaxed Tee\" class=\"absolute inset-0 w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-black/20\"></div><div class=\"relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full\"><div class=\"max-w-2xl\"><p class=\"text-xs uppercase tracking-widest text-white/80 mb-4\">Organic Cotton</p><h1 class=\"text-white font-light leading-none mb-6\" style=\"font-size: clamp(3rem, 8vw, 7rem);\">The Relaxed Tee</h1><p class=\"text-lg text-white/90 mb-8\">Soft, pre-washed, made to last.</p><a href=\"#product\" class=\"inline-block bg-white text-black px-8 py-4 text-sm font-medium uppercase tracking-wide hover:bg-gray-100 transition\">Shop Now</a></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "product",
      "html": "<section class=\"py-16 bg-white\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><div class=\"grid grid-cols-1 lg:grid-cols-2 gap-12\"><div><div data-island=\"ProductGallery\" data-props='{\"images\":[{\"url\":\"/hero-editorial.jpg\",\"alt\":\"Model wearing product\"},{\"url\":\"/front-flat.jpg\",\"alt\":\"Front view\"},{\"url\":\"/back-flat.jpg\",\"alt\":\"Back view\"},{\"url\":\"/detail-texture.jpg\",\"alt\":\"Fabric detail\"}],\"layout\":\"editorial\",\"zoom\":true,\"aspectRatio\":\"3:4\"}'></div></div><div class=\"flex flex-col gap-8\"><div><p class=\"text-xs uppercase tracking-widest text-gray-500 mb-3\">Organic Cotton</p><h2 class=\"text-4xl sm:text-5xl font-light mb-4\">The Relaxed Tee</h2><p class=\"text-base text-gray-600 mb-6\">Soft, pre-washed, made to last.</p><p class=\"text-2xl font-semibold mb-8\">$48</p></div><div><p class=\"text-sm font-medium mb-3\">Color</p><div data-island=\"VariantSwatches\" data-props='{\"type\":\"color\",\"display\":\"swatch\",\"size\":\"lg\",\"showLabel\":true}'></div></div><div><div class=\"flex items-center justify-between mb-3\"><p class=\"text-sm font-medium\">Size</p><button class=\"text-sm underline\">Size Guide</button></div><div data-island=\"VariantSwatches\" data-props='{\"type\":\"size\",\"display\":\"button\",\"size\":\"md\"}'></div></div><div data-island=\"BuyBox\" data-props='{\"showPrice\":false,\"showQuantity\":true,\"ctaText\":\"Add to Bag\"}'></div><div class=\"border-t pt-6\"><details class=\"group\"><summary class=\"flex items-center justify-between cursor-pointer text-sm font-medium mb-2\">Material<svg class=\"w-5 h-5 transition-transform group-open:rotate-180\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M19 9l-7 7-7-7\"/></svg></summary><p class=\"text-sm text-gray-600 mt-2\">100% organic cotton. GOTS certified.</p></details></div></div></div></div><div data-island=\"SizeGuide\" data-props='{\"measurements\":[{\"size\":\"XS\",\"chest\":\"32-34\\\"\",\"waist\":\"24-26\\\"\",\"hip\":\"34-36\\\"\"},{\"size\":\"S\",\"chest\":\"34-36\\\"\",\"waist\":\"26-28\\\"\",\"hip\":\"36-38\\\"\"}],\"fitDescription\":\"Relaxed fit. Size down for fitted.\",\"modelStats\":\"Model is 5'10\\\" (178cm), wearing M.\"}'></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "styling",
      "html": "<section class=\"py-24 bg-white\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><h2 class=\"text-4xl font-light mb-12\">3 Ways to Wear It</h2><div class=\"grid grid-cols-2 lg:grid-cols-4 gap-4\"><div class=\"col-span-2 row-span-2 relative aspect-[3/4] overflow-hidden group\"><img src=\"/styled-1.jpg\" alt=\"Casual\" class=\"w-full h-full object-cover transition-transform duration-700 group-hover:scale-105\" /></div><div class=\"col-span-1 row-span-2 relative aspect-[3/4] overflow-hidden group\"><img src=\"/styled-2.jpg\" alt=\"Layered\" class=\"w-full h-full object-cover transition-transform duration-700 group-hover:scale-105\" /></div><div class=\"col-span-1 row-span-1 relative aspect-square overflow-hidden group\"><img src=\"/styled-3.jpg\" alt=\"Dressed up\" class=\"w-full h-full object-cover transition-transform duration-700 group-hover:scale-105\" /></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cross-sell",
      "html": "<section class=\"py-16 bg-gray-50\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><h2 class=\"text-3xl font-light mb-8\">Complete the Look</h2><div data-island=\"ProductCarousel\" data-props='{\"products\":[{\"id\":\"prod_123\",\"title\":\"Wide Leg Cargo\",\"price\":\"$98\",\"image\":\"/cargo.jpg\"},{\"id\":\"prod_124\",\"title\":\"Canvas Sneaker\",\"price\":\"$68\",\"image\":\"/sneaker.jpg\"}],\"layout\":\"scroll\",\"ctaStyle\":\"quickAdd\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-24 bg-white\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><h2 class=\"text-4xl font-light mb-12\">What Customers Are Wearing</h2><div data-island=\"ReviewCarousel\" data-props='{\"displayMode\":\"ugc_gallery\",\"items\":[{\"customerName\":\"Alex M.\",\"customerStats\":\"5'8\\\", 145lbs, size M\",\"rating\":5,\"reviewText\":\"Perfect fit. True to size.\",\"customerPhoto\":\"/ugc-1.jpg\",\"sizeRating\":\"true_to_size\"}],\"sortBy\":\"photosFirst\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta",
      "html": "<section class=\"py-16 bg-gray-50\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center\"><a href=\"#product\" class=\"inline-block bg-black text-white px-12 py-5 text-sm font-medium uppercase tracking-wide hover:bg-gray-800 transition\">Add to Bag</a></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

## Summary

Fashion pages are **editorial, image-forward, minimal**. Photography does 80% of the work.

**Core principles:**
1. **Aspiration first** — hero imagery before specs
2. **Whitespace = luxury** — generous spacing (py-16, py-24)
3. **Dramatic typography** — huge heroes, tiny eyebrows
4. **Monochrome + one accent** — let product color pop
5. **Asymmetric layouts** — editorial ≠ symmetry
6. **Minimal copy** — 1-3 word headlines
7. **UGC > professional reviews** — real customers, real fit
8. **Size guide prominent** — reduce returns, model stats
9. **Lookbook grids** — asymmetric CSS Grid, mixed sizes
10. **Sub-vertical tailoring** — streetwear ≠ basics ≠ athleisure

Use HTML+Tailwind. Inject islands via `data-island`. Use CSS vars for theming. Test on mobile. Let imagery lead.
