---
name: optimize
description: Diagnose and improve an existing Lexsis storefront page for a specific business outcome. Starts with a focused optimization brief before making local-first section edits.
---

# Optimize a Page

Read:

- `references/evidence-led-cro.md`

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
`storefront-engine/references/lexsis-design-capabilities.md`. Every edit obeys
the house rules in `storefront-engine/references/design-rules.md`; an
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
2. Open its local page workspace. If missing, adopt the remote source into the
   standard local files before editing.
3. Compare the remote version with the manifest and stop on unexpected drift.
4. For a structural redesign, search relevant page kits and sections and
   compare them with the current structure. Do not force template comparison
   for copy-only, offer-only, metadata, or minor visual changes.
5. Classify proposed changes as keep, improve, replace, remove, or test.
6. Present an optimization brief:

```text
Outcome:
Evidence:
Main friction:
Proposed sections:
Protected elements:
Expected measurement:
Experiment recommended: yes/no
```

Obtain approval before making material changes.

## Apply Approved Changes

Modify `lexsis-source.html` first. Validate and compile the complete local
source with `page-theme.css`, compare section hashes, and patch only changed
sections with `expected_version`. A visible source or CSS change requires a
new compiled preview and design approval before the remote patch. Update the
manifest only after the remote write succeeds. Then run `diff`, `integrity`,
responsive checks, and affected commerce checks.

Never make an intentional remote-only edit. Preserve the URL and SEO fields
unless the user approved changing them.

## Experiment Handoff

When the value of a change is uncertain and traffic supports measurement,
return a focused hypothesis for `/experiment` instead of presenting the change
as proven.

## Return

Return the approved objective, evidence, changed sections, page version,
verification results, template comparison when applicable, MCP evidence, and
whether an experiment is recommended.
