from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_repository import find_semantic_fragments  # type: ignore


def test_find_semantic_fragments_detects_known_truncations():
    corrupted = """# Example Hub

## Core Questions

- What revenue, retention, or strategic risk appears if
  the team
- Expose what must be true about value, usability, viability, and
- A bet that only wins when three optimistic assumptions
  are
- Do not label work strategic if the only argument is that
- and
"""
    findings = find_semantic_fragments(corrupted)
    joined = " | ".join(findings).lower()
    assert findings, "expected corruption detector to report fragments"
    assert "appears if the team" in joined or "the team" in joined
    assert joined.rstrip().endswith(" and") or ", and" in joined or " viability, and" in joined
    assert "assumptions are" in joined or joined.endswith(" are") or " are" in joined
    assert any(item == "and" or item.lower().endswith(" is that") for item in findings)


def test_find_semantic_fragments_allows_complete_prose():
    clean = """# Example Hub

## Decision Rules

- What revenue, retention, or strategic risk appears if the team does nothing?
- Name the constrained resource, such as engineering capacity, market attention, or design bandwidth.
- A bet that only wins when several optimistic assumptions all hold should be treated as an explore bet.
- Do not label work strategic if the only argument is that leadership cares about it.
- Prepare a short legend for unknowns and assumptions.
"""
    assert find_semantic_fragments(clean) == []
