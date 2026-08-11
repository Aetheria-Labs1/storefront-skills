---
name: analyze-page
description: Analyze a reference webpage into a brand-safe structural brief. Use for competitor or inspiration URLs before visual-page; do not generate page source or production assets here.
---

# Analyze Storefront Page

Own structural analysis of a reference page. Do not write replacement HTML,
generate assets, create a page, or publish. `visual-page` owns the new-page
workflow after this brief is ready.

## Workflow

1. Capture the URL with `browser-analyze` when Browser is available.
2. Classify the page: PDP, landing, homepage, collection, editorial, or other.
3. Extract:
   - global design tokens and visual rhythm
   - section order, proportions, and responsive behavior
   - CTA, trust, urgency, and social-proof placement
   - interaction patterns and candidate Lexsis islands
4. Separate reusable structure from protected source material.
5. Output `VISUAL_PAGE_INPUT`:

```text
Source URL: [...]
Page type: [...]
Design direction: [...]
Section map: [...]
Responsive behavior: [...]
Conversion patterns: [...]
Candidate islands: [...]
Do not carry forward: [copy, logos, product imagery, claims, testimonials]
```

## Safety

- Use the source only for hierarchy, composition, and interaction patterns.
- Do not copy text, logos, images, product claims, pricing, reviews, or brand
  marks.
- Do not write source-format HTML in this skill.

## Optional Follow-Up

This skill can end after producing `VISUAL_PAGE_INPUT`. When the user wants a
new brand-owned page from that brief, `visual-page` can use it as input.
