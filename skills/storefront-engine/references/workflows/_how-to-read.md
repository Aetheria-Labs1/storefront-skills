# Shared page workflow

The compiler determines valid input. `references/design-rules.md` owns house
requirements; domain policy owns evidence and permissions. The selected
page-type contract owns anatomy and type-specific decisions. Workflows
execute those decisions, never relax their requirements.

## Reading order

1. Select one contract through `references/page-types/_index.md`.
2. Read its context requirements and checklist. Keep the required headings
   and JSON contract; record deviations with their reasons.
3. Execute each section's type-specific row through the four procedures
   below. Read each procedure once, then apply it to every relevant section.
4. Reconcile the asset budget and evidence, then inspect compiler results and
   perform the hosted review at 390, 768 and 1280 before `DESIGN_APPROVED`.

## Four procedures

| Procedure | Single home | Type-specific inputs |
|---|---|---|
| Asset acquisition and missing-slot handling | `references/workflows/section-asset-workflow.md` section 1 | Job, source/tag, crop, required count and legitimate fallback |
| View and section fit | `references/workflows/section-asset-workflow.md` section 2 | Product/variant, composition, adjacent slots and intended crop |
| Interactive selection | `references/workflows/island-selection-workflow.md` | Candidate family and the decision that requires behavior |
| Copy execution | `references/workflows/copy-workflow.md` | Message, evidence, specific ceilings and CTA destination |

A type file supplies the differences, not another copy of these procedures.
"Media: no" is a valid type-specific decision; not every section needs an
image. Static facts, native disclosures and tables remain legitimate content.

## Planning and design responsibilities

`/plan-page` resolves context and asset jobs, records functional intent and
visual direction, and names deviations. It does not choose schema props or
force an island. `/design-page` executes the interactive-selection procedure
against the current catalog and schemas, then compiles the source. Reopen a
planned decision only when new evidence or a contract conflict requires it.
A saved preset label is descriptive intent, not a prop bundle to paste.

## Evidence and handoff

Use `references/page-files.md` and `references/source-artifact-workflow.md`
for page/campaign records, direct MCP authoring and version evidence. Do not create
another ledger format here. Source eligibility and generation permissions
remain in `references/assets/`; proof and offer rows remain in their domain
ledgers. Production claims need the appropriate confirmed evidence.

Type deviations and copy findings are review notes; unsupported proof and
offers block readiness. Review notes do not make unsupported claims acceptable.
Hosted evidence and draft/release state follow `references/qa-recipe.md`
and `references/workflow-intent.md`.
