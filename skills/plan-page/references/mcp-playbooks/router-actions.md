# MCP router/action inventory

Derived from the `CONSOLIDATED_ROUTERS` declaration in the sibling MCP
service on 2026-09-11: 18 routers, 92 actions. Re-derive this inventory when
that source changes. This lists operation names, not arguments or island
props; resolve an unfamiliar action schema before calling it.

| Router | Actions |
|---|---|
| `lexsis_workspace` | `lexsis_workspace.list`, `lexsis_workspace.get`, `lexsis_workspace.stores`, `lexsis_workspace.credits` |
| `lexsis_assets` | `lexsis_assets.capabilities`, `lexsis_assets.view` |
| `lexsis_asset_library` | `lexsis_asset_library.search` |
| `lexsis_asset_import` | `lexsis_asset_import.import` |
| `lexsis_asset_upload` | `lexsis_asset_upload.upload` |
| `lexsis_campaigns` | `lexsis_campaigns.creatives`, `lexsis_campaigns.analyze`, `lexsis_campaigns.frames`, `lexsis_campaigns.personas`, `lexsis_campaigns.match_persona` |
| `lexsis_brand` | `lexsis_brand.context`, `lexsis_brand.brand_kit`, `lexsis_brand.list_themes`, `lexsis_brand.get_theme`, `lexsis_brand.navigation`, `lexsis_brand.compile_theme` |
| `lexsis_catalog` | `lexsis_catalog.list`, `lexsis_catalog.get`, `lexsis_catalog.reviews_status`, `lexsis_catalog.reviews`, `lexsis_catalog.reviews_search`, `lexsis_catalog.review_collections`, `lexsis_catalog.review_collection_items` |
| `lexsis_pages` | `lexsis_pages.list`, `lexsis_pages.find`, `lexsis_pages.get`, `lexsis_pages.edit_context`, `lexsis_pages.content`, `lexsis_pages.source`, `lexsis_pages.section_source`, `lexsis_pages.inspect`, `lexsis_pages.diff`, `lexsis_pages.integrity`, `lexsis_pages.qa`, `lexsis_pages.compile`, `lexsis_pages.compile_artifact` |
| `lexsis_drafts` | `lexsis_drafts.asset_generate`, `lexsis_drafts.theme_update`, `lexsis_drafts.page_replace`, `lexsis_drafts.page_patch`, `lexsis_drafts.page_attach_bundle`, `lexsis_drafts.page_update_section`, `lexsis_drafts.page_remove_section`, `lexsis_drafts.page_move_section`, `lexsis_drafts.page_update_head`, `lexsis_drafts.page_record_qa`, `lexsis_drafts.page_duplicate`, `lexsis_drafts.page_variation`, `lexsis_drafts.template_create`, `lexsis_drafts.template_update`, `lexsis_drafts.template_apply`, `lexsis_drafts.experiment_create`, `lexsis_drafts.funnel_create`, `lexsis_drafts.funnel_update`, `lexsis_drafts.cart_set`, `lexsis_drafts.cart_edit`, `lexsis_drafts.review_collection_create`, `lexsis_drafts.send_feedback` |
| `lexsis_page_create` | `lexsis_page_create.create` |
| `lexsis_live_ops` | `lexsis_live_ops.publish`, `lexsis_live_ops.unpublish`, `lexsis_live_ops.delete`, `lexsis_live_ops.rollback`, `lexsis_live_ops.template_publish`, `lexsis_live_ops.template_archive`, `lexsis_live_ops.scale_winner` |
| `lexsis_design` | `lexsis_design.guide`, `lexsis_design.islands`, `lexsis_design.island_schema`, `lexsis_design.get_section` |
| `lexsis_template_library` | `lexsis_template_library.search_sections`, `lexsis_template_library.search_page_kits`, `lexsis_template_library.get_kit`, `lexsis_template_library.list_mine`, `lexsis_template_library.get_mine` |
| `lexsis_analytics` | `lexsis_analytics.timeseries`, `lexsis_analytics.page`, `lexsis_analytics.attribution`, `lexsis_analytics.experiment` |
| `lexsis_capture` | `lexsis_capture.form_schemas`, `lexsis_capture.submissions`, `lexsis_capture.funnel_templates`, `lexsis_capture.funnel_template`, `lexsis_capture.get_funnel`, `lexsis_capture.validate_funnel`, `lexsis_capture.preview_funnel` |
| `lexsis_cart` | `lexsis_cart.get` |
| `lexsis_support` | `lexsis_support.search_docs` |
