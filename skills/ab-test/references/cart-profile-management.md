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
- the frozen `lifecycle.cart` snapshot schema and settled `onCart` subscriptions
- managed line, code, attribute, note, gift and variant commands with scoped responses
- module `visible_when`, condition fields/operators and no-JS binding paths

## `lexsis_cart.promotions`

Read configured profile offers plus active Shopify discount codes and automatic
discounts. This operation is read-only. Do not claim that the MCP can create,
edit, activate, or delete a promotion.

## `lexsis_cart.preview`

Pass `page_id` to render an immutable cart profile version on the existing
storefront page. The returned URL carries `preview=1`, `cart_profile_id`, and
`cart_version`. This path only reads the saved version snapshot: it does not
publish the profile, change page assignment, or create/update Shopify
discounts.

Omit `page_id` to create or refresh an isolated signed cart fixture preview.
Use either preview URL for desktop and mobile visual QA.

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
  "change_note": "Add a cart reminder above checkout",
  "patch": {
    "design_patch": {
      "shell": {"title": "Your cart"}
    },
    "custom_css": "[data-part=\"checkout\"] { font-weight: 700; }",
    "composition_ops": [
      {
        "operation": "upsert",
        "module_id": "checkout-reminder",
        "region": "footer",
        "source": "<!-- section: checkout-reminder -->\n<section><p>Review your cart before checkout.</p></section>",
        "before_module_id": "checkout",
        "visible_when": {
          "op": "AND",
          "clauses": [{"field": "cart.item_count", "op": "gt", "value": 0}]
        }
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
lines, summary, or checkout. Existing custom and optional built-in modules may
omit source when upserting `visible_when`; pass null to clear the condition.

Custom scripts read the frozen `lifecycle.cart` snapshot and subscribe with
`lifecycle.onCart((snapshot, previous) => ...)`. Subscriptions wait for confirmed
currency/prices and completed cart settlement, coalesce per frame, and clean up
on unmount. Money is `{amount, currencyCode, minor}` and matches CartSummary.
No default currency is invented.

Dispatch managed commands from `section` with `bubbles: true` and a unique
`requestId`: `lx:cart:add-items`, `update-line`, `remove-line`, `apply-code`,
`remove-code`, `set-attributes`, `set-note`, `choose-gift`, `swap-variant`
(all use the `lx:cart:` prefix). Read the exact payload and error contract from
capabilities. Responses return to the originating module. Identical replay
does not write again; a changed payload under the same ID is rejected.

`visible_when` uses AND/OR clauses over typed cart, reward and context fields.
Money comparisons use minor units; membership `neq` hides an offer when the
given variant is present. It sets `hidden`, including for inline offers and
inside-checkout payment logos. `data-lx-if` supports validated comparisons and
predicates; `data-lx-text="rewards.next.remaining"` formats real Money without
JavaScript. Unknown fields, types and expression paths fail before saving.
Customer context requires a host provider; collection membership requires
Shopify metadata access. Missing metadata is not proof of exclusion.

Design objects merge. Composition operations are applied in order. Pass
`custom_css: null` to remove profile CSS. The tool validates and compiles the
complete merged configuration and never publishes.

Presentation edits rebuild cart sections. `shell.title` controls the visible
header and dialog label. Disabled optional modules stay absent; product-offer
visibility is mirrored into offer slots so inline offers also disappear.

Use `design_patch.modules.payment_options.placement` for `inside_checkout`,
`below_checkout`, or `hidden`, and `providers` for a unique, ordered provider
list. The payment module's enabled flag gates both placements. Variant,
alignment, colors, and icon styling apply inside checkout too.

Read the returned `warnings` array. Entries with `code: "setting_not_rendered"`
identify a stored path with no effect. Responsive overrides support tokens,
`shell.width`, and module/state CSS; use base settings for island props.
Deprecated gift `lock_quantity` and the unused `warning` color token have no
effect. Confirmed gift quantities remain controlled by reward rules.

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
