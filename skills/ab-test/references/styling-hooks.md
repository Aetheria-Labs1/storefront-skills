# Cart Styling Hooks

Use typed `design_patch` first. Normal page selectors are excluded from the cart.
Profile custom CSS is scoped under `[data-lx-cart-profile]` in `lx-cart-custom`,
above `lx-cart-design` and island defaults. Custom-module CSS has its own
`@scope ([data-cart-custom-module="<id>"])`.

Use `[data-module="<layout-id>"]` for a particular module and
`[data-module-type="<layout type>"]` for a kind. Types use the layout's
snake_case values, for example `product_offer`. IDs match `layout_schema`,
including `offer-<uuid>`. Older generated sections used
`data-module="product-offer"`; regenerate/save a draft before using the new
selector on such a profile. Do not rename IDs in composition operations.
An after-line offer repeats the slot ID once per qualifying line.

## Drawer shell

Parts appear after the drawer first opens. These are not page sections.
Optional regions/controls exist only when enabled.

| `data-part` | Purpose | Inline styles |
| --- | --- | --- |
| `portal` | Profile root and portal mount | Pointer events and visibility |
| `overlay` | Backdrop close button | Animated opacity |
| `panel` | Drawer/dialog surface | Width/max-width, height/max-height, modal translate, animated transforms/opacity |
| `content` | Shell content column | None authored |
| `header-region` | Title row plus header modules | None |
| `header` | Header row | None |
| `header-title` | Visible `shell.title` | None |
| `header-count` | Quantity badge/inline count | None |
| `header-content` | Optional header module markup | None |
| `close` | Close button | Tap animation transform; circle is a class |
| `drag-handle` | Optional bottom-sheet handle | None |
| `committed-content` | Mounted cart content | None |
| `scroll-region` | Scrollable content and non-sticky regions | None |
| `body` | Body modules | None |
| `footer` | Footer module markup | None |
| `module-frame` | Built-in module container | None |
| `custom-module` | Custom wrapper / script event target | None supplied by renderer |

The `panel` also carries `data-mode`, `data-header-layout`, `data-count-style`,
`data-close-style`, `data-sticky-header`, `data-sticky-footer`,
`data-content-background` and `data-desktop-layout`. `shell.title` supplies both
the visible header and dialog label. Do not replace the header with literal HTML.

## Cart island parts

Below are all named parts in the cart islands and their cart-specific child
controls. Scope common names like `root`, `item` and `bar` to the island's
`[data-island]` mount or module. Runtime-only parts appear in their active state.

| Island | Parts |
| --- | --- |
| CartLines | `root`, `empty`, `empty-visual`, `empty-message`, `empty-cta`, `line-group`, `item`, `item-image-wrap`, `item-image`, `reward-badge`, `item-info`, `item-title`, `adding-indicator`, `remove-btn`, `free-gift-label`, `item-variant`, `item-price`, `discount-percent`, `purchase-option`, `optimistic-qty`, `qty-controls`, `qty-select`, `qty-decrease`, `qty-value`, `qty-increase`, `reward-qty`, `module-frame` |
| CartSummary | `root`, `line`, `line-label`, `line-value`, `subtotal`, `subtotal-label`, `subtotal-value` |
| CartRewardProgress | `root`, `message`, `track`, `bar`, `milestones`, `milestone`, `milestone-threshold`, `milestone-visual`, `milestone-label`, `milestone-status`, `configuration-badge`, `scoped-offer`, `offer-condition`, `gift-title`, `gift-select`, `gift-action` |
| CartCoupons | `root`, `summary`, `savings`, `coupon-view` |
| CartCheckoutButton | `root`, `cta`, `payment-logos`, `secondary-cta` |
| CartCrossSell | `root`, `heading`, `fallback`, `item`, `item-image`, `item-info`, `item-title`, `item-price`, `add-button` |
| CartProgressBar | `root`, `visual`, `track`, `bar`, `message` |
| PaymentOptions | `root`, `provider`, `provider-logo`, `provider-fallback`, `button`, `text`, `icons-row` |
| Shared cart status | `cart-sync-status`, `cart-action-dots` |

CartCoupons portals `coupon-view` into the shell panel, outside its island
mount. Target `[data-part="coupon-view"]` under the profile, not only below
`[data-island="CartCoupons"]`. Its internal form/cards have no stable named
parts yet; do not invent selectors such as `coupon-input`.

PaymentOptions parts depend on its variant. Logos may be inside checkout,
below checkout, or hidden. Use
`design_patch.modules.payment_options.{placement,providers}` to set placement
and provider order; `commerce_config.payment_settings` is also editable with
`cart_promotions_edit`. The optional payment module's enabled/visibility state
controls those logos even when they render inside checkout.

### Inline-style exceptions

- CartLines, CartSummary and CartCheckoutButton: motion writes opacity,
  transforms and, during layout/exit animations, dimensions. Quantity/remove
  controls may have tap transforms. Style colors/spacing with the typed API.
- CartRewardProgress: `track` has measured top and optional segmented mask;
  `bar` adds live progress width; `milestones` has grid-template-columns;
  fallback `milestone-visual` has gradient/image backgrounds.
- CartProgressBar: `bar` uses `transform:scaleX(...)` for live progress.
- CartCoupons: `root` and `coupon-view` carry theme CSS variables;
  `coupon-view` also has motion transforms/opacity.
- PaymentOptions: `provider-fallback` sets the provider brand background color.
- CartVisual images set width, height and object-fit inline. Loading dots use
  inline animation delays. CartCrossSell itself adds no inline style.

Do not override live transforms/progress widths to change decoration. Inline
values beat normal styles, even in a later layer. Prefer typed values and
supported CSS variables; avoid broad `!important` rules. Dynamic visibility
rules deliberately enforce `[hidden]` so they cannot be defeated by layout CSS.

## Examples

Use this as a named `css_ops` block to address all offers and one custom module:

```css
[data-module-type="product_offer"] [data-part="heading"] {
  font-weight: 700;
}
[data-module="matching-item"] {
  margin-block: 12px;
}
```

`custom_css` replaces all profile CSS and named blocks; null clears them.
`css_ops` changes named blocks in insertion order. `design_patch` is a JSON
Merge Patch: omitted values remain, null removes a stored override and defaults
can take effect, arrays replace whole arrays. A source-bearing composition
`upsert` replaces the entire custom module source; it is not a source diff.
Use dry run and signed fixture previews to inspect both populated and empty carts.
