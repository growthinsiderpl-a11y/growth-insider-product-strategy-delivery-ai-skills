# User Story Validation

Check whether a user story expresses real user value, bounded
scope, and clear readiness for team discussion.

## When To Run It

- stories are being refined for a sprint or release
- an epic must be split into smaller outcomes
- engineering or QA cannot tell what the story is for
- the backlog is accumulating task-shaped work

## Do Not Run It When

- the item is purely a technical maintenance task with no direct
  user story shape
- the team needs acceptance criteria more than story validation
- the story is intentionally just a placeholder and not ready for
  review
- nobody can describe the parent objective

## Inputs

- story statement or fields
- context or parent objective
- non-goals
- dependencies
- known rules
- expected outcome

## Procedure

### Check Structure

- confirm the story identifies actor, need, and outcome
- flag stories that describe implementation tasks instead of user
  value
- check for missing business or user consequence
- mark role ambiguity that would confuse priority
- rewrite only when the structure is the real problem

### Check Size

- ask whether the story can be discussed, built, and reviewed
  within the intended planning slice
- find multiple workflows or rules hiding in one story
- recommend splits by path, permission, rule set, or edge case
- avoid slicing so thin that value disappears
- look for hidden analytics or migration work that may require
  separate treatment

### Check Readiness

- look for missing context that blocks refinement
- surface unresolved dependency or policy questions
- ensure the story traces back to a product objective
- state whether the story is ready, needs split, or needs
  clarification
- record what information should exist before sprint commitment

### Improve Wording

- keep the rewritten version outcome-oriented
- preserve uncertainty instead of inventing false detail
- note required follow-up acceptance criteria
- avoid loading the story with UI or architectural direction
- make sure the wording still fits the parent requirement

### Close the Review

- summarize the minimum changes needed
- record any assumptions used in the review
- tag the story for follow-up if it is not ready
- avoid turning the review into a full PRD rewrite
- link severe problems back to the epic or PRD

## Decision Tests

- user value is visible
- scope is bounded
- readiness gaps are named
- the story still connects to the larger objective
- rewrites do not smuggle in hidden scope

## Outputs

- story validation result
- proposed split list
- rewritten story when helpful
- ready or not-ready recommendation
- dependency and policy question list

## Failure Modes

- approving task statements as user stories
- keeping one story so broad it masks multiple problems
- filling in missing context silently
- using story splitting to hide unclear requirements

## Review and Follow-through

- move to acceptance-criteria validation next
- feed severe issues back into the PRD
- recheck once the split or rewrite is complete
- capture frequent story anti-patterns for backlog hygiene

## Escalate or Stop When

- one story contains several roles with different goals
- the story implies a full workflow but names only one screen
  action
- dependencies outnumber the actual user outcome
- the item is really an implementation task pretending to be a
  story

## Worked Scenario

- Instead of one story that says admins manage delegations and
  notifications and audit history, split the work into delegation
  setup, active-delegation visibility, and history access.
- Each story then supports planning and acceptance review without
  dragging an entire mini-PRD into the sprint.
