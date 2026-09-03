#!/usr/bin/env python3
"""Validate the Growth Insider Product Strategy and Delivery AI Skills repository."""

from __future__ import annotations

import json
import re
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ID = 'growth-insider-product-strategy-delivery-ai-skills'
EXPECTED_TITLE = 'Growth Insider Product Strategy & Delivery AI Skills'
EXPECTED_VERSION = '1.0.0-rc.1'
FORBIDDEN_STRINGS = ['Alireza Rezvani', 'wondelai', 'cs-chief-of-staff', 'Act as a CPO', 'Act as a Head of Product', 'Act as a PM']
FORBIDDEN_FILLER_PHRASES = [
    'Treat these as product-owned decisions or product-owned artifacts unless a boundary section explicitly routes the work away.',
    'If this becomes the center of gravity, hand the work to the matching skill family rather than stretching the product scope.',
    'Keep the question visible while working so the artifact remains decision-oriented instead of becoming generic analysis.',
]
REQUIRED_HUBS = ['product-strategy-and-portfolio-decisions.md', 'product-discovery-and-opportunity-validation.md', 'product-market-fit-and-customer-evidence.md', 'product-analytics-metrics-and-learning.md', 'prioritization-roadmapping-and-tradeoffs.md', 'requirements-prds-and-user-stories.md', 'agile-delivery-and-release-planning.md', 'ux-research-and-customer-journeys.md', 'product-design-and-interface-quality.md', 'monetization-pricing-and-retention.md', 'stakeholder-board-and-product-communication.md', 'product-operations-project-and-portfolio-governance.md', 'product-to-engineering-translation.md']
REQUIRED_PLAYBOOKS = ['opportunity-assessment.md', 'discovery-interview-plan.md', 'assumption-mapping.md', 'pmf-evidence-rubric.md', 'product-experiment-design.md', 'prioritization-comparison.md', 'roadmap-consistency-check.md', 'prd-quality-review.md', 'user-story-validation.md', 'acceptance-criteria-validation.md', 'sprint-planning-tradeoffs.md', 'release-decision-gate.md', 'journey-mapping-workshop.md', 'retention-diagnosis.md', 'packaging-and-monetization-design.md', 'board-update-narrative.md', 'okr-cascade-validation.md', 'atlassian-jira-mutation-confirmation.md', 'engineering-handoff-packet.md']
REQUIRED_TOOLS = ['scripts/analytics/calculate_experiment_sample_size.py', 'scripts/analytics/calculate_product_metrics.py', 'scripts/analytics/calculate_retention_cohorts.py', 'scripts/discovery/evaluate_evidence_rubric.py', 'scripts/discovery/compare_prioritization_options.py', 'scripts/requirements/validate_user_story.py', 'scripts/requirements/validate_acceptance_criteria.py', 'scripts/delivery/validate_roadmap_consistency.py', 'scripts/delivery/validate_okr_cascade.py', 'scripts/_shared/tool_runtime.py', 'scripts/validate_repository.py', 'scripts/validate_behavioral_evals.py']
REQUIRED_COMMUNITY = ['SUPPORT.md', 'SECURITY.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'CHANGELOG.md', 'CITATION.cff']
MIN_HUB_LINES = 120
MIN_PLAYBOOK_LINES = 100
MIN_HUB_LINE_VARIETY = 3
MIN_PLAYBOOK_LINE_VARIETY = 6
# Highly diagnostic dangling function-word endings.
# Exclude stranded prepositions/pronouns that often end complete English clauses.
WEAK_END = re.compile(
    r'(?i)\b(the|a|an|if|when|while|and|or|but|to|of|with|from|into|'
    r'that|which|who|as|is|are|was|were|be|been|being|'
    r'can|could|should|would|will|must|may|might|whether|because|'
    r'although|unless|until|than)\s*$'
)
ORPHAN_WORD = re.compile(
    r'(?i)^(and|or|but|the|a|an|to|of|in|on|at|by|with|from|are|is|was|were|be|this|that)$'
)
INCOMPLETE_TAIL = re.compile(
    r'(?i)\b(if|when|while|unless|until|because|although|that|which|who)\s+(the|a|an)\s+\w+$'
)


class Results:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def content_units(text: str) -> list[str]:
    """Join soft-wrap continuations into semantic units.

    Supports both indented Markdown continuations and broken hard wraps where
    the previous line has no terminal punctuation and the next line continues
    the clause without a new list marker or heading.
    """
    units: list[str] = []
    buf: str | None = None
    for ln in text.splitlines():
        raw = ln.rstrip()
        if not raw.strip():
            if buf is not None:
                units.append(buf)
                buf = None
            continue
        stripped = raw.lstrip()
        if stripped.startswith('#') or stripped.startswith('```') or stripped.startswith('|'):
            if buf is not None:
                units.append(buf)
                buf = None
            continue
        starts_item = bool(re.match(r'^\s*([-*]|\d+\.)\s+', raw))
        indented_continuation = bool(re.match(r'^\s{2,}\S', raw)) and not starts_item
        hard_wrap_continuation = (
            buf is not None
            and not starts_item
            and buf.rstrip()[-1:] not in '.!?:;)}"\']'
            and not stripped.startswith('#')
        )
        if buf is not None and (indented_continuation or hard_wrap_continuation):
            buf = f'{buf.rstrip()} {stripped}'
            continue
        if buf is not None:
            units.append(buf)
        buf = raw
    if buf is not None:
        units.append(buf)
    return units


def find_semantic_fragments(text: str) -> list[str]:
    """Heuristic first-line defense for truncated hub/playbook prose."""
    findings: list[str] = []
    for unit in content_units(text):
        body = re.sub(r'^(\s*[-*]|\s*\d+\.)\s+', '', unit).strip()
        if not body:
            continue
        if ORPHAN_WORD.fullmatch(body):
            findings.append(body)
            continue
        if body[-1] in '.!?:;)}"\']':
            continue
        if WEAK_END.search(body) and len(body.split()) >= 3:
            findings.append(body)
            continue
        if INCOMPLETE_TAIL.search(body):
            findings.append(body)
    return findings

def main() -> int:
    results = Results()
    manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
    package = manifest['package']
    results.require(package['id'] == EXPECTED_ID, 'package id mismatch')
    results.require(package['title'] == EXPECTED_TITLE, 'package title mismatch')
    results.require(package['version'] == EXPECTED_VERSION, 'package version mismatch')
    results.require(ROOT.name == EXPECTED_ID, 'folder name mismatch')
    results.require((ROOT / 'SKILL.md').is_file(), 'missing SKILL.md')
    results.require((ROOT / 'README.md').is_file(), 'missing README.md')
    results.require((ROOT / 'LICENSE').is_file(), 'missing LICENSE')
    for name in REQUIRED_COMMUNITY:
        results.require((ROOT / name).is_file(), f'missing community file: {name}')

    hub_files = sorted(path.name for path in (ROOT / 'references' / 'hubs').glob('*.md'))
    playbook_files = sorted(path.name for path in (ROOT / 'references' / 'playbooks').glob('*.md'))
    tool_files = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / 'scripts').rglob('*.py'))
    results.require(hub_files == sorted(REQUIRED_HUBS), 'hub inventory mismatch')
    results.require(playbook_files == sorted(REQUIRED_PLAYBOOKS), 'playbook inventory mismatch')
    results.require(set(tool_files) == set(REQUIRED_TOOLS), 'tool inventory mismatch')

    hub_hashes = {}
    hub_line_counts = []
    for path in (ROOT / 'references' / 'hubs').glob('*.md'):
        text = path.read_text(encoding='utf-8')
        line_count = len(text.splitlines())
        hub_line_counts.append(line_count)
        results.require(line_count >= MIN_HUB_LINES, f'hub too shallow: {path.name} ({line_count} lines)')
        fragments = find_semantic_fragments(text)
        results.require(not fragments, f'semantic fragments in hub {path.name}: {fragments[:3]}')
        body_hash = sha256('\n'.join(text.splitlines()[1:]).strip().encode('utf-8')).hexdigest()
        hub_hashes.setdefault(body_hash, []).append(path.name)
    for names in hub_hashes.values():
        results.require(len(names) == 1, f'duplicate hub bodies: {", ".join(sorted(names))}')
    results.require(len(set(hub_line_counts)) >= MIN_HUB_LINE_VARIETY, f'hub lengths show low variety: {hub_line_counts}')

    playbook_hashes = {}
    playbook_line_counts = []
    for path in (ROOT / 'references' / 'playbooks').glob('*.md'):
        text = path.read_text(encoding='utf-8')
        lines = text.splitlines()
        line_count = len(lines)
        playbook_line_counts.append(line_count)
        results.require(line_count >= MIN_PLAYBOOK_LINES, f'playbook too shallow: {path.name} ({line_count} lines)')
        fragments = find_semantic_fragments(text)
        results.require(not fragments, f'semantic fragments in playbook {path.name}: {fragments[:3]}')
        body_hash = sha256('\n'.join(lines[1:]).strip().encode('utf-8')).hexdigest()
        playbook_hashes.setdefault(body_hash, []).append(path.name)
    for names in playbook_hashes.values():
        results.require(len(names) == 1, f'duplicate playbook bodies: {", ".join(sorted(names))}')
    results.require(len(set(playbook_line_counts)) >= MIN_PLAYBOOK_LINE_VARIETY, f'playbook lengths show low variety: {playbook_line_counts}')

    skill_text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    results.require('Business Context -> Real Constraint -> Evidence -> Minimum Sufficient Solution -> Implementation -> Measurement -> Review' in skill_text, 'missing philosophy sequence')
    results.require('Do not use this skill when' in skill_text, 'missing negative boundaries')
    results.require('Jira and Atlassian mutations require explicit confirmation' in skill_text, 'missing Jira confirmation rule')
    results.require('marketing skill' in skill_text and 'engineering skill' in skill_text, 'missing boundary routing references')

    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    results.require('Personalized AI Skills for Your Business' in readme, 'README missing Personalized AI Skills section')
    results.require('About Growth Insider' in readme, 'README missing About Growth Insider section')
    results.require('NOT MODEL TESTED' in (ROOT / 'docs' / 'platform-compatibility.md').read_text(encoding='utf-8'), 'platform compatibility missing model test boundary')
    results.require('support@growthinsider.pl' in (ROOT / 'SUPPORT.md').read_text(encoding='utf-8'), 'SUPPORT.md missing contact')

    csv_path = ROOT / 'docs' / 'capability-parity-matrix.csv'
    row_count = sum(1 for line in csv_path.read_text(encoding='utf-8-sig').splitlines()[1:] if line.strip())
    results.require(row_count == 357, f'expected 357 parity rows, found {row_count}')

    results.require(not any(path.suffix.lower() == '.zip' for path in ROOT.rglob('*') if path.is_file()), 'zip artifacts are not allowed inside target')
    results.require(not (ROOT / 'scripts' / 'discovery' / 'persona_generator.py').exists(), 'persona generator must not be ported')
    results.require(not (ROOT / 'scripts' / 'discovery' / 'rice_prioritizer.py').exists(), 'rice prioritizer must not be ported')
    results.require(not (ROOT / 'scripts' / 'delivery' / 'sprint_health_scorer.py').exists(), 'sprint health scorer must not be ported')

    scan_text = []
    for path in ROOT.rglob('*'):
        if not path.is_file() or path.suffix.lower() not in {'.md', '.py', '.json', '.yaml', '.yml', '.cff', '.txt'}:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith('tests/') or rel == 'scripts/validate_repository.py':
            continue
        scan_text.append(path.read_text(encoding='utf-8', errors='replace'))
    all_text = '\n'.join(scan_text)
    for token in FORBIDDEN_STRINGS:
        results.require(token not in all_text, f'forbidden legacy token present: {token}')
    for phrase in FORBIDDEN_FILLER_PHRASES:
        results.require(phrase not in all_text, f'forbidden filler phrase present: {phrase}')

    for path in ROOT.rglob('*.json'):
        try:
            json.loads(path.read_text(encoding='utf-8'))
        except json.JSONDecodeError as exc:
            results.errors.append(f'invalid json {path.relative_to(ROOT).as_posix()}: {exc}')
    for path in ROOT.rglob('*.py'):
        try:
            compile(path.read_text(encoding='utf-8'), str(path), 'exec')
        except SyntaxError as exc:
            results.errors.append(f'python syntax error {path.relative_to(ROOT).as_posix()}: {exc}')

    print(json.dumps({'status': 'PASS' if not results.errors else 'FAIL', 'errors': results.errors, 'warnings': results.warnings}, indent=2))
    return 0 if not results.errors else 1


if __name__ == '__main__':
    raise SystemExit(main())
