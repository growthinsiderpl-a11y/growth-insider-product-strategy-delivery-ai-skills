# Agile Delivery and Release Planning

Use this hub to connect product decisions to realistic sprint planning, release readiness, dependency trade-offs, and post-release learning.

## Purpose

This hub helps the team protect the intended outcome while negotiating scope, readiness, risk, and timing. It keeps delivery planning anchored in product consequences rather than in ceremony, utilization optics, or date pressure alone.

## What This Hub Owns

- Sprint goal framing from product intent.
- Delivery trade-offs and readiness discussions.
- Release gating from explicit evidence.
- Cadence decisions that preserve learning and reliability.
- Communication of what will and will not ship.
- Post-release review obligations.

## Route Away When

- The task is CI pipeline implementation or operational automation.
- The core work is rollout mechanics owned by engineering.
- The artifact would become agile ceremony with no real delivery decision.
- The request depends on hidden velocity scores or fake health metrics.
- The output is a dashboard that does not change a product call.

## Related Playbooks

- `references/playbooks/sprint-planning-tradeoffs.md`.
- `references/playbooks/release-decision-gate.md`.
- `references/playbooks/engineering-handoff-packet.md`.

## Core Questions

- What sprint or release decision is actually pending?
- Which stories matter to the outcome and which are only nice to have?
- What evidence says the release should proceed, narrow, delay, or stage?
- Which dependency could break the plan?
- What learning or rollout signal must exist after release?
- What is the cost of forcing the date anyway?

## Evidence To Gather

- Refined backlog with stories and acceptance intent.
- Capacity and dependency view.
- Known risks and unresolved scope questions.
- Test, rollout, and support evidence as provided by engineering, QA, or operations.
- Migration or support readiness where relevant.
- Post-release measurement plan.

## Decision Procedure

### Set Sprint Intent

- Start with the product outcome, not the ticket count.
- Choose the minimum story set that can deliver the intended result.
- Surface dependency and readiness risks before commitment.
- Separate must-ship scope from stretch scope.
- Record what learning the sprint should create.

### Trade Off Scope

- Remove low-leverage scope before negotiating quality or observability away.
- Protect instrumentation, release safety, and critical edge-case coverage.
- Identify stories that can move without invalidating the core outcome.
- Tell stakeholders what changed and why.
- Treat incomplete refinement as a planning risk, not as a surprise to absorb later.

### Gate the Release

- Request explicit evidence for readiness rather than confident language.
- Check rollback, reversal, or staged rollout options where relevant.
- Tie release approval to known risks and review windows.
- Document what is still unknown.
- Prefer staged release when uncertainty remains material.

### Review Outcomes

- Measure the target outcome and guardrails after release.
- Capture surprises in user behavior, support load, or operational burden.
- Update the roadmap or backlog based on what the release taught.
- Avoid declaring success on shipment alone.
- Carry forward unresolved debt explicitly.

## Failure Modes

- Planning around utilization instead of outcomes.
- Protecting scope while sacrificing quality visibility.
- Treating release approval as a calendar event.
- Using sprint metrics as a substitute for product judgment.
- Letting hidden dependencies surface too late.
- Pretending there is no trade-off when a date is forced.

## Cross-Skill Handoffs

- Engineering owns code-level rollout mechanics, automation, and deep technical readiness checks.
- Marketing owns launch communications and acquisition timing.
- Product owns the release decision trade-off, the scope boundary, and the post-release learning plan.
- Governance owns recording the approved decision and its conditions.

## Expected Outputs

- Sprint trade-off note.
- Release decision memo.
- Scope narrow recommendation.
- Post-release learning plan.
- Stakeholder readiness summary.
- Review checklist for high-risk releases.

## Example Prompts

- Should we narrow this sprint or keep the current scope?
- Assess whether this release has enough product evidence to proceed.
- Translate backlog uncertainty into a realistic delivery plan.

## Decision Rules

- Protect the outcome slice before protecting the ticket count.
- If release approval depends on optimism about support, migration, or monitoring, it is not really ready.
- A conditional release is only meaningful when the conditions are explicit and observable.
- Do not move a risk-heavy story into a sprint simply because the date is visible.
- When a date is fixed, the first negotiation should be scope, not quality.
- A release review should name what the product team will check after launch and by when.

## Worked Example

- A release includes a new approvals queue, team settings, and audit history.
- If migration notes are incomplete and support has not prepared for admin confusion, the full scope is not equally ready.
- The narrower move may be to ship the queue and settings first while staging audit history after support and migration materials are complete.
- That is not a failure of agile delivery. It is a product decision that protects user trust while preserving learning.
- The follow-up artifact should show which metrics and support signals determine whether the staged release expands.

## What A Narrower Release Should Show

- Which outcome is still protected after scope reduction.
- Which risk, migration burden, or support burden was removed by narrowing.
- Which deferred item remains important enough to re-enter the next planning window.
- Which post-release metric or signal will determine the next release decision.
