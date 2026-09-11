---
name: publish
description: Publish a synchronized and QA-passed Lexsis storefront draft. Use only when the user explicitly asks to release a specific page version.
---

# Publish a Page

Publishing is a separate, explicit action. Do not rebuild the page here.

Read `references/workflow-intent.md`. Intent inference may distinguish a draft
request from a live-release request, but it never substitutes for explicit
approval naming the page and version. A request to preview, create, finish,
review, or make a page production-ready is not publication approval.

Use `lexsis_pages.edit_context`, `lexsis_pages.integrity`,
`lexsis_pages.source`, `lexsis_workspace.get`, and
`lexsis_live_ops.publish`. Resolve unfamiliar argument schemas with exact
router/action discovery. Do not use a prose query for these known actions. An
empty discovery result is not a publishing outage; the actual context,
entitlement, or publish call determines availability. A local QA report cannot
authorize or substitute for a successful live publish.

## Gate

1. Read the page's operation record and hosted QA evidence under
   `references/source-artifact-workflow.md`.
2. Confirm the saved store/theme binding still exists.
3. Confirm reviewed source, bundle and section hashes match the persisted
   draft and recorded baseline.
4. Read `lexsis_pages` action `edit_context`.
5. Confirm the remote version equals `remote.lastKnownVersion`.
6. Confirm responsive, approved-versus-current hosted visual review, commerce, copy,
   claims, assets, and integrity checks passed against that same version and
   reviewed bundle.
7. Re-read integrity and source/bundle evidence through MCP. Missing or stale
   evidence blocks release; no local file or validator substitutes for it.
8. Confirm the store has the required entitlement.
9. Ask for explicit approval naming the page and version.

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
