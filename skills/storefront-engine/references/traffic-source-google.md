# Google Ads & SEO → Landing Page — Storefront Design Intelligence

> **When to load:** Page designed for Google Ads (Search/Shopping/Display) or organic SEO traffic.

## Philosophy

Google traffic arrives with **INTENT**. They searched. They typed keywords. They're already interested — your job is to **answer immediately**.

Unlike social traffic (discovery-driven, emotional), Google visitors want:
- **Information density** — specs, comparisons, evidence
- **Validation** — reviews, certifications, guarantees
- **Clarity** — clear pricing, transparent shipping, no surprises
- **Speed** — fast answers, visible CTAs, minimal friction

**Not needed:** Emotional hooks, storytelling, lifestyle imagery above the fold. They're past awareness — they're evaluating.

**Core principle:** Answer their search query in the first 3 seconds or lose them.

---

## Intent-Based Architecture

Google traffic falls into **4 intent categories**. Each requires a different page structure:

### 1. Transactional Intent ("buy X", "X for sale", "X price")
**User goal:** Make a purchase decision now.  
**Page focus:** Product + price + trust signals + fast checkout.  
**Sections:** 8-10 total.

### 2. Comparison Intent ("X vs Y", "best X", "X alternatives")
**User goal:** Evaluate options before deciding.  
**Page focus:** CompareTable-led, feature grids, "why us" positioning.  
**Sections:** 10-12 total.

### 3. Informational Intent ("how X works", "what is X", "X benefits")
**User goal:** Learn before committing.  
**Page focus:** Educational content, detailed explanations, FAQs.  
**Sections:** 10-14 total.

### 4. Navigational Intent (brand name search)
**User goal:** Find your specific brand.  
**Page focus:** Affirm their choice, show product range, make buying easy.  
**Sections:** 6-8 total.

---

## Section Sequences (by Intent)

### Transactional (8-10 sections)
1. **Product+Price Hero** — image, price, rating, CTA
2. **TrustBadgeBar** — shipping, guarantee, certifications
3. **Key Benefits Grid** — 3-4 benefits with icons
4. **Social Proof** — reviews or testimonials
5. **Product Details** — specs, ingredients, what's included
6. **FAQ** — 8-10 objection-handling questions
7. **Pricing Tiers** (if applicable) — BuyBox or QuantityBreaks
8. **Final CTA** — StickyBar or repeated buy button
9. *Optional:* ProductCarousel (related items)
10. *Optional:* ReviewCarousel (detailed reviews)

### Comparison (10-12 sections)
1. **Comparison Hero** — positioning statement + visual
2. **CompareTable** — you vs 2 competitors, 5-7 rows
3. **Why We Win Grid** — 3-4 differentiators
4. **Evidence Section** — certifications, lab results, press
5. **Detailed Feature Breakdown** — Tabs or accordion
6. **Social Proof** — aggregated reviews
7. **FAQ** — comparison-specific questions ("why more expensive?")
8. **Pricing Display** — clear, with value anchoring
9. **Guarantee/Risk Reversal** — money-back, trial period
10. **Final CTA**
11. *Optional:* Case studies or before/after
12. *Optional:* Video explainer

### Informational (10-14 sections)
1. **Answer-First Hero** — direct answer to search query
2. **Educational Content** — how it works, step-by-step
3. **Visual Explainer** — diagram or video
4. **Benefits Deep Dive** — detailed, with evidence
5. **Scientific Backing** — studies, certifications
6. **Use Cases** — who it's for, scenarios
7. **FAQ** — 10-12 questions (educational + objections)
8. **Social Proof** — reviews focusing on outcomes
9. **Product Details** — what you're actually buying
10. **Comparison** — vs alternatives or status quo
11. **Pricing** — transparent, value-focused
12. **Guarantee**
13. **Final CTA**
14. *Optional:* Related content or resources

### Navigational (6-8 sections)
1. **Brand Hero** — logo, tagline, category
2. **ProductCarousel** — full range
3. **Why Us** — 3-4 key differentiators
4. **Social Proof** — aggregate reviews
5. **FAQ** — brand-specific questions
6. **Final CTA**
7. *Optional:* Company story (brief)
8. *Optional:* Press mentions

---

## Above-the-Fold Rules

**Transactional intent MUST show:**
- Product image (high quality, zoomable)
- Price (actual number, not "learn more")
- Star rating + review count
- Primary CTA ("Add to Cart", not "Learn More")
- Key trust signal (free shipping, guarantee)

**Comparison intent MUST show:**
- Clear positioning ("The #1 alternative to X")
- Visual indication of comparison (split hero or table preview)
- Primary differentiator ("30% more effective")

**Informational intent MUST show:**
- Direct answer to the likely query
- Clear content structure (headings visible)
- Scroll indicator ("Learn more ↓")

**Example: Info-Dense Transactional Hero**
```html
<section class="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-16" style="background:var(--lx-bg-color)">
  <div>
    <img src="IMAGE_URL" alt="Product" class="w-full rounded-xl shadow-lg" />
  </div>
  <div class="flex flex-col justify-center space-y-4">
    <div class="flex items-center gap-2">
      <div class="flex text-yellow-400">
        <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
        <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
        <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
        <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
        <svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
      </div>
      <span class="text-sm font-medium" style="color:var(--lx-text-muted)">4.8/5 from 4,847 reviews</span>
    </div>
    
    <h1 class="font-bold leading-tight" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)">
      Premium Omega-3 Fish Oil — 2,847mg Per Serving
    </h1>
    
    <p class="text-base" style="color:var(--lx-text-muted)">
      Triple-strength formula • 90 softgels • 3-month supply
    </p>
    
    <div class="flex items-baseline gap-3">
      <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$34.99</span>
      <span class="text-xl line-through opacity-40" style="color:var(--lx-text-muted)">$49.99</span>
      <span class="text-xs px-2 py-1 rounded-full font-semibold" style="background:var(--lx-accent-color);color:white">30% OFF</span>
    </div>
    
    <p class="text-sm flex flex-col gap-1" style="color:var(--lx-text-muted)">
      <span>✓ Free shipping on all orders</span>
      <span>✓ 90-day money-back guarantee</span>
      <span>✓ Third-party lab tested</span>
    </p>
    
    <button class="w-full py-4 rounded-lg font-semibold text-lg transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white">
      Add to Cart — Free Shipping
    </button>
    
    <p class="text-xs text-center" style="color:var(--lx-text-muted)">
      In stock • Ships within 24 hours
    </p>
  </div>
</section>
```

---

## Hero Patterns

### Product+Price Hero (Transactional)

**Purpose:** Answer "what is it, how much, why trust you" in 3 seconds.

**Required elements:**
- High-quality product image (left on desktop)
- Star rating + review count (specific number, not "thousands")
- Product name + key benefit as H1
- Key specs or quantity (one line, scannable)
- Price (large, actual number) + compare-at price + discount badge
- 3 trust signals (shipping, guarantee, certification)
- Primary CTA (action-oriented: "Add to Cart", not "Shop Now")
- Stock/shipping status

```html
<!-- See example above -->
```

### Comparison Hero

**Purpose:** Immediately signal "we're better than X" and preview the proof.

```html
<section class="py-12 lg:py-20 px-4" style="background:linear-gradient(135deg, var(--lx-bg-surface) 0%, var(--lx-bg-color) 100%)">
  <div class="max-w-6xl mx-auto text-center">
    <div class="inline-block px-4 py-1 rounded-full text-sm font-semibold mb-4" style="background:var(--lx-accent-color);color:white;opacity:0.9">
      The #1 Alternative to Brand X
    </div>
    
    <h1 class="font-bold mb-4" style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,3rem);color:var(--lx-text-color)">
      30% More Effective. 40% Less Expensive.
    </h1>
    
    <p class="text-lg max-w-2xl mx-auto mb-8" style="color:var(--lx-text-muted)">
      Trusted by over 50,000 customers who switched from premium brands — same results, better value.
    </p>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-4xl mx-auto">
      <div class="p-4 rounded-lg" style="background:var(--lx-bg-color);border:1px solid var(--lx-border-color)">
        <div class="text-2xl font-bold mb-2" style="color:var(--lx-accent-color)">2,847mg</div>
        <div class="text-sm" style="color:var(--lx-text-muted)">vs Competitor's 2,100mg</div>
      </div>
      <div class="p-4 rounded-lg" style="background:var(--lx-bg-color);border:1px solid var(--lx-border-color)">
        <div class="text-2xl font-bold mb-2" style="color:var(--lx-accent-color)">$0.39</div>
        <div class="text-sm" style="color:var(--lx-text-muted)">per serving (vs $0.67)</div>
      </div>
      <div class="p-4 rounded-lg" style="background:var(--lx-bg-color);border:1px solid var(--lx-border-color)">
        <div class="text-2xl font-bold mb-2" style="color:var(--lx-accent-color)">4.8★</div>
        <div class="text-sm" style="color:var(--lx-text-muted)">from 4,847 reviews</div>
      </div>
    </div>
  </div>
</section>
```

### Answer-First Hero (Informational)

**Purpose:** Give them the answer immediately, then earn the click to "learn more".

```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto">
    <h1 class="font-bold mb-6 text-center" style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,3rem);color:var(--lx-text-color)">
      How Long Does It Take for Omega-3 to Work?
    </h1>
    
    <div class="p-6 rounded-xl mb-8" style="background:var(--lx-accent-color);color:white">
      <p class="text-xl font-semibold mb-4">Quick Answer:</p>
      <p class="text-lg leading-relaxed">
        Most people notice initial benefits within <strong>2-3 weeks</strong> (improved mood, focus). 
        Full cardiovascular and joint benefits typically appear after <strong>8-12 weeks</strong> of consistent use.
      </p>
    </div>
    
    <p class="text-lg mb-4" style="color:var(--lx-text-muted)">
      But the timeline depends on several factors. Here's everything you need to know:
    </p>
    
    <div class="flex justify-center">
      <svg class="w-6 h-6 animate-bounce" style="color:var(--lx-text-muted)" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
      </svg>
    </div>
  </div>
</section>
```

---

## CompareTable Strategy

**The power island for Google comparison traffic.** When someone searches "X vs Y", they want a table. Give it to them.

**Rules:**
- **Max 3 columns** — you + 2 competitors (or "typical brand" + "cheap alternative")
- **5-7 rows** — key decision factors only, not feature dump
- **Win the majority** — be honest, but pick rows where you win or tie 4+ times
- **Specific numbers** — not "high quality", but "2,847mg per serving"
- **Visual wins** — checkmarks (✓), crosses (✗), or color-coded cells

**CompareTable island HTML:**
```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-5xl mx-auto">
    <h2 class="text-center font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)">
      How We Compare to Leading Brands
    </h2>
    
    <div data-island="CompareTable" data-props='{
      "columns": ["Our Brand", "Brand X (Premium)", "Brand Y (Budget)"],
      "highlightColumn": 0,
      "rows": [
        {
          "label": "Omega-3 Per Serving",
          "values": ["2,847mg ✓", "2,100mg", "1,200mg"]
        },
        {
          "label": "Price Per Serving",
          "values": ["$0.39 ✓", "$0.67", "$0.28"]
        },
        {
          "label": "Third-Party Tested",
          "values": ["✓ Yes", "✓ Yes", "✗ No"]
        },
        {
          "label": "Purity (Mercury)",
          "values": ["<0.09ppm ✓", "<0.10ppm", "Unknown"]
        },
        {
          "label": "Money-Back Guarantee",
          "values": ["90 days ✓", "30 days", "None"]
        },
        {
          "label": "Free Shipping",
          "values": ["✓ All orders", "Over $50", "✗ Never"]
        },
        {
          "label": "Average Rating",
          "values": ["4.8/5 (4,847) ✓", "4.6/5 (2,103)", "3.9/5 (847)"]
        }
      ]
    }'></div>
    
    <p class="text-center text-sm mt-6" style="color:var(--lx-text-muted)">
      Data last verified: June 2026. Competitor pricing based on publicly listed prices.
    </p>
  </div>
</section>
```

**When to use:**
- Any comparison intent ("X vs Y", "best X", "X alternative")
- Transactional pages in competitive markets (supplement, SaaS, electronics)
- After hero, before deep dive (section 2-3)

---

## Information Density

Google searchers **want substance**. Unlike social traffic (skim, scroll, bounce), they came to read.

**What this means:**
- **More text is OK** — 200-300 word paragraphs are fine if well-structured
- **Use headings liberally** — H2 every 2-3 paragraphs, H3 for sub-points
- **Bullet lists** — break up dense info (specs, benefits, features)
- **Tabs or accordions** — for deep content (ingredients, scientific backing, detailed specs)
- **FAQ with 8-12 questions** — not 4-5 (they have LOTS of questions)

**Bad example (thin):**
```
Our product is the best. Buy now!
```

**Good example (dense but scannable):**
```html
<section class="py-12 px-4">
  <div class="max-w-4xl mx-auto">
    <h2 class="font-bold mb-6" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)">
      What Makes Our Formula Different
    </h2>
    
    <div class="space-y-6">
      <div>
        <h3 class="font-semibold text-xl mb-3" style="color:var(--lx-text-color)">1. Triple-Strength Concentration</h3>
        <p class="leading-relaxed mb-3" style="color:var(--lx-text-muted)">
          Each serving delivers <strong>2,847mg of omega-3 fatty acids</strong> — including 1,647mg EPA and 1,200mg DHA. 
          That's 30-40% more than most "premium" brands, which means faster results and better value per dose.
        </p>
        <ul class="list-disc list-inside space-y-1" style="color:var(--lx-text-muted)">
          <li>EPA: Supports cardiovascular health and reduces inflammation</li>
          <li>DHA: Critical for brain function and cognitive health</li>
          <li>Optimal 4:3 EPA:DHA ratio backed by clinical research</li>
        </ul>
      </div>
      
      <div>
        <h3 class="font-semibold text-xl mb-3" style="color:var(--lx-text-color)">2. Molecular Distillation for Purity</h3>
        <p class="leading-relaxed" style="color:var(--lx-text-muted)">
          We use a proprietary 5-step molecular distillation process to remove mercury, PCBs, and other contaminants. 
          Third-party lab results show <strong>less than 0.09ppm mercury</strong> — well below FDA limits and 
          competitive with pharmaceutical-grade fish oils.
        </p>
      </div>
      
      <div>
        <h3 class="font-semibold text-xl mb-3" style="color:var(--lx-text-color)">3. Triglyceride Form (Not Ethyl Ester)</h3>
        <p class="leading-relaxed" style="color:var(--lx-text-muted)">
          Our omega-3s are in <strong>re-esterified triglyceride (rTG) form</strong>, which studies show is 
          up to 70% more bioavailable than the cheaper ethyl ester (EE) form used by most brands. 
          That means your body actually absorbs what you're paying for.
        </p>
      </div>
    </div>
  </div>
</section>
```

---

## FAQ as Conversion Tool

FAQ is not an afterthought — it's a **conversion section** for Google traffic.

**Why:** Their search queries = questions. Answer them = earn trust.

**Rules:**
- **8-12 questions minimum** (not 4-5)
- **Questions = their actual searches** — use Google autocomplete, People Also Ask, your support tickets
- **Mix types:**
  - Product-specific ("How much EPA/DHA per serving?")
  - Objection-handling ("Why more expensive than Brand X?")
  - Usage ("When should I take it?")
  - Trust ("Is it third-party tested?")

**FAQ island HTML:**
```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-center font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)">
      Frequently Asked Questions
    </h2>
    
    <div data-island="FAQ" data-props='{
      "items": [
        {
          "question": "How much EPA and DHA does each serving contain?",
          "answer": "Each serving (2 softgels) contains 1,647mg EPA and 1,200mg DHA, for a total of 2,847mg of omega-3 fatty acids. This is 30-40% higher than most premium brands."
        },
        {
          "question": "Is your fish oil tested for mercury and contaminants?",
          "answer": "Yes. Every batch is third-party tested by an independent lab (ISO 17025 certified). Our mercury levels are consistently below 0.09ppm — well under FDA limits of 0.1ppm. Lab reports are available on request."
        },
        {
          "question": "Why is this more expensive than other fish oils?",
          "answer": "Three reasons: (1) Higher concentration (2,847mg vs typical 1,000-1,500mg), (2) Re-esterified triglyceride form (70% more bioavailable than cheap ethyl ester forms), (3) Rigorous purity testing. On a per-serving basis of absorbed omega-3, we are actually more cost-effective."
        },
        {
          "question": "How long until I see results?",
          "answer": "Most customers report improved mood and mental clarity within 2-3 weeks. Full cardiovascular benefits typically appear after 8-12 weeks of consistent daily use."
        },
        {
          "question": "What is the difference between triglyceride and ethyl ester forms?",
          "answer": "Ethyl ester (EE) is cheaper to produce but less bioavailable. Triglyceride (TG) and re-esterified triglyceride (rTG) forms are absorbed 50-70% better. We use rTG, which means more omega-3 reaches your cells per softgel."
        },
        {
          "question": "Do I need to take it with food?",
          "answer": "Yes. Omega-3s are fat-soluble, so taking them with a meal containing fat improves absorption by up to 3x. We recommend taking with breakfast or dinner."
        },
        {
          "question": "Is there a fishy aftertaste or burps?",
          "answer": "Our enteric-coated softgels dissolve in your small intestine (not stomach), which eliminates fishy burps. Over 90% of our customers report zero aftertaste."
        },
        {
          "question": "What is your return policy?",
          "answer": "90-day money-back guarantee. If you are not satisfied for any reason, return the bottle (even if empty) within 90 days for a full refund. No questions asked."
        },
        {
          "question": "How does this compare to krill oil?",
          "answer": "Krill oil has lower EPA/DHA content (typically 200-300mg vs our 2,847mg), making it 10x less cost-effective per mg of omega-3. While krill oil has phospholipid-bound omega-3s, our rTG form is comparably bioavailable at a fraction of the cost."
        },
        {
          "question": "Can I take this if I am on blood thinners?",
          "answer": "Omega-3s have mild blood-thinning properties. If you are on warfarin, aspirin, or other anticoagulants, consult your doctor before starting any omega-3 supplement."
        },
        {
          "question": "Is this safe during pregnancy?",
          "answer": "Omega-3s (especially DHA) are important during pregnancy for fetal brain development. However, you should always consult your OB-GYN before starting any supplement while pregnant or nursing."
        },
        {
          "question": "How should I store this?",
          "answer": "Store in a cool, dry place away from direct sunlight. Refrigeration is not required but can extend shelf life. Do not freeze."
        }
      ],
      "defaultOpen": 0
    }'></div>
  </div>
</section>
```

---

## Trust Signals

Google searchers are **validation-driven**. They want proof.

**Specific > vague:**
- ✗ "Thousands of happy customers"
- ✓ "4,847 verified reviews (4.8/5 average)"

**Verifiable > claimed:**
- ✗ "Highest quality"
- ✓ "Third-party tested by ISO 17025 lab (report available)"

**Quantified > general:**
- ✗ "Fast shipping"
- ✓ "Ships within 24 hours • Avg delivery: 3-5 days"

**TrustBadgeBar HTML (below hero):**
```html
<section class="py-6 px-4" style="background:var(--lx-bg-surface);border-top:1px solid var(--lx-border-color);border-bottom:1px solid var(--lx-border-color)">
  <div class="max-w-6xl mx-auto">
    <div data-island="TrustBadgeBar" data-props='{
      "badges": [
        {"icon": "shield-check", "label": "Third-Party Tested", "sublabel": "ISO 17025 certified lab"},
        {"icon": "truck", "label": "Free Shipping", "sublabel": "All orders • Ships in 24hrs"},
        {"icon": "refresh", "label": "90-Day Guarantee", "sublabel": "Full refund, no questions"},
        {"icon": "award", "label": "4.8★ Rating", "sublabel": "From 4,847 reviews"}
      ],
      "layout": "horizontal"
    }'></div>
  </div>
</section>
```

**Key trust signal types:**
1. **Reviews** — star rating + count + recent review snippets
2. **Certifications** — FDA-registered, GMP, NSF, third-party lab
3. **Guarantees** — money-back period, trial offers
4. **Shipping** — speed, cost, tracking
5. **Press/endorsements** — "As seen in X" (if true)
6. **Usage stats** — "50,000+ customers", "1M+ bottles sold"

---

## Pricing Display

**NEVER hide the price.** Google searchers came to evaluate — they will bounce if they can't see the price above fold.

**Rules:**
1. **Show the number** — not "Starting at", not "Learn more", but "$34.99"
2. **Above fold** — in hero or first 2 sections
3. **Anchoring** — show compare-at price if you have one ("$49.99" struck through)
4. **Per-unit for subscriptions** — "$1.17/day" or "$0.39/serving" alongside monthly price
5. **All-in cost** — "Free shipping" or "+$5.99 shipping" (no surprises)
6. **Payment options** — for high-ticket ($100+), show "or 4 payments of $X" (via PaymentOptions island)

**Pricing display HTML (standalone section):**
```html
<section class="py-12 px-4">
  <div class="max-w-3xl mx-auto text-center">
    <h2 class="font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)">
      Simple, Transparent Pricing
    </h2>
    
    <div class="p-8 rounded-xl" style="background:var(--lx-bg-surface);border:2px solid var(--lx-accent-color)">
      <div class="mb-4">
        <span class="text-sm font-semibold px-3 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">BEST VALUE</span>
      </div>
      
      <div class="mb-2">
        <span class="text-5xl font-bold" style="color:var(--lx-text-color)">$34.99</span>
        <span class="text-xl ml-2 line-through opacity-40" style="color:var(--lx-text-muted)">$49.99</span>
      </div>
      
      <p class="text-lg mb-4" style="color:var(--lx-text-muted)">
        $0.39 per serving • 90 servings
      </p>
      
      <ul class="text-left space-y-2 mb-6 max-w-sm mx-auto" style="color:var(--lx-text-muted)">
        <li class="flex items-start gap-2">
          <svg class="w-5 h-5 flex-shrink-0 mt-0.5" style="color:var(--lx-accent-color)" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          <span>2,847mg omega-3 per serving</span>
        </li>
        <li class="flex items-start gap-2">
          <svg class="w-5 h-5 flex-shrink-0 mt-0.5" style="color:var(--lx-accent-color)" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          <span>Free shipping • No subscription required</span>
        </li>
        <li class="flex items-start gap-2">
          <svg class="w-5 h-5 flex-shrink-0 mt-0.5" style="color:var(--lx-accent-color)" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          <span>90-day money-back guarantee</span>
        </li>
        <li class="flex items-start gap-2">
          <svg class="w-5 h-5 flex-shrink-0 mt-0.5" style="color:var(--lx-accent-color)" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          <span>Ships within 24 hours</span>
        </li>
      </ul>
      
      <button class="w-full py-4 rounded-lg font-semibold text-lg transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white">
        Add to Cart
      </button>
    </div>
    
    <p class="text-sm mt-4" style="color:var(--lx-text-muted)">
      One-time purchase • Cancel or modify anytime
    </p>
  </div>
</section>
```

---

## SEO-Ready Structure

Google searchers often came via **organic search** — your page should be SEO-optimized by default.

**Heading hierarchy:**
- One H1 (page title, in hero)
- H2s for major sections (every 400-600 words)
- H3s for sub-sections

**Schema signals** (if applicable):
- Product schema (name, price, rating, availability)
- FAQ schema (automatically added by FAQ island)
- Review schema (aggregate rating)

**Content patterns:**
- **Answer the search query in H1** — "How Long Does Omega-3 Take to Work?" not "Welcome to Our Site"
- **First paragraph = direct answer** — Google often pulls this for featured snippets
- **Use the keyword naturally** — in H1, first paragraph, 2-3 H2s, image alt text
- **Internal links** — to related products, blog posts, category pages
- **External links** — to studies, certifications (builds trust with Google)

---

## Anti-Patterns

**12 Google landing page killers:**

1. **Hidden pricing** — "Contact for quote", "See pricing", "Learn more". Instant bounce.
2. **Emotional-first hero** — Lifestyle imagery + vague tagline. They came to evaluate, not dream.
3. **No comparison** — In competitive markets, failing to position vs alternatives = lost sale.
4. **Thin content** — 3 sections, 400 words total. They have questions; answer them.
5. **No FAQ** — Means you are hiding something or don't understand their concerns.
6. **Fake scarcity** — "Only 3 left!" (refreshes to "Only 3 left!" again). Destroys trust.
7. **No reviews** — Or only 5-star reviews with no detail. Suspicious.
8. **Vague specs** — "High quality", "Premium ingredients". What does that MEAN?
9. **Slow above-fold CTA** — Button is in section 4. They bounced in section 2.
10. **No guarantee** — Asking them to take all the risk. Reduces conversions 20-40%.
11. **Auto-play video** — Especially with sound. Rage quit.
12. **Newsletter popup on entry** — They just arrived. Let them read first.

---

## Complete Blueprints

### Blueprint 1: Transactional Product Page (Omega-3 Example)

```json
{
  "page_id": "omega3-google-transactional",
  "intent": "transactional",
  "traffic_source": "google_ads_search",
  "target_query": "buy omega 3 fish oil",
  
  "head": {
    "title": "Premium Omega-3 Fish Oil (2,847mg) — $34.99 | Free Shipping",
    "description": "Triple-strength omega-3 with 2,847mg per serving. Third-party tested for purity. 4.8★ from 4,847 reviews. 90-day guarantee. Free shipping.",
    "keywords": ["omega 3", "fish oil", "EPA DHA", "omega 3 supplement"]
  },
  
  "theme_css": ":root{--lx-accent-color:#0066CC;--lx-text-color:#1a1a1a;--lx-text-muted:#666666;--lx-bg-color:#ffffff;--lx-bg-surface:#f5f5f5;--lx-border-color:#e0e0e0;--lx-font-heading:'Inter',sans-serif;--lx-font-body:'Inter',sans-serif}",
  
  "sections": [
    {
      "id": "hero",
      "type": "product_info_hero",
      "html": "<section class=\"grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-16\" style=\"background:var(--lx-bg-color)\"><div><img src=\"/images/omega3-bottle.jpg\" alt=\"Premium Omega-3 Fish Oil Bottle\" class=\"w-full rounded-xl shadow-lg\"/></div><div class=\"flex flex-col justify-center space-y-4\"><div class=\"flex items-center gap-2\"><div class=\"flex text-yellow-400\"><svg class=\"w-5 h-5 fill-current\" viewBox=\"0 0 20 20\"><path d=\"M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z\"/></svg><svg class=\"w-5 h-5 fill-current\" viewBox=\"0 0 20 20\"><path d=\"M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z\"/></svg><svg class=\"w-5 h-5 fill-current\" viewBox=\"0 0 20 20\"><path d=\"M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z\"/></svg><svg class=\"w-5 h-5 fill-current\" viewBox=\"0 0 20 20\"><path d=\"M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z\"/></svg><svg class=\"w-5 h-5 fill-current\" viewBox=\"0 0 20 20\"><path d=\"M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z\"/></svg></div><span class=\"text-sm font-medium\" style=\"color:var(--lx-text-muted)\">4.8/5 from 4,847 reviews</span></div><h1 class=\"font-bold leading-tight\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)\">Premium Omega-3 Fish Oil — 2,847mg Per Serving</h1><p class=\"text-base\" style=\"color:var(--lx-text-muted)\">Triple-strength formula • 90 softgels • 3-month supply</p><div class=\"flex items-baseline gap-3\"><span class=\"text-3xl font-bold\" style=\"color:var(--lx-text-color)\">$34.99</span><span class=\"text-xl line-through opacity-40\" style=\"color:var(--lx-text-muted)\">$49.99</span><span class=\"text-xs px-2 py-1 rounded-full font-semibold\" style=\"background:var(--lx-accent-color);color:white\">30% OFF</span></div><p class=\"text-sm flex flex-col gap-1\" style=\"color:var(--lx-text-muted)\"><span>✓ Free shipping on all orders</span><span>✓ 90-day money-back guarantee</span><span>✓ Third-party lab tested</span></p><button class=\"w-full py-4 rounded-lg font-semibold text-lg transition-transform hover:scale-105\" style=\"background:var(--lx-accent-color);color:white\">Add to Cart — Free Shipping</button><p class=\"text-xs text-center\" style=\"color:var(--lx-text-muted)\">In stock • Ships within 24 hours</p></div></section>"
    },
    {
      "id": "trust-bar",
      "type": "trust_badges",
      "html": "<section class=\"py-6 px-4\" style=\"background:var(--lx-bg-surface);border-top:1px solid var(--lx-border-color);border-bottom:1px solid var(--lx-border-color)\"><div class=\"max-w-6xl mx-auto\"><div data-island=\"TrustBadgeBar\" data-props='{\"badges\":[{\"icon\":\"shield-check\",\"label\":\"Third-Party Tested\",\"sublabel\":\"ISO 17025 certified lab\"},{\"icon\":\"truck\",\"label\":\"Free Shipping\",\"sublabel\":\"All orders • Ships in 24hrs\"},{\"icon\":\"refresh\",\"label\":\"90-Day Guarantee\",\"sublabel\":\"Full refund, no questions\"},{\"icon\":\"award\",\"label\":\"4.8★ Rating\",\"sublabel\":\"From 4,847 reviews\"}],\"layout\":\"horizontal\"}'></div></div></section>"
    },
    {
      "id": "benefits",
      "type": "benefits_grid",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><h2 class=\"text-center font-bold mb-12\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">Why Customers Choose Our Omega-3</h2><div class=\"grid grid-cols-1 md:grid-cols-3 gap-8\"><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-accent-color);opacity:0.1\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path d=\"M9 2a1 1 0 000 2h2a1 1 0 100-2H9z\"/><path fill-rule=\"evenodd\" d=\"M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm9.707 5.707a1 1 0 00-1.414-1.414L9 12.586l-1.293-1.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"/></svg></div><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">Triple-Strength Formula</h3><p style=\"color:var(--lx-text-muted)\">2,847mg per serving — 30-40% more than premium brands. Better value, faster results.</p></div><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-accent-color);opacity:0.1\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"/></svg></div><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">Pharmaceutical-Grade Purity</h3><p style=\"color:var(--lx-text-muted)\">Molecular distillation removes mercury, PCBs. Third-party tested every batch.</p></div><div class=\"text-center\"><div class=\"w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center\" style=\"background:var(--lx-accent-color);opacity:0.1\"><svg class=\"w-8 h-8\" style=\"color:var(--lx-accent-color)\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path fill-rule=\"evenodd\" d=\"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z\" clip-rule=\"evenodd\"/></svg></div><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">70% Better Absorption</h3><p style=\"color:var(--lx-text-muted)\">Re-esterified triglyceride (rTG) form — not cheap ethyl ester. Your body absorbs more.</p></div></div></div></section>"
    },
    {
      "id": "reviews",
      "type": "social_proof",
      "html": "<section class=\"py-12 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-6xl mx-auto\"><h2 class=\"text-center font-bold mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">What Customers Are Saying</h2><div data-island=\"ReviewCarousel\" data-props='{\"reviews\":[{\"name\":\"Sarah M.\",\"rating\":5,\"text\":\"I have tried 4 different omega-3 brands over the years. This one actually works — my joint pain is 80% better after 6 weeks. Worth every penny.\",\"verified\":true},{\"name\":\"Michael T.\",\"rating\":5,\"text\":\"No fishy burps! And my doctor said my triglyceride levels dropped 47 points in 3 months. Switching from my old brand was the best decision.\",\"verified\":true},{\"name\":\"Jennifer K.\",\"rating\":5,\"text\":\"I am a pharmacist and very picky about supplements. The rTG form and third-party testing sold me. My whole family takes this now.\",\"verified\":true}],\"autoplay\":true,\"interval\":5000}'></div></div></section>"
    },
    {
      "id": "details",
      "type": "product_details",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-4xl mx-auto\"><h2 class=\"font-bold mb-6\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">What Makes Our Formula Different</h2><div class=\"space-y-6\"><div><h3 class=\"font-semibold text-xl mb-3\" style=\"color:var(--lx-text-color)\">1. Triple-Strength Concentration</h3><p class=\"leading-relaxed mb-3\" style=\"color:var(--lx-text-muted)\">Each serving delivers <strong>2,847mg of omega-3 fatty acids</strong> — including 1,647mg EPA and 1,200mg DHA. That's 30-40% more than most \"premium\" brands, which means faster results and better value per dose.</p><ul class=\"list-disc list-inside space-y-1\" style=\"color:var(--lx-text-muted)\"><li>EPA: Supports cardiovascular health and reduces inflammation</li><li>DHA: Critical for brain function and cognitive health</li><li>Optimal 4:3 EPA:DHA ratio backed by clinical research</li></ul></div><div><h3 class=\"font-semibold text-xl mb-3\" style=\"color:var(--lx-text-color)\">2. Molecular Distillation for Purity</h3><p class=\"leading-relaxed\" style=\"color:var(--lx-text-muted)\">We use a proprietary 5-step molecular distillation process to remove mercury, PCBs, and other contaminants. Third-party lab results show <strong>less than 0.09ppm mercury</strong> — well below FDA limits and competitive with pharmaceutical-grade fish oils.</p></div><div><h3 class=\"font-semibold text-xl mb-3\" style=\"color:var(--lx-text-color)\">3. Triglyceride Form (Not Ethyl Ester)</h3><p class=\"leading-relaxed\" style=\"color:var(--lx-text-muted)\">Our omega-3s are in <strong>re-esterified triglyceride (rTG) form</strong>, which studies show is up to 70% more bioavailable than the cheaper ethyl ester (EE) form used by most brands. That means your body actually absorbs what you're paying for.</p></div></div></div></section>"
    },
    {
      "id": "faq",
      "type": "faq",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto\"><h2 class=\"text-center font-bold mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)\">Frequently Asked Questions</h2><div data-island=\"FAQ\" data-props='{\"items\":[{\"question\":\"How much EPA and DHA does each serving contain?\",\"answer\":\"Each serving (2 softgels) contains 1,647mg EPA and 1,200mg DHA, for a total of 2,847mg of omega-3 fatty acids. This is 30-40% higher than most premium brands.\"},{\"question\":\"Is your fish oil tested for mercury and contaminants?\",\"answer\":\"Yes. Every batch is third-party tested by an independent lab (ISO 17025 certified). Our mercury levels are consistently below 0.09ppm — well under FDA limits of 0.1ppm. Lab reports are available on request.\"},{\"question\":\"Why is this more expensive than other fish oils?\",\"answer\":\"Three reasons: (1) Higher concentration (2,847mg vs typical 1,000-1,500mg), (2) Re-esterified triglyceride form (70% more bioavailable than cheap ethyl ester forms), (3) Rigorous purity testing. On a per-serving basis of absorbed omega-3, we are actually more cost-effective.\"},{\"question\":\"How long until I see results?\",\"answer\":\"Most customers report improved mood and mental clarity within 2-3 weeks. Full cardiovascular benefits typically appear after 8-12 weeks of consistent daily use.\"},{\"question\":\"What is the difference between triglyceride and ethyl ester forms?\",\"answer\":\"Ethyl ester (EE) is cheaper to produce but less bioavailable. Triglyceride (TG) and re-esterified triglyceride (rTG) forms are absorbed 50-70% better. We use rTG, which means more omega-3 reaches your cells per softgel.\"},{\"question\":\"Do I need to take it with food?\",\"answer\":\"Yes. Omega-3s are fat-soluble, so taking them with a meal containing fat improves absorption by up to 3x. We recommend taking with breakfast or dinner.\"},{\"question\":\"Is there a fishy aftertaste or burps?\",\"answer\":\"Our enteric-coated softgels dissolve in your small intestine (not stomach), which eliminates fishy burps. Over 90% of our customers report zero aftertaste.\"},{\"question\":\"What is your return policy?\",\"answer\":\"90-day money-back guarantee. If you are not satisfied for any reason, return the bottle (even if empty) within 90 days for a full refund. No questions asked.\"}],\"defaultOpen\":0}'></div></div></section>"
    },
    {
      "id": "final-cta",
      "type": "sticky_cta",
      "html": "<section class=\"py-12 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-3xl mx-auto text-center\"><h2 class=\"font-bold mb-4\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">Try Risk-Free for 90 Days</h2><p class=\"text-lg mb-6\" style=\"color:var(--lx-text-muted)\">If you don't feel better in 90 days, return it for a full refund. No questions asked.</p><button class=\"px-12 py-4 rounded-lg font-semibold text-lg transition-transform hover:scale-105\" style=\"background:var(--lx-accent-color);color:white\">Add to Cart — $34.99</button><p class=\"text-sm mt-4\" style=\"color:var(--lx-text-muted)\">Free shipping • Ships within 24 hours</p></div></section>"
    }
  ]
}
```

### Blueprint 2: Comparison Page

```json
{
  "page_id": "omega3-google-comparison",
  "intent": "comparison",
  "traffic_source": "google_ads_search",
  "target_query": "best omega 3 supplement comparison",
  
  "head": {
    "title": "Best Omega-3 Comparison: We Test 12 Brands | 2026 Results",
    "description": "Independent comparison of top omega-3 brands. See purity tests, EPA/DHA levels, price per mg, and real customer results. Updated June 2026.",
    "keywords": ["omega 3 comparison", "best omega 3", "fish oil review"]
  },
  
  "theme_css": ":root{--lx-accent-color:#0066CC;--lx-text-color:#1a1a1a;--lx-text-muted:#666666;--lx-bg-color:#ffffff;--lx-bg-surface:#f5f5f5;--lx-border-color:#e0e0e0;--lx-font-heading:'Inter',sans-serif;--lx-font-body:'Inter',sans-serif}",
  
  "sections": [
    {
      "id": "hero",
      "type": "comparison_hero",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:linear-gradient(135deg, var(--lx-bg-surface) 0%, var(--lx-bg-color) 100%)\"><div class=\"max-w-6xl mx-auto text-center\"><div class=\"inline-block px-4 py-1 rounded-full text-sm font-semibold mb-4\" style=\"background:var(--lx-accent-color);color:white;opacity:0.9\">The #1 Alternative to Nordic Naturals</div><h1 class=\"font-bold mb-4\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,4vw,3rem);color:var(--lx-text-color)\">30% More EPA+DHA. 40% Less Expensive.</h1><p class=\"text-lg max-w-2xl mx-auto mb-8\" style=\"color:var(--lx-text-muted)\">Trusted by over 50,000 customers who switched from premium brands — same purity standards, better value.</p><div class=\"grid grid-cols-1 md:grid-cols-3 gap-4 max-w-4xl mx-auto\"><div class=\"p-4 rounded-lg\" style=\"background:var(--lx-bg-color);border:1px solid var(--lx-border-color)\"><div class=\"text-2xl font-bold mb-2\" style=\"color:var(--lx-accent-color)\">2,847mg</div><div class=\"text-sm\" style=\"color:var(--lx-text-muted)\">vs Nordic's 2,100mg</div></div><div class=\"p-4 rounded-lg\" style=\"background:var(--lx-bg-color);border:1px solid var(--lx-border-color)\"><div class=\"text-2xl font-bold mb-2\" style=\"color:var(--lx-accent-color)\">$0.39</div><div class=\"text-sm\" style=\"color:var(--lx-text-muted)\">per serving (vs $0.67)</div></div><div class=\"p-4 rounded-lg\" style=\"background:var(--lx-bg-color);border:1px solid var(--lx-border-color)\"><div class=\"text-2xl font-bold mb-2\" style=\"color:var(--lx-accent-color)\">4.8★</div><div class=\"text-sm\" style=\"color:var(--lx-text-muted)\">from 4,847 reviews</div></div></div></div></section>"
    },
    {
      "id": "compare-table",
      "type": "comparison_table",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-5xl mx-auto\"><h2 class=\"text-center font-bold mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)\">How We Compare to Leading Brands</h2><div data-island=\"CompareTable\" data-props='{\"columns\":[\"Our Brand\",\"Nordic Naturals\",\"Nature Made\"],\"highlightColumn\":0,\"rows\":[{\"label\":\"Omega-3 Per Serving\",\"values\":[\"2,847mg ✓\",\"2,100mg\",\"1,200mg\"]},{\"label\":\"Price Per Serving\",\"values\":[\"$0.39 ✓\",\"$0.67\",\"$0.28\"]},{\"label\":\"Form\",\"values\":[\"rTG (70% more bioavailable) ✓\",\"TG\",\"EE (ethyl ester)\"]},{\"label\":\"Purity (Mercury)\",\"values\":[\"<0.09ppm ✓\",\"<0.10ppm\",\"Not disclosed\"]},{\"label\":\"Third-Party Tested\",\"values\":[\"✓ Every batch\",\"✓ Yes\",\"✗ No\"]},{\"label\":\"Money-Back Guarantee\",\"values\":[\"90 days ✓\",\"30 days\",\"None\"]},{\"label\":\"Free Shipping\",\"values\":[\"✓ All orders\",\"Over $50\",\"✗ Never\"]},{\"label\":\"Average Rating\",\"values\":[\"4.8/5 (4,847) ✓\",\"4.6/5 (2,103)\",\"3.9/5 (847)\"]}]}'></div><p class=\"text-center text-sm mt-6\" style=\"color:var(--lx-text-muted)\">Data last verified: June 2026. Competitor pricing based on publicly listed prices.</p></div></section>"
    },
    {
      "id": "why-we-win",
      "type": "benefits_grid",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><h2 class=\"text-center font-bold mb-12\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">Why 50,000+ Customers Switched</h2><div class=\"grid grid-cols-1 md:grid-cols-3 gap-8\"><div class=\"text-center p-6\"><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">More Omega-3 Per Dollar</h3><p style=\"color:var(--lx-text-muted)\">At $0.39/serving for 2,847mg, you get <strong>7,300mg of absorbed omega-3 per dollar</strong> vs 3,100mg with Nordic Naturals.</p></div><div class=\"text-center p-6\"><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">Same Purity Standards</h3><p style=\"color:var(--lx-text-muted)\">We use the same third-party labs as premium brands. Mercury <0.09ppm, PCBs undetectable. Lab reports available.</p></div><div class=\"text-center p-6\"><h3 class=\"font-semibold text-lg mb-2\" style=\"color:var(--lx-text-color)\">3X Longer Guarantee</h3><p style=\"color:var(--lx-text-muted)\">90-day money-back (vs 30-day industry standard). We want you to actually see results before committing.</p></div></div></div></section>"
    },
    {
      "id": "faq",
      "type": "faq",
      "html": "<section class=\"py-12 lg:py-20 px-4\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto\"><h2 class=\"text-center font-bold mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem);color:var(--lx-text-color)\">Common Comparison Questions</h2><div data-island=\"FAQ\" data-props='{\"items\":[{\"question\":\"How can you be cheaper if you have more omega-3?\",\"answer\":\"We sell direct-to-consumer with no retail markup. Nordic Naturals pays 40-50% to retailers (Whole Foods, CVS). We pass those savings to you.\"},{\"question\":\"Is rTG form really better than regular TG?\",\"answer\":\"Both are good. rTG is molecularly identical to natural fish oil triglycerides but concentrated. Studies show 10-20% better absorption than TG, 50-70% better than EE (ethyl ester).\"},{\"question\":\"Why do you compare to Nordic Naturals specifically?\",\"answer\":\"They are the #1 premium brand and set the purity/quality standard. If we match or beat them on purity while offering 40% better value, it proves our quality.\"},{\"question\":\"How do I know your lab reports are real?\",\"answer\":\"Every bottle has a lot number. Email us with the lot number and we will send you the third-party lab report (COA) for that specific batch.\"}],\"defaultOpen\":0}'></div></div></section>"
    },
    {
      "id": "cta",
      "type": "final_cta",
      "html": "<section class=\"py-12 px-4\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-3xl mx-auto text-center\"><h2 class=\"font-bold mb-4\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2rem);color:var(--lx-text-color)\">Try the #1 Nordic Naturals Alternative</h2><p class=\"text-lg mb-6\" style=\"color:var(--lx-text-muted)\">90-day guarantee. If you don't prefer us, get a full refund.</p><button class=\"px-12 py-4 rounded-lg font-semibold text-lg transition-transform hover:scale-105\" style=\"background:var(--lx-accent-color);color:white\">Add to Cart — $34.99</button></div></section>"
    }
  ]
}
```

---

## Summary

**Google traffic = intent-driven.** Answer their query immediately, then earn the conversion with evidence.

**Key principles:**
1. **Show price above fold** — always
2. **Information density** — they want substance
3. **CompareTable for comparison intent** — the power island
4. **FAQ 8-12 questions** — their search queries = your FAQs
5. **Trust signals specific + verifiable** — not vague claims
6. **SEO-ready structure** — H1 = search query answer

**Avoid:** Hiding price, emotional-first heroes, thin content, no comparison, fake scarcity, vague specs.

**When in doubt:** Ask "Does this answer their search query in 3 seconds?" If no, rewrite.
