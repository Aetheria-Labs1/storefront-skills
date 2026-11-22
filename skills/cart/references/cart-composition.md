# Cart Profile Composition

A cart profile is a renderer-managed surface backed by a published profile.
Custom cart interactions, batch add flows, and controls selecting multiple
products use the documented `lx:cart:add-items` renderer command.

## Page contract

Cart V2 is enabled by default for every storefront. New source omits the
deprecated `use_cart_v2` compatibility field. Existing `true` values remain
valid; `false` fails validation because Cart V2 cannot be disabled.

The page must not contain `CartDrawer`, `DrawerShell`, or cart child islands.
The renderer resolves and injects the cart after the page sections.

Resolution order:

```text
page assignment > campaign assignment > store default > legacy fallback
```

Page metadata does not select a profile.

## Profile modules

The profile snapshot owns:

- Cart mode and responsive behavior
- Ordered layout modules
- Cart sections and rules
- Free-shipping progress
- Shopify selling-plan presentation
- Manual and Shopify-powered offers
- Checkout behavior
- Cart design settings and scoped CSS

Cart lines, order summary, and checkout are required. Optional modules include
shipping progress, purchase options, payment methods, and product offers.

## Offers and subscriptions

Offer placements:

- `header`
- `after_line`
- `after_lines`
- `before_checkout`

Manual offers use Shopify product GIDs. Recommendation offers use Shopify
`RELATED` or `COMPLEMENTARY` intent.

Selling-plan options are line-item capabilities. A profile can choose cards or
a select menu, but it cannot make an ineligible product subscribable.

## Trigger protocol

Add-to-cart controls and the site header emit `cart:open`. The hydrator bridges
DOM events into the cart event bus. The injected `DrawerShell` listens for the
event and lazily hydrates its children on first open.

Use the selected island's supported cart trigger for normal product controls.
For a custom interaction that owns a dynamic product selection, use the
renderer-managed `lx:cart:add-items` command instead of hidden BuyBoxes,
programmatic clicks, or a parallel Shopify/cart mutation. This is the custom
cart and batch add contract for controls that select multiple products.

See `references/module-authoring.md` for a complete compiler-tested upsell,
including its registered add control and request-scoped state handling.
Dispatch from `section`, the `[data-cart-custom-module="<id>"]` wrapper.
Responses return to that wrapper and bubble: `lx:cart:add-items:pending`,
`:accepted`, `:confirmed`, `:success`, and `:error`. Listen on the wrapper and
filter by requestId; a listener on an authored child section will not receive
an event dispatched from its parent.

No trigger should carry or infer a profile ID.

## Styling

Page `theme_css` provides brand defaults. Cart profile design values and
`custom_css` apply only under the cart profile root.

Custom CSS is sanitized and scoped at render time. Do not put profile CSS in
page sections or page metadata. See `references/styling-hooks.md` for the full
part map and inline-style exceptions.

## Patch and module identity contract

- `custom_css` replaces all CSS, including named blocks; null clears it.
  Use `css_ops` to upsert/remove named blocks without resending other blocks.
- `design_patch` is JSON Merge Patch: omitted fields remain, null removes a
  stored override, arrays replace arrays. Removing an override can expose a default.
- `composition_ops.upsert` with source replaces the whole module source.
  Omit source to preserve it during visibility/placement changes.
  New modules honour `before_module_id` or `after_module_id` on the first upsert.
  Without an explicit region, the module inherits its anchor's region,
  including header and before-checkout offer placements.
  Regions: `header`, `body`, `footer`, `above_title`, `floating_above`, `sheet`
  (hidden until opened; see module-authoring.md, Presentation commands).
- `data-module` equals the layout ID, including `offer-<uuid>` and custom IDs.
  `data-module-type` equals the layout type, such as `product_offer` or `custom`.
  Generated sections before `default@13` used `data-module="product-offer"`;
  recompile a draft to get consistent IDs. After-line offers repeat their slot
  ID under each qualifying line; use the line group to distinguish instances.
- Layout enabled flags are authoritative; offer-slot enabled flags are mirrored.
  Disabled optional modules are absent. `visible_when` keeps a module mounted
  with `hidden` while its cart-state predicate is false.

Built-in module DOM is identical in the sandbox and published renderer:
`[data-module="cart-lines"] [data-lx-island-runtime] > [data-part="root"]`.
The island can share its module frame or sit inside it. Use a module descendant
selector, or explicitly include the runtime wrapper in child
selectors. Gift rows follow paid rows.

Reward messages accept `{remaining}`, `{next_title}`, `{threshold}`,
`{unlocked_title}` and `{unlocked_list}`. Amounts are formatted money; unlocked
titles describe applied rewards and are empty before the first application.
`{reward_title}` is the triggering reward's title in `toast.template` only.
Use `{unlocked_title|Your rewards}` for a literal fallback, or
`{#if unlocked}{unlocked_title} unlocked. {/if}{remaining} more gets you {next_title}.`
for an optional clause. Conditional blocks cannot nest.

`compact_bar` applies state `text_color` to icons and labels and state
`border_color`/`background` to dots. Labels, icons and dots expose `data-state`.
Summary copy exposes separate `subtotal-label` and muted `subtotal-hint` spans.

Celebration particles start at the unlocked dot (or panel top). Cart scope
stays in the panel; viewport scope renders above the sheet and overlay.
Toasts fit the panel and clear close controls. Positions are `top` (below the
header), `bottom`, `above_header` (falls below the header when no space).
`toast.duration_ms` overrides the inherited celebration duration.

## Build the cart as files

`lexsis_build` with `cart_profile_id` (instead of `page_id`) exposes the
profile's presentation layer as a `lexsis.cart/1` tree, the cart counterpart of
`lexsis.page/2`:

```text
lexsis.json          every module in order: {id, type, enabled, visible_when?, region (custom)}
modules/<id>.html    one custom module source (<!-- section: id --> first)
styles/<block>.css   one file per named CSS block
```

- `get` returns `version`, `tree` (path → sha256) and the `files` you name.
- `commit` with `base_version` and only the changed files (`null` deletes)
  saves one new draft version. The server diffs the tree against the draft
  and applies it as `composition_ops` + `css_ops`, so every `cart_edit` rule
  holds: one section per module, no cart islands inside a module, required
  modules stay, module CSS is scoped. Diagnostics carry `file` + `line`.
  `dry_run:true` compiles and mints a preview without saving.
- `patch` applies `replace_text`, `upsert_css_rule`, `remove_css_rule`,
  `set_attr`, `move_section` and `remove_section` (module ids) to the tree,
  then commits. There is no `set_head`.
- `diff` compares two versions of the tree.
- Built-in modules have no file. Add, reorder, enable or condition them in
  `lexsis.json`; configure them (offers, rewards, rules, design) with
  `cart_edit` / `cart_promotions_edit`. Only custom modules can be added or
  removed as files.
- Only the current draft is readable as files; a stale `base_version` is
  `VERSION_CONFLICT` (re-read, re-apply, resend). No create: make the profile
  with `cart_create` first.
- Shell users: `LEXSIS_API_KEY=… npx @lexsis/cli pull --cart <cart_profile_id> ./cart`,
  edit, `npx @lexsis/cli push ./cart --dry-run`, then `push`. Cart profiles
  have no scoped push token yet.

Use files when a cart has several custom modules or a module is long (a sheet,
a bundle builder, a multi-step upsell). Use `cart_edit` for one small
composition change or anything that is configuration.

## Current cart workflow

The recent cart changes include paid-price reward eligibility/readiness,
page-to-cart CSS isolation, typed settings that reach the DOM, custom module
snapshots/commands/conditions, approved MCP lifecycle and promotion writes,
and compact edits with signed sample carts. The type-only component cleanup
adds no authoring API. Local source support does not upgrade an immutable
published runtime: verify the deployed capability/schema and preview.

Read `references/cart-profile-management.md` for the create, design, promotion,
preview, approved publish and rollback flow. `lexsis_cart.promotions` accepts a
profile ID alone and infers the store. Use `lexsis_discover` with
`query:"publish cart"` for up to 10 ranked results (schemas for the top 3), or
exact router/action discovery for an authoritative schema.

## Anti-patterns

| Anti-pattern | Correct behavior |
|---|---|
| Inline `DrawerShell` on a storefront page | Remove it and configure the effective profile |
| Cart selected through title or SEO metadata | Use a page assignment |
| Agent publishes a draft automatically | Review the exact draft; publish through approved `lexsis_live_ops.cart_publish` or the app |
| Fabricated products or selling plans | Use real store catalog data |
| Page-wide selectors in cart CSS | Use profile-scoped CSS |
| Hidden BuyBox plus `.click()` for a custom selection | Dispatch `lx:cart:add-items` from the registered section control |
| Direct `/cart/add.js` or Storefront API request | Let the renderer perform the managed GraphQL cart mutation |
