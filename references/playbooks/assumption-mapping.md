# Assumption Mapping

Expose what must be true about value, usability, viability, and
feasibility before the team spends delivery capacity.

## When To Run It

- a solution concept exists but certainty does not
- cross-functional debate mixes facts and guesses
- leaders want to know what should be tested first
- the team risks doing build-first discovery

## Do Not Run It When

- the request is merely to write requirements for already-proven
  behavior
- assumptions are being turned into secret scoring weights
- the team will not act on the map
- there is no specific concept or decision to examine

## Inputs

- problem statement
- solution concept or option set
- current evidence
- business constraints
- delivery constraints
- decision horizon

## Procedure

### List Assumptions by Class

- capture value, usability, viability, feasibility, adoption, and
  policy assumptions separately
- write each assumption as a testable statement
- avoid vague statements such as users will love this
- note the consequence if false
- link each assumption to a potential decision

### Rank Risk

- estimate consequence and uncertainty separately
- highlight assumptions that could kill the concept
- treat regulatory or permission assumptions as distinct from
  usability assumptions
- identify assumptions already resolved by evidence
- avoid over-weighting easy-to-test assumptions just because they
  are convenient

### Design Tests

- match high-risk assumptions to the cheapest credible evidence
  source
- prefer tests that can disconfirm quickly
- separate research tasks from build tasks
- record what remains unknown after each proposed test
- note any assumptions that require staged implementation to
  learn

### Sequence Learning

- test kill-shot assumptions before optimization questions
- avoid parallel research that answers the same thing twice
- fit the sequence to the real decision deadline
- reserve build work for assumptions that cannot be learned
  another way
- make explicit what the team can safely defer

### Communicate Decisions

- show what is safe to proceed on now
- show what must wait
- turn the map into a visible alignment artifact
- update it after each learning cycle
- retire assumptions once they become evidence-backed

## Decision Tests

- assumptions are written clearly enough to be wrong
- ranking reflects consequence and uncertainty instead of
  politics
- tests are proportionate to the decision stakes
- resolved assumptions are retired
- the map leads to actual sequencing decisions

## Outputs

- ranked assumption map
- test backlog
- governed learning sequence
- alignment memo for stakeholders
- evidence gap escalation list

## Failure Modes

- treating every assumption as equally important
- testing easy assumptions before dangerous ones
- allowing the map to become a workshop artifact only
- hiding policy assumptions inside feasibility language

## Review and Follow-through

- convert the top tests into discovery work
- revise roadmap timing if a critical assumption remains open
- repeat only when a new concept or constraint appears
- capture which assumptions were disproven for future teams

## Escalate or Stop When

- the concept has so many hidden assumptions that the team cannot
  explain the core proposition in one sentence
- high-risk assumptions are repeatedly deferred because they are
  politically uncomfortable
- the map is being used to justify delivery that leadership
  already promised publicly
- nobody is willing to own the next test

## Worked Scenario

- An automated reminder concept assumes approvers ignore tasks
  because they forget, not because they distrust the request.
- Assumption mapping should surface trust, role ambiguity, and
  notification timing as separate risks so the first test does
  not accidentally validate the wrong thing.
- That keeps the learning plan honest.
