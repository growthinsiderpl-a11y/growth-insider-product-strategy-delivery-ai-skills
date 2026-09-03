# Engineering Handoff Packet

Turn a product decision into a concise packet that engineering
can challenge, estimate, and implement without inheriting silent
ambiguity.

## When To Run It

- product work is moving into estimation or implementation
- engineering asks what is actually required
- prior handoffs created thrash or rework
- the team needs one authoritative handoff artifact

## Do Not Run It When

- the problem is still strategic or exploratory
- the user wants deep architecture design rather than a product
  packet
- there is no agreed product intent yet
- the packet would only duplicate a weak PRD without improving
  clarity

## Inputs

- approved problem statement
- scope
- workflow
- edge cases
- metrics
- release assumptions

## Procedure

### Package the Why

- start with problem, user, and evidence
- state the outcome and metric intent
- include what happens if the change is not made
- preserve known limitations
- show how the work fits the current roadmap or release

### Package the What

- describe the target behavior and scope boundaries
- list non-goals
- cover roles, permissions, and edge states that matter
- keep implementation suggestions clearly labeled as optional
  context
- show what must remain configurable or flexible

### Package the Prove-It Layer

- include acceptance intent, analytics expectations, and release
  guardrails
- identify rollout or support implications
- show what evidence should exist after release
- note risks that deserve engineering challenge
- state what product will review after delivery

### Package the Questions

- list unresolved points openly
- label which questions product owns and which engineering
  should answer
- state where phased delivery is acceptable
- invite alternatives that still satisfy the outcome
- note which unknowns are safe to leave open for estimation

### Finalize the Handoff

- summarize decisions in one digestible page or packet
- confirm owners and next meeting
- update source artifacts after feedback
- avoid duplicating entire PRDs when a packet is enough
- capture deltas after engineering review so the packet remains
  current

## Decision Tests

- the packet starts with the problem and evidence
- scope and non-goals are explicit
- acceptance and measurement expectations exist
- open questions are visible
- engineering can challenge assumptions without searching
  multiple files

## Outputs

- handoff packet
- clarification log
- release expectation note
- challenge prompts for engineering
- artifact delta summary after review

## Failure Modes

- sending engineering a feature wish list
- hiding ambiguity in long prose
- omitting measurement and release expectations
- pretending the handoff ends product ownership

## Review and Follow-through

- revise the packet after engineering challenge
- feed learning back into PRD and stories
- use post-release review to improve future handoffs
- record recurring ambiguity patterns for template improvement

## Escalate or Stop When

- the packet cannot state the user problem clearly
- non-goals are absent so scope can expand silently
- telemetry and release expectations are missing
- engineering challenge points are hidden instead of invited

## Worked Scenario

- For delegated approvals, the packet should define user risk,
  auditability, revocation, and staged rollout assumptions
  before engineering estimates implementation.
- That lets engineering challenge inherited-permission logic
  without losing the product boundary.
