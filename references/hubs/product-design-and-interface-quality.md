# Product Design and Interface Quality

Use this hub for product-level design quality decisions, including clarity, hierarchy, interaction trust, workflow quality, and decision criteria for interface changes.

## Purpose

This hub helps the team review an interface as a product decision surface. It focuses on whether the workflow is understandable, trustworthy, and fit for the user job, without collapsing into code-level implementation detail or aesthetic preference alone.

## What This Hub Owns

- Product-level interface quality reviews.
- Workflow clarity and cognitive load diagnosis.
- Trust and risk moments in the product experience.
- Decision criteria for interface changes.
- Trade-offs between simplicity, control, and speed.
- Design review outputs that can guide planning.

## Route Away When

- The real need is component implementation or design-system code.
- The request is animation polish or pixel execution review in code.
- The task is pure brand creative direction.
- The work is deep accessibility remediation detail owned by engineering.
- The main question is front-end architecture rather than product behavior.

## Related Playbooks

- `references/playbooks/journey-mapping-workshop.md`.
- `references/playbooks/acceptance-criteria-validation.md`.
- `references/playbooks/engineering-handoff-packet.md`.

## Core Questions

- What product decision depends on this interface quality review?
- Where does the interface create uncertainty, hesitation, or distrust?
- Which workflow step demands too much memory, interpretation, or policy inference from the user?
- What state transitions are invisible or confusing?
- Which design principle is being violated and what user consequence follows?
- How can the product improve without implying a full redesign?

## Evidence To Gather

- Screen captures, prototypes, or current product flows.
- Task-based usability observations.
- Support complaints about confusion, errors, or trust breakdowns.
- Journey maps that highlight cognitive load or handoff risk.
- Business-risk moments such as permissions, deletion, billing, or irreversible settings.
- Known platform, policy, or product constraints.

## Decision Procedure

### Review the Task Flow

- Walk the task in sequence from the user point of view.
- Identify what the user must notice, remember, decide, and trust at each step.
- Look for weak hierarchy, missing context, or overloaded states.
- Mark risky moments such as destructive actions, billing changes, and permission grants.
- Distinguish information problems from missing-rule problems.

### Assess Design Quality Principles

- Check clarity of purpose at each step.
- Look for system feedback after meaningful actions.
- Verify that defaults and guardrails match the user risk.
- Examine whether the interface explains consequences before commitment.
- Balance speed for experts with safety for occasional or delegated users.

### Recommend Product-Level Changes

- Prioritize product moves such as simplify, split, stage, clarify, or protect.
- Tie each recommendation to the user consequence it addresses.
- State where design quality depends on product policy, data clarity, or workflow rules.
- Preserve unresolved questions rather than hiding them under a visual recommendation.
- Avoid prescribing code architecture.

### Connect to Delivery

- State what should be reflected in requirements, stories, or acceptance criteria.
- Mark where more research is still needed.
- Define a measurement or observation plan after the change.
- Note whether the change affects retention, trust, monetization, or support burden.
- Identify what implementation teams still need to decide later.

## Failure Modes

- Turning a design review into an aesthetic taste debate.
- Jumping straight to implementation detail.
- Recommending redesign without naming the user harm.
- Confusing dense workflows with powerful workflows.
- Ignoring feedback, confirmation, or reversal states.
- Labeling policy or rules problems as generic UX issues.

## Cross-Skill Handoffs

- Engineering owns front-end implementation and deep technical accessibility work.
- Marketing owns landing-page persuasion and campaign design outside the product.
- Product owns the decision criteria and user consequences of the interface choices.
- Requirements and handoff artifacts carry the design decision into delivery.

## Expected Outputs

- Design quality review.
- Workflow simplification proposal.
- Risk-state checklist.
- Decision criteria for redesign.
- Before-and-after review plan.
- Requirements implications summary.

## Example Prompts

- Review this billing workflow for trust and clarity.
- Diagnose why our settings area feels hard to use without jumping to a redesign.
- Turn a vague interface complaint into decision-level design guidance.

## Decision Rules

- A design-quality review should explain the user harm before it explains the proposed change.
- Trust-heavy moments such as permissions, deletion, and payment deserve stronger clarity than low-risk settings.
- When a screen feels complex, decide whether the product is inherently complex or whether the interface is forcing unnecessary interpretation.
- Product design recommendations should change a decision, a requirement, or a review criterion.
- Feedback timing matters as much as feedback wording when users are waiting for confirmation.
- If the same issue appears across several screens, the underlying product rule may need revision rather than isolated polish.

## Worked Example

- An admin approvals page shows pending requests, policy notes, and action controls in one dense view.
- Users report that they hesitate to approve because they cannot tell what risk they are accepting.
- A product-level design review should propose clearer consequence framing, stronger action hierarchy, and cleaner separation between policy explanation and action controls.
- It should not jump straight to component APIs, CSS tokens, or implementation architecture.
- The resulting artifact becomes a requirement for safer approval behavior rather than a vague request to make the page feel better.

## What The Design Review Must Leave Behind

- A clearer rule about what the user should understand before acting in the risky part of the workflow.
- A small set of prioritized design changes tied to trust, speed, or comprehension outcomes.
- A record of which issues are product-rule problems and which truly belong to implementation craft.
- A test or observation plan for checking whether the revised flow actually reduces confusion.
