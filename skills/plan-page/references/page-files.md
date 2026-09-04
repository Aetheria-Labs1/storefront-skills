# Initial Page Files

Create:

```text
work/visual-pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
├── qa-report.md
└── assets/
```

Start the manifest with:

```json
{
  "schemaVersion": 1,
  "status": "planned",
  "workflow": { "skippedSkills": [] },
  "mcp": {
    "status": "connected",
    "checkedAt": "2026-09-04T12:00:00Z",
    "surfaceVersion": "3.0",
    "capabilities": [
      {
        "router": "lexsis_catalog",
        "actions": ["get"]
      }
    ]
  },
  "page": {
    "title": "...",
    "handle": "...",
    "archetype": "landing"
  },
  "workspaceId": "...",
  "storeId": "...",
  "themeId": "...",
  "template": {
    "mode": "page-kit",
    "pageKitId": "...",
    "sectionTemplateIds": ["..."],
    "evaluatedTemplates": [],
    "selectionReason": "...",
    "selectedAt": "2026-09-04T12:00:00Z"
  },
  "design": {
    "themeId": "...",
    "themeSource": "saved-and-verified",
    "stylePack": null,
    "compiledStyleManifest": null
  },
  "setupPath": "work/storefront/setup/setup.json",
  "brandDesignPath": "...",
  "themeCssPath": "...",
  "pageConfig": {
    "head": {},
    "themeCss": "",
    "scripts": []
  },
  "productBindings": [],
  "assets": [],
  "sections": [],
  "islands": [],
  "visual": {
    "status": "pending",
    "sourcePath": "visual-source.html",
    "previewPath": "visual-preview.html"
  },
  "sourceSync": {
    "lastCompiledBundleHash": null,
    "lastSyncedBundleHash": null,
    "lastSyncedSectionHashes": {},
    "lastChangedSections": []
  },
  "qa": {
    "status": "pending",
    "checkedVersion": null,
    "checkedBundleHash": null,
    "responsive": false,
    "commerce": false,
    "copy": false,
    "claims": false,
    "assets": false,
    "integrity": false
  },
  "remote": {
    "pageId": null,
    "lastKnownVersion": null,
    "previewUrl": null
  }
}
```

The page binds one saved store/theme pair. Do not write visual or production
source during planning. `template.mode` is `page-kit`, `sections`, or `custom`.
Custom composition requires recorded template evaluation and a
`selectionReason`. Do not invent a template version when Lexsis does not
return one.
