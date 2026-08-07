# Conversion Psychology — Storefront Design Intelligence

> When to load: ALWAYS. Read before generating any ecommerce page.

## The Conversion Stack (AIDA → Sections)

Map the AIDA framework to section order. Each stage requires specific psychology and placement.

### Short Page (5-7 sections) — Impulse / Low-consideration products

1. **Attention (1 section)**: Hero section
   - High-contrast gradient or bold product image
   - Benefit-driven headline (6-10 words)
   - `font-size: clamp(2.5rem, 5vw, 3.5rem)` for headline
   - Sticky CTA bar for persistent action

2. **Interest (2 sections)**: Value props + social proof stats
   - 3 icon-driven benefits max
   - Numbers: customer count, star rating, review count
   - `py-8 md:py-12` spacing

3. **Desire (2 sections)**: Reviews + transformation proof
   - Star-first review display, 3-6 reviews
   - Before/after images or testimonial carousel
   - `data-island="ReviewCarousel"` for dynamic trust

4. **Action (2 sections)**: CTA + footer
   - Urgency element (countdown or inventory indicator)
   - First-person CTA copy: "Get MY [benefit]"
   - `data-island="CountdownTimer"` or `data-island="InventoryIndicator"`

### Medium Page (8-12 sections) — Considered purchase / New-to-brand

1. **Attention (1)**: Hero with video or interactive media
2. **Interest (3)**: Value props → logo carousel → stats
   - Logo carousel = trust transfer from known brands
   - Neutral background between hero and body
3. **Desire (5)**: Feature grid → testimonials → before/after → reviews → comparison table
   - 3-6 features with icons
   - Transformation proof with `data-island="BeforeAfter"`
   - Compare you vs. 2 alternatives (3 columns max)
4. **Action (3)**: FAQ → CTA → footer
   - Preemptive objection handling (5-8 questions)
   - `data-island="EmailCapture"` for fence-sitters
   - `data-island="FAQ"` for progressive disclosure

### Long Page (12-16 sections) — High-ticket / Complex products

1. **Attention (2)**: Hero + announcement bar
   - Free shipping threshold / promo in bar
2. **Interest (4)**: Value props → logo carousel → stats → press mentions
   - Layer authority progressively: claims → endorsements → proof
3. **Desire (7)**: Feature showcase → testimonials → case study → feature grid → reviews → comparison → risk reversal
   - Hero feature with `data-island="VideoPlayer"`
   - Full customer journey (problem → solution → result)
   - Guarantee + return policy badge-driven
4. **Action (3)**: FAQ → dual CTA → footer
   - Dual CTA: buy now / learn more
   - `data-island="BundleBuilder"` for upsells

**Section Order Rules:**
- Never reviews before value props (prove value before social proof)
- FAQ immediately before final CTA (remove last objection)
- Stats or logo carousel within first 3 sections for trust anchoring
- Footer always last (consistency signal)

---

## Above-the-Fold Rules

What MUST be visible without scroll (< 900px viewport height). Violating this kills 40%+ of conversions.

### PDP (Product Detail Page)

**Mandatory visible elements:**
- Product image (left 50-60% width, min 600px tall)
- Product title (max 2 lines)
- Price + compare_at_price (if discounted)
- Star rating + review count (clickable to reviews)
- Primary CTA button
- 1-2 trust badges (free shipping, guarantee)

**HTML pattern:**
```html
<section class="grid md:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 py-8">
  <div class="relative">
    <img src="/product.jpg" alt="Product" class="w-full h-auto rounded-lg" />
  </div>
  <div class="flex flex-col justify-center space-y-6">
    <h1 class="text-4xl md:text-5xl font-bold leading-tight" style="color:var(--lx-text-color)">
      Premium Product Name
    </h1>
    <p class="text-lg md:text-xl opacity-80">One-line benefit promise that resonates</p>
    <div class="flex items-baseline gap-3">
      <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$89.00</span>
      <span class="text-lg line-through opacity-40">$129.00</span>
      <span class="text-xs font-semibold px-2 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">31% OFF</span>
    </div>
    <div class="flex items-center gap-2">
      <div class="flex">
        <span class="text-yellow-400">★★★★★</span>
      </div>
      <span class="text-sm opacity-70">(2,847 reviews)</span>
    </div>
    <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart — Free Shipping","showQuantity":true}'></div>
    <div class="flex gap-4 pt-4">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🚚</span>
        <span class="text-sm">Free Shipping</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-2xl">💯</span>
        <span class="text-sm">Money-Back Guarantee</span>
      </div>
    </div>
  </div>
</section>
```

### Landing Page (paid traffic)

**Mandatory visible:**
- Headline with specific benefit (not generic)
- Subline addressing pain point
- Hero image/video showing product in use
- Primary CTA (above fold)
- 1 trust signal (review stars or customer count)

**HTML pattern:**
```html
<section class="relative min-h-screen flex items-center justify-center text-center px-4 py-20" style="background:linear-gradient(135deg, #667eea 0%, #764ba2 100%)">
  <div class="max-w-4xl mx-auto space-y-8">
    <h1 class="text-5xl md:text-7xl font-extrabold leading-none text-white">
      Get Flawless Skin in 30 Days
    </h1>
    <p class="text-xl md:text-2xl text-white/90">
      Without harsh chemicals or expensive treatments. Guaranteed.
    </p>
    <button class="px-10 py-5 text-xl font-bold rounded-lg transition-transform hover:scale-105" style="background:white;color:var(--lx-accent-color)">
      Start MY Transformation
    </button>
    <p class="text-white/80 text-sm">Join 47,000+ customers who transformed their skin</p>
  </div>
  <div data-island="CountdownTimer" data-props='{"endDate":"2026-06-30T23:59:59Z","message":"Offer ends in:","urgencyThreshold":3600}'></div>
  <div data-island="SocialProofPopup" data-props='{"displayDuration":5000,"interval":15000,"maxPopups":3}'></div>
</section>
```

### Collection Page

**Mandatory visible:**
- Category headline + product count
- Filter bar (collapsible on mobile)
- First 4-6 products (2x3 grid desktop, 2 columns mobile)
- Sort dropdown
- Trust signal (delivery promise or return policy)

**Layout rule:** First product fold < 600px from top on desktop, < 800px on mobile.

---

## Price Psychology Patterns

### Anchoring (strikethrough + current)

Show original price crossed out. Minimum 20% discount to be credible, optimal 30-40%.

```html
<div class="flex items-baseline gap-3">
  <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$79.99</span>
  <span class="text-lg line-through opacity-40">$119.99</span>
  <span class="text-xs font-semibold px-2 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">33% OFF</span>
</div>
<p class="text-sm mt-2 opacity-70">Save $40 today</p>
```

### Charm Pricing

End prices in .97, .95, or .99. Never .00 for mid-market ($50-$300). Use .00 only for premium ($500+).

**Examples:**
- Low-ticket (<$50): $29.97, $14.99
- Mid-ticket ($50-$300): $129.95, $79.97
- High-ticket ($300+): $999.00, $1,500.00

### Bundle Pricing (quantity breaks)

Show per-unit savings, not just total discount.

```html
<div class="grid md:grid-cols-3 gap-4">
  <div class="p-6 border rounded-lg" style="border-color:var(--lx-border-color)">
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 1</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$59.99</p>
      <p class="text-sm opacity-70">$59.99 each</p>
      <button class="w-full px-4 py-2 mt-4 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
  <div class="p-6 border-2 rounded-lg relative transform scale-105" style="border-color:var(--lx-accent-color);box-shadow:0 20px 60px rgba(102,126,234,0.2)">
    <span class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 text-xs font-semibold rounded-full text-white" style="background:var(--lx-accent-color)">BEST VALUE</span>
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 3</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$119.99</p>
      <p class="text-sm opacity-70">$40.00 each — Save $60</p>
      <button class="w-full px-4 py-3 mt-4 rounded font-bold text-white" style="background:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
  <div class="p-6 border rounded-lg" style="border-color:var(--lx-border-color)">
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 2</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$99.99</p>
      <p class="text-sm opacity-70">$50.00 each — Save $20</p>
      <button class="w-full px-4 py-2 mt-4 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
</div>
```

### Payment Splitting (Afterpay/Klarna)

Show "or 4 payments of $X" beneath price. Increases conversion 20-30% for $100+ items.

```html
<div class="space-y-2">
  <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$159.99</p>
  <p class="text-sm opacity-70">or 4 interest-free payments of $40.00 with <strong>Afterpay</strong></p>
</div>
```

### Decoy Pricing (3-tier)

Always show 3 options. Middle option is the target, positioned as "most popular".

```html
<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <h3 class="text-2xl font-bold mb-2">Basic</h3>
    <p class="text-4xl font-bold mb-4" style="color:var(--lx-text-color)">$49.99</p>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature A</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature B</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
      Get Started
    </button>
  </div>
  <div class="p-8 rounded-lg relative transform scale-105" style="border:3px solid var(--lx-accent-color);box-shadow:0 20px 60px rgba(0,0,0,0.2)">
    <span class="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 text-sm font-semibold rounded-full text-white" style="background:var(--lx-accent-color)">MOST POPULAR</span>
    <h3 class="text-2xl font-bold mb-2">Pro</h3>
    <div class="flex items-baseline gap-2 mb-4">
      <p class="text-4xl font-bold" style="color:var(--lx-text-color)">$89.99</p>
      <p class="text-lg line-through opacity-40">$129.99</p>
    </div>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature A</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature B</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature C</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature D</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded font-bold text-white" style="background:var(--lx-accent-color)">
      Start Pro Trial
    </button>
  </div>
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <h3 class="text-2xl font-bold mb-2">Premium</h3>
    <p class="text-4xl font-bold mb-4" style="color:var(--lx-text-color)">$149.99</p>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Everything in Pro</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature E</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature F</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Priority Support</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
      Go Premium
    </button>
  </div>
</div>
```

---

## Social Proof Hierarchy

Rank order by persuasive power (highest to lowest). Use this sequence in sections.

### 1. Numbers (stats bar)

Raw metrics. Most credible when specific and large.

```html
<section class="py-16 px-4" style="background:var(--lx-bg-surface)">
  <div class="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-6xl mx-auto text-center">
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">247,000+</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Happy Customers</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">4.8/5.0</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Average Rating</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">12,000+</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">5-Star Reviews</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">94%</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Would Recommend</p>
    </div>
  </div>
</section>
```

**When to use:** First 3 sections. Anchor trust before storytelling.

### 2. Faces (testimonial cards)

Photos + quotes. Most effective for emotional products (beauty, wellness, lifestyle).

```html
<section class="py-16 px-4">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="color:var(--lx-text-color)">What Our Customers Say</h2>
    <div class="grid md:grid-cols-3 gap-8">
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface)">
        <div class="flex items-center gap-4 mb-4">
          <img src="/testimonials/sarah.jpg" alt="Sarah M." class="w-20 h-20 rounded-full" style="border:4px solid var(--lx-accent-color)" />
          <div>
            <p class="font-bold">Sarah M.</p>
            <p class="text-sm opacity-70">Verified Buyer</p>
            <div class="flex text-yellow-400">★★★★★</div>
          </div>
        </div>
        <p class="text-lg italic leading-relaxed opacity-90">
          "This completely changed how I approach skincare. I saw results in just 2 weeks."
        </p>
      </div>
      <!-- Repeat for more testimonials -->
    </div>
  </div>
</section>
```

**When to use:** After interest stage, before feature deep-dive. 3-6 testimonials max per section.

### 3. Logos (logo carousel)

Trust transfer from known brands. Works for B2B, press mentions, "as seen on".

```html
<section class="py-12 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto">
    <p class="text-center text-sm uppercase tracking-wide mb-8 opacity-70">Trusted by Leading Brands</p>
    <div class="flex justify-center items-center gap-12 flex-wrap">
      <img src="/logos/forbes.svg" alt="Forbes" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
      <img src="/logos/techcrunch.svg" alt="TechCrunch" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
      <img src="/logos/wsj.svg" alt="Wall Street Journal" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
    </div>
  </div>
</section>
```

**When to use:** Section 2-3. Before testimonials, after value props.

### 4. Quotes (review list)

Text-only reviews. Lowest impact but high volume works (10+ reviews).

```html
<section class="py-16 px-4">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="color:var(--lx-text-color)">12,000+ 5-Star Reviews</h2>
    <div data-island="ReviewCarousel" data-props='{"autoplay":true,"reviewsPerView":3,"reviews":[{"rating":5,"text":"Exceeded expectations. Results were visible in days. Highly recommend.","author":"John D.","verified":true,"date":"2026-06-15"}]}'></div>
  </div>
</section>
```

**When to use:** Mid-page (sections 5-8). Pile-on after testimonials for reinforcement.

---

## Urgency & Scarcity

Three types. Each requires different implementation and psychology.

### 1. Real Scarcity (Inventory)

Only use if actually tracking inventory. False scarcity destroys brand trust.

```html
<div class="inline-flex items-center gap-2 px-4 py-2 rounded" style="background:#fff3cd;color:#856404">
  <span class="font-semibold">⚠️ Only 7 left in stock</span>
</div>
<div data-island="InventoryIndicator" data-props='{"threshold":10,"lowStockMessage":"Only {count} left in stock","outOfStockMessage":"Sold out — join waitlist"}'></div>
```

**When to use:** High-demand products, limited editions, seasonal items.

### 2. Deadline (Countdown)

Time-limited offers. Must have real expiration.

```html
<div class="sticky top-0 z-50 py-3 px-4 text-center text-white font-semibold text-sm" style="background:#c9302c">
  🔥 Summer Sale: 30% Off Ends in
  <div data-island="CountdownTimer" data-props='{"endDate":"2026-06-30T23:59:59Z","message":"","urgencyThreshold":3600}'></div>
  <a href="#shop" class="ml-4 underline">Shop Now</a>
</div>
```

**When to use:** Flash sales, product launches, abandoned cart recovery.

### 3. Exclusivity (Limited Access)

Member-only, waitlist, invite-only framing.

```html
<section class="py-20 px-4 text-center" style="background:var(--lx-bg-surface)">
  <div class="max-w-2xl mx-auto space-y-6">
    <h2 class="text-4xl font-bold" style="color:var(--lx-text-color)">Join the Waitlist</h2>
    <p class="text-lg opacity-80">Limited to 500 founding members. Next batch ships August 2026.</p>
    <div class="inline-block px-4 py-2 rounded-full text-sm font-semibold" style="background:#f0f0f0">
      127 spots remaining
    </div>
    <div data-island="EmailCapture" data-props='{"placeholder":"Enter your email","buttonText":"Reserve Your Spot"}'></div>
  </div>
</section>
```

**When to use:** Pre-launch, beta access, VIP tiers.

### Anti-Patterns (Fake Urgency)

| ❌ Don't | Why | ✅ Do |
|----------|-----|-------|
| Evergreen countdowns (timer resets on refresh) | Users notice, trust tanks | Use real sale end dates, or remove timer |
| "Only 2 left!" for digital products | Obvious lie | Use enrollment caps ("Only 50 spots in this cohort") |
| "Sale ends tonight" every night | Cried wolf effect | Run real weekly/monthly sales with calendar |
| SocialProofPopup with fake names | "John from New York just bought" on loop | Only use if pulling real order events from API |

---

## Cognitive Load Management

Max 3 choices per section. More options = decision paralysis = abandonment.

### Feature Grid (3 features, not 7)

**Good (3 features):**
```html
<section class="py-16 px-4">
  <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
    <div class="text-center space-y-4">
      <span class="text-5xl">⚡</span>
      <h3 class="text-xl font-bold">Fast Results</h3>
      <p class="opacity-80">See improvements in 7 days or less</p>
    </div>
    <div class="text-center space-y-4">
      <span class="text-5xl">🛡️</span>
      <h3 class="text-xl font-bold">Risk-Free</h3>
      <p class="opacity-80">60-day money-back guarantee</p>
    </div>
    <div class="text-center space-y-4">
      <span class="text-5xl">❤️</span>
      <h3 class="text-xl font-bold">Love It</h3>
      <p class="opacity-80">Join 47,000+ happy customers</p>
    </div>
  </div>
</section>
```

**If you have 6+ features:** Split into 2 sections (benefits vs. technical specs).

### CompareTable (3 columns max, 5-8 rows)

```html
<div data-island="CompareTable" data-props='{"columns":[{"name":"Competitor A","highlight":false},{"name":"You","highlight":true},{"name":"Competitor B","highlight":false}],"rows":[{"feature":"Feature 1","values":["❌","✅","❌"]},{"feature":"Feature 2","values":["✅","✅","❌"]},{"feature":"Feature 3","values":["❌","✅","✅"]}]}'></div>
```

### Progressive Disclosure (Tabs/FAQ)

Use islands for deep info. Don't dump paragraphs.

```html
<div data-island="Tabs" data-props='{"tabs":[{"label":"How It Works","content":"..."},{"label":"Ingredients","content":"..."},{"label":"Shipping","content":"..."}]}'></div>
<div data-island="FAQ" data-props='{"items":[{"question":"How long does shipping take?","answer":"2-3 business days."}]}'></div>
```

---

## Trust Escalation Ladder

Move visitors from low-commitment → high-commitment actions. Don't ask for the sale immediately.

### Sequence:

1. **Browse encouragement** (no commitment)
   - Hero: "Explore our collection"
   - Value props: "See why 47,000+ customers love us"

2. **Email capture** (small commitment)
   - Offer: "Get 10% off your first order"
   - Placement: Section 3-5
   - `data-island="EmailCapture"`

3. **Cart confidence** (medium commitment)
   - `data-island="BuyBox"` with "Add to Cart"
   - Show: trust badges, free shipping, easy returns

4. **Purchase trigger** (high commitment)
   - Final CTA: "Complete your order"
   - Add: `data-island="CountdownTimer"` or `data-island="InventoryIndicator"`
   - Show: risk reversal (guarantee)

---

## CTA Psychology

Button copy is conversion science. Every word matters.

### First-Person Labels

**Bad (second-person):**
- "Get Started"
- "Buy Now"
- "Download the Guide"

**Good (first-person):**
- "Start MY Free Trial"
- "Add to MY Cart"
- "Send ME the Guide"

**Why it works:** First-person creates ownership before purchase.

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Start MY Transformation
</button>
```

### Benefit-Driven Copy

**Bad (action-only):**
- "Submit"
- "Continue"
- "Next"

**Good (action + benefit):**
- "Get My Discount"
- "Unlock Free Shipping"
- "Claim My Spot"

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Claim My 30% Off
</button>
```

### Contrast Principle

CTA button must have 4.5:1 contrast ratio against background (WCAG AA). Use high-chroma colors.

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg shadow-lg transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white;box-shadow:0 4px 12px rgba(102,126,234,0.4)">
  Add to Cart
</button>
```

**Color pairs (high contrast):**
- Blue CTA on white: `#667eea` / `#ffffff`
- Red CTA on dark: `#c9302c` / `#1a1a1a`
- Green CTA on light: `#28a745` / `#f9fafb`

### Button Hierarchy

**Primary (main action):**
```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Buy Now — $89
</button>
```

**Secondary (alternative action):**
```html
<button class="px-6 py-3 rounded-lg" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
  Learn More
</button>
```

**Ghost (low-commitment):**
```html
<button class="px-6 py-3 rounded-lg hover:bg-opacity-10" style="color:var(--lx-accent-color)">
  View Details
</button>
```

**Link (minimal friction):**
```html
<a href="#learn-more" class="underline" style="color:var(--lx-accent-color)">
  Learn More
</a>
```

### Dual CTA (high + low commitment)

Offer high-commitment + low-commitment options.

```html
<div class="flex gap-4 justify-center">
  <button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
    Buy Now — $89
  </button>
  <button class="px-6 py-3 rounded-lg" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
    Learn More
  </button>
</div>
```

**When to use:** High-ticket products ($300+), complex products needing education.

---

## Visual Hierarchy for Conversion

Eye-flow patterns direct attention to CTAs.

### Focal Points (element styles)

Use scale, color, and whitespace to create hierarchy.

**Headline (most important):**
```html
<h1 class="text-5xl md:text-7xl font-extrabold leading-tight mb-4" style="color:var(--lx-text-color)">
  Transform Your Skin in 30 Days
</h1>
```

**Subline (secondary):**
```html
<p class="text-xl md:text-2xl leading-relaxed mb-8" style="color:var(--lx-text-muted)">
  Clinically proven formula with visible results in just 2 weeks
</p>
```

**CTA (action):**
```html
<button class="px-10 py-5 text-xl font-bold rounded-lg shadow-2xl transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white;box-shadow:0 8px 24px rgba(102,126,234,0.5)">
  Get Started
</button>
```

### Whitespace for Emphasis

Surround CTAs with empty space (min 2rem padding).

```html
<section class="py-20 px-4">
  <!-- CTA content -->
</section>
```

---

## Anti-Patterns (Conversion Killers)

| ❌ | Why | ✅ |
|----|-----|-----|
| Generic headlines ("Welcome to Our Store") | No hook, no benefit | "Get [Specific Benefit] in [Timeframe]" |
| Hidden prices ("Contact for Pricing") | Friction, distrust | Show price upfront (even if high) |
| Walls of text (5-paragraph descriptions) | Cognitive overload | Bullet points, max 3 benefits |
| Too many CTAs (3+ above fold) | Decision paralysis | 1 primary CTA, 1 optional secondary |
| Tiny mobile buttons (40px tap target) | Poor UX, missed clicks | 48px minimum (py-3 or py-4) |
| Auto-playing video with sound | Annoys users | Muted autoplay, click to unmute |
| No trust signals above fold | Credibility gap | Add star rating or customer count near CTA |
| Fake urgency (evergreen countdown) | Trust erosion | Real sale end dates or remove timer |
| Cluttered forms (8-field email capture) | Abandonment | Email only with `data-island="EmailCapture"` |
| Slow load times (5+ second hero load) | Bounce rate spike | Optimize images, lazy-load below fold |
| No mobile optimization (desktop-only) | Poor mobile UX | Responsive spacing, clamp() font sizes |
| Unclear value prop ("We're the best") | Generic, meaningless | "Save 10 hours/week with automated [task]" |
| No risk reversal (no guarantee) | Fear of loss | Risk reversal section before final CTA |
| Dead-end pages (no next step) | Lost momentum | Every section ends with CTA or link |
| Inconsistent branding (5 button styles) | Unprofessional | Consistent colors via CSS vars |

---

## Complete Page Recipes

### Recipe 1: Lead Gen (Email Capture)

**Goal:** Maximize email signups for nurture sequence.

**VibePage structure (abbreviated):**
```json
{
  "head": {
    "title": "Get the Ultimate Skincare Guide",
    "fonts": ["https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap"]
  },
  "theme_css": ":root { --lx-accent-color: #667eea; --lx-text-color: #1a1a1a; --lx-bg-color: #ffffff; --lx-bg-surface: #f9fafb; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class='py-20 px-4 text-center' style='background:linear-gradient(135deg, #667eea 0%, #764ba2 100%)'><div class='max-w-3xl mx-auto space-y-6'><h1 class='text-5xl md:text-6xl font-extrabold text-white'>Get the Flawless Skin Guide</h1><p class='text-xl text-white/90'>Learn how to achieve radiant skin in 30 days. Free download.</p><div data-island='EmailCapture' data-props='{\"placeholder\":\"Enter your email\",\"buttonText\":\"Send Me the Guide\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "value-props",
      "html": "<section class='py-16 px-4'><div class='grid md:grid-cols-3 gap-8 max-w-5xl mx-auto'><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>Science-Backed Methods</h3><p class='opacity-80'>Proven techniques from dermatologists</p></div><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>Natural Ingredients</h3><p class='opacity-80'>No harsh chemicals or side effects</p></div><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>30-Day Results</h3><p class='opacity-80'>See visible improvements in one month</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "stats",
      "html": "<section class='py-12 px-4' style='background:var(--lx-bg-surface)'><div class='grid grid-cols-2 gap-8 max-w-4xl mx-auto text-center'><div><p class='text-5xl font-extrabold' style='color:var(--lx-accent-color)'>47,000+</p><p class='text-sm uppercase mt-2 opacity-70'>Downloads</p></div><div><p class='text-5xl font-extrabold' style='color:var(--lx-accent-color)'>4.9/5</p><p class='text-sm uppercase mt-2 opacity-70'>Rating</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta",
      "html": "<section class='py-20 px-4 text-center'><div class='max-w-2xl mx-auto space-y-6'><h2 class='text-4xl font-bold' style='color:var(--lx-text-color)'>Ready to Get Started?</h2><div data-island='EmailCapture' data-props='{\"placeholder\":\"Enter your email\",\"buttonText\":\"Download Now — It\\'s Free\"}'></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

### Recipe 2: Direct Purchase (Low-ticket <$100)

**Goal:** Impulse buy, minimal friction.

**VibePage structure (abbreviated):**
```json
{
  "sections": [
    {
      "id": "hero",
      "html": "<section class='grid md:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 py-8'><div><img src='/product.jpg' class='w-full rounded-lg'/></div><div class='flex flex-col justify-center space-y-6'><h1 class='text-5xl font-bold' style='color:var(--lx-text-color)'>Premium Serum</h1><p class='text-xl opacity-80'>Transform your skin in 30 days</p><div class='flex items-baseline gap-3'><span class='text-3xl font-bold' style='color:var(--lx-text-color)'>$79.99</span><span class='text-lg line-through opacity-40'>$119.99</span><span class='text-xs font-semibold px-2 py-1 rounded-full text-white' style='background:var(--lx-accent-color)'>33% OFF</span></div><div data-island='BuyBox' data-props='{\"productId\":\"gid://shopify/Product/123\",\"ctaText\":\"Add to Cart — Free Shipping\"}'></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

### Recipe 3: High-AOV ($500+)

**Goal:** Build trust for expensive purchase.

**VibePage structure (abbreviated):**
```json
{
  "sections": [
    {
      "id": "hero",
      "html": "<section class='relative min-h-screen flex items-center justify-center px-4' style='background:url(/hero.jpg) center/cover'><div class='max-w-3xl text-center space-y-6 text-white'><h1 class='text-6xl font-extrabold'>Enterprise CRM Platform</h1><p class='text-2xl'>Trusted by Fortune 500 companies</p><button class='px-8 py-4 text-lg font-bold rounded-lg' style='background:white;color:var(--lx-accent-color)'>Schedule a Demo</button></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "logos",
      "html": "<section class='py-12 px-4' style='background:var(--lx-bg-surface)'><p class='text-center text-sm uppercase tracking-wide mb-8 opacity-70'>Trusted by Industry Leaders</p><div class='flex justify-center gap-12 flex-wrap'><img src='/logos/company1.svg' class='h-10 opacity-60'/><img src='/logos/company2.svg' class='h-10 opacity-60'/><img src='/logos/company3.svg' class='h-10 opacity-60'/></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

**End of conversion-psychology.md**
