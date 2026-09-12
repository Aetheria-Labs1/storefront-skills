# Shared page workflow

The compiler determines valid input. `references/design-rules.md` owns house
requirements; domain policy owns evidence and permissions. The selected
page-type contract owns anatomy and type-specific decisions. Workflows
execute those decisions, never relax their requirements.

## Reading order

1. Select one contract through `references/page-types/_index.md`.
2. Read its context requirements and checklist. Keep the required headings
   and JSON contract; record deviations with their reasons.
3. During planning, turn each section row into final copy, layout intent,
   proof decisions, interaction intent, and production asset requirements.
4. `/plan-assets` later resolves those jobs through the asset workflow;
   `/design-page` selects implementation schemas and performs hosted review.

## Four procedures

| Procedure | Single home | Type-specific inputs |
|---|---|---|
| Asset acquisition and missing-slot handling | owned by `/plan-assets` | Job, source/tag, crop, required count and legitimate fallback |
| View and section fit | owned by `/plan-assets` | Product/variant, composition, adjacent slots and intended crop |
| Interactive selection | `references/workflows/island-selection-workflow.md` | Candidate family and the decision that requires behavior |
| Copy execution | `references/workflows/copy-workflow.md` | Message, evidence, specific ceilings and CTA destination |

A type file supplies the differences, not another copy of these procedures.
"Media: no" is a valid type-specific decision; not every section needs an
image. Static facts, native disclosures and tables remain legitimate content.

## Planning and design responsibilities

`/plan-page` resolves context and asset requirements, records functional
intent and visual direction, and names deviations. `/plan-assets` resolves
production media. `/design-page` executes the interactive-selection procedure
against current schemas, then compiles the source. Reopen a planned decision
only when new evidence or a contract conflict requires it.

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
