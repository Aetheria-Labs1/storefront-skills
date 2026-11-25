# URL-First A/B Testing

Build a controlled Lexsis page experiment from an existing landing-page URL.
The URL may use the Lexsis storefront domain or a connected custom domain, but
the resolved page must belong to a workspace the user can edit.

## Inspect and Resolve the Control

Open the supplied URL with the browser capability available in the host:
Codex's browser, Claude Code with Playwright, or an equivalent browser tool.
Inspect desktop and mobile before proposing a test. Capture:

- headline, offer, CTA, media, proof, section order, and visual hierarchy;
- responsive behavior and obvious usability problems;
- interactive commerce behavior relevant to the proposed change;
- the current page title and URL path.

If no browser is available, accept current screenshots from the user and state
which behavior could not be verified. Do not claim a visual review from source
alone.

Extract likely handles or short ids from the path and resolve the owned page
with `lexsis_pages` action `find`. Confirm the match with `get`,
`edit_context`, and `source`. For a custom domain or root route that does not
map cleanly to one page, compare the observed title and content with the
candidate pages and ask the user only when more than one remains plausible.
Stop if the URL is not an editable Lexsis page; for external inspiration,
inspect the URL in the host browser.

## Define One Hypothesis

After inspection, present the strongest testable opportunities and ask what
the user wants to test. Supported scope includes:

- headline, supporting copy, offer, or CTA;
- CSS, typography, spacing, color, or layout;
- hero or other media;
- adding, removing, reordering, or replacing sections;
- mobile presentation;
- an island or commerce interaction supported by the current schema.

Confirm the primary hypothesis, primary metric (`cvr`, `aov`, or `rpv`),
protected elements, audience or segment, traffic weights, and stopping rule.
Default to the control plus one challenger with equal traffic. Add more
challengers only when the user explicitly asks and approves the additional
credit cost.

One experiment should isolate one decision. A design challenger may contain
coordinated CSS changes that express one visual hypothesis, but do not bundle
an unrelated headline, offer, section order, and design rewrite into the same
challenger.

For offer, positioning, or pricing tests, use
`references/offers/offer-strategy.md` and carry the relevant Page strategy
rationale into the hypothesis. Default price/offer economics tests to `rpv`;
review `cvr` and `aov` alongside it. Record merchant-supplied contribution
margin, refund, or retention guardrails when available, with their sources
and measurement windows. Do not invent native profit metrics or call higher
AOV a profit improvement when costs are unknown.

For an actual price change, record the confirmed commerce configuration that
honors each arm's price, eligibility, and recurring terms from page through
cart and checkout. If that support is unavailable, leave the test as a proposal;
do not duplicate, build, or activate price challengers that only change the
displayed price. A presentation-only test keeps payable terms unchanged.
Preserve existing rules against preselecting multipacks, paid add-ons, or
subscriptions, and retain the existing promotional tier-badge rules.

Write `ab-test-plan.md` with:

- observed control evidence;
- hypothesis and rationale;
- control and challenger definitions;
- exact intended differences and protected elements;
- metric, audience, weights, and stopping rule;
- required browser and commerce checks.

Return `AB_TEST_PLAN_READY` and obtain approval before paid page duplication.

## Create Source-First Challengers

Check credits and state the number of paid duplicates before creating them.
For each approved challenger:

1. Prepare an isolated source value from the current persisted control.
2. Apply only its planned change.
3. Compile the complete source and fix blocking compiler errors.
4. Call `lexsis_drafts` action `page_duplicate` with a stable idempotency key.
5. Apply the challenger change to the duplicate with `lexsis_build.patch` or
   `lexsis_build.commit` (only the changed files, `base_version` from
   `lexsis_build.get` on the duplicate).
6. Record the duplicate page id, blueprint id, version and
   compile evidence.
7. Run page integrity, affected commerce checks, and browser checks at mobile
   and desktop widths.

Do not use `page_variation` for this workflow: it creates a 50/50 experiment
before the challenger has been authored and verified.

When sub-agents are available, give one isolated source challenger to each
sub-agent. The parent owns the control, shared plan, compilation review,
credit confirmation, duplicate calls, remote writes, and experiment creation.
Sub-agents never spend credits or mutate remote pages. Without sub-agents,
build challengers sequentially using the same isolation.

Before experiment creation, compare control and challenger source and confirm
that every visible difference is covered by the approved plan. Return
`AB_VARIANTS_READY` with all preview URLs.

## Create the Draft Experiment

Ask which goal the test is judged on before creating it; it cannot be changed
later:

- `cvr` (conversion rate, the default): use when prices are the same across
  arms.
- `rpv` (revenue per visitor): use when the arms change price, offer, bundle
  or anything else that moves order value.

Lexsis nominates a winner candidate on the chosen goal when one is
statistically clear. A person always confirms it.

After variant approval, call `lexsis_drafts.page_split_create` using the live
schema. Supply:

- the store id and a name;
- one arm per page: the original page id as the control (`is_control`), each
  duplicate page id as a challenger;
- approved labels and `weight_bps` summing to 10000;
- `primary_metric` and the hypothesis.

Experiment creation is a reversible draft operation. Return
`AB_TEST_DRAFT_CREATED` with the experiment id, goal metric and arm mapping.

## Prepare the Test

Call `lexsis_drafts.page_split_prepare` with step `start`. Preparing freezes
every arm at its page's current version and renders it. It does not affect
visitors and needs no extra approval beyond the approved plan.

Poll step `status` every few seconds until the run is `ready` or `failed`:

- `ready`: continue to starting the test.
- `failed`: report `error_code`, `error_message` and the failing arm. Fix the
  page if the error names one, then call step `retry`.
- To change arms, weights or pages after preparing, call step `reopen`, make
  the edit with `lexsis_drafts.page_split_update` or the page tools, and
  prepare again. Page edits made after preparing are not in the test until
  then.

## Start the Test

Starting sends real visitors to the arms. Require explicit approval that names
the experiment, its arms and traffic split. Never treat plan approval,
experiment creation or preparation as permission to route live traffic.

After approval, call `lexsis_live_ops.page_split_control` with step `start`.
Report every URL in the response with its checked state, not only the first.
If the call fails:

- `experiment_not_prepared`: prepare first.
- an entitlement error such as `active_experiment_limit_reached`: tell the
  user which limit was hit; do not stop another test to make room unless
  asked.
- the test did not go live: repeat step `start` once, then report the error.

The same action runs the test afterwards, each step after approval: `pause`
serves the control to everyone, `resume` splits again, `stop` ends the test
with no winner and cannot be undone.

## Evaluate

For later evaluation, read `lexsis_analytics` action `experiment` and report:

- exposure and sample size per arm;
- primary and guardrail movement;
- statistical decision returned by Lexsis;
- device, targeting, or data-quality concerns;
- recommended next action: continue, pause, stop, or promote.

Do not call a winner from directional movement alone. To end a page-split
test on a winner, call `lexsis_live_ops.page_split_control` with step `winner`
and the arm id; it is a live operation and requires explicit approval for the
named arm.

- Pick the winner candidate Lexsis reports for the test's goal. On an `rpv`
  test also report the conversion-rate movement, so the user sees both.
- Any other arm needs `manual: true` and the user's explicit choice.
- A holdout's theme arm cannot be the winner.

`scale_winner` applies only to legacy blueprint experiments.
