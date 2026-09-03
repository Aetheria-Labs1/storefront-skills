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
Public skills may use these resources because the Lexsis pack is installed as
one unit.

Command-specific validators and preview builders live under the owning skill's
`scripts/` directory.

Do not invent island names or props. Update the generated schema contract or
read the current Lexsis schema before changing examples.

## Generated Files

Do not edit `gpt/instructions.md` or `gpt/knowledge.md` directly.

After changing a skill or shared reference, run:

```bash
python3 scripts/build-distributions.py
```

## Validation

Before opening a pull request:

```bash
python3 scripts/build-distributions.py --check
python3 scripts/validate-island-contracts.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

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
