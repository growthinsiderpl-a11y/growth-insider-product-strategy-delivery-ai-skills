# Acceptance Criteria Validation

Check whether acceptance criteria are observable, complete
enough for delivery discussion, and categorized across critical
paths and risks.

## When To Run It

- a story is being prepared for implementation
- QA and engineering need a cleaner definition of done
- a release-critical workflow needs stronger validation detail
- product needs to tighten scope without prescribing code

## Do Not Run It When

- the work is still at concept stage
- criteria are being used to prescribe code architecture
- the user only wants generic boilerplate examples
- there is no parent story or workflow to anchor the review

## Inputs

- acceptance criteria list
- parent story or requirement
- critical workflow
- role or permission rules
- analytics or rollout needs
- risk notes

## Procedure

### Check Observability

- each criterion should describe what can be seen, verified, or
  measured
- flag vague language such as works correctly or is intuitive
- prefer behavior and outcome statements over implementation
  detail
- ensure failure states are explicit when important
- check whether audit or telemetry expectations are stated where
  needed

### Check Coverage

- look for happy path, validation, failure, permission, and data
  capture coverage where relevant
- note if accessibility or auditability must be present
- check whether criteria reflect the actual story boundary
- avoid hidden requirements leaking through comments
- state what important category is still absent

### Check Categorization

- assign or verify categories such as happy_path, validation,
  error_state, telemetry, accessibility, and permissions
- ensure categories are not used performatively but to expose
  gaps
- mark missing categories only when the story truly needs them
- keep categories consistent across the artifact
- surface categories that are overstuffed with too many
  unrelated checks

### Tighten Wording

- rewrite ambiguous criteria into observable language
- split compound criteria that hide multiple outcomes
- preserve open questions instead of guessing policy
- note which criteria likely block implementation readiness
- keep the rewrite short enough to remain readable in backlog
  tools

### Report the Result

- state whether the criteria are ready, partial, or insufficient
- list the highest-risk omissions first
- recommend only the missing additions required for the next
  planning step
- keep the output concise
- show how the product boundary is preserved without dictating
  implementation

## Decision Tests

- criteria are observable
- coverage matches the workflow risk
- categories expose omissions
- implementation detail is not masquerading as acceptance
- the result supports planning rather than adding paperwork

## Outputs

- criteria validation report
- rewritten criteria suggestions
- coverage gap list
- readiness recommendation
- category map for risky workflows

## Failure Modes

- treating acceptance criteria as UI copy notes
- skipping error states for risky workflows
- approving compound criteria that cannot be tested cleanly
- padding the list until nobody reads it

## Review and Follow-through

- attach the review to the story or PRD
- raise policy questions before sprint commitment
- revalidate after major scope changes
- carry missing telemetry or auditability into the handoff
  packet

## Escalate or Stop When

- criteria rely on vague words such as intuitive or works
  correctly
- error states are risky but omitted
- permission rules are implied rather than written
- telemetry or audit expectations matter but are absent

## Worked Scenario

- For delegation setup, criteria should cover valid creation,
  invalid overlap, revocation behavior, audit event logging, and
  permission denial.
- That set gives engineering and QA a shared boundary without
  dictating component structure.
