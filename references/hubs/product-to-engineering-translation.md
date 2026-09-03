# Product-to-Engineering Translation

Use this hub when product decisions must cross into engineering with enough clarity, constraints, sequencing, and verification to avoid thrash.

## Purpose

This hub turns a product decision into a handoff packet that engineering can challenge, estimate, and implement without inheriting silent ambiguity. It keeps the product boundary clear while leaving technical ownership where it belongs.

## What This Hub Owns

- Engineering handoff packets.
- Scope translation from outcome to buildable work.
- Open-question and dependency signaling.
- Non-functional expectations at the product boundary.
- Challenge prompts that engineering should answer before implementation.
- Closing the loop after engineering review.

## Route Away When

- The real need is architecture ownership or repository design.
- The request is pure product strategy detached from build readiness.
- The work is external launch packaging.
- The artifact would treat technical estimation heuristics as product truth.
- There is no agreed product intent to hand off yet.

## Related Playbooks

- `references/playbooks/engineering-handoff-packet.md`.
- `references/playbooks/prd-quality-review.md`.
- `references/playbooks/release-decision-gate.md`.

## Core Questions

- What must engineering understand in order to challenge or build the work responsibly?
- Which assumptions remain product-owned and which require engineering judgment?
- What non-functional expectations matter to the user outcome?
- What can be staged or reduced to reach a minimum sufficient release?
- Which open question can still alter scope materially?
- What evidence will prove that the handoff succeeded?

## Evidence To Gather

- Approved product intent and scope.
- User workflow and edge-case notes.
- Metric and instrumentation expectations.
- Dependency and rollout assumptions.
- Policy, audit, or permission rules.
- Release and support implications.

## Decision Procedure

### Package the Problem

- State the user problem, evidence, and desired behavior.
- Name the workflow steps and boundary conditions that matter.
- Carry over non-goals so engineering can help protect scope.
- Include metric definitions and instrumentation expectations.
- Show why the work matters in the current portfolio or release context.

### Invite Engineering Challenge

- List the assumptions engineering should test or question.
- Flag feasibility, performance, data, or security questions that may change the plan.
- Mark whether the release can be staged.
- State where product is flexible and where it is not.
- Encourage alternatives that still satisfy the user outcome.

### Prepare Release Logic

- Identify critical acceptance, rollout, and monitoring expectations.
- State reversibility constraints where they matter.
- Note support, migration, or communication implications.
- Carry forward risk-heavy states such as billing, permissions, delegation, or irreversible settings.
- Align on what evidence is needed before launch and after launch.

### Close the Loop

- Confirm what engineering accepted, challenged, or reframed.
- Update the source artifact after handoff instead of leaving the correction in meeting notes only.
- Capture agreed sequencing and remaining unknowns.
- Measure whether the delivered result matched the original outcome intent.
- Reuse the packet structure only when it still fits the kind of work.

## Failure Modes

- Handing off solution sketches with no product logic behind them.
- Treating engineering questions as resistance rather than risk reduction.
- Burying key constraints inside long prose.
- Omitting telemetry, rollout, or support expectations.
- Closing the handoff without revising the product source artifact.
- Pretending product ownership ends once engineering starts.

## Cross-Skill Handoffs

- Engineering owns architecture, technical decomposition, and implementation planning.
- Marketing owns external launch narrative and market-facing materials.
- Product owns clarity of problem, scope, acceptance intent, sequencing, and outcome measurement.
- Governance can preserve the final agreement without replacing the engineering challenge process.

## Expected Outputs

- Engineering handoff packet.
- Product-to-engineering clarification memo.
- Open questions log.
- Non-functional expectations summary.
- Release intent checklist.
- Artifact delta after engineering review.

## Example Prompts

- Turn this PRD into a clean engineering handoff packet.
- Show what engineering still needs before they estimate the work.
- Audit whether our handoff hides product ambiguity.

## Decision Rules

- A handoff is healthy when engineering can challenge the plan without searching through several disconnected artifacts.
- Non-goals matter as much as requirements because they protect the intended slice.
- If the product team cannot explain which metric should move and why, the handoff is not ready.
- Open questions should be labeled by ownership so they do not linger invisibly.
- A staged release path belongs in product scope when it changes the user promise or the risk posture.
- The handoff packet should shrink ambiguity, not increase documentation volume for its own sake.

## Worked Example

- Product wants delegated approvals for absent reviewers.
- A strong handoff packet states the user problem, the trust implications, the permission boundary, the auditability requirement, and the expected success signals.
- It also identifies telemetry expectations, support implications, and which questions engineering should challenge first.
- That packet lets engineering propose safer technical options without losing the product boundary.
- When engineering review changes a core assumption, the product artifact should be revised explicitly.

## What A High-Trust Handoff Makes Explicit

- Which assumptions engineering is expected to challenge.
- What telemetry, rollout, or support evidence product expects after release.
- What can be staged, simplified, or deferred without breaking the intended outcome.
- Which unanswered question would force product and engineering to revisit scope together.
