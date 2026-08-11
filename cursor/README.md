# Cursor

Nothing to install here. Cursor reads the [Agent Skills](https://agentskills.io)
standard natively from `.agents/skills/`, which this repo provides at the root —
clone the repo (or `npx skills add Aetheria-Labs1/storefront-skills`) and the
skills appear automatically.

If you previously copied `cursor/rules/lexsis-storefront.mdc`, delete it — that
file was hand-maintained, went stale, and has been removed in v5.0.0. Cursor's
`/migrate-to-skills` command converts old rules if needed.
