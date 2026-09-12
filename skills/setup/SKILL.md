---
name: setup
description: "Connect Lexsis storefront workspaces and build reusable, structured store context covering brand, design, products, personas, rules, and themes. Run initially, then refresh only the context domain that changed."
---

# Set Up Lexsis

Build the durable store map that later storefront skills read before making
page decisions. Setup is read-only: it resolves Lexsis data and writes local
Markdown/CSS context files; it does not create pages or production assets.

Use these exact action slots:

- identity: `lexsis_workspace.list`, `lexsis_workspace.get`,
`lexsis_workspace.stores`;
- brand and theme: `lexsis_brand.context`, `lexsis_brand.brand_kit`,
`lexsis_brand.list_themes`, `lexsis_brand.get_theme`,
`lexsis_brand.navigation`, `lexsis_design.guide`;
- catalog: `lexsis_catalog.list`, `lexsis_catalog.get`;
- proof availability: `lexsis_catalog.reviews_status`,
`lexsis_catalog.review_collections`.

Build persona context from verified brand/store data, catalog patterns, existing merchant notes, and information the user confirms.

When an action's arguments are unfamiliar, resolve that exact router/action
schema before calling it. A directory lookup with no result is not a
connection failure; the domain call is authoritative.

## Store Context

Write only this compact, human-readable structure:

```text
work/storefront/
+-- setup.md
+-- stores/
    +-- <workspace-id>/
        +-- <store-id>/
            +-- brand.md
            +-- design.md
            +-- products.md
            +-- persona.md
            +-- rules.md
            +-- themes/
                +-- <theme-id>.css
```

Use ids in paths and names in headings. Never combine context from different
workspaces, stores, or themes.

## Procedure



### 1. Select the scope

1. Read an existing `work/storefront/setup.md` when present.
2. Call `lexsis_workspace.list`, then `lexsis_workspace.get` for candidate
  workspaces and `lexsis_workspace.stores` for connected stores.
3. Show choices by name and domain. Ask the user only when more than one valid
  choice exists or they want to save several.
4. Resolve themes with `lexsis_brand.list_themes`. Use an explicit choice,
  otherwise the sole or marked default theme.
5. Record one default workspace, store, and theme. Defaults must point to
  entries saved in the same hierarchy.

`design.md` always binds to the store's default working theme. Save every
additional selected theme as its own CSS file without merging theme systems.

An initial run refreshes every context domain. A later run may refresh
`brand`, `design`, `products`, `persona`, `rules`, `themes`, or `all`.
Preserve unaffected files and user-confirmed notes.

### 2. Read store context

For each selected store:

1. Read workspace details, `lexsis_brand.context`,
  `lexsis_brand.brand_kit`, and `lexsis_brand.navigation`.
2. Read every selected theme with `lexsis_brand.get_theme`.
3. Read the selected theme's exact `lexsis_design.guide`.
4. Page through `lexsis_catalog.list` until no next cursor remains. Use the
  maximum supported page size.
5. If lightweight catalog rows omit fields required by `products.md`, call
  `lexsis_catalog.get` in supported batches for those product ids.
6. Read `lexsis_catalog.reviews_status`, then page through active
  `lexsis_catalog.review_collections`.
7. Merge verified MCP facts with existing merchant-confirmed local notes.
  Mark unresolved or inferred information explicitly.

Do not silently stop after the first catalog or review-collection page.

When material context remains unclear:

- Use available web search or browser research for public facts.
- For private merchant decisions, conflicting positioning, unsupported claims,
  and missing facts that would change later page strategy, ask the user.
- For every saved fact, retain the source URL or source action and the access/refresh date.
- If a fact cannot be verified, record the item as an open question.

### 3. Write store files

Write complete files to temporary sibling paths first, validate their
bindings and required headings, then replace the prior files. Always write
`setup.md` last so its index never points at an incomplete refresh.

If one domain call fails, retain the last good content for that domain, record
the failure and its date in `setup.md`, and continue with independent domains.
Never erase good context because another domain is unavailable.

## File Contracts

Use these headings exactly. Keep prose compact and prefer short tables.

### `setup.md`

```markdown
# Storefront setup

## Defaults
- Workspace: <name> (`<workspace-id>`)
- Store: <name/domain> (`<store-id>`)
- Theme: <name> (`<theme-id>`)

## Saved stores
| Workspace | Store | Domain | Default theme | Context path | Refreshed | Status |

## Context map
| Store | Brand | Design | Products | Personas | Rules | Themes |

## Incomplete context
| Store | Domain | Last good refresh | Current issue | Next action |
```

Use paths relative to `work/storefront/`.

### `brand.md`

```markdown
# <Brand name>

## Binding and provenance
| Field | Value |

## Identity
- Description:
- Vertical:
- Primary markets:
- Storefront URL:

## Positioning
- Core promise:
- Differentiators:
- Product categories:
- Purchase model:

## Message hierarchy
1.

## Voice and vocabulary
- Voice principles:
- Preferred words:
- Prohibited or sensitive language:

## Visual identity
- Logo:
- Favicon:
- Colors:
- Fonts:
- Theme screenshots or brand-owned visual references:

## Navigation
- Header:
- Footer:

## Known customer concerns
| Concern | Applicable products/categories | Source | Confidence |

## Open questions
- <question or none>
```

Exact theme tokens belong in the theme CSS and `design.md`; summarize them
here only to make the brand map searchable.

### `design.md`

```markdown
# Design guide

## Binding
- Workspace:
- Store:
- Theme:
- Refreshed:
- Source: `lexsis_design.guide`

<exact design guide returned by Lexsis>
```

Do not rewrite, normalize, or merge the returned guide into a new design
system. Add only the binding header.

### `products.md`

```markdown
# Product catalog

## Snapshot
- Refreshed:
- Product count:
- Product types:
- Common tags:
- Snapshot price range:
- Availability note:

## Products
| Product id | Handle | Title | Status | Type | Vendor | Tags | Variants | Options | Media | Hero media | Selling plans |

## Catalog gaps
| Product | Missing field | Refresh action |
```

Keep one compact row per product. Label price and availability as a dated
snapshot. This file is a discovery map, not commerce authority: later skills
refresh every selected product live before using variants, prices,
availability, media, or selling plans.

### `persona.md`

```markdown
# Persona map

## Binding and confidence
- Workspace:
- Store:
- Refreshed:
- Evidence rule: confirmed facts, labelled inferences, and open questions

## Market context
| Market/location | Language or locale | Buying context | Notes | Source |

## Persona index
| Persona id | Name | Status | Market | Priority | Product/category fit | Source |

## Persona: <stable id and name>

### Snapshot
- Status: <merchant-confirmed, evidence-supported inference, or draft>
- Market/location:
- Life or work context:
- Primary job to be done:

### Behaviour
- Discovery behaviour:
- Evaluation behaviour:
- Purchase behaviour:
- Repeat-purchase or loyalty behaviour:

### Concerns and barriers
1.

### Triggers and desired outcomes
1.

### Language
- Words and phrases they use:
- Questions they ask:
- Terms the brand may echo:
- Terms to avoid:

### Decision criteria
1.

### Proof required
1.

### Product and category map
| Product/category | Relevance | Use case | Main objection |

### Evidence
| Statement | Status | Source | Confidence |

### Open questions
- <question or none>
```

Preserve stable persona ids across refreshes. Do not invent demographics,
locations, behaviours, or quotations. When the available evidence supports a
useful hypothesis, label it `evidence-supported inference` and keep the
supporting source. Ask the user for missing persona facts that materially
change page strategy; leave lesser gaps as open questions.

### `rules.md`

```markdown
# Store rules

## Claim ledger
| Claim | Status | Evidence/reference | Products | Markets | Last verified |

## Language controls
- Required language:
- Prohibited language:

## Guarantees, shipping, returns, and delivery
| Rule | Value | Markets/products | Source | Last verified |

## Offers and pricing controls
| Rule | Allowed use | Restrictions | Source |

## Certifications and regulated content
| Item | Status | Evidence required | Restrictions |

## Review availability
- Connection status:
- Imported count:

## Active review collections
| Collection id | Name | Item count | Applicable products/categories |

## Merchant decisions
| Decision | Scope | Date | Source |

## Unknowns requiring confirmation
- <question or none>
```

Store only review availability and active collection summaries. Do not copy
customer records or full review text into setup.

### `themes/<theme-id>.css`

Save the exact `theme_css` returned for that theme. Keep separate files for
separate themes and identify the default in `setup.md`.

## Validation

Before returning:

- every saved store path contains all five Markdown files and at least one
selected theme CSS file;
- ids in file bindings match their path and `setup.md`;
- defaults resolve to saved entries in the same hierarchy;
- catalog pagination reached its terminal cursor;
- each product appears once in `products.md`;
- personas use stable ids and evidence labels;
- unavailable domains appear in `setup.md`;
- no credentials, authorization values, customer records, full review text,
image binaries, or raw product JSON were saved.



## Return

Report:

- the `work/storefront/setup.md` path;
- saved workspace, store, and theme names;
- defaults;
- refreshed domains and dates;
- product count and persona count per store;
- incomplete context, failed MCP reads, and open user confirmations.

Later skills read this context directly and refresh volatile facts live. They
never invoke `/setup` automatically.
