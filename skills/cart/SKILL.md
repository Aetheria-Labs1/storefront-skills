---
name: cart
description: Inspect, assign, design, compose, or preview Lexsis cart profiles. Supports responsive design, scoped CSS, custom source-format modules, and read-only promotion diagnostics.
---

# Configure a Cart

Cart profiles are managed separately from page section HTML.

Use `lexsis_cart.get`, `lexsis_cart.capabilities`,
`lexsis_cart.promotions`, and `lexsis_cart.preview`. When requested, use
`lexsis_drafts.cart_set` and `lexsis_drafts.cart_edit`. Resolve unfamiliar
argument schemas with exact router/action discovery. An empty discovery result
is not a cart outage; the actual cart call determines availability. Do not
infer the effective cart profile from page HTML.

Resolve the target store from a page binding, an explicit saved choice, or the
unambiguous default in `work/storefront/setup/setup.json`. If it is not saved,
stop and ask the user to run `/setup`; never invoke setup automatically.

## Rules

- A page enables the cart through its supported page configuration; do not add
  DrawerShell or cart-line markup to page sections.
- Effective profile order is page assignment, campaign assignment, store
  default, then legacy fallback.
- Draft profile edits are not live until published in the Lexsis app.
- Do not invent products, prices, currencies, offers, or selling plans.
- Promotion, discount, offer, shipping-threshold, and cart-rule configuration
  is read-only through MCP. Never try to recreate those writes through another
  tool.
- Custom modules use the same Lexsis source format as normal pages: HTML,
  `<style>`, section `<script>`, managed motion, and registered `<lx-island>`
  components. Cart lines, order summary, checkout, and DrawerShell remain
  renderer-owned.

## Workflow

1. Call `lexsis_cart.get`.
   - Use `page_id` to inspect the effective profile and resolution source.
   - Use `cart_profile_id` to inspect an editable profile.
   - Use `store_id` to list profiles.
2. Call `lexsis_cart.capabilities` before the first design or composition edit
   in a task. Resolve island props through `lexsis_design.island_schema`.
3. For discounts or offers, call `lexsis_cart.promotions` and report the
   configured profile values, active Shopify discounts, and readiness or
   conflict diagnostics without changing them.
4. When requested, assign a published profile with
   `lexsis_drafts` action `cart_set`. Passing a null profile removes the page
   assignment.
5. Edit a draft with `lexsis_drafts` action `cart_edit` and a partial patch.
   Supported areas are cart mode, typed design settings, responsive
   presentation, scoped custom CSS, and composition operations.
   - `upsert` adds or replaces one custom module from one source section.
   - `move` reorders a module within its header, body, or footer region.
   - `set_enabled` toggles custom or optional modules.
   - `remove` deletes only custom modules.
   - Use `before_module_id: "checkout"` and `region: "footer"` for a block
     immediately above checkout.
6. Re-read the profile with `lexsis_cart.get`.
7. Call `lexsis_cart.preview`, then verify the signed preview on desktop and
   mobile. Test both populated and empty cart states when the design changes
   structure.

Use real catalog and review data in custom modules. For example, a rotating
review strip above checkout should use `ReviewCarousel` with an active review
collection or merchant-confirmed reviews; never fabricate quotes or ratings.
Cart triggers dispatch `cart:open`; they do not need a profile ID.

Custom CSS must remain scoped to the cart. External imports, remote URLs,
script escapes, and unbalanced rules are not allowed.

## Return

Report the effective profile, resolution source, composition and design
changes, promotion diagnostics, preview URL/evidence, page assignment, and
which actions still require review or publication in Lexsis.
