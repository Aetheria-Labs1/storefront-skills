#!/usr/bin/env python3
"""Validate local Lexsis storefront page files without changing them."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path
from typing import Any


SECTION_RE = re.compile(
    r"<!--\s*section:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*-->(.*?)(?=<!--\s*section:|\Z)",
    re.IGNORECASE | re.DOTALL,
)
SECTION_ID_RE = re.compile(r"<section\b[^>]*\bid\s*=\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)
ID_RE = re.compile(r"\bid\s*=\s*['\"]([^'\"]+)['\"]", re.IGNORECASE)
TAG_RE = re.compile(r"<([a-z][\w:-]*)\b([^>]*)>", re.IGNORECASE | re.DOTALL)
STYLE_RE = re.compile(r"<style\b[^>]*>(.*?)</style\s*>", re.IGNORECASE | re.DOTALL)
ISLAND_RE = re.compile(r"<lx-island\b([^>]*)>(.*?)</lx-island\s*>", re.IGNORECASE | re.DOTALL)
JSON_SCRIPT_RE = re.compile(
    r"<script\b[^>]*\btype\s*=\s*['\"]application/json['\"][^>]*>(.*?)</script\s*>",
    re.IGNORECASE | re.DOTALL,
)
INLINE_HANDLER_RE = re.compile(r"\son[a-z]+\s*=", re.IGNORECASE)
SCRIPT_SRC_RE = re.compile(r"<script\b[^>]*\bsrc\s*=", re.IGNORECASE)
LOCAL_PATH_RE = re.compile(r"(?:file://|(?:src|href)\s*=\s*['\"](?:/tmp/|\.{1,2}/))", re.IGNORECASE)
MEDIA_URL_RE = re.compile(
    r"<(?:img|video|source)\b[^>]*\b(?:src|poster)\s*=\s*(['\"])(.*?)\1",
    re.IGNORECASE | re.DOTALL,
)
JSON_MEDIA_URL_RE = re.compile(
    r'"(?:src|poster|image|imageSrc|videoSrc|thumbnail|thumbnailUrl)"\s*:\s*"([^"]+)"',
    re.IGNORECASE,
)
CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
PLACEHOLDER_URL_RE = re.compile(
    r"(?:placeholder\.(?:com|co)|example\.(?:com|org)|localhost|127\.0\.0\.1|TEMP_URL|ASSET_URL|IMAGE_URL)",
    re.IGNORECASE,
)
PLACEHOLDER_TOKEN_RE = re.compile(
    r"(?:\{\{[^{}]+\}\}|ASSET\[[^\]]+\]|"
    r"\b(?:PRODUCT|VARIANT|PAGE_SHORT|WORKSPACE|STORE|THEME|ASSET|IMAGE|VIDEO)_ID\b)",
    re.IGNORECASE,
)
PREVIEW_PLACEHOLDER_RE = re.compile(
    r"(?:assets/placeholders/|preview-placeholder|PREVIEW PLACEHOLDER)",
    re.IGNORECASE,
)
UNSUPPORTED_JS_RE = re.compile(
    r"\b(?:fetch|XMLHttpRequest|eval|localStorage|WebSocket)\s*(?:\(|\.)",
    re.IGNORECASE,
)
BANNED_COPY = (
    "matched to the meta creative",
    "creator energy",
    "product clarity",
    "proof point",
    "placeholder",
    "layout concept",
    "insert copy",
    "ashton hall approved",
    "agent instruction",
    "implementation note",
)
QA_FIELDS = (
    "responsive",
    "visualRegression",
    "commerce",
    "copy",
    "claims",
    "assets",
    "integrity",
)
SOURCE_PHASES = {"design", "visual", "precompile", "adopted", "draft", "publish"}
PRODUCTION_PHASES = {"precompile", "adopted", "draft", "publish"}
REMOTE_READY_PHASES = {"draft", "publish"}


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def canonical_config(
    page_config: dict[str, Any],
    compile_inputs: dict[str, Any] | None = None,
) -> str:
    payload = {
        "head": page_config.get("head", {}),
        "scripts": page_config.get("scripts", []),
        "compileInputs": compile_inputs or {},
    }
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def config_hash(
    page_config: dict[str, Any],
    compile_inputs: dict[str, Any] | None = None,
) -> str:
    return sha256(canonical_config(page_config, compile_inputs))


def canonical_bundle(
    source: str,
    page_config: dict[str, Any],
    theme_css: str = "",
    compile_inputs: dict[str, Any] | None = None,
) -> str:
    payload = {
        "source": source,
        "head": page_config.get("head", {}),
        "themeCss": theme_css or page_config.get("themeCss", ""),
        "scripts": page_config.get("scripts", []),
        "compileInputs": compile_inputs or {},
    }
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def bundle_hash(
    source: str,
    page_config: dict[str, Any],
    theme_css: str = "",
    compile_inputs: dict[str, Any] | None = None,
) -> str:
    return sha256(canonical_bundle(source, page_config, theme_css, compile_inputs))


def compiled_response_hash(response: dict[str, Any]) -> str:
    candidates = [
        response.get("page"),
        response.get("compiled_page"),
        response.get("result", {}).get("page")
        if isinstance(response.get("result"), dict)
        else None,
    ]
    compiled = next((item for item in candidates if isinstance(item, dict)), None)
    if compiled is None and isinstance(response.get("sections"), list):
        compiled = {"sections": response["sections"]}
    if compiled is None:
        raise ValueError("Compile response does not contain a compiled page")
    return sha256(
        json.dumps(compiled, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    )


def section_hashes(source: str) -> dict[str, str]:
    return {match.group(1): sha256(match.group(0)) for match in SECTION_RE.finditer(source)}


def structure_hash(source: str) -> str:
    structure: list[dict[str, Any]] = []
    for match in SECTION_RE.finditer(source):
        section_id, body = match.group(1), match.group(2)
        tags = [
            {
                "name": tag.group(1).lower(),
                "attrs": re.sub(r"\s+", " ", tag.group(2)).strip(),
            }
            for tag in TAG_RE.finditer(body)
            if tag.group(1).lower() not in {"script", "style"}
        ]
        styles = [re.sub(r"\s+", " ", item).strip() for item in STYLE_RE.findall(body)]
        islands = [
            {
                "name": attr_value(item.group(1), "name"),
                "headless": bool(re.search(r"(?:^|\s)headless(?:\s|=|$)", item.group(1), re.IGNORECASE)),
            }
            for item in ISLAND_RE.finditer(body)
        ]
        structure.append(
            {"sectionId": section_id, "tags": tags, "styles": styles, "islands": islands}
        )
    return sha256(
        json.dumps(structure, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    )


def attr_value(attrs: str, name: str) -> str | None:
    match = re.search(
        rf"\b{re.escape(name)}\s*=\s*(['\"])(.*?)\1",
        attrs,
        re.IGNORECASE | re.DOTALL,
    )
    return match.group(2) if match else None


def visible_text(source: str) -> str:
    text = re.sub(
        r"<!--.*?-->|<style\b.*?</style\s*>|<script\b.*?</script\s*>",
        " ",
        source,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def finding(code: str, message: str, path: str | None = None) -> dict[str, str]:
    item = {"code": code, "message": message}
    if path:
        item["path"] = path
    return item


def resolve_workspace_path(directory: Path, raw_path: Any) -> Path:
    path = Path(str(raw_path))
    if path.is_absolute():
        return path
    for base in (directory, Path.cwd(), *directory.parents):
        candidate = base / path
        if candidate.exists():
            return candidate
    return directory / path


def read_json_file(path: Path, errors: list[dict[str, str]], code: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(finding(code, f"Invalid JSON: {exc}", path.name))
        return {}
    if not isinstance(value, dict):
        errors.append(finding(code, "JSON root must be an object", path.name))
        return {}
    return value


def validate_workspace(
    directory: Path,
    phase: str,
    current_remote_version: int | str | None = None,
    remote_source_hash: str | None = None,
    remote_bundle_hash: str | None = None,
) -> dict[str, Any]:
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    required = ["page-plan.md", "page-manifest.json"]
    if phase in SOURCE_PHASES:
        required.extend(["lexsis-source.html", "page-theme.css"])
    if phase in {"adopted", "draft", "publish"}:
        required.append("qa-report.md")
    for name in required:
        if not (directory / name).is_file():
            errors.append(finding("missing_artifact", f"Missing required file: {name}", name))
    if not (directory / "assets").is_dir():
        errors.append(finding("missing_assets_directory", "Missing assets/ directory", "assets"))

    manifest_path = directory / "page-manifest.json"
    manifest = (
        read_json_file(manifest_path, errors, "invalid_manifest")
        if manifest_path.is_file()
        else {}
    )

    if manifest:
        if manifest.get("schemaVersion") != 3:
            errors.append(
                finding(
                    "manifest_schema",
                    "Manifest must use schemaVersion 3; migrate legacy workspaces first",
                    manifest_path.name,
                )
            )
        page = manifest.get("page")
        if not isinstance(page, dict) or not all(
            page.get(key) for key in ("title", "handle", "archetype")
        ):
            errors.append(
                finding(
                    "manifest_page",
                    "Manifest page requires title, handle, and archetype",
                    manifest_path.name,
                )
            )
        for key in ("workspaceId", "storeId", "themeId", "setupPath"):
            if not manifest.get(key):
                errors.append(
                    finding("manifest_binding", f"Manifest requires {key}", manifest_path.name)
                )
        if not isinstance(manifest.get("sections"), list):
            errors.append(
                finding("manifest_sections", "Manifest sections must be an array", manifest_path.name)
            )
        products = manifest.get("products", [])
        if not isinstance(products, list) or any(
            not isinstance(item, dict) or not item.get("productId")
            for item in products
        ):
            errors.append(
                finding(
                    "manifest_products",
                    "Manifest products must contain compact productId bindings",
                    manifest_path.name,
                )
            )

        template = manifest.get("template")
        if not isinstance(template, dict) or template.get("mode") not in {
            "page-kit",
            "sections",
            "custom",
        }:
            errors.append(
                finding(
                    "template_mode",
                    "Manifest template mode must be page-kit, sections, or custom",
                    manifest_path.name,
                )
            )
        elif template.get("mode") == "page-kit" and not template.get("pageKitId"):
            errors.append(
                finding("template_page_kit", "Page-kit mode requires pageKitId", manifest_path.name)
            )
        elif template.get("mode") == "sections" and not template.get("sectionTemplateIds"):
            errors.append(
                finding(
                    "template_sections",
                    "Section mode requires sectionTemplateIds",
                    manifest_path.name,
                )
            )

        setup_path = resolve_workspace_path(directory, manifest.get("setupPath", ""))
        if not setup_path.is_file():
            errors.append(finding("setup_missing", "Saved setup file does not exist", str(setup_path)))
        else:
            setup = read_json_file(setup_path, errors, "setup_invalid")
            if setup:
                if setup.get("workspaceId") != manifest.get("workspaceId"):
                    errors.append(
                        finding(
                            "setup_workspace",
                            "Manifest workspace does not match saved setup",
                            manifest_path.name,
                        )
                    )
                selected_store = next(
                    (
                        item
                        for item in setup.get("stores", [])
                        if isinstance(item, dict)
                        and item.get("storeId") == manifest.get("storeId")
                    ),
                    None,
                )
                if not selected_store:
                    errors.append(
                        finding(
                            "setup_store",
                            "Manifest store is not present in saved setup",
                            manifest_path.name,
                        )
                    )
                else:
                    brand_path = resolve_workspace_path(
                        setup_path.parent,
                        selected_store.get("brandDesignPath", ""),
                    )
                    if not brand_path.is_file():
                        errors.append(
                            finding("brand_design_missing", "Saved brand design does not exist", str(brand_path))
                        )
                    selected_theme = next(
                        (
                            item
                            for item in selected_store.get("themes", [])
                            if isinstance(item, dict)
                            and item.get("themeId") == manifest.get("themeId")
                        ),
                        None,
                    )
                    if not selected_theme:
                        errors.append(
                            finding(
                                "setup_theme",
                                "Manifest theme is not saved for the selected store",
                                manifest_path.name,
                            )
                        )
                    else:
                        theme_file = resolve_workspace_path(
                            setup_path.parent,
                            selected_theme.get("themeCssPath", ""),
                        )
                        if not theme_file.is_file():
                            errors.append(
                                finding("theme_css_missing", "Saved theme CSS does not exist", str(theme_file))
                            )

        if phase in SOURCE_PHASES:
            if not isinstance(manifest.get("config", {}), dict):
                errors.append(
                    finding("manifest_config", "Manifest config must be an object", manifest_path.name)
                )
            if not isinstance(manifest.get("assets", []), list):
                errors.append(
                    finding("manifest_assets", "Manifest assets must be an array", manifest_path.name)
                )
            if not isinstance(manifest.get("islands", []), list):
                errors.append(
                    finding("manifest_islands", "Manifest islands must be an array", manifest_path.name)
                )

    source_path = directory / "lexsis-source.html"
    source = source_path.read_text(encoding="utf-8") if source_path.is_file() else ""
    theme_path = directory / "page-theme.css"
    theme_css = theme_path.read_text(encoding="utf-8") if theme_path.is_file() else ""
    config = manifest.get("config", {}) if manifest else {}
    if not isinstance(config, dict):
        config = {}
    page_config = {
        "head": config.get("head", {}),
        "scripts": config.get("scripts", []),
    }
    compile_inputs = {
        "productBinding": config.get("productBinding", {}),
        "commerceConfig": config.get("commerceConfig", {}),
    }
    if manifest and "themeCss" in config:
        errors.append(
            finding(
                "embedded_theme_css",
                "Store global CSS in page-theme.css, not manifest config",
                manifest_path.name,
            )
        )
    if phase in SOURCE_PHASES:
        if not source.strip():
            errors.append(finding("empty_source", "Canonical source cannot be empty", source_path.name))
        if not theme_css.strip():
            errors.append(finding("page_theme", "page-theme.css cannot be empty", theme_path.name))
        if not isinstance(page_config.get("head"), dict):
            errors.append(finding("page_head", "config.head must be an object", manifest_path.name))
        if not isinstance(page_config.get("scripts"), list):
            errors.append(finding("page_scripts", "config.scripts must be an array", manifest_path.name))

    source_sections: list[str] = []
    source_islands: list[dict[str, str]] = []
    hashes: dict[str, str] = {}
    if source:
        matches = list(SECTION_RE.finditer(source))
        source_sections = [match.group(1) for match in matches]
        hashes = section_hashes(source)
        if not matches:
            errors.append(finding("missing_sections", "Source has no section delimiters", source_path.name))
        elif source[: matches[0].start()].strip():
            errors.append(
                finding(
                    "content_before_section",
                    "Source contains content before the first section",
                    source_path.name,
                )
            )
        if len(source_sections) != len(set(source_sections)):
            errors.append(finding("duplicate_section", "Source has duplicate section delimiters", source_path.name))
        all_ids = ID_RE.findall(source)
        if len(all_ids) != len(set(all_ids)):
            errors.append(finding("duplicate_html_id", "Source has duplicate HTML IDs", source_path.name))
        for match in matches:
            section_id, body = match.group(1), match.group(2)
            section_tag = SECTION_ID_RE.search(body)
            if not section_tag:
                errors.append(
                    finding(
                        "missing_section_id",
                        f"Section {section_id!r} has no matching <section id>",
                        source_path.name,
                    )
                )
            elif section_tag.group(1) != section_id:
                errors.append(
                    finding(
                        "section_id_mismatch",
                        f"Delimiter {section_id!r} does not match section id {section_tag.group(1)!r}",
                        source_path.name,
                    )
                )
            for island in ISLAND_RE.finditer(body):
                attrs, island_body = island.group(1), island.group(2)
                name = attr_value(attrs, "name")
                if not name:
                    errors.append(
                        finding(
                            "island_missing_name",
                            f"Island in section {section_id!r} has no name",
                            source_path.name,
                        )
                    )
                    continue
                source_islands.append({"sectionId": section_id, "name": name})
                payload = JSON_SCRIPT_RE.search(island_body)
                if not payload:
                    errors.append(
                        finding(
                            "island_missing_json",
                            f"Island {name!r} has no application/json script",
                            source_path.name,
                        )
                    )
                else:
                    try:
                        json.loads(payload.group(1))
                    except json.JSONDecodeError as exc:
                        errors.append(
                            finding(
                                "invalid_island_json",
                                f"Island {name!r} has invalid JSON: {exc}",
                                source_path.name,
                            )
                        )
        if re.search(r"\bdata-island\s*=", source, re.IGNORECASE):
            errors.append(
                finding(
                    "compiled_source_island",
                    "Source must use <lx-island>, not compiled data-island markup",
                    source_path.name,
                )
            )
        if INLINE_HANDLER_RE.search(source):
            errors.append(finding("inline_handler", "Source contains an inline event handler", source_path.name))
        if SCRIPT_SRC_RE.search(source):
            errors.append(finding("script_src", "External scripts belong in config.scripts", source_path.name))
        if UNSUPPORTED_JS_RE.search(source):
            errors.append(finding("unsupported_script", "Source contains unsupported JavaScript", source_path.name))
        if PLACEHOLDER_URL_RE.search(source):
            errors.append(
                finding(
                    "placeholder_url",
                    "Source contains a placeholder or development URL",
                    source_path.name,
                )
            )
        if PLACEHOLDER_TOKEN_RE.search(source):
            errors.append(
                finding(
                    "placeholder_token",
                    "Source contains an unresolved placeholder token",
                    source_path.name,
                )
            )
        semantic = re.sub(
            r"<!--.*?-->|<style\b.*?</style\s*>|<script\b.*?</script\s*>",
            "",
            source,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if (
            len(matches) <= 1
            and len(re.findall(r"<img\b", semantic, re.IGNORECASE)) == 1
            and not re.search(
                r"<(?:h1|h2|p|button|form|details|lx-island)\b",
                semantic,
                re.IGNORECASE,
            )
        ):
            errors.append(
                finding(
                    "complete_page_image",
                    "One image cannot be used as the complete page layout",
                    source_path.name,
                )
            )
        customer_copy = visible_text(source).casefold()
        for phrase in BANNED_COPY:
            if phrase in customer_copy:
                errors.append(
                    finding(
                        "internal_copy",
                        f"Customer copy contains internal wording: {phrase}",
                        source_path.name,
                    )
                )
        for comment in re.findall(r"<!--(.*?)-->", source, re.DOTALL):
            if not re.fullmatch(
                r"\s*section:\s*[a-z0-9]+(?:-[a-z0-9]+)*\s*",
                comment,
                re.IGNORECASE,
            ):
                errors.append(
                    finding(
                        "production_comment",
                        "Source comments may only be section delimiters",
                        source_path.name,
                    )
                )

        if phase in PRODUCTION_PHASES:
            if PREVIEW_PLACEHOLDER_RE.search(source):
                errors.append(
                    finding(
                        "placeholder_in_source",
                        "Replace visual placeholders before production",
                        source_path.name,
                    )
                )
            if LOCAL_PATH_RE.search(source):
                errors.append(finding("local_path", "Production source contains a local path", source_path.name))
            for value in [
                *[item for _, item in MEDIA_URL_RE.findall(source)],
                *JSON_MEDIA_URL_RE.findall(source),
                *[item for _, item in CSS_URL_RE.findall(source)],
            ]:
                if not value.startswith("https://"):
                    errors.append(
                        finding(
                            "relative_media_url",
                            f"Production media must use a permanent HTTPS URL: {value}",
                            source_path.name,
                        )
                    )

    manifest_sections = manifest.get("sections", []) if manifest else []
    if source and manifest_sections != source_sections:
        errors.append(
            finding(
                "manifest_sections",
                "Manifest section order does not match canonical source",
                manifest_path.name,
            )
        )

    manifest_islands = manifest.get("islands", []) if manifest else []
    if phase in SOURCE_PHASES:
        for island in manifest_islands:
            if not isinstance(island, dict):
                continue
            if (
                not island.get("schemaVersion")
                or island.get("lifecycleStatus") != "active"
            ):
                errors.append(
                    finding(
                        "island_schema_evidence",
                        f"Island {island.get('name', '<unknown>')!r} requires an active schema version",
                        manifest_path.name,
                    )
                )
            if phase in PRODUCTION_PHASES and island.get("mode") not in {
                "native",
                "headless",
            }:
                errors.append(
                    finding(
                        "island_production_mode",
                        f"Island {island.get('name', '<unknown>')!r} requires native or headless mode",
                        manifest_path.name,
                    )
                )
    expected_islands = [
        {"sectionId": item.get("sectionId"), "name": item.get("name")}
        for item in manifest_islands
        if isinstance(item, dict)
    ]
    if source and expected_islands != source_islands:
        errors.append(
            finding(
                "manifest_islands",
                "Manifest island order does not match canonical source",
                manifest_path.name,
            )
        )

    design_state = manifest.get("design", {}) if manifest else {}
    design_status = design_state.get("status")
    skipped = manifest.get("workflow", {}).get("skippedSkills", []) if manifest else []
    if phase in {"design", "visual", "precompile", "draft", "publish"}:
        allowed_statuses = {"approved", "skipped"}
        if design_status not in allowed_statuses:
            errors.append(
                finding(
                    "design_status",
                    "Design status must be approved or explicitly skipped",
                    manifest_path.name,
                )
            )
        if design_status == "skipped" and not {
            "design-page",
            "visual-page",
        }.intersection(skipped):
            errors.append(
                finding(
                    "unrecorded_design_skip",
                    "Record design-page in workflow.skippedSkills",
                    manifest_path.name,
                )
            )
    if phase == "adopted" and design_status not in {"not-used", "skipped", "approved"}:
        errors.append(
            finding(
                "design_status",
                "Adopted pages require not-used, skipped, or approved design status",
                manifest_path.name,
            )
        )
    approved_hash_keys = (
        "sourceHash",
        "themeCssHash",
        "configHash",
        "structureHash",
        "bundleHash",
        "compiledBundleHash",
    )
    if design_status == "not-used" and any(design_state.get(key) for key in approved_hash_keys):
        errors.append(
            finding(
                "design_approval_bypass",
                "An approved design cannot be relabelled not-used",
                manifest_path.name,
            )
        )
    if design_status == "skipped" and (
        any(design_state.get(key) for key in approved_hash_keys)
        or (directory / "compile-artifact.json").is_file()
    ):
        errors.append(
            finding(
                "design_approval_bypass",
                "An approved design cannot be relabelled skipped",
                manifest_path.name,
            )
        )

    current_source_hash = sha256(source) if source else None
    current_theme_hash = sha256(theme_css) if theme_css else None
    current_config_hash = (
        config_hash(page_config, compile_inputs) if page_config else None
    )
    current_structure_hash = structure_hash(source) if source else None
    current_bundle_hash = (
        bundle_hash(source, page_config, theme_css, compile_inputs)
        if source and theme_css and page_config
        else None
    )

    page_preview_path = directory / "page-preview.html"
    compile_artifact_path = directory / "compile-artifact.json"
    if design_status == "approved":
        if not design_state.get("stylePack"):
            errors.append(
                finding("design_style", "Approved design requires a stylePack", manifest_path.name)
            )
        if not isinstance(design_state.get("compiledStyleManifest"), dict):
            errors.append(
                finding(
                    "design_style_manifest",
                    "Approved design requires the compiler style manifest",
                    manifest_path.name,
                )
            )
        for name in ("page-preview.html", "compile-artifact.json"):
            if not (directory / name).is_file():
                errors.append(
                    finding(
                        "missing_design_artifact",
                        f"Approved design file is missing: {name}",
                        name,
                    )
                )
        for key, current, code in (
            ("sourceHash", current_source_hash, "design_source_drift"),
            ("themeCssHash", current_theme_hash, "design_theme_drift"),
            ("configHash", current_config_hash, "design_config_drift"),
            ("structureHash", current_structure_hash, "design_structure_drift"),
            ("bundleHash", current_bundle_hash, "design_bundle_drift"),
        ):
            if not design_state.get(key) or design_state.get(key) != current:
                errors.append(
                    finding(code, f"Current page no longer matches {key}", manifest_path.name)
                )
        hydration_evidence = design_state.get("hydration")
        if not isinstance(hydration_evidence, dict) or hydration_evidence.get("status") != "passed":
            errors.append(
                finding(
                    "design_hydration",
                    "Approved design requires passing island hydration",
                    manifest_path.name,
                )
            )
        expected_hydration_keys = [
            f"{index}:{item['name']}" for index, item in enumerate(source_islands)
        ]
        if (
            not isinstance(hydration_evidence, dict)
            or hydration_evidence.get("bundleHash") != current_bundle_hash
            or hydration_evidence.get("expectedIslands") != expected_hydration_keys
            or hydration_evidence.get("hydratedIslands") != expected_hydration_keys
            or not hydration_evidence.get("checkedAt")
        ):
            errors.append(
                finding(
                    "design_hydration_evidence",
                    "Hydration evidence must cover every expected island instance for the approved bundle",
                    manifest_path.name,
                )
            )
        fallback_islands = [
            item.get("name")
            for item in manifest_islands
            if isinstance(item, dict) and item.get("previewMode") != "hydrated"
        ]
        if fallback_islands:
            errors.append(
                finding(
                    "design_island_fallback",
                    f"Approved design still has non-hydrated islands: {', '.join(filter(None, fallback_islands))}",
                    manifest_path.name,
                )
            )

        if page_preview_path.is_file():
            page_preview = page_preview_path.read_text(encoding="utf-8")
            for code, marker in {
                "preview_marker": "data-lx-visual-preview",
                "preview_css": "https://storefront.trylexsis.com/islands/storefront.css",
                "preview_runtime": "https://storefront.trylexsis.com/islands/islands.js",
                "preview_hydration": "LexsisIslands.hydrateIslands",
                "preview_hydration_state": "data-lx-hydration-status",
                "preview_status_object": "__LEXSIS_PREVIEW_STATUS__",
            }.items():
                if marker not in page_preview:
                    errors.append(
                        finding(code, f"Page preview is missing {marker}", page_preview_path.name)
                    )
            if re.search(r"\{\{[A-Z0-9_]+\}\}", page_preview):
                errors.append(
                    finding(
                        "preview_template_token",
                        "Page preview still contains shell template tokens",
                        page_preview_path.name,
                    )
                )

        if compile_artifact_path.is_file():
            artifact = read_json_file(
                compile_artifact_path, errors, "invalid_compile_artifact"
            )
            if artifact:
                if artifact.get("schemaVersion") != 1:
                    errors.append(
                        finding(
                            "compile_artifact_schema",
                            "Compile artifact must use schemaVersion 1",
                            compile_artifact_path.name,
                        )
                    )
                for key, current in (
                    ("sourceHash", current_source_hash),
                    ("themeCssHash", current_theme_hash),
                    ("configHash", current_config_hash),
                    ("structureHash", current_structure_hash),
                    ("bundleHash", current_bundle_hash),
                ):
                    if artifact.get(key) != current:
                        errors.append(
                            finding(
                                "compile_artifact_drift",
                                f"Compile artifact {key} does not match current input",
                                compile_artifact_path.name,
                            )
                        )
                response = artifact.get("response")
                try:
                    derived_compiled_hash = (
                        compiled_response_hash(response)
                        if isinstance(response, dict)
                        else None
                    )
                except ValueError as exc:
                    derived_compiled_hash = None
                    errors.append(
                        finding(
                            "compile_artifact_evidence",
                            str(exc),
                            compile_artifact_path.name,
                        )
                    )
                compiled_hash = artifact.get("compiledBundleHash")
                if (
                    not compiled_hash
                    or compiled_hash != derived_compiled_hash
                    or compiled_hash != design_state.get("compiledBundleHash")
                ):
                    errors.append(
                        finding(
                            "compile_bundle_drift",
                            "Approved compiled bundle hash does not match compile artifact",
                            compile_artifact_path.name,
                        )
                    )
                if not artifact.get("compiledAt") or not isinstance(response, dict):
                    errors.append(
                        finding(
                            "compile_artifact_evidence",
                            "Compile artifact requires compiledAt and response",
                            compile_artifact_path.name,
                        )
                    )

    manifest_asset_urls: set[str] = set()
    for asset in manifest.get("assets", []) if manifest else []:
        if not isinstance(asset, dict):
            errors.append(
                finding("invalid_asset", "Manifest asset entries must be objects", manifest_path.name)
            )
            continue
        common = (
            "role",
            "sectionId",
            "sourceType",
            "status",
        )
        missing = [field for field in common if not asset.get(field)]
        if missing:
            errors.append(
                finding(
                    "asset_metadata",
                    f"Asset lacks: {', '.join(missing)}",
                    manifest_path.name,
                )
            )
        if asset.get("sourceType") == "lexsis" and not asset.get("assetId"):
            errors.append(finding("asset_identity", "Lexsis assets require assetId", manifest_path.name))
        if asset.get("sourceType") == "shopify" and not all(
            asset.get(key) for key in ("productId", "mediaId")
        ):
            errors.append(
                finding(
                    "asset_identity",
                    "Shopify assets require productId and mediaId",
                    manifest_path.name,
                )
            )
        source_type = asset.get("sourceType")
        if source_type not in {"lexsis", "shopify", "preview-placeholder"}:
            errors.append(finding("asset_source", "Unknown asset source type", manifest_path.name))
        if source_type == "preview-placeholder" and phase in PRODUCTION_PHASES:
            errors.append(
                finding(
                    "preview_asset_in_production",
                    "Replace preview placeholder assets before production",
                    manifest_path.name,
                )
            )
        if asset.get("status") != "verified":
            item = finding(
                "unverified_asset",
                f"Asset role {asset.get('role', '<unknown>')!r} is not verified",
                manifest_path.name,
            )
            if phase in PRODUCTION_PHASES:
                errors.append(item)
            else:
                warnings.append(item)
        url = str(asset.get("url", ""))
        if source_type == "preview-placeholder":
            if not url:
                errors.append(
                    finding(
                        "asset_url",
                        "Preview placeholder lacks a local asset path",
                        manifest_path.name,
                    )
                )
        elif (
            not url
            or not url.startswith("https://")
            or PLACEHOLDER_URL_RE.search(url)
            or LOCAL_PATH_RE.search(f'src="{url}"')
        ):
            errors.append(finding("asset_url", "Asset lacks a permanent URL", manifest_path.name))
        else:
            manifest_asset_urls.add(url)

    if source and phase in PRODUCTION_PHASES:
        for value in [
            *[item for _, item in MEDIA_URL_RE.findall(source)],
            *JSON_MEDIA_URL_RE.findall(source),
            *[item for _, item in CSS_URL_RE.findall(source)],
        ]:
            if value.startswith("https://") and value not in manifest_asset_urls:
                errors.append(
                    finding(
                        "untracked_media",
                        f"Production media is not recorded in the manifest: {value}",
                        source_path.name,
                    )
                )

    if phase == "adopted" and source:
        remote = manifest.get("remote", {})
        sync = manifest.get("sync", {})
        if not remote.get("pageId") or remote.get("lastKnownVersion") is None:
            errors.append(
                finding(
                    "adopted_remote",
                    "Adopted pages require page ID and version",
                    manifest_path.name,
                )
            )
        if sync.get("lastSyncedBundleHash") != current_bundle_hash:
            errors.append(
                finding(
                    "adopted_sync",
                    "Adopted page bundle is not recorded as synchronized",
                    manifest_path.name,
                )
            )

    if phase in REMOTE_READY_PHASES and source:
        remote = manifest.get("remote", {})
        sync = manifest.get("sync", {})
        qa = manifest.get("qa", {})
        label = "Publish" if phase == "publish" else "DRAFT_READY"
        if manifest.get("status") != "qa_passed":
            errors.append(
                finding(
                    "ready_status",
                    f"{label} requires status qa_passed",
                    manifest_path.name,
                )
            )
        if not remote.get("pageId") or remote.get("lastKnownVersion") is None:
            errors.append(
                finding(
                    "ready_remote",
                    f"{label} requires page ID and version",
                    manifest_path.name,
                )
            )
        if sync.get("lastCompiledBundleHash") != current_bundle_hash:
            errors.append(
                finding(
                    "compile_stale",
                    "Local page changed since the last clean compile",
                    manifest_path.name,
                )
            )
        if sync.get("lastSyncedBundleHash") != current_bundle_hash:
            errors.append(
                finding(
                    "source_not_synced",
                    "Local page does not match the synchronized draft",
                    manifest_path.name,
                )
            )
        if sync.get("lastSyncedSectionHashes") != hashes:
            errors.append(
                finding(
                    "sections_not_synced",
                    "Local sections do not match the synchronized draft",
                    manifest_path.name,
                )
            )
        if (
            sync.get("remoteSourceHash") != current_source_hash
            or sync.get("remoteBundleHash") != current_bundle_hash
        ):
            errors.append(
                finding(
                    "fidelity_failed",
                    "Local compile and persisted remote hashes must match",
                    manifest_path.name,
                )
            )
        if not remote_source_hash or not remote_bundle_hash:
            errors.append(
                finding(
                    "remote_evidence_missing",
                    f"{label} requires live remote source and bundle hashes",
                    manifest_path.name,
                )
            )
        elif (
            remote_source_hash != current_source_hash
            or remote_bundle_hash != current_bundle_hash
            or sync.get("remoteSourceHash") != remote_source_hash
            or sync.get("remoteBundleHash") != remote_bundle_hash
        ):
            errors.append(
                finding(
                    "remote_evidence_mismatch",
                    "Live remote hashes differ from the local and manifest baseline",
                    manifest_path.name,
                )
            )
        qa_checks = qa.get("checks", {})
        if qa.get("status") != "passed" or any(
            qa_checks.get(field) is not True for field in QA_FIELDS
        ):
            errors.append(
                finding(
                    "qa_failed",
                    f"All QA checks must pass before {label}",
                    manifest_path.name,
                )
            )
        if qa.get("version") != remote.get("lastKnownVersion"):
            errors.append(
                finding(
                    "qa_version",
                    "QA was not run against the current draft version",
                    manifest_path.name,
                )
            )
        if qa.get("bundleHash") != current_bundle_hash:
            errors.append(
                finding(
                    "qa_bundle",
                    "QA was not run against the current local page",
                    manifest_path.name,
                )
            )

    if current_remote_version is not None and manifest:
        expected_remote_version = manifest.get("remote", {}).get("lastKnownVersion")
        if str(current_remote_version) != str(expected_remote_version):
            errors.append(
                finding(
                    "remote_version_mismatch",
                    f"Remote version {current_remote_version} differs from local baseline {expected_remote_version}",
                    manifest_path.name,
                )
            )

    synced_hashes = (
        manifest.get("sync", {}).get("lastSyncedSectionHashes", {})
        if manifest
        else {}
    )
    changed_sections = [
        section_id
        for section_id in dict.fromkeys([*hashes, *synced_hashes])
        if hashes.get(section_id) != synced_hashes.get(section_id)
    ]

    return {
        "ok": not errors,
        "phase": phase,
        "workingDirectory": str(directory),
        "sourceHash": current_source_hash,
        "themeCssHash": current_theme_hash,
        "configHash": current_config_hash,
        "structureHash": current_structure_hash,
        "bundleHash": current_bundle_hash,
        "sectionHashes": hashes,
        "changedSections": changed_sections,
        "sections": source_sections,
        "islands": source_islands,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("working_directory", type=Path)
    parser.add_argument(
        "--phase",
        choices=["plan", "design", "visual", "precompile", "adopted", "draft", "publish"],
        default="precompile",
    )
    parser.add_argument("--remote-version", help="Current remote page version for drift detection")
    parser.add_argument("--remote-source-hash", help="Source hash fetched live from the remote draft")
    parser.add_argument("--remote-bundle-hash", help="Bundle hash fetched live from the remote draft")
    parser.add_argument("--json", action="store_true", help="Emit compact JSON")
    args = parser.parse_args()
    result = validate_workspace(
        args.working_directory.resolve(),
        args.phase,
        current_remote_version=args.remote_version,
        remote_source_hash=args.remote_source_hash,
        remote_bundle_hash=args.remote_bundle_hash,
    )
    print(json.dumps(result, indent=None if args.json else 2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
