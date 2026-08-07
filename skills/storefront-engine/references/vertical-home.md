# Home & Lifestyle — Storefront Design Intelligence

> **When to load:** Furniture, home decor, candles, textiles, bedding, kitchenware, outdoor living, rugs, lighting, wall art, planters, storage, tableware.

## Philosophy

**Context is everything.** Home goods buyers need to see the product in a real space before they can imagine it in their own. A dining table photographed in isolation tells you nothing about scale, proportion, or how it anchors a room. The same table in a styled dining room, with chairs, a rug, lighting, and place settings, becomes tangible — the buyer can measure it against their own space and see the lifestyle it enables.

This vertical demands:
- **Visualization in space** — product shown in real rooms, not white void
- **Scale & proportion** — dimensional reference, human scale, room fit
- **Material quality trust** — close-ups of grain, weave, finish, hardware
- **Styling inspiration** — layered vignettes showing how to use/style the product
- **Lifestyle storytelling** — the feeling of living with the product

Treat the page like a walk through a styled showroom: curated, cohesive, aspirational but achievable.

---

## Section Sequences

### Furniture PDP (10-12 sections)
1. **Room Scene Hero** — product in fully styled room, focal point
2. **Quick Specs** — dimensions, materials, weight, assembly (above fold)
3. **Product Gallery** — room context + detail shots + scale reference
4. **Dimensions Deep Dive** — Tabs island (Dimensions | Materials | Care | Shipping)
5. **Material Story** — bento grid with material origin, craftsmanship, finish
6. **Room Inspiration Gallery** — asymmetric grid showing 4-6 different room settings
7. **Cross-Sell ("Complete the Room")** — ProductCarousel with related items
8. **Before/After Testimonials** — BeforeAfter island with room makeovers
9. **Photo Reviews** — ReviewCarousel with customer room photos
10. **FAQ** — assembly, shipping, returns (FAQ island)
11. **Design Philosophy** — brand story, values, sustainability
12. **Footer CTA** — EmailCapture for design tips

### Room/Style Guide (8-10 sections)
1. **Full-Bleed Room Hero** — aspirational lifestyle shot
2. **Intro Text** — design philosophy, collection story
3. **Shop the Look** — ProductCarousel with all items in the room
4. **Room Breakdown** — bento grid with annotated product callouts
5. **Styling Tips** — 2-column text + image pairs
6. **Material Palette** — visual grid of finishes, fabrics, metals
7. **Alternative Colorways** — Tabs island showing room in different finishes
8. **Customer Rooms** — ReviewCarousel with real customer interpretations
9. **FAQ** — design services, customization, lead times
10. **Footer CTA** — book consultation or save to Pinterest

### Collection Page (8-10 sections)
1. **Lifestyle Hero** — collection in a cohesive room setting
2. **Collection Intro** — philosophy, materials, range
3. **Product Grid** — filterable, sortable (use semantic HTML + CSS)
4. **Featured Product Deep Dive** — spotlight on hero piece
5. **Material Story** — shared materials/craftsmanship across collection
6. **Room Vignettes** — 3-4 styled settings mixing collection pieces
7. **Customer Favorites** — top-rated items from ReviewCarousel
8. **Cross-Collection Pairings** — ProductCarousel with complementary collections
9. **FAQ** — custom orders, trade program, lead times
10. **Footer CTA** — EmailCapture for new releases

### Small Goods (Candles, Textiles, Tableware) (8-10 sections)
1. **Lifestyle Hero** — product in styled vignette (not floating)
2. **Product Gallery** — detail shots, scale reference, in-use
3. **Quick Specs** — size, materials, care (compact)
4. **Material & Craft** — origin story, artisan process, sustainability
5. **Styling Vignettes** — 3-4 ways to use/display (bento grid)
6. **Scent/Texture/Color Deep Dive** — sensory storytelling (for candles/textiles)
7. **Gift Sets** — ProductCarousel with curated bundles
8. **Photo Reviews** — ReviewCarousel with customer styling
9. **FAQ** — care, shipping, gift wrap
10. **Footer CTA** — EmailCapture for seasonal collections

---

## Island Combinations

### Furniture PDP
```html
<!-- ProductGallery: room context + detail + scale -->
<div data-island="ProductGallery" data-props='{
  "images": [
    {"src": "room-wide.jpg", "alt": "Dining table in styled room", "type": "room"},
    {"src": "detail-leg.jpg", "alt": "Close-up of oak leg joinery", "type": "detail"},
    {"src": "scale-room.jpg", "alt": "Table with person seated", "type": "scale"},
    {"src": "room-angle2.jpg", "alt": "Dining room from kitchen view", "type": "room"}
  ],
  "thumbnailPosition": "left"
}'></div>

<!-- ImageZoom: material close-ups -->
<div data-island="ImageZoom" data-props='{
  "src": "oak-grain-macro.jpg",
  "alt": "White oak grain detail",
  "zoomLevel": 2.5
}'></div>

<!-- Tabs: specs, materials, care, shipping -->
<div data-island="Tabs" data-props='{
  "tabs": [
    {"id": "dimensions", "label": "Dimensions", "content": "<h3>Dimensions</h3><ul><li>H: 30\" × W: 72\" × D: 36\"</li><li>Weight: 145 lbs</li><li>Clearance: 24\" recommended</li><li>No assembly required</li></ul>"},
    {"id": "materials", "label": "Materials", "content": "<h3>Materials</h3><p>Solid white oak from sustainably managed forests in Vermont. Natural oil finish. Stainless steel leveling feet.</p>"},
    {"id": "care", "label": "Care", "content": "<h3>Care</h3><p>Wipe with damp cloth. Avoid harsh chemicals. Re-oil annually with included maintenance kit.</p>"},
    {"id": "shipping", "label": "Shipping", "content": "<h3>Shipping</h3><p>White-glove delivery in 4-6 weeks. We'll schedule delivery and bring the table to your room of choice.</p>"}
  ],
  "defaultTab": "dimensions"
}'></div>

<!-- ProductCarousel: complete the room -->
<div data-island="ProductCarousel" data-props='{
  "title": "Complete the Room",
  "products": [
    {"id": "bench-01", "name": "Matching Bench", "price": "$485", "image": "bench.jpg"},
    {"id": "chair-01", "name": "Oak Dining Chair", "price": "$295", "image": "chair.jpg"},
    {"id": "sideboard-01", "name": "Oak Sideboard", "price": "$1,850", "image": "sideboard.jpg"}
  ],
  "slidesToShow": 3
}'></div>

<!-- BeforeAfter: room makeover with product as anchor -->
<div data-island="BeforeAfter" data-props='{
  "beforeImage": "before-dining-room.jpg",
  "afterImage": "after-dining-room.jpg",
  "beforeLabel": "Before",
  "afterLabel": "After",
  "caption": "Sarah's dining room transformation with The Everyday Table"
}'></div>
```

### Room Inspiration Gallery
```html
<!-- ReviewCarousel: customer photos with room metadata -->
<div data-island="ReviewCarousel" data-props='{
  "reviews": [
    {
      "id": "r1",
      "author": "Jessica M.",
      "rating": 5,
      "text": "Perfect for our open-plan kitchen. The oak warms up the whole space.",
      "images": ["customer-room-1.jpg"],
      "metadata": {"room": "Kitchen/Dining", "style": "Modern Farmhouse"}
    },
    {
      "id": "r2",
      "author": "David L.",
      "rating": 5,
      "text": "Seats 8 comfortably. The finish is bulletproof with two kids.",
      "images": ["customer-room-2.jpg", "customer-room-2b.jpg"],
      "metadata": {"room": "Dining Room", "style": "Transitional"}
    }
  ],
  "showPhotosOnly": false
}'></div>
```

---

## Typography & Color

### Typography
- **Headings:** Warm serif (Fraunces, Quincy CF, Canela) or geometric sans (Avenir Next, Graphik, Suisse Intl) at 400-500 weight
- **Body:** 15-17px, 1.6-1.7 line-height, never below 14px
- **Eyebrow:** 11-12px uppercase, 0.12em letter-spacing, muted color
- **Hierarchy:** Large product name (3-4rem), subdued descriptors (0.875rem), generous whitespace

### Color
**Warm neutrals only.** Home buyers are hyper-sensitive to color — stark white (#FFF) reads as cold/clinical and undermines the "warm home" feeling.

```css
:root {
  --lx-bg-color: #FAFAF8;       /* Warm off-white, not stark */
  --lx-bg-surface: #F7F5F2;      /* Slightly warmer for cards */
  --lx-text-color: #2C2C2C;      /* Warm black, not pure black */
  --lx-text-muted: #6B6B6B;      /* Warm gray for secondary text */
  --lx-border-color: #E8E6E1;    /* Warm border, not cool gray */
  --lx-accent-color: #8B7355;    /* Derived from product material (walnut brown, ceramic sage, linen beige) */
  --lx-font-heading: 'Fraunces', Georgia, serif;
  --lx-font-body: 'Avenir Next', -apple-system, sans-serif;
}
```

**Accent from product:** If oak furniture → warm brown accent. If ceramic → soft sage or clay. If linen → warm beige. Never generic blue/red.

---

## Hero Patterns

### Room Scene Hero (Furniture)
```html
<section class="relative min-h-[85vh]" id="hero">
  <img 
    src="ASSET[dining-room-wide-hero.jpg]" 
    alt="The Everyday Table in a sunlit dining room with oak chairs and linen curtains" 
    class="absolute inset-0 w-full h-full object-cover"
    loading="eager"
  />
  <!-- Gradient overlay for text legibility -->
  <div class="absolute inset-0 bg-gradient-to-r from-white/80 via-white/40 to-transparent"></div>
  
  <div class="relative z-10 flex items-center min-h-[85vh] px-6 lg:px-16">
    <div class="max-w-lg space-y-5">
      <p class="text-xs uppercase tracking-[0.12em]" style="color:var(--lx-text-muted)">
        Solid White Oak
      </p>
      <h1 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:400;line-height:1.15;color:var(--lx-text-color)">
        The Everyday Table
      </h1>
      <p class="text-sm" style="color:var(--lx-text-muted)">
        72" × 36" × 30" • Seats 6-8 • No assembly required
      </p>
      <div class="flex gap-4 items-center">
        <span class="text-2xl font-medium" style="color:var(--lx-text-color)">$1,850</span>
        <a 
          href="#details" 
          class="inline-block text-sm font-medium border-b pb-1 transition-colors hover:opacity-70" 
          style="color:var(--lx-text-color);border-color:var(--lx-border-color)"
        >
          View Details →
        </a>
      </div>
    </div>
  </div>
</section>
```

### Lifestyle Hero (Small Goods — Candle)
```html
<section class="relative min-h-[75vh]" id="hero">
  <img 
    src="ASSET[candle-vignette-hero.jpg]" 
    alt="Cedarwood candle on styled shelf with books and ceramics" 
    class="absolute inset-0 w-full h-full object-cover"
  />
  <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-black/20 to-transparent"></div>
  
  <div class="relative z-10 flex items-end min-h-[75vh] px-6 lg:px-16 pb-12">
    <div class="max-w-md space-y-4">
      <p class="text-xs uppercase tracking-[0.12em] text-white/80">
        Hand-Poured Soy Wax
      </p>
      <h1 style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3.5vw,2.5rem);font-weight:400;line-height:1.2;color:white">
        Cedarwood & Amber
      </h1>
      <p class="text-sm text-white/80">
        8 oz • 50-hour burn • Smokeless cotton wick
      </p>
      <div class="flex gap-4 items-center">
        <span class="text-xl font-medium text-white">$38</span>
        <a 
          href="#details" 
          class="inline-block text-sm font-medium border-b border-white/50 pb-1 text-white hover:opacity-70 transition-opacity"
        >
          Shop Now →
        </a>
      </div>
    </div>
  </div>
</section>
```

---

## Dimensions Section (NON-NEGOTIABLE)

**For furniture, dimensions MUST be in the first 2-3 sections.** Use the Tabs island with Dimensions as the default open tab.

```html
<section class="py-16 px-6 lg:px-16" style="background:var(--lx-bg-surface)">
  <div class="max-w-4xl mx-auto">
    <div data-island="Tabs" data-props='{
      "tabs": [
        {
          "id": "dimensions",
          "label": "Dimensions",
          "content": "<div class=\"space-y-4\"><h3 class=\"text-lg font-medium mb-3\">Dimensions</h3><ul class=\"space-y-2 text-sm\" style=\"color:var(--lx-text-muted)\"><li><strong>Height:</strong> 30 inches</li><li><strong>Width:</strong> 72 inches</li><li><strong>Depth:</strong> 36 inches</li><li><strong>Weight:</strong> 145 lbs</li><li><strong>Clearance:</strong> 24\" recommended around table</li><li><strong>Assembly:</strong> None required — delivered fully assembled</li></ul><p class=\"text-xs mt-4\" style=\"color:var(--lx-text-muted)\">Custom sizes available. <a href=\"#contact\" class=\"underline\">Contact us</a> for quote.</p></div>"
        },
        {
          "id": "materials",
          "label": "Materials",
          "content": "<div class=\"space-y-4\"><h3 class=\"text-lg font-medium mb-3\">Materials</h3><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Solid white oak from sustainably managed forests in Vermont. Each plank is hand-selected for grain consistency. Natural oil finish (not polyurethane) for a matte, tactile surface. Stainless steel leveling feet with felt pads.</p></div>"
        },
        {
          "id": "care",
          "label": "Care",
          "content": "<div class=\"space-y-4\"><h3 class=\"text-lg font-medium mb-3\">Care Instructions</h3><ul class=\"space-y-2 text-sm\" style=\"color:var(--lx-text-muted)\"><li>Wipe spills immediately with a damp cloth</li><li>Avoid harsh chemicals and abrasive cleaners</li><li>Re-oil annually with the included maintenance kit (instructions provided)</li><li>Use placemats or trivets for hot items</li></ul></div>"
        },
        {
          "id": "shipping",
          "label": "Shipping",
          "content": "<div class=\"space-y-4\"><h3 class=\"text-lg font-medium mb-3\">Shipping & Delivery</h3><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">White-glove delivery in 4-6 weeks. We'll call to schedule a delivery window, bring the table to your room of choice, unpack, and remove all packaging. Free shipping within the continental US. Alaska/Hawaii: contact for quote.</p></div>"
        }
      ],
      "defaultTab": "dimensions"
    }'></div>
  </div>
</section>
```

---

## Material Story Section

**The "why it costs what it costs" section.** Bento-style grid with material origin, craftsmanship, finish, and durability. Pair with ImageZoom for tactile close-ups.

```html
<section class="py-20 px-6 lg:px-16" style="background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400;color:var(--lx-text-color)">
        Crafted to Last Generations
      </h2>
      <p class="mt-3 text-sm" style="color:var(--lx-text-muted)">
        Why we chose white oak, hand-joinery, and natural oil
      </p>
    </div>

    <!-- Bento Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
      <!-- Large image: oak forest -->
      <div class="lg:col-span-7 lg:row-span-2 relative overflow-hidden rounded-lg" style="background:var(--lx-bg-surface)">
        <img 
          src="ASSET[oak-forest-vermont.jpg]" 
          alt="White oak forest in Vermont" 
          class="w-full h-full object-cover min-h-[400px]"
        />
      </div>

      <!-- Text: origin -->
      <div class="lg:col-span-5 p-8 rounded-lg flex flex-col justify-center" style="background:var(--lx-bg-surface)">
        <h3 class="text-lg font-medium mb-3" style="color:var(--lx-text-color)">Sustainably Sourced</h3>
        <p class="text-sm leading-relaxed" style="color:var(--lx-text-muted)">
          Our white oak comes from family-owned forests in Vermont, certified by the Forest Stewardship Council. Each tree is tracked from forest to finish.
        </p>
      </div>

      <!-- Image: joinery close-up -->
      <div class="lg:col-span-5 relative overflow-hidden rounded-lg" style="background:var(--lx-bg-surface)">
        <div data-island="ImageZoom" data-props='{
          "src": "ASSET[mortise-tenon-joint.jpg]",
          "alt": "Mortise and tenon joinery detail",
          "zoomLevel": 2.5
        }'></div>
      </div>

      <!-- Text: craftsmanship -->
      <div class="lg:col-span-5 p-8 rounded-lg flex flex-col justify-center" style="background:var(--lx-bg-surface)">
        <h3 class="text-lg font-medium mb-3" style="color:var(--lx-text-color)">Hand-Joined</h3>
        <p class="text-sm leading-relaxed" style="color:var(--lx-text-muted)">
          Mortise-and-tenon joinery — the same technique used in 18th-century furniture. No screws, no glue failures. The table tightens over time.
        </p>
      </div>

      <!-- Text: finish -->
      <div class="lg:col-span-7 p-8 rounded-lg flex flex-col justify-center" style="background:var(--lx-bg-surface)">
        <h3 class="text-lg font-medium mb-3" style="color:var(--lx-text-color)">Natural Oil Finish</h3>
        <p class="text-sm leading-relaxed" style="color:var(--lx-text-muted)">
          We skip polyurethane in favor of Danish oil. The surface is matte, warm to the touch, and ages beautifully. Minor scratches can be buffed out with the included kit — no refinishing needed.
        </p>
      </div>

      <!-- Image: grain macro -->
      <div class="lg:col-span-5 relative overflow-hidden rounded-lg" style="background:var(--lx-bg-surface)">
        <div data-island="ImageZoom" data-props='{
          "src": "ASSET[oak-grain-macro.jpg]",
          "alt": "White oak grain close-up",
          "zoomLevel": 3
        }'></div>
      </div>
    </div>
  </div>
</section>
```

---

## Room Inspiration Gallery

**Asymmetric CSS Grid showing the product in 4-6 different room settings.** Critical for buyers who need to see versatility.

```html
<section class="py-20 px-6 lg:px-16" style="background:var(--lx-bg-color)">
  <div class="max-w-7xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400;color:var(--lx-text-color)">
        Styled Six Ways
      </h2>
      <p class="mt-3 text-sm" style="color:var(--lx-text-muted)">
        From modern farmhouse to mid-century minimal
      </p>
    </div>

    <!-- Asymmetric grid -->
    <div class="grid grid-cols-4 lg:grid-cols-8 gap-4">
      <!-- Large: modern farmhouse -->
      <div class="col-span-4 row-span-2 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-modern-farmhouse.jpg]" 
          alt="Table in modern farmhouse dining room" 
          class="w-full h-full object-cover min-h-[500px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-sm font-medium">Modern Farmhouse</p>
          <p class="text-white/80 text-xs mt-1">With linen chairs and pendant lighting</p>
        </div>
      </div>

      <!-- Small: mid-century -->
      <div class="col-span-2 lg:col-span-4 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-midcentury.jpg]" 
          alt="Table in mid-century modern dining room" 
          class="w-full h-full object-cover min-h-[240px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-xs font-medium">Mid-Century</p>
        </div>
      </div>

      <!-- Small: scandinavian -->
      <div class="col-span-2 lg:col-span-4 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-scandinavian.jpg]" 
          alt="Table in Scandinavian-style dining room" 
          class="w-full h-full object-cover min-h-[240px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-xs font-medium">Scandinavian</p>
        </div>
      </div>

      <!-- Medium: industrial -->
      <div class="col-span-2 lg:col-span-3 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-industrial.jpg]" 
          alt="Table in industrial loft dining room" 
          class="w-full h-full object-cover min-h-[300px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-xs font-medium">Industrial</p>
        </div>
      </div>

      <!-- Medium: coastal -->
      <div class="col-span-2 lg:col-span-3 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-coastal.jpg]" 
          alt="Table in coastal-style dining room" 
          class="w-full h-full object-cover min-h-[300px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-xs font-medium">Coastal</p>
        </div>
      </div>

      <!-- Small: transitional -->
      <div class="col-span-2 lg:col-span-2 relative overflow-hidden rounded-lg group">
        <img 
          src="ASSET[table-transitional.jpg]" 
          alt="Table in transitional dining room" 
          class="w-full h-full object-cover min-h-[240px] transition-transform duration-500 group-hover:scale-105"
        />
        <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/60 to-transparent">
          <p class="text-white text-xs font-medium">Transitional</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Social Proof

**Photo reviews showing the product in REAL customer homes** (not staged). This is the most trusted content in the home vertical — buyers want to see the product after delivery, in imperfect lighting, in real rooms.

```html
<section class="py-20 px-6 lg:px-16" style="background:var(--lx-bg-surface)">
  <div class="max-w-7xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400;color:var(--lx-text-color)">
        In Your Homes
      </h2>
      <p class="mt-3 text-sm" style="color:var(--lx-text-muted)">
        Real rooms, real reviews
      </p>
    </div>

    <div data-island="ReviewCarousel" data-props='{
      "reviews": [
        {
          "id": "r1",
          "author": "Jessica M.",
          "location": "Portland, OR",
          "rating": 5,
          "title": "Exactly what we needed",
          "text": "Perfect size for our open-plan kitchen. The oak warms up the whole space. We've had it for 6 months and it still looks brand new despite daily use with two kids.",
          "images": ["ASSET[customer-room-jessica.jpg]", "ASSET[customer-detail-jessica.jpg]"],
          "metadata": {"room": "Kitchen/Dining", "style": "Modern Farmhouse"},
          "verifiedPurchase": true,
          "date": "2026-05-12"
        },
        {
          "id": "r2",
          "author": "David L.",
          "location": "Austin, TX",
          "rating": 5,
          "title": "Worth every penny",
          "text": "We deliberated for weeks before buying. No regrets. The finish is bulletproof, seats 8 comfortably, and the craftsmanship is obvious. It's the anchor of our dining room.",
          "images": ["ASSET[customer-room-david.jpg]", "ASSET[customer-room-david-2.jpg]"],
          "metadata": {"room": "Dining Room", "style": "Transitional"},
          "verifiedPurchase": true,
          "date": "2026-04-28"
        },
        {
          "id": "r3",
          "author": "Priya S.",
          "location": "Seattle, WA",
          "rating": 5,
          "title": "Finally, a table that fits our space",
          "text": "We have a narrow dining room and most tables are either too wide or too small. This is the Goldilocks table — 72\" is perfect. The delivery team was incredibly careful and professional.",
          "images": ["ASSET[customer-room-priya.jpg]"],
          "metadata": {"room": "Dining Room", "style": "Mid-Century"},
          "verifiedPurchase": true,
          "date": "2026-03-15"
        }
      ],
      "showPhotosOnly": false,
      "slidesToShow": 1,
      "autoplay": false
    }'></div>
  </div>
</section>
```

---

## Photography

**Room context is non-negotiable.** Do not show furniture floating in a white void — it reads as cheap, despite the price point.

### Required shot types (in order of priority):
1. **Room-wide hero** — product as focal point in a fully styled room (rug, lighting, accessories, wall art)
2. **Scale reference** — product with a person seated/standing nearby (or known-size objects like books, plates)
3. **Detail shots** — joinery, grain, hardware, finish (macro lens, natural light)
4. **Alternate angles** — room from 2-3 different viewpoints
5. **In-use shots** — table set for a meal, candle lit, textiles draped/styled
6. **Material close-ups** — ImageZoom-ready macros of wood grain, fabric weave, ceramic glaze

### Asset keyword patterns:
- `room-wide-hero`, `room-angle-2`, `room-kitchen-view`
- `detail-leg-joinery`, `detail-oak-grain`, `detail-hardware`
- `scale-person-seated`, `scale-room-context`
- `styled-dining-table-set`, `styled-breakfast-nook`
- `customer-room-[name]`, `customer-detail-[name]`

### Anti-pattern:
Never use product photos with:
- Pure white backgrounds (reads as e-commerce commodity, not heirloom furniture)
- No scale reference (can't tell if it's 4 feet or 8 feet)
- Harsh studio lighting (looks artificial)
- Empty rooms (reads as "before" photo, not aspirational)

---

## Anti-Patterns

### 12 Home Page Killers

1. **No room context** — product floating in white void. NEVER.
2. **Missing dimensions above the fold** — buyers can't proceed without H×W×D.
3. **Tiny product images** — home buyers zoom obsessively. Use ImageZoom islands.
4. **Cold color palette** — stark white (#FFF), cool grays, blue accents. Reads as clinical/office, not home.
5. **Generic product photography** — no styling, no accessories, no life.
6. **Buried shipping/assembly info** — surprise fees or assembly requirements kill conversions.
7. **No material story** — "solid oak" means nothing without origin, finish, durability.
8. **No customer room photos** — staged rooms are aspirational, customer rooms build trust.
9. **Mobile-hostile specs** — dimensions in a dense paragraph instead of scannable list.
10. **No cross-sells** — buyers want to see the full room, not just one piece.
11. **Flat typography** — home is tactile. Use warm serifs, generous spacing, hierarchy.
12. **No scale reference** — table could be 4 feet or 12 feet. Show a person or known-size object.

### Warning Signs in Blueprint Prompts:
- "Minimalist design" → often means cold/sparse. Home needs warmth.
- "Lots of whitespace" → yes, but warm off-white (#FAFAF8), not stark.
- "Product gallery" → must specify room context shots, not just product-on-white.
- "Clean and modern" → risk of sterile. Clarify "warm modern" or "organic modern."

---

## Complete Blueprint Example

**Full VibePage JSON for Furniture PDP (Dining Table)**

```json
{
  "head": {
    "title": "The Everyday Table — Solid White Oak | [Brand Name]",
    "description": "Hand-crafted dining table in solid white oak. 72\" × 36\" × 30\". Seats 6-8. Mortise-and-tenon joinery. Natural oil finish. White-glove delivery in 4-6 weeks.",
    "og_image": "ASSET[og-everyday-table.jpg]"
  },
  "theme_css": ":root{--lx-bg-color:#FAFAF8;--lx-bg-surface:#F7F5F2;--lx-text-color:#2C2C2C;--lx-text-muted:#6B6B6B;--lx-border-color:#E8E6E1;--lx-accent-color:#8B7355;--lx-font-heading:'Fraunces',Georgia,serif;--lx-font-body:'Avenir Next',-apple-system,sans-serif}",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[85vh]\"><img src=\"ASSET[dining-room-wide-hero.jpg]\" alt=\"The Everyday Table in sunlit dining room\" class=\"absolute inset-0 w-full h-full object-cover\" loading=\"eager\"/><div class=\"absolute inset-0 bg-gradient-to-r from-white/80 via-white/40 to-transparent\"></div><div class=\"relative z-10 flex items-center min-h-[85vh] px-6 lg:px-16\"><div class=\"max-w-lg space-y-5\"><p class=\"text-xs uppercase tracking-[0.12em]\" style=\"color:var(--lx-text-muted)\">Solid White Oak</p><h1 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:400;line-height:1.15;color:var(--lx-text-color)\">The Everyday Table</h1><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">72\" × 36\" × 30\" • Seats 6-8 • No assembly required</p><div class=\"flex gap-4 items-center\"><span class=\"text-2xl font-medium\" style=\"color:var(--lx-text-color)\">$1,850</span><a href=\"#details\" class=\"inline-block text-sm font-medium border-b pb-1 transition-colors hover:opacity-70\" style=\"color:var(--lx-text-color);border-color:var(--lx-border-color)\">View Details →</a></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "quick-specs",
      "html": "<section class=\"py-12 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto grid grid-cols-2 lg:grid-cols-4 gap-6 text-center\"><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Dimensions</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">72\" × 36\" × 30\"</p></div><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Material</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">Solid White Oak</p></div><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Finish</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">Natural Oil</p></div><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Delivery</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">4-6 Weeks</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "product-gallery",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><div data-island=\"ProductGallery\" data-props='{\"images\":[{\"src\":\"ASSET[table-room-wide.jpg]\",\"alt\":\"Dining table in styled room\",\"type\":\"room\"},{\"src\":\"ASSET[table-detail-leg.jpg]\",\"alt\":\"Oak leg joinery close-up\",\"type\":\"detail\"},{\"src\":\"ASSET[table-scale-person.jpg]\",\"alt\":\"Table with person seated\",\"type\":\"scale\"},{\"src\":\"ASSET[table-room-angle2.jpg]\",\"alt\":\"Dining room from kitchen view\",\"type\":\"room\"},{\"src\":\"ASSET[table-detail-grain.jpg]\",\"alt\":\"Oak grain macro\",\"type\":\"detail\"}],\"thumbnailPosition\":\"left\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "dimensions-tabs",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto\"><div data-island=\"Tabs\" data-props='{\"tabs\":[{\"id\":\"dimensions\",\"label\":\"Dimensions\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Dimensions</h3><ul class=\\\"space-y-2 text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\"><li><strong>Height:</strong> 30 inches</li><li><strong>Width:</strong> 72 inches</li><li><strong>Depth:</strong> 36 inches</li><li><strong>Weight:</strong> 145 lbs</li><li><strong>Clearance:</strong> 24\\\" recommended</li><li><strong>Assembly:</strong> None — delivered fully assembled</li></ul></div>\"},{\"id\":\"materials\",\"label\":\"Materials\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Materials</h3><p class=\\\"text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\">Solid white oak from Vermont. Natural oil finish. Stainless steel leveling feet.</p></div>\"},{\"id\":\"care\",\"label\":\"Care\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Care</h3><p class=\\\"text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\">Wipe with damp cloth. Re-oil annually.</p></div>\"},{\"id\":\"shipping\",\"label\":\"Shipping\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Shipping</h3><p class=\\\"text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\">White-glove delivery in 4-6 weeks.</p></div>\"}],\"defaultTab\":\"dimensions\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "material-story",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400;color:var(--lx-text-color)\">Crafted to Last Generations</h2></div><div class=\"grid grid-cols-1 lg:grid-cols-12 gap-4\"><div class=\"lg:col-span-7 lg:row-span-2 relative overflow-hidden rounded-lg\"><img src=\"ASSET[oak-forest.jpg]\" alt=\"Vermont oak forest\" class=\"w-full h-full object-cover min-h-[400px]\"/></div><div class=\"lg:col-span-5 p-8 rounded-lg\" style=\"background:var(--lx-bg-surface)\"><h3 class=\"text-lg font-medium mb-3\">Sustainably Sourced</h3><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">FSC-certified Vermont oak.</p></div><div class=\"lg:col-span-5 relative overflow-hidden rounded-lg\"><div data-island=\"ImageZoom\" data-props='{\"src\":\"ASSET[mortise-tenon.jpg]\",\"alt\":\"Joinery detail\",\"zoomLevel\":2.5}'></div></div><div class=\"lg:col-span-7 p-8 rounded-lg\" style=\"background:var(--lx-bg-surface)\"><h3 class=\"text-lg font-medium mb-3\">Natural Oil Finish</h3><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Matte, warm, repairable.</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "room-gallery",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-7xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400\">Styled Six Ways</h2></div><div class=\"grid grid-cols-4 lg:grid-cols-8 gap-4\"><div class=\"col-span-4 row-span-2 relative overflow-hidden rounded-lg group\"><img src=\"ASSET[table-farmhouse.jpg]\" alt=\"Modern farmhouse\" class=\"w-full h-full object-cover min-h-[500px] transition-transform duration-500 group-hover:scale-105\"/><div class=\"absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/60 to-transparent\"><p class=\"text-white text-sm font-medium\">Modern Farmhouse</p></div></div><div class=\"col-span-2 lg:col-span-4 relative overflow-hidden rounded-lg group\"><img src=\"ASSET[table-midcentury.jpg]\" alt=\"Mid-century\" class=\"w-full h-full object-cover min-h-[240px] transition-transform duration-500 group-hover:scale-105\"/></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cross-sell",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-7xl mx-auto\"><div data-island=\"ProductCarousel\" data-props='{\"title\":\"Complete the Room\",\"products\":[{\"id\":\"bench-01\",\"name\":\"Matching Bench\",\"price\":\"$485\",\"image\":\"ASSET[bench.jpg]\"},{\"id\":\"chair-01\",\"name\":\"Oak Dining Chair\",\"price\":\"$295\",\"image\":\"ASSET[chair.jpg]\"}],\"slidesToShow\":3}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "before-after",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-5xl mx-auto\"><div class=\"text-center mb-8\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400\">Room Transformations</h2></div><div data-island=\"BeforeAfter\" data-props='{\"beforeImage\":\"ASSET[before-dining.jpg]\",\"afterImage\":\"ASSET[after-dining.jpg]\",\"caption\":\"Sarah's dining room with The Everyday Table\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-7xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400\">In Your Homes</h2></div><div data-island=\"ReviewCarousel\" data-props='{\"reviews\":[{\"id\":\"r1\",\"author\":\"Jessica M.\",\"rating\":5,\"text\":\"Perfect for our open-plan kitchen.\",\"images\":[\"ASSET[customer-1.jpg]\"],\"verifiedPurchase\":true}],\"slidesToShow\":1}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "faq",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-3xl mx-auto\"><h2 class=\"text-center mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,2.5vw,2rem);font-weight:400\">Frequently Asked Questions</h2><div data-island=\"FAQ\" data-props='{\"items\":[{\"question\":\"Is assembly required?\",\"answer\":\"No. The table is delivered fully assembled.\"},{\"question\":\"Can I customize the size?\",\"answer\":\"Yes. Contact us for a quote on custom dimensions.\"},{\"question\":\"What's your return policy?\",\"answer\":\"30-day returns. We'll arrange pickup and issue a full refund.\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta-footer",
      "html": "<section class=\"py-20 px-6 lg:px-16 text-center\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-xl mx-auto\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,2.5vw,2rem);font-weight:400;color:var(--lx-text-color)\">Get Design Tips in Your Inbox</h2><p class=\"mt-3 text-sm\" style=\"color:var(--lx-text-muted)\">Room styling ideas, new releases, and exclusive offers</p><div class=\"mt-6\"><div data-island=\"EmailCapture\" data-props='{\"placeholder\":\"Your email\",\"buttonText\":\"Subscribe\",\"successMessage\":\"Thanks! Check your inbox.\"}'></div></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

## Summary

Home & lifestyle pages succeed when they **transport the buyer into the space** — not just show them a product. Every section should answer: "What will this look like in my home? How will it feel? Will it fit? Is it worth the price?" Context, scale, material story, and real customer rooms are the four pillars. Skip any of them and conversions collapse.
