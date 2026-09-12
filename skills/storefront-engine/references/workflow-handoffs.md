# Public Storefront Workflow

The customer-facing pack has seven commands. Four form the normal page
journey:

```text
/setup
  U+2192 /plan-page
  U+2192 /design-page
  U+2192 /publish
```

| Command | Owns | Main output |
|---|---|---|
| `setup` | Saved store and theme design context | `setup.json` and design files |
| `plan-page` | The complete page specification: final section copy, an asset decision per section, claim gate, work queue and plan status | approved `page plan` (`PLAN_APPROVED`) |
| `design-page` | Plan gate, assets, islands, source, compile, one hosted draft, hosted QA at 390, 768 and 1280, later edits | `DRAFT_CREATED`, then `DESIGN_APPROVED` after hosted QA |
| `publish` | Explicit live release | published version |

Three optional commands support the workflow:

| Command | Owns |
|---|---|
| `optimize` | Score an existing page, propose a strict optimization plan, apply approved changes |
| `ab-test` | URL-first controlled variants and experiment evaluation |
| `cart` | Cart profile inspection, assignment, and editing |

## Rules

1. Each command owns one outcome and can be invoked independently.
2. Commands read artifacts from earlier steps but never invoke earlier steps
   automatically.
3. Explicit skips are recorded in the page record.
4. Every page binds one saved store/theme pair.
5. Persisted MCP source and version are the edit baseline.
6. Draft creation is not publishing approval.
7. Infer only question depth and publish-versus-draft intent from the whole
   request; the plan is always approved before design.
8. A visual concept is optional evidence inside `design-page`, not production
   page media.
9. Design creates `DRAFT_CREATED`, runs hosted QA and edits, and owns
   `DESIGN_APPROVED`; `publish` gates on it for the same version.
