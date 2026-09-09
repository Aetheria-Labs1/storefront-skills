# StickyBar - Island Directory

Fixed-bottom purchase bar that appears when the primary BuyBox or Hero CTA scrolls out of viewport.

## Quick Reference

- **Variants**: (single default)
- **Input**: bound `productId`, explicit `product`, or a collection CTA
- **Schema**: `vibe://schema/island/StickyBar`
- **Contract**: follows `_contract.md` rules

## Composition

- Triggers when BuyBox or ProductHero scrolls out of viewport
- Place in section AFTER the primary purchase island (BuyBox or ProductHero)
- Max 1 StickyBar per page
- Touch target: min 44px height on mobile
- Uses `position: fixed; bottom: 0` — account for mobile browser chrome
- z-index: 40 (above content, below modals/drawers)

## Optional Purchase Controls

- `showVariantSelector` and `showQuantitySelector` default to false.
- Explicit products keep `variantId` and may include `variants` with id, title, price, available, optional image and compareAtPrice.
- Bound products resolve the full variant catalog. Do not invent variant IDs or prices.
- Match `syncKey` with a rendered or headless BuyBox using the same complete catalog. Both interfaces share variant, quantity, effective price, selling plan, availability, and cart pending state.
- The linked bar waits for BuyBox initialization. Mismatched catalogs disable purchasing. Omit `syncKey` for independent controls.
- Enable `listenForEvents` on BuyBox for external selectors and wrap selectors in `data-scope` equal to `syncKey`. Unscoped events do not drive a linked group.
- Tier-controlled selections remain purchasable, but the bar's variant and quantity controls become read-only. Change options returns to the main purchase controls.
- Active subscription variants require the main plan controls; never reuse an unverified plan price across variants.
- Keep default responsive styling or use `variant-selector`, `quantity`, `quantity-decrement`, `quantity-input`, `quantity-increment`, `change-options`, `cta`, and `error` parts.
- `showAfter` accepts a CSS selector or numeric pixel offset. Do not use `triggerOffset` or `showPrice`; they are not StickyBar props.
