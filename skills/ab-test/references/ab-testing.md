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
Stop if the URL is not an editable Lexsis page; external inspiration belongs
to `/analyze-page`.

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

Write `ab-test-plan.md` with:

- observed control evidence;
- hypothesis and rationale;
- control and challenger definitions;
- exact intended differences and protected elements;
- metric, audience, weights, and stopping rule;
- required browser and commerce checks.

Return `AB_TEST_PLAN_READY` and obtain approval before paid page duplication.

## Create Local-First Challengers

Check credits and state the number of paid duplicates before creating them.
For each approved challenger:

1. Create an isolated local directory from the synchronized control source.
2. Apply only its planned change.
3. Compile the complete source and fix blocking compiler errors.
4. Call `lexsis_drafts` action `page_duplicate` with a stable idempotency key.
5. Apply the compiled challenger source to the duplicate with `page_replace`
   or the smallest safe section action using `expected_version`.
6. Record the duplicate page id, blueprint id, version, source path, and
   compile evidence.
7. Run page integrity, affected commerce checks, and browser checks at mobile
   and desktop widths.

Do not use `page_variation` for this workflow: it creates a 50/50 experiment
before the challenger has been authored and verified.

When sub-agents are available, give one isolated local challenger to each
sub-agent. The parent owns the control, shared plan, compilation review,
credit confirmation, duplicate calls, remote writes, and experiment creation.
Sub-agents never spend credits or mutate remote pages. Without sub-agents,
build challengers sequentially using the same isolation.

Before experiment creation, compare control and challenger source and confirm
that every visible difference is covered by the approved plan. Return
`AB_VARIANTS_READY` with all preview URLs.

## Create the Draft Experiment

After variant approval, call `lexsis_drafts` action `experiment_create` using
the live schema. Supply:

- the original page id;
- original blueprint as the control;
- duplicate blueprint ids as challengers;
- approved labels and weights summing to 1;
- the supported primary metric and hypothesis fields.

Experiment creation is a reversible draft operation. Return
`AB_TEST_DRAFT_CREATED` with the experiment id and variant mapping.

Starting traffic is separate. Before publishing variants or starting the
experiment, require explicit approval that names the experiment and pages.
Resolve the current start action through exact discovery if it is exposed; if
the MCP has no start action, direct the user to activate the draft in Lexsis.
Never treat experiment creation as permission to publish pages or route live
traffic.

## Evaluate

For later evaluation, read `lexsis_analytics` action `experiment` and report:

- exposure and sample size per arm;
- primary and guardrail movement;
- statistical decision returned by Lexsis;
- device, targeting, or data-quality concerns;
- recommended next action: continue, pause, stop, or promote.

Do not call a winner from directional movement alone. `scale_winner` is a live
operation and requires explicit approval for the reported winning variant.

