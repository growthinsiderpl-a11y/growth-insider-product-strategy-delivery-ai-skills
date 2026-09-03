from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))


def test_identity() -> None:
    assert MANIFEST['package']['id'] == 'growth-insider-product-strategy-delivery-ai-skills'
    assert MANIFEST['package']['title'] == 'Growth Insider Product Strategy & Delivery AI Skills'
    assert MANIFEST['package']['version'] == '1.0.0-rc.1'


def test_hub_and_playbook_counts() -> None:
    assert len(MANIFEST['hubs']) == 13
    assert len(MANIFEST['playbooks']) >= 18


def test_hubs_and_playbooks_have_depth_and_unique_bodies() -> None:
    hub_paths = sorted((ROOT / 'references' / 'hubs').glob('*.md'))
    playbook_paths = sorted((ROOT / 'references' / 'playbooks').glob('*.md'))

    for path in hub_paths:
        assert len(path.read_text(encoding='utf-8').splitlines()) >= 120

    hashes = []
    for path in playbook_paths:
        lines = path.read_text(encoding='utf-8').splitlines()
        assert len(lines) >= 100
        hashes.append(sha256('\n'.join(lines[1:]).strip().encode('utf-8')).hexdigest())

    assert len(hashes) == len(set(hashes))


def test_product_scope() -> None:
    text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    assert 'marketing skill' in text
    assert 'engineering skill' in text
    assert 'Jira and Atlassian mutations require explicit confirmation' in text


def test_examples_and_tests_registered() -> None:
    for path in MANIFEST['examples'] + MANIFEST['tests']:
        assert (ROOT / path).exists()
