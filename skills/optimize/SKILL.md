---
name: optimize
description: Diagnose and improve an existing Lexsis storefront page for a specific business outcome. Starts with a focused optimization brief before making versioned source edits.
---

# Optimize a Page

Read:

- `references/evidence-led-cro.md`
- `references/source-artifact-workflow.md`
- `references/consumer-behavior-cro.md`
- `references/authoring/css-and-styling.md` before any CSS or class change
- `references/animation-system.md` before adding or editing motion

Use the needed exact actions from
`lexsis_pages.edit_context`, `lexsis_pages.source`,
`lexsis_pages.section_source`, `lexsis_pages.compile`,
`lexsis_pages.integrity`, `lexsis_pages.diff`, `lexsis_analytics.page`,
`lexsis_analytics.timeseries`, `lexsis_analytics.attribution`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`,
`lexsis_drafts.page_update_section`, and `lexsis_drafts.page_patch`. Resolve
only unfamiliar schemas through exact router/action discovery. A zero-result
directory lookup does not make page or analytics data unavailable. If the
actual live read fails, state that limitation; generic CRO guidance is not a
substitute.

The full skill pack includes optional deeper design guidance at
`references/lexsis-design-capabilities.md`. Every edit obeys
the house rules in `references/design-rules.md`; an
optimization never adds emoji, gradients, hover transforms, or a section
background.

Start by confirming:

1. Target outcome: conversion, add-to-cart, AOV, bounce, trust, mobile UX,
   speed, or SEO.
2. Target page, audience, and traffic source.
3. Diagnosis only or permission to edit.
4. Copy, sections, SEO fields, or offers that must remain unchanged.

Do not edit until the objective and scope are clear.

Confirm the page's store/theme binding exists in
`work/storefront/setup/setup.json`. If it is missing, stop with
`Run /setup for this store and theme first.` Never run setup automatically.

## Use Relevant Guidance Only

Read only the matching section of `references/industry-cro.md`.

Use general guidance when no industry fits. Treat analytics and observed user
behavior as stronger evidence than generic patterns.

## Diagnose

1. Locate the page and read its analytics, structure, source, and current
   remote version.
2. Use the current MCP source as the editable baseline. Retain its version
   with the intended change; do not create local source or QA files.
3. Compare the remote version with the page record and stop on unexpected drift.
4. For a structural redesign, search relevant page kits and sections and
   compare them with the current structure. Do not force template comparison
   for copy-only, offer-only, metadata, or minor visual changes.
5. Classify proposed changes as keep, improve, replace, remove, or test.
6. Use the consumer-behavior framework to identify the visitor mode, top
   unanswered decision question, and the smallest relevant behavioral
   hypothesis. Analytics and observed behavior override generic guidance.
7. Present an optimization brief:

```text
Outcome:
Evidence:
Main friction:
Visitor mode:
Behavioral hypothesis:
Proposed sections:
Protected elements:
Expected measurement:
Experiment recommended: yes/no
```

Obtain approval before making material changes.

## Apply Approved Changes

Modify editable source. Validate and compile it with any page-wide
`theme_css`, compare section hashes, and patch only changed sections with
`expected_version`. Review visible changes on the updated unpublished hosted
draft; never require a local preview before the patch. Update the operation
record only after the remote write succeeds. Run `diff`, `integrity`,
responsive checks, and affected commerce checks.

Never edit compiled output in place of source. Preserve the URL and SEO fields
unless the user approved changing them.

## Experiment Handoff

When the value of a change is uncertain and traffic supports measurement,
return a focused hypothesis for `/ab-test` instead of presenting the change
as proven.

## Return

Return the approved objective, evidence, changed sections, page version,
verification results, template comparison when applicable, MCP evidence, and
whether an experiment is recommended.
