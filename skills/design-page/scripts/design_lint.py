#!/usr/bin/env python3
"""Static design-rule checks for a Lexsis page workspace.

Usage: design_lint.py <workspace>
Runs the grep-able rules from storefront-engine/references/design-rules.md
(N1, N3-N7, N9, N10, N12-N14, A11, A12) against lexsis-source.html and
page-theme.css. Exit 1 when any check fails. N2, N8, N11, A4 and A7 need the
browser checks described in design-rules.md.
"""
import pathlib
import re
import sys

W = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
src = (W / "lexsis-source.html").read_text(encoding="utf-8")
css_path = W / "page-theme.css"
css = css_path.read_text(encoding="utf-8") if css_path.exists() else ""
both = src + "\n" + css

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

checks = [
    ("N1 emoji", len(EMOJI.findall(both)), 0),
    ("N3 stroke-width variants", max(0, len(set(re.findall(r'stroke-width="([^"]*)"', src))) - 1), 0),
    ("N3 img used as icon", count(r'<img[^>]*class="[^"]*icon', src), 0),
    ("N4 font families (<=3)", max(0, len(set(re.findall(r"family=([A-Za-z+]+)", css))) - 3), 0),
    ("N5 uppercase", count(r"\buppercase\b|text-transform:\s*uppercase", both), 0),
    ("N6 accent inside headline", count(r"<h[1-3][^>]*>[^<]*<(span|em|strong|i|b|mark)", src), 0),
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
    ("A11 focus-visible present", 0 if ":focus-visible" in css else 1, 0),
    ("A12 stock CTA copy", count(r">(Shop Now|Get Started|Learn More|Buy Now)\s*(→)?<", src), 0),
]

fails = 0
print(f"{'check':34} {'count':>5}  result")
for name, n, allowed in checks:
    ok = n <= allowed
    fails += not ok
    print(f"{name:34} {n:>5}  {'PASS' if ok else 'FAIL'}")
print("\nBrowser checks still required: N2 (one page background), N8 (cards), N11 (proof), A4 (measure), A7 (contrast).")
sys.exit(1 if fails else 0)
