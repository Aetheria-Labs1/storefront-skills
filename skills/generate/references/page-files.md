# Page and campaign evidence

Keep these records in the task handoff, alongside the MCP page id and version.
They are not files to create or arguments to submit to page actions.
`references/source-artifact-workflow.md` owns direct authoring and persisted
state. Existing one-time setup context may be reused; no per-page folder,
manifest, source file or CSS file is required.

## Binding and campaign

Record one `workspaceId`, `storeId` and `themeId`, the page title/handle and
any existing page id. Confirm ambiguous names through current MCP context.
Never silently move an existing page to another store or theme.

Group related pages by the campaign's purpose, occasion and audience, not a
filesystem path. `campaign.type` comes from
`references/offers/campaign-calendar.md`; confirmed start/end dates are
recorded only when the merchant supplies or verifies them. Related pages
share campaign facts, not an assumed permission to publish or spend credits.

## Page decision record

- `page.pageType`, `funnelStage`, `awareness`, `trafficSource`: choose through
  `references/page-types/_index.md`; use the vocabulary in
  `references/page-types/_checklist-format.md`.
- `sections`: ordered canonical section ids and any justified deviations.
- `template`: chosen kit/section ids or the reason for custom composition.
- `products`: current product and variant bindings, never stale sample ids.
- `offer`: selected offer id or none, merchant-confirmed terms and evidence;
  its ledger follows `references/offers/offer-ledger.md`.
- `reviews`: verified source, collection/product ids, available count and
  rights/provenance; its ledger follows `references/proof/proof-ledger.md`.
- `assets`: slot id, job, section id, final permanent URL and asset/media id,
  source, rights basis and verified/planned status. Source eligibility,
  generation records and approval belong to `references/assets/`.
- `workflow`: intent, explicit skipped stages and remaining approval/QA work.

Do not conflate a pending slot, an available library candidate and a verified
asset. Creative reasoning, claim sources and approvals stay in readable
planning evidence rather than a second set of machine-only defaults.

## Stage transitions

Planning records the type, design direction, section jobs, ledgers and gaps.
Design resolves current interactive schemas, authors source through MCP,
creates one unpublished draft and returns `DRAFT_CREATED`.
Generation reuses that draft and upgrades it to `DRAFT_READY` only after
matching persisted-version evidence and hosted QA. Publication is separate.
Keep the last returned page id, version and preview URL available throughout.
