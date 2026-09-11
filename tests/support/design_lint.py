#!/usr/bin/env python3
"""Repository-only regression checks for design-rule fixtures.

Usage: design_lint.py <workspace> | design_lint.py --input-json -
The stdin object contains source, optional theme_css, plan and manifest.
Runs the grep-able rules from storefront-engine/references/design-rules.md
(N1, N3-N7, N9, N10, N12-N14, A11, A12) against lexsis-source.html and
page-theme.css, plus the mechanical proof (P), offer / dark-pattern (O) and
copy (C) rules from references/proof/proof-ledger.md,
references/anti-patterns/dark-patterns.md and
references/anti-patterns/copy-anti-patterns.md. Exit 1 when any check fails.
N2, N8, N11, A4 and A7 need the browser checks described in design-rules.md.
"""
import argparse
import json
import pathlib
import re
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("workspace", nargs="?", type=pathlib.Path)
parser.add_argument("--input-json", choices=["-"], help="Read exact review inputs from stdin")
arguments = parser.parse_args()
if arguments.input_json and arguments.workspace:
    parser.error("choose a workspace or --input-json -, not both")
if arguments.input_json:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as error:
        parser.error(f"invalid input JSON: {error}")
    if not isinstance(payload, dict):
        parser.error("input must be a JSON object")
    src = payload.get("source")
    css = payload.get("theme_css", "")
    plan = payload.get("plan", "")
    manifest = payload.get("manifest", {})
    if not isinstance(src, str) or not src.strip():
        parser.error("source must be a non-empty string")
    if not isinstance(css, str) or not isinstance(plan, str):
        parser.error("theme_css and plan must be strings")
    if not isinstance(manifest, dict):
        parser.error("manifest must be an object")
else:
    workspace = arguments.workspace or pathlib.Path(".")
    src = (workspace / "lexsis-source.html").read_text(encoding="utf-8")
    css_path = workspace / "page-theme.css"
    css = css_path.read_text(encoding="utf-8") if css_path.exists() else ""
    plan_path = workspace / "page-plan.md"
    plan = plan_path.read_text(encoding="utf-8") if plan_path.exists() else ""
    manifest_path = workspace / "page-manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    except json.JSONDecodeError:
        manifest = {}
both = src + "\n" + css
# N1 exception: the plan records a merchant-insisted "Emoji in copy: allowed" line.
emoji_in_copy_allowed = bool(re.search(r"Emoji in copy\W+\s*allowed", plan, re.I))

# Same ranges as the perl -CSD check in design-rules.md N1.
EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF☀-➿⬀-⯿⌀-⏿"
    "\U0001F1E6-\U0001F1FF️‍‼⁉]"
)


def count(pat: str, text: str, flags: int = 0) -> int:
    return len(re.findall(pat, text, flags))


radii = {
    (a or b).replace("!important", "").strip()
    for a, b in re.findall(r'border-radius:\s*([^;"}]+)|(rounded(?:-[a-z0-9\[\]]+)?)', both)
}

emoji_count = len(EMOJI.findall(both))
checks = [
    ("N1 emoji" + (" (plan allows in copy)" if emoji_in_copy_allowed else ""), emoji_count, emoji_count if emoji_in_copy_allowed else 0),
    ("N3 stroke-width variants", max(0, len(set(re.findall(r'stroke-width="([^"]*)"', src))) - 1), 0),
    ("N3 img used as icon", count(r'<img[^>]*class="[^"]*icon', src), 0),
    ("N4 font families (<=3)", max(0, len(set(re.findall(r"family=([A-Za-z+]+)", css))) - 3), 0),
    ("N5 uppercase", count(r"\buppercase\b|text-transform:\s*uppercase", both), 0),
    ("N6 accent inside headline", count(r"<h[1-3][^>]*>[^<]*<(span|em|strong|i|b|mark)", src), 0),
    (
        "N7 coloured glow shadow",
        count(r"box-shadow:[^;}]*(--lx-accent|color-mix\(|rgba?\([^)]*\)[^;}]*\b(1[6-9]|[2-9][0-9])px)", both, re.I),
        0,
    ),
    (
        "N7 gradient/shimmer/hover-scale",
        count(
            r"gradient\(|bg-gradient|shimmer|animate-pulse|pulseRing|float-|hover:scale|hover:-translate|scale\(1\.[0-9]|box-shadow:\s*0 0 ",
            both,
        ),
        0,
    ),
    ("N9 discount pills", count(r"\b[0-9]{1,2}% ?OFF\b|BEST VALUE|MOST POPULAR|LIMITED TIME|NEW ARRIVAL", src), 0),
    ("N10 unplanned motion", count(r"data-reveal|IntersectionObserver|@keyframes|animation:", both), 0),
    ("N12 arrows in CTAs", count(r"(→|&rarr;|»)\s*</(a|button)", src), 0),
    ("N12 icon tiles", count(r'w-1[0-6] h-1[0-6][^"]*rounded', src), 0),
    ("N13 distinct radii (<=4)", max(0, len(radii) - 4), 0),
    (
        "N14 off-brand hex",
        count(r"#667eea|#764ba2|#8b5cf6|#f9fafb|#6366f1|#7c3aed|text-(yellow|gray|slate|purple|indigo)-[0-9]", both, re.I),
        0,
    ),
    ("A11 focus-visible present", 0 if ":focus-visible" in both else 1, 0),
    ("A12 stock CTA copy", count(r">(Shop Now|Get Started|Learn More|Buy Now)\s*(→)?<", src), 0),
]

# Proof, offer and copy rules. The word lists mirror the canonical blocks in
# references/anti-patterns/copy-anti-patterns.md (section 9) and
# references/anti-patterns/dark-patterns.md (section 4); update both together.
page_type = (manifest.get("page") or {}).get("pageType", "")
funnel_stage = (manifest.get("page") or {}).get("funnelStage", "")

SLOP_WORDS = (
    r"\b(elevate[sd]?|unleash(es|ed)?|unlock(s|ed)?|delve[sd]?|seamless(ly)?|game-?changer|"
    r"game-?changing|revolutioni[sz]e[sd]?|revolutionary|effortless(ly)?|curated|indulge|"
    r"embrace|look no further|say goodbye to|in today'?s fast-paced|whether you'?re|"
    r"it'?s not just|crafted with (care|love|passion)|meticulously|premium quality|"
    r"world-class|cutting-edge|next-level|transform(s|ed)? your|elevate your|"
    r"discover the (power|magic|difference)|experience the (difference|magic)|"
    r"the ultimate|your journey|treat yourself|introducing the|"
    r"empower(s|ed|ing)?|harness(es|ed)?|leverage[sd]?|supercharge[sd]?|streamline[sd]?|"
    r"reimagine[sd]?|redefine[sd]?|showcas(e|es|ed|ing)|foster(s|ed)?|dive into|"
    r"next-gen(eration)?|state-of-the-art|best-in-class|innovative|unparalleled|unmatched|"
    r"unrivall?ed|exquisite|meticulous|intricate|bespoke|artisanal|holistic|synergy|robust|"
    r"tapestry|realm|testament|beacon|pivotal|crucial|vibrant|must-have|perfect for|stunning|"
    r"breathtaking|say hello to|designed with you in mind|the perfect blend|at its finest|"
    r"like never before|you deserve|the secret to|your go-to|made for modern life|"
    r"we'?ve got you covered|sit back and relax|the best part\?|here'?s the thing|"
    r"let'?s face it|in a world where|gone are the days|nestled|boasts|a testament to|"
    r"and everything in between|welcome to|level up|unlock your potential|step into|dive in)\b"
)
CAPS_ALLOWLIST = {"FSSAI", "GST", "UPI", "MRP", "BIS", "ISO", "NSF", "USDA", "SPF", "COD", "EMI", "BNPL", "INCI", "GMP", "HACCP"}
HYPE_PUNCT = r"!{2,}|\?!|[A-Z]{6,}(?![a-z])"
STOCK_PHRASES = (
    r"\bonly \d+ left\b|\b\d+ (people|others) (are )?(viewing|looking)|"
    r"\b(bought|purchased|ordered) (this )?(in the last|today|recently)|selling fast|"
    r"almost gone|hurry|last chance|don'?t miss out|limited stock|"
    r"\bends? (soon|tonight|today|in)\b|\blimited time\b|\bwhile (stocks|supplies) last\b|\blow stock\b"
)
CONFIRMSHAME = (
    r"no,? (thanks,? )?i (don'?t|do not|hate|prefer|like paying|want to pay)|"
    r"i'?ll (pay full price|stay|pass on)"
)
STOCK_CTA = r">\s*(Submit|Click here|Learn more|Shop now|Get started|Read more|Continue|OK|Yes|Go|Sign up|Download" + ("" if funnel_stage == "bof" else "|Buy now") + r")\s*<"
ANTITHESIS = r"(isn'?t|not|is more than) just\b.*\b(but|it'?s|it is)\b"
IMAGINE = r"(^|[.!?>]\s*)(imagine|picture this)\b"
SUMMARY = r"\b(in conclusion|ultimately|overall|to sum up|in summary|all in all)\b"
GENERIC_OPENER = r"(^|>)\s*(welcome to|at [A-Z][A-Za-z]+,? we (believe|are passionate)|we are passionate)"
BOLD_LABEL_BULLET = r"<li>\s*<(strong|b)>[^<]{1,20}:</(strong|b)>"
SUPERLATIVE = (
    r"\b(#\s?1|no\.?\s?1|number one|the best|world'?s (best|most)|most (trusted|advanced|popular|loved)|"
    r"clinically (proven|tested)|(doctor|dermatologist)[- ](recommended|tested)|award[- ]winning|"
    r"100% (natural|safe|effective)|chemical-free|toxin-free|guaranteed results|proven to)\b"
)
RESULTS_DISCLAIMER = r"results (may )?(not typical|vary)"
PLACEHOLDER = r"lorem|ipsum|\bTODO\b|\bTBD\b|\[(brand|product|name|city|number)\]|\{\{|your (headline|text|copy) here|insert (your|a|the)|product name here"
ASSISTANT_VOICE = r"\bas an ai\b|\bcertainly[,!]|\bhere'?s an? \w+ (headline|copy|version)|i hope this|feel free to|let me know"
FREE_ASTERISK = r"\bfree\*"
FAKE_SYSTEM_UI = r"\b(virus|infected|system alert|analy[sz]ing your|applying your discount)\b"
NEGATED_CHOICE = r"\b(opt.?out|un(check|tick|subscribe)|do not|don'?t) [^<]{0,40}(receive|get|miss)\b"

# $T: visible text without quoted reviews or review islands (their words are the customer's).
text_src = re.sub(r"<blockquote\b.*?</blockquote>", " ", src, flags=re.S | re.I)
text_src = re.sub(r'<lx-island name="Review[^"]*">.*?</lx-island>', " ", text_src, flags=re.S)
T = re.sub(r"<[^>]+>", " ", text_src)
T_caps = " ".join(w for w in T.split() if w.strip(".,;:!?()") not in CAPS_ALLOWLIST)
sections = re.findall(r"<!-- section: ([a-z0-9-]+) -->(.*?)(?=<!-- section:|\Z)", src, re.S)

def section_text(pred):
    return [(sid, re.sub(r"<[^>]+>", " ", body)) for sid, body in sections if pred(sid)]

press_sections = [(sid, body) for sid, body in sections if re.match(r"press|as-seen", sid)]
unlinked_logos = sum(
    len(re.findall(r"<img\b", body)) - len(re.findall(r"<a\b[^>]*href=[^>]*>\s*(?:<[^a][^>]*>\s*)*<img\b", body))
    for _, body in press_sections
)
plan_has_end = bool(re.search(r"\bend date\b.*\b20\d\d-\d\d-\d\d", plan, re.I))
countdowns = count(r'<lx-island name="Countdown(Timer)?"', src)
superlatives_unbacked = [m for m in re.findall(SUPERLATIVE, T, re.I) if (m[0] if isinstance(m, tuple) else m).lower() not in plan.lower()]
results_unqualified = sum(
    1 for _, t in section_text(lambda s: True)
    if re.search(RESULTS_DISCLAIMER, t, re.I) and not re.search(r"generally expected|typical result|most (customers|users|people)", t, re.I)
)
subscription_missing_terms = sum(
    1 for _, t in section_text(lambda s: s.startswith(("subscription-toggle", "plan-selector", "pricing")))
    if not (re.search(r"(every|per|/)\s*(month|week|\d+ days)", t, re.I) and re.search(r"cancel", t, re.I))
)
buybox_missing_costs = sum(
    1 for _, t in section_text(lambda s: s.startswith(("buy-box", "pricing", "offer")))
    if not (re.search(r"shipping|delivery", t, re.I) and re.search(r"tax|gst|inclusive|incl\.", t, re.I))
)
first_three = " ".join(body for _, body in sections[:3])
ad_label_missing = 1 if page_type in {"advertorial", "listicle"} and not re.search(r"advertis(ement|ing)|sponsored|paid partnership", first_three, re.I) else 0
strikes_unsourced = count(r"<(s|del)\b(?![^>]*data-source=)", src)
checks += [
    ("P1 social proof popup / live counts", count(r'SocialProofPopup|people are viewing|viewing this|bought in the last', src, re.I), 0),
    ("P2 unlinked press logos", max(0, unlinked_logos), 0),
    ('P3 "as seen in" caption', count(r"as seen (in|on)", src, re.I), 0),
    ("P4 star glyphs without count", count(r"(★|&#9733;|&starf;){3,}(?![^<]*\d)", src), 0),
    ("O1 stock / hurry / deadline phrases", count(STOCK_PHRASES, T, re.I), 0),
    ("O2 countdown without plan end date", 0 if (countdowns == 0 or plan_has_end) else countdowns, 0),
    ("O3 pre-checked add-on inputs", count(r'<input[^>]*type="(checkbox|radio)"[^>]*\bchecked\b(?![^>]*data-lx-default)', src), 0),
    ("O4 confirmshaming dismiss copy", count(CONFIRMSHAME, T, re.I), 0),
    ("O5 required consent inputs", count(r'<input[^>]*(consent|marketing|sms|newsletter)[^>]*\brequired\b', src, re.I), 0),
    ("O6 subscription section lacks cadence+cancel", subscription_missing_terms, 0),
    ("O7 buy-box/pricing lacks shipping+tax line", buybox_missing_costs, 0),
    ("O8 advertorial/listicle without ad label", ad_label_missing, 0),
    ("O9 negated choice labels", count(NEGATED_CHOICE, T, re.I), 0),
    ("O10 fake system UI / faux processing", count(FAKE_SYSTEM_UI, T, re.I), 0),
    ("O11 RECOMMENDED ribbon", count(r"\bRECOMMENDED\b", src), 0),
    ("O12 strike-through without data-source", strikes_unsourced, 0),
    ("C1 AI-slop vocabulary", count(SLOP_WORDS, T, re.I), 0),
    ("C2 hype punctuation / caps words", count(HYPE_PUNCT, T_caps), 0),
    ("C3 headline em-dash chains", count(r"<h[1-3][^>]*>[^<]*—[^<]*—", src), 0),
    ("C4 stock control copy", count(STOCK_CTA, src, re.I), 0),
    ("C5 'not just X but Y' antithesis", count(ANTITHESIS, T, re.I), 0),
    ("C6 'Imagine…' opener", count(IMAGINE, T, re.I), 0),
    ("C7 summary transitions", count(SUMMARY, T, re.I), 0),
    ("C8 generic opener", count(GENERIC_OPENER, src, re.I), 0),
    ("C9 bold-label bullets", count(BOLD_LABEL_BULLET, src, re.I), 0),
    ("C10 placeholder text", count(PLACEHOLDER, both, re.I), 0),
    ("C12 assistant voice", count(ASSISTANT_VOICE, T, re.I), 0),
    ("C13 'Free*' asterisk", count(FREE_ASTERISK, T, re.I), 0),
    ("C14 superlatives without plan claim", len(superlatives_unbacked), 0),
    ("C16 'results vary' without expected result", results_unqualified, 0),
]

fails = 0
print(f"{'check':34} {'count':>5}  result")
for name, n, allowed in checks:
    ok = n <= allowed
    advisory = name.startswith("C")  # copy findings are review notes, not blockers
    fails += (not ok) and not advisory
    print(f"{name:34} {n:>5}  {'PASS' if ok else ('WARN' if advisory else 'FAIL')}")
print("\nBrowser checks still required: N2 (one page background), N8 (cards), N11 (proof), A4 (measure), A7 (contrast).")
if emoji_in_copy_allowed and emoji_count:
    print(f"N1: {emoji_count} emoji allowed by the plan; confirm on the 1280 screenshot that none acts as an icon or separator.")
sys.exit(1 if fails else 0)
