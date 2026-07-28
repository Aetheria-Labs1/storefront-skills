---
description: Generate a complete Shopify storefront page — auto-detects page type (landing, PDP, collection, homepage, editorial, listicle, bundle) and applies conversion-optimized patterns
allowed-tools: mcp__lexsis-ai__*
---

# /generate

Generate a complete Shopify storefront page with conversion-optimized patterns.

## Context

- **storefront-craft**: Load first on any generation task.
- **conversion-psychology**: Read before generating any ecommerce page.
- **island-patterns**: How to embed, wrap, and combine React islands.

## Workflow

> **STOP — Planning Required First**
> Before running any generation phase, execute the Page Planning workflow.
> Assess what the user has told you, ask clarifying questions if < 4 signals are present, generate a section plan, and get user approval.
> Do NOT proceed to Phase 0 until a page plan is confirmed by the user.
> Exception: If user explicitly says "skip planning" or "just build it".

1. Read `vibe://skills/plan-page` — execute planning (signal check → questions → plan → approval)
2. Read `vibe://skills/generation-protocol` — execute Phase 0-4 (context → assets → HTML → validate → publish)
3. Read the page-type doc matching the plan (e.g. `vibe://skills/generate-pdp`) — apply CRO patterns

## Ad-to-Page Shortcut

When user provides an ad creative:
1. Read `vibe://skills/ad-to-page` — execute the ad-to-page workflow
2. `analyze_ad_creative` → extract headline, claims, colors, tone, CTA
3. `match_persona_to_ad` → identify target audience
4. Continue with Phase 0-4 using extracted context
