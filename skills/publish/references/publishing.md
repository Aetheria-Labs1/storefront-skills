# Publishing and lifecycle

Publication promotes a reviewed draft; it does not create another page.
`references/source-artifact-workflow.md` owns source and version evidence.

## Publish gate

1. Resolve the existing page id and confirm its store/theme binding.
2. Read current `lexsis_pages.edit_context`, source and integrity.
3. Match the current version and source/bundle hashes to the approved hosted
   QA evidence from `references/qa-recipe.md`. Stale evidence blocks release.
4. Verify current publish permissions and entitlement.
5. Obtain explicit approval naming this page and version.
6. Call `lexsis_live_ops.publish` using the discovered argument schema.
7. Re-read the published version and verify the returned public URL. Report
   publication and live HTTP verification separately.

If no draft exists, use `references/generation-protocol.md` first. If a draft
exists, reuse its returned preview URL; previewing never creates another page.
No local source, CSS, manifest, compile artifact or QA file is required.

## Other lifecycle operations

`lexsis_live_ops.unpublish` and `lexsis_live_ops.rollback` require explicit
authorization and a confirmed target. Edits to a published page remain
draft-only until publish succeeds. A failed republish leaves the previous
published version in place; verify this rather than assuming recovery.

Variants follow `references/ab-testing.md`; every variant keeps its own
page/version and hosted QA evidence. Never infer publication from draft
creation, design approval, experiment creation or a request for a preview.
