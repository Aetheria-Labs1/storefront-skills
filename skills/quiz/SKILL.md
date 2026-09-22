---
name: quiz
description: Create, update, validate, or preview a Lexsis Quiz island for product finders, assessments, branching journeys, variant matching, profile scoring, and guided recommendations.
---

# Create a Quiz

Use the live `Quiz` island rather than a funnel runtime, hidden commerce
controls, or a custom section state machine.

Read `references/quiz-authoring.md` before authoring or
changing a quiz. Read the current `vibe://schema/island/Quiz` resource before
compilation because the schema is the contract authority.

## Workflow

1. Resolve the exact workspace, store, page, and theme.
2. Inspect real candidate products and variants with `lexsis_catalog`; never
   invent Shopify IDs, prices, availability, or option values.
3. Define the journey before writing source:
   - Stable quiz, question, option, product, and result keys
   - Question order and conditional paths
   - How every meaningful answer changes scoring, eligibility, variant
     selection, or the final result
   - Deterministic fallback result
   - Result products, reasons, quantities, and actions
4. Author one complete `Quiz` props definition in normal page source.
5. Build the design through surrounding HTML, theme variables, and
   section-scoped CSS. Do not use or invent runtime design presets.
6. Compile and repair every blocking validation issue.
7. Create or update only the requested unpublished page draft with version
   protection.
8. Exercise every reachable path, fallback, unavailable-product state,
   required variant choice, restart, resume, and Cart V2 result action at
   mobile and desktop widths.

## Boundaries

- Quiz definitions live in page source, not Forms.
- Email and phone question values remain local quiz answers; do not claim they
  were captured or subscribed.
- Result commerce uses Quiz `add_items`; do not add hidden BuyBoxes, direct
  Shopify requests, authored cart shells, or programmatic clicks.
- `reward` and `offer` actions are unavailable until a managed reward service
  exists.
- Use only renderer islands returned by the live schema. Host-only renderers
  cannot be placed directly in page source.
- If scoped CSS and the default Quiz structure cannot express the requested
  interaction, report that a reusable engineering-owned Quiz host island is
  required. Do not fabricate an island name or inject arbitrary JavaScript.
- Templates may be consulted as examples when available, but remain editable
  source—not runtime presets or hidden dependencies.

## Return

Report the page and version, hosted preview, question and result count, logic
types used, reachable paths tested, product and variant sources, Cart V2
evidence, responsive QA, and any unsupported interaction that needs a reusable
host island.
