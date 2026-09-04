---
name: publish
description: Publish a synchronized and QA-passed Lexsis storefront draft. Use only when the user explicitly asks to release a specific page version.
---

# Publish a Page

Publishing is a separate, explicit action. Do not rebuild the page here.

Complete a fresh MCP preflight and discover the exact page-context,
entitlement, and publish actions required by this run. If discovery fails,
return `BLOCKED_LEXSIS_MCP`; a local QA report cannot authorize or substitute
for a live publish action.

## Gate

1. Read the page manifest and QA report.
2. Confirm the saved store/theme binding still exists.
3. Confirm the current local bundle and section hashes match the synchronized
   values in the manifest.
4. Read `lexsis_pages` action `edit_context`.
5. Confirm the remote version equals `remote.lastKnownVersion`.
6. Confirm responsive, commerce, copy, claims, assets, and integrity checks
   passed against that same version and local bundle.
7. Confirm the store has the required entitlement.
8. Ask for explicit approval naming the page and version.

Only then call:

```text
lexsis_live_ops({ action: "publish", args: { page_id } })
```

Do not treat draft creation or a preview request as publishing approval.

## Other Lifecycle Actions

Use `lexsis_live_ops` for unpublish or rollback only when the user explicitly
requests that action and the target page/version is clear.

## Return

Report the published page, version, public URL, and whether the previous live
version remains available for rollback. Include the MCP capability and action
evidence.
