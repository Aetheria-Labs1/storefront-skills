# Storefront Page Generation

> **Full workflow:** See `generation-protocol.md` for Phases 1-5 execution (context gathering, HTML generation, validation, publishing, visual verification).

This file covers quick-reference patterns for generation.

---

## Template-First Rule

Always search `search_section_templates` before generating sections from scratch. It returns metadata only — fetch markup for the ids you pick with `get_section_template`:

```
search_section_templates({ query: "hero with video background for fashion", section: "hero", industry: "fashion", mood: "editorial" })
get_section_template({ ids: ["<chosen id from results>"] })
```

- If a matching template is found (score > 0.7): USE IT. Its returned `source`
  contains the section markup, CSS, and JS ready to tailor with brand-specific
  copy/images, then pass to
  `compile_page_source`.
- If no match: generate from scratch in Phase 4.

Templates are conversion-proven, pixel-perfect, and faster than custom generation.
Use `format: "compiled_reference"` only to inspect renderer output; never paste its
`data-island` / `data-props` markup into source-authoring tools.

For a full page, check `search_page_kits` before assembling sections one at a time — it returns curated multi-section groupings that already share one palette/vertical:

```
search_page_kits({ query: "clinical supplements PDP", page_type: "pdp", industry: "supplements" })
```

---

## Page Type Section Defaults

**Product Landing (PDP)** — 8-10 sections:
Hero (split) → Gallery → BuyBox → Benefits → Ingredients/Specs → Reviews → Related Products → FAQ → Sticky CTA → Footer

**Campaign Landing** — 10 sections:
Hero → Problem/Pain → Solution → Key Benefits → Social Proof → How It Works → Comparison → Offer/Pricing → FAQ → CTA

**Homepage** — 7-8 sections:
Hero → Featured Products → Brand Story → Categories → Testimonials → Newsletter → Trust Bar → Footer

**Collection** — 6 sections:
Hero Banner → Filter/Sort → Product Grid → Promo Card → Social Proof → Footer

**Editorial** — 6-8 sections:
Full-Bleed Hero → Intro Copy → Shoppable Gallery → Content Block → Product Spotlight → Related Reads → Footer

**Listicle** — 7-9 sections:
Hero + TOC → Methodology → Numbered Items → Comparison Table → Verdict → FAQ → CTA

**Bundle** — 6-8 sections:
Hero + Savings Hook → Step Progress → Product Selection → Social Proof → FAQ → Sticky Summary
