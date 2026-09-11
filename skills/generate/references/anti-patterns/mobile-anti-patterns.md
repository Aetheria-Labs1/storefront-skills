# Mobile anti-patterns

Failures that appear only, or mostly, on a phone. `/design-page` runs these
in the hosted review at 390 x 844 (canonical) and spot-checks 320, 375 and
430 wide; `/generate` repeats them in production QA. Baymard's mobile
research (20,000+ hours of mobile-only testing) frames three root
constraints: slow, error-prone touch typing; loss of page overview (the
keyboard takes about half of a portrait viewport); and no hover state.
https://baymard.com/research/mcommerce-usability ; https://baymard.com/blog/mobile-checkout

Design-rules A8 (price and add-to-cart within 1.5 viewports at 390) and A11
(48 px targets, focus, reduced motion) are house rules; the MA rules below
add the checks around them. Severity BLOCK, FAIL, WARN. Tag LAW, RESEARCH,
OPERATOR, HEURISTIC. Checks use persisted MCP source and the hosted draft.

## 1. Viewport set and budgets

| Viewport | Use |
|---|---|
| 390 x 844 (iPhone 12 to 15 class) | canonical mobile screenshot; all pixel thresholds below refer to it |
| 375 x 667 | small-phone overflow and fixed-height stress test |
| 320 x 568 | horizontal-overflow floor |
| 430 x 932 | large-phone layout check |

Fixed-element budget at 390 x 844 (RESEARCH: Baymard mobile header findings; NN/g overlay overload):

| Region | Allowed elements | Height cap | Notes |
|---|---|---|---|
| Top | announcement bar + header | 15 percent of viewport (126 px); header alone at most 64 px, announcement at most 40 px and collapses on scroll | one top region |
| Bottom | sticky CTA bar OR consent sheet, never both at once | sticky CTA at most 72 px; consent sheet at most 25 percent (211 px) | chat launcher counts against this region |
| Total fixed | all `position: fixed` or `sticky` elements visible at once | 30 percent of viewport (253 px); at most 3 elements | measured at every scroll position sampled |

## 2. Layout and text

| Id | Anti-pattern | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| MA1 | Horizontal page scroll; element wider than the viewport | Nothing wider than 100vw at 320 to 430. Tables scroll inside their own container. | FAIL | RESEARCH |
| MA2 | Body text under 16 px; captions under 13 px; anything under 12 px | Body `p, li` at least 16 px; captions at least 13 px. Shopify Theme Store: 4.5:1 body contrast, 3:1 at 18 pt and above. https://shopify.dev/docs/storefronts/themes/store/requirements | FAIL | RESEARCH, LAW |
| MA3 | Inputs zoom on focus (iOS); zoom disabled | Inputs, selects, textareas and buttons at least 16 px computed. Never `maximum-scale=1` or `user-scalable=no` (WCAG 1.4.4; Shopify accessibility guidance). https://css-tricks.com/16px-or-larger-text-prevents-ios-form-zoom/ ; https://shopify.dev/docs/storefronts/themes/best-practices/accessibility | FAIL | LAW, RESEARCH |
| MA4 | Fixed header taller than 15 percent of the viewport | Top fixed region at most 126 px at 844; announcement collapses after the first scroll. | FAIL | RESEARCH |
| MA5 | Stacked fixed elements (announcement + header + sticky CTA + consent + chat) | One top region, one bottom region, total at most 30 percent, at most 3 elements. Consent and sticky CTA never coexist; chat launcher hides while the sticky CTA shows. | FAIL | RESEARCH |
| MA6 | Images not sized for the device | Every `<img>` has `srcset` and `sizes`, `width` and `height` (CLS), `loading="lazy"` below the fold; the hero has `fetchpriority="high"` and no lazy attribute. Slot aspect from `references/assets/slot-spec.md`. | FAIL | RESEARCH |
| MA7 | Text baked into images (headline, price, offer inside the hero image) | Headlines, prices and offer terms are live text (WCAG 1.4.5). Generation policy already forbids text in generated images. | FAIL | LAW |
| MA8 | Text over imagery without a scrim | Text on photographs measured against rendered pixels at 4.5:1 (A7); use the single permitted black-to-transparent overlay (N7) only in the plan's bold moment. | FAIL | LAW |
| MA9 | Centred long paragraphs, measure over 80 characters or under 45 | Left-align body at 390; A4 measure rule. | WARN | RESEARCH |

## 3. Interaction and targets

| Id | Anti-pattern | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| MA10 | Hover-only interactions (tooltips, hover zoom, hover-reveal CTAs) | No hover; 76 percent of sites have unclear hit areas (Baymard). Every hover behaviour has a tap equivalent; image zoom supports tap or pinch. https://baymard.com/blog/mobile-commerce-design | FAIL | RESEARCH |
| MA11 | Tap targets under the house 48 x 48 CSS px floor | House A11 requires 48 x 48 for every tap target; lower external minima do not reduce this requirement. https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html | BLOCK | LAW |
| MA12 | Side-by-side buttons that wrap or fall under 140 px wide | Stack CTAs vertically under 480 px; only one is filled (CA4). | WARN | OPERATOR |
| MA13 | Carousels without cues | Peek the next card (about 15 percent), show dots or a counter, visible edge arrows on swatch scrollers (Baymard). https://baymard.com/blog/mobile-ux-ecommerce | WARN | RESEARCH |
| MA14 | Thumb-zone violations | Primary action reachable one-handed: within the first screen's lower 85 percent or in a sticky bar. Modals dismiss from a bottom-sheet button, not only a top-right X. | WARN | RESEARCH |
| MA15 | Drag-only interactions (before/after sliders, range inputs) | Offer tap or button alternatives (WCAG 2.5.7 AA). | FAIL | LAW |
| MA16 | Sticky element covers the focused control or content | WCAG 2.4.11 focus not obscured. Sticky bar height is reserved with `scroll-padding-bottom` or body padding. | FAIL | LAW |
| MA17 | Auto-rotating carousels on touch | CA1. | FAIL | RESEARCH |

## 4. Forms

| Id | Anti-pattern | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| MA18 | Placeholder-only labels; labels beside fields | Visible `<label>` above each field (Baymard: inline or placeholder labels cause issues on 38 percent of sites); mark both required and optional. https://baymard.com/blog/mobile-ecommerce-checkout-forms | FAIL | RESEARCH |
| MA19 | Wrong keyboard | `type="email"` with `autocapitalize="off"` and `autocomplete="email"`; `type="tel"`; `inputmode="numeric"` for OTP, PIN, postcode; Baymard: 60 percent of sites fail two of five keyboard optimisations. | FAIL | RESEARCH |
| MA20 | Modal taller than the viewport or locking scroll | Dialogs scroll internally, `max-height: 85vh`, close control visible without scrolling; popups at most 60 percent of viewport height, bottom sheet preferred (CA3, DP14). | FAIL | RESEARCH |
| MA21 | Close control under 48 px, under 3:1 contrast, or not the first tappable element | Close at least 48 x 48 under A11, 3:1, reachable; Esc and backdrop tap close (DP10). | BLOCK | LAW |
| MA22 | Asking again for data already given | Prefill checkout email from the capture form (WCAG 3.3.7). | WARN | LAW |

## 5. First screen at 390

MA23 (FAIL, OPERATOR). The first 844 px contain exactly what the type file's
"Above the fold (390px)" section lists, in that order, and nothing else:
no popup, no chat launcher, no cookie sheet over the hero, no second CTA
style, no carousel. `price_above_fold` is obeyed. On `advertorial` and
`video-sales-page` the first screen may have no CTA; on every other selling
type the primary CTA is visible or reachable within 1.5 screens (A8).

Generic first-screen recipe when the type file is silent (from the
teardowns, internal research audit (2026-09-10) Part D section 3):

| Type family | First screen order |
|---|---|
| pdp, pdp-hybrid-landing | gallery, title, rating + count (ledger), one-sentence claim, price with tax wording, variant control, CTA, shipping/returns line |
| ad-landing-page, offer-page, restock | headline, subhead, proof line, price, CTA, one-line risk reversal |
| listicle | optional offer bar (ledger), numbered headline with audience or verified count, subhead, proof strip, first CTA |
| advertorial | kicker plus "Advertisement" label, headline, lead sentence; no CTA |
| quiz-funnel, lead-capture-giveaway | outcome headline, one sentence, the single control |
| homepage, collection-landing | headline, one sentence, CTA, trust line |

Check (Playwright, 390 x 844): list the visible elements with `top < 844`
and compare against the type file's list; any extra element fails.

## 6. Check scripts

Run in the hosted draft after load and again after scrolling to 50 and 100
percent. Record results in `QA record`.

```js
// MA4, MA5: fixed-element budget
(() => {
  const f = [...document.querySelectorAll('*')].filter(e => ['fixed','sticky'].includes(getComputedStyle(e).position) && e.offsetParent !== null && e.getBoundingClientRect().height > 0);
  const h = e => e.getBoundingClientRect().height;
  const top = f.filter(e => e.getBoundingClientRect().top < innerHeight * 0.2).reduce((s, e) => s + h(e), 0);
  const total = f.reduce((s, e) => s + h(e), 0);
  return { count: f.length, top, total, ok: top <= innerHeight * 0.15 && total <= innerHeight * 0.30 && f.length <= 3 };
})();

// MA11: all tap targets use the A11 house floor
(() => [...document.querySelectorAll('a,button,[role=button],input:not([type=hidden]),select,summary')]
  .filter(e => e.offsetParent !== null && !e.closest('p'))
  .map(e => { const r = e.getBoundingClientRect();
    const min = 48;
    return { el: e.textContent.trim().slice(0, 30) || e.tagName, w: Math.round(r.width), h: Math.round(r.height), min, ok: r.width >= min && r.height >= min }; })
  .filter(x => !x.ok))();   // []

// MA23: first-screen inventory
(() => [...document.querySelectorAll('h1,h2,p,button,a.btn,[role=button],img,video,[data-part=price],[role=dialog],[data-part=chat-launcher]')]
  .filter(e => e.offsetParent !== null && e.getBoundingClientRect().top < innerHeight)
  .map(e => (e.closest('[data-section]')?.dataset.section || '?') + ':' + e.tagName + ':' + (e.dataset.part || e.textContent.trim().slice(0, 25))))();
```
