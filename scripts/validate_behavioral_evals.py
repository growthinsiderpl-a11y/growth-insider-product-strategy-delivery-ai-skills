#!/usr/bin/env python3
"""Validate behavioral evaluation case files."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE_FILES = [ROOT / 'tests' / 'domain-behavior-cases.json', ROOT / 'tests' / 'routing-safety-cases.json']


def main() -> int:
    errors: list[str] = []
    for path in CASE_FILES:
        payload = json.loads(path.read_text(encoding='utf-8'))
        if payload.get('schema_version') != '1.0.0':
            errors.append(f'{path.name}: schema_version must be 1.0.0')
        cases = payload.get('cases')
        if not isinstance(cases, list) or not cases:
            errors.append(f'{path.name}: cases must be a non-empty list')
            continue
        for index, case in enumerate(cases):
            if not isinstance(case.get('id'), str) or not case['id'].strip():
                errors.append(f'{path.name}: case {index} missing id')
            if not isinstance(case.get('request'), str) or not case['request'].strip():
                errors.append(f'{path.name}: case {index} missing request')
            behavior = case.get('expected_behavior')
            if not isinstance(behavior, list) or not behavior or not all(isinstance(item, str) and item.strip() for item in behavior):
                errors.append(f'{path.name}: case {index} expected_behavior invalid')
    print(json.dumps({'status': 'PASS' if not errors else 'FAIL', 'errors': errors}, indent=2))
    return 0 if not errors else 1


if __name__ == '__main__':
    raise SystemExit(main())
