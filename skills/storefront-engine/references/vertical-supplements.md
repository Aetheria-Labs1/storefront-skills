# Supplements & Performance DTC — Storefront Design Intelligence

> **When to load:** Product vertical is supplements, vitamins, protein, nootropics, fitness nutrition, biohacking, wellness, performance enhancers, adaptogens, pre-workout, recovery formulas.

## Philosophy

Supplements occupy a unique trust chasm: buyers are both skeptical (burned by false claims) AND impulsive (desperate for results). The page must be simultaneously **clinical authority** and **modern performance brand**.

**Key tensions:**
- Science-backed credibility vs. accessible storytelling
- Clinical proof vs. urgency/scarcity
- Educational depth vs. fast conversion
- Premium positioning vs. value stacking

**Design mandate:** Dark mode default (performance/tech signaling), bold typography, electric accents, modular proof architecture. NOT pharmaceutical-boring, NOT bro-science clickbait.

---

## Section Sequences

### Single Product (12-14 sections)
1. **Hero** — bold benefit + trust anchor (rating, sold count)
2. **Trust Bar** — certifications, 3rd-party tested, made-in badges
3. **Problem/Solution** — visceral problem state → product as solution
4. **Key Benefits** — 3-4 benefits with icons, clinical language
5. **Ingredient Spotlight** — Tabs island for each active ingredient
6. **Clinical Proof** — stats grid + research references
7. **How It Works** — timeline or process flow
8. **Pricing/Offer** — QuantityBreaks island + SubscriptionToggle
9. **Comparison Table** — CompareTable island vs. competitors
10. **Social Proof** — ReviewCarousel island + SocialProofPopup
11. **FAQ** — FAQ island (dosing, safety, interactions)
12. **Stack Recommendation** — ProductCarousel island for bundles
13. **Guarantee** — risk reversal (60-day refund, money-back)
14. **Final CTA** — StickyBar island with countdown

### Stack/Bundle (10-12 sections)
1. Hero (stack benefit)
2. Trust Bar
3. Stack Breakdown (each product card)
4. Combined Benefits (synergy story)
5. Clinical Proof
6. Pricing (bundle discount)
7. Comparison (stack vs. buying separately)
8. Social Proof
9. FAQ
10. Guarantee
11. Final CTA

### Subscription (8-10 sections)
1. Hero (recurring benefit)
2. Trust Bar
3. Subscription Value Prop (save %, auto-refill, cancel anytime)
4. Key Benefits
5. Clinical Proof
6. Pricing (SubscriptionToggle)
7. Social Proof
8. FAQ
9. Guarantee
10. Final CTA

### Comparison (8-10 sections)
For pages comparing multiple products or your product vs. competitors.
1. Hero (category overview)
2. Trust Bar
3. Comparison Table (CompareTable island)
4. Winner Spotlight (your product)
5. Clinical Proof (why yours wins)
6. Pricing
7. Social Proof
8. FAQ
9. Final CTA

---

## Island Combinations

### CompareTable + QuantityBreaks + CountdownTimer

```html
<section class="py-12 px-4" style="background:#0a0a0a">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-center font-bold text-white mb-8" style="font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)">See How We Compare</h2>
    <div data-island="CompareTable" data-props='{"columns":["Our Formula","Competitor A","Competitor B"],"rows":[{"label":"Active Ingredients","ours":"5000mg L-Citrulline, 3000mg Beta-Alanine","a":"2000mg L-Citrulline, 1500mg Beta-Alanine","b":"3000mg L-Citrulline, 2000mg Beta-Alanine"},{"label":"3rd Party Tested","ours":"✓ NSF Certified","a":"✗ Not Tested","b":"✓ Informed Sport"},{"label":"Price per Serving","ours":"$1.20","a":"$1.80","b":"$1.50"},{"label":"Money-Back Guarantee","ours":"60 Days","a":"30 Days","b":"No Guarantee"}]}'></div>
  </div>
</section>

<section class="py-12 px-4" style="background:#0f0f0f">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-center font-bold text-white mb-2" style="font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)">Choose Your Supply</h2>
    <p class="text-center text-gray-400 mb-8">Save more when you stock up</p>
    <div data-island="QuantityBreaks" data-props='{"options":[{"quantity":1,"label":"1 Month Supply","price":59.99,"unit_price":"$1.99/serving","badge":""},{"quantity":3,"label":"3 Month Supply","price":149.97,"unit_price":"$1.66/serving","badge":"Save 16%","recommended":true},{"quantity":6,"label":"6 Month Supply","price":269.94,"unit_price":"$1.49/serving","badge":"Save 25%"}]}'></div>
  </div>
</section>

<section class="py-12 px-4" style="background:#0a0a0a">
  <div class="max-w-2xl mx-auto text-center">
    <div data-island="CountdownTimer" data-props='{"end_date":"2026-06-30T23:59:59Z","headline":"Limited Time: 20% Off Ends In","urgency_text":"This offer expires soon"}'></div>
  </div>
</section>
```

### SubscriptionToggle + TrustBadgeBar + StickyBar

```html
<section class="py-12 px-4" style="background:#0f0f0f">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-center font-bold text-white mb-8" style="font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)">Never Run Out — Subscribe & Save</h2>
    <div data-island="SubscriptionToggle" data-props='{"one_time_price":59.99,"subscription_price":47.99,"subscription_discount":"20%","subscription_benefits":["Cancel anytime","Free shipping","Priority support","Early access to new products"]}'></div>
  </div>
</section>

<section class="py-8 px-4" style="background:#0a0a0a;border-top:1px solid rgba(255,255,255,0.1)">
  <div data-island="TrustBadgeBar" data-props='{"badges":["3rd Party Tested","NSF Certified for Sport","Made in USA","GMP Certified","Non-GMO","Gluten Free"]}'></div>
</section>

<div data-island="StickyBar" data-props='{"cta_text":"Add to Cart","price":"$47.99","show_at_scroll":800,"variant":"dark"}'></div>
```

### Tabs (Ingredients) + ReviewCarousel + SocialProofPopup

```html
<section class="py-12 px-4" style="background:#0a0a0a">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-center font-bold text-white mb-8" style="font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)">Clinically Dosed Ingredients</h2>
    <div data-island="Tabs" data-props='{"tabs":[{"label":"L-Citrulline (5000mg)","content":"<p class=\"text-white mb-4\">Increases nitric oxide production for improved blood flow and muscle pumps.</p><p class=\"text-gray-400 text-sm\">Clinically effective dose: 3000-6000mg. Our formula delivers 5000mg per serving.</p>"},{"label":"Beta-Alanine (3000mg)","content":"<p class=\"text-white mb-4\">Buffers lactic acid to delay muscle fatigue and extend endurance.</p><p class=\"text-gray-400 text-sm\">Clinically effective dose: 2000-5000mg. Our formula delivers 3000mg per serving.</p>"},{"label":"Caffeine (200mg)","content":"<p class=\"text-white mb-4\">Enhances focus, energy, and exercise performance.</p><p class=\"text-gray-400 text-sm\">Clinically effective dose: 100-400mg. Our formula delivers 200mg per serving (equivalent to 2 cups of coffee).</p>"}],"variant":"dark"}'></div>
  </div>
</section>

<section class="py-12 px-4" style="background:#0f0f0f">
  <div class="max-w-5xl mx-auto">
    <h2 class="text-center font-bold text-white mb-8" style="font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)">What Athletes Are Saying</h2>
    <div data-island="ReviewCarousel" data-props='{"reviews":[{"author":"Mike T.","rating":5,"text":"Best pre-workout I've tried. Clean energy, no crash, insane pumps.","verified":true},{"author":"Sarah K.","rating":5,"text":"Finally a pre-workout that doesn't make me jittery. Love the focus.","verified":true},{"author":"James R.","rating":5,"text":"Increased my reps by 20% in the first week. This stuff works.","verified":true}],"auto_play":true}'></div>
  </div>
</section>

<div data-island="SocialProofPopup" data-props='{"notifications":[{"text":"Someone in New York just purchased Performance Pre-Workout","time":"2 minutes ago"},{"text":"Someone in California just purchased Performance Pre-Workout","time":"5 minutes ago"}],"delay":3000}'></div>
```

---

## Typography & Color

### Dark Mode Default
```css
:root {
  --lx-bg-color: #0a0a0a;
  --lx-bg-surface: #0f0f0f;
  --lx-text-color: #ffffff;
  --lx-text-muted: #9ca3af;
  --lx-accent-color: #84cc16; /* electric lime */
  --lx-accent-secondary: #3b82f6; /* blue */
  --lx-border-color: rgba(255,255,255,0.1);
  --lx-font-heading: 'Inter', -apple-system, sans-serif;
  --lx-font-body: 'Inter', -apple-system, sans-serif;
}
```

### Typography Rules
- **Headings:** 700-800 weight, tight tracking (-0.02em), clamp sizing
- **Body:** 400-500 weight, 1.6 line-height, 16-18px base
- **Clinical Text:** 14px, gray-400, uppercase labels for credibility
- **CTA Buttons:** 600 weight, 16px, electric accent colors

### Color Strategy
- **Background:** #0a0a0a (primary), #0f0f0f (surface)
- **Accent:** #84cc16 (lime, energy), #3b82f6 (blue, trust)
- **Text:** #ffffff (primary), #9ca3af (muted)
- **Borders:** rgba(255,255,255,0.1)

---

## Hero Patterns

### Bold Centered Dark Hero

```html
<section class="relative py-20 px-4 flex items-center justify-center min-h-[80vh]" style="background:linear-gradient(135deg,#0a0a0a 0%,#1a1a1a 100%)">
  <div class="max-w-4xl mx-auto text-center">
    <h1 class="font-bold text-white mb-4" style="font-size:clamp(2rem,5vw,4rem);line-height:1.1;letter-spacing:-0.02em;font-family:var(--lx-font-heading)">
      Peak Performance.<br>Clinical Dosing.
    </h1>
    <p class="text-xl text-gray-300 mb-6 max-w-2xl mx-auto">
      Amplify strength, endurance, and focus with 5000mg L-Citrulline, 3000mg Beta-Alanine, and 200mg caffeine.
    </p>
    <div class="flex items-center justify-center gap-4 mb-8">
      <div class="flex items-center gap-1">
        <span class="text-yellow-400">★★★★★</span>
        <span class="text-white font-semibold">4.9/5</span>
        <span class="text-gray-400">(2,847 reviews)</span>
      </div>
      <span class="text-gray-400">|</span>
      <span class="text-gray-300">18,492 sold this month</span>
    </div>
    <button class="px-8 py-4 rounded-lg font-semibold text-lg text-black hover:opacity-90 transition" style="background:var(--lx-accent-color)">
      Shop Now — $47.99
    </button>
  </div>
</section>
```

### Trust-Bar Hero

```html
<section class="py-16 px-4" style="background:#0a0a0a">
  <div class="max-w-6xl mx-auto">
    <div class="grid md:grid-cols-2 gap-8 items-center">
      <div>
        <h1 class="font-bold text-white mb-4" style="font-size:clamp(2rem,5vw,3.5rem);line-height:1.1;font-family:var(--lx-font-heading)">
          Pre-Workout Trusted by Elite Athletes
        </h1>
        <p class="text-lg text-gray-300 mb-6">
          NSF Certified for Sport. 3rd-party tested for banned substances. Clinically dosed ingredients.
        </p>
        <div data-island="TrustBadgeBar" data-props='{"badges":["NSF Certified","3rd Party Tested","Made in USA","GMP Certified"]}'></div>
        <button class="mt-6 px-8 py-4 rounded-lg font-semibold text-lg text-black hover:opacity-90 transition" style="background:var(--lx-accent-color)">
          Get Started
        </button>
      </div>
      <div class="relative">
        <img src="https://placeholder.co/600x700/0f0f0f/84cc16?text=Product+Image" alt="Product" class="w-full h-auto rounded-lg" />
      </div>
    </div>
  </div>
</section>
```

### Countdown Hero

```html
<section class="py-16 px-4" style="background:linear-gradient(135deg,#0a0a0a 0%,#1a1a1a 100%)">
  <div class="max-w-4xl mx-auto text-center">
    <div data-island="CountdownTimer" data-props='{"end_date":"2026-06-30T23:59:59Z","headline":"Limited Time: 25% Off","urgency_text":"Offer ends soon"}'></div>
    <h1 class="font-bold text-white mb-4 mt-6" style="font-size:clamp(2rem,5vw,3.5rem);line-height:1.1;font-family:var(--lx-font-heading)">
      Stock Up & Save on Performance Pre-Workout
    </h1>
    <p class="text-lg text-gray-300 mb-6">
      Get 25% off 3-month and 6-month supplies. Free shipping on all orders.
    </p>
    <button class="px-8 py-4 rounded-lg font-semibold text-lg text-black hover:opacity-90 transition" style="background:var(--lx-accent-color)">
      Shop the Sale
    </button>
  </div>
</section>
```

---

## Clinical Proof Section

```html
<section class="py-12 px-4" style="background:#0f0f0f">
  <div class="max-w-5xl mx-auto">
    <h2 class="text-center font-bold text-white mb-12" style="font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)">Backed by Science</h2>
    <div class="grid md:grid-cols-3 gap-8 mb-12">
      <div class="text-center">
        <div class="text-5xl font-bold mb-2" style="color:var(--lx-accent-color)">23%</div>
        <p class="text-white font-semibold mb-2">Increase in Strength</p>
        <p class="text-sm text-gray-400">After 8 weeks (Journal of Strength Research, 2024)</p>
      </div>
      <div class="text-center">
        <div class="text-5xl font-bold mb-2" style="color:var(--lx-accent-color)">18%</div>
        <p class="text-white font-semibold mb-2">Longer Endurance</p>
        <p class="text-sm text-gray-400">Before fatigue onset (Sports Medicine Study, 2025)</p>
      </div>
      <div class="text-center">
        <div class="text-5xl font-bold mb-2" style="color:var(--lx-accent-color)">94%</div>
        <p class="text-white font-semibold mb-2">Users Report Better Focus</p>
        <p class="text-sm text-gray-400">In our customer survey (n=1,847)</p>
      </div>
    </div>
    <div data-island="Tabs" data-props='{"tabs":[{"label":"Study 1: Strength Gains","content":"<p class=\"text-white mb-2\"><strong>Title:</strong> Effects of L-Citrulline Supplementation on Resistance Training Adaptations</p><p class=\"text-gray-400 text-sm mb-2\"><strong>Published:</strong> Journal of Strength Research, 2024</p><p class=\"text-gray-300\"><strong>Findings:</strong> Participants supplementing with 5000mg L-Citrulline daily showed a 23% greater increase in 1RM bench press compared to placebo after 8 weeks.</p>"},{"label":"Study 2: Endurance Extension","content":"<p class=\"text-white mb-2\"><strong>Title:</strong> Beta-Alanine and Exercise Performance: A Meta-Analysis</p><p class=\"text-gray-400 text-sm mb-2\"><strong>Published:</strong> Sports Medicine, 2025</p><p class=\"text-gray-300\"><strong>Findings:</strong> Meta-analysis of 27 studies showed beta-alanine supplementation (2.4-6.4g daily) increased time to exhaustion by 18% in high-intensity exercise.</p>"},{"label":"Study 3: Cognitive Enhancement","content":"<p class=\"text-white mb-2\"><strong>Title:</strong> Caffeine and Cognitive Performance During Exercise</p><p class=\"text-gray-400 text-sm mb-2\"><strong>Published:</strong> Nutrition Reviews, 2024</p><p class=\"text-gray-300\"><strong>Findings:</strong> 200mg caffeine improved reaction time, focus, and decision-making during prolonged exercise by 12-15% compared to placebo.</p>"}],"variant":"dark"}'></div>
  </div>
</section>
```

---

## Pricing Section

```html
<section class="py-12 px-4" style="background:#0a0a0a">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-center font-bold text-white mb-2" style="font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)">Choose Your Supply</h2>
    <p class="text-center text-gray-400 mb-8">Best value when you stock up</p>
    <div data-island="QuantityBreaks" data-props='{"options":[{"quantity":1,"label":"1 Month Supply (30 servings)","price":59.99,"unit_price":"$1.99/serving","badge":""},{"quantity":3,"label":"3 Month Supply (90 servings)","price":149.97,"unit_price":"$1.66/serving","badge":"Save 16%","recommended":true},{"quantity":6,"label":"6 Month Supply (180 servings)","price":269.94,"unit_price":"$1.49/serving","badge":"Save 25% — Best Deal"}]}'></div>
    <div class="mt-8">
      <div data-island="SubscriptionToggle" data-props='{"one_time_price":59.99,"subscription_price":47.99,"subscription_discount":"20%","subscription_benefits":["Cancel anytime","Free shipping","Priority support","Early access to new products"]}'></div>
    </div>
  </div>
</section>

<div data-island="StickyBar" data-props='{"cta_text":"Add to Cart","price":"$47.99","show_at_scroll":800,"variant":"dark"}'></div>
```

---

## Comparison Section

```html
<section class="py-12 px-4" style="background:#0f0f0f">
  <div class="max-w-5xl mx-auto">
    <h2 class="text-center font-bold text-white mb-4" style="font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)">How We Stack Up</h2>
    <p class="text-center text-gray-400 mb-8">Most pre-workouts under-dose key ingredients. We don't.</p>
    <div data-island="CompareTable" data-props='{"columns":["Our Formula","Brand A","Brand B","Brand C"],"rows":[{"label":"L-Citrulline (clinical dose: 3000-6000mg)","ours":"5000mg","a":"2000mg","b":"3000mg","c":"1500mg"},{"label":"Beta-Alanine (clinical dose: 2000-5000mg)","ours":"3000mg","a":"1500mg","b":"2000mg","c":"1000mg"},{"label":"Caffeine (clinical dose: 100-400mg)","ours":"200mg","a":"150mg","b":"300mg","c":"200mg"},{"label":"3rd Party Tested","ours":"✓ NSF Certified","a":"✗","b":"✓ Informed Sport","c":"✗"},{"label":"Price per Serving","ours":"$1.66 (with 3-month)","a":"$2.50","b":"$1.99","c":"$1.80"},{"label":"Money-Back Guarantee","ours":"60 Days","a":"30 Days","b":"30 Days","c":"No Guarantee"}]}'></div>
    <div class="text-center mt-8">
      <button class="px-8 py-4 rounded-lg font-semibold text-lg text-black hover:opacity-90 transition" style="background:var(--lx-accent-color)">
        Choose the Winner
      </button>
    </div>
  </div>
</section>
```

---

## Compliance

### FDA Disclaimer

```html
<section class="py-8 px-4" style="background:#0a0a0a;border-top:1px solid rgba(255,255,255,0.1)">
  <div class="max-w-4xl mx-auto">
    <p class="text-xs text-gray-500 text-center leading-relaxed">
      * These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease. Individual results may vary. Consult your healthcare provider before use if you are pregnant, nursing, taking medication, or have a medical condition.
    </p>
  </div>
</section>
```

Place this near the bottom of the page, after all claims and testimonials.

---

## Anti-Patterns

### 12 Supplement Page Killers (and Fixes)

1. **Under-dosed ingredients with no transparency**
   - Fix: Show exact dosages + clinical effective ranges in Tabs island

2. **Generic "proprietary blend" with hidden amounts**
   - Fix: Full transparency. List every ingredient and dose.

3. **No 3rd-party testing badges**
   - Fix: TrustBadgeBar island with NSF/Informed Sport/GMP

4. **Overpromising ("lose 30 lbs in 30 days")**
   - Fix: Realistic claims with clinical backing + FDA disclaimer

5. **No comparison to competitors**
   - Fix: CompareTable island showing ingredient differences

6. **Weak social proof (5 reviews)**
   - Fix: ReviewCarousel island + SocialProofPopup + aggregate rating in hero

7. **Single pricing option (no volume discount)**
   - Fix: QuantityBreaks island with 3-6 tiers

8. **No subscription offer**
   - Fix: SubscriptionToggle island (20%+ discount)

9. **Missing FAQ for common objections**
   - Fix: FAQ island covering dosing, safety, interactions, timing

10. **No urgency or scarcity**
    - Fix: CountdownTimer island + InventoryIndicator island

11. **Weak guarantee (or none)**
    - Fix: 60-day money-back guarantee section

12. **Light mode on a performance product**
    - Fix: Dark mode default (performance/tech signaling)

---

## Complete Blueprint

Full VibePage JSON for flagship supplement page (dark mode, 10+ sections):

```json
{
  "head": {
    "title": "Performance Pre-Workout — Clinically Dosed for Peak Results",
    "description": "Amplify strength, endurance, and focus with 5000mg L-Citrulline, 3000mg Beta-Alanine, and 200mg caffeine. NSF Certified for Sport.",
    "og_image": "https://cdn.lexsis.ai/products/pre-workout-og.jpg"
  },
  "theme_css": ":root { --lx-bg-color: #0a0a0a; --lx-bg-surface: #0f0f0f; --lx-text-color: #ffffff; --lx-text-muted: #9ca3af; --lx-accent-color: #84cc16; --lx-accent-secondary: #3b82f6; --lx-border-color: rgba(255,255,255,0.1); --lx-font-heading: 'Inter', -apple-system, sans-serif; --lx-font-body: 'Inter', -apple-system, sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative py-20 px-4 flex items-center justify-center min-h-[80vh]\" style=\"background:linear-gradient(135deg,#0a0a0a 0%,#1a1a1a 100%)\"><div class=\"max-w-4xl mx-auto text-center\"><h1 class=\"font-bold text-white mb-4\" style=\"font-size:clamp(2rem,5vw,4rem);line-height:1.1;letter-spacing:-0.02em;font-family:var(--lx-font-heading)\">Peak Performance.<br>Clinical Dosing.</h1><p class=\"text-xl text-gray-300 mb-6 max-w-2xl mx-auto\">Amplify strength, endurance, and focus with 5000mg L-Citrulline, 3000mg Beta-Alanine, and 200mg caffeine.</p><div class=\"flex items-center justify-center gap-4 mb-8\"><div class=\"flex items-center gap-1\"><span class=\"text-yellow-400\">★★★★★</span><span class=\"text-white font-semibold\">4.9/5</span><span class=\"text-gray-400\">(2,847 reviews)</span></div><span class=\"text-gray-400\">|</span><span class=\"text-gray-300\">18,492 sold this month</span></div><button class=\"px-8 py-4 rounded-lg font-semibold text-lg text-black hover:opacity-90 transition\" style=\"background:var(--lx-accent-color)\">Shop Now — $47.99</button></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "trust-bar",
      "html": "<section class=\"py-8 px-4\" style=\"background:#0a0a0a;border-top:1px solid rgba(255,255,255,0.1)\"><div data-island=\"TrustBadgeBar\" data-props='{\"badges\":[\"3rd Party Tested\",\"NSF Certified for Sport\",\"Made in USA\",\"GMP Certified\",\"Non-GMO\",\"Gluten Free\"]}'></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "problem-solution",
      "html": "<section class=\"py-12 px-4\" style=\"background:#0f0f0f\"><div class=\"max-w-4xl mx-auto grid md:grid-cols-2 gap-8\"><div><h2 class=\"font-bold text-white mb-4\" style=\"font-size:clamp(1.5rem,3vw,2rem);font-family:var(--lx-font-heading)\">The Problem</h2><p class=\"text-gray-300 leading-relaxed\">Most pre-workouts under-dose key ingredients or hide them in proprietary blends. You're left with jitters, crashes, and mediocre results.</p></div><div><h2 class=\"font-bold mb-4\" style=\"font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-accent-color);font-family:var(--lx-font-heading)\">The Solution</h2><p class=\"text-gray-300 leading-relaxed\">Full clinical doses of proven ingredients. 3rd-party tested. No proprietary blends. No fillers. Just results.</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "key-benefits",
      "html": "<section class=\"py-12 px-4\" style=\"background:#0a0a0a\"><div class=\"max-w-5xl mx-auto\"><h2 class=\"text-center font-bold text-white mb-12\" style=\"font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)\">What You'll Experience</h2><div class=\"grid md:grid-cols-3 gap-8\"><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:rgba(132,204,22,0.1)\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M13 10V3L4 14h7v7l9-11h-7z\"></path></svg></div><h3 class=\"font-bold text-white mb-2\" style=\"font-size:1.25rem\">Explosive Energy</h3><p class=\"text-gray-400\">200mg caffeine for clean, sustained energy without the crash</p></div><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:rgba(132,204,22,0.1)\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z\"></path></svg></div><h3 class=\"font-bold text-white mb-2\" style=\"font-size:1.25rem\">Insane Pumps</h3><p class=\"text-gray-400\">5000mg L-Citrulline for maximum blood flow and vascularity</p></div><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:rgba(132,204,22,0.1)\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z\"></path></svg></div><h3 class=\"font-bold text-white mb-2\" style=\"font-size:1.25rem\">Extended Endurance</h3><p class=\"text-gray-400\">3000mg Beta-Alanine to delay fatigue and power through</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "ingredient-spotlight",
      "html": "<section class=\"py-12 px-4\" style=\"background:#0f0f0f\"><div class=\"max-w-4xl mx-auto\"><h2 class=\"text-center font-bold text-white mb-8\" style=\"font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)\">Clinically Dosed Ingredients</h2><div data-island=\"Tabs\" data-props='{\"tabs\":[{\"label\":\"L-Citrulline (5000mg)\",\"content\":\"<p class=\\\"text-white mb-4\\\">Increases nitric oxide production for improved blood flow and muscle pumps.</p><p class=\\\"text-gray-400 text-sm\\\">Clinically effective dose: 3000-6000mg. Our formula delivers 5000mg per serving.</p>\"},{\"label\":\"Beta-Alanine (3000mg)\",\"content\":\"<p class=\\\"text-white mb-4\\\">Buffers lactic acid to delay muscle fatigue and extend endurance.</p><p class=\\\"text-gray-400 text-sm\\\">Clinically effective dose: 2000-5000mg. Our formula delivers 3000mg per serving.</p>\"},{\"label\":\"Caffeine (200mg)\",\"content\":\"<p class=\\\"text-white mb-4\\\">Enhances focus, energy, and exercise performance.</p><p class=\\\"text-gray-400 text-sm\\\">Clinically effective dose: 100-400mg. Our formula delivers 200mg per serving (equivalent to 2 cups of coffee).</p>\"}],\"variant\":\"dark\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "clinical-proof",
      "html": "<section class=\"py-12 px-4\" style=\"background:#0a0a0a\"><div class=\"max-w-5xl mx-auto\"><h2 class=\"text-center font-bold text-white mb-12\" style=\"font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)\">Backed by Science</h2><div class=\"grid md:grid-cols-3 gap-8 mb-12\"><div class=\"text-center\"><div class=\"text-5xl font-bold mb-2\" style=\"color:var(--lx-accent-color)\">23%</div><p class=\"text-white font-semibold mb-2\">Increase in Strength</p><p class=\"text-sm text-gray-400\">After 8 weeks (Journal of Strength Research, 2024)</p></div><div class=\"text-center\"><div class=\"text-5xl font-bold mb-2\" style=\"color:var(--lx-accent-color)\">18%</div><p class=\"text-white font-semibold mb-2\">Longer Endurance</p><p class=\"text-sm text-gray-400\">Before fatigue onset (Sports Medicine Study, 2025)</p></div><div class=\"text-center\"><div class=\"text-5xl font-bold mb-2\" style=\"color:var(--lx-accent-color)\">94%</div><p class=\"text-white font-semibold mb-2\">Users Report Better Focus</p><p class=\"text-sm text-gray-400\">In our customer survey (n=1,847)</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "pricing",
      "html": "<section class=\"py-12 px-4\" style=\"background:#0f0f0f\"><div class=\"max-w-3xl mx-auto\"><h2 class=\"text-center font-bold text-white mb-2\" style=\"font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)\">Choose Your Supply</h2><p class=\"text-center text-gray-400 mb-8\">Best value when you stock up</p><div data-island=\"QuantityBreaks\" data-props='{\"options\":[{\"quantity\":1,\"label\":\"1 Month Supply (30 servings)\",\"price\":59.99,\"unit_price\":\"$1.99/serving\",\"badge\":\"\"},{\"quantity\":3,\"label\":\"3 Month Supply (90 servings)\",\"price\":149.97,\"unit_price\":\"$1.66/serving\",\"badge\":\"Save 16%\",\"recommended\":true},{\"quantity\":6,\"label\":\"6 Month Supply (180 servings)\",\"price\":269.94,\"unit_price\":\"$1.49/serving\",\"badge\":\"Save 25% — Best Deal\"}]}'></div><div class=\"mt-8\"><div data-island=\"SubscriptionToggle\" data-props='{\"one_time_price\":59.99,\"subscription_price\":47.99,\"subscription_discount\":\"20%\",\"subscription_benefits\":[\"Cancel anytime\",\"Free shipping\",\"Priority support\",\"Early access to new products\"]}'></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "comparison",
      "html": "<section class=\"py-12 px-4\" style=\"background:#0a0a0a\"><div class=\"max-w-5xl mx-auto\"><h2 class=\"text-center font-bold text-white mb-4\" style=\"font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)\">How We Stack Up</h2><p class=\"text-center text-gray-400 mb-8\">Most pre-workouts under-dose key ingredients. We don't.</p><div data-island=\"CompareTable\" data-props='{\"columns\":[\"Our Formula\",\"Brand A\",\"Brand B\",\"Brand C\"],\"rows\":[{\"label\":\"L-Citrulline (clinical dose: 3000-6000mg)\",\"ours\":\"5000mg\",\"a\":\"2000mg\",\"b\":\"3000mg\",\"c\":\"1500mg\"},{\"label\":\"Beta-Alanine (clinical dose: 2000-5000mg)\",\"ours\":\"3000mg\",\"a\":\"1500mg\",\"b\":\"2000mg\",\"c\":\"1000mg\"},{\"label\":\"Caffeine (clinical dose: 100-400mg)\",\"ours\":\"200mg\",\"a\":\"150mg\",\"b\":\"300mg\",\"c\":\"200mg\"},{\"label\":\"3rd Party Tested\",\"ours\":\"✓ NSF Certified\",\"a\":\"✗\",\"b\":\"✓ Informed Sport\",\"c\":\"✗\"},{\"label\":\"Price per Serving\",\"ours\":\"$1.66 (with 3-month)\",\"a\":\"$2.50\",\"b\":\"$1.99\",\"c\":\"$1.80\"},{\"label\":\"Money-Back Guarantee\",\"ours\":\"60 Days\",\"a\":\"30 Days\",\"b\":\"30 Days\",\"c\":\"No Guarantee\"}]}'></div><div class=\"text-center mt-8\"><button class=\"px-8 py-4 rounded-lg font-semibold text-lg text-black hover:opacity-90 transition\" style=\"background:var(--lx-accent-color)\">Choose the Winner</button></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "social-proof",
      "html": "<section class=\"py-12 px-4\" style=\"background:#0f0f0f\"><div class=\"max-w-5xl mx-auto\"><h2 class=\"text-center font-bold text-white mb-8\" style=\"font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)\">What Athletes Are Saying</h2><div data-island=\"ReviewCarousel\" data-props='{\"reviews\":[{\"author\":\"Mike T.\",\"rating\":5,\"text\":\"Best pre-workout I've tried. Clean energy, no crash, insane pumps.\",\"verified\":true},{\"author\":\"Sarah K.\",\"rating\":5,\"text\":\"Finally a pre-workout that doesn't make me jittery. Love the focus.\",\"verified\":true},{\"author\":\"James R.\",\"rating\":5,\"text\":\"Increased my reps by 20% in the first week. This stuff works.\",\"verified\":true}],\"auto_play\":true}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "faq",
      "html": "<section class=\"py-12 px-4\" style=\"background:#0a0a0a\"><div class=\"max-w-3xl mx-auto\"><h2 class=\"text-center font-bold text-white mb-8\" style=\"font-size:clamp(1.5rem,3vw,2.25rem);font-family:var(--lx-font-heading)\">Frequently Asked Questions</h2><div data-island=\"FAQ\" data-props='{\"items\":[{\"question\":\"When should I take this pre-workout?\",\"answer\":\"Take 1 scoop 20-30 minutes before your workout. Mix with 8-10oz of water.\"},{\"question\":\"Will this cause jitters or crash?\",\"answer\":\"Our formula uses 200mg caffeine (equivalent to 2 cups of coffee) for clean energy without jitters. No crash reported by 94% of users.\"},{\"question\":\"Is this safe for daily use?\",\"answer\":\"Yes, when used as directed. However, we recommend cycling (5 days on, 2 days off) to maintain sensitivity. Consult your doctor if you have medical conditions.\"},{\"question\":\"Is it 3rd-party tested?\",\"answer\":\"Yes, every batch is tested by NSF Certified for Sport to ensure purity and absence of banned substances.\"},{\"question\":\"What's your return policy?\",\"answer\":\"60-day money-back guarantee. If you're not satisfied, return it for a full refund — even if the container is empty.\"}],\"variant\":\"dark\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "guarantee",
      "html": "<section class=\"py-12 px-4\" style=\"background:#0f0f0f\"><div class=\"max-w-3xl mx-auto text-center\"><h2 class=\"font-bold text-white mb-4\" style=\"font-size:clamp(1.5rem,3vw,2rem);font-family:var(--lx-font-heading)\">60-Day Money-Back Guarantee</h2><p class=\"text-gray-300 mb-6\">Try it risk-free. If you don't experience better workouts in 60 days, we'll refund every penny — even if the container is empty.</p><button class=\"px-8 py-4 rounded-lg font-semibold text-lg text-black hover:opacity-90 transition\" style=\"background:var(--lx-accent-color)\">Order Risk-Free</button></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "fda-disclaimer",
      "html": "<section class=\"py-8 px-4\" style=\"background:#0a0a0a;border-top:1px solid rgba(255,255,255,0.1)\"><div class=\"max-w-4xl mx-auto\"><p class=\"text-xs text-gray-500 text-center leading-relaxed\">* These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease. Individual results may vary. Consult your healthcare provider before use if you are pregnant, nursing, taking medication, or have a medical condition.</p></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

## Usage Notes

- **Load this skill** when product vertical is supplements, vitamins, protein, nootropics, fitness nutrition, biohacking, wellness, performance enhancers.
- **Dark mode is default** for performance/tech signaling. Use `--lx-bg-color: #0a0a0a` and `--lx-bg-surface: #0f0f0f`.
- **Always show exact ingredient dosages** in Tabs island. Transparency builds trust.
- **Always include TrustBadgeBar** with 3rd-party testing (NSF/Informed Sport/GMP).
- **Always include CompareTable** to show ingredient superiority vs. competitors.
- **Always include QuantityBreaks** (1/3/6 month) and SubscriptionToggle (20%+ discount).
- **Always include FDA disclaimer** near bottom of page.
- **Use islands aggressively** for pricing, comparison, social proof, ingredients, FAQ.
- **Electric accents** (#84cc16 lime, #3b82f6 blue) for energy/urgency signaling.
- **Clinical language** in body copy (dosages, studies, efficacy) paired with bold headlines.
