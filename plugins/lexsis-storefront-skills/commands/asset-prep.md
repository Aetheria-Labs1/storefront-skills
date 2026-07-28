---
description: Source and prepare visual assets for a page — searches library, generates images, integrates external MCPs (Exa, HiggsField, OpenArt) for video and reference imagery
allowed-tools: mcp__lexsis-ai__*
---

# /asset-prep

Multi-source asset preparation — built-in generation + external MCPs for video and research.

## Context

- **design-enrichment**: Built-in generate_asset/edit_asset/view_asset pipeline and prompt patterns.
- **asset-pipeline**: Full multi-source strategy including external MCPs, video, import_asset flow.

## Workflow

1. Read `vibe://skills/asset-pipeline` — load the full asset sourcing workflow
2. Execute: decision tree → source per section → verify → produce asset manifest

## Prerequisites

Run `/plan-page` first — the asset pipeline uses the approved plan's section list to determine what images/video are needed per section.
