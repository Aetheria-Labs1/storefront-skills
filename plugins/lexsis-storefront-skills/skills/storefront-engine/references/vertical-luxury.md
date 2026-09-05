# High-AOV Luxury & Jewelry — Storefront Design Intelligence

> **When to load**: Luxury goods, fine jewelry, watches, premium accessories, AOV > $300.

## Philosophy

**RESTRAINT IS EVERYTHING.** Luxury pages sell through what they DON'T do.

No urgency. No aggressive CTAs. No discounts. No visual noise. The page is a museum, not a marketplace. The product is art, not inventory. Whitespace = premium. 6-8 sections maximum.

Every element earns its space through the negative space around it. Stillness = contemplation = luxury.

---

## Section Sequences

### Single Hero Product (6-8 sections MAX)

One flagship piece. Museum-like focus. No distractions.

```
1. Hero (cinematic, dark) — product on black pedestal
2. Parallax (editorial) — craftsmanship story
3. Gallery (detail shots) — macro photography
4. Features (2-3 only) — material provenance
5. Testimonial (ONE quote) — press or notable
6. Whisper CTA — "Inquire" or "Discover"
```

**Why 6-8?** More than 8 = catalog browsing. Luxury is focus.

### Collection (8-10 sections)

Showcases breadth without overwhelming.

```
1. Hero — collection name as headline
2. Parallax — brand story
3. Lookbook grid — 6-8 pieces, asymmetric
4. Feature grid — individual callouts
5. Parallax — heritage
6. Press mentions — grayscale logos
7. Newsletter — exclusive access
8. Whisper CTA
```

### Gifting / Occasion (6-8 sections)

Thoughtful, not transactional.

```
1. Hero — lifestyle, occasion-driven
2. Parallax — gift philosophy
3. Lookbook grid — 4-6 gift pieces
4. Features — services (wrapping, engraving)
5. Testimonial — gifting experience
6. Newsletter — gift concierge
7. Whisper CTA
```

**No urgency.** "Last-minute gifts" destroys luxury positioning. If there's a shipping deadline, mention once in footer—never as primary messaging.

---

## Island Combinations

Luxury uses **minimal islands**, selected for refinement, not utility.

### Essential Islands

**ProductGallery** — cinematic, 4-6 large images, dark backgrounds, dramatic lighting, zoom_on_hover: false, lightbox: true

**ImageZoom** — detail shots of craftsmanship (clasp, stone setting, engraving, leather stitching), macro photography

**VideoPlayer** — brand film (NOT product demo), atelier footage, heritage story, autoplay: false

**BuyBox** — show_inventory: false, show_sku: false, urgency_indicators: false, cta_text: "Add to Bag" (never "Cart")

**EmailCapture** — "Join our circle" or "Receive early access", single field (email only), placed late (section 6+), never discount-incentivized

### Islands Luxury NEVER Uses

- **CountdownTimer** — urgency destroys premium positioning
- **QuantityBreaks** — volume discounts = mass market
- **CompareTable** — comparison shopping = commoditization
- **StickyBar** with "Add to Cart" — aggressive, pushy
- **ReviewCarousel** (star ratings) — see Social Proof section

---

## Typography & Color

### Typography

Typography is the voice of the page. Luxury speaks softly.

**Hero Headlines:**
```css
font-size: clamp(36px, 5vw, 64px);  /* NOT oversized */
font-weight: 300-400;  /* Ultra-light to light */
letter-spacing: 0;  /* Tight, not expanded */
line-height: 1.1;
font-family: serif (Cormorant, Lora, Playfair) or elegant sans (Futura, Montserrat Light);
text-transform: none;  /* Sentence case, not ALL CAPS */
```

**Why 64px max?** Oversized headlines (80px+) scream "look at me"—the opposite of luxury restraint.

**Eyebrows (ONLY place uppercase is acceptable):**
```css
font-size: 11px-13px;
font-weight: 500;
letter-spacing: 0.1em-0.2em;  /* Generous tracking */
text-transform: uppercase;
color: rgba(255,255,255,0.6) or rgba(0,0,0,0.5);  /* Subdued */
```

Use for: material name ("18K GOLD"), collection name ("THE ETERNAL COLLECTION"), artisan credit ("HANDCRAFTED IN FLORENCE").

**Body:**
```css
font-size: 16px-18px;
font-weight: 400;
line-height: 1.7-1.8;  /* Everything breathes */
max-width: 600px;  /* Readable line length */
```

**One sentence sublines. Two maximum.** If you need a third, the copy is too verbose.

### Color

Luxury color palettes are **binary**: deep darks OR pure whites. Nothing in between.

**Dark Luxury (jewelry, watches):**
- Primary: `#0a0a0a` (near-black, NOT pure black—pure black = digital)
- Text: `#ffffff` headlines, `rgba(255,255,255,0.8)` body
- Accent (10% rule): Gold `#d4af37`, Cream `#f4f1ea`, Rose gold `#e0bfb8`

**Light Luxury (fashion, accessories):**
- Primary: `#ffffff`, `#fafafa`
- Text: `#0a0a0a` headlines, `rgba(0,0,0,0.8)` body
- Accent: Charcoal `#2a2a2a`

**Where to use accent:** Thin borders, icons, CTA hover states. **Where NOT to use:** Section backgrounds, large text blocks, multiple buttons.

**NEVER for luxury:** Gradients, colored section backgrounds (blue/green/purple), image backgrounds with text overlay (except hero with dark overlay), patterns/textures.

---

## Hero Patterns

### Cinematic Product Hero (Dark)

```html
<section class="relative min-h-[90vh] flex items-center justify-center bg-[#0a0a0a]">
  <div class="max-w-4xl mx-auto text-center space-y-8 px-6">
    <p class="text-[11px] uppercase tracking-[0.25em] font-medium text-[var(--lx-accent-color)]">
      Handcrafted in Italy
    </p>
    <h1 class="text-[clamp(2.5rem,5vw,4rem)] font-light leading-[1.1] text-white" style="font-family:var(--lx-font-heading);letter-spacing:-0.01em">
      Eternal
    </h1>
    <img src="IMAGE_URL" alt="Ring detail" class="mx-auto max-w-md w-full" />
    <a href="#discover" class="inline-block text-sm tracking-wider border-b pb-1 transition-opacity hover:opacity-70 text-[var(--lx-accent-color)]" style="border-color:var(--lx-accent-color)">
      Discover
    </a>
  </div>
</section>
```

### Editorial Split (Light Variant)

```html
<section class="relative min-h-[70vh] bg-white">
  <div class="container mx-auto px-6 grid md:grid-cols-2 gap-16 items-center">
    <img src="IMAGE_URL" alt="Atelier" class="w-full h-full object-cover" />
    <div class="space-y-6 max-w-xl">
      <p class="text-[11px] uppercase tracking-[0.2em] font-medium text-black/50">
        Since 1847
      </p>
      <h2 class="text-[clamp(1.75rem,3vw,2.25rem)] font-light leading-[1.2] text-[#0a0a0a]" style="font-family:var(--lx-font-heading)">
        Crafted by Hand
      </h2>
      <p class="text-base leading-[1.8] text-black/80">
        Each setting is executed by master jewelers in our Florence atelier.
      </p>
    </div>
  </div>
</section>
```

---

## Craftsmanship Story Section

```html
<section class="relative min-h-[60vh] bg-[#0a0a0a] flex items-center py-32">
  <div class="container mx-auto px-6 grid md:grid-cols-[1fr,40%] gap-20 items-center">
    <img src="ATELIER_IMAGE_URL" alt="Workshop" class="w-full h-[500px] object-cover" />
    <div class="space-y-6">
      <h2 class="text-[clamp(1.75rem,3vw,2.25rem)] font-light leading-[1.2] text-white" style="font-family:var(--lx-font-heading)">
        A Legacy of Precision
      </h2>
      <p class="text-base leading-[1.8] text-white/80 max-w-[600px]">
        Born in the Vallée de Joux. Refined over 175 years. Five generations of master watchmakers.
      </p>
    </div>
  </div>
</section>
```

---

## Detail Gallery

ProductGallery + ImageZoom integration for macro shots:

```html
<section class="relative bg-white py-32">
  <div class="container mx-auto px-6">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
      <div class="aspect-square relative overflow-hidden group">
        <img src="DETAIL_1_URL" alt="Clasp mechanism" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
      </div>
      <div class="aspect-square relative overflow-hidden group">
        <img src="DETAIL_2_URL" alt="Stone setting" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
      </div>
      <div class="aspect-square relative overflow-hidden group">
        <img src="DETAIL_3_URL" alt="Engraving" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
      </div>
      <div class="aspect-square relative overflow-hidden group">
        <img src="DETAIL_4_URL" alt="Texture" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
      </div>
    </div>
  </div>
</section>
```

---

## Single Testimonial

One quote, centered, large serif. NOT carousel. Press attribution.

```html
<section class="relative bg-[#fafafa] py-32">
  <div class="container mx-auto px-6 max-w-3xl text-center">
    <blockquote class="space-y-8">
      <p class="text-[clamp(1.25rem,2.5vw,1.75rem)] font-light italic leading-[1.6] text-[#0a0a0a]" style="font-family:var(--lx-font-heading)">
        "A masterpiece of craftsmanship. The attention to detail is extraordinary."
      </p>
      <footer class="text-sm tracking-wider uppercase text-black/60">
        — Harper's Bazaar
      </footer>
    </blockquote>
  </div>
</section>
```

---

## Whisper CTA

Small ghost button, centered, generous whitespace around it.

```html
<section class="relative bg-[#0a0a0a] py-40">
  <div class="container mx-auto px-6 text-center">
    <a href="/inquire" class="inline-block px-8 py-3 text-sm tracking-wider border border-[var(--lx-accent-color)] text-[var(--lx-accent-color)] transition-opacity hover:opacity-70">
      Inquire
    </a>
  </div>
</section>
```

---

## What Luxury NEVER Has

Explicit forbidden list with reasoning:

1. **Countdown timers** — urgency = scarcity = mass market. Luxury is timeless.
2. **"Limited stock" warnings** — FOMO tactics cheapen the product.
3. **Discount/sale language** — "50% OFF" signals overstock or desperation.
4. **Urgency messaging** — "Order in the next 2 hours..." = pushy.
5. **Comparison tables** — cheapens product to feature checklist.
6. **Popup notifications** — "Sarah just bought this!" = aggressive.
7. **Bright accent colors** — blues/greens/oranges destroy premium feel.
8. **Emoji anywhere** — playful, not premium.
9. **Exclamation marks** — excitement is unbecoming.
10. **FOMO language** — "Don't miss out!", "Last chance!" = desperation.
11. **Multiple CTAs per section** — one CTA per section max. Focus, not choice overload.
12. **"Add to Cart"** — transactional. Use "Add to Bag" or "Inquire".

---

## Animation

**The luxury animation rule: ONE animated element maximum per entire page.**

Stillness = premium. Motion = distraction.

### Allowed Animation (hero only)

```json
{
  "settings": {
    "animation": {
      "preset": "fade_in",
      "speed": "slow",
      "trigger": "load"
    }
  }
}
```

The hero fades in slowly (1.5s duration). That's it. No other animations anywhere.

### Forbidden Animations

- **slide_up** — feels like PowerPoint
- **zoom_in** — too aggressive
- **bounce** — playful, not premium
- **Multiple animations** — one per page is already generous

**Hover States:** Fade opacity 100% → 80% (subtle). NO scale transforms, NO shadows appearing, NO color shifts.

---

## Price Presentation

Price is **never hidden**, but **never emphasized**.

### Where Price Appears

**BuyBox:**
- Below product name
- Font size: 16-18px (same as body text)
- Font weight: 400 (not bold)
- Color: same as body text
- No `compare_at_price` / crossed-out pricing
- No "Save $X" or "X% OFF"

**Payment Options:**
- ✅ "Four interest-free payments of $300 available"
- ✅ "Flexible payment options available"
- ❌ "Or 4 payments of $300 with Afterpay!" (too promotional)

**Shipping:**
- ✅ "Complimentary shipping"
- ✅ "Complimentary gift wrapping"
- ❌ "FREE SHIPPING" (all caps = promotional)

### What Luxury Price Presentation NEVER Does

- `compare_at_price` ($1,200 ~~$2,000~~)
- "Save $800" messaging
- Large, bold price (24px+, bold weight, accent color)
- Price in hero headline
- Countdown next to price

### High-AOV Nuance (>$5k)

- Consider "Inquire for pricing" instead of displayed price
- Offer "Schedule a private viewing" CTA
- Payment plans: "Flexible financing available" (not "Buy now, pay later")

For $300-$5k:
- Display price (transparency expected)
- Installment options okay (but subdued)
- "Add to Bag" CTA acceptable

---

## Anti-Patterns

Twelve specific mistakes that destroy luxury positioning:

### 1. Urgency/Scarcity Messaging

**The mistake:** "Only 3 left!", "Sale ends tonight!", countdown timers.

**Why it kills luxury:** Urgency implies the product might not sell otherwise—the opposite of desirability.

**The fix:** Remove all urgency. If stock is genuinely limited, frame as "Singular piece" or "Edition of one"—exclusivity, not scarcity.

### 2. Loud Primary CTA Buttons

**The mistake:** Bright blue "BUY NOW" button, large, repeated every section.

**Why it kills luxury:** Aggressive CTAs feel pushy. Luxury sells itself—the page invites, doesn't push.

**The fix:** Ghost or outline buttons. Small. Text: "Discover" or "Inquire". One CTA per page.

### 3. Too Many Sections (>8)

**The mistake:** 12+ sections trying to communicate everything.

**Why it kills luxury:** Scroll fatigue. Luxury is about focus, not exhaustive information.

**The fix:** 6-8 sections maximum. Each section earns its place.

### 4. Corporate Sans-Serif Typography

**The mistake:** Helvetica, Arial, default system fonts. Bold weights (600-700).

**Why it kills luxury:** Corporate sans = tech company, not fine goods. Bold = shouting.

**The fix:** Elegant serif (Cormorant, Lora, Playfair) or refined sans (Futura, Montserrat Light). Weights 300-400. Never bold.

### 5. Equal-Column Grids

**The mistake:** Two-column layout, equal-width, symmetrical.

**Why it kills luxury:** Symmetry = catalog = functional, not editorial.

**The fix:** Asymmetric layouts. 60/40 splits. Varied tile sizes.

### 6. Stock Photography

**The mistake:** Generic lifestyle photos (smiling models, bright backgrounds).

**Why it kills luxury:** Recognizable stock = low budget = not premium.

**The fix:** Custom photography or highly curated stock (dark backgrounds, dramatic lighting, product-focused).

### 7. Small Product Images

**The mistake:** Product images <50% viewport width.

**Why it kills luxury:** The product should dominate. Small images = commodity.

**The fix:** Hero image full-bleed or 80%+ viewport. Gallery images large (40-50% each).

### 8. Discount-First Messaging

**The mistake:** Hero headline: "50% Off Sitewide", crossed-out prices.

**Why it kills luxury:** Discounts signal overstock or desperation.

**The fix:** Price is presented but never emphasized. No `compare_at_price`. No "Save $X".

### 9. Heavy Animation

**The mistake:** Every section slides up on scroll. Hero zooms. Buttons bounce.

**Why it kills luxury:** Motion = excitement = youth brands. Luxury = stillness = contemplation.

**The fix:** One fade-in on hero, speed: slow. Everything else static.

### 10. Colored Section Backgrounds

**The mistake:** Alternating sections with colored backgrounds (blue, green, purple).

**Why it kills luxury:** Colored backgrounds = playful, tech-y, consumer-y.

**The fix:** Dark (#0a0a0a) or white (#ffffff). Nothing in between.

### 11. Paragraph-Length Descriptions

**The mistake:** Three paragraphs of body text.

**Why it kills luxury:** Walls of text = instruction manual, not narrative.

**The fix:** One sentence sublines. Two maximum.

### 12. "Add to Cart" Language

**The mistake:** CTA text: "Add to Cart", "Buy Now", "Shop Now".

**Why it kills luxury:** Transactional language. "Cart" = grocery shopping.

**The fix:** "Add to Bag" ($300-2k). "Inquire" (>$5k). "Discover", "Explore" (non-transactional).

---

## Complete Blueprint

Full VibePage JSON for 6-section jewelry page:

```json
{
  "head": {
    "title": "Eternal Beauty — Fine Jewelry",
    "description": "Handcrafted by master artisans. A piece to treasure for generations.",
    "og_image": "HERO_IMAGE_URL"
  },
  "theme_css": ":root { --lx-accent-color: #d4af37; --lx-text-color: #0a0a0a; --lx-text-muted: rgba(0,0,0,0.6); --lx-bg-color: #ffffff; --lx-bg-surface: #fafafa; --lx-border-color: rgba(0,0,0,0.1); --lx-font-heading: 'Cormorant Garamond', serif; --lx-font-body: 'Inter', sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[90vh] flex items-center justify-center bg-[#0a0a0a]\"><div class=\"max-w-4xl mx-auto text-center space-y-8 px-6\"><p class=\"text-[11px] uppercase tracking-[0.25em] font-medium\" style=\"color:var(--lx-accent-color)\">Handcrafted in Italy</p><h1 class=\"text-[clamp(2.5rem,5vw,4rem)] font-light leading-[1.1] text-white\" style=\"font-family:var(--lx-font-heading);letter-spacing:-0.01em\">Eternal Beauty</h1><img src=\"HERO_IMAGE_URL\" alt=\"Ring on black pedestal\" class=\"mx-auto max-w-md w-full\" /><a href=\"#discover\" class=\"inline-block text-sm tracking-wider border-b pb-1 transition-opacity hover:opacity-70\" style=\"color:var(--lx-accent-color);border-color:var(--lx-accent-color)\">Discover</a></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "craftsmanship",
      "html": "<section class=\"relative bg-white py-32\"><div class=\"container mx-auto px-6 grid md:grid-cols-[1fr,40%] gap-20 items-center\"><img src=\"ATELIER_IMAGE_URL\" alt=\"Atelier\" class=\"w-full h-[500px] object-cover\" /><div class=\"space-y-6\"><p class=\"text-[11px] uppercase tracking-[0.2em] font-medium text-black/50\">Since 1847</p><h2 class=\"text-[clamp(1.75rem,3vw,2.25rem)] font-light leading-[1.2] text-[#0a0a0a]\" style=\"font-family:var(--lx-font-heading)\">Crafted by Hand</h2><p class=\"text-base leading-[1.8] text-black/80 max-w-[600px]\">Each setting is executed by master jewelers in our Florence atelier.</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "gallery",
      "html": "<section class=\"relative bg-white py-32\"><div class=\"container mx-auto px-6\"><div class=\"grid grid-cols-2 md:grid-cols-4 gap-4\"><div class=\"aspect-square relative overflow-hidden group\"><img src=\"DETAIL_1_URL\" alt=\"Clasp mechanism\" class=\"w-full h-full object-cover transition-transform duration-500 group-hover:scale-105\" /></div><div class=\"aspect-square relative overflow-hidden group\"><img src=\"DETAIL_2_URL\" alt=\"Stone setting\" class=\"w-full h-full object-cover transition-transform duration-500 group-hover:scale-105\" /></div><div class=\"aspect-square relative overflow-hidden group\"><img src=\"DETAIL_3_URL\" alt=\"Engraving\" class=\"w-full h-full object-cover transition-transform duration-500 group-hover:scale-105\" /></div><div class=\"aspect-square relative overflow-hidden group\"><img src=\"DETAIL_4_URL\" alt=\"Texture\" class=\"w-full h-full object-cover transition-transform duration-500 group-hover:scale-105\" /></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "features",
      "html": "<section class=\"relative bg-[#0a0a0a] py-32\"><div class=\"container mx-auto px-6 max-w-4xl\"><div class=\"grid md:grid-cols-2 gap-16 text-center\"><div class=\"space-y-4\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\" d=\"M5 13l4 4L19 7\"></path></svg><h3 class=\"text-sm uppercase tracking-wider font-medium text-white\">Ethically Sourced</h3><p class=\"text-sm text-white/70\">Materials selected for origin and quality</p></div><div class=\"space-y-4\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\" d=\"M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z\"></path></svg><h3 class=\"text-sm uppercase tracking-wider font-medium text-white\">Lifetime Warranty</h3><p class=\"text-sm text-white/70\">Complimentary service and care</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "testimonial",
      "html": "<section class=\"relative bg-[#fafafa] py-32\"><div class=\"container mx-auto px-6 max-w-3xl text-center\"><blockquote class=\"space-y-8\"><p class=\"text-[clamp(1.25rem,2.5vw,1.75rem)] font-light italic leading-[1.6] text-[#0a0a0a]\" style=\"font-family:var(--lx-font-heading)\">A masterpiece of craftsmanship. The attention to detail is extraordinary.</p><footer class=\"text-sm tracking-wider uppercase text-black/60\">— Harper's Bazaar</footer></blockquote></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta",
      "html": "<section class=\"relative bg-[#0a0a0a] py-40\"><div class=\"container mx-auto px-6 text-center\"><a href=\"/inquire\" class=\"inline-block px-8 py-3 text-sm tracking-wider border transition-opacity hover:opacity-70\" style=\"border-color:var(--lx-accent-color);color:var(--lx-accent-color)\">Inquire</a></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

**Final thought:** When in doubt, remove. Luxury is bought, not sold. The page's job is to be a gallery. The product's job is to be art. Your job is to not get in the way.
