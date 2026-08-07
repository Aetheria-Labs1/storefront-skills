# Food & Beverage DTC — Storefront Design Intelligence

> When to load: Product vertical is food, beverages, snacks, meal kits, coffee, tea, specialty food.

## Philosophy

Food pages sell with the SENSES. The visitor should almost taste/smell the product through the screen. Photography is 80% of the conversion. Every section should trigger appetite or curiosity.

Design must feel: **warm, inviting, appetizing, honest**. Like a farmer's market stall or a well-curated specialty store, not a supermarket shelf.

Key insight: food buyers are driven by:
1. **Appetite** (visual appeal, make them hungry)
2. **Values** (sourcing, ingredients, sustainability)
3. **Convenience** (subscription, bundles, easy reorder)
4. **Community** (reviews, recipes, shared experiences)

The golden rule: if the visitor can't imagine the taste/smell/texture from your hero section, you've lost them. Food is the most sensory-driven vertical in ecommerce.

Pages = **raw HTML + Tailwind CSS + CSS custom properties + React islands**.

## Architecture

**VibePage format:**
```json
{
  "head": {
    "title": "Rich, Bold, Unforgettable Coffee",
    "description": "...",
    "keywords": ["coffee", "single-origin", "organic"]
  },
  "theme_css": ":root { --lx-accent-color: #6F4E37; --lx-text-color: #2C1810; ... }",
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

**CSS custom properties:**
- `var(--lx-accent-color)` — primary brand color
- `var(--lx-text-color)` — body text
- `var(--lx-text-muted)` — secondary text
- `var(--lx-bg-color)` — page background
- `var(--lx-bg-surface)` — card/surface background
- `var(--lx-border-color)` — border color
- `var(--lx-font-heading)` — heading font family
- `var(--lx-font-body)` — body font family

**React islands:**
BuyBox, ProductGallery, BundleBuilder, SubscriptionToggle, ReviewCarousel, SocialProofPopup, TrustBadgeBar, FAQ, VideoPlayer, Tabs, ProductCarousel, CountdownTimer, EmailCapture, QuantityBreaks

Islands are hydrated via: `<div data-island="Name" data-props='{"key":"value"}'></div>`

**Tailwind CSS:** All utilities available. Responsive design via breakpoints (`sm:`, `md:`, `lg:`, `xl:`).

---

## Section Sequences

### Single Product (coffee, hot sauce, artisan snack)

**8-10 sections. Sensory-first flow:**

1. **Hero** — Appetizing full-width image (macro pour, steam, drizzle, bite). Headline describes TASTE or EXPERIENCE.
2. **Value Props** — 3 taste/quality pillars (icons + short text).
3. **Origin Story** — Large immersive section with farm/source imagery. Build trust through transparency.
4. **How to Use** — Recipe inspiration, preparation methods (3-4 tiles).
5. **Reviews** — Taste-focused reviews with photo uploads.
6. **Subscription** — BuyBox + SubscriptionToggle island, show savings.
7. **Nutrition Tabs** — Tabs island (Ingredients | Nutrition | Allergens | Sourcing).
8. **Trust Stats** — Social proof numbers.
9. **Final CTA** — Lifestyle shot with one-click add-to-cart.

**Islands:** BuyBox (with SubscriptionToggle), ReviewCarousel, Tabs, TrustBadgeBar

---

### Subscription Box (meal kit, snack box, coffee club)

**10-12 sections. Value-first, convenience-focused:**

1. **Hero** — Unboxing moment (flat-lay of box contents).
2. **How It Works** — 3-step explainer.
3. **What's Inside** — Product grid for this month's box.
4. **Customization** — Dietary filters, frequency selector.
5. **Pricing Plans** — QuantityBreaks island (1/3/6/12-month tiers).
6. **Sourcing Story** — Farm partners, quality curation.
7. **Reviews** — Subscription longevity reviews.
8. **Press Mentions** — Logo carousel.
9. **FAQ** — Skip/pause, cancellation, allergens.
10. **Final CTA** — "Start Your Subscription" with risk-free messaging.

**Islands:** BundleBuilder (if build-your-own-box), SubscriptionToggle, QuantityBreaks, ReviewCarousel, FAQ

---

### Variety Pack / Bundle

**8-10 sections. Discovery-first, flavor exploration:**

1. **Hero** — Spread/flat-lay of all flavors.
2. **Flavor Grid** — Each flavor gets a tile (photo + name + taste description).
3. **Build-Your-Own** — BundleBuilder island with visual selector.
4. **Savings Display** — QuantityBreaks island (3/6/12-pack tiers).
5. **Flavor-Specific Reviews** — Group by product.
6. **Pairing Suggestions** — Lifestyle photos, recipe ideas.
7. **FAQ** — Flavor recommendations, freshness.
8. **Cross-Sell** — ProductCarousel island.

**Islands:** BundleBuilder, QuantityBreaks, ReviewCarousel (flavor-segmented), ProductCarousel, Tabs

---

### Brand Story / Farm-to-Table

**6-8 sections. For sourcing stories, founder journey, sustainability:**

1. **Hero** — Founder or farm photo (warm, authentic).
2. **Origin Story** — Large immersive section with farm/source imagery.
3. **Commitments** — 4-tile sustainability/quality grid.
4. **Community Testimonials** — Values alignment focus.
5. **Certifications** — Logo carousel (USDA Organic, Fair Trade, etc.).
6. **Impact Stats** — Environmental/social impact numbers.
7. **Final CTA** — "Shop Our Story" with product link.

---

## Island Combinations

**The Food DTC Conversion Stack:**

### BundleBuilder
For variety packs, build-your-box subscriptions, flavor samplers. Visual selector with dynamic pricing.

```html
<div class="max-w-5xl mx-auto px-6 py-20">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Build Your Custom 6-Pack
    </h2>
    <p style="font-size:1.125rem;color:var(--lx-text-muted);margin-top:0.75rem">
      Choose your favorite flavors
    </p>
  </div>
  <div data-island="BundleBuilder" data-props='{"products":[{"id":"espresso","name":"Espresso Blend","image":"espresso.jpg","price":12},{"id":"light","name":"Light Roast","image":"light.jpg","price":12},{"id":"dark","name":"Dark Roast","image":"dark.jpg","price":12},{"id":"decaf","name":"Decaf","image":"decaf.jpg","price":12}],"minSelection":6,"maxSelection":6,"bundlePrice":66,"savings":6}'></div>
</div>
```

---

### SubscriptionToggle
For recurring delivery. Toggle between one-time and subscription with savings prominently displayed.

```html
<div class="max-w-2xl mx-auto px-6 py-20">
  <div class="bg-white rounded-2xl shadow-lg p-8">
    <div class="flex items-center justify-center gap-6 mb-6">
      <img src="PRODUCT_IMAGE" alt="Coffee bag" class="w-48 h-48 object-cover rounded-lg" />
      <div>
        <h3 style="font-family:var(--lx-font-heading);font-size:1.75rem;font-weight:600;color:var(--lx-text-color);margin-bottom:0.5rem">
          Ethiopian Yirgacheffe
        </h3>
        <p style="font-size:1rem;color:var(--lx-text-muted);margin-bottom:1.5rem">
          Single-origin, small-batch roasted
        </p>
        <div data-island="SubscriptionToggle" data-props='{"oneTimePrice":24,"subscriptionPrice":19.20,"savingsPercent":20,"frequencies":["Every 2 weeks","Every 1 month","Every 2 months"]}'></div>
      </div>
    </div>
  </div>
</div>
```

---

### QuantityBreaks
For bulk savings (3-pack, 6-pack, 12-pack). Tiered pricing cards with "Best Value" badge.

```html
<div class="max-w-5xl mx-auto px-6 py-20">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Stock Up & Save
    </h2>
  </div>
  <div data-island="QuantityBreaks" data-props='{"tiers":[{"quantity":3,"price":36,"perUnit":12,"savings":6},{"quantity":6,"price":66,"perUnit":11,"savings":12,"badge":"Best Value"},{"quantity":12,"price":120,"perUnit":10,"savings":24}]}'></div>
</div>
```

---

### ReviewCarousel
Taste and flavor-focused reviews. Filter by product/flavor. Highlight photo reviews.

```html
<div class="max-w-6xl mx-auto px-6 py-20" style="background:var(--lx-bg-surface)">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Loved by 12,847 Coffee Enthusiasts
    </h2>
  </div>
  <div data-island="ReviewCarousel" data-props='{"productId":"coffee-ethiopian","filterOptions":["5-star","Photo reviews","Verified purchase"],"highlightKeywords":["delicious","fresh","authentic","best"]}'></div>
</div>
```

---

### Tabs (Nutritional Transparency)
For ingredients, nutrition facts, allergens, sourcing story.

```html
<div class="max-w-4xl mx-auto px-6 py-20">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Transparency Matters
    </h2>
  </div>
  <div data-island="Tabs" data-props='{"tabs":[{"label":"Ingredients","content":"<div class=\"space-y-4\"><div class=\"flex items-center gap-2 text-sm\"><svg class=\"w-5 h-5 text-green-600\">...</svg>Certified Organic</div><div class=\"flex items-center gap-2 text-sm\"><svg class=\"w-5 h-5 text-green-600\">...</svg>Fair Trade</div><p class=\"mt-4\">100% Arabica Coffee Beans from Ethiopia</p></div>"},{"label":"Nutrition","content":"<table class=\"w-full text-sm\"><tr><td>Calories</td><td>5</td></tr><tr><td>Caffeine</td><td>95mg</td></tr></table>"},{"label":"Allergens","content":"<p>Contains: None</p><p class=\"text-xs text-gray-500 mt-2\">Processed in a facility that handles tree nuts</p>"},{"label":"Sourcing","content":"<p>Sourced from the Yirgacheffe region of Ethiopia, where our partner cooperative Abebech works with over 200 smallholder farmers. Harvested at 1,800-2,200 meters elevation.</p>"}]}'></div>
</div>
```

---

### ProductCarousel
For cross-sells and pantry completion.

```html
<div class="max-w-6xl mx-auto px-6 py-20">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Complete Your Pantry
    </h2>
  </div>
  <div data-island="ProductCarousel" data-props='{"products":[{"id":"grinder","name":"Coffee Grinder","image":"grinder.jpg","price":49},{"id":"mug","name":"Ceramic Mug","image":"mug.jpg","price":18},{"id":"pourover","name":"Pour Over Kit","image":"pourover.jpg","price":34},{"id":"beans","name":"Espresso Blend","image":"beans.jpg","price":24}]}'></div>
</div>
```

---

### TrustBadgeBar
Certifications and trust signals. Place near BuyBox or after hero.

```html
<div class="max-w-6xl mx-auto px-6 py-12 border-y" style="border-color:var(--lx-border-color)">
  <div data-island="TrustBadgeBar" data-props='{"badges":[{"icon":"organic","label":"USDA Organic"},{"icon":"fairtrade","label":"Fair Trade"},{"icon":"nongmo","label":"Non-GMO"},{"icon":"vegan","label":"Vegan"},{"icon":"glutenfree","label":"Gluten-Free"}]}'></div>
</div>
```

---

### FAQ
For objection handling. Cover shipping freshness, allergens, subscription management.

```html
<div class="max-w-3xl mx-auto px-6 py-20">
  <div class="text-center mb-12">
    <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
      Frequently Asked Questions
    </h2>
  </div>
  <div data-island="FAQ" data-props='{"questions":[{"q":"How should I store my coffee?","a":"Store in an airtight container in a cool, dry place. Avoid refrigeration."},{"q":"What is the caffeine content?","a":"Approximately 95mg per 8oz cup."},{"q":"Can I change my subscription frequency?","a":"Yes, you can skip, pause, or adjust frequency anytime in your account."},{"q":"What is your freshness guarantee?","a":"We roast to order and ship within 24 hours. All coffee is roasted within 7 days of delivery."}]}'></div>
</div>
```

---

## Typography & Color

### Typography

Warm and approachable. **Rounded sans-serif or friendly serif for headlines.**

**Weights:** 500-700 (medium to bold). Food isn't tech — avoid thin weights (300) and ultra-bold (800+).

**Sizes:**
- **Hero headline:** `clamp(2.25rem, 5vw, 4rem)` (36px → 64px)
- **Section headlines:** `clamp(1.75rem, 3.5vw, 3rem)` (28px → 48px)
- **Subline:** `clamp(1rem, 2vw, 1.25rem)` (16px → 20px), line-height: 1.6-1.7
- **Eyebrow:** `clamp(0.875rem, 1.5vw, 1rem)` (14px → 16px), letter-spacing: `0.05em`

**Font pairing suggestions:**
- **Warm modern:** Inter (body) + Fraunces (headlines, friendly serif)
- **Artisan/craft:** Source Sans 3 (body) + Playfair Display (headlines, editorial serif)
- **Fun/snack brand:** DM Sans (body) + Quicksand (headlines, rounded sans)
- **Premium/luxury:** Crimson Text (body + headlines, elegant serif) or Cormorant (headlines) + Lato (body)

---

### Color & Backgrounds

Warm palette ALWAYS. Derive from food/ingredient colors:

- **Coffee/chocolate:** rich browns (#4A2C2A, #6F4E37), cream (#F5EDE4), burnt orange (#D2691E)
- **Tomato/sauce:** deep red (#C1440E), terracotta (#E07A5F), warm white (#FFFDF7)
- **Avocado/health:** sage green (#88A096), olive (#6B8E23), off-white (#FAFAF5)
- **Honey/bakery:** golden yellow (#F4A460), amber (#FFBF00), warm beige (#F5E6D3)
- **Berry/fruit:** deep purple (#6A0572), raspberry (#E30B5C), blush pink (#FFB6C1)
- **Organic/earth:** khaki (#C3B091), clay (#B87333), natural linen (#FAF0E6)

**NEVER:**
- Clinical white (#FFFFFF) — too sterile
- Tech blue (#0066FF) or neon (#00FFFF)
- Pure black (#000000) — use warm dark brown (#2C1810)

**Example theme_css:**

```css
:root {
  --lx-accent-color: #6F4E37;
  --lx-text-color: #2C1810;
  --lx-text-muted: #5C4A42;
  --lx-bg-color: #FFFDF7;
  --lx-bg-surface: #F5EDE4;
  --lx-border-color: #E5D7CB;
  --lx-font-heading: 'Fraunces', serif;
  --lx-font-body: 'Inter', sans-serif;
}
```

---

## Hero Patterns

### Food Photography Hero

```html
<section class="relative min-h-[80vh] flex items-end" style="background:var(--lx-bg-color)">
  <img src="IMAGE_URL" alt="Coffee pour" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
  <div class="relative z-10 max-w-3xl mx-auto text-center pb-16 px-6 text-white space-y-4">
    <p class="text-xs uppercase tracking-[0.15em] opacity-80">Single Origin • Small Batch</p>
    <h1 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem);font-weight:600">
      Your Morning Ritual, Perfected
    </h1>
    <p style="font-size:clamp(1rem,2vw,1.25rem);line-height:1.6;opacity:90">
      Rich, bold Ethiopian Yirgacheffe with notes of blueberry and dark chocolate
    </p>
    <button class="px-8 py-4 rounded-lg font-semibold bg-white text-black text-sm hover:bg-gray-100 transition">
      Shop Coffee →
    </button>
  </div>
</section>
```

---

### Flat-lay Grid Hero

```html
<section class="relative min-h-[90vh] flex items-center justify-center" style="background:var(--lx-bg-color)">
  <img src="FLATLAY_IMAGE" alt="All five flavors spread" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-black/30"></div>
  <div class="relative z-10 max-w-4xl mx-auto text-center px-6 text-white space-y-6">
    <p class="text-sm uppercase tracking-[0.15em] opacity-90">Variety Pack</p>
    <h1 style="font-family:var(--lx-font-heading);font-size:clamp(2.5rem,6vw,4.5rem);font-weight:700">
      Discover Your New Favorite
    </h1>
    <p style="font-size:clamp(1.125rem,2.5vw,1.5rem);line-height:1.5;max-width:40rem;margin:0 auto">
      Five bold flavors in one sampler pack. Crunchy, satisfying, and made with real ingredients.
    </p>
    <button class="px-10 py-5 rounded-lg font-semibold text-base" style="background:var(--lx-accent-color);color:white">
      Shop the Sampler
    </button>
  </div>
</section>
```

---

## Subscription Section

```html
<section class="py-24 px-6" style="background:var(--lx-bg-surface)">
  <div class="max-w-5xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
        Never Run Out
      </h2>
      <p style="font-size:1.125rem;color:var(--lx-text-muted);margin-top:0.75rem">
        Subscribe and save 20% on every delivery
      </p>
    </div>
    
    <div class="bg-white rounded-2xl shadow-xl p-10 max-w-2xl mx-auto">
      <div class="flex flex-col md:flex-row items-center gap-8">
        <img src="PRODUCT_IMAGE" alt="Coffee bag" class="w-64 h-64 object-cover rounded-xl" />
        <div class="flex-1">
          <h3 style="font-family:var(--lx-font-heading);font-size:1.5rem;font-weight:600;color:var(--lx-text-color);margin-bottom:1rem">
            Ethiopian Yirgacheffe
          </h3>
          <div data-island="SubscriptionToggle" data-props='{"oneTimePrice":24,"subscriptionPrice":19.20,"savingsPercent":20,"frequencies":["Every 2 weeks","Every 1 month","Every 2 months"],"defaultFrequency":"Every 1 month"}'></div>
          <p class="text-xs text-gray-500 mt-4">Skip or cancel anytime. No commitment.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Bundle Builder

```html
<section class="py-24 px-6" style="background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
        Build Your Perfect Pack
      </h2>
      <p style="font-size:1.125rem;color:var(--lx-text-muted);margin-top:0.75rem">
        Choose 6 bags and save $12
      </p>
    </div>
    
    <div data-island="BundleBuilder" data-props='{
      "products": [
        {"id":"espresso","name":"Espresso Blend","description":"Bold & Intense","image":"espresso.jpg","price":12},
        {"id":"light","name":"Light Roast","description":"Bright & Fruity","image":"light.jpg","price":12},
        {"id":"dark","name":"Dark Roast","description":"Smoky & Rich","image":"dark.jpg","price":12},
        {"id":"decaf","name":"Decaf","description":"Smooth & Mellow","image":"decaf.jpg","price":12},
        {"id":"cold-brew","name":"Cold Brew Blend","description":"Sweet & Refreshing","image":"cold-brew.jpg","price":12},
        {"id":"french-roast","name":"French Roast","description":"Deep & Robust","image":"french.jpg","price":12}
      ],
      "minSelection": 6,
      "maxSelection": 6,
      "bundlePrice": 66,
      "savings": 6
    }'></div>
  </div>
</section>
```

---

## Nutritional Transparency

```html
<section class="py-24 px-6" style="background:var(--lx-bg-surface)">
  <div class="max-w-4xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
        What's Inside
      </h2>
      <p style="font-size:1.125rem;color:var(--lx-text-muted);margin-top:0.75rem">
        Transparency matters
      </p>
    </div>
    
    <div data-island="Tabs" data-props='{
      "tabs": [
        {
          "label": "Ingredients",
          "content": "<div class=\"space-y-4\"><div class=\"flex flex-wrap gap-3 mb-6\"><span class=\"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\"><svg class=\"w-4 h-4\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"></path></svg>Certified Organic</span><span class=\"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\"><svg class=\"w-4 h-4\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"></path></svg>Fair Trade</span><span class=\"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\"><svg class=\"w-4 h-4\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"></path></svg>Single Origin</span></div><p class=\"text-base\" style=\"color:var(--lx-text-color)\">100% Arabica Coffee Beans from Ethiopia</p><p class=\"text-sm mt-3\" style=\"color:var(--lx-text-muted)\">Roasted in small batches in Portland, Oregon</p></div>"
        },
        {
          "label": "Nutrition",
          "content": "<table class=\"w-full text-sm\"><tbody><tr class=\"border-b\" style=\"border-color:var(--lx-border-color)\"><td class=\"py-3\" style=\"color:var(--lx-text-color)\">Serving Size</td><td class=\"py-3 text-right font-medium\" style=\"color:var(--lx-text-color)\">8 fl oz (237mL)</td></tr><tr class=\"border-b\" style=\"border-color:var(--lx-border-color)\"><td class=\"py-3\" style=\"color:var(--lx-text-color)\">Calories</td><td class=\"py-3 text-right font-medium\" style=\"color:var(--lx-text-color)\">5</td></tr><tr class=\"border-b\" style=\"border-color:var(--lx-border-color)\"><td class=\"py-3\" style=\"color:var(--lx-text-color)\">Caffeine</td><td class=\"py-3 text-right font-medium\" style=\"color:var(--lx-text-color)\">95mg</td></tr><tr><td class=\"py-3\" style=\"color:var(--lx-text-color)\">Fat</td><td class=\"py-3 text-right font-medium\" style=\"color:var(--lx-text-color)\">0g</td></tr></tbody></table>"
        },
        {
          "label": "Allergens",
          "content": "<div class=\"space-y-4\"><p class=\"text-base font-medium\" style=\"color:var(--lx-text-color)\">Contains: None</p><p class=\"text-sm mt-4\" style=\"color:var(--lx-text-muted)\">Processed in a facility that also handles tree nuts</p><div class=\"flex flex-wrap gap-2 mt-6\"><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-gray-100\" style=\"color:var(--lx-text-color)\">Gluten-Free</span><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-gray-100\" style=\"color:var(--lx-text-color)\">Dairy-Free</span><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-gray-100\" style=\"color:var(--lx-text-color)\">Vegan</span></div></div>"
        },
        {
          "label": "Sourcing",
          "content": "<div class=\"space-y-4\"><p class=\"text-base\" style=\"color:var(--lx-text-color)\">Sourced from the Yirgacheffe region of Ethiopia, where our partner cooperative Abebech works with over 200 smallholder farmers.</p><p class=\"text-base mt-4\" style=\"color:var(--lx-text-color)\">Harvested at 1,800-2,200 meters elevation, processed naturally, and shipped directly to our roastery in Portland.</p><div class=\"mt-6 p-4 rounded-lg\" style=\"background:var(--lx-bg-surface)\"><p class=\"text-xs uppercase tracking-wider font-semibold mb-2\" style=\"color:var(--lx-text-muted)\">Certifications</p><div class=\"flex flex-wrap gap-2\"><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\">USDA Organic</span><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800\">Fair Trade</span><span class=\"px-3 py-1 rounded-full text-xs font-medium bg-amber-100 text-amber-800\">Rainforest Alliance</span></div></div></div>"
        }
      ]
    }'></div>
  </div>
</section>
```

---

## Social Proof for Food

```html
<section class="py-24 px-6" style="background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-12">
      <p class="text-sm uppercase tracking-wider font-semibold mb-2" style="color:var(--lx-accent-color)">Loved by Thousands</p>
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)">
        Join 12,847 Happy Customers
      </h2>
      <div class="flex items-center justify-center gap-2 mt-4">
        <div class="flex">
          <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
          <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
          <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
          <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
          <svg class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
        </div>
        <span class="text-sm font-medium" style="color:var(--lx-text-color)">4.9 out of 5</span>
      </div>
    </div>
    
    <div data-island="ReviewCarousel" data-props='{
      "productId": "coffee-ethiopian",
      "filterOptions": ["5-star", "Photo reviews", "Verified purchase"],
      "highlightKeywords": ["delicious", "fresh", "authentic", "best", "amazing", "perfect"]
    }'></div>
  </div>
</section>
```

---

## Photography

**CRITICAL:** Food is a visual vertical. Photography makes or breaks conversion.

### Photography Angles

1. **Overhead flat-lay** — Ingredients spread out. Shows abundance. Perfect for: variety packs, meal kit "what's inside".
2. **45-degree hero angle** — Product in use (mug, plate). Creates appetite. Perfect for: hero sections, lifestyle moments.
3. **Macro texture** — Extreme close-up (pour, drizzle, steam). Triggers sensory response. Perfect for: parallax sections, product detail.
4. **Ingredient heroes** — Raw materials (coffee cherries, tomatoes on vine). Shows quality. Perfect for: origin stories, farm-to-table.
5. **Preparation moments** — Action shots (pouring, stirring, chopping). Shows how to use. Perfect for: recipe sections, how-to.
6. **Unboxing** — Subscription box opened, products arranged. Shows value. Perfect for: subscription landing pages.

### Asset Generation Keywords

**For coffee/beverages:**
- "Overhead shot of steaming coffee cup on rustic wooden table, morning light, minimalist aesthetic"
- "Macro close-up of coffee beans being poured, shallow depth of field, warm tones"
- "Pour-over coffee setup with gooseneck kettle, artisan aesthetic, soft natural light"

**For snacks/packaged food:**
- "Flat-lay of colorful snack variety pack, vibrant packaging, scattered arrangement, white background"
- "Close-up of crunchy snack texture, appetizing macro shot, warm lighting"
- "Hand holding snack bag outdoors, lifestyle moment, natural setting"

**For meal kits/fresh food:**
- "Overhead flat-lay of fresh ingredients for meal kit, vibrant vegetables, recipe card visible"
- "Plated finished meal, restaurant-quality presentation, garnished, natural light"
- "Hands chopping vegetables on wooden cutting board, cooking process, warm kitchen"

**For sauces/condiments:**
- "Sauce drizzle on dish, macro shot, appetizing texture, shallow depth of field"
- "Hot sauce bottles arranged on rustic shelf, warm lighting, artisan aesthetic"
- "Close-up of sauce texture in bowl, vibrant color, food photography style"

---

## Anti-Patterns

These mistakes will tank conversion:

1. **Small food images** — Food must be 600px+ on desktop. Thumbnails don't trigger appetite.
2. **Clinical/sterile layouts** — All-white backgrounds look like a pharmacy. Add warmth.
3. **Missing texture/appetite cues** — No steam, drizzle, pour shots, close-ups = no sensory response.
4. **No sourcing story** — Food buyers care WHERE food comes from. Omitting origin = missed trust-building.
5. **Generic product-on-white** — Stock-looking shots with no context scream "commodity".
6. **Cold color palettes** — Blues, teals, grays are wrong for food. Use warm tones.
7. **Tech-style typography** — Ultra-thin fonts (200-300) feel cold. Use 400-600 weights.
8. **No preparation/recipe context** — Visitors need to imagine USING the product.
9. **Hiding nutrition info** — Health-conscious buyers need ingredients, allergens, macros.
10. **Subscription without clear savings** — Savings MUST be immediately visible, not hidden.
11. **Stock food photography** — Generic, perfect images scream "fake". Use real product photos.
12. **Too many flavors without guidance** — 12 flavors with no bestseller/sampler = decision paralysis.
13. **No freshness messaging** — Communicate "roasted this week", "made to order", "ships within 24 hours".
14. **Ignoring dietary filters** — No allergen info or vegan/gluten-free badges = losing customer segments.
15. **Weak CTAs** — "Buy Now" is boring. Use specific: "Shop [Flavor]", "Try the Sampler", "Build Your Box".

---

## Complete Blueprint: Premium Coffee PDP

```json
{
  "head": {
    "title": "Rich, Bold Ethiopian Yirgacheffe Coffee | Single-Origin",
    "description": "Premium single-origin Ethiopian Yirgacheffe coffee with notes of blueberry and dark chocolate. Roasted fresh weekly. Subscribe and save 20%.",
    "keywords": ["coffee", "single-origin", "ethiopian coffee", "organic coffee", "fair trade"]
  },
  "theme_css": ":root { --lx-accent-color: #6F4E37; --lx-text-color: #2C1810; --lx-text-muted: #5C4A42; --lx-bg-color: #FFFDF7; --lx-bg-surface: #F5EDE4; --lx-border-color: #E5D7CB; --lx-font-heading: 'Fraunces', serif; --lx-font-body: 'Inter', sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[80vh] flex items-end\" style=\"background:var(--lx-bg-color)\"><img src=\"coffee-hero.jpg\" alt=\"Coffee pour\" class=\"absolute inset-0 w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent\"></div><div class=\"relative z-10 max-w-3xl mx-auto text-center pb-16 px-6 text-white space-y-4\"><p class=\"text-xs uppercase tracking-[0.15em] opacity-80\">Single Origin • Small Batch</p><h1 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem);font-weight:600\">Your Morning Ritual, Perfected</h1><p style=\"font-size:clamp(1rem,2vw,1.25rem);line-height:1.6;opacity:90\">Rich Ethiopian Yirgacheffe with notes of blueberry and dark chocolate</p><button class=\"px-8 py-4 rounded-lg font-semibold bg-white text-black text-sm hover:bg-gray-100 transition\">Shop Coffee →</button></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "value-props",
      "html": "<section class=\"py-20 px-6\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-5xl mx-auto\"><div class=\"grid grid-cols-1 md:grid-cols-3 gap-12\"><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-bg-surface)\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path d=\"M10 3.5a1.5 1.5 0 013 0V4a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-.5a1.5 1.5 0 000 3h.5a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-.5a1.5 1.5 0 00-3 0v.5a1 1 0 01-1 1H6a1 1 0 01-1-1v-3a1 1 0 00-1-1h-.5a1.5 1.5 0 010-3H4a1 1 0 001-1V6a1 1 0 011-1h3a1 1 0 001-1v-.5z\"></path></svg></div><h3 style=\"font-family:var(--lx-font-heading);font-size:1.25rem;font-weight:600;color:var(--lx-text-color);margin-bottom:0.5rem\">Single-Origin Ethiopia</h3><p style=\"font-size:0.875rem;color:var(--lx-text-muted)\">From the Yirgacheffe region, 2,000m elevation</p></div><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-bg-surface)\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z\" clip-rule=\"evenodd\"></path></svg></div><h3 style=\"font-family:var(--lx-font-heading);font-size:1.25rem;font-weight:600;color:var(--lx-text-color);margin-bottom:0.5rem\">Small-Batch Roasted</h3><p style=\"font-size:0.875rem;color:var(--lx-text-muted)\">Roasted fresh weekly in Portland, Oregon</p></div><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-bg-surface)\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path d=\"M9 2a1 1 0 000 2h2a1 1 0 100-2H9z\"></path><path fill-rule=\"evenodd\" d=\"M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z\" clip-rule=\"evenodd\"></path></svg></div><h3 style=\"font-family:var(--lx-font-heading);font-size:1.25rem;font-weight:600;color:var(--lx-text-color);margin-bottom:0.5rem\">Tasting Notes</h3><p style=\"font-size:0.875rem;color:var(--lx-text-muted)\">Blueberry, dark chocolate, caramel finish</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "origin-story",
      "html": "<section class=\"relative min-h-[500px] flex items-center\" style=\"background:var(--lx-bg-color)\"><img src=\"farm.jpg\" alt=\"Ethiopian coffee farm\" class=\"absolute inset-0 w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-black/40\"></div><div class=\"relative z-10 max-w-3xl mx-auto text-center px-6 text-white space-y-4\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600\">Grown at 2,000 Meters in Yirgacheffe</h2><p style=\"font-size:clamp(1rem,2vw,1.25rem);line-height:1.65;max-width:40rem;margin:0 auto\">Sourced from the Abebech Women's Cooperative, where 200 smallholder farmers cultivate coffee with care and tradition.</p></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "subscription",
      "html": "<section class=\"py-24 px-6\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-5xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)\">Never Run Out</h2><p style=\"font-size:1.125rem;color:var(--lx-text-muted);margin-top:0.75rem\">Subscribe and save 20% on every delivery</p></div><div class=\"bg-white rounded-2xl shadow-xl p-10 max-w-2xl mx-auto\"><div class=\"flex flex-col md:flex-row items-center gap-8\"><img src=\"product.jpg\" alt=\"Coffee bag\" class=\"w-64 h-64 object-cover rounded-xl\" /><div class=\"flex-1\"><h3 style=\"font-family:var(--lx-font-heading);font-size:1.5rem;font-weight:600;color:var(--lx-text-color);margin-bottom:1rem\">Ethiopian Yirgacheffe</h3><div data-island=\"SubscriptionToggle\" data-props='{\"oneTimePrice\":24,\"subscriptionPrice\":19.20,\"savingsPercent\":20,\"frequencies\":[\"Every 2 weeks\",\"Every 1 month\",\"Every 2 months\"],\"defaultFrequency\":\"Every 1 month\"}'></div><p class=\"text-xs text-gray-500 mt-4\">Skip or cancel anytime. No commitment.</p></div></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-24 px-6\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><div class=\"text-center mb-12\"><p class=\"text-sm uppercase tracking-wider font-semibold mb-2\" style=\"color:var(--lx-accent-color)\">Loved by Thousands</p><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)\">Join 12,847 Happy Customers</h2></div><div data-island=\"ReviewCarousel\" data-props='{\"productId\":\"coffee-ethiopian\",\"filterOptions\":[\"5-star\",\"Photo reviews\",\"Verified purchase\"],\"highlightKeywords\":[\"delicious\",\"fresh\",\"authentic\",\"best\"]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "transparency",
      "html": "<section class=\"py-24 px-6\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)\">What's Inside</h2></div><div data-island=\"Tabs\" data-props='{\"tabs\":[{\"label\":\"Ingredients\",\"content\":\"<div class=\\\"space-y-4\\\"><div class=\\\"flex flex-wrap gap-3 mb-6\\\"><span class=\\\"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\\\">✓ Certified Organic</span><span class=\\\"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800\\\">✓ Fair Trade</span></div><p class=\\\"text-base\\\">100% Arabica Coffee Beans from Ethiopia</p></div>\"},{\"label\":\"Nutrition\",\"content\":\"<table class=\\\"w-full text-sm\\\"><tr class=\\\"border-b\\\"><td class=\\\"py-3\\\">Serving Size</td><td class=\\\"py-3 text-right font-medium\\\">8 fl oz</td></tr><tr class=\\\"border-b\\\"><td class=\\\"py-3\\\">Calories</td><td class=\\\"py-3 text-right font-medium\\\">5</td></tr><tr class=\\\"border-b\\\"><td class=\\\"py-3\\\">Caffeine</td><td class=\\\"py-3 text-right font-medium\\\">95mg</td></tr></table>\"},{\"label\":\"Allergens\",\"content\":\"<p>Contains: None</p><p class=\\\"text-xs text-gray-500 mt-2\\\">Processed in a facility that handles tree nuts</p>\"},{\"label\":\"Sourcing\",\"content\":\"<p>Sourced from the Yirgacheffe region of Ethiopia, where our partner cooperative Abebech works with over 200 smallholder farmers. Harvested at 1,800-2,200 meters elevation.</p>\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "faq",
      "html": "<section class=\"py-24 px-6\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-3xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--lx-text-color)\">Frequently Asked Questions</h2></div><div data-island=\"FAQ\" data-props='{\"questions\":[{\"q\":\"How should I store my coffee?\",\"a\":\"Store in an airtight container in a cool, dry place. Avoid refrigeration.\"},{\"q\":\"What is the caffeine content?\",\"a\":\"Approximately 95mg per 8oz cup.\"},{\"q\":\"Can I change my subscription frequency?\",\"a\":\"Yes, you can skip, pause, or adjust frequency anytime in your account.\"},{\"q\":\"What is your freshness guarantee?\",\"a\":\"We roast to order and ship within 24 hours. All coffee is roasted within 7 days of delivery.\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "stats",
      "html": "<section class=\"py-20 px-6\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-5xl mx-auto\"><div class=\"grid grid-cols-2 md:grid-cols-4 gap-8 text-center\"><div><p style=\"font-family:var(--lx-font-heading);font-size:2.5rem;font-weight:700;color:var(--lx-accent-color)\">500K+</p><p style=\"font-size:0.875rem;color:var(--lx-text-muted);margin-top:0.5rem\">Bags Shipped</p></div><div><p style=\"font-family:var(--lx-font-heading);font-size:2.5rem;font-weight:700;color:var(--lx-accent-color)\">4.9★</p><p style=\"font-size:0.875rem;color:var(--lx-text-muted);margin-top:0.5rem\">Average Rating</p></div><div><p style=\"font-family:var(--lx-font-heading);font-size:2.5rem;font-weight:700;color:var(--lx-accent-color)\">Fresh</p><p style=\"font-size:0.875rem;color:var(--lx-text-muted);margin-top:0.5rem\">Roasted Weekly</p></div><div><p style=\"font-family:var(--lx-font-heading);font-size:2.5rem;font-weight:700;color:var(--lx-accent-color)\">100%</p><p style=\"font-size:0.875rem;color:var(--lx-text-muted);margin-top:0.5rem\">Certified Organic</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "final-cta",
      "html": "<section class=\"relative min-h-[400px] flex items-center justify-center\"><img src=\"cta.jpg\" alt=\"Coffee mug on table\" class=\"absolute inset-0 w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-black/30\"></div><div class=\"relative z-10 text-center px-6 text-white space-y-6\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem);font-weight:600\">Your Morning Ritual, Perfected</h2><button class=\"px-10 py-5 rounded-lg font-semibold text-base bg-white text-black hover:bg-gray-100 transition\">Order Now</button></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

## Summary: The Food Page Playbook

1. **Lead with appetite** — Hero image must be large, appetizing, sensory (macro shots, steam, drizzle, texture).
2. **Warm everything** — Colors (browns, golds, reds, greens), lighting (morning sun, soft shadows), typography (friendly, readable).
3. **Tell the origin story** — Where it comes from matters. Build trust through transparency.
4. **Make it large** — Food images 600px+ on desktop. Never thumbnails.
5. **Subscriptions sell** — For consumables, show savings prominently, reduce commitment fear ("skip/cancel anytime").
6. **Nutrition transparency** — Tabs for ingredients, allergens, sourcing. Health-conscious buyers need this.
7. **Social proof = taste proof** — Reviews must emphasize flavor, freshness, repeat purchase. Photo reviews prioritized.
8. **Spacing is generous** — 80-96px between sections. Let food breathe.
9. **BundleBuilder for variety** — Visual selector, dynamic pricing, savings callout.
10. **Avoid coldness** — No clinical white, no tech blue, no thin fonts, no small images.

This is the blueprint for food pages that convert.
