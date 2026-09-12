# Compile and draft protocol

House rules in `storefront-engine/references/design-rules.md` govern the
presentation. The source contract is `references/authoring/source-authoring.md`;
`references/source-artifact-workflow.md` owns artifact and manifest state.
Choose section order from the page-type contract, not from this protocol.

## Compile exact inputs

1. Reuse the bound workspace, store and theme; read current page context for
   edits through `lexsis_pages.edit_context` and editable source through
   `lexsis_pages.source` or `lexsis_pages.section_source`.
2. Prepare complete source and any page-wide theme CSS as values, not
   mandatory files. Resolve only the interactive
   decisions through `references/workflows/island-selection-workflow.md`.
3. Call `lexsis_pages.compile` with the exact `source`, `head`, `theme_css`
   and optional `scripts` inputs. `lexsis_pages.compile_artifact` retrieves
   an existing result by `compile_id` for inspection; it does not compile.
4. Read all `validation_errors`, publish validation and missing utility
   candidates. Repair the source rather than mutating compiled JSON.
5. Save the successful response and input hashes as compile evidence.

## Create or edit one draft

Use `lexsis_page_create.create` with `compile_id` and `publish: false`
only when the workspace has no existing page id. Otherwise use the relevant
versioned draft action: `page_update_section`, `page_patch`, `page_replace`,
`page_update_head`, `page_move_section`, or `page_remove_section` on
`lexsis_drafts`, with `expected_version` when the action supports it.
On a version conflict, read the latest context and reconcile; do not overwrite
blindly. Return the hosted draft URL and exact version as `DRAFT_CREATED`.

## Review and release boundary

A clean compile is structural evidence, not a visual pass. Hosted design
review and commerce checks follow `references/qa-recipe.md`. `DRAFT_CREATED`
may leave review pending; `DESIGN_APPROVED` cannot be claimed without hosted
review evidence. Publication follows `references/publishing.md` and requires
explicit authorization. Report the exact state and do not equate draft
creation, approval, publication, and live HTTP verification.

The exact mutually exclusive creation inputs and hosted verification
are owned by `references/source-artifact-workflow.md`.
