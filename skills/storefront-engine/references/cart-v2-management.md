# Cart V2 Management — MCP Workflow

How to read, modify, and validate store-level cart configuration using MCP tools.

---

## Store Config Shape

The actual API response from `get_cart_config`:

```json
{
  "id": "uuid",
  "store_id": "uuid",
  "cart_mode": "drawer-right",
  "cart_sections": [{"id": "cart-drawer", "html": "...", "css": "...", "js": "..."}],
  "cart_rules": [...],
  "commerce_config": {
    "free_shipping_threshold": 7500,
    "currency": "USD",
    "upsells": [{"trigger_product_ids": ["gid://shopify/Product/123"], "recommend_product_ids": ["gid://shopify/Product/789"], "label": "Complete your routine"}],
    "cart_style": {"mode": "drawer-right", "responsive": {"mobile": "bottom-sheet"}, "width": "420px", "animate": "spring"},
    "checkout_mode": "standard"
  }
}
```

---

## Available Tools (ONLY these 3)

### `get_cart_config`

Read current config. **Always call first.**

**Params:** `store_id` (UUID)

---

### `update_cart_config`

Partial update. Validates rules before persisting.

**Params:**
- `store_id` (UUID, required)
- `cart_mode` (optional)
- `cart_sections` (optional, array of `{id, html, css?, js?}`)
- `cart_rules` (optional, array)
- `commerce_config` (optional, object)

---

### `validate_cart_rules`

Dry-run validation. Does not persist.

**Params:**
- `store_id` (UUID)
- `rules` (array)

**Returns:** `{valid, errors[]}`

---

## Reactive Workflow

1. Call `get_cart_config` to read current state
2. Modify the relevant field (`commerce_config` for thresholds/upsells, `cart_sections` for HTML, `cart_rules` for conditional logic)
3. Call `update_cart_config` with only the changed fields
4. Islands react automatically — CartProgressBar reads `free_shipping_threshold`, CartCrossSell reads `upsells`

---

## Common Operations

### Add upsell

1. Read config
2. Append to `commerce_config.upsells`:
```json
{"trigger_product_ids": ["gid://shopify/Product/123"], "recommend_product_ids": ["gid://shopify/Product/789"], "label": "Complete your routine"}
```
3. Call `update_cart_config` with updated `commerce_config`

### Change threshold

1. Read config
2. Set `commerce_config.free_shipping_threshold` to new value (cents)
3. Call `update_cart_config` with updated `commerce_config`

### Add rule

1. Read config
2. Append to `cart_rules`
3. Validate first via `validate_cart_rules`
4. Call `update_cart_config` with updated `cart_rules`

### Change mode

Call `update_cart_config` with `cart_mode: "bottom-sheet"` (or other valid mode).

---

## Important Notes

- `cart_sections` is a JSONB array (not a string) — same structure as page sections
- Product IDs in upsells must be Shopify GIDs (`gid://shopify/Product/XXX`)
- Islands are self-managing: CartCrossSell shows/hides based on cart contents matching `trigger_product_ids`
- No need to regenerate HTML when changing `commerce_config` — islands read it live
