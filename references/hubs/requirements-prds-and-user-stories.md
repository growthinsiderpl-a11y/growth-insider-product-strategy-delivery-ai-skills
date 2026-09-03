# Requirements, PRDs, and User Stories

Use this hub when product intent must become precise requirements, crisp PRDs, testable user stories, and acceptance criteria that remain tied to outcomes.

## Purpose

This hub turns a product decision into artifacts that engineering, design, QA, support, and leadership can all challenge and use without guessing the problem, the scope boundary, or the success condition.

## What This Hub Owns

- Problem-first PRD structure.
- Scope and non-goals.
- User story quality and slicing.
- Acceptance criteria completeness.
- Analytics, risk, and rollout requirements at the product boundary.
- Artifact quality before handoff.

## Route Away When

- The real need is code-level design or architecture detail.
- The request is a marketing brief, launch deck, or external messaging artifact.
- The team needs legal or compliance determination that product cannot decide alone.
- The artifact is being padded with prose to hide missing decisions.
- The work belongs in engineering design documents rather than in product requirements.

## Related Playbooks

- `references/playbooks/prd-quality-review.md`.
- `references/playbooks/user-story-validation.md`.
- `references/playbooks/acceptance-criteria-validation.md`.
- `references/playbooks/engineering-handoff-packet.md`.

## Core Questions

- What decision does this document lock in?
- Which user and workflow does the requirement cover?
- What is explicitly out of scope?
- How will delivery and QA know when the requirement is satisfied?
- What instrumentation, rollout, or support detail matters before launch?
- Which unresolved question is still too important to hide?

## Evidence To Gather

- Problem evidence and user context.
- Workflow or journey maps for the target slice.
- Edge cases, permission rules, and service constraints.
- Metric expectations and guardrails.
- Dependency and rollout considerations.
- Open questions that could materially change scope or risk.

## Decision Procedure

### Shape the PRD

- Start from the problem, evidence, user, and desired outcome.
- State scope and non-goals early.
- Separate required behavior from implementation guesses.
- Capture the success metric and relevant guardrails.
- Keep open questions visible rather than burying them late in the document.

### Write Real Stories

- Express who needs what and why it matters.
- Keep stories small enough to discuss, estimate, and test.
- Remove delivery-step tasks that are pretending to be user value.
- Split stories along workflow, rule, permission, or role boundaries when that preserves clarity.
- Preserve traceability from each story back to the parent requirement.

### Define Acceptance

- Write observable conditions rather than intentions.
- Cover happy path, validation, failure handling, permissions, and data capture where relevant.
- Call out telemetry, auditability, or rollout behavior when those affect launch confidence.
- Mark unresolved policy decisions instead of guessing them.
- Use examples only when they reduce ambiguity materially.

### Prepare the Package

- Summarize dependencies, assumptions, and release notes that matter to planning.
- Note analytics, support, and migration implications where relevant.
- Explain what engineering should challenge rather than merely implement.
- Document what changed since the prior draft if the artifact is iterative.
- Keep the package tight enough that teams can actually read it.

## Failure Modes

- Confusing a feature pitch with a requirement.
- Writing stories so broad that every edge case becomes a surprise later.
- Using acceptance criteria as a copy of UI labels.
- Burying non-goals or risks near the end.
- Locking implementation choices too early.
- Treating longer documents as better documents.

## Cross-Skill Handoffs

- Send deep system design and architecture decisions to engineering.
- Send demand narrative and external launch communication to marketing.
- Keep product intent, scope decisions, user value, and acceptance intent here.
- Feed requirement review findings into delivery planning and release gating after the product package is solid.

## Expected Outputs

- PRD review.
- Story slicing recommendation.
- Acceptance criteria checklist.
- Scope clarification memo.
- Hardened handoff packet.
- Ready or not-ready decision for refinement.

## Example Prompts

- Review this PRD for missing decisions before engineering refinement.
- Turn one epic into smaller user stories with real value boundaries.
- Check whether our requirements still reflect the actual user problem.

## Decision Rules

- A PRD should be harder to misunderstand than to skim.
- User stories should describe a change in capability or outcome, not merely a work step.
- Acceptance criteria are incomplete when they skip the risky path, the failure path, or the permission path.
- Open questions belong near the decision surface, not hidden in appendices.
- If non-goals cannot be written clearly, the scope is still too loose.
- The best PRD revision often deletes speculative prose and replaces it with sharper boundaries.

## Worked Example

- A requirement says admins should manage delegated approvals during absence periods.
- A weak version lists screens and fields but never states the user risk or the business consequence.
- A stronger version names the problem, defines the target workflow, and states that revocation, auditability, and role clarity are part of launch confidence.
- Stories can then split cleanly into delegation setup, active-delegation visibility, and history access.
- That rewrite reduces engineering back-and-forth because the product boundary is explicit.

## What Engineering Should Not Have To Guess

- Why the workflow matters now and which user risk the change is meant to reduce.
- What stays out of scope even if adjacent requests sound reasonable.
- Which edge cases are essential to launch confidence.
- How product will know after release whether the requirement actually improved the target outcome.
