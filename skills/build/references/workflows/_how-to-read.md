# How to read a workflow

The `workflows/` folder holds the two procedures every page type shares. The
per-type procedure lives inside each type file as its `## Workflow` block
(`references/page-types/<type>.md`, shaped by
`references/page-types/_checklist-format.md`). That block runs the context
reads for the type, then walks the Anatomy section by section, and for each
section it calls the two files here:

- `references/workflows/section-asset-workflow.md` decides the media: does
  the section need imagery, which job and aspect, where the image comes from
  (catalog, library, merchant-owned, allowed generation). When nothing covers
  a slot it tells the user what is missing and offers upload, generation
  where the policy allows it, or skipping the section; a section is never
  dropped silently.
- `references/workflows/island-selection-workflow.md` decides the interactive
  component from the same context reads (image count, variant axes, review
  band, page length, vertical). Islands and their schemas are resolved live
  with `lexsis_design.islands` and `lexsis_design.island_schema`; no
  reference file enumerates props.

Neither file repeats policy. Media policy is `references/assets/*.md`
(sourcing order, ALLOW / ASK / NEVER, jobs, slot specs, video, verticals);
trust policy is `references/proof/*.md`; house rules are
`references/design-rules.md`. When a workflow and a policy file seem to
disagree, the policy file wins and the workflow needs fixing.

## Reading order

1. `references/page-types/_index.md`: choose exactly one page type from the
   brief and record it.
2. `references/page-types/<type>.md`: read the whole file once, then follow
   `## Workflow` in order. Its `## Checklist` JSON is the default the workflow
   lands on, not a hard limit.
3. For each section in the Workflow's "Section by section" block, run the
   media loop, then the island decision, then write the copy to its ceiling.
4. Fill the Workflow's "Asset budget" table for this product: what the catalog
   and library already supply, which jobs are missing, and per gap what the
   user is offered: upload, generate (with the purpose) where the policy
   allows, or skip the section when they choose.
5. Note every departure from the type default and its reason.

`/plan-page` does steps 1 to 5 and writes the plan. `/design-page` re-reads
the same type file and executes the decisions; it reopens one only when live
catalog, asset or policy evidence contradicts the plan.

## How a plan records the decisions

All in `page-plan.md`, mirrored as ids only in `page-manifest.json`
(`references/page-files.md`):

- **Page type block**: Type, Funnel stage, Awareness, Traffic, Offer,
  Campaign, Copy framework, "Mandatory sections omitted" with a reason per id,
  and the **Deviations from the type default** line (field, new value,
  reason). A deviation with a reason is a decision; one without is a question.
- **Design direction**: palette, type, wireframe with a slot id on every
  media box, icons, emoji line, background rule, the one bold moment, motion,
  the generic-default check, overrides of the brand's design.md.
- **Imagery and background plan**: one line per imagery section naming its
  slot ids and treatment; the single full-bleed is the bold moment.
- **Asset slots**: one row per slot (Slot, Section, Role/purpose with the job,
  Aspect, Source decision with the step name and rights basis, Id / URL,
  Status `verified` or `planned`), plus a **Generation record** row for every
  generated slot. A `planned` row names the remedy offered to the user
  (upload, generate, skip); the same list appears in the draft summary as
  "Missing assets". The manifest `assets[]` carries ids, `sourceType`,
  `status`, and for generated slots `generated`, `provider` and, for ASK
  purposes, `askApproved`.
- **Proof ledger**: every star, count, quote, logo, badge and customer photo
  as a row with source, evidence and status before it renders.
- **Offer ledger**: exact terms, math, compare-at basis, dates, stock basis
  when the page carries any offer or urgency.
- Island decisions appear as a `Preset:` token or a one-line note per section;
  the plan never names schemas or props.

## What the lint is for

`python3 <plan-page-skill>/scripts/plan_lint.py <page-workspace>` compares the
plan and manifest with the type's checklist and prints WARN rows. It is
advisory: the WARN list is the deviation list, and each row should already
have a matching reason in the plan. `--strict` exits non-zero and is for CI
or when someone asks for a hard gate. The two cases that stop work regardless
of mode are a reviews section with no review data and urgency with no verified
basis; everything else is a conversation with the plan owner. `/design-page`
runs the same lint before composing and reads its rows next to the plan's
Deviations line.

## The order of thinking, on one screen

```text
Context reads          catalog media (count, jobs covered, variant images),
                       price and compare-at, selling plans, inventory,
                       review band, theme tokens and voice, library by tag,
                       ad creative when traffic is paid
Per section, in order  1. media: job, aspect, catalog, library tag, merchant
                          sources; if still missing, tell the user and offer
                          upload, generation where allowed, or skip
                       2. island: resolved live from the reads and the
                          island's schema
                       3. copy: pattern and ceiling, written to the image
Asset budget           supplied / missing / per gap: upload, generate
                       (purpose) where allowed, or skip on the user's word;
                       never a band, emoji, icon tiles or text
Deviations noted       every departure from the checklist with its reason;
                       lint WARN rows match this list
```

Precedence when files disagree: `design-rules.md`, then `references/assets/`
and `references/proof/`, then the type file, then the vertical and traffic
files, then these workflows and the tool-mechanics references
(`references/asset-prep.md`, `references/design-enrichment.md`,
`references/design-assets.md`).
