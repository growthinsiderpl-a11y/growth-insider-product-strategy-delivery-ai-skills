# UX Research and Customer Journeys

Use this hub for qualitative research planning, journey mapping, usability diagnosis, mental-model framing, and customer-context synthesis that inform product choices.

## Purpose

This hub helps product teams understand how users move through a workflow, where the real friction sits, how trust breaks down, and which research method can reduce uncertainty before design or delivery work grows.

## What This Hub Owns

- Research plans and interview structures.
- Journey mapping and service blueprint thinking.
- Usability and workflow friction framing.
- Mental models, triggers, and context of use.
- Research synthesis tied to product decisions.
- Translation of qualitative evidence into next actions.

## Route Away When

- The real need is pixel-perfect implementation guidance.
- The request is a front-end code audit or design-system implementation task.
- The work is campaign message testing for acquisition.
- The team wants personas as a substitute for evidence.
- The request is visual brand direction disconnected from product use.

## Related Playbooks

- `references/playbooks/discovery-interview-plan.md`.
- `references/playbooks/journey-mapping-workshop.md`.
- `references/playbooks/opportunity-assessment.md`.

## Core Questions

- Where in the customer journey does the important friction happen?
- What trigger starts the journey?
- Which handoff between people, systems, or moments is creating the breakdown?
- What does the user think is happening versus what the product or organization is actually doing?
- Which evidence source can capture that mismatch best?
- How will this research change a concrete decision?

## Evidence To Gather

- Interviews grounded in recent behavior.
- Journey maps with blockers, workarounds, and emotional load.
- Usability observations from real tasks.
- Support, onboarding, or customer-success transcripts.
- Screen recordings, workflow notes, or service handoff details.
- Segment-specific context such as device, role, risk exposure, and collaboration model.

## Decision Procedure

### Plan Research

- Tie the research plan to a decision and a named audience.
- Choose the method by evidence need, such as interview, usability session, observation, or workshop.
- Recruit by behavior and workflow context rather than by demographics alone.
- Write neutral prompts that recover real sequence, stakes, and workarounds.
- State what the chosen method cannot answer.

### Map the Journey

- Start from the triggering event, not from the first screen the team happens to control.
- Show the stages, actors, tools, and moments of delay or uncertainty.
- Mark trust-heavy steps, risk-heavy steps, and handoffs that create confusion.
- Separate the current-state journey from any proposed future-state concept.
- Capture backstage dependencies when they materially shape the user experience.

### Synthesize Findings

- Cluster evidence by repeating problem pattern and consequence.
- Link friction to product decisions such as onboarding, permissions, delegation, or support design.
- Preserve contradictions and outliers instead of flattening them away.
- Convert observations into opportunity statements or requirement implications.
- Keep evidence traceable to real sessions or artifacts.

### Close the Loop

- Decide what to change, test, defer, or leave alone.
- State what the research still did not answer.
- Share findings in a form that product, design, and engineering can use.
- Avoid turning the output into a long research novel.
- Schedule follow-up only if another decision remains open.

## Failure Modes

- Running UX research after the decision is already locked.
- Producing generic personas instead of journey evidence.
- Ignoring environmental context such as role, device, timing, or organizational constraints.
- Mapping desired future flows without grounding in current reality.
- Treating usability complaints as isolated when they share the same root cause.
- Presenting qualitative evidence as unquestionable truth rather than as observable input.

## Cross-Skill Handoffs

- Send interface implementation depth and code-level remediation to engineering.
- Send acquisition messaging experiments to marketing.
- Keep customer context, journey evidence, and decision-level synthesis here.
- Bring product design review in after journey evidence makes the design problem concrete.

## Expected Outputs

- Research plan.
- Journey map workshop plan.
- Usability synthesis.
- Opportunity themes.
- Decision memo grounded in customer context.
- Evidence trace with direct examples.

## Example Prompts

- Plan a journey mapping workshop for activation drop-off.
- Design usability research for a complex admin workflow.
- Translate scattered customer feedback into a coherent journey diagnosis.

## Decision Rules

- A journey map should start from a trigger and end with an outcome or abandonment state.
- Research quotes matter most when paired with the exact behavior or consequence they illuminate.
- If stakeholders want personas before they can describe the actual workflow, the evidence model is still weak.
- A journey workshop is valuable when it resolves a real question, not when it merely creates a mural.
- Usability findings are stronger when they preserve context, sequence, and user stakes.
- Future-state mapping must remain clearly separated from current-state evidence.

## Worked Example

- A team believes onboarding fails because the setup wizard is too long.
- Journey evidence may instead show that the real break happens after invite receipt, when delegated approvers do not understand why the request is safe.
- That changes the product question from form simplification to trust, role clarity, and cross-user workflow design.
- The journey artifact should therefore include the invite, the off-screen coordination, and the first risky decision point.
- Without that fidelity, the team would optimize the wrong part of the journey.

## What A Durable Journey Artifact Captures

- The moment the user recognizes the job and the moments where risk or uncertainty intensifies.
- The workaround or avoidance behavior that proves the current flow is failing.
- The evidence source for each important claim so future teams can revisit the reasoning.
- The decision or backlog consequence created by the map.
