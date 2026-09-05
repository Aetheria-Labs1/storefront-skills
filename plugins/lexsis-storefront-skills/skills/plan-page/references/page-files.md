# Initial Page Files

Create:

```text
work/visual-pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
└── assets/
```

Start with a compact progressive manifest:

```json
{
  "schemaVersion": 3,
  "status": "planned",
  "workflow": {
    "skippedSkills": []
  },
  "page": {
    "title": "...",
    "handle": "...",
    "archetype": "landing"
  },
  "workspaceId": "...",
  "storeId": "...",
  "themeId": "...",
  "setupPath": "work/storefront/setup/setup.json",
  "template": {
    "mode": "page-kit",
    "pageKitId": "...",
    "sectionTemplateIds": ["..."]
  },
  "sections": [
    "hero",
    "benefits",
    "closing-cta"
  ],
  "products": [
    {
      "productId": "...",
      "variantIds": ["..."]
    }
  ]
}
```

`template.mode` is `page-kit`, `sections`, or `custom`. For custom
composition, keep the rationale in `page-plan.md`; do not store template
search transcripts in JSON.

The manifest grows only when later stages have real state to record:

- `/design-page` adds compact `config`, `assets`, `islands`, and `design`
  records.
- `/generate` adds `sync`, `remote`, and `qa`.

Do not prefill null production, approval, hash, QA, or remote fields. Do not
store copy intent, claims, occasion research, omitted components, or creative
notes in the manifest.
