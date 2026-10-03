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

Embed one complete props object in an `<lx-island name="Quiz">` with a single
JSON script child, in ordinary versioned page source. Empty question/result
arrays are not a valid starting definition. Use the public Quiz example or the
live schema, and replace illustrative IDs with the selected store's catalog IDs.

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
phone values are answer fields, not automatic subscriptions. Persisting any
answer requires the managed capture policy and shopper consent described below.

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

## Optional response saving

Definitions remain in page source. A version-bound capture policy controls
whether the published Quiz offers saving and which answers are retained.
Discover exact arguments before calling these actions:

| Action | Purpose and boundary |
|---|---|
| `lexsis_capture.quiz_inspect` | Read the saved page version's instances, hashes, and current capture state. |
| `lexsis_drafts.quiz_prepare` | Prepare an inactive definition and policy; does not enable collection. |
| `lexsis_live_ops.quiz_activate` | Activate the exact reviewed policy with explicit approval. |
| `lexsis_live_ops.quiz_deactivate` | Stop collection with explicit approval; retained responses are not deleted. |
| `lexsis_capture.quiz_responses` | Paginated retained response summaries, filtered by definition, status, and test mode. |
| `lexsis_capture.quiz_response` | Read one attempt; personal/sensitive values are redacted in MCP. |

Every call needs `store_id`; supply `workspace_id` explicitly when selection is
ambiguous. Inspect uses `page_id` and immutable `page_version_id`, not the display
version number. Prepare uses that version, `instance_id`,
`expected_definition_hash`, and `policy`. Activation/deactivation uses
`definition_id`, `expected_definition_hash`, and `expected_active_definition_id`
(the current ID, or null when none is active). Re-read conflicts; do not retry
with a guessed hash or silently replace another active definition.

Policy fields:

| Field | Contract |
|---|---|
| `version`, `mode` | `1`, `"responses"` |
| `purpose`, `disclosure` | State why answers are saved and explain the shopper's choice. |
| `fields` | Every `question_id`, classification (`categorical`, `personal`, `sensitive`), and `merchant_visible`. |
| `partial_retention_days` | 1-30 days for unfinished responses. |
| `completed_retention_days` | 1-365 days for completed responses. |
| `resume_ttl_minutes` | 1-10080 minutes for resume credentials. |
| `contact_fields`, `contact_purpose` | Optional email/phone/name plus a separate purpose when collecting contact. |

Choose the shortest retention that serves the stated purpose. The limits are
validation bounds, not recommended defaults. Do not misclassify contact, free
text, or sensitive questions as categorical to expose them through MCP.
The policy must cover every question, and resume cannot outlive unfinished
retention. Text, textarea, email, phone, and date cannot be categorical.

Saving is an unchecked choice; the visitor can continue without it. Contact
collection has a separate unchecked choice. Analytics consent is independent:
saving while analytics is denied can create a Forms response without events.
Neither saving nor contact collection sends results by email or enrolls marketing.

The managed service protects answer/contact values. Forms submissions reference
attempts rather than duplicating plaintext answers. When managed capture is
available, the browser does not persist a local raw-answer snapshot; scoped
credentials allow resume within policy and current-version limits. A result
screen is not proof of saving: wait for confirmed save status and inspect the
response. The merchant Forms viewer provides controlled reveal and export of
displayed answers; MCP exposes only merchant-visible categorical answers.

Prepare and activate the same version that will be published. Page publication
and policy activation require their own explicit authorization; an existing
approval for the exact scope remains valid. Editing source requires fresh
inspection and a matching policy. Preview does not collect production responses.
Normal visits used for testing a published page are not automatically test-mode
records. Respect response filters, pagination, and retention when verifying.

## Journey analytics

Quiz emits identifier-only `lx_quiz_*` events for exposure, start/resume/restart,
question views, committed/changed answers, skipped questions, branches, review,
validation/errors, completion, results, products, cart outcomes, and explicit
dismissal. Do not emit answer text, contact values, or question labels.
`analytics.answerAllowlist` remains a compatibility field and does not permit
raw answers. Respect analytics denial and preview suppression.

`lx_quiz_completed` means a result was reached. `lx_quiz_submission_saved` is a
server event for a persisted completion with analytics linkage. Cart outcome is
separate from both, and none of these proves payment. The current tools do not
provide a dedicated question drop-off or quiz-to-paid-order report. Missing
completion does not establish a specific exit point or cause.

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

Compile before creating or editing a draft. Review at 390, 768, and 1280. Verify:

- Every reachable branch and result
- Default and tied scores
- Back, review, restart, and resume behavior
- Required and optional answer validation
- Missing and unavailable exact variants
- Multiple Quiz instances when present
- Cart pending, success, partial, and error states
- Keyboard operation, focus visibility, selected state, and error
  announcements
- Mobile, tablet, and desktop layout without overflow
- Forward/back/review/result transition motion, keyboard focus after each change,
  reduced motion, and visible saving/error/retry states

Do not claim a Quiz is ready when only the start screen or happy path was
tested.

After authorized activation and publication, test on the returned published URL:

- Saving declined: the quiz still works and creates no saved response.
- Saving accepted and analytics allowed: confirmed save, one completed Forms row,
  and consented identifier-only events without duplicate counts on retry.
- Saving accepted and analytics denied: saved response with no quiz analytics.
- Edit/back/reload/retry: restored state within the active version and resume
  window, with visible failure handling when saving or resume is unavailable.
- Correct product/variant and final cart outcome; inspect existing promotions
  separately when gifts or discounts change the cart.

Store concise evidence in existing hosted QA/operation records, not local JSON
or screenshot bundles. Mark pre-publication capture checks pending, rather than
claiming preview captured a response. Distinguish a design approval from live
capture proof. Historical-version resume, preview capture, automatic result
email, dedicated funnel dashboards, and paid-order attribution remain deferred.
