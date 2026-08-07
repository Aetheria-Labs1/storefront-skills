# PlanSelector — Island Directory

Subscribe-and-save plan cards — the dominant DTC PDP purchase pattern: large radio cards (Autoship vs One-Time) with per-card price, compare-at, per-unit cost, benefit checklist, and live re-pricing from a tier selector.

## Files

| File | Purpose |
|------|---------|
| `schema.json` | Auto-generated props/parts/examples |

## Quick Reference

- **Component**: PlanSelector
- **Category**: commerce
- **Props**: 7 (plans, defaultPlanId, variant, listenForTiers, emitEvents, showBenefits, __innerHTML)
- **Required props**: `plans` (array of {id, title, price, compareAtPrice?, perUnit?, sellingPlanId?, frequency?, benefits?, note?, badge?, static?})
- **Variants**: `cards` (default), `stacked`, `minimal`
- **Schema**: `vibe://schema/island/PlanSelector`
- **Contract**: follows `_contract.md` rules

## Behavior

- Radio-card selection; the selected card carries `data-selected="true"` — style selection state via CSS on that attribute, never inline overrides.
- Emits `subscription:changed` ({active, sellingPlanId?, price, frequency?}) on mount and every change — a `BuyBox` with `listenForEvents:true` picks up the selling plan and price with zero extra wiring.
- `listenForTiers:true` subscribes to `tiers:changed` (emitted by `QuantityBreaks` with `emitEvents:true`): the selling-plan card re-prices from the payload's `subscribePrice`/`subscribeCompareAt`/`subscribePerUnit` and shows the `cadence` line; one-time cards re-price from the base `price`/`compareAtPrice`/`perUnit`. Mark a plan `static:true` to pin its price (e.g. a fixed one-time price regardless of tier).
- **Container slot**: add `data-island-container` to the placement div and put child HTML (typically a `QuantityBreaks` island) inside it — it renders inside the FIRST plan card body (`data-part="plan-slot"`) and child islands hydrate via the rescan mechanism. This is how "tiers inside the Autoship card" layouts compose.

## data-parts (CSS customization surface)

`root`, `plan`, `plan-radio`, `plan-title`, `plan-price`, `plan-compare`, `plan-per-unit`, `plan-benefits`, `benefit-item`, `plan-note`, `plan-badge`, `plan-slot`, `cadence-line`

All default colors use `--lx-accent-color`, `--lx-border-color`, `--lx-surface`, `--lx-text-color` with fallbacks — fully re-themeable per section.

## Composition

- Pair with: QuantityBreaks (`emitEvents:true, showCta:false`) for tier-driven re-pricing, BuyBox (`listenForEvents:true`) for the CTA, CartDrawer, PaymentOptions
- Never combine with SubscriptionToggle on the same page (both emit `subscription:changed`)
- PlanSelector selects — it does not add to cart. Always pair with a BuyBox or ProceedToCart CTA.
- Reference retrofits: templates `pdp-biotin-gummies-purna` (side-by-side PlanSelector + QuantityBreaks cards) and `pdp-beauty-strip-nustrips` (QuantityBreaks columns nested in the container slot).
