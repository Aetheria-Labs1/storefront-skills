"""Fail when a live MCP action is documented in no skill (monorepo checkouts only)."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONSOLIDATED = ROOT.parent / "services/storefront-blueprint-mcp/src/tools/consolidated.ts"
# Actions that are deliberately not part of any skill workflow.
INTENTIONALLY_UNDOCUMENTED: set[str] = set()


class McpActionCoverageTests(unittest.TestCase):
    @unittest.skipUnless(CONSOLIDATED.exists(), "MCP source not available")
    def test_every_action_appears_in_a_skill(self) -> None:
        actions = set(re.findall(r'operation\("([a-z_]+)"', CONSOLIDATED.read_text()))
        corpus = "\n".join(p.read_text() for p in (ROOT / "skills").rglob("*.md"))
        missing = {a for a in actions if not re.search(rf"\b{a}\b", corpus)}
        self.assertEqual(missing - INTENTIONALLY_UNDOCUMENTED, set())


if __name__ == "__main__":
    unittest.main()
