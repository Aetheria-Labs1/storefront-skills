# MCP source and verification state

Author pages directly through MCP. Do not create local page decision records,
source/CSS files, compile artifacts, preview builds or local QA reports.
The persisted page source and bundle are the baseline; the hosted draft is
the only preview used by these workflows.

## Create one draft

1. Confirm the workspace, store and theme binding through saved context or
   current MCP reads. Prepare `source` and structured `head` with a title.
   Include `theme_css` only when supplying page-wide CSS. Omitting the field
   does not excuse missing theme tokens or accessibility styles.
2. Send the exact values to `lexsis_pages.compile`. Read blocking errors,
   warnings, missing utilities, hashes and the short-lived `compile_id`.
   Repair source, not compiled JSON.
3. Call `lexsis_page_create.create` with `compile_id`, creation metadata and
   `publish:false`. Omit `source`, `head`, `theme_css`, `scripts` and
   `runtime_dependencies` when passing `compile_id`. Alternatively send the
   exact source/head and optional CSS/scripts directly; create compiles them
   server-side. Never combine the two input modes.
4. Reuse an existing page id rather than spending another creation credit.
   If the compile id expires, recompile the unchanged inputs once.
5. Record the returned page id, version, preview URL and compile hash in the
   task handoff. Surface `DRAFT_CREATED` immediately; it is not a QA pass.

`lexsis_pages.compile_artifact` retrieves an existing compile result for
inspection; it is not another compile route. `lexsis_drafts.page_attach_bundle`
is recovery for a source write whose bundle attachment failed, with
`expected_version`; it is not a normal creation step.

## Edit the persisted source

1. Read `lexsis_pages.edit_context` and `lexsis_pages.source` or
   `lexsis_pages.section_source`. Confirm the target and current version.
2. Reconcile unexpected version drift before writing. Edit the source value
   returned by MCP, keeping stable section ids.
3. Compile changed inputs, compare the intended section changes and use the
   smallest source-based draft action with `expected_version`.
4. Update recorded version/hash evidence only after a successful write.
   Read back source and run `lexsis_pages.diff` and `lexsis_pages.integrity`.
5. Review the updated hosted draft. Editing a draft is not publishing it.

## Evidence without files

Keep the plan, proof/offer ledgers, confirmed asset decisions, approvals and
QA findings in the task's handoff record. `references/page-files.md` defines
the fields, not a filesystem requirement. Do not invent an MCP action for
storing a plan or manifest.

On continuation, recover the page through MCP and recover or re-establish
any missing evidence and approvals. A page id is not evidence that a claim,
asset right or previous approval was verified.

For production readiness, compare the reviewed inputs with the persisted
source, bundle and version; perform `references/qa-recipe.md` against the
hosted draft. Use `lexsis_pages.qa` to read recorded QA and
`lexsis_drafts.page_record_qa` to save supported evidence fields according to
the current schema. A tool acknowledgment does not replace browser evidence.
Missing browser access, evidence or matching hashes keeps QA pending.

Publication requires explicit approval for that same page and version under
`references/publishing.md`. No local validator or file can grant approval.
