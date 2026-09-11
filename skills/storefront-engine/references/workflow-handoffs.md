# Public Storefront Workflow

The customer-facing pack has twelve commands. Five form the normal page
journey:

```text
/setup
  U+2192 /plan-page
  U+2192 /design-page
  U+2192 /generate
  U+2192 /publish
```

| Command | Owns | Main output |
|---|---|---|
| `setup` | Saved store and theme design context | `setup.json` and design files |
| `plan-page` | One-page campaign and section strategy | approved `page plan` |
| `design-page` | Assets, islands, source, compile, and hosted design review | `DRAFT_CREATED` or `DESIGN_APPROVED` |
| `generate` | Draft creation when needed, then synchronization and hosted QA | `DRAFT_CREATED` or `DRAFT_READY` |
| `publish` | Explicit live release | published version |

Seven optional commands support the workflow:

| Command | Owns |
|---|---|
| `analyze-page` | URL, screenshot, ad, or own-page analysis |
| `asset-prep` | Independent asset search, generation, import, or replacement |
| `optimize` | Outcome-led existing-page improvement |
| `ab-test` | URL-first controlled variants and experiment evaluation |
| `cart` | Cart profile inspection, assignment, and editing |
| `build` | Fast unpublished draft from a prompt or selected/automatic page kit |
| `build-with-template` | Fast unpublished draft from an explicit template URL |

## Rules

1. Each command owns one outcome and can be invoked independently.
2. Commands read artifacts from earlier steps but never invoke earlier steps
   automatically.
3. Explicit skips are recorded in the page record.
4. Every page binds one saved store/theme pair.
5. Persisted MCP source and version are the edit baseline.
6. Draft creation is not publishing approval.
7. Infer fast-draft versus production-ready intent from the whole request;
   reversible ambiguity defaults to fast-draft.
8. A visual concept is optional evidence inside `design-page`, not production
   page media.
9. Design and fast-build routes create `DRAFT_CREATED`; `generate` reuses that
   draft and owns upgrading it to `DRAFT_READY`.
