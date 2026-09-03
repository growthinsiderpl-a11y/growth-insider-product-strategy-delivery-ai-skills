# Product Operations, Project, and Portfolio Governance

Use this hub to keep product work operationally governable through decision rights, intake, governance cadences, Jira or Atlassian change safety, and portfolio review hygiene.

## Purpose

This hub helps the organization preserve accountability and clarity without adding performative process. It defines how planning artifacts stay trustworthy, how governance forums earn their time, and how planning-system changes stay explicit and reviewable.

## What This Hub Owns

- Decision rights and governance structures.
- Portfolio and project review cadence.
- Intake and change-control hygiene.
- Atlassian or Jira mutation confirmation rules.
- Operating artifacts that preserve accountability without paperwork theater.
- Clear interfaces between planning systems and human approval.

## Route Away When

- The real need is tool administration deep dives better owned by specialist admins.
- The task is software engineering workflow implementation.
- The artifact is generic project status theater.
- The request depends on secret portfolio ranking formulas.
- The work would mutate live planning tools without explicit approval logic.

## Related Playbooks

- `references/playbooks/atlassian-jira-mutation-confirmation.md`.
- `references/playbooks/okr-cascade-validation.md`.
- `references/playbooks/roadmap-consistency-check.md`.

## Core Questions

- Who can decide, who must be consulted, and who only needs visibility?
- What operating artifact is missing and causing confusion or churn?
- Which Jira or Atlassian change would mutate a source of truth?
- How do we preserve speed without unreviewed structural changes?
- Where is the governance loop too heavy or too weak?
- What evidence should accompany a portfolio or project review?

## Evidence To Gather

- Current decision forums, attendees, and cadences.
- Backlog or portfolio hygiene problems.
- Jira workflow, field, automation, or permission change proposals.
- Examples of lost ownership, duplicate work, or contradictory priorities.
- Signs that current reviews are not producing real decisions.
- Audit trail expectations for structural planning changes.

## Decision Procedure

### Map Governance

- List forums, owners, and cadence.
- Clarify the decision each forum exists to make.
- Remove forums that only repeat status without changing action.
- Define escalation paths for blocked cross-functional decisions.
- State where product operations ends and delivery execution begins.

### Harden Operating Artifacts

- Standardize the minimum fields for intake, roadmap items, decision notes, and portfolio views.
- Make decision dates and owners visible.
- Limit required fields to what improves a real decision.
- Define archival, retirement, and stale-item cleanup rules.
- Show which artifacts are authoritative and which are merely presentational.

### Protect Jira and Atlassian Mutations

- Classify each requested action as read-only analysis, calculation, draft, local change, or external side effect.
- Require explicit confirmation before any action that changes shared planning data, workflow, fields, automations, or permissions.
- Draft the intended mutation and expected blast radius before execution.
- Record rollback, restore, or sandbox validation steps where relevant.
- Store the approval and the outcome in a reviewable place.

### Run Governance Reviews

- Bring portfolio, project, and governance evidence into one decision-oriented review.
- Focus on choices, changes, and risks rather than on presentation polish.
- Document follow-through with owners and dates.
- Measure whether the governance change reduced ambiguity, waste, or rework.
- Revise the operating model when it becomes ceremony.

## Failure Modes

- Governance that exists only to generate artifacts.
- Jira changes executed because they appear harmless.
- Unclear decision rights leading to side-channel commitments.
- Review meetings that never retire work.
- Adding process without naming the failure it fixes.
- Treating planning-system mutations as low-risk convenience.

## Cross-Skill Handoffs

- Engineering owns CI, repository automation, and code workflow mechanics.
- Marketing owns campaign operations and martech workflows.
- Product owns product governance, planning hygiene, review design, and change safety for product planning systems.
- Security or admin owners may review structural mutations without replacing product approval responsibility.

## Expected Outputs

- Operating model note.
- Portfolio review checklist.
- Jira mutation confirmation draft.
- Governance simplification plan.
- Decision-rights matrix.
- Source-of-truth policy note.

## Example Prompts

- Define confirmation rules before an AI agent touches Jira.
- Clean up our portfolio governance without adding bureaucracy.
- Design a product operations cadence that actually changes decisions.

## Decision Rules

- Governance should reduce ambiguity or risk. If it does neither, simplify it.
- Every recurring review meeting should exist to make a decision, not merely to share updates.
- Jira and Atlassian mutations belong behind explicit confirmation and visible scope.
- A source-of-truth field is not safe to automate until ownership and rollback are clear.
- Portfolio governance must preserve kill decisions, not just approval decisions.
- If product operations is always cleaning stale data, the operating model is likely too permissive or too vague.

## Worked Example

- An organization wants an agent to relabel Jira statuses and update custom fields across several product projects.
- A good governance artifact classifies those steps as explicit external side effects and requires a drafted scope, blast-radius note, approval, and rollback path.
- It also records whether the change belongs in sandbox or production first.
- That discipline is not bureaucracy for its own sake. It is how the source of truth remains trustworthy.
- The same governance note should also define which read-only analyses remain safe without extra approval.

## What A Safe Governance Record Includes

- The decision right, the artifact updated, and the system of record affected.
- The difference between local drafting and live mutation.
- The rollback or restore path for any planning-system change that touches workflows, permissions, or shared fields.
- The review date for checking whether the governance change actually reduced confusion or rework.
