# Atlassian and Jira Mutation Confirmation

Define a safe, explicit confirmation workflow before any AI-
assisted action mutates Jira or Atlassian data, workflow,
fields, automations, or permissions.

## When To Run It

- an agent or teammate proposes changing Jira configuration or
  issue data
- planning-system source of truth could be altered
- the blast radius of an admin action is unclear
- product operations needs an approval-safe workflow

## Do Not Run It When

- the action is read-only reporting
- the user only needs local drafting with no external side
  effect
- the task belongs to engineering systems with no product-
  governance consequence
- nobody can name the environment or scope of the requested
  change

## Inputs

- requested action
- target project or config surface
- actor
- environment
- rollback path
- reason for change

## Procedure

### Classify the Action

- mark it as READ, CALCULATE, DRAFT, MUTATE_LOCAL, or
  EXTERNAL_SIDE_EFFECT
- treat Jira or Atlassian changes as EXTERNAL_SIDE_EFFECT
  unless proven otherwise
- note whether issue data, workflow, field schemes,
  permissions, or automations are affected
- capture environment such as sandbox or production
- record whether the change touches a source-of-truth artifact

### Draft Before Mutate

- write the intended change in human-readable language
- list entities affected and expected result
- state why the change is necessary
- estimate blast radius and who must review
- show the exact thing the confirmer is being asked to approve

### Require Explicit Confirmation

- obtain user confirmation in the same thread or documented
  workflow before execution
- repeat the exact mutation scope back to the confirmer
- do not infer consent from general enthusiasm
- capture the confirmation timestamp and actor
- state what remains out of scope even after approval

### Prepare Reversibility

- document rollback or restore steps
- prefer sandbox validation first
- note whether backups or exports are needed
- record irreversible elements clearly
- state what evidence would indicate the change had unintended
  impact

### Close the Loop

- log what changed
- capture any unexpected result
- update governance artifacts if the source of truth changed
- review whether future mutations need a better guardrail
- store the final approval record with the outcome

## Decision Tests

- the action is classified
- a draft exists before execution
- confirmation is explicit
- rollback thinking is documented
- scope is specific enough to approve or reject

## Outputs

- mutation confirmation draft
- blast-radius note
- approval checklist
- post-change review prompt
- approval record template

## Failure Modes

- treating admin changes as harmless
- mutating live workflow from an implied request
- forgetting rollback on structural changes
- mixing read-only analysis with live mutation steps in one
  approval

## Review and Follow-through

- store the final approved change record
- tighten permissions if repeated risky requests appear
- teach teams the side-effect classes consistently
- reuse the workflow for future planning-system changes

## Escalate or Stop When

- the requested mutation scope is unclear
- no rollback or export path exists for a structural change
- shared workflows or field schemes could affect other teams
- approval is implied rather than explicit

## Worked Scenario

- Before bulk-updating workflow statuses or field rules, draft
  the exact projects, entities, and expected post-change state.
- Only after explicit confirmation should any live mutation be
  considered, and only with the blast radius documented.
