# Cart Profile MCP Management

The Storefront MCP exposes cart inspection, draft design/promotion editing,
previews and approved lifecycle operations through the same backend as the app.

## `lexsis_cart.get`

Inspect the effective cart for a page or one editable profile.

Inputs:

- `page_id`
- `cart_profile_id`
- `store_id` as an optional multi-store hint
- `include_available_profiles`
- `include_history` for the latest 100 lifecycle events, authenticated actor/client and diff summaries
- `fields` for selected profile fields/dotted paths; unknown paths fail
- `response:"full"` for complete source; metadata is the default

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
discounts. Pass `cart_profile_id` alone to infer its store; `store_id` is an
optional explicit scope. A store-only call lists Shopify discounts without
profile readiness. This operation is read-only. Use `cart_promotions_edit` for requested
draft edits and explicitly approved `cart_publish` for Shopify synchronization.

## `lexsis_cart.preview`

Pass `page_id`, `cart_profile_id`, and a fixture name: `empty`,
`below_first_reward`, `between_rewards`, `all_unlocked`, `gift_chosen`, or
`code_applied`. Optional `cart_version` pins a saved version. Explicit fixture:
`{lines:[{variantId,quantity,sellingPlanId?}],codes?:[]}` (real store GIDs,
12 lines, quantity 1-999, 10 codes). Default fixture is empty.

The URL carries `preview=1`, `cart_version` and a signed `fixture` token,
expiring in 15 minutes. Omit `page_id` for an isolated sample cart. No browser
is started. Open the URL in your own browser. Samples are computed from synced
catalogue prices and shared reward calculations, marked `source:"computed"`.
They do not mutate Shopify, restore/write `lx_cartId`, or permit checkout.
Tracking is suppressed. Tampering/expiry logs `fixture_invalid` and falls back
to normal cart: only interact as a sample when its badge is present.

## `lexsis_cart.preview_states`

Pass `{page_id,cart_profile_id}` for all six signed URLs, CartSnapshots, module
visibility and static checks in one response. Checks: setting warnings,
configured color contrast, shown unready rewards, custom compilation and
hardcoded checkout links. No screenshots or DOM measurements. Unavailable
fixtures/checks are explicit warnings or `not_run`, not proof of success.

## Edit-loop response and CSS contract

Draft writes return compact summaries by default; `response:"full"` returns
full profile source. `cart_edit dry_run:true` runs the same compiler, returns
errors/warnings, a module tree and signed uncommitted URL without saving a
version. Module visibility uses an empty fixture; an unavailable evaluator is
reported explicitly. Saved edits with `preview_error` should retry preview,
not the write.

`custom_css` replaces all CSS, including named blocks; null clears it.
`css_ops:[{op:"upsert",id:"checkout",css:"..."},{op:"remove",id:"old"}]` updates
named blocks in insertion order. Upsert keeps the position; removal requires
an existing ID. First use preserves old CSS as `legacy`. Both together fail.
Each block and their concatenation are sanitized and scoped.

`island_schema` defaults to a compact overview with shared `$defs.iconName`.
`fields:["rewards"]` expands a prop; `verbose:true` adds full styling/examples.
`type_expression` definitions preserve the authoring DSL with `$ref(...)`
aliases; they are not standalone JSON Schema.

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

## Lifecycle and promotion actions

Capabilities report `lifecycle_access: "mcp_with_approval"` and
`promotion_access: "draft_then_publish"`. The custom-module lifecycle is under
`module_lifecycle`, alongside the unchanged snapshot and command schemas.

| Router | Action | Arguments |
|---|---|---|
| `lexsis_drafts` | `cart_create` | `store_id`, `name`, optional `from_preset` or `from_profile_id` |
| `lexsis_drafts` | `cart_duplicate` | `cart_profile_id`, `name` |
| `lexsis_drafts` | `cart_promotions_edit` | `cart_profile_id`, `expected_version`, `patch` |
| `lexsis_drafts` | `cart_archive` | `cart_profile_id`, optional `reassign_to` |
| `lexsis_drafts` | `cart_assign_campaign` | `campaign_id`, `cart_profile_id` (nullable) |
| `lexsis_live_ops` | `cart_publish` | `cart_profile_id`, `expected_version`, `allow_partial:false`, `skip_reward_ids:[]` |
| `lexsis_live_ops` | `cart_rollback` | `cart_profile_id`, `target_version` |
| `lexsis_live_ops` | `cart_set_default` | `store_id`, `cart_profile_id` |

Presets: `default`, `subscription`, `aov_booster`. Creation and duplication are
unpublished. Optional `store_id` speeds profile/campaign lookup.

Promotion patches merge `rewards`, `offer_slots`, `quantity_promotions` and
`cart_rules` by ID. Omitted rows remain. `{id,operation:"remove"}` removes one
existing row; an empty patch array is a no-op. New rows need complete required
fields. `coupon_settings` and `payment_settings` merge objects; nested arrays
replace. Coupon allow-list is `coupon_settings.coupons`; manual entry is
`allow_manual_entry`. Payment `placement` is `inside_checkout | below_checkout |
hidden`; `providers` is an ordered unique list. Monetary thresholds use minor
currency units. Gift/qualifying products and collections use verified Shopify IDs.

The promotion edit response includes `profile` and `readiness`. Incomplete setup
can be saved; malformed values and stale versions fail. Shopify transport
failure returns a saved draft with `readiness_unavailable`. No promotion edit
writes to Shopify. Readiness uses the same validator as publication.

Publishing requires explicit approval and publish access. It checks the exact
version, provisions the managed contracts, then commits the live pointer.
`CART_NOT_READY` includes issues; `VERSION_CONFLICT` includes the current version.
Partial publication disables only the explicitly approved `skip_reward_ids`,
then reruns readiness. Remaining/global issues still block publication. The
response gives `published_version`, created/updated/disabled Shopify discount IDs
and warnings. Contract resolution can add a version. Use the returned version.

Rollback makes a new forward draft and leaves the live version unchanged.
Preview it, then obtain separate approval for `cart_publish`. Default and
campaign/page assignment change live resolution and require approval plus
publish access. Campaign assignment is under drafts but is not draft-only.
Archive blocks default or assigned profiles unless `reassign_to` is a published
replacement in the same store. It preserves assignment priority/enabled state.

Shopify has no cross-mutation transaction. On failure the publisher compensates
created/retired discounts; an unconfirmed cleanup returns
`CART_PUBLISH_RECOVERY_REQUIRED` and must be resolved before retrying. A discount
still shared by another published profile remains active with a warning.

## Verification

After a mutation, re-read the draft with `lexsis_cart.get`, then call
`lexsis_cart.preview`. Confirm the profile ID and version, and visually inspect
the preview at desktop and mobile widths. Assignment and publication remain separate approved actions.
Use `get` with `include_history:true` to inspect the actor/client and diff summary.
