# Optional Workflow Connections

Each skill owns one outcome and can run independently. The connections below
describe reusable outputs, not mandatory sequencing.

| Skill | Owns | Output | May inform |
|---|---|---|---|
| `storefront-engine` | Routing only | Selected workflow | One owner from this table |
| `browser-analyze` | Browser capture and raw evidence | `PAGE_ANALYSIS_INPUT` | `analyze-page`, `remix`, or `optimize` |
| `analyze-page` | Reference page structural analysis | `VISUAL_PAGE_INPUT` | `visual-page` |
| `remix` | Brand-safe reference/ad adaptation brief | `VISUAL_PAGE_INPUT` | `visual-page` |
| `plan-page` | Standalone approved content and section plan | `PAGE_PLAN` | `asset-prep` or `visual-page` |
| `visual-page` | New-page visual layout concept and single approval | approved plan + layout brief | `asset-prep` |
| `asset-prep` | Final production asset sourcing | `ASSET_MANIFEST` | `generate` |
| `generate` | Source-format page, compile, draft preview, visual QA | `DRAFT_READY` | `publish` |
| `publish` | Live release or lifecycle action | live status | `experiment` or `optimize` |
| `optimize` | Existing-page, performance-led improvements | validated page update | `publish` or `experiment` |
| `experiment` | Controlled variants and result evaluation | winner or learning | `optimize` |
| `cart` | Cart profile configuration | reviewed cart profile | `generate` only if page integration changes |
| `search-docs` | Documentation lookup | answer and selected workflow | matching owner |
| `extract-island` | Maintainer reusable island layout | contribution-ready layout | maintainer review |

## Connection Rules

1. Pass compact named artifacts, not a second copy of upstream instructions.
2. Preserve tenant-scoped asset and product identifiers.
3. A layout concept is composition guidance only, never final page media.
4. A `DRAFT_READY` page is not live. Only `publish` can release it after
   explicit user approval.
5. Stop after the requested outcome. Follow a connection only when the user
   asks for the downstream outcome.
