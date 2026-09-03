---
name: optimize
description: Diagnose and improve an existing Lexsis storefront page for a specific business outcome. Starts with a focused optimization brief before making local-first section edits.
---

# Optimize a Page

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

Read `references/evidence-led-cro.md`, then read only the matching section of
`references/industry-cro.md`.

Use general guidance when no industry fits. Treat analytics and observed user
behavior as stronger evidence than generic patterns.

## Diagnose

1. Locate the page and read its analytics, structure, source, and current
   remote version.
2. Open its local page workspace. If missing, adopt the remote source into the
   standard local files before editing.
3. Compare the remote version with the manifest and stop on unexpected drift.
4. Classify proposed changes as keep, improve, replace, remove, or test.
5. Present an optimization brief:

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
source, compare section hashes, and patch only changed sections with
`expected_version`. Update the manifest only after the remote write succeeds.
Then run `diff`, `integrity`, responsive checks, and affected commerce checks.

Never make an intentional remote-only edit. Preserve the URL and SEO fields
unless the user approved changing them.

## Experiment Handoff

When the value of a change is uncertain and traffic supports measurement,
return a focused hypothesis for `/experiment` instead of presenting the change
as proven.

## Return

Return the approved objective, evidence, changed sections, page version,
verification results, and whether an experiment is recommended.
