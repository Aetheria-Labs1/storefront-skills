# Copy anti-patterns

The canonical vocabulary and structure blacklist for generated page copy.
`/design-page` applies it in Compose step 8; `design_lint.py` C1 to C4
mirror the lists below (update both together); `brand_kit.banned_phrases`
is merged in at run time. Positive rules for headlines, CTAs, FAQs and
microcopy are in `references/copy/headline-and-cta-rules.md`; frameworks in
`references/copy/copy-frameworks.md`; sourcing real language in
`references/copy/voice-of-customer-mining.md`.

Scope of a hit. FAIL when the word or structure appears in an `h1`, `h2`,
`h3`, subhead, button, link label, CTA microcopy or announcement bar. WARN
when it appears in body text fewer than two times; FAIL at two or more body
hits. Text inside `<blockquote>` and review islands is exempt: reviews are
verbatim (`references/proof/proof-ledger.md` rule 4).

Severity BLOCK, FAIL, WARN. Tag LAW, RESEARCH, OPERATOR, HEURISTIC. `$T` is
the extracted text with quotes removed:
`perl -0pe 's/<blockquote.*?<\/blockquote>//sg; s/<lx-island name="Review.*?<\/lx-island>//sg; s/<[^>]+>/ /g' $W/lexsis-source.html > $T`.

## 1. Evidence

- Kobak et al., Science Advances 2024/25, 15M PubMed abstracts: after ChatGPT, 379 style words spiked; "delves" 28x, "underscores" 13.8x, "showcasing" 10.7x; 66 percent of excess style words are verbs. https://arxiv.org/html/2406.07016v5
- Pangram (vendor, per 10k words, AI vs human): em dashes 17 vs 2 (10x), triads 19 vs 5 (4x), "not just X but Y" 3 vs 1 (3x), "delve into" class phrases 30 vs 3, bullet lists 9x, emoji 2x. https://www.pangram.com/signs-of-ai-writing
- Community catalogues derived from Wikipedia "Signs of AI writing": antithesis cadence, "from X to Y" sweeps, colon reveals, fragment punchlines. https://github.com/crypdick/unslop/blob/main/skills/unslop/references/ai-writing-patterns.md
- Copyhackers/Beachway: a headline lifted from a real review beat the marketing-written one by over 400 percent in clicks. Real language wins; generic language loses. https://copyhackers.com/2014/10/amazon-review-mining/

## 2. Vocabulary blacklist

CP1 (FAIL in headings and controls; WARN then FAIL in body; RESEARCH, OPERATOR). None of the following appears outside verbatim quotes. The lint list is the union of the three blocks plus `brand_kit.banned_phrases`.

Verbs and verb phrases:
```text
elevate, unleash, unlock (except a literal gate: "Unlock free shipping at ₹999" is allowed), delve, embrace, indulge,
discover (as an imperative opener), experience (as an imperative opener), transform your, revolutionize, revolutionise,
empower, harness, leverage, supercharge, streamline, optimize (consumer copy), reimagine, redefine, showcase, foster,
navigate (metaphorical), dive into, take ... to the next level, say goodbye to, say hello to, look no further, treat yourself
```

Adjectives and nouns:
```text
seamless, effortless, game-changer, game-changing, revolutionary, cutting-edge, next-level, next-generation, state-of-the-art,
world-class, best-in-class, innovative, unparalleled, unmatched, unrivalled, ultimate, premium (unqualified; allowed inside a tier or product name),
luxurious (unqualified), exquisite, meticulous, meticulously, intricate, curated, bespoke (unless made to order), artisanal (unless hand-made),
holistic, synergy, robust, tapestry, realm, journey (metaphorical), landscape (metaphorical), testament, beacon, pivotal, crucial,
vibrant, dynamic, must-have, perfect for, stunning, breathtaking, elevated, sleek, effortlessly chic
```

Phrases and openers:
```text
elevate your routine, in today's fast-paced world, whether you're X or Y, it's not just X, it's Y, not just ... but (also), more than just,
Imagine ... (opener), Picture this, Introducing (headline), crafted with care, crafted with love, premium quality, designed with you in mind,
the perfect blend of, at its finest, like never before, you deserve, the secret to, your go-to, made for modern life, we've got you covered,
sit back and relax, the best part?, here's the thing, let's face it, in a world where, gone are the days, nestled, boasts, a testament to,
from X to Y and everything in between, welcome to, at [Brand], we believe, discover the difference, experience the difference, the ultimate,
your journey, level up, game on, ready to ..., unlock your potential, step into, dive in
```

Allowlist handling. `brand_kit.allowlist` (or the plan's "Copy allowlist" line) removes a term when it is literal: a brand named "Elevate", a tier named "Premium", a hair oil that is literally "curated" by a named person. Every allowlisted hit is recorded in `page-plan.md` with the reason.

## 3. Claims

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP2 | Superlatives and objective claims without substantiation: best, #1, No.1, most trusted, most advanced, clinically proven, doctor recommended, dermatologist tested, award-winning, 100% natural, chemical-free, toxin-free, guaranteed results, proven to | FTC: objective claims need a reasonable basis before publication; "clinically proven" needs that evidence. India ASCI/CCPA: "No.1" only with market-share data; disclaimers may not contradict the claim. Each hit must map to a proof-ledger row (`test-data`, `award`, `certification`, `customer-count`). https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business ; https://www.ascionline.in/wp-content/uploads/2022/09/asci_june_july_2020_ccc_pr.pdf | BLOCK | LAW | `grep -niE '\b(#\s?1|no\.?\s?1|number one|the best|world'"'"'s (best|most)|most (trusted|advanced|popular|loved)|clinically (proven|tested)|(doctor|dermatologist)[- ](recommended|tested)|award[- ]winning|100% (natural|safe|effective)|chemical-free|toxin-free|guaranteed results|proven to)\b' $T`; every line maps to a ledger row |
| CP3 | Hedged non-claims: may help support, can help promote, is believed to, designed to help, supports healthy ... | Either a substantiated fact with a number, or cut the sentence. Where regulation mandates a hedge (supplement structure/function claims), keep the mandated wording and pair it with dose, ingredient or study n. | WARN | OPERATOR | `grep -ciE '\b(may help|can help|might help|is believed to|designed to help|helps? support|supports? (healthy|overall))\b' $T` |
| CP4 | "Results not typical" or "results may vary" as the only qualifier beside a results testimonial | FTC Endorsement Guides: disclose the generally expected result in the same block; the bare disclaimer does not comply. https://www.govinfo.gov/content/pkg/CFR-2023-title16-vol1/pdf/CFR-2023-title16-vol1-part255.pdf | BLOCK | LAW | any hit of `results (may )?(not typical|vary)` requires `generally|typical(ly)? (see|lose|gain|report)` in the same section |

## 4. Structure tells

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP5 | Em-dash chains | At most one em dash per 150 words; none in headings, buttons or subheads. Prefer a full stop. Pangram: 10x more em dashes in AI text. | FAIL | RESEARCH | lint C3 (headline chains); `perl -ne '$d+=()=/\x{2014}|\x{2013}| - /g; $w+=split; END{printf "%.2f per 150w\n",$d/($w/150)}' $T` under 1.0 |
| CP6 | Rule of three everywhere ("soft, breathable, and durable") | At most one adjective triad per section. Lists of specifics beat adjective triads. | WARN | RESEARCH | `grep -ciE '\b\w+, \w+,? and \w+\b'` per section text at most 1 |
| CP7 | Antithesis: "not just X, it's Y", "isn't just ... it's", "more than just" | Zero. | FAIL | RESEARCH | `grep -ciE "(isn'?t|not|is more than) just\b.*\b(but|it'?s|it is)\b" $T` is 0 |
| CP8 | Rhetorical-question openers ("Tired of ...?", "Ever wondered ...?") | At most one question heading per page; never the h1 unless the type uses `qualifier-lead` and the question genuinely selects the reader. | WARN | OPERATOR | `grep -c '?' <headings>` at most 1 |
| CP9 | "Imagine ..." or "Picture this" | Zero. | FAIL | RESEARCH | `grep -ciE '^\s*(imagine|picture this)\b' $T` is 0 |
| CP10 | Exclamation marks | Zero outside verbatim reviews. | FAIL | OPERATOR | `grep -c '!' $T` is 0 |
| CP11 | Uniform sentence and paragraph length | Standard deviation of sentence length at least 4 words per section; no three consecutive paragraphs within 10 percent of the same word count. | WARN | HEURISTIC | sentence-length variance script in section 9 |
| CP12 | Identical section rhythm (headline, subhead, three bullets, CTA, repeated) | Adjacent sections never share the same layout skeleton (`references/anti-patterns/design-anti-patterns.md` DA14). | FAIL | OPERATOR | DA14 check |
| CP13 | Alliterative or fragment triad headlines ("Pure. Potent. Proven.") | At most one fragment-triad heading per page. | FAIL | RESEARCH | `grep -cE '^[A-Z][a-z]+\. [A-Z][a-z]+\. [A-Z][a-z]+\.$' <headings>` at most 1 |
| CP14 | Summary and conclusion language ("In conclusion", "Ultimately", "Overall", "To sum up") | Zero. A landing page asks; it does not conclude. | FAIL | OPERATOR | `grep -ciE '\b(in conclusion|ultimately|overall|to sum up|in summary|all in all)\b' $T` is 0 |
| CP15 | Colon reveal in headings ("The result: skin that ...") | At most one per page. | WARN | RESEARCH | `grep -c ': ' <headings>` at most 1 |
| CP16 | Title Case Headings | Sentence case for headings, subheads, buttons, labels; product names keep brand casing. USAGov moved to sentence case sitewide in 2023 with no trust drop. https://www.usa.gov/blog/2023/09/making-the-case-for-sentence-case | FAIL | RESEARCH | `grep -cE '^([A-Z][a-z]+\s){3,}[A-Z][a-z]+' <headings>` is 0 after the product-name allowlist |
| CP17 | Bold-label bullets ("**Fast:** ...", "**Simple:** ...") | Zero. Write the specific. | FAIL | RESEARCH | `grep -cE '<li>\s*<(strong|b)>[^<]{1,20}:</(strong|b)>' $W/lexsis-source.html` is 0 |
| CP18 | False ranges ("from busy parents to pro athletes") | Only when X and Y are real endpoints of one scale the merchant serves. | WARN | RESEARCH | `grep -ciE '\bfrom \w+( \w+)? to \w+( \w+)?( and everything in between)?\b' $T`; each hit reviewed |
| CP19 | Generic openers ("Welcome to ...", "At [Brand], we believe ...", "We are passionate about") | Zero. Lead with the shopper's problem or a specific. | FAIL | OPERATOR | `grep -ciE '^\s*(welcome to|at [A-Z][A-Za-z]+,? we (believe|are passionate)|we are passionate)' $T` is 0 |
| CP20 | Subhead restates the headline | The subhead resolves the headline (mechanism, proof or who it is for); token overlap with the h1 under 50 percent. | FAIL | OPERATOR | overlap script in section 9 |

## 5. Punctuation and case

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP21 | Hype punctuation: "!!", "?!", "..." trails in headings | Zero. | FAIL | OPERATOR | lint C2 `!{2,}|\?!` |
| CP22 | ALL-CAPS words of six or more letters | None outside a `CAPS_ALLOWLIST` of acronyms and registered marks (GST, FSSAI, UPI, MRP, BIS, ISO, NSF, USDA, SPF, COD, EMI, BNPL). Labels of three words or fewer may be caps only under a merchant-stated rule (design-rules N5). | FAIL | RESEARCH | lint C2 `[A-Z]{6,}(?![a-z])` after allowlist removal |
| CP23 | Arrow glyphs or "->" in link and button text | Design-rules N12. | FAIL | OPERATOR | lint N12 |
| CP24 | Emoji anywhere in copy | Design-rules N1. | FAIL | OPERATOR | lint N1 |
| CP25 | Middle dots (U+00B7) joining meta strings ("Free shipping", dot, "30-day returns", dot, "Made in India") | Use a full stop or separate lines; N12 names middle-dot joins as chrome. | WARN | OPERATOR | `grep -c '\xc2\xb7' $W/lexsis-source.html` is 0 |

## 6. CTA and control copy

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP26 | Stock CTA labels: Shop Now, Get Started, Learn More, Buy Now (tof/mof), Submit, Click here, Continue (no object), OK, Yes, Go, Read more | Design-rules A12; `references/copy/headline-and-cta-rules.md` HC12 to HC14. The CTA is verb plus object plus outcome or price, at most four words, sentence case. | FAIL | OPERATOR | lint A12 and C4 plus the extension in section 10 |
| CP27 | CTA that does not start with a verb, or exceeds four words | HC12. | FAIL | OPERATOR | CTA verb script in section 9 |
| CP28 | "Free" with an asterisk or a later condition | Offers OF5: the condition sits in the same line. | BLOCK | LAW | `grep -ciE '\bfree\*' $T` is 0 |

## 7. Placeholder and model leakage

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP29 | Placeholder text: lorem ipsum, TODO, TBD, [brand], [product], {{ }}, "Your headline here", "Insert ...", "Product name", "Lorem" | Zero. A12 already forbids placeholder copy. | BLOCK | OPERATOR | `grep -ciE 'lorem|ipsum|\bTODO\b|\bTBD\b|\[(brand|product|name|city|number)\]|\{\{|your (headline|text|copy) here|insert (your|a|the)|product name here' $W/lexsis-source.html` is 0 |
| CP30 | Framework labels leaking into copy ("Problem:", "Agitate:", "Solution:", "Benefit:", "Call to action") | Zero. Frameworks shape the order, never the words. | FAIL | OPERATOR | `grep -ciE '^\s*(problem|agitat(e|ion)|solution|benefit|proof|push|hook|story|offer|call to action)\s*:' $T` is 0 |
| CP31 | Assistant voice leaking ("As an AI", "Certainly", "Here's a", "I hope this helps", "Feel free to") | Zero. | BLOCK | OPERATOR | `grep -ciE "as an ai|certainly|here'?s an? |i hope this|feel free to|let me know" $T` is 0 |

## 8. Brand voice

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP32 | A `brand_kit.banned_phrases` entry appears | BLOCK in any position, including body. Merged into the lint list at run time; the plan's "Copy allowlist" cannot override a merchant ban. | BLOCK | OPERATOR | `for p in "${BANNED[@]}"; do grep -ciF "$p" $T; done` all 0 |
| CP33 | Register mismatch with `voice_md` (jokey copy for a clinical brand; clinical copy for a playful brand) | Reviewed by an LLM pass against the voice adjectives and "we say / we don't say" pairs; not regex. | WARN | OPERATOR | one-line finding per section in `qa-report.md` |
| CP34 | Brand name outnumbers "you/your" | Second person leads; Apple's iPhone 5 copy used "you/your" more than "iPhone" and "Apple" combined. https://neilpatel.com/blog/write-copy-like-apple/ | WARN | RESEARCH | ratio script in section 9 |
| CP35 | Spelling locale drift (color and colour on one page) | One locale from `brand_kit` or the store market. | WARN | OPERATOR | `grep -ciE '\bcolor\b' $T` and `grep -ciE '\bcolour\b' $T` are not both non-zero |

## 9. Canonical regex and scripts

Python `re` form, case-insensitive, applied to `$T`. Lines marked `# lint` are already in `design_lint.py`; `# NEW` are additions for the lead to adopt.

```python
SLOP_WORDS = r"\b(elevate[sd]?|unleash(es|ed)?|unlock(s|ed)?|delve[sd]?|seamless(ly)?|game-?changer|game-?changing|revolutioni[sz]e[sd]?|revolutionary|effortless(ly)?|curated|indulge|embrace|look no further|say goodbye to|in today'?s fast-paced|whether you'?re|it'?s not just|crafted with (care|love|passion)|meticulously|premium quality|world-class|cutting-edge|next-level|transform(s|ed)? your|elevate your|discover the (power|magic|difference)|experience the (difference|magic)|the ultimate|your journey|treat yourself|introducing the)\b"   # lint C1
SLOP_WORDS_EXT = r"\b(empower(s|ed|ing)?|harness(es|ed)?|leverage[sd]?|supercharge[sd]?|streamline[sd]?|reimagine[sd]?|redefine[sd]?|showcas(e|es|ed|ing)|foster(s|ed)?|dive into|next-gen(eration)?|state-of-the-art|best-in-class|innovative|unparalleled|unmatched|unrivall?ed|exquisite|meticulous|intricate|bespoke|artisanal|holistic|synergy|robust|tapestry|realm|testament|beacon|pivotal|crucial|vibrant|must-have|perfect for|stunning|breathtaking|say hello to|designed with you in mind|the perfect blend|at its finest|like never before|you deserve|the secret to|your go-to|made for modern life|we'?ve got you covered|sit back and relax|the best part\?|here'?s the thing|let'?s face it|in a world where|gone are the days|nestled|boasts|a testament to|and everything in between|welcome to|at [A-Z][a-z]+,? we believe|level up|unlock your potential|step into|dive in)\b"   # NEW
HYPE_PUNCT = r"!{2,}|\?!|[A-Z]{6,}(?![a-z])"   # lint C2 (apply CAPS_ALLOWLIST first)
CAPS_ALLOWLIST = {"FSSAI","GST","UPI","MRP","BIS","ISO","NSF","USDA","SPF","COD","EMI","BNPL","INCI","GMP","HACCP"}   # NEW
HEADLINE_EMDASH = r"<h[1-3][^>]*>[^<]*\u2014[^<]*\u2014"   # lint C3 (the script uses the literal em dash)
STOCK_CTA = r">\s*(Submit|Click here|Learn more)\s*<"   # lint C4
STOCK_CTA_EXT = r">\s*(Shop now|Get started|Buy now|Read more|Continue|OK|Yes|Go|Sign up|Download)\s*(<|$)"   # NEW (Buy now only when funnelStage != bof)
ANTITHESIS = r"(isn'?t|not|is more than) just\b.*\b(but|it'?s|it is)\b"   # NEW
IMAGINE = r"^\s*(imagine|picture this)\b"   # NEW
SUMMARY = r"\b(in conclusion|ultimately|overall|to sum up|in summary|all in all)\b"   # NEW
GENERIC_OPENER = r"^\s*(welcome to|at [A-Z][A-Za-z]+,? we (believe|are passionate)|we are passionate)"   # NEW
BOLD_LABEL_BULLET = r"<li>\s*<(strong|b)>[^<]{1,20}:</(strong|b)>"   # NEW (source html)
SUPERLATIVE = r"\b(#\s?1|no\.?\s?1|number one|the best|world'?s (best|most)|most (trusted|advanced|popular|loved)|clinically (proven|tested)|(doctor|dermatologist)[- ](recommended|tested)|award[- ]winning|100% (natural|safe|effective)|chemical-free|toxin-free|guaranteed results|proven to)\b"   # NEW, BLOCK unless ledger row
HEDGE = r"\b(may help|can help|might help|is believed to|designed to help|helps? support|supports? (healthy|overall))\b"   # NEW, WARN
RESULTS_DISCLAIMER = r"results (may )?(not typical|vary)"   # NEW, BLOCK without 'generally expected'
PLACEHOLDER = r"lorem|ipsum|\bTODO\b|\bTBD\b|\[(brand|product|name|city|number)\]|\{\{|your (headline|text|copy) here|insert (your|a|the)|product name here"   # NEW, BLOCK
FRAMEWORK_LABEL = r"^\s*(problem|agitat(e|ion)|solution|benefit|proof|push|hook|story|offer|call to action)\s*:"   # NEW
ASSISTANT_VOICE = r"as an ai|certainly|here'?s an? |i hope this|feel free to|let me know"   # NEW, BLOCK
FREE_ASTERISK = r"\bfree\*"   # NEW, BLOCK
TITLE_CASE_HEADING = r"^([A-Z][a-z]+\s){3,}[A-Z][a-z]+"   # NEW, on heading text after product-name allowlist
FRAGMENT_TRIAD = r"^[A-Z][a-z]+\. [A-Z][a-z]+\. [A-Z][a-z]+\.$"   # NEW, on heading text, allow 1
```

```python
# CP11 sentence-length variance, CP20 subhead overlap, CP27 CTA verb, CP34 you/brand ratio
import re, statistics
def sentences(t): return [s for s in re.split(r'[.!?]+\s', t) if s.strip()]
def cp11(section_text):
    L = [len(s.split()) for s in sentences(section_text)]
    return len(L) < 3 or statistics.pstdev(L) >= 4
def cp20(h1, sub):
    a, b = set(re.findall(r'\w+', h1.lower())), set(re.findall(r'\w+', sub.lower()))
    return len(a & b) / max(1, len(b)) < 0.5
VERBS = {'add','get','start','claim','buy','shop','send','try','join','grab','order','choose','see','show','save','pre-order','subscribe','reserve','book','take','find','build','pick','complete','apply','check'}
def cp27(label):
    w = label.strip().lower().split()
    return 1 <= len(w) <= 4 and w[0] in VERBS and (len(w) > 1 or w[0] in {'buy','shop','order','subscribe'})
def cp34(text, brand):
    return len(re.findall(r'\byou(r|rs)?\b', text, re.I)) >= len(re.findall(re.escape(brand), text, re.I))
```

## 10. Rewrite procedure for a hit

1. Ask Harry Dry's three questions of the sentence: can the reader visualise it, can it be falsified, could no competitor say it. A line failing all three is deleted, not rephrased. https://www.demandcurve.com/lessons/fundamental-rules-of-good-copy
2. Replace the banned word with what specifically happens: "seamless" becomes "arrives assembled, no tools"; "premium quality" becomes the material, weight or test.
3. Pull the replacement from the voice-of-customer worksheet (`references/copy/voice-of-customer-mining.md`) before inventing one.
4. Re-run the section checks; a heading hit blocks compile, a body hit produces a rewrite note in `qa-report.md` with the span and the rule id.

## 11. Lint alignment

`design_lint.py` today: C1 `SLOP_WORDS`, C2 `HYPE_PUNCT`, C3 headline em-dash chains, C4 Submit/Click here/Learn more. Adopt, in this order of value:

1. Merge `SLOP_WORDS_EXT` into C1 and honour `brand_kit.allowlist` plus the plan's "Copy allowlist" line (CP1).
2. Merge `brand_kit.banned_phrases` as literal, case-insensitive matches, BLOCK in any position (CP32).
3. Add `CAPS_ALLOWLIST` stripping before C2 (CP22).
4. Add `STOCK_CTA_EXT` to C4, with "Buy now" gated on `manifest.page.funnelStage != "bof"` (CP26).
5. New checks C5 `ANTITHESIS`, C6 `IMAGINE`, C7 `SUMMARY`, C8 `GENERIC_OPENER`, C9 `BOLD_LABEL_BULLET`, C10 `PLACEHOLDER` (BLOCK), C11 `FRAMEWORK_LABEL`, C12 `ASSISTANT_VOICE` (BLOCK), C13 `FREE_ASTERISK` (BLOCK), C14 `SUPERLATIVE` (BLOCK unless a ledger row is named in `page-plan.md` "Claims confirmed"), C15 `HEDGE` (WARN), C16 `RESULTS_DISCLAIMER` (BLOCK without a "generally expected" phrase in the same section).
6. Heading-text checks C17 `TITLE_CASE_HEADING`, C18 `FRAGMENT_TRIAD` (allow 1), C19 question headings (allow 1), C20 colon reveals (allow 1), C21 em-dash density under 1 per 150 words on `$T`.
7. Structural scripts C22 `cp11`, C23 `cp20`, C24 `cp27` on every button and `a.btn` label, C25 `cp34`.
8. Scope: run C1 and the structure checks on `$T` with `<blockquote>` and review islands removed, and report heading hits as FAIL and body hits as WARN (FAIL at two or more).
