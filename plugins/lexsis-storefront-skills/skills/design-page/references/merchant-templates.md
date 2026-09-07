# Merchant-Owned Section Templates

Merchant templates are reusable, versioned source-format sections. They use the
existing template and revision model; they are not renderer defaults, global
shell assignments, or a separate recipe system.

## Contract

- A template contains exactly one compilable source section.
- The section may be a Header, Footer, Announcement, product composition, or
  any future supported island composition.
- CSS remains inside canonical section source and follows the normal compiler
  and source-format rules.
- Applying a template copies its source into the target page and creates one
  ordinary page version. The page does not retain a live dependency on the
  template.
- Updating, publishing, archiving, or deleting template metadata never mutates
  pages that already materialized its source.
- Listing is metadata-only. Fetch one template before reading or editing its
  source.

## MCP Actions

Read:

```text
lexsis_template_library({ action: "list_mine", args: { workspace_id } })
lexsis_template_library({ action: "get_mine", args: { workspace_id, template_id } })
```

Reversible draft operations:

```text
lexsis_drafts({
  action: "template_create",
  args: { workspace_id, name, source, visibility, description?, section?, tags? }
})

lexsis_drafts({
  action: "template_update",
  args: { workspace_id, template_id, source?, name?, description?, visibility?, section?, tags? }
})

lexsis_drafts({
  action: "template_apply",
  args: {
    template_id,
    page_id,
    expected_version,
    expected_source_sha256?,
    position?,
    section_id?,
    idempotency_key?
  }
})
```

`position` is `first`, `last`, `{ "before": "<section-id>" }`, or
`{ "after": "<section-id>" }`. `section_id` optionally renames the copied
section so it does not collide with an existing page section.

Sensitive lifecycle operations require explicit approval:

```text
lexsis_live_ops({ action: "template_publish", args: { workspace_id, template_id, revision_id? } })
lexsis_live_ops({ action: "template_archive", args: { workspace_id, template_id } })
```

## Source Authority

Header, navigation, announcement, and footer are ordinary authored sections.
Do not:

- inject them at renderer level;
- depend on inherited header/footer flags;
- create a `shell`, `navigation_profile`, Recipes route, or `lexsis_styles`
  tool;
- regenerate an entire page when a reusable section can be applied;
- assume a template is Header/Footer-specific.

Use Templates → My templates for the user-owned library. Use the Design Library
for brand tokens and navigation/footer link data, not as a second page renderer.
