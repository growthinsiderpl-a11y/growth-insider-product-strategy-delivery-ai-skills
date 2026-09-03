# Release Decision Gate

Decide whether a release should proceed, narrow, delay, or stage
based on explicit evidence rather than momentum.

## When To Run It

- a product release has meaningful user, revenue, trust, or
  operational risk
- stakeholders want product sign-off
- uncertainty about readiness is high
- timing pressure could override sober product judgment

## Do Not Run It When

- the task is a code-level production-readiness review owned by
  engineering detail
- there is no product consequence to the release decision
- the organization wants approval language without evidence
- the release scope itself is still undefined

## Inputs

- release scope
- readiness evidence
- known risks
- rollback or reversal notes
- support readiness
- post-release measurement plan

## Procedure

### Clarify the Release Decision

- name what is being released and to whom
- state the product reason for the release now
- record the cost of delay and the cost of failure
- identify if staging is possible
- note whether scope can be narrowed while preserving the
  intended value

### Check Required Evidence

- review tests, support readiness, rollout notes, analytics,
  communications, and dependency confirmations as provided by the
  relevant owners
- flag missing evidence clearly
- do not convert confidence language into evidence
- check whether the release changes critical workflows or
  monetization
- mark what evidence will only exist after a limited release

### Review Risk Posture

- categorize user harm, revenue harm, trust harm, and operational
  complexity
- look for unresolved migration or support issues
- decide whether the release can be narrowed safely
- ensure guardrail monitoring exists for the risky paths
- check whether customer communication is needed before exposure

### Make the Decision

- choose proceed, proceed with conditions, narrow, delay, or
  stage
- write the rationale in one paragraph
- name the owner and review window
- document what would cause rollback or pause
- capture which risks are knowingly accepted

### Prepare Follow-through

- define first-look metrics
- make the post-release review date explicit
- capture any debt or deferred work created by the decision
- share the result with stakeholders succinctly
- feed the release outcome back into future gating standards

## Decision Tests

- the decision is one of several explicit outcomes
- missing evidence remains visible
- risk is reviewed in product terms
- post-release review is scheduled
- accepted risk is named rather than implied

## Outputs

- release gate memo
- missing-evidence list
- conditional approval statement
- review plan
- scope-narrowing recommendation when needed

## Failure Modes

- approving because the date exists
- burying risk under optimism
- treating lack of evidence as a small issue for later
- assuming staging solves every readiness problem

## Review and Follow-through

- review real behavior after release
- log lessons for future gates
- feed important misses into requirements and planning practices
- update stakeholders when the actual outcome diverges from the
  gate assumption

## Escalate or Stop When

- the decision depends on evidence that does not exist yet
- rollback or reversal logic is hand-waved
- support is expected to absorb confusion without preparation
- the release changes billing, permissions, or trust-heavy
  behavior without targeted monitoring

## Worked Scenario

- A permissions update is ready for a small governed cohort but
  not for all accounts because migration guidance is incomplete.
- The gate should recommend staged release with explicit review
  signals rather than a binary approve or reject posture.
- That keeps trust and learning intact.
