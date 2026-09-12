# Voice-of-customer mining

How to collect the shopper's own language before writing a line of copy,
and how to use it without inventing anything. `/plan-page` runs the
procedure while it fills the Proof ledger (the same review calls feed
both); the output is a worksheet in the page's task record that `/design-page`
reads in Compose step 8. Quoted text on the page comes only from
`references/proof/proof-ledger.md` rows; this file governs the unquoted
copy that borrows the shopper's words.

Evidence: a headline lifted from a real review ("If you think you need
rehab, you do") beat the agency headline by over 400 percent in clicks and
lifted form fills 20 percent (Copyhackers/Beachway). https://copyhackers.com/2014/10/amazon-review-mining/
Concrete beats abstract: readers remember "charging pitbull", not "seamless
transition" (Harry Dry). https://www.demandcurve.com/lessons/fundamental-rules-of-good-copy

Severity BLOCK, FAIL, WARN. Tag LAW, RESEARCH, OPERATOR, HEURISTIC.

## 1. Inputs and tools

| Source | Tool | What it gives | When |
|---|---|---|---|
| The merchant's reviews, by intent | `lexsis_catalog.reviews_search` with `query` set to a decision question or claim | Semantically ranked verbatim reviews for that question | one call per decision question, always first |
| The merchant's reviews, by keyword | `lexsis_catalog.reviews` with `q` free text plus `rating_min`, `has_media`, `product_id` | Exact-phrase hits, low-star hits, media reviews | objections, complaints, competitor mentions |
| Review status and collections | `lexsis_catalog.reviews_status`, `lexsis_catalog.review_collections` | Counts, distribution, active collections | before any mining; decides tier |
| Personas | selected `persona.md` entry or merchant-supplied audience description | Persona vocabulary, pains, market, behaviour, and decision context | persona-led pages |
| Ad comments and creative text | merchant-supplied campaign material | The words the ad already uses; objections in comments when supplied | message match (`references/copy/message-match.md`) |
| Brand voice | `lexsis_brand.brand_kit` `voice_md`, `banned_phrases` | Register, we-say/we-don't-say pairs, forbidden words | reconciliation, section 7 |
| Support and merchant notes | merchant-supplied tickets, chat logs, returns reasons | Objections the reviews do not show | when the merchant supplies them |
| External public reviews (zero-review stores only) | host web search, marketplaces, Reddit, YouTube, per `references/proof/reviews-sourcing.md` | Category language and objections | evidence for wording only; never quoted without an `external-verified-quote` ledger row |

## 2. Procedure

VC1 (FAIL, OPERATOR). Write the decision questions first. Take the top three to five from the plan's Consumer decision model (`references/consumer-behavior-cro.md`) and add the two that every page must answer: "how fast do I get it" and "what if it does not work for me".
Check: `page plan` Consumer decision model block lists the questions; the worksheet header repeats them.

VC2 (FAIL, OPERATOR). Run `lexsis_catalog.reviews_search` once per decision question with the question or the claim as `query`. Keep the top 5 to 8 verbatim results per question. Do not paraphrase at this step.
Check: worksheet section A has one block per question with the review ids.

VC3 (WARN, OPERATOR). Run `lexsis_catalog.reviews` with `q` for objection words ("too", "but", "wish", "smell", "sticky", "size", "return", "expensive", "didn't", competitor names) and with `rating_min: 1` capped at 3 stars to read the complaints. Keep 5 to 10 lines.
Check: worksheet section B has at least five lines from reviews rated 3 stars or below when such reviews exist.

VC4 (WARN, OPERATOR). Read the selected `persona.md` entry and any merchant-supplied audience description. Copy its market, vocabulary, pain statements, behaviours, objections, and decision context into the worksheet.
Check: worksheet section C present when personas exist.

VC5 (FAIL, OPERATOR). Read `voice_md` and `banned_phrases` before writing. Copy the register adjectives and the we-say/we-don't-say pairs into the worksheet.
Check: worksheet section D filled.

VC6 (BLOCK, LAW). With zero usable reviews, follow the zero-review playbook in `references/proof/reviews-sourcing.md`. External text informs wording only; it enters the page as a quote only as an `external-verified-quote` ledger row with URL, merchant approval and platform permission. Marketplace text whose terms forbid reuse is never copied to the page.
Check: any external line in the worksheet is tagged `external` and never appears verbatim in `rendered text` unless the ledger row exists.

## 3. What to extract

| Tag | What it is | Example shape | Where it goes on the page |
|---|---|---|---|
| `pain` | the before state in the shopper's words | "sweat through my shirt by 11am" | h1 (problem-aware), `problem`, qualifier |
| `desire` | the outcome they wanted | "wanted to wear it without socks" | subhead, `benefits`, bullets |
| `benefit-phrase` | how they describe what the product did | "still smelt fine after a 5-mile run" | h1 (solution-aware), bullets, `benefits` |
| `objection` | doubt, complaint, condition | "worried it would feel cakey", "too small for a 15-inch laptop" | FAQ questions, `qualifier` not-for lines, comparison rows |
| `comparison` | what they used before or instead | "switched from [competitor] because" | `comparison`, `alternatives`, listicle item 1 |
| `number` | timeframes, counts, measurements they report | "by week three", "50 washes", "two cups a day" | h1 or subhead specific, bullets, `results-timeline` |
| `sticky-phrase` | a memorable, quotable line | "put the pans in my will" | ledger quote candidate only |
| `context` | who they are, when they use it | "night shift", "postpartum", "Bengaluru summer" | persona line, qualifier, imagery brief |

## 4. Tag and count

VC7 (FAIL, OPERATOR). Collect 20 to 30 verbatim lines in total. Tag each with one or more tags from section 3 and the review id. Count phrase frequency across lines; the most frequent `pain` or `benefit-phrase` is the headline candidate; the most frequent `objection` is FAQ question one after shipping and returns; the most frequent `number` becomes the specific in the h1 or subhead. Sources: https://copyhackers.com/write-copy-amazon-review-mining/
Check: worksheet section E table has at least 20 rows with tags and ids, and a frequency list of at least five phrases.

## 5. Using the worksheet

VC8 (FAIL, RESEARCH). Headlines and subheads use the shopper's words, not the brand's. Unquoted copy may adopt a customer phrase or paraphrase it; it may not put quotation marks around it or attribute it unless it is a ledger quote rendered verbatim.
Check: the plan's "Headline VoC source" line names the worksheet row id; no quotation marks in h1 or subhead unless the text equals a ledger row.

VC9 (FAIL, OPERATOR). FAQ questions are the `objection` lines rephrased as the shopper would type them; answers open with the answer (HC21 to HC23). At least three of the FAQ questions trace to worksheet rows.
Check: worksheet section F maps each FAQ question to a row id.

VC10 (FAIL, OPERATOR). Bullets and benefit copy carry the `number` and `benefit-phrase` specifics from the worksheet, not adjectives. A bullet without a worksheet or catalog specific is rewritten or cut.
Check: each `<li>` in benefit sections maps to a worksheet row or a catalog spec in the plan.

VC11 (BLOCK, LAW). Never fabricate. No invented quotes, names, cities, ratings, counts, timeframes or "customers say" summaries that no review supports. A composite quote (two reviews spliced) is fabrication. FTC 16 CFR 465; proof-ledger rule 4.

VC12 (BLOCK, LAW). Quoted text renders only through the proof ledger with attribution as stored and the date. The worksheet is a writing aid, not a rendering source.
Check: the source/hosted review N11 numeral trace; every `[data-part=quote]` has a ledger row id.

VC13 (WARN, OPERATOR). When a customer word and a marketing word compete, the customer word wins: "exhausting" over "time-consuming", "still smells fine after a run" over "high-performance". Record each replacement in the worksheet.
Check: worksheet section G lists replacements; `references/anti-patterns/copy-anti-patterns.md` CP1 hits are 0 after replacement.

VC14 (WARN, OPERATOR). Keep the review's own specifics when quoting (variant, timeframe, use, limitation). Prefer quotes that mention the claim they sit beside and, where possible, a limitation; all-praise sets read as fake (proof-ledger rule 4).
Check: at least one rendered quote contains a limitation word (`but|only|wish|although|except`) when 20 or more reviews exist.

VC15 (FAIL, OPERATOR). Retain the VoC worksheet in the page's task record and reference it from `page plan` under "Copy sources". Sub-agents writing sections read it; they do not call the review tools again.

## 6. Worksheet template

```markdown
# VoC worksheet: <page handle>

Decision questions: 1. <q> 2. <q> 3. <q> 4. How fast do I get it 5. What if it does not work for me

## A. reviews_search per question
### Q1 <question>
| Review id | Rating | Verbatim line (trimmed with [...]) | Tags |
|---|---|---|---|
| 9a1c... | 5 | "still smelt fine after a 5-mile run" | benefit-phrase, number, context |

## B. Objections and low-star lines (reviews q=..., rating <= 3)
| Review id | Rating | Verbatim line | Tags |

## C. Persona vocabulary
Persona id and name: ... Market: ... Words they use: ... Pains: ... Behaviours: ... Objections: ...

## D. Brand voice (voice_md, banned_phrases)
Register: ... We say / we don't say: ... Banned: ...

## E. Frequency
| Phrase | Count | Tag | Candidate use |
|---|---|---|---|
| "by week three" | 6 | number | subhead specific |

## F. FAQ mapping
| FAQ question (as the shopper types it) | Worksheet row ids |

## G. Replacements
| Draft word | Customer word | Row id |

## H. External lines (zero-review stores only; wording evidence, never quoted)
| Source URL | Line | Tag |
```

## 7. Banned-phrase reconciliation

VC16 (BLOCK, OPERATOR). Precedence when sources disagree: `voice_md` register and merchant-stated rules, then `brand_kit.banned_phrases`, then the blacklist in `references/anti-patterns/copy-anti-patterns.md` CP1. A merchant ban is absolute in brand copy. A customer phrase that contains a banned or blacklisted word may still be rendered verbatim inside a ledger quote (reviews are not edited), but the brand's own copy does not adopt it.
Check: `banned_phrases` hits in `rendered text` outside `<blockquote>` and review islands are 0; blacklist hits are 0 or allowlisted in the plan.

VC17 (WARN, OPERATOR). Allowlisting a blacklist word requires a literal reason (a product named "Curated", a tier named "Premium") recorded in `page plan` under "Copy allowlist" with the word and the reason. Customer usage alone ("reviewers say seamless") is not a reason.
Check: every allowlisted word has a reason line.

VC18 (WARN, OPERATOR). Locale and spelling follow the store market (`en-IN`, `en-GB`, `en-US`); customer quotes keep their own spelling; brand copy uses one locale (CP35).
Check: CP35.
