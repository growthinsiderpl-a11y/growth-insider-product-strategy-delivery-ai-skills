---
name: growth-insider-product-strategy-delivery-ai-skills
description: Structured product operating skill for strategy, portfolio, discovery, customer evidence, JTBD opportunity framing, analytics, prioritization, roadmapping, requirements, delivery planning, UX research, design-quality decisions, monetization, retention, governance, and product-to-engineering translation. Use when the user needs a decision-ready product artifact tied to evidence and constraints. Do not use for acquisition marketing strategy, SEO campaigns, software architecture, implementation planning, or production systems.
license: MIT
metadata:
  title: Growth Insider Product Strategy & Delivery AI Skills
  product: Growth Insider Product Strategy & Delivery AI Skills
  product_id: growth-insider-product-strategy-delivery-ai-skills
  version: 1.0.0-rc.1
  author: Growth Insider
  maintainer: Growth Insider
  publisher: Growth Insider
  organization: Growth Insider
  website: https://growthinsider.pl/en/
  contact: support@growthinsider.pl
  location: Wrocław, Poland
  copyright: Copyright (c) 2026 Growth Insider
  status: release-candidate
  architecture: compact-skill-hubs-playbooks-tools
  compatibility: Designed for Agent Skills compatible runtimes that can read markdown, optionally run local scripts, and preserve user control over evidence, prioritization logic, and external side effects.
---

# Growth Insider Product Strategy & Delivery AI Skills

Turn product questions into evidence-grounded decisions, bounded plans, delivery-ready artifacts, and measurable review loops.

This package does not simulate a CPO, Head of Product, or PM character. It starts from the product problem, the real constraint, the quality of the evidence, and the minimum sufficient move.

## Use this skill when

- the user needs product strategy, portfolio, discovery, or product-market-fit reasoning
- roadmap, prioritization, or trade-off decisions need explicit criteria and evidence
- requirements, PRDs, user stories, acceptance criteria, sprint planning, or release gates need product-level structure
- product analytics, retention, monetization, packaging, or design-quality decisions are the core problem
- a board, stakeholder, or product-operations artifact must preserve uncertainty and decision logic
- engineering needs a cleaner product handoff with scope, acceptance intent, and measurement expectations

## Do not use this skill when

- the request is primarily acquisition strategy, SEO strategy, campaign design, or external launch communications
- the request is software architecture, repository design, code implementation, CI, infrastructure, observability, or production operations
- the user wants hidden prioritization weights, fake PMF scores, persona generators, or velocity theater instead of explicit reasoning
- the task is generic brainstorming with no decision, evidence need, or operating consequence

## Operating philosophy

Always follow this sequence:

`Business Context -> Real Constraint -> Evidence -> Minimum Sufficient Solution -> Implementation -> Measurement -> Review`

Prefer the smallest product artifact that can improve a real decision.

## Evidence rules

Classify material claims as:

- `FACT_USER`
- `FACT_FILE`
- `FACT_TOOL`
- `FACT_EXTERNAL`
- `CALCULATION`
- `ASSUMPTION`
- `HYPOTHESIS`
- `UNKNOWN`

Use additional labels when relevant: `EXAMPLE`, `HEURISTIC`, `POLICY`, `BENCHMARK`, `LIMITATION`.

Read [references/evidence-and-uncertainty.md](references/evidence-and-uncertainty.md) whenever the decision carries strategic, delivery, monetization, or governance risk.

## Side-effect classes

Classify actions before proposing them:

- `READ`: inspect existing product, planning, or analytics information
- `CALCULATE`: run a deterministic local tool over user-supplied inputs
- `DRAFT`: create a memo, PRD, roadmap comparison, interview guide, or other draft artifact
- `MUTATE_LOCAL`: edit a local repository file or local planning artifact
- `EXTERNAL_SIDE_EFFECT`: change a live system, planning tool, issue tracker, workflow, permission, or automation

Jira and Atlassian mutations require explicit confirmation before execution.

## Workflow

### 1. Frame the product decision

State the business goal, user or segment, time horizon, operating constraint, evidence available, and what decision will change if the work is good.

### 2. Diagnose the real constraint

Determine whether the core problem is primarily:

- strategic focus or portfolio allocation
- discovery or opportunity uncertainty
- weak product-market-fit evidence
- unclear metrics or instrumentation
- prioritization or roadmap inconsistency
- requirement quality or handoff ambiguity
- delivery or release trade-offs
- UX research or journey confusion
- product design quality and interface trust
- monetization, pricing, or retention inside the product experience
- stakeholder communication or governance

### 3. Route

Load only the relevant hub from `references/hubs/`, then the focused playbook from `references/playbooks/`, then a deterministic script from `scripts/` when structure or arithmetic will reduce ambiguity.

### 4. Decide the method

Prefer the minimum sufficient method:

- direct recommendation for bounded product questions
- one hub plus one playbook for most specialist work
- multiple hubs only when strategy, delivery, monetization, or governance concerns materially interact

### 5. Produce the artifact

Valid outputs include:

- strategy memo
- portfolio trade-off review
- opportunity assessment
- discovery interview plan
- PMF evidence memo
- prioritization comparison
- roadmap consistency review
- PRD or story review
- sprint trade-off note
- release decision gate
- journey workshop plan
- retention diagnosis
- packaging design memo
- board update narrative
- engineering handoff packet

### 6. Measure and review

Every non-trivial answer should include expected signals, stop conditions or review timing, and what evidence would falsify the recommendation.

## Boundary routing

Use this repository for product-owned decisions from strategy through handoff.

Escalate to other skill families when the center of gravity shifts:

- acquisition, messaging, channels, lifecycle marketing, launch communications, or SEO strategy -> marketing skill
- architecture, implementation, code change planning, CI, reliability, observability, or production systems -> engineering skill

See [docs/cross-skill-routing-boundaries.md](docs/cross-skill-routing-boundaries.md).

## Tool discipline

Registered scripts return deterministic JSON, publish their schema via `--schema`, and never depend on the network. Use them when explicit calculations or structure validation reduce ambiguity, not as a substitute for product judgment.

- Experiment sample sizing: `scripts/analytics/calculate_experiment_sample_size.py`
- Product metrics: `scripts/analytics/calculate_product_metrics.py`
- Retention cohorts: `scripts/analytics/calculate_retention_cohorts.py`
- Evidence rubric completeness: `scripts/discovery/evaluate_evidence_rubric.py`
- Weighted prioritization comparison: `scripts/discovery/compare_prioritization_options.py`
- User story validation: `scripts/requirements/validate_user_story.py`
- Acceptance criteria validation: `scripts/requirements/validate_acceptance_criteria.py`
- Roadmap consistency: `scripts/delivery/validate_roadmap_consistency.py`
- OKR cascade validation: `scripts/delivery/validate_okr_cascade.py`

## Safety and misuse warnings

- Do not fabricate customer evidence, retention proof, or PMF certainty.
- Do not present RICE defaults, fake product scores, or hidden weights as truth.
- Do not use persona generators or sprint health scores in the core package.
- Do not claim release readiness, stakeholder alignment, or customer demand from partial evidence.
- Do not execute Jira or Atlassian mutations without explicit confirmation and a drafted scope.

## Progressive disclosure

Load in this order:

1. `references/capability-catalog.md`
2. relevant hub in `references/hubs/`
3. matching playbook in `references/playbooks/`
4. deterministic tool schema if calculation or validation is needed
5. example request or adapter only if the runtime or format requires it

Machine-readable inventory lives in [manifest.json](manifest.json).
