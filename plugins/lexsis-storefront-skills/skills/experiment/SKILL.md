---
name: experiment
description: Create or evaluate a focused Lexsis storefront experiment from a clear hypothesis. Keeps every variant synchronized with its own local source before remote writes.
---

# Run a Storefront Experiment

Use this for a measurable comparison, not ordinary page editing.

Use `lexsis_pages.edit_context`, `lexsis_pages.source`,
`lexsis_pages.compile`, `lexsis_pages.integrity`, `lexsis_analytics.page`,
`lexsis_analytics.experiment`, `lexsis_drafts.page_duplicate`,
`lexsis_drafts.page_variation`, and `lexsis_drafts.experiment_create`.
Resolve unfamiliar argument schemas with exact router/action discovery. Do
not interpret an empty discovery result as a page or analytics outage. Report
any failure from the actual read or mutation and do not claim that operation
succeeded.

Confirm the base page's store/theme binding exists in
`work/storefront/setup/setup.json`. If it is missing, stop and ask the user to
run `/setup`; never invoke setup automatically.

## Define the Test

Confirm:

- page and current baseline version
- one primary hypothesis
- primary metric and guardrail metrics
- intended audience or traffic segment
- approved traffic split and stopping rule

Change as few elements as needed to test the hypothesis. If several unrelated
ideas are bundled together, split them into separate tests.

## Local-First Variants

Before duplicating or changing a remote page:

1. Confirm the base page has synchronized local source and manifest.
2. Create a separate local directory, source file, and manifest for each
   variant.
3. Apply the variant change locally.
4. Validate and compile the complete variant source.
5. Create or update the remote variant with the expected base version.
6. Store every returned page ID and version locally.
7. Run integrity, responsive, and affected commerce checks.

Never let a remote variant become the only copy of a change.

## Launch

Use the currently discovered Lexsis experiment actions and schemas. Confirm
entitlement and credits before creation. Do not publish a base page or variant
without explicit approval.

## Evaluate

Read the experiment's current status and results from Lexsis. Report:

- sample sizes and exposure split
- primary and guardrail metric movement
- whether the configured decision rule has been reached
- data-quality or targeting concerns
- recommended action: continue, stop, promote, or discard

Do not call a winner from directional movement alone.

## Return

Return the hypothesis, local variant paths, remote page/version IDs, experiment
ID, launch state, current decision, and MCP evidence.
