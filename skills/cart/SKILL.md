---
name: cart
description: Inspect, assign, and edit cart profiles, including offers, shipping goals, subscriptions, responsive behavior, and scoped custom CSS.
---

# Configure Cart Profiles

Use this workflow for cart profile configuration and page targeting.

## Architecture

- A generated page declares only `head.use_cart_v2: true`.
- Never add `DrawerShell`, `CartLines`, or cart HTML to page sections.
- The renderer injects the resolved published profile after page sections.
- Resolution order is page assignment, campaign assignment, store default,
  then legacy fallback.
- Page titles and SEO metadata never select a cart.
- Draft profile edits do not affect shoppers until the merchant publishes.
- Assignment changes and profile publish/rollback operations automatically
  refresh affected published Shopify pages after the database commit.

## MCP Surface

Use only these cart tools:

1. `lexsis_cart.get`
2. `lexsis_drafts.cart_set`
3. `lexsis_drafts.cart_edit`

Profile creation, duplication, publishing, rollback, defaults, campaign
targeting, history, and archival remain in the Lexsis app.

## Workflow

### 1. Inspect

Call `lexsis_cart.get` before making changes.

- Pass `page_id` to inspect the effective profile and resolution source.
- Pass `cart_profile_id` to inspect an editable draft.
- Pass `store_id` alone to list available profiles.

Do not assume that the store default is the page's effective cart.

### 2. Assign when requested

Call `lexsis_drafts.cart_set` with `page_id` and a published `cart_profile_id`.

Pass `cart_profile_id: null` to remove the page assignment. This restores
campaign, default, or legacy fallback resolution.

### 3. Edit the draft

Call `lexsis_drafts.cart_edit` with a partial patch. The same tool handles:

- `cart_mode`
- `layout_schema`
- `cart_rules`
- `commerce_config`
- `custom_css`

Use `commerce_config` for free shipping, selling-plan presentation, offers,
checkout behavior, currency, and `cart_style`. Nested objects merge with the
existing draft. Arrays such as `offer_slots` replace the existing array.

Example:

```json
{
  "cart_profile_id": "PROFILE_UUID",
  "change_note": "Campaign cart treatment",
  "patch": {
    "commerce_config": {
      "free_shipping_threshold": 7500,
      "free_shipping_celebration": true,
      "cart_style": {
        "width": "440px",
        "responsive": {
          "mobile": "bottom-sheet"
        },
        "line_spacing": "comfortable"
      }
    },
    "custom_css": "[data-part=\"checkout\"] { font-weight: 600; }"
  }
}
```

`lexsis_drafts.cart_edit` never publishes. Tell the merchant to review and publish in the
Lexsis app when the response reports unpublished changes.

## Offers

Offer placements are:

- `header`
- `after_line`
- `after_lines`
- `before_checkout`

Use Shopify product GIDs. Manual offers require recommended product IDs.
Shopify-powered offers use `RELATED` or `COMPLEMENTARY` recommendation intent.

Do not fabricate products, prices, currencies, or selling plans. Subscription
purchase options appear only for products with real Shopify selling plans.

## Trigger Communication

All cart triggers use `cart:open`.

1. Add-to-cart actions emit `cart:open` immediately.
2. The hydrator bridges DOM `cart:open` events to the cart event bus.
3. The injected `DrawerShell` listens for the event and opens.
4. Child cart islands hydrate on first open.
5. The cart confirms or rolls back the optimistic line.

The header cart button uses the same event. Custom page code may dispatch:

```js
document.dispatchEvent(new CustomEvent("cart:open"))
```

The trigger never needs the profile ID. Profile resolution happens before
hydration.

## Styling

Page `theme_css` provides brand defaults. Cart profile design settings and
`custom_css` provide cart-only overrides.

Custom CSS is sanitized, scoped to the profile cart root, and published with
the profile snapshot. External imports, external URLs, script escapes, and
unbalanced rules are rejected.

## Verification

After assignment or editing:

1. Call `lexsis_cart.get` with the page ID.
2. Confirm `resolution_source` and profile identity.
3. Preview add-to-cart and header cart triggers.
4. Check desktop and mobile modes.
5. Confirm offers use real products and subscriptions appear only when
   selling plans exist.
6. Confirm draft changes remain non-live until published.

Read `storefront-engine/references/cart-composition.md` and
the cart profile management reference for the detailed contract.

## Optional Follow-Up

This skill is complete when the cart profile is reviewed in the Lexsis app. If
the user separately requests page integration, `generate` can use the confirmed
profile requirements.
