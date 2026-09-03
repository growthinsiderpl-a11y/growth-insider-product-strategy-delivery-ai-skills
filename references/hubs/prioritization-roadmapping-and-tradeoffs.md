# Prioritization, Roadmapping, and Trade-offs

Use this hub for explicit prioritization logic, roadmap structure, dependency-aware sequencing, and trade-offs that remain transparent to stakeholders.

## Purpose

This hub helps product teams compare options honestly, sequence work coherently, and maintain a roadmap that reflects real constraints, real choices, and real uncertainty rather than political safety.

## What This Hub Owns

- Decision criteria design.
- Comparison of options using explicit weights or ranked factors.
- Roadmap consistency and dependency sequencing.
- Capacity-aware trade-off framing.
- Deferral, narrowing, and retirement decisions.
- Maintenance of roadmap honesty over time.

## Route Away When

- The request is for an opaque ranking authority or canned answer.
- The work is sprint choreography owned by delivery planning.
- The main need is a marketing calendar rather than a product roadmap.
- The core issue is deep architecture dependency mapping.
- The roadmap artifact merely mirrors stakeholder politics.

## Related Playbooks

- `references/playbooks/prioritization-comparison.md`.
- `references/playbooks/roadmap-consistency-check.md`.
- `references/playbooks/sprint-planning-tradeoffs.md`.
- `references/playbooks/board-update-narrative.md`.

## Core Questions

- What decision is the prioritization output supposed to support?
- Which criteria actually matter under current strategy and constraints?
- How do dependencies change apparent impact, speed, or reversibility?
- What does the roadmap clearly say no to?
- Which initiative is reversible and which one is expensive to unwind?
- What evidence or trigger would justify re-sequencing?

## Evidence To Gather

- Explicit objective and target outcome.
- Opportunity evidence or customer impact rationale.
- Capacity assumptions and known delivery limits.
- Product-level dependency map.
- Commercial, compliance, or operational timing constraints.
- Records of prior roadmap promises that still influence perception.

## Decision Procedure

### Set Criteria

- Name the criteria in plain language.
- Let the decision owner choose the weighting or ranking logic explicitly.
- Write why each criterion matters now.
- Remove redundant criteria that only restate the same argument twice.
- Record which criteria were considered and intentionally left out.

### Compare Options

- Score or rank options from evidence or clearly labeled assumptions.
- Add short rationale next to each comparison result.
- Surface uncertainty and missing inputs rather than forcing precision.
- Test whether the recommendation changes under a different but plausible weighting.
- Identify which option produces the fastest reliable learning.

### Build the Roadmap

- Group items by outcome theme, customer problem, or strategic risk.
- Show intended sequence and the logic behind it.
- Mark each item as committed, conditional, or exploratory.
- Balance learning work with delivery work instead of hiding discovery inside committed promises.
- Make the cost of leaving an item in the roadmap visible, including attention cost and trust cost.

### Maintain Consistency

- Review the roadmap against strategy, constraints, and current evidence.
- Retire orphan items with no objective linkage.
- Flag releases or quarters overloaded beyond plausible capacity.
- Explain sequence changes in terms of evidence, risk, or dependency movement.
- Preserve the rationale so future revisions can be compared against prior logic.

## Failure Modes

- Treating comparison models as automatic truth.
- Hiding politics behind apparently neutral numbers.
- Publishing roadmap items with no outcome link.
- Overstuffing every quarter because everything feels urgent.
- Using roadmap slides as promise theater.
- Failing to re-check priority after conditions change.

## Cross-Skill Handoffs

- Send campaign timing and external launch calendars to marketing.
- Send code-level complexity breakdown and technical sequencing detail to engineering.
- Keep product trade-offs, sequencing rationale, and decision logic here.
- Feed approved priority changes into governance and stakeholder communication once the product call is made.

## Expected Outputs

- Weighted comparison or ranked trade-off note.
- Roadmap consistency review.
- Defer, narrow, or kill recommendation.
- Outcome-themed roadmap narrative.
- Stakeholder explanation for priority changes.
- Sensitivity note that shows what could change the ranking.

## Example Prompts

- Help us choose among onboarding redesign, pricing cleanup, and governed approvals.
- Audit our roadmap for contradictions before the quarterly review.
- Build an explicit prioritization model without hidden assumptions.

## Decision Rules

- A roadmap item with no stated objective and no clear consequence of delay does not deserve committed space.
- When one option wins only because effort was estimated optimistically, treat the ranking as fragile.
- If a recommendation collapses when one criterion changes slightly, the decision should be framed as conditional.
- Roadmaps should distinguish learning bets from delivery commitments.
- A defer decision is credible only when the cost of delay is named openly.
- If priority depends on another team changing policy or behavior, that dependency must appear in the roadmap logic.

## Worked Example

- Suppose the team must choose between search relevance work, governed approvals, and invoice export.
- Search relevance affects many accounts, but the evidence is diffuse and the path to measured improvement is broad.
- Governed approvals affect fewer accounts, but they unblock expansion in the segment the company is actively targeting.
- Invoice export is requested loudly by sales but depends on policy choices that are still unsettled.
- A transparent comparison can therefore rank governed approvals first, keep search relevance as a bounded learning track, and defer invoice export until the policy dependency is resolved.

## What A Trustworthy Roadmap Call Includes

- A visible explanation of why one item moved up and what moved down as a consequence.
- Confidence labeling that distinguishes evidence-backed commitments from exploratory work.
- Dependency notes that explain whether another team, policy, or prerequisite can still alter timing.
- The first trigger that would justify re-ranking the roadmap.
