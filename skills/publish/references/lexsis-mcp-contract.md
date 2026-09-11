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

## Asset Import and Upload

`lexsis_asset_import.import` requires exactly one source: `url`, image
`data` + `mime_type`, or a non-empty `attachments` array of conversation
attachment IDs. It imports directly into the library and never opens the upload UI.
Do not call import without a source or combine multiple source types.

`lexsis_asset_upload.upload` exclusively opens the local image/video upload UI.
Pass only the selected `workspace_id` and `theme_id`; do not send URL, base64,
or attachment inputs to this action. In inline-UI hosts,
wait for the user's uploaded-asset message before using its asset ID and URL.
Opening the panel is not evidence that an asset was uploaded.

If the host has no inline UI, ask for a URL or conversation attachment and
use `lexsis_asset_import.import` with that source instead. Do not repeatedly
open an unsupported upload panel. `lexsis_asset_library.search` selects
existing library assets; it is not a local-file upload action.

## Managed Motion Compilation

Custom animation is authored in source as
`<script type="application/lexsis-motion">`. The `lexsis_pages` `compile`
action:

1. extracts each motion function into the owning section's `motion[]`
2. parses its AST and rejects unsafe globals, raw loops/observers/timers,
   arbitrary networking, dynamic code, programmatic clicks, and undeclared
   capabilities
3. validates page source, loop, and WebGL budgets
4. emits the animation manifest used for diagnostics and risk classification
5. preserves the module through source reads, page bundles, section patches,
   and versioned drafts

The renderer then supplies only the declared managed APIs. `three.load()` uses
the renderer-owned Three.js package and reserves a managed WebGL context;
`webgl.context()` supplies raw WebGL. Agents do not add Three.js, GSAP, Lottie,
or Rive CDN scripts.

Compilation proves that the module satisfies the contract. It does not prove
that a 3D composition is framed well or that an interaction feels correct.
Always review the hosted draft visually. Read `animation-system.md` before
authoring or editing managed motion.

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

## When Lexsis Behaviour Is Unclear

`lexsis_support` action `search_docs` searches the Lexsis storefront
documentation and returns passages about islands, tools, recipes, page schema
and workflows. Use it when a behaviour is genuinely unclear, before guessing or
before telling the user something is impossible. It answers questions about the
product; it does not replace `lexsis_design` action `island_schema` for prop
shapes or `lexsis_discover` for an action's arguments.

## Recovery and Inspection Actions

Three actions exist for narrow situations and should not appear in a normal
build:

- `lexsis_pages` action `compile_artifact` retrieves a short-lived compiled
  bundle by `compile_id`. Draft creation consumes `compile_id` directly, so
  fetch the artifact only to inspect a compile result. Never fetch it merely to
  read the page back.
- `lexsis_drafts` action `page_attach_bundle` attaches an existing successful
  compile artifact to the current version without creating a new one. Use it
  only to recover a page whose source was stored but whose bundle attachment
  failed, with `expected_version`.
- `lexsis_pages` action `qa` reads the stored QA record for a page;
  `lexsis_drafts` action `page_record_qa` writes it.

## Reporting a Defect

`lexsis_drafts` action `send_feedback` files a bug or gap with the Lexsis dev
team. Use it when the platform, not the page, is at fault, and say so to the
user rather than filing silently. Categories: `island-bug`,
`island-variant-request`, `validator-issue`, `generation-quality`, `ux-issue`,
`docs-gap`, `composition-issue`, `api-bug`, `api-gap`, `platform-bug`, with a
severity. The distinction that matters: `docs-gap` means the guidance is
missing or wrong and documenting it would fix the problem, while `api-gap`
means no tool exists for a necessary operation and documentation would not.

File one when an island renders wrong with schema-valid props, the compiler
rejects something the contract allows, a tool returns a misleading result, or a
required primitive has no action. Do not file for a page-level mistake you can
fix yourself, and never let filing substitute for finishing or for telling the
user what is blocked.

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

An offline prototype does not update the normal page record or replace the
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

When useful for diagnosis, a Lexsis-dependent command result or `QA record`
reports:

- MCP connection status
- capabilities and resolution method used
- Lexsis router actions called
- selected template or reason for custom composition
- live product and asset bindings used
- fallbacks used
- blocking limitations

Do not store discovery logs, capability inventories, action transcripts, or
connection status in `page record`. The manifest is a compact workflow
state ledger.

`setup` has no page record, so it returns this evidence directly with its
saved setup paths.
