# PRD Quality Review

Review a PRD for decision clarity, scope discipline, evidence
traceability, risk visibility, and readiness for cross-functional
challenge.

## When To Run It

- a PRD will be shared with engineering, design, or leadership
- the team suspects the document is long but weak
- a feature request must be hardened before planning
- stakeholders are likely to challenge scope or rationale

## Do Not Run It When

- the artifact is only a rough note and the team is not yet ready
  for review
- the need is a code-level technical design review
- the document is being used to backfill a decision already made
  without evidence
- the real problem is missing discovery, not missing prose

## Inputs

- PRD text or structure
- problem evidence
- metric intent
- scope and non-goals
- dependencies
- release assumptions

## Procedure

### Check the Opening

- verify the PRD states the problem, user, and desired outcome
  early
- look for evidence or context that explains why now
- flag solution-first openings that skip the problem
- confirm the decision the PRD is seeking to lock
- check whether the opening sets expectations for the rest of the
  artifact

### Inspect Scope Control

- find explicit scope and non-goals
- look for hidden scope inside examples or edge-case prose
- check whether dependencies and assumptions are visible
- mark where the PRD is ambiguous enough to create rework
- identify where future phases are mixed into current commitment

### Review Validation Logic

- confirm success metrics and guardrails exist
- check whether analytics, rollout, and risk notes are present
  when relevant
- ensure open questions are not buried
- look for claims with no evidence source
- note where acceptance intent is still too vague to guide
  planning

### Assess Usability for Partners

- would engineering know what to challenge?
- would design know where uncertainty remains?
- would QA know what must be true?
- would leadership see the trade-off?
- would support or operations know what to prepare if this ships?

### Deliver the Verdict

- classify issues as blocking, important, or nice to improve
- rewrite the highest-risk gaps in concise language
- suggest the smallest revision set that materially improves the
  artifact
- note what does not need more prose
- state whether the PRD is ready, conditionally ready, or not
  ready

## Decision Tests

- problem and decision are explicit
- scope is bounded
- metrics and risks are present where needed
- the PRD is usable by cross-functional partners
- the review distinguishes blocking issues from polish

## Outputs

- PRD review with findings
- blocking issues list
- recommended revisions
- ready or not-ready judgment with rationale
- follow-up questions for the author

## Failure Modes

- rewarding verbosity over clarity
- ignoring scope ambiguity because the vision sounds strong
- failing to distinguish blocking problems from polish
- treating a rewrite as the only solution

## Review and Follow-through

- re-review after material changes
- carry remaining open questions into the handoff packet
- do not approve on tone alone
- capture common PRD failures for future templates

## Escalate or Stop When

- the problem statement and proposed solution conflict
- scope is implicit in examples instead of explicit in boundaries
- open questions would materially change effort or risk
- the PRD assumes engineering implementation choices without
  marking them as assumptions

## Worked Scenario

- A PRD for delegated approvals says trust matters but omits
  auditability and revocation behavior.
- The review should flag those as blocking because they shape
  user risk and release conditions, not as optional polish.
- That is the kind of correction that prevents rework later.
