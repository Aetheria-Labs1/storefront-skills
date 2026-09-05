# Lexsis MCP Contract

Lexsis MCP is the system of record for templates, catalogue data, assets,
island schemas, compilation, drafts, remote versions, analytics, carts,
experiments, and publishing.

MCP dependency metadata and an `.mcp.json` entry describe configuration. They
do not prove that the server or its tools are available in the current
session.

## Required Preflight

Before reading live Lexsis data or creating, reading, or changing standard
page artifacts:

1. Confirm that the `lexsis-ai` MCP server exposes `lexsis_discover`.
2. Call `lexsis_discover` for each router/action needed by the current skill.
   Use the returned schema as authoritative; never guess arguments from memory.
3. Record the successful discovery in `page-manifest.json` when a page
   workspace exists.
4. Use live Lexsis reads for changing data such as products, variants, prices,
   availability, assets, island schemas, permissions, analytics, and remote
   versions.

Discover only the capabilities required for the current task. Do not load the
entire action catalogue when a small targeted query is enough.

## Failure Policy

### MCP unavailable

If `lexsis_discover` is absent, fails, or cannot return the required action
schemas:

- stop with `BLOCKED_LEXSIS_MCP`
- name the unavailable capabilities
- do not create or modify standard page artifacts
- do not present static HTML, cached catalogue data, or custom commerce
  controls as an equivalent Lexsis result

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

## Manifest Evidence

Record the latest successful preflight:

```json
{
  "mcp": {
    "status": "connected",
    "checkedAt": "2026-09-04T12:00:00Z",
    "surfaceVersion": "3.0",
    "capabilities": [
      {
        "router": "lexsis_template_library",
        "actions": ["search_page_kits", "search_sections"]
      }
    ]
  }
}
```

Store capability names, not full schemas or credentials. Update this record
when another skill performs a new preflight.

## Result Evidence

Every Lexsis-dependent result reports:

- MCP connection status
- discovered capabilities used
- Lexsis router actions called
- selected template or reason for custom composition
- live product and asset bindings used
- fallbacks used
- blocking limitations

`setup` has no page manifest, so it returns this evidence directly with its
saved setup paths.
