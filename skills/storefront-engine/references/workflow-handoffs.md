# Public Storefront Workflow

The customer-facing pack has ten commands. Five form the normal page journey:

```text
/setup
  → /plan-page
  → /design-page
  → /generate
  → /publish
```

| Command | Owns | Main output |
|---|---|---|
| `setup` | Saved store and theme design context | `setup.json` and design files |
| `plan-page` | One-page campaign and section strategy | approved `page-plan.md` |
| `design-page` | Assets, islands, source, and responsive preview | canonical source and preview |
| `generate` | Production source, draft, and hosted QA | `DRAFT_READY` |
| `publish` | Explicit live release | published version |

Four optional commands support the workflow:

| Command | Owns |
|---|---|
| `analyze-page` | URL, screenshot, ad, or own-page analysis |
| `asset-prep` | Independent asset search, generation, import, or replacement |
| `optimize` | Outcome-led existing-page improvement |
| `experiment` | Controlled variants and result evaluation |
| `cart` | Cart profile inspection, assignment, and editing |

## Rules

1. Each command owns one outcome and can be invoked independently.
2. Commands read artifacts from earlier steps but never invoke earlier steps
   automatically.
3. Explicit skips are recorded in the page manifest.
4. Every page binds one saved store/theme pair.
5. `lexsis-source.html` is the production source of truth.
6. Draft creation is not publishing approval.
