#!/usr/bin/env python3
"""Repair layout data-props drift against the islands' real Props interfaces.

Kept in the repo as the audit trail for the one-time corpus repair: each table
below records WHY a prop was renamed, dropped, or refilled, which the resulting
JSON diff alone doesn't show. Re-running is safe — the script is idempotent, so
it is also usable if hand-authored layouts drift again.

Every rule was derived from the island's real `interface Props` in
packages/storefront-components/src/islands/, cross-checked against the generated
skills/storefront-engine/references/islands/*/schema.json. Rules are one of:

  RENAME   prop was authored under a name the island never had
  DROP     prop does not exist and has no equivalent — remove it
  RETARGET productId → the props the island actually needs
  VALUE    prop exists but the value isn't in the declared enum
  FILL     required prop absent with no resolver to supply it

Verify with: python3 scripts/validate-island-layouts.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ISLANDS_DIR = Path("skills/storefront-engine/references/islands")

# ---------------------------------------------------------------------------
# Per-island prop rewrites.
#   "old": "new"   → rename, value preserved
#   "old": None    → drop
# ---------------------------------------------------------------------------
RENAMES: dict[str, dict[str, str | None]] = {
    # `variant` was never a ProductHero prop; the union it carried is `layout`.
    # ctaText/showPrice/darkMode describe a buy-box, which ProductHero is not —
    # the surrounding layout HTML already renders headline/subheadline/CTA.
    "ProductHero": {
        "variant": "layout",
        "ctaText": None,
        "showPrice": None,
        "darkMode": None,
    },
    # BeforeAfter always renders labels when before.label/after.label are set.
    "BeforeAfter": {"showLabels": None},
    # CountdownTimer's visual union is `style`, not `variant`.
    "CountdownTimer": {"variant": "style"},
    # EmailCapture posts through the shared capture client — no per-mount
    # provider/theme/layout hooks exist.
    "EmailCapture": {
        "ctaText": "buttonText",
        "provider": None,
        "theme": None,
        "layout": None,
    },
    # FAQ has no split mode; the two-column layout does the splitting in CSS.
    "FAQ": {"split": None},
    # IngredientExplorer's union is `layout`; benefits always render when present.
    "IngredientExplorer": {
        "variant": "layout",
        "showBenefits": None,
        "expandable": None,
    },
    "ProceedToCart": {"text": "label"},
    # ProductCarousel sizes itself from `columns`; arrows/dots/gap/loop/
    # autoScroll/speed are not wired.
    "ProductCarousel": {
        "visibleCount": "columns",
        "showArrows": None,
        "showDots": None,
        "gap": None,
        "loop": None,
        "autoScroll": None,
        "speed": None,
    },
    # ProductGallery: zoom is always on; thumbnails are positioned via
    # thumbPosition; aspect ratio comes from the theme, not a prop.
    "ProductGallery": {
        "enableZoom": None,
        "showThumbnails": None,
        "aspectRatio": None,
        "maxImages": None,
    },
    "StickyBar": {"ctaText": "cta", "showImage": None, "variant": None},
    "BuyBox": {"showPaymentIcons": "showTrustBadges", "showQuantity": None},
    # QuantityBreaks highlights the best tier itself.
    "QuantityBreaks": {"highlightBest": None},
    # SubscriptionToggle derives savings from plan discounts; cadence lives on
    # each plan, not the mount.
    "SubscriptionToggle": {"savingsPercent": None, "frequency": None},
    # BundleBuilder's union is `layout`. It takes resolved product objects
    # (mainProduct + recommendations[]), not id lists — nothing expands
    # productIds for it — and a single `bundleDiscount`, not a tier ladder.
    # CTA text and item caps aren't props.
    "BundleBuilder": {
        "variant": "layout",
        "productIds": None,
        "discountTiers": None,
        "ctaText": None,
        "maxItems": None,
        "showProgress": None,
    },
    "ReviewCarousel": {"layout": None, "maxReviews": "pageSize"},
    # SizeGuide takes a single `tip` string; there is no diagram renderer.
    "SizeGuide": {"measurementTips": "tip", "showDiagram": None},
    # Modal: `title`→headline, `description`→body, `showClose`→closable.
    # `trigger` is the mechanism enum (click/delay/scroll/…), so the button text
    # these layouts put there belongs in `triggerLabel`; `id` is `storageKey`.
    # primaryAction/secondaryAction/fullscreen/scrollable/preventClose have no
    # implementation — position/size already cover fullscreen + scroll.
    "Modal": {
        "title": "headline",
        "description": "body",
        "showClose": "closable",
        "trigger": "triggerLabel",
        "id": "storageKey",
        "primaryAction": None,
        "secondaryAction": None,
        "fullscreen": None,
        "scrollable": None,
        "preventClose": None,
    },
    "VariantSwatches": {
        "layout": "type",
        "size": None,
        "showLabel": None,
        "showStock": None,
    },
    # VideoPlayer always shows native controls unless autoplay+muted (loop bg).
    "VideoPlayer": {"controls": None},
    "WishlistButton": {"variant": None, "showCount": None, "position": None},
}

# ---------------------------------------------------------------------------
# Renames to skip when the value is ALREADY correct for the source prop.
#
# `Modal.trigger` is a real prop, so `trigger → triggerLabel` is only right when
# the value is button text rather than a mechanism. Without this guard a second
# run would move the `trigger:"click"` this script just pinned into
# `triggerLabel`, overwriting the real label — i.e. the repair would corrupt the
# corpus it already fixed. Values are the declared enum members.
# ---------------------------------------------------------------------------
RENAME_SKIP_VALUES: dict[str, dict[str, set[str]]] = {
    "Modal": {"trigger": {"click", "exit_intent", "delay", "scroll", "event"}},
}

# ---------------------------------------------------------------------------
# Enum values that were authored in the wrong casing/spelling.
# ---------------------------------------------------------------------------
VALUE_FIXES: dict[str, dict[str, dict[str, str]]] = {
    "Modal": {
        "animation": {"slideUp": "slide-up", "slideRight": "slide-right"},
        # `backdrop` is a boolean; "dim"/"blur" were treated as styles.
        "backdrop": {"dim": True, "blur": True, "none": False},
    },
    "VariantSwatches": {
        # After layout→type: circles/images/buttons → the real union.
        "type": {
            "circles": "color",
            "images": "image",
            "buttons": "size_grid",
            "grid": "size_grid",
        },
    },
    "ProductCarousel": {"cardVariant": {"compact": "compact"}},
    "BundleBuilder": {"layout": {"horizontal": "horizontal", "stacked": "stacked"}},
    "ProductHero": {
        "layout": {
            "splitLeft": "splitLeft",
            "splitRight": "splitRight",
            "fullHeight": "fullHeight",
            "stacked": "stacked",
        }
    },
}

# ---------------------------------------------------------------------------
# `productId` on an island the runtime resolver does not serve. The resolver
# (services/storefront-renderer/app/lib/islands/product-resolver.client.ts)
# only expands productId for PRODUCT_RESOLVE_ISLANDS; everywhere else it is a
# no-op and the island's required props stay undefined.
#
# ProductHero is the exception: it is being ADDED to the resolver in this same
# change (its required `images` matches mapToGalleryProps exactly), so its
# productId is kept.
# ---------------------------------------------------------------------------
PRODUCT_ID_RETARGET: dict[str, dict] = {
    # DeliveryEstimate needs no product data — it's a date/cutoff calculator.
    "DeliveryEstimate": {"drop": True},
    # ReviewCarousel's fetch mode is reviewsEndpoint + productIds[].
    "ReviewCarousel": {
        "rename": "productIds",
        "wrap_in_array": True,
        "add": {"reviewsEndpoint": "{{REVIEWS_ENDPOINT}}"},
    },
}
PRODUCT_ID_KEEP = {"ProductHero"}

# ---------------------------------------------------------------------------
# Islands referenced by layouts that do not exist in the registry.
#   replace_with: mount a real island that covers the same intent
#   inline:       drop the mount, the surrounding static HTML already covers it
# ---------------------------------------------------------------------------
PHANTOM_ISLANDS: dict[str, dict] = {
    # No TrustBadgeBar island exists. BuyBox's showTrustBadges covers the same
    # PDP trust row, and split-pdp already mounts a BuyBox.
    "TrustBadgeBar": {"inline": True},
    # No SocialIcons island. Footer renders socialLinks itself, and all three
    # footer layouts already pass socialLinks to their Footer mount.
    "SocialIcons": {"inline": True},
}

# ---------------------------------------------------------------------------
# Required props missing with no resolver to fill them. Each value is a
# placeholder the generating agent substitutes, consistent with the
# {{TEMPLATE_VAR}} convention already used across the corpus.
# ---------------------------------------------------------------------------
REQUIRED_FILLS: dict[str, dict[str, str]] = {
    "PaymentOptions": {"price": "{{PRICE_CENTS}}"},
    "QuantityBreaks": {"variantId": "{{VARIANT_ID}}"},
    "SubscriptionToggle": {"oneTimePrice": "{{ONE_TIME_PRICE}}"},
    "BundleBuilder": {
        "mainProduct": "{{MAIN_PRODUCT_JSON}}",
        "recommendations": "{{RECOMMENDATIONS_JSON}}",
        "bundleDiscount": "{{BUNDLE_DISCOUNT_JSON}}",
    },
    "Footer": {"links": "{{FOOTER_LINKS}}"},
    "ProductHero": {},  # served by the resolver via productId
}

# ---------------------------------------------------------------------------
# Nested-object rewrites. An object prop present but missing a required field of
# its shape still crashes — the top-level key check can't see it.
#   "a.b": "a.c"   → rename nested key
#   "a.b": None    → drop nested key
# ---------------------------------------------------------------------------
NESTED_RENAMES: dict[str, dict[str, str | None]] = {
    # Navbar/SiteHeader render `cta.label`, not `cta.text`.
    "Navbar": {"cta.text": "cta.label"},
    "SiteHeader": {
        "navbar.cta.text": "navbar.cta.label",
        # `announcement.messages` is a string[] the rotator indexes into;
        # `announcement.text` was a single string. `announcement.link` is a
        # plain URL string, not {url, text}.
        "announcement.text": "announcement.messages",
        "announcement.link": None,
    },
    # SizeGuide's `units` is {metric, imperial} label strings — the labels shown
    # on the toggle — not {default, available}.
    "SizeGuide": {"units.default": None, "units.available": None},
}

# Nested values to coerce into the shape the island expects, after renames.
#   (prop path) → callable applied to the value
NESTED_COERCE: dict[str, dict[str, str]] = {
    # A single announcement string becomes a one-element messages array.
    "SiteHeader": {"announcement.messages": "wrap_in_array"},
}

# Nested fields to fill when the parent object is present but the field missing.
NESTED_FILLS: dict[str, dict[str, object]] = {
    "QuickAdd": {"product.variants": "{{VARIANTS_JSON}}"},
    "SizeGuide": {"units.metric": "cm", "units.imperial": "in"},
}

# ---------------------------------------------------------------------------
# Placeholders whose name/quoting still advertises the OLD type after a rename.
# Applied only when the current value is a placeholder.
# ---------------------------------------------------------------------------
RETYPE_PLACEHOLDER: dict[str, dict[str, str]] = {
    # measurementTips → tip renames a plural to a `?string`, but the value stayed
    # a bare `{{TIPS_JSON}}` — both the name and the missing quotes still tell the
    # generating agent to substitute an array. Re-point it at a quoted scalar.
    "SizeGuide": {"tip": "{{MEASUREMENT_TIP}}"},
}

# ---------------------------------------------------------------------------
# Props to pin after renames, where the island's default would otherwise change
# behaviour. Only applied when the key is absent.
# ---------------------------------------------------------------------------
ENSURE: dict[str, dict[str, object]] = {
    # These layouts put button text in `trigger`, which means they intended a
    # click-to-open modal. Modal's `trigger` default is "delay" (auto-opens
    # after 5s), so leaving it unset would turn a size-guide button into an
    # uninvited popup.
    "Modal": {"trigger": "click"},
}

PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")

# Rewrite the opening tag only. Mounts vary: some are self-closing empty divs,
# some carry extra attributes (class/style), some wrap children (Modal). Matching
# just the tag keeps all three intact.
MOUNT_RE = re.compile(
    r"""<(?P<tag>\w+)(?P<pre>[^>]*?)\sdata-island="(?P<name>[A-Za-z0-9_]+)\""""
    r"""(?P<mid>[^>]*?)\sdata-props='(?P<props>[^']*)'(?P<post>[^>]*?)>"""
)
# A phantom mount is always an empty div, so it is safe to delete whole.
PHANTOM_RE = re.compile(
    r"""<div[^>]*?\sdata-island="(?P<name>[A-Za-z0-9_]+)\"[^>]*?>\s*</div>"""
)


def props_to_json(raw: str) -> tuple[dict, dict[str, str], set[str]]:
    """Parse data-props, remembering which keys held {{PLACEHOLDERS}}.

    Returns (props, token_by_sentinel, sentinels_that_were_bare). A bare
    placeholder (`"x":{{FOO}}`) stood in for an array/object/number; a quoted one
    (`"x":"{{FOO}}"`) stood in for a string. Round-tripping has to preserve that
    distinction or a `"[...]"` string reaches an island expecting an array.
    """
    holders: dict[str, str] = {}
    bare: set[str] = set()

    def stash(match: re.Match) -> str:
        token = match.group(0)
        key = f"__PH{len(holders)}__"
        holders[key] = token
        # Quoted in the source iff the chars either side are both quotes.
        start, end = match.span()
        was_quoted = (
            start > 0 and raw[start - 1] == '"'
            and end < len(raw) and raw[end] == '"'
        )
        if not was_quoted:
            bare.add(key)
        return f'"{key}"'

    text = PLACEHOLDER_RE.sub(stash, raw)
    # A placeholder that was already quoted is now ""__PH0__"" — collapse it.
    text = re.sub(r'""(__PH\d+__)""', r'"\1"', text)
    return json.loads(text), holders, bare


# Placeholders this script introduces. They live in the fill tables as Python
# strings, so serialising emits them quoted; anything standing for a non-string
# has to be unquoted again or the island receives "[...]" where it wants [...].
# Every fill placeholder must appear in exactly one set — assert_fills_classified()
# turns an omission into a crash instead of a silently corrupted layout.
FILL_IS_BARE = {
    "{{PRICE_CENTS}}",  # number
    "{{FOOTER_LINKS}}",  # array
    "{{MAIN_PRODUCT_JSON}}",  # object
    "{{RECOMMENDATIONS_JSON}}",  # array
    "{{BUNDLE_DISCOUNT_JSON}}",  # object
    "{{VARIANTS_JSON}}",  # array
}
FILL_IS_STRING = {
    "{{VARIANT_ID}}",
    "{{ONE_TIME_PRICE}}",
    "{{REVIEWS_ENDPOINT}}",
}


def assert_fills_classified() -> None:
    """Every placeholder in a fill table must be classified bare or string."""
    used: set[str] = set()
    for table in (REQUIRED_FILLS, NESTED_FILLS):
        for fills in table.values():
            used.update(v for v in fills.values() if isinstance(v, str))
    for rule in PRODUCT_ID_RETARGET.values():
        used.update(v for v in rule.get("add", {}).values() if isinstance(v, str))

    used = {v for v in used if PLACEHOLDER_RE.fullmatch(v)}
    unclassified = used - FILL_IS_BARE - FILL_IS_STRING
    if unclassified:
        raise SystemExit(
            "unclassified fill placeholder(s): "
            + ", ".join(sorted(unclassified))
            + " — add each to FILL_IS_BARE (array/object/number) or FILL_IS_STRING"
        )
    both = FILL_IS_BARE & FILL_IS_STRING
    if both:
        raise SystemExit(f"placeholder in both fill sets: {sorted(both)}")

    # Retyped placeholders are emitted quoted via the holders map; if one also sat
    # in FILL_IS_BARE, json_to_props' final pass would unquote it again.
    retyped = {t for table in RETYPE_PLACEHOLDER.values() for t in table.values()}
    clash = retyped & FILL_IS_BARE
    if clash:
        raise SystemExit(f"retyped placeholder(s) also in FILL_IS_BARE: {sorted(clash)}")


def json_to_props(data: dict, holders: dict[str, str], bare: set[str]) -> str:
    """Serialise back to a data-props blob, restoring placeholder quoting."""
    text = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    for key, token in holders.items():
        if key in bare:
            text = text.replace(f'"{key}"', token)
        else:
            text = text.replace(key, token)
    # Placeholders this script added are literal strings in `data`; unquote the
    # ones standing for arrays/objects/numbers.
    for token in FILL_IS_BARE:
        text = text.replace(f'"{token}"', token)
    return text


def retype_placeholders(
    island: str, props: dict, holders: dict[str, str], bare: set[str]
) -> list[str]:
    """Swap a placeholder for one whose name and quoting match the new type.

    Operates on the holders map rather than on `props` so the quoting decision
    stays in json_to_props: dropping the key out of `bare` is what re-quotes it.
    """
    log: list[str] = []
    for key, new_token in RETYPE_PLACEHOLDER.get(island, {}).items():
        holder = props.get(key)
        if not isinstance(holder, str) or holder not in holders:
            continue
        old_token = holders[holder]
        if old_token == new_token:
            continue
        holders[holder] = new_token
        bare.discard(holder)  # emit quoted — it stands for a string now
        log.append(f"{key}: {old_token} → \"{new_token}\"")
    return log


def dig(obj: dict, path: str) -> tuple[dict | None, str]:
    """Walk a dotted path, returning (parent_dict, last_key) or (None, key)."""
    parts = path.split(".")
    cur = obj
    for part in parts[:-1]:
        nxt = cur.get(part) if isinstance(cur, dict) else None
        if not isinstance(nxt, dict):
            return None, parts[-1]
        cur = nxt
    return cur, parts[-1]


def repair_props(island: str, props: dict) -> tuple[dict, list[str]]:
    """Apply every rule for one mount. Returns (new_props, change log)."""
    out = dict(props)
    log: list[str] = []

    # 1. productId retargeting (before renames, so renames see final keys).
    if "productId" in out and island not in PRODUCT_ID_KEEP:
        rule = PRODUCT_ID_RETARGET.get(island)
        if rule is None:
            pass  # island is resolver-served; leave it alone
        elif rule.get("drop"):
            out.pop("productId")
            log.append("drop productId (not resolver-served, island needs no product)")
        else:
            value = out.pop("productId")
            new_key = rule["rename"]
            out[new_key] = [value] if rule.get("wrap_in_array") else value
            for k, v in rule.get("add", {}).items():
                out.setdefault(k, v)
            log.append(f"productId → {new_key}" + (" + reviewsEndpoint" if rule.get("add") else ""))

    # 2. Renames and drops.
    skips = RENAME_SKIP_VALUES.get(island, {})
    for old, new in RENAMES.get(island, {}).items():
        if old not in out:
            continue
        # Only scalars can be a declared enum member, and dict/list values are
        # unhashable — check the type before the set lookup.
        if isinstance(out[old], str) and out[old] in skips.get(old, set()):
            continue  # already a valid value for this prop — nothing to move
        value = out.pop(old)
        if new is None:
            log.append(f"drop {old}")
        else:
            out[new] = value
            log.append(f"{old} → {new}")

    # 3. Enum / type value corrections.
    for key, mapping in VALUE_FIXES.get(island, {}).items():
        if key in out and isinstance(out[key], str) and out[key] in mapping:
            before = out[key]
            out[key] = mapping[before]
            if before != out[key]:
                log.append(f"{key}: {before!r} → {out[key]!r}")

    # 4. Fill required props the resolver won't supply.
    for key, placeholder in REQUIRED_FILLS.get(island, {}).items():
        if key not in out:
            out[key] = placeholder
            log.append(f"add required {key}")

    # 5. Nested renames / drops.
    out = json.loads(json.dumps(out))  # deep copy before mutating nested dicts
    for path, new_path in NESTED_RENAMES.get(island, {}).items():
        parent, key = dig(out, path)
        if parent is None or key not in parent:
            continue
        value = parent.pop(key)
        if new_path is None:
            log.append(f"drop {path}")
            continue
        target_parent, target_key = dig(out, new_path)
        if target_parent is None:
            continue
        target_parent[target_key] = value
        log.append(f"{path} → {new_path}")

    # 6. Nested coercions.
    for path, how in NESTED_COERCE.get(island, {}).items():
        parent, key = dig(out, path)
        if parent is None or key not in parent:
            continue
        if how == "wrap_in_array" and not isinstance(parent[key], list):
            parent[key] = [parent[key]]
            log.append(f"{path} → array")

    # 7. Nested required fills.
    for path, value in NESTED_FILLS.get(island, {}).items():
        parent, key = dig(out, path)
        if parent is None or key in parent:
            continue
        parent[key] = value
        log.append(f"add required {path}")

    # 8. Pin props whose default would otherwise change behaviour.
    if log:  # only when we already touched this mount
        for key, pinned in ENSURE.get(island, {}).items():
            if key not in out:
                out[key] = pinned
                log.append(f"pin {key}={pinned!r}")

    return out, log


def main() -> int:
    dry = "--dry-run" in sys.argv
    assert_fills_classified()
    if not ISLANDS_DIR.is_dir():
        print(f"error: {ISLANDS_DIR} not found — run from the repo root")
        return 1

    touched = 0
    for path in sorted(ISLANDS_DIR.glob("*/layouts/*.json")):
        layout = json.loads(path.read_text(encoding="utf-8"))
        html = layout.get("html", "") or ""
        file_log: list[str] = []

        def drop_phantom(match: re.Match) -> str:
            island = match.group("name")
            phantom = PHANTOM_ISLANDS.get(island)
            if phantom and phantom.get("inline"):
                file_log.append(f"{island}: remove phantom mount (island does not exist)")
                return ""
            return match.group(0)

        def rewrite(match: re.Match) -> str:
            island = match.group("name")
            if island in PHANTOM_ISLANDS:
                return match.group(0)  # already handled by drop_phantom

            try:
                props, holders, bare = props_to_json(match.group("props"))
            except json.JSONDecodeError as exc:
                file_log.append(f"{island}: SKIPPED — unparseable data-props ({exc})")
                return match.group(0)

            new_props, changes = repair_props(island, props)
            changes += retype_placeholders(island, new_props, holders, bare)
            if not changes:
                return match.group(0)
            file_log.extend(f"{island}: {c}" for c in changes)
            blob = json_to_props(new_props, holders, bare)
            # Preserve the tag name and every other attribute; swap data-props.
            return (
                f"<{match.group('tag')}{match.group('pre')}"
                f' data-island="{island}"{match.group("mid")}'
                f" data-props='{blob}'{match.group('post')}>"
            )

        new_html = MOUNT_RE.sub(rewrite, PHANTOM_RE.sub(drop_phantom, html))

        if new_html == html:
            continue

        touched += 1
        print(f"\n{path.as_posix()}")
        for line in file_log:
            print(f"  {line}")

        if not dry:
            layout["html"] = new_html
            path.write_text(
                json.dumps(layout, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

    print(f"\n{'would touch' if dry else 'repaired'} {touched} layout file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
