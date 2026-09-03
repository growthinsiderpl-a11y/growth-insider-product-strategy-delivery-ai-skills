# Sprint Planning Trade-offs

Prepare or review sprint planning decisions with explicit product
trade-offs, protected outcome intent, and realistic scope control.

## When To Run It

- a sprint commitment is about to be made
- too much work is entering the sprint
- leaders want clarity on what should give first
- refinement quality varies across candidate work

## Do Not Run It When

- the issue is really annual planning or roadmap logic
- the request is to compute fake health or velocity scores
- engineering still lacks essential feasibility input
- nobody has defined the sprint outcome yet

## Inputs

- sprint goal
- candidate stories
- capacity assumptions
- dependencies
- known risks
- release timing

## Procedure

### Anchor the Sprint Goal

- write the intended user or business outcome
- separate must-have scope from supporting tasks
- clarify what success means by sprint end
- prevent the plan from becoming a ticket-count exercise
- identify which work would invalidate the sprint if absent

### Review Candidate Stories

- check alignment to the sprint goal
- remove stories that only add scope weight with low outcome
  leverage
- look for missing readiness information
- mark stories dependent on other teams or unresolved policy
- surface stories that can safely shift without harming the
  outcome

### Trade Off Intelligently

- drop optional scope before risking the core workflow
- protect instrumentation and release-safety needs
- identify stories that can move without invalidating the sprint
  goal
- make the cost of keeping each marginal story explicit
- note what debt the trade-off intentionally creates

### Prepare Stakeholder Language

- write what the team is committing to and what it is not
- explain why some stories are deferred
- name the review point if mid-sprint trade-offs become necessary
- set expectations around uncertainty honestly
- keep the statement short enough to survive a planning meeting

### Close the Plan

- capture blockers, owners, and contingency actions
- note what evidence would trigger replanning
- document the final scope in one place
- keep the artifact usable in the sprint ceremony
- tie the plan back to the roadmap and release window if relevant

## Decision Tests

- the sprint goal is not just a list of tasks
- marginal scope is challenged explicitly
- dependency risk is surfaced
- deferred work is named
- the plan states how it will be revisited if conditions change

## Outputs

- sprint trade-off brief
- must-have versus stretch split
- stakeholder note
- replanning triggers list
- scope protection memo for the sprint lead

## Failure Modes

- optimizing for utilization instead of outcome
- letting every stakeholder keep one extra item
- hiding unresolved dependencies
- pretending that a date erases missing readiness

## Review and Follow-through

- review after sprint planning
- use post-sprint learning to improve future trade-offs
- do not backfill the sprint silently without revisiting intent
- record recurring causes of overcommitment

## Escalate or Stop When

- the sprint goal changes depending on who is speaking
- stretch work quietly becomes committed work
- critical dependencies have no delivery or approval owner
- support, migration, or analytics work is excluded to preserve
  optics

## Worked Scenario

- If the sprint must deliver governed approvals, defer dashboard
  polish before cutting audit telemetry or revocation handling.
- That trade-off protects the outcome and keeps the release gate
  honest.
- The stakeholder note should explain exactly why the scope
  narrowed.
