# Beauty & Skincare — Storefront Design Intelligence

> When to load: Product vertical is beauty, skincare, haircare, body care, fragrance, or cosmetics.

## Philosophy

Beauty pages sell transformation, not product. Every section answers "what will I become?" not "what is this thing?"

**Key insight**: Beauty buyers are educated, ingredient-aware, results-driven. They've read Reddit threads, watched YouTube reviews, studied ingredient percentages. Design must feel premium but accessible — never condescending, never opaque about formulation.

**The conversion stack**: Before/After proof → Ingredient transparency → Social proof from people like me → Easy entry point. This order matters because beauty purchases are mini commitments to a 6-week transformation journey.

**What beauty pages are NOT**: Hype machines. Urgency timers kill trust. Stock models kill aspiration. Generic "clean beauty" claims kill credibility. Every element must answer: "Will this work for MY skin?"

---

## Section Sequences (by page type)

### PDP (Single Product)

**10-12 section sequence for a skincare/beauty product page:**

1. **Editorial Split Hero** — Hero ingredient or texture shot FIRST, then promise. Beauty is visual proof.
2. **Trust Strip** — Immediate credibility signals before they scroll
3. **Before/After Island** — Proof before they invest cognitive energy
4. **Multi-sensory Story** — Texture, application, ingredient close-ups
5. **Ingredient Explorer Island** — The beauty buyer's research moment
6. **Clinical Stats** — Proof translated to outcomes
7. **Review Carousel Island** — Social proof from skin types like mine
8. **Benefit Deep Dive** — How to use, what to expect, layering guidance
9. **FAQ Island** — Overcome formulation/safety objections
10. **UGC Gallery** — Community validation
11. **Product Carousel Island** — Upsell complementary steps
12. **Final CTA** — Conversion moment with trust reinforcement

### Routine Builder / Bundle

**8-10 sections for a multi-product routine page:**

1. **Centered Hero** — "Your [concern] routine in 3 steps"
2. **Step-by-step Grid** — Routine breakdown with application moments
3. **BuyBox Island** — Bundle configuration with savings
4. **Timeline Bento** — Results journey visualization (Week 1, 2, 4, 8)
5. **Before/After Island** — Full routine proof
6. **Tabs Island** — Ingredient transparency per product
7. **Bundle Reviews** — "Is it worth buying all 3?" social proof
8. **Routine FAQ** — Order, wait times, mixing safety
9. **Split CTA** — Bundle vs individual choice

### Before/After Results Page

**8-10 sections centered around transformation proof:**

1. **Split Hero** — Compelling before/after hero shot
2. **Clinical Stats** — Quantified transformation
3. **Before/After Gallery** — 6-10 transformations, filterable by skin type
4. **Video Testimonials** — Voice behind the transformation
5. **Interactive Parallax** — Scroll to reveal after state
6. **Timeline Expectations** — What to expect week by week
7. **Ingredient Explorer** — "How does it work?" after they're convinced
8. **UGC Feed** — Proof at scale
9. **Social Proof CTA** — "Join [number] others"

---

## Island Combinations

### IngredientExplorer + BeforeAfter = The Beauty Conversion Stack

**HTML Pattern:**

```html
<!-- BeforeAfter Island (Proof) -->
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-center mb-4 font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)">
      Real Results, Real People
    </h2>
    <p class="text-center mb-12 max-w-2xl mx-auto" style="color:var(--lx-text-muted);font-size:clamp(1rem,2vw,1.125rem)">
      All participants used the serum twice daily for 8 weeks. Same lighting, no filters.
    </p>
    <div data-island="BeforeAfter" data-props='{"transformations":[{"before_url":"before-1.jpg","after_url":"after-1.jpg","timeline":"8 weeks","caption":"Combo skin, 30s, hyperpigmentation"},{"before_url":"before-2.jpg","after_url":"after-2.jpg","timeline":"4 weeks","caption":"Dry skin, 40s, dullness"}]}'></div>
  </div>
</section>

<!-- IngredientExplorer Island (Mechanism) -->
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-center mb-4 font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)">
      The Science Behind the Results
    </h2>
    <p class="text-center mb-12 max-w-2xl mx-auto" style="color:var(--lx-text-muted);font-size:clamp(1rem,2vw,1.125rem)">
      4 powerful actives, clinically proven concentrations
    </p>
    <div data-island="IngredientExplorer" data-props='{"ingredients":[{"name":"Vitamin C (L-Ascorbic Acid)","percentage":"20%","benefit":"Brightens skin tone, fades hyperpigmentation, boosts collagen","source":"Derived from citrus fruits, stabilized in anhydrous base"},{"name":"Ferulic Acid","percentage":"0.5%","benefit":"Stabilizes vitamin C, enhances antioxidant protection","source":"Plant-derived from rice bran"},{"name":"Vitamin E","percentage":"1%","benefit":"Antioxidant protection, soothes and moisturizes","source":"Natural source tocopherol"},{"name":"Hyaluronic Acid","benefit":"Plumps skin, delivers 72-hour hydration","source":"Low + high molecular weight blend"}]}'></div>
  </div>
</section>
```

**Placement rules:**
- BeforeAfter above fold if it's your strongest asset
- IngredientExplorer after initial desire is established (never lead with ingredients)
- Stack them directly to create "It works, here's why" flow

### ReviewCarousel with Skin Type Metadata

```html
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-center mb-4 font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)">
      Love from Real Skin Types
    </h2>
    <div data-island="ReviewCarousel" data-props='{"reviews":[{"author":"Sarah M.","author_meta":"Combo skin, 30s, hyperpigmentation","rating":5,"title":"Finally, a vitamin C that doesn&apos;t irritate","body":"I&apos;ve tried 5+ vitamin C serums and they all made my skin red. This one is gentle and I&apos;m seeing results after 6 weeks.","usage_period":"6 weeks","image_url":"ugc-sarah.jpg"}]}'></div>
  </div>
</section>
```

### ProductCarousel for Routine Upsell

```html
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-7xl mx-auto">
    <h2 class="text-center mb-4 font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)">
      Complete Your Routine
    </h2>
    <p class="text-center mb-12" style="color:var(--lx-text-muted);font-size:clamp(1rem,2vw,1.125rem)">
      Pair with these complementary products for maximum results
    </p>
    <div data-island="ProductCarousel" data-props='{"products":[{"id":"gentle-cleanser","name":"Gentle Cleanser","price":28,"image":"cleanser.jpg"},{"id":"moisturizer","name":"Hydrating Moisturizer","price":42,"image":"moisturizer.jpg"}]}'></div>
  </div>
</section>
```

---

## Typography & Color

### Headline Styles

Beauty typography should feel **airy** and **editorial**, not bold and urgent.

```html
<!-- Hero Headline -->
<h1 class="mb-6" style="font-family:var(--lx-font-heading);font-size:clamp(2.5rem,5vw,4.5rem);font-weight:300;letter-spacing:-0.02em;line-height:1.1;color:var(--lx-text-color);max-width:20ch">
  Your Glass Skin Starts Here
</h1>

<!-- Section Headline -->
<h2 class="mb-4 font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);letter-spacing:-0.01em;line-height:1.2;color:var(--lx-text-color);max-width:24ch">
  Real Results, Real People
</h2>

<!-- Eyebrow (Trust Signal) -->
<p class="mb-3 uppercase tracking-widest" style="font-size:clamp(0.75rem,2vw,0.875rem);font-weight:500;letter-spacing:0.1em;color:var(--lx-text-muted)">
  Clinically Proven
</p>

<!-- Subline (Benefit Copy) -->
<p class="mb-6" style="font-size:clamp(1rem,2.5vw,1.25rem);font-weight:400;line-height:1.6;color:var(--lx-text-muted);max-width:48ch">
  Visibly reduce fine lines and hyperpigmentation in 4 weeks—without irritation.
</p>

<!-- Body Text -->
<p class="mb-4" style="font-size:clamp(0.875rem,2vw,1rem);font-weight:400;line-height:1.7;color:var(--lx-text-muted);max-width:65ch">
  This lightweight serum delivers hydration that lasts 72 hours, for plump, dewy skin.
</p>
```

### Color Patterns

**Foundation:**
```css
:root {
  --lx-bg-color: hsl(0, 0%, 98%);          /* Clean white */
  --lx-bg-surface: hsl(0, 0%, 96%);        /* Soft neutral */
  --lx-bg-surface-alt: hsl(30, 20%, 95%);  /* Warm tint for social proof */
  --lx-text-color: hsl(0, 0%, 10%);
  --lx-text-muted: hsl(0, 0%, 40%);
  --lx-border-color: hsl(0, 0%, 90%);
}
```

**Accent (derive from hero ingredient):**
- Vitamin C: `--lx-accent-color: hsl(30, 80%, 60%);` (warm gold/peach)
- Retinol: `--lx-accent-color: hsl(280, 40%, 50%);` (deep purple/plum)
- Hyaluronic acid: `--lx-accent-color: hsl(200, 60%, 60%);` (water blue)
- Niacinamide: `--lx-accent-color: hsl(340, 50%, 70%);` (soft rose)
- Botanical/green tea: `--lx-accent-color: hsl(120, 20%, 50%);` (sage green)

**Usage:**
```html
<button class="px-8 py-4 rounded-lg font-medium" style="background:var(--lx-accent-color);color:white">
  Shop Vitamin C Serum
</button>
```

---

## Hero Patterns

### Editorial Split Hero (Beauty)

```html
<section class="grid grid-cols-1 lg:grid-cols-2 min-h-[85vh]">
  <div class="flex items-center px-6 lg:px-16 py-16 order-2 lg:order-1" style="background:var(--lx-bg-color)">
    <div class="space-y-6 max-w-lg">
      <p class="text-xs uppercase tracking-widest" style="color:var(--lx-accent-color)">
        Vitamin C Serum
      </p>
      <h1 class="leading-tight" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3.5rem);font-weight:400;color:var(--lx-text-color)">
        Your Glow Starts Here
      </h1>
      <p class="text-base leading-relaxed" style="color:var(--lx-text-muted)">
        15% L-Ascorbic Acid + Ferulic Acid. Clinically proven to brighten in 14 days.
      </p>
      <button class="px-8 py-4 rounded-lg font-medium text-sm transition-opacity hover:opacity-90" style="background:var(--lx-accent-color);color:white">
        Shop Vitamin C →
      </button>
    </div>
  </div>
  <div class="relative order-1 lg:order-2 min-h-[50vh] lg:min-h-full">
    <img src="IMAGE_URL" alt="Vitamin C Serum texture" class="absolute inset-0 w-full h-full object-cover" />
  </div>
</section>
```

### Before/After Hero

```html
<section class="min-h-[90vh] flex flex-col items-center justify-center px-4 py-16" style="background:var(--lx-bg-color)">
  <div class="text-center mb-12 max-w-3xl">
    <p class="text-xs uppercase tracking-widest mb-4" style="color:var(--lx-accent-color)">
      Clinical Results
    </p>
    <h1 class="mb-6" style="font-family:var(--lx-font-heading);font-size:clamp(2.5rem,5vw,4rem);font-weight:300;letter-spacing:-0.02em;line-height:1.1;color:var(--lx-text-color)">
      94% Saw Smoother Skin in 4 Weeks
    </h1>
    <p style="font-size:clamp(1rem,2.5vw,1.25rem);color:var(--lx-text-muted)">
      Retinol 1% + bakuchiol: clinical strength, zero irritation.
    </p>
  </div>
  <div class="w-full max-w-4xl">
    <div data-island="BeforeAfter" data-props='{"transformations":[{"before_url":"hero-before.jpg","after_url":"hero-after.jpg","timeline":"8 weeks","caption":"Dry skin, 40s, fine lines"}]}'></div>
  </div>
</section>
```

---

## Ingredient Section Pattern

```html
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-4xl mx-auto">
    <div class="text-center mb-12">
      <p class="text-xs uppercase tracking-widest mb-3" style="color:var(--lx-accent-color)">
        Active Ingredients
      </p>
      <h2 class="mb-4 font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)">
        4 Powerful Actives, One Gentle Formula
      </h2>
      <p class="max-w-2xl mx-auto" style="color:var(--lx-text-muted);font-size:clamp(1rem,2vw,1.125rem)">
        Clinically proven concentrations for visible results
      </p>
    </div>
    <div data-island="IngredientExplorer" data-props='{"ingredients":[{"name":"Vitamin C (L-Ascorbic Acid)","percentage":"20%","benefit":"Brightens skin tone, fades hyperpigmentation, boosts collagen production","source":"Derived from citrus fruits, stabilized in anhydrous base"},{"name":"Ferulic Acid","percentage":"0.5%","benefit":"Stabilizes vitamin C, enhances antioxidant protection","source":"Plant-derived from rice bran"},{"name":"Vitamin E (Tocopherol)","percentage":"1%","benefit":"Antioxidant protection, soothes and moisturizes","source":"Natural source tocopherol"},{"name":"Hyaluronic Acid","benefit":"Plumps skin, delivers 72-hour hydration","source":"Low + high molecular weight blend"}]}'></div>
  </div>
</section>
```

---

## Social Proof for Beauty

### Review Grid with Skin Type Metadata

```html
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-center mb-4 font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)">
      Real Results from Real Skin Types
    </h2>
    <p class="text-center mb-12 max-w-2xl mx-auto" style="color:var(--lx-text-muted);font-size:clamp(1rem,2vw,1.125rem)">
      Verified reviews from customers like you
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- Review Card -->
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface);border:1px solid var(--lx-border-color)">
        <div class="flex items-center gap-1 mb-3">
          <span class="text-yellow-400">★★★★★</span>
        </div>
        <h3 class="font-bold mb-2" style="color:var(--lx-text-color)">
          Finally, a vitamin C that doesn't irritate
        </h3>
        <p class="text-sm mb-4" style="color:var(--lx-text-muted);line-height:1.6">
          I've tried 5+ vitamin C serums and they all made my skin red. This one is gentle and I'm seeing results after 6 weeks.
        </p>
        <div class="flex items-center gap-2">
          <img src="avatar.jpg" alt="Sarah M." class="w-10 h-10 rounded-full object-cover" />
          <div>
            <p class="text-sm font-medium" style="color:var(--lx-text-color)">Sarah M.</p>
            <p class="text-xs" style="color:var(--lx-text-muted)">Combo skin, 30s, hyperpigmentation</p>
          </div>
        </div>
      </div>
      <!-- Repeat for more reviews -->
    </div>
  </div>
</section>
```

### UGC Gallery

```html
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-surface-alt)">
  <div class="max-w-7xl mx-auto">
    <h2 class="text-center mb-4 font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)">
      10,000+ Transformations and Counting
    </h2>
    <p class="text-center mb-12" style="color:var(--lx-text-muted);font-size:clamp(1rem,2vw,1.125rem)">
      #YourBrandResults
    </p>
    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      <div class="aspect-square rounded-lg overflow-hidden">
        <img src="ugc-1.jpg" alt="Customer result" class="w-full h-full object-cover hover:scale-105 transition-transform duration-300" />
      </div>
      <div class="aspect-square rounded-lg overflow-hidden">
        <img src="ugc-2.jpg" alt="Customer result" class="w-full h-full object-cover hover:scale-105 transition-transform duration-300" />
      </div>
      <!-- Repeat for more UGC -->
    </div>
  </div>
</section>
```

### Clinical Stats

```html
<section class="py-16 lg:py-24 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto">
    <p class="text-center text-xs uppercase tracking-widest mb-3" style="color:var(--lx-accent-color)">
      Clinical Results
    </p>
    <h2 class="text-center mb-16 font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)">
      Proven in Clinical Studies
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
      <div class="text-center">
        <div class="mb-3" style="font-size:clamp(3rem,6vw,5rem);font-weight:700;color:var(--lx-accent-color)">
          94%
        </div>
        <p class="font-medium mb-2" style="color:var(--lx-text-color)">
          Saw brighter, more even skin tone
        </p>
        <p class="text-sm" style="color:var(--lx-text-muted)">
          In 4 weeks*
        </p>
      </div>
      <div class="text-center">
        <div class="mb-3" style="font-size:clamp(3rem,6vw,5rem);font-weight:700;color:var(--lx-accent-color)">
          87%
        </div>
        <p class="font-medium mb-2" style="color:var(--lx-text-color)">
          Noticed reduced hyperpigmentation
        </p>
        <p class="text-sm" style="color:var(--lx-text-muted)">
          In 8 weeks*
        </p>
      </div>
      <div class="text-center">
        <div class="mb-3" style="font-size:clamp(3rem,6vw,5rem);font-weight:700;color:var(--lx-accent-color)">
          4.8★
        </div>
        <p class="font-medium mb-2" style="color:var(--lx-text-color)">
          Average rating from 2,847 reviews
        </p>
        <p class="text-sm" style="color:var(--lx-text-muted)">
          Verified purchases
        </p>
      </div>
    </div>
    <p class="text-center mt-12 text-xs" style="color:var(--lx-text-muted)">
      *Clinical study of 50 participants using product twice daily
    </p>
  </div>
</section>
```

---

## Photography & Assets

### What to Search/Generate

**Texture shots:**
- "Close-up macro shot of vitamin C serum texture, golden drop, refracted light, clean white background, product photography, 4k"
- "Cream swirl texture macro, rich moisturizer, soft lighting, beauty editorial photography"
- "Lightweight oil serum on glass, sheen effect, non-greasy proof, product photography"

**Application moments:**
- "Hand applying serum to cheekbone, fingertips, natural skin tone, soft diffused lighting, beauty editorial"
- "Dropper above skin close-up, precision application, clean aesthetic, skincare photography"

**Ingredient hero shots:**
- "Orange citrus slices and vitamin C serum, bright airy lighting, minimal composition, skincare photography"
- "Purple starry night botanical illustration, retinol concept, luxury skincare aesthetic"
- "Water drops on dewy petals macro, hyaluronic acid visual metaphor, clean beauty photography"
- "Niacinamide ingredient illustration, soft pink flowers, morning light, botanical photography"

**Before/After specifications:**
- Same lighting (indoor, diffused, front-facing)
- Same angle (straight-on for face, 45° for body)
- Unfiltered, unretouched (credibility)
- Include timeline text overlay

---

## Anti-Patterns (Beauty Killers)

| Anti-Pattern | Why It Kills | Fix |
|---|---|---|
| Generic product-on-white photography | Commodity positioning, no differentiation | Add context (marble, botanicals), show texture, show application |
| "Clean beauty" without specifics | Vague, virtue-signaling, no trust | Specify exclusions (parabens, sulfates) AND why |
| Too many products on one page | Decision paralysis | One hero product per page, cross-sell via carousel at end |
| Scientific jargon without explanation | Alienates non-expert buyers | Translate: "Niacinamide 10%" → "Minimizes pores and evens skin tone" |
| Stock model faces (full face) | Looks like an ad, can't see skin detail | Macro skin shots, hands applying, before/after close-ups |
| Masculine/aggressive typography | Feels urgent = cheap | Light weights (300-400), generous spacing, serif optional |
| Urgency timers on luxury beauty | Scarcity tactics destroy premium positioning | Use social proof numbers instead ("Join 10,000+ others") |
| Ignoring skin type targeting | "Will this work for MY skin?" is question #1 | Tag products with skin types, show filtered reviews |
| No ingredient transparency | Opacity = hiding something | Full ingredient list accessible, hero ingredients called out |
| Before/after in different lighting | Looks manipulated, kills trust instantly | Same lighting, angle, distance; unfiltered; timeline overlay |
| Generic benefits copy | "Hydrates skin" = every product ever | Specific, quantified: "72-hour hydration" "Reduces lines 23% in 4 weeks" |
| No usage instructions | Beauty buyers need to know HOW | Include "How to use": AM/PM? Before/after moisturizer? How much? |

---

## Complete Page Blueprint

### Premium Vitamin C Serum PDP (VibePage Format)

```json
{
  "head": {
    "title": "Vitamin C Serum 20% — Brighten & Even Skin Tone",
    "description": "Clinical-strength vitamin C serum with ferulic acid. Visibly brighten skin and fade hyperpigmentation in 4 weeks. Gentle, pH-balanced formula.",
    "fonts": [
      "https://fonts.googleapis.com/css2?family=Cormorant:wght@300;400;500&family=Inter:wght@400;500;600&display=swap"
    ]
  },
  "theme_css": ":root { --lx-accent-color: hsl(30, 80%, 60%); --lx-text-color: hsl(0, 0%, 10%); --lx-text-muted: hsl(0, 0%, 40%); --lx-bg-color: hsl(0, 0%, 98%); --lx-bg-surface: hsl(0, 0%, 96%); --lx-bg-surface-alt: hsl(30, 20%, 95%); --lx-border-color: hsl(0, 0%, 90%); --lx-font-heading: 'Cormorant', serif; --lx-font-body: 'Inter', sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"grid grid-cols-1 lg:grid-cols-2 min-h-[85vh]\"><div class=\"flex items-center px-6 lg:px-16 py-16 order-2 lg:order-1\" style=\"background:var(--lx-bg-color)\"><div class=\"space-y-6 max-w-lg\"><p class=\"text-xs uppercase tracking-widest\" style=\"color:var(--lx-accent-color)\">Vitamin C Serum</p><h1 class=\"leading-tight\" style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3.5rem);font-weight:400;color:var(--lx-text-color)\">Your Glow Starts Here</h1><p class=\"text-base leading-relaxed\" style=\"color:var(--lx-text-muted)\">20% L-Ascorbic Acid + Ferulic Acid. Clinically proven to brighten in 14 days.</p><button class=\"px-8 py-4 rounded-lg font-medium text-sm transition-opacity hover:opacity-90\" style=\"background:var(--lx-accent-color);color:white\">Shop Vitamin C →</button></div></div><div class=\"relative order-1 lg:order-2 min-h-[50vh] lg:min-h-full\"><img src=\"serum-texture-hero.jpg\" alt=\"Vitamin C Serum golden texture\" class=\"absolute inset-0 w-full h-full object-cover\" /></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "trust-strip",
      "html": "<section class=\"py-12 px-4\" style=\"background:var(--lx-bg-surface);border-top:1px solid var(--lx-border-color);border-bottom:1px solid var(--lx-border-color)\"><div class=\"max-w-5xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8\"><div class=\"text-center\"><div class=\"w-12 h-12 mx-auto mb-3 rounded-full flex items-center justify-center\" style=\"background:var(--lx-accent-color);color:white\"><svg class=\"w-6 h-6\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z\"/></svg></div><p class=\"text-sm font-medium\" style=\"color:var(--lx-text-color)\">Clinically Proven</p></div><div class=\"text-center\"><div class=\"w-12 h-12 mx-auto mb-3 rounded-full flex items-center justify-center\" style=\"background:var(--lx-accent-color);color:white\"><svg class=\"w-6 h-6\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z\"/></svg></div><p class=\"text-sm font-medium\" style=\"color:var(--lx-text-color)\">Dermatologist Tested</p></div><div class=\"text-center\"><div class=\"w-12 h-12 mx-auto mb-3 rounded-full flex items-center justify-center\" style=\"background:var(--lx-accent-color);color:white\"><svg class=\"w-6 h-6\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z\"/></svg></div><p class=\"text-sm font-medium\" style=\"color:var(--lx-text-color)\">Clean Ingredients</p></div><div class=\"text-center\"><div class=\"w-12 h-12 mx-auto mb-3 rounded-full flex items-center justify-center\" style=\"background:var(--lx-accent-color);color:white\"><svg class=\"w-6 h-6\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z\"/></svg></div><p class=\"text-sm font-medium\" style=\"color:var(--lx-text-color)\">Cruelty-Free</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "before-after",
      "html": "<section class=\"py-16 lg:py-24 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><h2 class=\"text-center mb-4 font-bold\" style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)\">Real Results, Real People</h2><p class=\"text-center mb-12 max-w-2xl mx-auto\" style=\"color:var(--lx-text-muted);font-size:clamp(1rem,2vw,1.125rem)\">All participants used the serum twice daily for 8 weeks. Same lighting, no filters.</p><div data-island=\"BeforeAfter\" data-props='{\"transformations\":[{\"before_url\":\"before-1.jpg\",\"after_url\":\"after-1.jpg\",\"timeline\":\"8 weeks\",\"caption\":\"Combo skin, 30s, hyperpigmentation\"},{\"before_url\":\"before-2.jpg\",\"after_url\":\"after-2.jpg\",\"timeline\":\"4 weeks\",\"caption\":\"Dry skin, 40s, dullness\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "texture-story",
      "html": "<section class=\"py-16 lg:py-24 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4\"><div class=\"relative aspect-square overflow-hidden rounded-lg\"><img src=\"texture-macro.jpg\" alt=\"Serum texture\" class=\"w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-6\"><p class=\"text-white font-medium\">Lightweight, fast-absorbing</p></div></div><div class=\"relative aspect-square overflow-hidden rounded-lg\"><video src=\"application.mp4\" autoplay loop muted playsinline class=\"w-full h-full object-cover\"></video><div class=\"absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-6\"><p class=\"text-white font-medium\">One dropper, morning + evening</p></div></div><div class=\"relative aspect-square overflow-hidden rounded-lg\"><img src=\"orange-citrus.jpg\" alt=\"Vitamin C source\" class=\"w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-6\"><p class=\"text-white font-medium\">Pure L-Ascorbic Acid</p></div></div><div class=\"relative aspect-square overflow-hidden rounded-lg flex flex-col items-center justify-center p-6\" style=\"background:var(--lx-accent-color);color:white\"><h3 class=\"text-2xl font-bold mb-2\" style=\"font-family:var(--lx-font-heading)\">Stable & Potent</h3><p class=\"text-sm text-center\">Anhydrous formula keeps vitamin C at peak efficacy</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "ingredients",
      "html": "<section class=\"py-16 lg:py-24 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-4xl mx-auto\"><div class=\"text-center mb-12\"><p class=\"text-xs uppercase tracking-widest mb-3\" style=\"color:var(--lx-accent-color)\">Active Ingredients</p><h2 class=\"mb-4 font-bold\" style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)\">4 Powerful Actives, One Gentle Formula</h2><p class=\"max-w-2xl mx-auto\" style=\"color:var(--lx-text-muted);font-size:clamp(1rem,2vw,1.125rem)\">Clinically proven concentrations for visible results</p></div><div data-island=\"IngredientExplorer\" data-props='{\"ingredients\":[{\"name\":\"Vitamin C (L-Ascorbic Acid)\",\"percentage\":\"20%\",\"benefit\":\"Brightens skin tone, fades hyperpigmentation, boosts collagen production\",\"source\":\"Derived from citrus fruits, stabilized in anhydrous base\"},{\"name\":\"Ferulic Acid\",\"percentage\":\"0.5%\",\"benefit\":\"Stabilizes vitamin C, enhances antioxidant protection\",\"source\":\"Plant-derived from rice bran\"},{\"name\":\"Vitamin E (Tocopherol)\",\"percentage\":\"1%\",\"benefit\":\"Antioxidant protection, soothes and moisturizes\",\"source\":\"Natural source tocopherol\"},{\"name\":\"Hyaluronic Acid\",\"benefit\":\"Plumps skin, delivers 72-hour hydration\",\"source\":\"Low + high molecular weight blend\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "clinical-stats",
      "html": "<section class=\"py-16 lg:py-24 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-6xl mx-auto\"><p class=\"text-center text-xs uppercase tracking-widest mb-3\" style=\"color:var(--lx-accent-color)\">Clinical Results</p><h2 class=\"text-center mb-16 font-bold\" style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)\">Proven in Clinical Studies</h2><div class=\"grid grid-cols-1 md:grid-cols-3 gap-12\"><div class=\"text-center\"><div class=\"mb-3\" style=\"font-size:clamp(3rem,6vw,5rem);font-weight:700;color:var(--lx-accent-color)\">94%</div><p class=\"font-medium mb-2\" style=\"color:var(--lx-text-color)\">Saw brighter, more even skin tone</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">In 4 weeks*</p></div><div class=\"text-center\"><div class=\"mb-3\" style=\"font-size:clamp(3rem,6vw,5rem);font-weight:700;color:var(--lx-accent-color)\">87%</div><p class=\"font-medium mb-2\" style=\"color:var(--lx-text-color)\">Noticed reduced hyperpigmentation</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">In 8 weeks*</p></div><div class=\"text-center\"><div class=\"mb-3\" style=\"font-size:clamp(3rem,6vw,5rem);font-weight:700;color:var(--lx-accent-color)\">4.8★</div><p class=\"font-medium mb-2\" style=\"color:var(--lx-text-color)\">Average rating from 2,847 reviews</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Verified purchases</p></div></div><p class=\"text-center mt-12 text-xs\" style=\"color:var(--lx-text-muted)\">*Clinical study of 50 participants using product twice daily</p></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-16 lg:py-24 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><h2 class=\"text-center mb-4 font-bold\" style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)\">Love from Real Skin Types</h2><div data-island=\"ReviewCarousel\" data-props='{\"reviews\":[{\"author\":\"Sarah M.\",\"author_meta\":\"Combo skin, 30s, hyperpigmentation\",\"rating\":5,\"title\":\"Finally, a vitamin C that doesn&apos;t irritate\",\"body\":\"I&apos;ve tried 5+ vitamin C serums and they all made my skin red. This one is gentle and I&apos;m seeing results after 6 weeks.\",\"usage_period\":\"6 weeks\",\"image_url\":\"ugc-sarah.jpg\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "how-to-use",
      "html": "<section class=\"py-16 lg:py-24 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-6xl mx-auto\"><div class=\"grid grid-cols-1 lg:grid-cols-3 gap-12\"><div><h3 class=\"text-xl font-bold mb-4\" style=\"font-family:var(--lx-font-heading);color:var(--lx-text-color)\">How to Use</h3><p style=\"color:var(--lx-text-muted);line-height:1.7\">Apply 3-4 drops to clean, dry skin every morning. Follow with moisturizer and SPF.</p></div><div><h3 class=\"text-xl font-bold mb-4\" style=\"font-family:var(--lx-font-heading);color:var(--lx-text-color)\">What to Expect</h3><p style=\"color:var(--lx-text-muted);line-height:1.7\">Week 1: Brighter, more radiant skin. Week 4: Fading hyperpigmentation. Week 8: Visibly even tone.</p></div><div><h3 class=\"text-xl font-bold mb-4\" style=\"font-family:var(--lx-font-heading);color:var(--lx-text-color)\">Layer with Confidence</h3><p style=\"color:var(--lx-text-muted);line-height:1.7\">Pairs perfectly with hyaluronic acid, niacinamide, and retinol (use retinol at night).</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "faq",
      "html": "<section class=\"py-16 lg:py-24 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-3xl mx-auto\"><h2 class=\"text-center mb-12 font-bold\" style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);color:var(--lx-text-color)\">Your Questions, Answered</h2><div data-island=\"FAQ\" data-props='{\"items\":[{\"question\":\"Is this safe for sensitive skin?\",\"answer\":\"Yes. While vitamin C can be irritating at high concentrations, our formula is pH-balanced and includes soothing ferulic acid.\"},{\"question\":\"Can I use this while pregnant or breastfeeding?\",\"answer\":\"Vitamin C is generally considered safe during pregnancy, but consult your doctor before starting any new skincare product.\"},{\"question\":\"Why is the serum slightly yellow?\",\"answer\":\"Pure L-ascorbic acid has a natural yellow tint. This is normal and indicates freshness. Oxidized vitamin C turns dark brown.\"},{\"question\":\"Can I use this with retinol?\",\"answer\":\"Yes. Use vitamin C in the morning and retinol at night for best results.\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta",
      "html": "<section class=\"py-16 lg:py-24 px-4\" style=\"background:linear-gradient(135deg, hsl(30, 80%, 60%) 0%, hsl(30, 70%, 50%) 100%)\"><div class=\"max-w-3xl mx-auto text-center\"><h2 class=\"mb-6 font-bold text-white\" style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem)\">Start Your Glass Skin Journey</h2><p class=\"mb-8 text-white/90\" style=\"font-size:clamp(1rem,2vw,1.125rem)\">Join 10,000+ others who've transformed their skin with clinical-strength vitamin C.</p><button class=\"px-10 py-5 rounded-lg font-semibold text-lg transition-all hover:scale-105\" style=\"background:white;color:hsl(30, 80%, 60%)\">Shop Vitamin C Serum</button><div class=\"flex items-center justify-center gap-8 mt-8 text-white/80 text-sm\"><span>✓ Free shipping</span><span>✓ 60-day returns</span><span>✓ Dermatologist approved</span></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```
