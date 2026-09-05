---
name: analyze-page
description: Analyze a URL, screenshot, or ad into a safe storefront brief. Use for inspiration, message-match, or existing-page diagnosis; this skill does not generate page source.
---

# Analyze a Page or Creative

Choose one mode:

- **Inspiration:** extract reusable layout and interaction patterns.
- **Own-page review:** identify design and conversion weaknesses.
- **Message-match:** compare an ad or screenshot with the intended landing
  page.

Generic URL or screenshot analysis can use the host browser without Lexsis and
reports `MCP status: not-required`. Any request that reads a Lexsis campaign,
catalogue, page, asset, or stored analysis requires the normal MCP preflight.
Confirm `lexsis_discover` is available and discover the exact actions needed.
If that preflight fails, return `BLOCKED_LEXSIS_MCP` rather than replacing
missing live data with assumptions.

## Capture

When a URL is available, use the host browser capability to inspect desktop
and mobile views, headings, sections, CTAs, media, and interactions. If browser
access is unavailable, use supplied screenshots and state what could not be
verified.

For ads, use `lexsis_campaigns` analysis actions when available.

## Analyze

Record:

- page type and audience
- section order and visual rhythm
- desktop/mobile behavior
- CTA and trust placement
- useful interaction patterns and candidate Lexsis islands
- message-match strengths or gaps
- accessibility or usability issues visible in the evidence

Do not use unsupported benchmark percentages or generic lift claims.

## Brand Safety

Carry forward structure and design intent only. Exclude competitor copy,
logos, product imagery, pricing, claims, reviews, testimonials, and protected
brand elements.

## Return

Return `PAGE_ANALYSIS`:

```text
Mode: [inspiration | own-page | message-match]
Source: [...]
Page type: [...]
Reusable structure: [...]
Responsive behavior: [...]
Conversion observations: [...]
Candidate islands: [...]
Avoid copying: [...]
Evidence limits: [...]
```

Include MCP status, discovered capabilities, actions, fallbacks, and blockers
when Lexsis was used. This can inform `/plan-page` for a new page or
`/optimize` for an existing one.
