# Quiz authoring

Use `Quiz` for any deterministic interaction that collects answers and
resolves content, products, exact variants, navigation, or Cart V2 actions.
Examples include product finders, shade and size matching, assessments,
calculators, gift finders, routine builders, profile quizzes, and guided
selling.

Search aliases: product finder quiz, branching assessment, variant matching
quiz, guided recommendation.

## Source of truth

Read `vibe://schema/island/Quiz` immediately before authoring. The current
schema defines available fields, limits, host roles, and styling hooks.

The definition is embedded in ordinary versioned page source:

```html
<lx-island name="Quiz" hydrate="visible">
  <script type="application/json">
    {
      "schemaVersion": 1,
      "quizKey": "routine_finder",
      "content": {
        "title": "Find your routine"
      },
      "questions": [],
      "results": [],
      "fallbackResultKey": "balanced"
    }
  </script>
</lx-island>
```

Do not put resolved product data, current prices, inventory, or authored
copies of Shopify variants in production source. Use `lexsis_catalog` to
resolve real Product and ProductVariant GIDs; the renderer hydrates current
commerce facts.

## Definition design

Use stable lowercase IDs. Each meaningful answer must affect at least one of:

- Next question
- Product or result score
- Eligibility or exclusion
- Named profile score or trait
- Exact variant mapping
- Result explanation

Delete questions that do not change the journey or provide necessary context.
Always define a deterministic fallback result.

Supported question families include choices, booleans, scales, numeric
ranges, numbers, selects, text, textarea, email, phone, and date. Email and
phone are local answer values in this release; they are not Forms submissions.

## Logic choices

- Put simple weights directly on option `effects`.
- Use `dynamicScoring.entries` when the same answer affects several products,
  variants, results, or profiles.
- Use `rules` for nested if/then eligibility, traits, forced results, badges,
  reasons, and variant-option selection.
- Use `branches` to skip irrelevant questions or terminate early.
- Use `pointProfiles` when answers first produce a shopper characteristic and
  that characteristic determines the result.
- Use `variantMatrices` when answers must resolve an exact Shopify SKU.

These systems may be combined. Keep rule priority explicit and verify tied
scores resolve predictably.

## Products and actions

Declare Shopify products once in `catalog` and reference their stable keys
from results. Every recommended product should include a concise reason tied
to the shopper's answers.

Use `add_items` for one or several recommended products. Quiz constructs one
renderer-managed `lx:cart:add-items` request and uses the effective Cart V2
profile. Never call Shopify directly or click hidden controls.

Use `view_product`, `navigate`, or `restart` for non-cart outcomes.
Do not use `reward` or `offer`; those require a future managed adapter.

## Custom visual design

There are no Quiz presets. Create the requested design through:

- Surrounding section HTML
- Page theme variables
- Quiz content and layout props
- Scoped CSS targeting the schema's `data-part`, `data-state`,
  `data-selected`, `data-question-id`, `data-result-key`, and availability
  hooks

The page-authored island remains `Quiz`. `QuizExperience`, `QuizInput`, and
`QuizResult` are host-only default renderers and cannot be placed directly.

Use a custom registered host only when it appears in the current schema with
the required `quiz:experience`, `quiz:input`, or `quiz:result` capability.
When the desired structure cannot be built with the default hooks, request a
reusable host-island implementation rather than inventing one.

Templates may later package complete Quiz definitions, section composition,
and CSS as examples. Adapt them to the current store and products; do not
treat them as hardcoded runtime modes.

## QA

Compile before creating or editing a draft. Verify:

- Every reachable branch and result
- Default and tied scores
- Back, review, restart, and resume behavior
- Required and optional answer validation
- Missing and unavailable exact variants
- Multiple Quiz instances when present
- Cart pending, success, partial, and error states
- Keyboard operation, focus visibility, selected state, and error
  announcements
- Mobile and desktop layout without overflow

Do not claim a Quiz is ready when only the start screen or happy path was
tested.
