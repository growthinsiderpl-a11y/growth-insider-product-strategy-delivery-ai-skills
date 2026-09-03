# Product Experiment Design

Design a product experiment with an explicit hypothesis, success
metric, sample logic, instrumentation plan, and interpretation
limits.

## When To Run It

- a product change needs bounded validation
- the team wants to test behavior change before a broad rollout
- competing variants need a fair comparison
- leadership wants evidence stronger than intuition but smaller
  than a full launch

## Do Not Run It When

- the change is too large and confounded to interpret cleanly
- inputs required for sample logic are missing and cannot be
  estimated honestly
- the request is for marketing campaign experimentation
- nobody is prepared to read the result carefully

## Inputs

- hypothesis
- current behavior baseline
- target behavior change
- primary metric
- guardrails
- exposure or traffic limits

## Procedure

### State the Hypothesis

- write the changed behavior, affected segment, and expected
  mechanism
- name the primary metric and review window
- separate the core hypothesis from exploratory observations
- define guardrails before launch
- state what business decision the result could change

### Design the Treatment

- keep the treatment narrow enough to interpret
- avoid simultaneous changes that break attribution
- document eligibility and rollout logic
- record what stays constant across variants
- note any implementation caveat that could bias behavior

### Plan Measurement

- verify event definitions and data joins
- specify sample-size assumptions explicitly
- estimate run time from real traffic
- state what the experiment cannot tell you
- prepare how missing data or exposure imbalance will be handled

### Set Operating Rules

- define launch, pause, and stop conditions
- record who can change or abort the test
- log risk scenarios such as revenue or trust harm
- prepare a readout template before launch
- make it clear how segmentation will be treated

### Interpret Responsibly

- separate observed result from broader product meaning
- note missing power or sample issues
- look for segment differences carefully
- turn the outcome into a next decision, not just a chart
- avoid pretending that statistical output resolves strategic
  trade-offs alone

## Decision Tests

- one primary metric exists
- guardrails are documented
- sample logic uses supplied assumptions
- interpretation limits are stated
- operating rules are written before launch

## Outputs

- experiment brief
- sample-size estimate input sheet
- instrumentation checklist
- readout template
- decision tree for likely outcomes

## Failure Modes

- running too many changes at once
- ignoring guardrail harm because the primary metric improved
- claiming certainty from underpowered results
- letting the experiment answer a different question than the one
  stated

## Review and Follow-through

- schedule a readout date before launch
- feed result into roadmap decisions
- archive assumptions for future comparison
- review whether the treatment should graduate, iterate, or stop

## Escalate or Stop When

- the experiment changes too many variables to interpret
- the primary metric cannot be measured cleanly with existing
  events
- sample-size assumptions are guessed but not labeled as guesses
- guardrail harm is possible yet unmonitored

## Worked Scenario

- To test delegated approvals, change only the delegation setup
  and assignment flow while keeping notifications stable.
- Measure completed approval rate and time to first delegated
  action, while monitoring support tickets and revoked
  delegations as guardrails.
- That yields a usable readout instead of a broad redesign story.
