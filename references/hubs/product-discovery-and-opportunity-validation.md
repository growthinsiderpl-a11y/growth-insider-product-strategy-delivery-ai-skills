# Product Discovery and Opportunity Validation

Use this hub when the team has candidate problems or solutions but not enough evidence to decide what deserves investment.

## Purpose

This hub turns product uncertainty into a bounded discovery plan, a testable opportunity claim, and a clear recommendation about whether to reject, defer, validate, or move toward delivery planning.

## What This Hub Owns

- Problem framing and opportunity sizing.
- Assumption mapping and evidence gaps.
- Discovery interview design.
- Opportunity-solution reasoning.
- Bounded validation sequences before delivery commitment.
- Decision-ready discovery synthesis.

## Route Away When

- The request is persona generation without behavioral evidence.
- The work is campaign copywriting or channel experimentation.
- The real need is implementation design or repository planning.
- The team wants statistical theater without real evidence.
- The request is broad concepting disconnected from a product question.

## Related Playbooks

- `references/playbooks/opportunity-assessment.md`.
- `references/playbooks/discovery-interview-plan.md`.
- `references/playbooks/assumption-mapping.md`.
- `references/playbooks/product-experiment-design.md`.

## Core Questions

- What user behavior or pain is already observed?
- Which assumption must be true for this opportunity to matter?
- Who experiences the problem often enough to justify attention?
- What evidence would reduce uncertainty fastest?
- What is the cheapest test that could disconfirm the current idea?
- When should discovery stop and delivery planning begin?

## Evidence To Gather

- Interview notes with direct quotes tied to recent behavior.
- Support tickets, lost deals, or churn reasons connected to the same workflow.
- Session recordings, usability observations, or journey friction notes.
- Funnel drops or adoption failures tied to specific moments.
- Prototype, concierge, fake-door, or workflow-shadowing results when appropriate.
- Records of previous failed bets and what they actually taught.

## Decision Procedure

### Write the Opportunity Claim

- State the user, problem, and expected value in plain language.
- Name the decision that will change if the opportunity proves real.
- Remove feature language unless it is necessary to describe the proposed mechanism.
- Record what is still assumed rather than observed.
- Make the opportunity small enough to compare with alternatives.

### Map Assumptions

- Separate value, usability, viability, feasibility, adoption, and policy assumptions.
- Rank assumptions by consequence if false and by current uncertainty.
- Tie each assumption to a decision that would change if it fails.
- Retire assumptions that are already resolved by evidence.
- Expose assumptions that stakeholders are treating as facts without proof.

### Design the Discovery Sequence

- Recruit participants by behavior and workflow context rather than by convenience.
- Choose the smallest method that can answer the question, such as interviews, observation, prototype testing, or a narrow experiment.
- Predefine what would count as disconfirming evidence before collection starts.
- Keep each cycle short enough to synthesize and decide.
- Schedule synthesis immediately after the evidence collection window.

### Judge the Opportunity

- Compare the opportunity against at least one other use of the same capacity.
- Separate problem evidence from enthusiasm about a proposed solution.
- Surface the no-build option explicitly.
- Recommend reject, defer, validate, or move to planning.
- Name the owner, due date, and evidence threshold for the next review.

## Failure Modes

- Running discovery that cannot change a real decision.
- Over-relying on opinions about future behavior.
- Letting solution sketches hide an unproven problem.
- Treating one loud customer as a market proxy.
- Calling activity discovery even when no uncertainty is being reduced.
- Keeping discovery alive after the core decision has already been answered.

## Cross-Skill Handoffs

- Ask marketing to validate message-market fit or channel response after the product opportunity is shaped.
- Ask engineering for feasibility review only after product has clarified the decision and the user value claim.
- Keep the evidence gap, opportunity logic, and recommendation inside the product boundary.
- Route deep instrumentation implementation to engineering after the discovery plan specifies what should be measured.

## Expected Outputs

- Opportunity brief.
- Ranked assumption map.
- Interview or observation plan.
- Evidence log.
- Go, no-go, or not-yet recommendation.
- Discovery sequence tied to a decision date.

## Example Prompts

- Validate whether operations managers actually need delegated approvals or only clearer exception handling.
- Design a discovery cycle for a new trial onboarding idea.
- Assess whether repeated customer complaints represent a scalable opportunity or a local workaround issue.

## Decision Rules

- When discovery is meant to decide whether a problem is worth solving, lead with problem evidence before any solution shape.
- Treat repeated workaround behavior as stronger evidence than stated feature preference.
- If the target segment cannot be reached repeatedly for evidence collection, confidence in the opportunity should remain low.
- Discovery should narrow decisions, not simply generate artifacts.
- A high-consequence assumption deserves an explicit owner and a planned test.
- If a concierge or fake-door test can answer the question credibly, do not jump to full delivery work.

## Worked Example

- An operations SaaS team hears repeated complaints that approval routing breaks during absences.
- Interview planning should recruit admins who recently faced the problem, approvers who ignored or delayed requests, and accounts that solved the issue outside the product.
- The first cycle should test whether the pain is driven by trust, policy ambiguity, notification timing, or missing delegation control.
- Only after those causes are narrowed should the team move to a prototype or limited workflow experiment.
- That sequence protects the roadmap from building a polished solution to the wrong problem.

## What Good Discovery Produces

- A narrower and more accurate problem statement than the team started with.
- At least one disproven assumption or one materially upgraded evidence claim.
- Clearer segment, workflow, and context boundaries for the opportunity.
- A decision recommendation with explicit confidence language and known unknowns.
