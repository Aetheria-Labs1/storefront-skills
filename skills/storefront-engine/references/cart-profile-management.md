# Cart Profile MCP Management

The Storefront MCP exposes cart inspection, design/composition editing, and
ephemeral preview operations. Keep lifecycle and promotion management in the
app.

## `lexsis_cart.get`

Inspect the effective cart for a page or one editable profile.

Inputs:

- `page_id`
- `cart_profile_id`
- `store_id` as an optional multi-store hint
- `include_available_profiles`

Pass `page_id` to get the published snapshot a shopper receives and its
`resolution_source`. Pass `cart_profile_id` to inspect the draft.

Always call this tool before assigning or editing.

## `lexsis_cart.capabilities`

Read the current cart composition contract before authoring a custom module.
The response describes:

- supported layout schema and module types
- protected renderer-owned cart modules
- source compilation and placement operations
- design token and custom CSS capabilities
- promotion access boundaries

## `lexsis_cart.promotions`

Read configured profile offers plus active Shopify discount codes and automatic
discounts. This operation is read-only. Do not claim that the MCP can create,
edit, activate, or delete a promotion.

## `lexsis_cart.preview`

Create or refresh an ephemeral signed preview for the current profile draft.
Use the returned preview URL for desktop and mobile visual QA. A preview is not
a published profile and does not change page assignment.

## `lexsis_drafts.cart_set`

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

## `lexsis_drafts.cart_edit`

Apply a design or composition patch to a profile draft:

```json
{
  "cart_profile_id": "PROFILE_UUID",
  "expected_version": 12,
  "change_note": "Add rotating reviews above checkout",
  "patch": {
    "design_patch": {
      "checkout": {
        "button": {
          "radius": "pill"
        }
      }
    },
    "custom_css": "[data-part=\"checkout\"] { font-weight: 700; }",
    "composition_ops": [
      {
        "op": "upsert",
        "module": {
          "id": "checkout-reviews",
          "region": "body",
          "source": {
            "html": "<section class=\"review-strip\" aria-label=\"Customer reviews\"><p>Rated 4.9 by verified buyers</p></section>",
            "css": ".review-strip { overflow: hidden; padding: .75rem 1rem; }",
            "js": "const items = section.querySelectorAll('[data-review]');",
            "motion": []
          }
        },
        "before": "checkout"
      }
    ]
  }
}
```

Supported patch fields:

- `cart_mode`
- `design_patch`
- `custom_css`
- `composition_ops`

Composition operations support `upsert`, `move`, `set_enabled`, and `remove`.
An upsert compiles the same section source shape used by normal storefront
pages: HTML, CSS, JavaScript, and managed motion. It may use active storefront
islands, but it cannot replace or nest renderer-owned cart modules such as cart
lines, summary, or checkout.

Design objects merge. Composition operations are applied in order. Pass
`custom_css: null` to remove profile CSS. The tool validates and compiles the
complete merged configuration and never publishes.

Promotion configuration, cart rules, raw commerce configuration, and raw layout
schema are deliberately absent from the MCP edit contract.

## App-only operations

Use the Lexsis app to:

- Create, duplicate, rename, and archive profiles
- Publish and roll back versions
- Set the store default
- Manage campaign assignments
- Create, edit, activate, and delete discounts or offers
- Review assignment history and analytics

## Verification

After a mutation, re-read the draft with `lexsis_cart.get`, then call
`lexsis_cart.preview`. Confirm the profile ID and version, and visually inspect
the preview at desktop and mobile widths. Assignment and publication remain
separate app-managed states.
