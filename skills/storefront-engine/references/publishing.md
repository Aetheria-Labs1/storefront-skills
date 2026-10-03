# Publishing and lifecycle

Publication promotes a reviewed draft; it does not create another page.
`references/source-artifact-workflow.md` owns source and version evidence.

## Publish gate

1. Resolve the existing page id and confirm its store/theme binding.
2. Read current `lexsis_pages.edit_context`, source and integrity.
3. Match the current version and source/bundle hashes to the approved hosted
   QA evidence from `references/qa-recipe.md`. Stale evidence blocks release.
4. Verify current publish permissions and entitlement.
5. Confirm explicit approval naming this page and version; reuse approval
   already given for the same scope.
6. Call `lexsis_live_ops.publish` using the discovered argument schema.
7. Re-read the published version and verify the returned public URL. Report
   publication and live HTTP verification separately.

If no draft exists, use `references/generation-protocol.md` first. If a draft
exists, reuse its returned preview URL; previewing never creates another page.
No local source, CSS, manifest, compile artifact or QA file is required.

## Quiz policies and verification

A `/quiz` draft can carry `DESIGN_APPROVED` after the same hosted QA and explicit
version approval as `/design-page` or `/optimize`. If saving is requested, follow
`references/quiz-authoring.md` to inspect and prepare the policy for the immutable
page-version UUID. Activate only with capture-policy approval; publish with page
release approval. Any source edit requires fresh inspection and matching policy.

Preview verifies design, logic, product mapping, focus, and transition motion.
Verify production saving and analytics after publication on the returned public
URL, including consent denial, retry/edit/reload, and the Forms response. A
published page, a saved response, an analytics event, and a purchase are distinct
facts. Deactivation stops collection without deleting retained responses.

## Other lifecycle operations

`lexsis_live_ops.unpublish` and `lexsis_live_ops.rollback` require explicit
authorization and a confirmed target. Edits to a published page remain
draft-only until publish succeeds. A failed republish leaves the previous
published version in place; verify this rather than assuming recovery.

Variants follow `references/ab-testing.md`; every variant keeps its own
page/version and hosted QA evidence. Never infer publication from draft
creation, design approval, experiment creation or a request for a preview.
