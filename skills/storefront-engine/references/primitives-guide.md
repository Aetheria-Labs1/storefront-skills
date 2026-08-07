# Composable Primitives Guide

## Three-Tier System

### Tier 1: Behaviors (`data-behavior="..."`, zero React overhead)

Use for UI that needs ONLY class/attribute toggling — no React rendering.

| Behavior | Purpose | Config |
|----------|---------|--------|
| `scroll-reveal` | Fade/slide elements on scroll into view | `threshold`, `rootMargin`, `once`, `stagger` |
| `accordion` | Expand/collapse panels | `mode: "single"\|"multiple"`, `defaultOpen: number[]` |
| `horizontal-scroll` | Arrow-navigated horizontal scroller | `scrollerSelector`, `scrollAmount` |
| `sticky-reveal` | Show/hide on scroll threshold | `threshold`, `position`, `hideDirection` |
| `variant-select` | Headless variant picking → emits scoped events | `variants[]`, `productId` |

**Data attributes set by behaviors** (target with section CSS):
- `scroll-reveal` → `[data-visible="true"]`
- `accordion` → `[aria-expanded="true"]`, `[data-state="open|closed"]`
- `horizontal-scroll` → `[data-can-scroll-left]`, `[data-can-scroll-right]`
- `sticky-reveal` → `[data-sticky="true"]`, `[data-hidden="true"]`
- `variant-select` → `[data-selected="true"]` on option buttons

### Tier 2: Primitive Islands (`data-island="..."`, lightweight React)

| Island | Purpose | Key Props |
|--------|---------|-----------|
| **MediaCarousel** | Image/video cycling | `media[]`, `transition`, `autoplay`, `hoverAdvance`, `showArrows`, `showDots`, `aspect` |
| **HeroMedia** | Full-bleed hero background (image/carousel/video + effects) | `type`, `src`, `slides[]`, `videoSrc`, `effect`, `overlay`, `overlayColor`, `minHeight` |
| **QuickAdd** | Add-to-cart button | `product`, `render: "button"\|"icon"\|"minimal"\|"custom-trigger"`, `iconSize` |
| **Countdown** | Countdown timer | `endDate`, `style: "simple"\|"flip"\|"circular"\|"headless"`, `expiredAction` |
| **VariantSelector** | Visual variant picker | `product`, `render: "swatches"\|"dropdown"\|"buttons"` |

### Tier 3: Composite Islands (keep as-is, full React)

BuyBox, CartDrawer, CartLines, CartSummary, CartCheckoutButton, CartProgressBar, CartDiscountInput, CartCrossSell, BundleBuilder, ProductCarousel, ProductGallery, ProductHero, ReviewCarousel, VideoPlayer, EmailCapture, SocialProofPopup, MobileMenu, Modal, DrawerShell, Navbar, Footer, SiteHeader, AnnouncementBar.

---

## Rules for New Pages

1. **NEVER use deprecated islands**: ProductCard, EditorialProductGrid, CompareTable, PDPInfoCards, TrustBadgeBar, Tabs
2. **Product grids/carousels**: custom HTML cards + `MediaCarousel` + `QuickAdd(render:"icon")`
3. **Accordions/FAQs**: `data-behavior="accordion"` — NOT the FAQ island
4. **Scroll animations**: `data-behavior="scroll-reveal"` with `[data-visible]` CSS transitions
5. **Multi-product sections**: wrap each card in `data-scope="product:{{handle}}"` to isolate events
6. **Below-fold islands**: set `data-hydrate="visible"`
7. **Hover-triggered islands** (QuickAdd in grids): set `data-hydrate="interaction"`
8. **Trust badges/comparison tables**: plain HTML — no island needed
9. **Horizontal scrolling**: `data-behavior="horizontal-scroll"` wrapping a flex container

---

## Hydration Strategy Guide

| Island Context | Strategy |
|----------------|----------|
| Navbar, SiteHeader, Footer | `immediate` (default, omit attr) |
| CartDrawer, Cart* islands | `idle` |
| BuyBox, ProductHero, HeroMedia (above fold) | `immediate` |
| MediaCarousel in product grids | `visible` |
| QuickAdd in product grids | `interaction` |
| ReviewCarousel, SocialProofPopup | `visible` |
| CountdownTimer | `immediate` (urgency element) |
| VariantSelector on PDP | `immediate` |
| VariantSelector in grid cards | `interaction` |

---

## Scoped Events

When multiple products exist on a page, use `data-scope` to prevent event collisions:

```html
<div data-scope="product:wireless-headphones">
  <!-- VariantSelector emits scoped variant:changed -->
  <!-- QuickAdd listens to scoped variant:changed for correct variant -->
</div>
```

Without scope: `variant:changed` from one product updates ALL listeners on page.
