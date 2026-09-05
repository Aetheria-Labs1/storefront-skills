---
name: plan-page
description: Turn campaign and product requirements into a concise one-page storefront section plan. Use before page design; this skill does not choose islands or implementation details.
---

# Plan a Page

Produce a concise strategy and section blueprint that can be reviewed quickly.

Read:

- `references/page-files.md`

Use `lexsis_catalog.list`, `lexsis_catalog.get`,
`lexsis_template_library.search_page_kits`, and
`lexsis_template_library.search_sections`. Resolve an unfamiliar schema with
exact router/action discovery.

Read `work/storefront/setup/setup.json`, select one saved store/theme pair, and
read its brand design. If the selection is not saved, stop with
`Run /setup for this store and theme first.`

## Ask Only What Is Missing

Collect:

1. Page or campaign type.
2. Product or collection.
3. Audience and customer problem.
4. Traffic source.
5. Primary conversion goal and CTA.
6. Required proof, offer, claim, or section constraints.

Ask no more than four questions at once. Read current products, variants,
prices, and availability from Lexsis.

## Choose a Direction

Search page kits using the page type, objective, industry, and mood. If no kit
fits, inspect the returned status before deciding why:

- A successful catalog response with zero results means that shelf is empty.
  Continue with section search or a custom direction; do not make an unrelated
  control call merely to prove the service works.
- A failed request is a tool error, not an empty shelf. Report it and use only
  an explicitly documented fallback.

Search sections for useful structural references when no page kit fits. Record
only the selected kit or section IDs in the manifest; put the short selection
rationale in the plan.

Template selection at this stage is directional. `/design-page` owns fetching
source, adapting layouts, selecting islands, and resolving schemas.
The plan must not define islands.

## Write a One-Page Plan

Keep `page-plan.md` concise enough to scan in one view. Include:

- objective, audience, traffic source, product, and primary CTA
- selected template direction
- ordered section list
- one sentence describing each section's purpose
- broad media roles such as hero, product media, or lifestyle proof
- offers and claims that require confirmation

Verify facts that control the page's urgency or trust before treating them as
copy. This includes occasion dates, delivery cutoffs, prices, availability,
medical or performance claims, certifications, endorsements, and legal or
safety language. Use an authoritative current source where one exists. Mark an
unverified item as unresolved in the plan instead of guessing it.

Do not include:

- island names or schemas
- island props or hydration modes
- HTML, CSS, Tailwind classes, or implementation notes
- detailed asset records
- template search transcripts
- QA, compilation, synchronization, or publishing state

Create the page directory, `assets/`, and a compact schema-v3
`page-manifest.json` using `references/page-files.md`. Do not create source,
preview, compile, or QA files.

## Approval

Present:

```text
Page:
Goal:
Audience:
Template direction:
Sections:
Media needed:
Claims to confirm:
```

Wait for approval.

## Return

Return the working directory, plan path, manifest path, and `PLAN_APPROVED`.
The next normal command is `/design-page`.
