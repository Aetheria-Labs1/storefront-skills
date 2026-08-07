# Meta Ads → Landing Page — Storefront Design Intelligence

> **When to load**: Page generated from Meta (Facebook/Instagram) ad creative.  
> **Auto-loads as**: `vibe://skills/traffic-source-meta`

---

## The #1 Rule: Message Match

Meta traffic arrives **interrupted** — they were scrolling feed, not searching. The #1 conversion killer is message discontinuity between ad and landing page.

### Exact Match (Best for Direct Response)
Ad headline: "Finally, a yoga mat that doesn't slip during downward dog"  
Page headline: "Finally, a yoga mat that doesn't slip during downward dog"

```html
<h1 class="font-bold leading-[1.1]" style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem)">
  Finally, a yoga mat that doesn't slip during downward dog
</h1>
<p class="text-lg mt-3" style="color:var(--lx-text-muted)">
  Join 47,000+ yogis who switched to the GripFlow™ non-slip surface
</p>
```

### Evolved Match (Best for Product Pages)
Ad headline: "The yoga mat your feet won't slide on"  
Page headline: "Meet the GripFlow™ Yoga Mat"

```html
<h1 class="font-bold leading-[1.1]" style="font-family:var(--lx-font-heading);font-size:clamp(2.25rem,6vw,4rem)">
  Meet the GripFlow™ Yoga Mat
</h1>
<p class="text-xl mt-4" style="color:var(--lx-text-muted)">
  The non-slip surface that keeps you locked in—even in hot yoga
</p>
```

### Visual Continuity
If the ad shows **product on pink background** → hero must match:

```html
<section class="relative min-h-[85vh] flex items-center" 
  style="background:linear-gradient(to bottom, #FFE5F0 0%, #FFFFFF 100%)">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <!-- Product hero content -->
  </div>
</section>
```

If the ad shows **bold sans-serif headline** → page font must match:

```css
:root {
  --lx-font-heading: 'Inter', system-ui, sans-serif;
}
```

**Ad CTA color = page CTA color:**

```css
:root {
  --lx-accent-color: #FF6B6B;  /* Extracted from ad creative */
}
```

---

## Mobile-First Reality

**85%+ of Meta ad traffic is mobile.** Every design decision must pass the "thumb-zone test."

### Typography for Mobile
All text uses fluid sizing:

```html
<!-- Hero headline -->
<h1 style="font-size:clamp(2rem,5vw,3.5rem);line-height:1.1;letter-spacing:-0.02em;font-weight:700">
  Your yoga mat won't slip anymore
</h1>

<!-- Subline -->
<p style="font-size:clamp(1.125rem,3vw,1.375rem);line-height:1.4;margin-top:1rem">
  The GripFlow™ surface stays locked—even in hot yoga
</p>

<!-- Body copy -->
<p style="font-size:clamp(1rem,2.5vw,1.125rem);line-height:1.6">
  No more adjusting your hands mid-flow. No more slipping in downward dog.
</p>
```

### Spacing for Mobile
Use `clamp()` for all vertical spacing:

```html
<section style="padding-top:clamp(2rem,8vw,5rem);padding-bottom:clamp(2rem,8vw,5rem)">
  <!-- Section content -->
</section>
```

### Tap Targets & Thumb Zone
**All CTAs: min 44px height, large tap area**

```html
<!-- Primary CTA -->
<button class="w-full sm:w-auto px-8 rounded-lg font-semibold transition-colors"
  style="padding-top:0.875rem;padding-bottom:0.875rem;min-height:44px;background:var(--lx-accent-color);color:white">
  Get yours now
</button>

<!-- Sticky CTA (thumb zone) -->
<div data-island="StickyBar" data-props='{
  "trigger_scroll": "50vh",
  "cta_text": "Get my GripFlow mat",
  "price": "$79",
  "trust_badge": "60-day guarantee"
}'></div>
```

---

## Section Sequence (The Meta Formula)

This is the **proven sequence for cold Meta traffic** (no brand familiarity, interrupted state):

### 1. Hero (Message Match + Immediate Trust)
**Why first**: 3-second decision window.

```html
<section class="relative min-h-[80vh] flex items-center px-4" style="background:var(--lx-bg-color)">
  <div class="max-w-2xl mx-auto text-center space-y-5">
    <!-- Trust bar (immediate) -->
    <div class="flex justify-center items-center gap-2 text-sm">
      <div class="flex">
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
        <svg class="w-5 h-5" style="fill:gold"><!-- star --></svg>
      </div>
      <span class="font-semibold" style="color:var(--lx-text-color)">4.9/5 from 12,847 reviews</span>
    </div>

    <!-- Headline (message match) -->
    <h1 class="font-bold leading-[1.1]" 
      style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem)">
      Your yoga mat won't slip anymore
    </h1>

    <!-- Subline -->
    <p class="text-lg" style="color:var(--lx-text-muted)">
      Join 47,000+ yogis who solved their slipping problem
    </p>

    <!-- CTA -->
    <button class="px-8 py-4 rounded-lg font-semibold" 
      style="background:var(--lx-accent-color);color:white">
      Get yours now
    </button>

    <!-- Product image -->
    <img src="product-in-use.jpg" alt="GripFlow Yoga Mat" 
      class="w-full max-w-md mx-auto rounded-lg" />
  </div>
</section>
```

### 2. Trust Strip (Immediately After Hero)
**Why second**: Meta traffic has ZERO brand equity.

```html
<section class="py-8 border-b" style="background:var(--lx-bg-surface);border-color:var(--lx-border-color)">
  <div class="max-w-7xl mx-auto px-4">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- shield icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">60-Day Guarantee</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">Love it or return it</p>
      </div>
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- truck icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">Free Shipping</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">On all US orders</p>
      </div>
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- star icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">12,847 5-Star Reviews</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">Rated Excellent</p>
      </div>
      <div class="space-y-1">
        <svg class="w-8 h-8 mx-auto" style="color:var(--lx-accent-color)"><!-- award icon --></svg>
        <p class="font-semibold" style="color:var(--lx-text-color)">Featured in Yoga Journal</p>
        <p class="text-sm" style="color:var(--lx-text-muted)">Best Mat 2025</p>
      </div>
    </div>
  </div>
</section>
```

### 3. Problem Agitation
**Why third**: Twist the knife before showing solution.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto px-4">
    <h2 class="text-center font-bold mb-12" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      Sick of yoga mats that work against you?
    </h2>
    <div class="grid md:grid-cols-3 gap-6">
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface);border:1px solid var(--lx-border-color)">
        <svg class="w-10 h-10 mb-4" style="color:#EF4444"><!-- x-circle --></svg>
        <h3 class="font-semibold mb-2" style="color:var(--lx-text-color)">Slipping during downward dog</h3>
        <p style="color:var(--lx-text-muted)">You adjust your hands 5 times per flow</p>
      </div>
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface);border:1px solid var(--lx-border-color)">
        <svg class="w-10 h-10 mb-4" style="color:#EF4444"><!-- x-circle --></svg>
        <h3 class="font-semibold mb-2" style="color:var(--lx-text-color)">Sweaty palms = zero grip</h3>
        <p style="color:var(--lx-text-muted)">Hot yoga becomes a safety hazard</p>
      </div>
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface);border:1px solid var(--lx-border-color)">
        <svg class="w-10 h-10 mb-4" style="color:#EF4444"><!-- x-circle --></svg>
        <h3 class="font-semibold mb-2" style="color:var(--lx-text-color)">Cheap mats fall apart</h3>
        <p style="color:var(--lx-text-muted)">You've replaced yours 3 times already</p>
      </div>
    </div>
  </div>
</section>
```

### 4. Solution (The Reveal)
**Why fourth**: Now they're primed.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto px-4">
    <div class="text-center mb-12">
      <h2 class="font-bold mb-4" 
        style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
        Meet the GripFlow™ Yoga Mat
      </h2>
      <p class="text-lg" style="color:var(--lx-text-muted)">
        Engineered to solve every problem you just nodded at
      </p>
    </div>

    <div class="grid md:grid-cols-3 gap-8">
      <!-- Feature 1 -->
      <div class="text-center space-y-4">
        <img src="texture-closeup.jpg" alt="GripFlow surface" class="w-full rounded-lg" />
        <h3 class="font-bold text-xl" style="color:var(--lx-text-color)">GripFlow™ Non-Slip Surface</h3>
        <p style="color:var(--lx-text-muted)">
          Proprietary texture that gets grippier as you sweat
        </p>
      </div>

      <!-- Feature 2 -->
      <div class="text-center space-y-4">
        <img src="thickness-demo.jpg" alt="6mm cushion" class="w-full rounded-lg" />
        <h3 class="font-bold text-xl" style="color:var(--lx-text-color)">6mm Cushion Core</h3>
        <p style="color:var(--lx-text-muted)">
          Knee-saving thickness without sacrificing stability
        </p>
      </div>

      <!-- Feature 3 -->
      <div class="text-center space-y-4">
        <img src="durability.jpg" alt="Lifetime warranty" class="w-full rounded-lg" />
        <h3 class="font-bold text-xl" style="color:var(--lx-text-color)">Lifetime Durability</h3>
        <p style="color:var(--lx-text-muted)">
          Won't peel, crack, or fade—backed by lifetime warranty
        </p>
      </div>
    </div>
  </div>
</section>
```

### 5. Social Proof (Overcome Skepticism)
**Why fifth**: Flood them with proof.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto px-4">
    <h2 class="text-center font-bold mb-12" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      47,000+ yogis upgraded their practice
    </h2>

    <div class="grid md:grid-cols-3 gap-6">
      <!-- Review 1 -->
      <div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid var(--lx-border-color)">
        <div class="flex">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
        </div>
        <p style="color:var(--lx-text-color);font-size:0.9375rem;line-height:1.5">
          "I've tried 8 different mats. This is the only one that doesn't slip during hot yoga. The grip actually gets better when I sweat. Insane."
        </p>
        <div class="flex items-center gap-3">
          <img src="sarah-avatar.jpg" class="w-10 h-10 rounded-full" alt="Sarah M." />
          <div>
            <p class="font-semibold text-sm" style="color:var(--lx-text-color)">Sarah M.</p>
            <p class="text-xs" style="color:var(--lx-text-muted)">Verified Buyer</p>
          </div>
        </div>
      </div>

      <!-- Review 2 -->
      <div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid var(--lx-border-color)">
        <div class="flex">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
        </div>
        <p style="color:var(--lx-text-color);font-size:0.9375rem;line-height:1.5">
          "Replaced my Manduka after 5 years. Should've done it sooner. The cushion is perfect—my knees don't hurt anymore."
        </p>
        <div class="flex items-center gap-3">
          <img src="mike-avatar.jpg" class="w-10 h-10 rounded-full" alt="Mike T." />
          <div>
            <p class="font-semibold text-sm" style="color:var(--lx-text-color)">Mike T.</p>
            <p class="text-xs" style="color:var(--lx-text-muted)">Verified Buyer</p>
          </div>
        </div>
      </div>

      <!-- Review 3 -->
      <div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid var(--lx-border-color)">
        <div class="flex">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
        </div>
        <p style="color:var(--lx-text-color);font-size:0.9375rem;line-height:1.5">
          "okay so i was super skeptical but this mat is actually insane. doesn't slip AT ALL even when i'm drenched. worth every penny"
        </p>
        <div class="flex items-center gap-3">
          <img src="emma-avatar.jpg" class="w-10 h-10 rounded-full" alt="Emma L." />
          <div>
            <p class="font-semibold text-sm" style="color:var(--lx-text-color)">Emma L.</p>
            <p class="text-xs" style="color:var(--lx-text-muted)">Verified Buyer</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### 6. Stats & Authority
**Why sixth**: Quantify the transformation.

```html
<section class="py-16 border-y" style="background:var(--lx-bg-surface);border-color:var(--lx-border-color)">
  <div class="max-w-5xl mx-auto px-4">
    <div class="grid md:grid-cols-3 gap-8 text-center">
      <div>
        <p class="font-bold" style="font-size:clamp(2.5rem,6vw,4rem);color:var(--lx-accent-color)">47K+</p>
        <p class="text-lg font-semibold" style="color:var(--lx-text-color)">Happy Customers</p>
      </div>
      <div>
        <p class="font-bold" style="font-size:clamp(2.5rem,6vw,4rem);color:var(--lx-accent-color)">4.9/5</p>
        <p class="text-lg font-semibold" style="color:var(--lx-text-color)">Average Rating</p>
      </div>
      <div>
        <p class="font-bold" style="font-size:clamp(2.5rem,6vw,4rem);color:var(--lx-accent-color)">99%</p>
        <p class="text-lg font-semibold" style="color:var(--lx-text-color)">Recommend to Friends</p>
      </div>
    </div>
  </div>
</section>
```

### 7. FAQ (Objection Handling)
**Why seventh**: Address the 5 questions stopping them.

```html
<section style="padding:clamp(3rem,10vw,6rem) 0;background:var(--lx-bg-color)">
  <div class="max-w-3xl mx-auto px-4">
    <h2 class="text-center font-bold mb-12" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      Questions?
    </h2>

    <div data-island="FAQ" data-props='{
      "items": [
        {
          "question": "What's your return policy?",
          "answer": "60-day money-back guarantee. If you don't love it, return it for a full refund—no questions asked."
        },
        {
          "question": "How long does shipping take?",
          "answer": "All orders ship within 24 hours. Free 2-3 day shipping in the US."
        },
        {
          "question": "Is this really better than Manduka/Liforme?",
          "answer": "The GripFlow™ surface is proprietary. It's physics-tested to grip better as you sweat—other mats get slippery."
        },
        {
          "question": "What if I don't like it?",
          "answer": "Full refund within 60 days. We'll even cover return shipping."
        },
        {
          "question": "Do you have different colors/sizes?",
          "answer": "Yes! Available in 5 colors and 2 sizes (standard + XL). All colors have the same GripFlow™ surface."
        }
      ],
      "style": "minimal"
    }'></div>
  </div>
</section>
```

### 8. Final CTA (Last Chance)
**Why eighth**: They scrolled this far—remove all friction.

```html
<section style="padding:clamp(3rem,8vw,5rem) 0;background:var(--lx-bg-surface)">
  <div class="max-w-2xl mx-auto px-4 text-center space-y-6">
    <h2 class="font-bold" 
      style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,2.5rem)">
      Your last slippery yoga mat
    </h2>
    <p class="text-lg" style="color:var(--lx-text-muted)">
      Join 47,000+ yogis who upgraded to GripFlow™
    </p>
    <button class="w-full sm:w-auto px-10 py-4 rounded-lg font-semibold text-lg" 
      style="background:var(--lx-accent-color);color:white">
      Get my mat now
    </button>
    <div class="flex justify-center items-center gap-4 text-sm" style="color:var(--lx-text-muted)">
      <span class="flex items-center gap-1">
        <svg class="w-4 h-4"><!-- shield --></svg>
        60-day guarantee
      </span>
      <span>•</span>
      <span class="flex items-center gap-1">
        <svg class="w-4 h-4"><!-- truck --></svg>
        Free shipping
      </span>
    </div>
  </div>
</section>
```

---

## Hero Patterns for Meta Traffic

### Pattern 1: Social Proof Hero
**Best for**: High-review-count products

```html
<section class="relative min-h-[85vh] flex items-center px-4" style="background:white">
  <div class="max-w-2xl mx-auto text-center space-y-6">
    <!-- Eyebrow -->
    <p class="text-sm font-semibold uppercase tracking-wide" style="color:var(--lx-accent-color)">
      Rated #1 Yoga Mat of 2025
    </p>

    <!-- Trust stars (prominent) -->
    <div class="flex justify-center items-center gap-2">
      <div class="flex">
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
        <svg class="w-6 h-6" style="fill:gold"><!-- star --></svg>
      </div>
      <span class="text-lg font-bold" style="color:var(--lx-text-color)">4.9/5 stars (12,847 reviews)</span>
    </div>

    <!-- Headline -->
    <h1 class="font-extrabold leading-[1.1]" 
      style="font-family:var(--lx-font-heading);font-size:clamp(2.25rem,7vw,4rem);letter-spacing:-0.03em">
      The mat that finally grips
    </h1>

    <!-- Subline -->
    <p style="font-size:clamp(1.125rem,3vw,1.5rem);color:#4B5563">
      Join 47,000+ yogis who solved their slipping problem
    </p>

    <!-- CTAs -->
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="px-8 py-4 rounded-lg font-semibold" 
        style="background:var(--lx-accent-color);color:white">
        Get yours now
      </button>
      <button class="px-8 py-4 rounded-lg font-semibold border" 
        style="border-color:var(--lx-border-color);color:var(--lx-text-color)">
        Watch 60-sec review
      </button>
    </div>

    <!-- Product image -->
    <img src="product-in-use.jpg" alt="GripFlow Mat" class="w-full max-w-lg mx-auto rounded-lg" />

    <!-- Trust badges -->
    <div class="flex flex-wrap justify-center gap-6 text-sm pt-4">
      <span class="flex items-center gap-2">
        <svg class="w-5 h-5" style="color:var(--lx-accent-color)"><!-- users --></svg>
        <span>47,000+ customers</span>
      </span>
      <span class="flex items-center gap-2">
        <svg class="w-5 h-5" style="color:var(--lx-accent-color)"><!-- shield --></svg>
        <span>60-day money-back guarantee</span>
      </span>
    </div>
  </div>
</section>
```

### Pattern 2: Video Hero
**Best for**: Demo-heavy products

```html
<section class="relative min-h-[90vh] flex items-center" style="background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto px-4 space-y-6">
    <!-- Video -->
    <div data-island="VideoPlayer" data-props='{
      "video_url": "grip-test-demo.mp4",
      "autoplay": true,
      "loop": true,
      "muted": true,
      "controls": true,
      "aspect_ratio": "16:9"
    }'></div>

    <!-- Content below video -->
    <div class="text-center space-y-4">
      <h1 class="font-bold leading-[1.1]" 
        style="font-family:var(--lx-font-heading);font-size:clamp(2rem,5vw,3.5rem)">
        Watch it grip in real-time
      </h1>
      <p class="text-lg" style="color:var(--lx-text-muted)">
        The surface that gets better as you sweat
      </p>
      <button class="px-8 py-4 rounded-lg font-semibold" 
        style="background:var(--lx-accent-color);color:white">
        Get my GripFlow mat
      </button>
      <div class="flex justify-center gap-4 text-sm pt-2">
        <span class="flex items-center gap-1">
          <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
          <span>4.9/5 stars</span>
        </span>
        <span>•</span>
        <span class="flex items-center gap-1">
          <svg class="w-4 h-4"><!-- truck --></svg>
          <span>Free 2-day shipping</span>
        </span>
      </div>
    </div>
  </div>
</section>
```

### Pattern 3: UGC-Style Hero
**Best for**: Facebook, high authenticity

```html
<section class="relative min-h-[80vh] flex items-center px-4" style="background:#FAFAFA">
  <div class="max-w-5xl mx-auto">
    <div class="grid md:grid-cols-2 gap-8 items-center">
      <!-- Real customer photo -->
      <img src="customer-selfie-with-mat.jpg" alt="Customer photo" 
        class="w-full rounded-lg shadow-lg" />

      <!-- Content -->
      <div class="space-y-5">
        <h1 class="font-semibold leading-[1.15]" 
          style="font-family:var(--lx-font-body);font-size:clamp(1.75rem,5vw,3rem)">
          "This mat changed my practice"
        </h1>
        <p class="text-lg" style="color:var(--lx-text-muted)">
          — Sarah M., verified customer (+ 46,999 others)
        </p>
        <button class="w-full md:w-auto px-8 py-4 rounded-lg font-semibold" 
          style="background:var(--lx-accent-color);color:white">
          Try it risk-free
        </button>
        <div class="flex flex-wrap gap-4 text-sm pt-2">
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" style="color:var(--lx-accent-color)"><!-- shield --></svg>
            <span>60-day guarantee</span>
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
            <span>4.9/5 from 12,847 reviews</span>
          </span>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Pattern 4: Countdown Urgency Hero
**Best for**: Sales/launches

```html
<section class="relative min-h-[85vh] flex items-center px-4" 
  style="background:linear-gradient(to bottom, #FEF3C7 0%, #FFFFFF 100%)">
  <div class="max-w-2xl mx-auto text-center space-y-6">
    <!-- Eyebrow -->
    <p class="text-sm font-bold uppercase tracking-wide" style="color:#B45309">
      Limited Time: Launch Sale
    </p>

    <!-- Headline -->
    <h1 class="font-extrabold leading-[1.1]" 
      style="font-family:var(--lx-font-heading);font-size:clamp(2.25rem,6vw,4rem)">
      40% off ends tonight
    </h1>

    <!-- Subline -->
    <p class="text-xl" style="color:var(--lx-text-muted)">
      The GripFlow mat at its lowest price ever
    </p>

    <!-- Countdown -->
    <div data-island="CountdownTimer" data-props='{
      "end_time": "2026-12-31T23:59:59Z",
      "headline": "Sale ends in:",
      "style": "minimal",
      "size": "large"
    }'></div>

    <!-- CTA -->
    <button class="px-10 py-4 rounded-lg font-semibold text-lg" 
      style="background:var(--lx-accent-color);color:white">
      Claim my 40% off
    </button>

    <!-- Product image -->
    <img src="product-hero.jpg" alt="GripFlow Mat" class="w-full max-w-md mx-auto rounded-lg" />
  </div>
</section>
```

---

## Trust Stacking (Critical for Cold Traffic)

Meta traffic has **ZERO brand familiarity**. Trust must be immediate, overwhelming, and specific.

### The Trust Stack (All 3 Layers)

#### Layer 1: Hero Trust Bar
```html
<div class="flex flex-wrap justify-center gap-4 text-sm">
  <span class="flex items-center gap-2 font-semibold">
    <div class="flex">
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
      <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    </div>
    <span>4.9/5 (12,847 reviews)</span>
  </span>
  <span class="flex items-center gap-2 font-semibold">
    <svg class="w-4 h-4" style="color:var(--lx-accent-color)"><!-- shield --></svg>
    <span>60-Day Guarantee</span>
  </span>
</div>
```

#### Layer 2: Persistent Trust Badge Bar
```html
<div data-island="TrustBadgeBar" data-props='{
  "position": "top_sticky",
  "badges": [
    {"icon": "star", "text": "4.9/5 (12,847)", "color": "gold"},
    {"icon": "shield_check", "text": "60-Day Guarantee", "color": "blue"},
    {"icon": "truck", "text": "Free Shipping", "color": "green"},
    {"icon": "award", "text": "Yoga Journal Pick", "color": "purple"}
  ],
  "layout": "scroll",
  "background": "white"
}'></div>
```

#### Layer 3: Social Proof Popup
```html
<div data-island="SocialProofPopup" data-props='{
  "position": "bottom_left",
  "events": [
    {"type": "purchase", "name": "Sarah from NYC", "product": "GripFlow Mat", "time": "2 min ago"},
    {"type": "review", "name": "Mike from LA", "rating": 5, "time": "5 min ago"},
    {"type": "purchase", "name": "Emma from Austin", "product": "GripFlow Mat", "time": "8 min ago"}
  ],
  "interval": 8000,
  "show_delay": 3000,
  "style": "minimal"
}'></div>
```

### Trust Signal Hierarchy

**Tier 1 (Hero)**: Star rating + review count, customer count, guarantee  
**Tier 2 (Trust Strip)**: Free shipping, press mentions, security badges  
**Tier 3 (Section 5)**: Detailed testimonials with photos, before/after, expert endorsements

---

## Social Proof (UGC > Polished)

Meta traffic trusts **authentic > polished**.

### UGC-Style Reviews (Facebook)
```html
<div class="p-6 rounded-lg space-y-3" style="background:white;border:1px solid #E5E7EB">
  <!-- Stars -->
  <div class="flex">
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
    <svg class="w-4 h-4" style="fill:gold"><!-- star --></svg>
  </div>

  <!-- Review text (casual tone) -->
  <p style="color:#1F2937;font-size:0.9375rem;line-height:1.5">
    okay so i was super skeptical but this mat is actually insane. doesn't slip AT ALL even when i'm drenched. worth every penny
  </p>

  <!-- Author -->
  <div class="flex items-center gap-3">
    <img src="customer-selfie.jpg" class="w-10 h-10 rounded-full" alt="Sarah M." />
    <div>
      <p class="font-semibold text-sm">Sarah M.</p>
      <p class="text-xs" style="color:#6B7280">Verified Buyer • New York, NY</p>
    </div>
  </div>

  <!-- Optional: customer photo with product -->
  <img src="review-photo-in-use.jpg" class="w-full rounded-lg mt-3" alt="Customer photo" />
</div>
```

### Specific Numbers > Vague Claims

❌ "Thousands of happy customers"  
✅ "47,482 customers (and counting)"

❌ "Highly rated"  
✅ "4.9/5 stars from 12,847 verified reviews"

❌ "Fast shipping"  
✅ "Ships in 24 hours • Arrives in 2-3 days"

---

## CTA Strategy (Single Goal, Repeat 3x)

### The Rule: One Conversion Goal
All CTAs point to the same action.

**Single product**: "Get my GripFlow mat"  
**Multi-product**: "Shop yoga mats"  
**Lead gen**: "Get my free guide"

### Benefit-Driven CTA Copy

❌ Generic: "Shop now" / "Buy now"  
✅ Benefit-driven:
- "Get my GripFlow mat"
- "Solve my slipping problem"
- "Try it risk-free"
- "Claim my 40% off"

### CTA Placement (3x Rule)

**CTA #1: Hero**
```html
<button class="px-8 py-4 rounded-lg font-semibold" 
  style="background:var(--lx-accent-color);color:white">
  Get my GripFlow mat
</button>
```

**CTA #2: After Social Proof**
```html
<div class="text-center space-y-4">
  <h3 class="font-bold text-2xl">Ready to upgrade?</h3>
  <button class="px-8 py-4 rounded-lg font-semibold" 
    style="background:var(--lx-accent-color);color:white">
    Get yours now
  </button>
  <p class="text-sm" style="color:var(--lx-text-muted)">60-day guarantee • Free shipping</p>
</div>
```

**CTA #3: Sticky Bar**
```html
<div data-island="StickyBar" data-props='{
  "position": "bottom",
  "trigger_scroll": "50vh",
  "cta_text": "Get my GripFlow mat",
  "price": "$79",
  "trust_badge": "Free shipping • 60-day guarantee"
}'></div>
```

### Mobile CTA Sizing
```html
<button class="w-full sm:w-auto px-8 rounded-lg font-semibold" 
  style="padding-top:0.875rem;padding-bottom:0.875rem;min-height:44px;background:var(--lx-accent-color);color:white;font-size:1rem">
  Get yours now
</button>
```

---

## Urgency for Meta Traffic (Use Sparingly)

### When to Use Urgency
✅ Real sale with deadline  
✅ Limited inventory (< 50 units)  
✅ Launch window  
✅ Seasonal cutoff

❌ Fake scarcity  
❌ Persistent urgency

### CountdownTimer
```html
<div data-island="CountdownTimer" data-props='{
  "end_time": "2026-12-31T23:59:59Z",
  "headline": "Sale ends in:",
  "style": "minimal",
  "show_labels": true,
  "size": "large"
}'></div>
```

### Inventory Indicator
```html
<div data-island="InventoryIndicator" data-props='{
  "threshold": 50,
  "text": "Only {count} left in stock",
  "style": "warning"
}'></div>
```

---

## Mobile Patterns

### Container Padding
```html
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <!-- Content -->
</div>
```

### Responsive Grid
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- Grid items -->
</div>
```

### Full-Width CTA on Mobile
```html
<button class="w-full sm:w-auto px-8 py-4 rounded-lg font-semibold" 
  style="background:var(--lx-accent-color);color:white">
  Get yours now
</button>
```

### Stack on Mobile
```html
<div class="flex flex-col sm:flex-row gap-4">
  <button>Primary CTA</button>
  <button>Secondary CTA</button>
</div>
```

---

## Anti-Patterns (Meta Killers)

### ❌ Message Mismatch
**What**: Ad says "40% off" → page doesn't mention sale  
**Fix**: Ad headline = page headline

### ❌ Desktop-First Design
**What**: 85% mobile traffic hits tiny text, cramped spacing  
**Fix**: `clamp()` for all text, test on real iPhone

### ❌ No Social Proof Above Fold
**What**: Hero has zero trust signals  
**Fix**: Trust bar in hero. "4.9/5 from 12,847 reviews" immediately visible

### ❌ Multiple Competing CTAs
**What**: "Shop now" | "Learn more" | "Watch video" | "Compare"  
**Fix**: One goal. All CTAs → same action

### ❌ Slow-Loading Hero
**What**: 5MB image, 3+ second load  
**Fix**: < 200KB for hero. WebP format. Lazy-load below fold

### ❌ Asking for Email Too Early
**What**: EmailCapture popup 2 seconds after landing  
**Fix**: After social proof section, or exit-intent only

### ❌ Generic Stock Photos
**What**: Diverse-group-laughing-at-salad imagery  
**Fix**: Real product photos. Real customer photos. UGC > stock

### ❌ Burying the Price
**What**: No price until checkout  
**Fix**: Show price in hero or BuyBox. Transparency = trust

### ❌ No Mobile Sticky CTA
**What**: CTA only in hero. After scroll, no path to convert  
**Fix**: StickyBar after 50vh

### ❌ Over-Designing for Aesthetics
**What**: Parallax, auto-play videos, carousels  
**Fix**: Minimal animations. Fast > fancy

### ❌ No Guarantee
**What**: "Buy now" with no mention of returns  
**Fix**: "60-day money-back guarantee" everywhere

### ❌ Feature Dumping
**What**: "6mm TPE, dual-layer, eco-certified"  
**Fix**: "6mm cushion = your knees won't hurt." Translate features → benefits

---

## Complete VibePage Blueprint: Product Launch (New Product)

```json
{
  "head": {
    "title": "GripFlow™ Yoga Mat — The Mat That Won't Slip",
    "description": "Join 47,000+ yogis who solved their slipping problem. 60-day guarantee.",
    "fonts": [
      "https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap"
    ]
  },
  "theme_css": ":root { --lx-accent-color: #4F46E5; --lx-text-color: #111827; --lx-text-muted: #6B7280; --lx-bg-color: #FFFFFF; --lx-bg-surface: #F9FAFB; --lx-border-color: #E5E7EB; --lx-font-heading: 'Inter', system-ui, sans-serif; --lx-font-body: 'Inter', system-ui, sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[85vh] flex items-center px-4\" style=\"background:white\"><div class=\"max-w-2xl mx-auto text-center space-y-6\"><p class=\"text-sm font-semibold uppercase tracking-wide\" style=\"color:var(--lx-accent-color)\">Rated #1 Yoga Mat of 2025</p><div class=\"flex justify-center items-center gap-2\"><div class=\"flex\"><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg></div><span class=\"text-lg font-bold\" style=\"color:var(--lx-text-color)\">4.9/5 stars (12,847 reviews)</span></div><h1 class=\"font-extrabold leading-[1.1]\" style=\"font-family:var(--lx-font-heading);font-size:clamp(2.25rem,7vw,4rem);letter-spacing:-0.03em\">The mat that finally grips</h1><p style=\"font-size:clamp(1.125rem,3vw,1.5rem);color:#4B5563\">Join 47,000+ yogis who solved their slipping problem</p><div class=\"flex flex-col sm:flex-row gap-4 justify-center\"><button class=\"px-8 py-4 rounded-lg font-semibold\" style=\"background:var(--lx-accent-color);color:white\">Get yours now</button></div><img src=\"{{product_image_url}}\" alt=\"GripFlow Mat\" class=\"w-full max-w-lg mx-auto rounded-lg\"/><div class=\"flex flex-wrap justify-center gap-6 text-sm pt-4\"><span class=\"flex items-center gap-2\"><svg class=\"w-5 h-5\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z\"/></svg><span>47,000+ customers</span></span><span class=\"flex items-center gap-2\"><svg class=\"w-5 h-5\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z\"/></svg><span>60-day money-back guarantee</span></span></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "trust-strip",
      "html": "<section class=\"py-8 border-b\" style=\"background:var(--lx-bg-surface);border-color:var(--lx-border-color)\"><div class=\"max-w-7xl mx-auto px-4\"><div class=\"grid grid-cols-2 md:grid-cols-4 gap-6 text-center\"><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">60-Day Guarantee</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Love it or return it</p></div><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path d=\"M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z\"/><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">Free Shipping</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">On all US orders</p></div><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"gold\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">12,847 5-Star Reviews</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Rated Excellent</p></div><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">Featured in Yoga Journal</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Best Mat 2025</p></div></div></div></section>",
      "css": "",
      "js": ""
    }
  ],
  "islands": [
    {
      "type": "StickyBar",
      "props": {
        "trigger_scroll": "50vh",
        "cta_text": "Get my GripFlow mat",
        "price": "$79",
        "trust_badge": "60-day guarantee • Free shipping"
      }
    }
  ]
}
```

---

## TL;DR — The Meta Landing Page Checklist

✅ **Message match**: Ad headline → page headline  
✅ **Mobile-first**: `clamp()` for text/spacing, 44px tap targets  
✅ **Trust immediately**: Star rating + review count in hero  
✅ **Single CTA goal**: All buttons → same action  
✅ **CTA 3x minimum**: Hero, post-social-proof, sticky bar  
✅ **UGC > polished** (Facebook) OR **editorial > UGC** (Instagram)  
✅ **Social proof section**: 6-8 reviews with photos  
✅ **Urgency (if applicable)**: Real countdown, real inventory  
✅ **FAQ section**: Top 5 objections  
✅ **Load speed**: < 3 seconds on mobile  
✅ **Visual continuity**: Ad colors → page colors

**If any are missing, the page will underperform.** Meta traffic is unforgiving.
