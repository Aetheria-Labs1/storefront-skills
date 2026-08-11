---
name: search-docs
description: Search Lexsis storefront documentation — islands, skills, conversion patterns, verticals, workflows, tools, and troubleshooting. Use when you need to look up how something works before generating or editing.
---

# Search Lexsis Documentation

Search documentation, skill knowledge, island patterns, and industry guidance via the MCP.

## When to Use

- Before generating: look up island props, variant names, content schemas
- For vertical/industry patterns: "beauty hero patterns", "supplements trust signals"
- For conversion techniques: "urgency patterns", "social proof placement"
- For workflow steps: "how to publish", "A/B test setup"
- For troubleshooting: "island not rendering", "publish fails"
- When unsure which island to use for a UI pattern

## Workflow

1. Call `search_docs` with the user's query (or your own lookup query)
2. If results include a resource URI, read that exact URI for full content.
3. If results reference an island, read `vibe://catalog/islands/{name}` for schema + props + variants
4. Synthesize relevant findings — don't dump raw results, extract what's actionable

## Tool Usage

### Primary search
```json
{ "name": "search_docs", "arguments": { "query": "<search terms>", "limit": 5 } }
```

### Narrow by category
Use `category` to focus results:
- `islands` — interactive component schemas, props, variants
- `tools` — MCP tool documentation and parameters
- `recipes` — end-to-end workflows (ad-to-page, A/B testing, brand setup)
- `vibe-page` — page schema, theming, animations, publishing
- `skills` — conversion psychology, craft guide, generation protocols, verticals
- `verticals` — industry-specific patterns (beauty, supplements, fashion, food, home, luxury)
- `troubleshooting` — common issues and fixes
- `getting-started` — setup, auth, quickstart
- `resources` — MCP resources reference

### Deep-read a result
Use only a resource URI returned by `search_docs`. Do not invent a resource
name or rely on a hard-coded catalog: the search result is the authoritative
availability check.

### Deep-read an island
Read resource URI: `vibe://catalog/islands/{islandName}`
Returns schema with all props, variants, and usage hints.

## Examples

| User asks | Search call | Follow-up |
|-----------|------------|-----------|
| "How does BuyBox work?" | `search_docs({ query: "BuyBox", category: "islands" })` | Read `vibe://catalog/islands/BuyBox` |
| "Beauty landing page patterns" | `search_docs({ query: "beauty landing page", category: "verticals" })` | Read the returned resource URI |
| "Countdown urgency techniques" | `search_docs({ query: "countdown urgency scarcity" })` | — |
| "Publishing workflow" | `search_docs({ query: "publish page workflow", category: "recipes" })` | Read the returned resource URI |
| "What islands handle reviews?" | `search_docs({ query: "reviews testimonials", category: "islands" })` | Read `vibe://catalog/islands/ReviewCarousel` |

## Tips

- Use specific terms, not vague questions — "BuyBox variant swatches" not "how to show products"
- Combine category filter with query for best results
- If search returns nothing, try broader terms or drop the category filter
- Skill resources contain full implementation guides — always read them when referenced

## Optional Follow-Up

This skill can end after returning the concise answer. Its findings can inform
any workflow the user explicitly chooses, including `visual-page`, `plan-page`,
`asset-prep`, `generate`, `optimize`, `experiment`, `cart`, or `publish`.
