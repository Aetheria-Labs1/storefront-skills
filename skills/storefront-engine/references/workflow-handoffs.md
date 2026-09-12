# Public Storefront Workflow

```text
/setup
  U+2192 /plan-page
  U+2192 /visualize-page (optional and repeatable)
  U+2192 /plan-assets
  U+2192 /design-page
  U+2192 /publish
  U+2192 /ab-test
```

| Command | Owns | Main output |
|---|---|---|
| `setup` | Structured reusable store context | `setup.md`, brand, design, products, personas, rules, themes |
| `plan-page` | Strategy, final copy, sections, proof, offers, claims, responsive layout, asset requirements, template direction | `PLAN_APPROVED` |
| `visualize-page` | Optional iterative concept frames | `VISUAL_DIRECTION_APPROVED` or `VISUAL_DIRECTION_SKIPPED` |
| `plan-assets` | Production asset inventory, choices, import/upload, permitted generation/editing, persistence and verification | `ASSETS_READY` |
| `design-page` | Source, islands, compilation, one unpublished hosted draft and hosted QA | `DESIGN_APPROVED` |
| `publish` | Explicit live release | published version |
| `ab-test` | Controlled challengers and experiment evaluation | experiment status |

`optimize` and `cart` remain independently invokable operations.

## Handoff Rules

1. Each command owns one outcome and never silently performs an earlier stage.
2. `/plan-page` contains final copy and production requirements, not asset
   execution or implementation schemas.
3. `/visualize-page` is optional. Its concept images are design evidence, not
   production page media.
4. `/plan-assets` begins only from `PLAN_APPROVED` and returns permanent
   verified bindings.
5. `/design-page` requires `PLAN_APPROVED` and `ASSETS_READY`; visual approval
   is optional.
6. A visual or asset decision that changes strategy, sections, claims, offer,
   or copy returns to `/plan-page`.
7. Draft creation does not imply publication approval.
8. Every page binds one workspace, store, and theme.
9. Paid generation and live publication each retain their own explicit
   approval.
