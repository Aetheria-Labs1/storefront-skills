---
name: remix
description: Convert a competitor page, inspiration site, or ad creative into a brand-safe visual reference brief. Use when a user wants to adapt a reference; hand the brief to visual-page instead of building the page here.
---

# Remix Reference Into a Brief

Own reference interpretation only. Do not generate page source, production
assets, drafts, or live pages. `visual-page` owns the new-page workflow.

## Inputs

- competitor or inspiration URL
- screenshot or ad creative
- user's product, page goal, and brand direction

## Workflow

1. Capture the source with `browser-analyze` when a URL is available.
2. For ads, call `analyze_ad_creative` and `match_persona_to_ad`.
3. Extract only reusable design signals:
   - page type and section order
   - hierarchy, grids, proportions, whitespace, and motion
   - CTA and trust-signal placement
   - responsive behavior
   - candidate Lexsis islands
4. Exclude competitor copy, product claims, logos, imagery, testimonials,
   pricing, and proprietary marks.
5. Output `VISUAL_PAGE_INPUT`:

```text
Source type: [URL | screenshot | ad]
Page type: [landing | PDP | homepage | collection | editorial]
Audience and conversion goal: [...]
Safe composition cues: [...]
Section map: [...]
Mobile behavior: [...]
Candidate islands: [...]
Avoid: [competitor-specific content and patterns]
```

## Non-Negotiable Safety

- Recreate structure and visual intent, never protected content.
- Use the user's own brand kit, products, claims, assets, and copy.
- Do not hotlink or import competitor images into production media.

## Optional Follow-Up

This skill can end after returning `VISUAL_PAGE_INPUT`. `visual-page` can use
that brief when the user wants a visual layout reference and brand-owned draft.
