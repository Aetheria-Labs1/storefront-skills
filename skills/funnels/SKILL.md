---
name: funnels
description: Plan, create, update, validate, and interactively preview a Lexsis storefront funnel from a plain-language request. Use for product-finder quizzes, branching offers, gift reveals, and multi-step lead capture. Creates drafts only; never attaches, activates, or publishes a funnel.
---

# Create a Funnel

Read `references/funnels.md`.

Turn the merchant's desired shopper journey into one complete, reviewable
funnel definition. A funnel is reusable journey logic, not a page. Do not edit
page source or add a `FunnelRuntime` island while running this skill.

Use:

- `lexsis_capture` action `funnel_capabilities`
- `lexsis_capture` actions `funnel_templates` and `funnel_template`
- `lexsis_capture` actions `get_funnel`, `validate_funnel`, and
  `preview_funnel`
- `lexsis_drafts` actions `funnel_create` and `funnel_update`

Use `lexsis_catalog` and `lexsis_pages` to resolve real product and page
destinations before putting identifiers into outcomes. Resolve unfamiliar
argument schemas with `lexsis_discover`. An empty discovery result is not a
funnel outage; call the documented router action and report its concrete error.

Resolve the store from an explicitly supplied workspace/page URL, the page
binding, a saved store choice, or the unambiguous default saved by `/setup`.
If multiple stores remain possible, ask the merchant to choose. Never invoke
`/setup` automatically.

## Workflow

1. Read `funnel_capabilities`. Treat the returned schema version, node kinds,
   triggers, outcomes, and activation availability as authoritative.
2. List the backend-owned templates. Read the closest template when it reduces
   unnecessary custom work; do not create an empty shell.
3. Clarify only missing decisions that change the journey: audience, goal,
   questions, branch logic, result for every path, desired presentation, and
   eventual entry point.
4. Resolve every referenced product, collection, or page. Never invent an ID,
   price, reward, discount, product relationship, or destination.
5. Present a concise funnel plan before mutation:
   - entry trigger and modal/inline presentation;
   - ordered questions and answer options;
   - branch conditions and default paths;
   - terminal result and intended outcome for every reachable path;
   - unresolved activation work.
6. After the merchant approves the plan, create one complete version-2 draft
   with `lexsis_drafts` action `funnel_create`.
7. Re-read it with `get_funnel`, run `validate_funnel`, and fix all errors.
   Warnings must be reported and may remain only when they concern a later
   publish or activation step.
8. Create a signed preview with `preview_funnel`. Open it using the host's
   browser capability and exercise every reachable path at mobile and desktop
   widths. Preview answers are local and do not prove capture, analytics,
   attachment, or live runtime behavior.
9. For revisions, read the draft again and pass its exact `revision` as
   `expected_revision` to `funnel_update`. Replace the complete definition;
   do not patch isolated steps from stale state.

## Safety boundaries

- Draft creation and updates are reversible writes and require the normal
  `lexsis_drafts` approval.
- There is no funnel publish, attachment, or activation action in the current
  MCP contract. Do not substitute page editing or `lexsis_live_ops`.
- A dedicated funnel URL will be a normal Lexsis page with an inline funnel
  placement. It is not created by this skill.
- Existing-button, inserted-button, automatic, and custom-event triggers are
  definition contracts for later placement activation. Recording a trigger in
  a draft does not make it live.
- Never use arbitrary JavaScript. Do not use a CSS selector when a stable page
  block or action ID is available.
- Never claim an outcome navigates, adds to cart, starts checkout, captures a
  lead, or records analytics until activation and runtime execution are
  separately available and verified.

## Return

Report the funnel ID, store, revision, definition summary, validation errors
and warnings, preview URL and expiry, paths exercised, and the exact work still
required for page placement, activation, outcomes, and publication.
