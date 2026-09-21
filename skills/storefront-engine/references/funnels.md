# Funnel Authoring

## Mental model

```text
Trigger -> Presentation -> Journey -> Outcome
```

A funnel is a reusable, versioned journey. It is not a page. The same journey
may eventually be placed on several pages with different triggers. A dedicated
funnel URL is a normal Lexsis page with the funnel placed inline.

The current MCP release supports complete draft creation, revision-guarded
replacement, authoritative validation, and isolated interactive preview. It
does not yet expose page placement, activation, or funnel publishing.

Start every custom definition with
`lexsis_capture.funnel_capabilities`.

## Version 2 definition

Every write sends one complete definition:

```json
{
  "schema_version": 2,
  "name": "Routine finder",
  "description": "Match shoppers to the right routine.",
  "type": "branching",
  "entry_step_key": "goal",
  "presentation": "modal",
  "trigger": { "type": "manual" },
  "settings": {},
  "steps": [
    {
      "key": "goal",
      "name": "Primary goal",
      "kind": "quiz_question",
      "config": {
        "question": "What would you like help with?",
        "field_key": "goal",
        "required": true,
        "options": [
          { "value": "hydrate", "label": "Hydration" },
          { "value": "clarify", "label": "Clarity" }
        ]
      },
      "transitions": {
        "rules": [
          {
            "when": {
              "field": "goal",
              "operator": "equals",
              "value": "clarify"
            },
            "goto": "clarity-result"
          }
        ],
        "default_goto": "hydration-result"
      }
    },
    {
      "key": "hydration-result",
      "name": "Hydration result",
      "kind": "offer",
      "config": {
        "title": "Your hydration routine",
        "cta_text": "View the routine"
      },
      "transitions": { "rules": [] },
      "outcome": { "type": "show_result", "target": {} }
    },
    {
      "key": "clarity-result",
      "name": "Clarity result",
      "kind": "offer",
      "config": {
        "title": "Your clarity routine",
        "cta_text": "View the routine"
      },
      "transitions": { "rules": [] },
      "outcome": { "type": "show_result", "target": {} }
    }
  ]
}
```

Defaults are schema version 2, modal presentation, and a manual trigger.
Step keys begin with a lowercase letter and use lowercase letters, numbers,
hyphens, or underscores. Keep step keys and `field_key` values stable when
revising an established funnel.

## Supported contracts

Journey types are `quiz`, `sequential`, and `branching`.

Step kinds are `page`, `quiz_question`, `offer`, `thankyou`, `email_capture`,
`gift_reveal`, and `product_recommendation`.

Condition operators are `equals`, `not_equals`, `in`, and `contains`. Every
non-terminal step needs a reachable next step. Use explicit rules for
meaningful branches and `default_goto` for the fallback path.

Presentation is `modal` for short, focused journeys or `inline` for longer
journeys and a future dedicated funnel page.

Trigger contracts are `manual`, `immediate`, `delay`, `scroll`,
`exit_intent`, `existing_button`, `inserted_button`, and `custom_event`.
Trigger-specific fields include `delay_seconds`, `scroll_percent`,
`event_name`, and `source_block_id`. These describe intended activation; they
do not attach or activate the draft.

Outcome contracts are `show_result`, `navigate_to_page`, `navigate_to_url`,
`navigate_to_product`, `navigate_to_collection`, `add_to_cart`, `open_cart`,
`start_checkout`, `capture_and_close`, and `show_thank_you`. Every terminal
path needs an explicit outcome. Resolve target identifiers from the active
store. The presence of an outcome does not prove live execution.

## Templates

Backend-owned starting points currently include `product-finder-quiz`,
`mystery-gift-reveal`, and `offer-capture`. Read the template before using it.
Customize the complete definition and validate it against the active store
instead of assuming its sample copy or result actions are suitable.

## Validation

Validation should reject or surface:

- duplicate or malformed step keys;
- duplicate field keys;
- missing entry steps or transition targets;
- unreachable steps, cycles, and non-terminal dead ends;
- terminal steps without outcomes;
- products or pages outside the selected store;
- invalid trigger parameters or unsupported node/outcome types.

Draft warnings may identify work that belongs to publication or activation.
Do not convert warnings into claims that the funnel is live.

## Revisions and preview

Draft replacement is atomic. Read the latest draft, preserve its complete
definition, and send the returned revision as `expected_revision`. On a
revision conflict, re-read and reconcile rather than retrying stale content.

Preview URLs are signed, isolated, and expire after 15 minutes. Exercise each
reachable answer path. Preview answers remain in the preview and create no
lead captures or analytics. A successful preview proves draft interaction
only; it does not prove page placement, live triggers, outcome execution, or
publication.
