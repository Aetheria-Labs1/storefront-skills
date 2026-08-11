# Cart Profile MCP Management

The MCP exposes three cart operations. Keep lifecycle management in the app.

## `get_cart_profile`

Inspect the effective cart for a page or one editable profile.

Inputs:

- `page_id`
- `cart_profile_id`
- `store_id` as an optional multi-store hint
- `include_available_profiles`

Pass `page_id` to get the published snapshot a shopper receives and its
`resolution_source`. Pass `cart_profile_id` to inspect the draft.

Always call this tool before assigning or editing.

## `set_cart_profile`

Assign a published profile to a page:

```json
{
  "page_id": "PAGE_UUID",
  "cart_profile_id": "PROFILE_UUID"
}
```

Remove the page assignment and restore fallback resolution:

```json
{
  "page_id": "PAGE_UUID",
  "cart_profile_id": null
}
```

The page and profile must belong to the same store. Draft and archived profiles
cannot be assigned.

## `edit_cart`

Apply a partial patch to a profile draft:

```json
{
  "cart_profile_id": "PROFILE_UUID",
  "change_note": "Increase shipping target and update offer",
  "patch": {
    "cart_mode": "drawer-right",
    "commerce_config": {
      "free_shipping_threshold": 7500,
      "offer_slots": [
        {
          "id": "pairs-well",
          "placement": "after_line",
          "source": "shopify_recommendations",
          "recommendation_intent": "COMPLEMENTARY",
          "heading": "Pairs well with",
          "trigger_product_ids": [],
          "recommend_product_ids": [],
          "max_items": 1,
          "enabled": true
        }
      ]
    },
    "custom_css": "[data-part=\"checkout\"] { font-weight: 600; }"
  }
}
```

Supported patch fields:

- `cart_mode`
- `layout_schema`
- `cart_rules`
- `commerce_config`
- `custom_css`

Nested commerce objects merge. Arrays replace their previous value. Pass
`custom_css: null` to remove profile CSS.

The tool validates the complete merged configuration and never publishes.

## App-only operations

Use the Lexsis app to:

- Create, duplicate, rename, and archive profiles
- Publish and roll back versions
- Set the store default
- Manage campaign assignments
- Review assignment history and analytics

## Verification

After a mutation, resolve the page again with `get_cart_profile`. Confirm the
profile ID, version, and resolution source before telling the merchant the
targeting is correct.
