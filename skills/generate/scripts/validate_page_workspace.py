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
ISLAND_RE = re.compile(r"<lx-island\b([^>]*)>(.*?)</lx-island\s*>", re.IGNORECASE | re.DOTALL)
JSON_SCRIPT_RE = re.compile(
    r"<script\b[^>]*\btype\s*=\s*['\"]application/json['\"][^>]*>(.*?)</script\s*>",
    re.IGNORECASE | re.DOTALL,
)
INLINE_HANDLER_RE = re.compile(r"\son[a-z]+\s*=", re.IGNORECASE)
SCRIPT_SRC_RE = re.compile(r"<script\b[^>]*\bsrc\s*=", re.IGNORECASE)
NON_JSON_SCRIPT_RE = re.compile(
    r"<script\b(?![^>]*\btype\s*=\s*['\"]application/json['\"])[^>]*>",
    re.IGNORECASE | re.DOTALL,
)
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
QA_FIELDS = ("responsive", "commerce", "copy", "claims", "assets", "integrity")


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def canonical_bundle(source: str, page_config: dict[str, Any]) -> str:
    payload = {
        "source": source,
        "head": page_config.get("head", {}),
        "themeCss": page_config.get("themeCss", ""),
        "scripts": page_config.get("scripts", []),
    }
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def bundle_hash(source: str, page_config: dict[str, Any]) -> str:
    return sha256(canonical_bundle(source, page_config))


def section_hashes(source: str) -> dict[str, str]:
    return {match.group(1): sha256(match.group(0)) for match in SECTION_RE.finditer(source)}


def attr_value(attrs: str, name: str) -> str | None:
    match = re.search(rf"\b{re.escape(name)}\s*=\s*(['\"])(.*?)\1", attrs, re.IGNORECASE | re.DOTALL)
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
    for base in (Path.cwd(), directory, *directory.parents):
        candidate = base / path
        if candidate.exists():
            return candidate
    return directory / path


def validate_workspace(
    directory: Path,
    phase: str,
    current_remote_version: int | str | None = None,
) -> dict[str, Any]:
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    required = ["page-plan.md", "page-manifest.json", "qa-report.md"]
    if phase in {"precompile", "adopted", "publish"}:
        required.append("lexsis-source.html")
    for name in required:
        if not (directory / name).is_file():
            errors.append(finding("missing_artifact", f"Missing required file: {name}", name))
    if not (directory / "assets").is_dir():
        errors.append(finding("missing_assets_directory", "Missing assets/ directory", "assets"))

    manifest: dict[str, Any] = {}
    manifest_path = directory / "page-manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(finding("invalid_manifest", f"Invalid page-manifest.json: {exc}", manifest_path.name))

    if manifest:
        if manifest.get("schemaVersion") != 1:
            errors.append(finding("manifest_schema", "Manifest must use schemaVersion 1", manifest_path.name))
        page = manifest.get("page")
        if not isinstance(page, dict) or not all(page.get(key) for key in ("title", "handle", "archetype")):
            errors.append(finding("manifest_page", "Manifest page requires title, handle, and archetype", manifest_path.name))
        for key in (
            "workspaceId",
            "storeId",
            "themeId",
            "setupPath",
            "brandDesignPath",
            "themeCssPath",
        ):
            if not manifest.get(key):
                errors.append(finding("manifest_binding", f"Manifest requires {key}", manifest_path.name))
        if not isinstance(manifest.get("sections"), list) or not isinstance(manifest.get("islands"), list):
            errors.append(finding("manifest_lists", "Manifest sections and islands must be arrays", manifest_path.name))
        source_sync = manifest.get("sourceSync")
        if not isinstance(source_sync, dict) or not isinstance(source_sync.get("lastChangedSections"), list):
            errors.append(finding("manifest_sync", "Manifest sourceSync requires lastChangedSections array", manifest_path.name))

        mcp = manifest.get("mcp")
        if not isinstance(mcp, dict) or mcp.get("status") != "connected":
            errors.append(finding("mcp_status", "Standard page workflows require a successful Lexsis MCP preflight", manifest_path.name))
        elif not mcp.get("checkedAt") or not mcp.get("surfaceVersion"):
            errors.append(finding("mcp_evidence", "Manifest MCP evidence requires checkedAt and surfaceVersion", manifest_path.name))
        else:
            capabilities = mcp.get("capabilities")
            if not isinstance(capabilities, list) or not capabilities:
                errors.append(finding("mcp_capabilities", "Manifest MCP evidence requires discovered capabilities", manifest_path.name))
            elif any(
                not isinstance(item, dict)
                or not item.get("router")
                or not isinstance(item.get("actions"), list)
                or not item.get("actions")
                for item in capabilities
            ):
                errors.append(finding("mcp_capabilities", "Every MCP capability requires a router and actions", manifest_path.name))

        template = manifest.get("template")
        if not isinstance(template, dict) or template.get("mode") not in {"page-kit", "sections", "custom"}:
            errors.append(finding("template_mode", "Manifest template mode must be page-kit, sections, or custom", manifest_path.name))
        else:
            if not isinstance(template.get("evaluatedTemplates"), list):
                errors.append(finding("template_evidence", "Template selection requires evaluatedTemplates", manifest_path.name))
            if not template.get("selectionReason") or not template.get("selectedAt"):
                errors.append(finding("template_evidence", "Template selection requires selectionReason and selectedAt", manifest_path.name))
            if template.get("mode") == "page-kit" and not template.get("pageKitId"):
                errors.append(finding("template_page_kit", "Page-kit mode requires pageKitId", manifest_path.name))
            if template.get("mode") in {"page-kit", "sections"}:
                section_template_ids = template.get("sectionTemplateIds")
                if not isinstance(section_template_ids, list) or not section_template_ids:
                    errors.append(finding("template_sections", "Selected templates require sectionTemplateIds", manifest_path.name))

        design = manifest.get("design")
        if not isinstance(design, dict):
            errors.append(finding("design_evidence", "Manifest requires a design record", manifest_path.name))
        else:
            if design.get("themeId") != manifest.get("themeId"):
                errors.append(finding("design_theme", "Design themeId must match the page themeId", manifest_path.name))
            if not design.get("themeSource"):
                errors.append(finding("design_source", "Design record requires themeSource", manifest_path.name))
            if phase in {"visual", "precompile", "adopted", "publish"} and not design.get("stylePack"):
                errors.append(finding("design_style", "Visual and production phases require one coherent stylePack", manifest_path.name))
            if phase == "publish" and not isinstance(design.get("compiledStyleManifest"), dict):
                errors.append(finding("design_compile", "Publish requires the compiler style manifest", manifest_path.name))

        setup_path = resolve_workspace_path(directory, manifest.get("setupPath", ""))
        if not setup_path.is_file():
            errors.append(finding("setup_missing", "Saved setup file does not exist", str(setup_path)))
        else:
            try:
                setup = json.loads(setup_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(finding("setup_invalid", f"Saved setup file is invalid: {exc}", str(setup_path)))
                setup = {}
            if setup:
                if setup.get("workspaceId") != manifest.get("workspaceId"):
                    errors.append(finding("setup_workspace", "Manifest workspace does not match saved setup", manifest_path.name))
                stores = setup.get("stores", [])
                selected_store = next(
                    (
                        item
                        for item in stores
                        if isinstance(item, dict)
                        and item.get("storeId") == manifest.get("storeId")
                    ),
                    None,
                )
                if not selected_store:
                    errors.append(finding("setup_store", "Manifest store is not present in saved setup", manifest_path.name))
                else:
                    themes = selected_store.get("themes", [])
                    if not any(
                        isinstance(item, dict)
                        and item.get("themeId") == manifest.get("themeId")
                        for item in themes
                    ):
                        errors.append(finding("setup_theme", "Manifest theme is not saved for the selected store", manifest_path.name))

        for key, code in (
            ("brandDesignPath", "brand_design_missing"),
            ("themeCssPath", "theme_css_missing"),
        ):
            resolved = resolve_workspace_path(directory, manifest.get(key, ""))
            if not resolved.is_file():
                errors.append(finding(code, f"Manifest {key} does not exist", str(resolved)))

    visual_state = manifest.get("visual", {}) if manifest else {}
    visual_status = visual_state.get("status")
    skipped = manifest.get("workflow", {}).get("skippedSkills", []) if manifest else []
    if phase in {"visual", "precompile", "publish"}:
        if visual_status not in {"approved", "skipped", "not-used"}:
            errors.append(finding("visual_status", "Visual status must be approved, skipped, or not-used", manifest_path.name))
        if visual_status == "approved":
            for name in ("visual-source.html", "visual-preview.html"):
                if not (directory / name).is_file():
                    errors.append(finding("missing_visual_artifact", f"Approved visual file is missing: {name}", name))
        if visual_status == "skipped" and "visual-page" not in skipped:
            errors.append(finding("unrecorded_visual_skip", "Record visual-page in workflow.skippedSkills", manifest_path.name))

    visual_source_path = directory / "visual-source.html"
    visual_source = (
        visual_source_path.read_text(encoding="utf-8")
        if visual_source_path.is_file()
        else ""
    )
    visual_sections: list[str] = []
    visual_islands: list[dict[str, str]] = []
    if visual_source:
        visual_matches = list(SECTION_RE.finditer(visual_source))
        visual_sections = [match.group(1) for match in visual_matches]
        if not visual_matches:
            errors.append(finding("visual_missing_sections", "Visual source has no section delimiters", visual_source_path.name))
        elif visual_source[: visual_matches[0].start()].strip():
            errors.append(finding("visual_content_before_section", "Visual source contains content before the first section", visual_source_path.name))
        if len(visual_sections) != len(set(visual_sections)):
            errors.append(finding("visual_duplicate_section", "Visual source has duplicate section delimiters", visual_source_path.name))
        visual_ids = ID_RE.findall(visual_source)
        if len(visual_ids) != len(set(visual_ids)):
            errors.append(finding("visual_duplicate_html_id", "Visual source has duplicate HTML IDs", visual_source_path.name))
        for match in visual_matches:
            section_id, body = match.group(1), match.group(2)
            section_tag = SECTION_ID_RE.search(body)
            if not section_tag or section_tag.group(1) != section_id:
                errors.append(finding("visual_section_id", f"Visual section {section_id!r} needs a matching <section id>", visual_source_path.name))
            for island in ISLAND_RE.finditer(body):
                attrs, island_body = island.group(1), island.group(2)
                name = attr_value(attrs, "name")
                if not name:
                    errors.append(finding("visual_island_name", f"Island in section {section_id!r} has no name", visual_source_path.name))
                    continue
                visual_islands.append({"sectionId": section_id, "name": name})
                payload = JSON_SCRIPT_RE.search(island_body)
                if not payload:
                    errors.append(finding("visual_island_json", f"Preview island {name!r} has no application/json script", visual_source_path.name))
                else:
                    try:
                        json.loads(payload.group(1))
                    except json.JSONDecodeError as exc:
                        errors.append(finding("visual_island_json", f"Preview island {name!r} has invalid JSON: {exc}", visual_source_path.name))
        if re.search(r"\bdata-island\s*=", visual_source, re.IGNORECASE):
            errors.append(finding("compiled_visual_island", "Visual source must use <lx-island>, not compiled data-island markup", visual_source_path.name))
        if INLINE_HANDLER_RE.search(visual_source):
            errors.append(finding("visual_inline_handler", "Visual source contains an inline event handler", visual_source_path.name))
        if SCRIPT_SRC_RE.search(visual_source) or NON_JSON_SCRIPT_RE.search(visual_source):
            errors.append(finding("visual_script", "Visual source may only contain island application/json scripts", visual_source_path.name))

    visual_preview_path = directory / "visual-preview.html"
    visual_preview = (
        visual_preview_path.read_text(encoding="utf-8")
        if visual_preview_path.is_file()
        else ""
    )
    if visual_status == "approved" and visual_preview:
        preview_requirements = {
            "preview_marker": "data-lx-visual-preview",
            "preview_css": "https://storefront.trylexsis.com/islands/storefront.css",
            "preview_runtime": "https://storefront.trylexsis.com/islands/islands.js",
            "preview_hydration": "LexsisIslands.hydrateIslands",
        }
        for code, marker in preview_requirements.items():
            if marker not in visual_preview:
                errors.append(finding(code, f"Visual preview is missing {marker}", visual_preview_path.name))
        if re.search(r"\{\{[A-Z0-9_]+\}\}", visual_preview):
            errors.append(finding("preview_template_token", "Visual preview still contains shell template tokens", visual_preview_path.name))

    source_path = directory / "lexsis-source.html"
    source = source_path.read_text(encoding="utf-8") if source_path.is_file() else ""
    source_sections: list[str] = []
    source_islands: list[dict[str, str]] = []
    hashes: dict[str, str] = {}
    if phase in {"precompile", "adopted", "publish"} and not source.strip():
        errors.append(finding("empty_source", "Production source cannot be empty", source_path.name))
    if source:
        matches = list(SECTION_RE.finditer(source))
        source_sections = [match.group(1) for match in matches]
        hashes = section_hashes(source)
        if not matches:
            errors.append(finding("missing_sections", "Production source has no section delimiters", source_path.name))
        elif source[: matches[0].start()].strip():
            errors.append(finding("content_before_section", "Production source contains content before the first section", source_path.name))
        if len(source_sections) != len(set(source_sections)):
            errors.append(finding("duplicate_section", "Production source has duplicate section delimiters", source_path.name))
        all_ids = ID_RE.findall(source)
        if len(all_ids) != len(set(all_ids)):
            errors.append(finding("duplicate_html_id", "Production source has duplicate HTML IDs", source_path.name))
        for match in matches:
            section_id, body = match.group(1), match.group(2)
            section_tag = SECTION_ID_RE.search(body)
            if not section_tag:
                errors.append(finding("missing_section_id", f"Section {section_id!r} has no matching <section id>", source_path.name))
            elif section_tag.group(1) != section_id:
                errors.append(finding("section_id_mismatch", f"Delimiter {section_id!r} does not match section id {section_tag.group(1)!r}", source_path.name))
            for island in ISLAND_RE.finditer(body):
                attrs, island_body = island.group(1), island.group(2)
                name = attr_value(attrs, "name")
                if not name:
                    errors.append(finding("island_missing_name", f"Island in section {section_id!r} has no name", source_path.name))
                    continue
                source_islands.append({"sectionId": section_id, "name": name})
                payload = JSON_SCRIPT_RE.search(island_body)
                if not payload:
                    errors.append(finding("island_missing_json", f"Island {name!r} has no application/json script", source_path.name))
                else:
                    try:
                        json.loads(payload.group(1))
                    except json.JSONDecodeError as exc:
                        errors.append(finding("invalid_island_json", f"Island {name!r} has invalid JSON: {exc}", source_path.name))
        if PREVIEW_PLACEHOLDER_RE.search(source):
            errors.append(finding("placeholder_in_source", "Production source still contains a visual placeholder", source_path.name))
        if INLINE_HANDLER_RE.search(source):
            errors.append(finding("inline_handler", "Production source contains an inline event handler", source_path.name))
        if SCRIPT_SRC_RE.search(source):
            errors.append(finding("script_src", "External scripts belong in pageConfig.scripts", source_path.name))
        if NON_JSON_SCRIPT_RE.search(source):
            errors.append(finding("unsupported_script", "Production source may only contain island application/json scripts", source_path.name))
        if UNSUPPORTED_JS_RE.search(source):
            errors.append(finding("unsupported_script", "Production source contains unsupported JavaScript", source_path.name))
        if LOCAL_PATH_RE.search(source):
            errors.append(finding("local_path", "Production source contains a local path", source_path.name))
        if PLACEHOLDER_URL_RE.search(source):
            errors.append(finding("placeholder_url", "Production source contains a placeholder or development URL", source_path.name))
        if PLACEHOLDER_TOKEN_RE.search(source):
            errors.append(finding("placeholder_token", "Production source contains an unresolved placeholder token", source_path.name))
        production_media = [
            *[value for _, value in MEDIA_URL_RE.findall(source)],
            *JSON_MEDIA_URL_RE.findall(source),
            *[value for _, value in CSS_URL_RE.findall(source)],
        ]
        for value in production_media:
            if not value.startswith("https://"):
                errors.append(finding("relative_media_url", f"Production media must use a permanent HTTPS URL: {value}", source_path.name))
        semantic = re.sub(r"<!--.*?-->|<style\b.*?</style\s*>|<script\b.*?</script\s*>", "", source, flags=re.IGNORECASE | re.DOTALL)
        if (
            len(matches) <= 1
            and len(re.findall(r"<img\b", semantic, re.IGNORECASE)) == 1
            and not re.search(r"<(?:h1|h2|p|button|form|details|lx-island)\b", semantic, re.IGNORECASE)
        ):
            errors.append(finding("complete_page_image", "One image cannot be used as the complete page layout", source_path.name))
        customer_copy = visible_text(source).casefold()
        for phrase in BANNED_COPY:
            if phrase in customer_copy:
                errors.append(finding("internal_copy", f"Customer copy contains internal wording: {phrase}", source_path.name))
        for comment in re.findall(r"<!--(.*?)-->", source, re.DOTALL):
            if not re.fullmatch(r"\s*section:\s*[a-z0-9]+(?:-[a-z0-9]+)*\s*", comment, re.IGNORECASE):
                errors.append(finding("production_comment", "Production comments may only be section delimiters", source_path.name))

    manifest_sections = manifest.get("sections", []) if manifest else []
    if source and manifest_sections != source_sections:
        errors.append(finding("manifest_sections", "Manifest section order does not match production source", manifest_path.name))

    manifest_islands = manifest.get("islands", []) if manifest else []
    if phase in {"visual", "precompile", "adopted", "publish"}:
        for island in manifest_islands:
            if not isinstance(island, dict):
                continue
            schema = island.get("schema")
            if (
                not isinstance(schema, dict)
                or not schema.get("version")
                or schema.get("lifecycleStatus") != "active"
                or not schema.get("resolvedAt")
            ):
                errors.append(
                    finding(
                        "island_schema_evidence",
                        f"Island {island.get('name', '<unknown>')!r} requires an active resolved schema",
                        manifest_path.name,
                    )
                )
            if (
                phase in {"precompile", "adopted", "publish"}
                and island.get("productionMode") not in {"native", "headless"}
            ):
                errors.append(
                    finding(
                        "island_production_mode",
                        f"Island {island.get('name', '<unknown>')!r} requires native or headless productionMode",
                        manifest_path.name,
                    )
                )
    expected_islands = [
        {"sectionId": item.get("sectionId"), "name": item.get("name")}
        for item in manifest_islands
        if isinstance(item, dict)
    ]
    if visual_source and manifest_sections != visual_sections:
        errors.append(finding("visual_manifest_sections", "Manifest section order does not match visual source", manifest_path.name))
    if visual_source and expected_islands != visual_islands:
        errors.append(finding("visual_manifest_islands", "Manifest island order does not match visual source", manifest_path.name))
    if source and expected_islands != source_islands:
        errors.append(finding("manifest_islands", "Manifest island order does not match production source", manifest_path.name))

    manifest_asset_urls: set[str] = set()
    for asset in manifest.get("assets", []) if manifest else []:
        if not isinstance(asset, dict):
            errors.append(finding("invalid_asset", "Manifest asset entries must be objects", manifest_path.name))
            continue
        common = ("role", "sectionId", "url", "width", "height", "desktopCrop", "mobileCrop", "altTextIntent", "sourceType", "verificationStatus")
        missing = [field for field in common if not asset.get(field)]
        if missing:
            errors.append(finding("asset_metadata", f"Asset lacks: {', '.join(missing)}", manifest_path.name))
        if asset.get("sourceType") == "lexsis" and not asset.get("assetId"):
            errors.append(finding("asset_identity", "Lexsis assets require assetId", manifest_path.name))
        if asset.get("sourceType") == "shopify" and not all(asset.get(key) for key in ("productId", "mediaId")):
            errors.append(finding("asset_identity", "Shopify assets require productId and mediaId", manifest_path.name))
        source_type = asset.get("sourceType")
        if source_type not in {"lexsis", "shopify", "preview-placeholder"}:
            errors.append(finding("asset_source", "Unknown asset source type", manifest_path.name))
        if source_type == "preview-placeholder" and phase in {"precompile", "adopted", "publish"}:
            errors.append(finding("preview_asset_in_production", "Replace preview placeholder assets before production", manifest_path.name))
        if asset.get("verificationStatus") != "verified":
            item = finding("unverified_asset", f"Asset role {asset.get('role', '<unknown>')!r} is not verified", manifest_path.name)
            if phase in {"precompile", "adopted", "publish"}:
                errors.append(item)
            else:
                warnings.append(item)
        url = str(asset.get("url", ""))
        if source_type == "preview-placeholder":
            if not url:
                errors.append(finding("asset_url", "Preview placeholder lacks a local asset path", manifest_path.name))
        elif (
            not url
            or not url.startswith("https://")
            or PLACEHOLDER_URL_RE.search(url)
            or LOCAL_PATH_RE.search(f'src="{url}"')
        ):
            errors.append(finding("asset_url", "Asset lacks a permanent URL", manifest_path.name))
        else:
            manifest_asset_urls.add(url)

    if source:
        production_media = [
            *[value for _, value in MEDIA_URL_RE.findall(source)],
            *JSON_MEDIA_URL_RE.findall(source),
            *[value for _, value in CSS_URL_RE.findall(source)],
        ]
        for value in production_media:
            if value.startswith("https://") and value not in manifest_asset_urls:
                errors.append(finding("untracked_media", f"Production media is not recorded in the manifest: {value}", source_path.name))

    page_config = manifest.get("pageConfig", {}) if manifest else {}
    current_bundle_hash: str | None = None
    if phase in {"precompile", "adopted", "publish"}:
        if not isinstance(page_config, dict):
            errors.append(finding("page_config", "Manifest requires pageConfig", manifest_path.name))
            page_config = {}
        if not isinstance(page_config.get("head"), dict):
            errors.append(finding("page_head", "pageConfig.head must be an object", manifest_path.name))
        if not isinstance(page_config.get("themeCss"), str) or not page_config.get("themeCss", "").strip():
            errors.append(finding("page_theme", "pageConfig.themeCss must contain the selected theme CSS", manifest_path.name))
        if not isinstance(page_config.get("scripts"), list):
            errors.append(finding("page_scripts", "pageConfig.scripts must be an array", manifest_path.name))
        if source:
            current_bundle_hash = bundle_hash(source, page_config)

    if phase == "adopted" and source:
        remote = manifest.get("remote", {})
        sync = manifest.get("sourceSync", {})
        if not remote.get("pageId") or remote.get("lastKnownVersion") is None:
            errors.append(finding("adopted_remote", "Adopted pages require page ID and version", manifest_path.name))
        if sync.get("lastSyncedBundleHash") != current_bundle_hash:
            errors.append(finding("adopted_sync", "Adopted page bundle is not recorded as synchronized", manifest_path.name))

    if phase == "publish" and source:
        remote = manifest.get("remote", {})
        sync = manifest.get("sourceSync", {})
        qa = manifest.get("qa", {})
        if manifest.get("status") != "qa_passed":
            errors.append(finding("publish_status", "Publish requires status qa_passed", manifest_path.name))
        if not remote.get("pageId") or remote.get("lastKnownVersion") is None:
            errors.append(finding("publish_remote", "Publish requires page ID and version", manifest_path.name))
        if sync.get("lastCompiledBundleHash") != current_bundle_hash:
            errors.append(finding("compile_stale", "Local page changed since the last clean compile", manifest_path.name))
        if sync.get("lastSyncedBundleHash") != current_bundle_hash:
            errors.append(finding("source_not_synced", "Local page does not match the synchronized draft", manifest_path.name))
        if sync.get("lastSyncedSectionHashes") != hashes:
            errors.append(finding("sections_not_synced", "Local sections do not match the synchronized draft", manifest_path.name))
        if qa.get("status") != "passed" or any(qa.get(field) is not True for field in QA_FIELDS):
            errors.append(finding("qa_failed", "All QA checks must pass before publication", manifest_path.name))
        if qa.get("checkedVersion") != remote.get("lastKnownVersion"):
            errors.append(finding("qa_version", "QA was not run against the current draft version", manifest_path.name))
        if qa.get("checkedBundleHash") != current_bundle_hash:
            errors.append(finding("qa_bundle", "QA was not run against the current local page", manifest_path.name))

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
        manifest.get("sourceSync", {}).get("lastSyncedSectionHashes", {})
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
    parser.add_argument("--phase", choices=["plan", "visual", "precompile", "adopted", "publish"], default="precompile")
    parser.add_argument("--remote-version", help="Current remote page version for drift detection")
    parser.add_argument("--json", action="store_true", help="Emit compact JSON")
    args = parser.parse_args()
    result = validate_workspace(
        args.working_directory.resolve(),
        args.phase,
        current_remote_version=args.remote_version,
    )
    print(json.dumps(result, indent=None if args.json else 2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
