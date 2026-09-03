---
name: cart
description: Inspect, assign, or edit Lexsis cart profiles for a storefront page. Covers offers, shipping goals, subscriptions, responsive behavior, and scoped cart styling.
---

# Configure a Cart

Cart profiles are managed separately from page section HTML.

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

## Workflow

1. Call `lexsis_cart.get`.
   - Use `page_id` to inspect the effective profile and resolution source.
   - Use `cart_profile_id` to inspect an editable profile.
   - Use `store_id` to list profiles.
2. When requested, assign a published profile with
   `lexsis_drafts` action `cart_set`. Passing a null profile removes the page
   assignment.
3. Edit a draft with `lexsis_drafts` action `cart_edit` and a partial patch.
   Supported areas include mode, layout, rules, commerce settings, offers,
   responsive presentation, and scoped custom CSS.
4. Re-read the page with `lexsis_cart.get`.
5. Preview add-to-cart and header cart triggers on desktop and mobile.

Use Shopify product GIDs for offers. Show subscriptions only when real selling
plans exist. Cart triggers dispatch `cart:open`; they do not need a profile ID.

Custom CSS must remain scoped to the cart. External imports, remote URLs,
script escapes, and unbalanced rules are not allowed.

## Return

Report the effective profile, resolution source, draft changes, page
assignment, and which actions still require review or publication in Lexsis.
