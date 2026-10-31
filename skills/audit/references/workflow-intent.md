# Storefront Workflow Intent

Infer the outcome the user wants from their words, the current conversation,
the requested deliverable, and the reversibility of the next action. Do not
require a magic phrase.

## Modes

| Mode | Typical intent | Outcome |
|---|---|---|
| `fast-draft` | create, try, show, preview, explore, iterate, make a first version, move quickly | ask fewer optional questions; the plan is still complete and approved before design |
| `production-ready` | final polish, campaign handoff, exhaustive QA, launch preparation, ready for review | collect every optional choice explicitly; `DESIGN_APPROVED` only after hosted QA |
| `publish` | release, launch live, publish this version | use the separate publish workflow and require explicit approval for the named page/version |

Signals such as "assume specifics", "use your judgment", "do whatever is
needed", or impatience with questions strengthen `fast-draft`; they are not
required. A previous request for a preview or first pass also counts.

## Routing Rules

1. Prefer the outcome implied by the whole request, not one keyword.
2. If the next action is reversible and intent is reasonably clear, proceed
   and state the inferred mode briefly.
3. If question depth is ambiguous, ask fewer questions; never skip plan
   approval.
4. Ask only when the missing choice would materially change the campaign,
   spend credits, publish, delete, overwrite shared work, or perform another
   consequential action.
5. Inferred intent never authorizes publishing, paid generation, deletion, or
   destructive replacement.
6. A user correction overrides the inference immediately.

## Manifest Evidence

Record compact evidence under `workflow`:

```json
{
  "intentMode": "fast-draft",
  "intentConfidence": "high",
  "intentSignals": ["asked to create a preview", "delegated specifics"],
  "userOverride": false
}
```

Use `high`, `medium`, or `low` confidence. Keep signals short and derived from
the request; do not store private chain-of-thought or long conversation text.
