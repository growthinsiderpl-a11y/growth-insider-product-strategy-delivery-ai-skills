# Growth Insider Product Strategy & Delivery AI Skills

[![Release](https://img.shields.io/badge/release-v1.0.0-rc.1-175CD3)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-12B76A)](LICENSE)
[![Format: Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-7A5AF8)](https://agentskills.io/specification)
[![Validation: local](https://img.shields.io/badge/validation-local%20static%20checks-F79009)](scripts/validate_repository.py)

Constraint-first product skill infrastructure for teams, founders, consultants, and AI runtimes.

This repository turns vague requests such as "what should we build next," "is this roadmap coherent," "do we have product-market fit," "why is retention slipping," or "is this PRD ready for engineering" into evidence-labeled product analysis, bounded decisions, deterministic validation, and reviewable operating artifacts.

## Why This Exists

Many product prompts jump from opinion to solution. That creates polished planning artifacts before the real problem is clear.

Growth Insider uses a stricter sequence:

`Business Context -> Real Constraint -> Evidence -> Minimum Sufficient Solution -> Implementation -> Measurement -> Review`

The package does not begin with role-play. It begins with the product problem, the operational constraint, and the quality of the available evidence.

## What It Does

- covers product strategy, portfolio, discovery, opportunity validation, PMF evidence, analytics, prioritization, roadmapping, requirements, delivery planning, UX research, product design quality, monetization, retention, governance, and product-to-engineering translation
- organizes knowledge into 13 substantive hubs and 19 focused playbooks
- provides 9 deterministic local tools plus repository and behavioral validators
- distinguishes facts, calculations, assumptions, hypotheses, heuristics, policies, and unknowns
- keeps Jira and Atlassian changes behind explicit confirmation rules
- preserves strict routing boundaries against marketing and engineering ownership

## How It Works

1. Frame the product outcome, the decision, the segment, and the constraint.
2. Diagnose the binding product problem instead of optimizing everything at once.
3. Load the smallest relevant hub and playbook.
4. Run deterministic local tools only where explicit math or structural validation helps.
5. Produce a memo, plan, review, or handoff packet with next actions and review conditions.

## Quick Start

Clone or download the release candidate:

```bash
git clone https://github.com/growthinsiderpl-a11y/growth-insider-product-strategy-delivery-ai-skills.git
``` 

1. Place the `growth-insider-product-strategy-delivery-ai-skills` folder in an Agent Skills compatible location.
2. Keep the folder name unchanged.
3. Start with a concrete product question and any known evidence, metrics, or constraints.
4. Let the runtime load `SKILL.md`, then only the referenced hubs, playbooks, and scripts needed for the request.

Example prompts:

- "Choose between improving activation and building a new premium workflow for the next quarter."
- "Assess whether our product has real fit in team-based operations use cases or just one noisy enterprise account."
- "Review this PRD and tell me what engineering will challenge before estimation."
- "Build a discovery interview plan for a churn spike among first-month users."
- "Check whether our roadmap is coherent with our OKRs and known dependencies."
- "Draft a board update that explains why we narrowed scope and delayed the release."

## Decision Surface

The package is organized around product problems, not job-title simulation.

| Area | Primary artifact |
| --- | --- |
| Strategy and portfolio | strategy memo, bet comparison, portfolio allocation |
| Discovery and validation | interview plan, assumption map, opportunity assessment |
| PMF and customer evidence | fit claim memo, evidence gap review |
| Analytics and learning | metric definition, cohort interpretation, learning plan |
| Prioritization and roadmap | weighted comparison, roadmap consistency review |
| Requirements and handoff | PRD review, story validation, acceptance criteria review |
| Delivery and release | sprint trade-off note, release gate |
| UX and design quality | journey workshop, usability synthesis, interface quality review |
| Monetization and retention | packaging memo, retention diagnosis |
| Governance and communication | OKR cascade review, board narrative, Jira mutation confirmation |

## Repository Structure

```text
growth-insider-product-strategy-delivery-ai-skills/
??? SKILL.md
??? manifest.json
??? references/
?   ??? hubs/
?   ??? playbooks/
??? scripts/
??? adapters/
??? examples/
??? docs/
??? tests/
??? .github/
```

## Platform Compatibility

The package follows the open [Agent Skills specification](https://agentskills.io/specification), is documented for current [OpenAI Build Skills guidance](https://learn.chatgpt.com/docs/build-skills), references current [Anthropic Agent Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), and ships an OpenAI-oriented descriptor in `agents/openai.yaml`.

Compatibility claims in this release are limited to:

- `DESIGNED_FOR`: open Agent Skills compatible runtimes
- `STATICALLY_VALIDATED`: repository structure, manifests, links, and schemas
- `LOCALLY_TESTED`: deterministic scripts and local tests
- `NOT MODEL TESTED`: no claim of live platform model execution

See [docs/platform-compatibility.md](docs/platform-compatibility.md).

## Personalized AI Skills for Your Business

The public package is a reusable product operating system. Personalized AI Skills go further by encoding a company's actual segments, product principles, event definitions, planning rituals, approved templates, governance rules, and escalation boundaries.

Growth Insider can adapt this pattern to a specific business context, including:

- company-specific strategy and roadmap logic
- approved discovery and evidence workflows
- house definitions for activation, retention, and monetization metrics
- product-specific planning, review, and handoff templates
- internal evaluation suites and routing rules

That is custom operating logic, not a generic prompt bundle.

## About Growth Insider

[Growth Insider](https://growthinsider.pl/en/) works across product, software, and growth with a constraint-first approach. The aim is not to maximize complexity; it is to reach the minimum sufficient solution that matches the real constraint, can be implemented, can be measured, and can be reviewed.

Growth Insider is based in WrocĹ‚aw, Poland. Contact: [support@growthinsider.pl](mailto:support@growthinsider.pl).

## Security and Privacy

The core package runs locally and ships no mandatory network integration. Scripts are deterministic and intended to analyze user-supplied product artifacts, planning structures, or offline evidence.

## Trademarks and Non-Affiliation

References to OpenAI, ChatGPT, Codex, Anthropic, Claude, and Agent Skills describe interoperability targets and public documentation only. No partnership, certification, or endorsement is claimed.

## License

Released under the [MIT License](LICENSE). Copyright (c) 2026 Growth Insider
