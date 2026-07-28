---
description: Generate a complete Shopify storefront page — auto-detects page type (landing, PDP, collection, homepage, editorial, listicle, bundle) and applies conversion-optimized patterns
allowed-tools: mcp__lexsis-ai__*
---

# /generate

Generate a complete Shopify storefront page with conversion-optimized patterns.

## Context

- **storefront-craft**: Load first on any generation task.
- **workflow-orchestration**: Tool sequences, parallelization, flow selection.
- **conversion-psychology**: Read before generating any ecommerce page.
- **island-patterns**: How to embed, wrap, and combine React islands.

## Workflow

> **STOP — Planning Required First**
> Before running any generation phase, execute the Page Planning workflow.
> Assess what the user has told you, ask clarifying questions if < 4 signals are present, generate a section plan, and get user approval.
> Do NOT proceed to Phase 0 until a page plan is confirmed by the user.
> Exception: If user explicitly says "skip planning" or "just build it".

See `reference/page-generation.md` for the full generation flow (Phase 0-4).
See `reference/generation-protocol.md` for VibePage schema, CSS variables, island integration, and visual verification.

## Ad-to-Page Shortcut

When converting an ad creative to a landing page:
1. `analyze_ad_creative` → extract headline, claims, colors, tone, CTA
2. `match_persona_to_ad` → identify target audience
3. Continue with standard Phase 0-4 using extracted context
4. Ensure "scent continuity" — ad headline ≈ page hero headline

See `reference/ad-to-page.md` for the full ad-to-page workflow.
