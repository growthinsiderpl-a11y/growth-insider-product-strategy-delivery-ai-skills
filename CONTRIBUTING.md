# Contributing

## Principles

- preserve Growth Insider identity and authorship
- keep product scope separate from marketing and engineering skill families
- prefer deterministic tooling over opaque scoring
- label evidence, assumptions, heuristics, and unknowns explicitly
- avoid mandatory network dependencies in the core package
- require explicit confirmation before any Jira or Atlassian mutation workflow

## Before opening a change

Run:

```text
python scripts/validate_repository.py
python -m pytest tests/ -q
```
