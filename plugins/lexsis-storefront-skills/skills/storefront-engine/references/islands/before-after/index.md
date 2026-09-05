# BeforeAfter — Island Directory

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

Transformation comparison island. Shows before/after states via slider, side-by-side, or toggle.

## Quick Reference

- **Variants**: slider, side-by-side, toggle
- **Required prop**: `before` (object with `src`, `label`)
- **Schema**: `vibe://schema/island/BeforeAfter`
- **Contract**: follows `_contract.md` rules

## Composition

- Pair with: Testimonials, ProductDetails, BuyBox
- Place mid-page to demonstrate product transformation results
- Works well below a hero and above social proof
- Never use more than 2 BeforeAfter islands on a single page

## Hero Integration Pattern

Two BeforeAfter sliders side-by-side inside a gradient-bordered card, paired with a numbered features list:

```html
<section>
  <!-- Centered heading + CTA above -->
  <div class="card-wrapper" style="background: linear-gradient(...);">
    <div class="card" style="display:flex;">
      <div class="sliders" style="flex:1;display:flex;gap:8px;">
        <div data-island="BeforeAfter" data-props='{"before":{"src":"...","label":"BEFORE"},"after":{"src":"...","label":"AFTER"},"orientation":"horizontal","initialPosition":50}'></div>
        <div data-island="BeforeAfter" data-props='{"before":{"src":"...","label":"BEFORE"},"after":{"src":"...","label":"AFTER"},"orientation":"horizontal","initialPosition":50}'></div>
      </div>
      <div class="features">
        <!-- Numbered feature list (01, 02, 03...) -->
      </div>
    </div>
  </div>
</section>
```

Templates: `hero-before-after-skincare`, `hero-before-after-nordic`, `hero-before-after-glam`
