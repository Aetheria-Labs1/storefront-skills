---
name: plan-page
description: Plan a storefront page before generation. Use to gather requirements and create an approved section, animation, and visual-rhythm blueprint.
---

# Plan Storefront Page

Plan a storefront page before generation — gathers requirements, designs section layout, animations, and visual rhythm.

## Context

- **storefront-craft**: Load this skill first on any storefront page generation task.
- **conversion-psychology**: Read before planning any ecommerce page.

## Workflow

# Page Planning Workflow

> This produces a structured page blueprint. Run it standalone, or use it as Phase 1 before `$generate`.

## Step 1 — Assess What's Known

Score the user's input:

| Signal | Check |
|--------|-------|
| Page type (landing, PDP, homepage, collection, editorial, listicle, bundle) | stated? |
| Target audience / persona | described? |
| Products or collection to feature | named? |
| Traffic source (Meta, Google, TikTok, email, organic) | mentioned? |
| Conversion goal (purchase, signup, browse) | clear? |
| Reference URL or ad creative | provided? |
| Tone/style preference | specified? |

- **4+ signals present** → proceed to Step 3 (auto-plan)
- **< 4 signals** → proceed to Step 2 (ask questions)

## Step 2 — Adaptive Discovery

Ask ONLY questions whose answers are missing. Never ask more than 4 at once.

**Tier 1 (always ask if missing):**
1. "What type of page?" (landing / PDP / homepage / collection / editorial)
2. "Who is this for?" (audience: demographics + pain point)
3. "What should visitors do?" (single conversion goal)

**Tier 2 (ask if Tier 1 reveals complexity):**
4. "Where does traffic come from?" (impacts visual density + social proof weight)
5. "Any sections you specifically want?" (hero style, FAQ, comparison table, etc.)
6. "Should this feel bold/energetic or minimal/premium?" (visual approach)
7. "Any animations or scroll effects?" (parallax, reveal-on-scroll, sticky elements)

**Follow-up triggers:**
- Multiple products mentioned → "Which is the hero product? Are others cross-sells or equals?"
- Health/beauty vertical → "Do you have clinical data or certifications to feature?"
- Ad creative provided → "Should the page match the ad's exact style, or just the message?"

## Step 3 — Generate Page Plan

Use MCP tools to gather brand context:
```
lexsis_brand → brand_kit/get_theme → colors, fonts, voice, spacing
lexsis_design → guide              → brand philosophy + don'ts
lexsis_catalog → list              → available product data
lexsis_brand → navigation          → navbar/footer links
```

Then produce a structured plan covering:

**A. Section Sequence** (ordered list)
For each section:
- Section ID + type (e.g. `hero-split`, `social-proof-bar`, `features-grid`)
- Purpose (what it communicates / why it's here in this position)
- Key content (headline direction, imagery type, specific products)
- Island requirement (if interactive: BuyBox, FAQ, ReviewCarousel, etc.)
- Animation (fade-up, parallax, sticky, reveal, none)

**B. Visual Rhythm**
- Spacing pattern (tight-loose-tight, progressive relaxation, etc.)
- Color temperature flow (hero warm → middle neutral → CTA warm)
- Typography hierarchy (display → heading → body sizes)

**C. Inter-Section Communication**
- Narrative thread (how sections connect logically)
- CTA placement strategy (where and how many)
- Social proof distribution (where trust signals appear and why)
- Scroll incentives (what makes user keep scrolling)

**D. Technical Requirements**
- Islands needed (exact list)
- Custom animations (scroll-triggered reveals, parallax, sticky)
- Asset requirements (hero image, lifestyle shots, textures, icons)

## Step 4 — Present Plan for Approval

### Embedded Use by `visual-page`

When `visual-page` calls this workflow, produce the same plan as
`PLAN_DRAFT` and do not ask for approval yet. `visual-page` creates a visual
layout reference with `lexsis_drafts` action `asset_generate` and presents it
plus the plan as one
approval decision.

Show the plan to the user in this format:

```
📋 Page Plan: [Page Type] for [Audience]

Goal: [Conversion goal]
Sections: [N] | Islands: [list] | Style: [visual approach]

Section Layout:
1. [hero-split] — Hook headline + product image + primary CTA
   Animation: fade-up on load
2. [trust-bar] — Star rating + press logos + "X customers served"
   Animation: none (instant credibility)
3. [problem-solution] — Pain → product as answer (emotional)
   Animation: reveal on scroll
...

Visual Flow: [spacing + color temperature description]
CTA Strategy: [where + how many]

Proceed with this plan? (Or tell me what to change)
```

When run directly, wait for user confirmation. If user suggests changes, update
the plan and re-present.

## Step 5 — Next Steps

Once approved, the user can:
- Run `$generate` — carry the plan forward as the binding blueprint
- Or use the plan with any generation flow

The plan becomes BINDING for generation:
- Phase 2 context gathering targets the plan's requirements
- Phase 3 asset generation follows the plan's imagery needs
- Phase 4 HTML generation follows the plan's section sequence EXACTLY
- Section purposes from the plan guide the copywriting
- Animation choices from the plan guide the JS/CSS

## Optional Follow-Up

This skill can end with an approved plan. `visual-page` can use it for a
visual-first concept, or `asset-prep` and `generate` can use it when the user
wants to continue directly to a draft.
