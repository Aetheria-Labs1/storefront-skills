# Lexsis MCP Contract

Lexsis MCP is the system of record for templates, catalogue data, assets,
island schemas, compilation, drafts, remote versions, analytics, carts,
experiments, and publishing.

## Source and Template Authority

Page source is authoritative for section order and visible page chrome.
Headers, announcement bars, navigation, and footers are ordinary source
sections; the renderer must not inject a hidden shell around them.

Reusable user-owned sections use the merchant-template actions:

- `lexsis_template_library`: `list_mine`, `get_mine`
- `lexsis_drafts`: `template_create`, `template_update`, `template_apply`
- `lexsis_live_ops`: `template_publish`, `template_archive`

Read `merchant-templates.md` before creating, updating, or applying one. There
is no `lexsis_styles` router or Navigation Profile workflow.

MCP dependency metadata and an `.mcp.json` entry describe configuration. They
do not prove that the server or its tools are available in the current
session.

## Resolve Actions with Exact Slots

The public skills declare the stable router and action pairs they use. Resolve
an unfamiliar input schema with the structured discovery fields:

```json
{
  "router": "lexsis_catalog",
  "action": "list"
}
```

Do not use a natural-language `query` for a known workflow action. The `query`
field is only a convenience when the router/action is genuinely unknown or
when mapping a former tool name.

`lexsis_discover` is an API directory, not a connection test and not the tool
that performs the operation. A response with `ok: true` and `count: 0` is a
lookup miss. It does not mean Lexsis MCP, the target router, or the storefront
is unavailable.

Before live Lexsis work:

1. Use the exact router/action pairs listed by the active skill.
2. When an action's arguments are unfamiliar, call `lexsis_discover` with
   `router` and `action`; never improvise a prose query for a known pair.
3. Invoke the real domain router for the operation.
4. Read changing products, variants, prices, availability, assets, island
   schemas, permissions, analytics, and remote versions live.

## Error Handling

- `ok: true, count: 0` from discovery: keep working. Retry with the exact
  router/action pair, then use the current MCP tool schema or bundled Lexsis
  contract. Record discovery as degraded when appropriate.
- Missing router, authentication failure, transport failure, or an error from
  the actual domain call: report that concrete error and identify the affected
  operation.
- Continue work that does not depend on the failed live operation.
- Do not claim live data, successful compilation, a remote write, QA, or
  publishing when the corresponding real call did not succeed.
- Never substitute static HTML, cached catalogue data, or custom commerce
  controls as an equivalent successful Lexsis result.
- For a write, use only fields defined by the current MCP schema or bundled
  Lexsis contract. Do not guess mutation arguments.

### Explicit offline prototype

Continue without MCP only when the user explicitly requests an offline
prototype. Write it under an `offline-prototype/` directory, label it
non-production, and do not:

- mark planning, visual approval, asset readiness, draft readiness, QA, or
  publish readiness as complete
- claim live prices, inventory, variants, assets, commerce, or island behavior
- create or patch a Lexsis page

An offline prototype does not update the normal page manifest or replace the
standard Lexsis workflow.

### Individual capability unavailable

Continue only when the current skill defines a safe equivalent. Record the
capability, fallback, and limitation.

Examples:

- No suitable template result: custom composition is allowed after recording
  the searches and rejection reason.
- One island lacks safe preview data: static fallback is allowed for that
  island during visual review.
- Island schema or production compilation fails: do not mark the page
  production-ready.

## Result Evidence

When useful for diagnosis, a Lexsis-dependent command result or `qa-report.md`
reports:

- MCP connection status
- capabilities and resolution method used
- Lexsis router actions called
- selected template or reason for custom composition
- live product and asset bindings used
- fallbacks used
- blocking limitations

Do not store discovery logs, capability inventories, action transcripts, or
connection status in `page-manifest.json`. The manifest is a compact workflow
state ledger.

`setup` has no page manifest, so it returns this evidence directly with its
saved setup paths.
