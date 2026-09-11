# Contributing to Lexsis Storefront Skills

The canonical source is `skills/`. Claude, Codex, Cursor, and GPT
distributions are derived from that tree.

## Public Commands

Each public command lives at:

```text
skills/<command>/
├── SKILL.md
├── agents/openai.yaml
├── references/        optional
├── scripts/           optional
└── assets/            optional
```

`SKILL.md` uses Agent Skills frontmatter:

```yaml
---
name: command-name
description: Clear description of what the command owns and when to use it.
---
```

Keep entrypoints concise. Put conditional procedures in `references/`,
deterministic repeated work in `scripts/`, and reusable output files in
`assets/`.

## Shared Storefront Resources

Shared references and island contracts live in:

```text
skills/storefront-engine/
└── references/
    └── islands/
```

`storefront-engine` is a resource directory, not a public slash command.
`scripts/build-distributions.py` copies the shared documents consumed by each
public skill into that skill's local `references/` directory. This keeps
Skills CLI and per-skill Codex installations self-contained. Edit the shared
source and regenerate; do not hand-edit those copied files.

Command-specific validators and preview builders live under the owning skill's
`scripts/` directory.

Do not invent island names or props. Update the generated schema contract or
read the current Lexsis schema before changing examples.

## Generated Files

Do not edit `gpt/instructions.md` or `gpt/knowledge.md` directly. The Claude
plugin consumes canonical `skills/` from the repository root; do not create a
second materialized skill tree under `plugins/`.

After changing a skill or shared reference, run:

```bash
python3 scripts/build-distributions.py
```

## Validation

Before opening a pull request:

```bash
python3 scripts/build-distributions.py --check
python3 scripts/validate-island-contracts.py
python3 scripts/validate-page-types.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

Page-type files under `skills/storefront-engine/references/page-types/`
follow `_checklist-format.md`: fixed headings plus one JSON checklist block
that `plan-page/scripts/plan_lint.py` enforces. Add a section id, proof kind
or image job to the vocabulary in `_checklist-format.md` before using it.
Shared reference sub-directories (`page-types/`, `proof/`, `offers/`,
`assets/`, `anti-patterns/`, `copy/`, `mcp-playbooks/`) are declared as
directory entries in `SKILL_SHARED_REFERENCES` and copied whole.

Also run the skill validator for each new or substantially changed command:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/<command>
```

## Pull Requests

- Keep one concern per commit.
- Use conventional commits such as `feat:`, `fix:`, or `docs:`.
- Preserve explicit approval boundaries for paid generation, remote writes,
  experiments, and publishing.
- Distinguish verified behavior from expected behavior.
- Include generated distribution changes.

CI validates JSON, skill frontmatter, island contracts, generated-file drift,
public command inventory, visual-preview assets, and page workspace rules.
