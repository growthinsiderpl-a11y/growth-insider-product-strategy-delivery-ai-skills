# Monetization, Pricing, and Retention

Use this hub when the core product decision concerns pricing structure, packaging logic, paywall or upgrade friction, retention drivers, and product-led growth loops.

## Purpose

This hub helps the team decide how the product should earn revenue without weakening trust, misreading retention, or confusing packaging problems with value problems.

## What This Hub Owns

- Packaging and price architecture on the product side.
- In-product upgrade, downgrade, and expansion behavior.
- Retention diagnosis inside the product experience.
- Habit and value-loop reasoning bounded by evidence.
- Commercial guardrails for monetization changes.
- Measurement planning for product-led monetization moves.

## Route Away When

- The request is acquisition pricing, promotions, or campaign offers.
- The analysis is finance-only pricing strategy with no product behavior.
- The work is billing implementation detail owned by engineering.
- The plan depends on manipulative dark patterns.
- The request is generic churn advice with no product diagnosis.

## Related Playbooks

- `references/playbooks/packaging-and-monetization-design.md`.
- `references/playbooks/retention-diagnosis.md`.
- `references/playbooks/product-experiment-design.md`.

## Core Questions

- What user behavior indicates willingness to pay, expand, or stay?
- Is the issue primarily pricing, packaging, timing, or trust?
- What value moments are missing before the product asks for payment or upgrade?
- Which retention loss is about product value and which is about lifecycle or commercial handling?
- What segmentation matters for packaging and retention decisions?
- How should monetization changes be measured safely?

## Evidence To Gather

- Conversion to paid by segment, entry path, and tenure.
- Downgrade, churn, and upgrade reasons.
- Feature adoption relative to plan boundaries.
- Retention curves around key value moments.
- Support friction tied to billing, packaging, or trust confusion.
- Qualitative evidence of willingness to pay, hesitation, or fairness concerns.

## Decision Procedure

### Diagnose the Real Monetization Problem

- Separate pricing, packaging, timing, and trust issues.
- Check whether users hit meaningful value before the paywall, upgrade gate, or renewal decision.
- Compare actual usage clusters with current plan boundaries.
- State the business goal explicitly, such as conversion, retention, expansion, or simplicity.
- Note whether the apparent monetization problem is actually weak setup, weak value proof, or weak trust.

### Design Option Sets

- Compare at least two credible packaging or flow options.
- Show trade-offs across simplicity, upsell potential, fairness, support burden, and trust.
- Preserve reversible experiments where possible.
- Avoid inflated forecast certainty or hidden ranking formulas.
- Document the customer-facing implications clearly.

### Improve Retention Where It Matters

- Identify where the value loop breaks for the target segment.
- Check whether activation, collaboration, trust, or repeated-use conditions are missing.
- Tie interventions to a specific user behavior rather than to a generic desire for engagement.
- Separate product retention work from lifecycle messaging that belongs to marketing.
- Protect the experience from manipulative monetization tactics.

### Measure and Review

- Set a primary conversion or retention metric plus guardrails.
- Segment results by plan, use case, tenure, and customer type when relevant.
- Track support, trust, and downgrade side effects.
- Define a review window before broad rollout.
- State what would make the team revert, narrow, or redesign the change.

## Failure Modes

- Treating price as the answer to a value problem.
- Copying competitor packaging without evidence.
- Using dark patterns to simulate monetization gains.
- Ignoring plan complexity costs.
- Calling churn a retention problem when users never reached value.
- Evaluating a packaging change only through top-line revenue.

## Cross-Skill Handoffs

- Marketing owns promotional offers, acquisition pricing, and external messaging.
- Engineering owns billing system implementation and payment mechanics.
- Product owns packaging logic, product-side conversion behavior, retention diagnosis, and rollout guardrails.
- Stakeholder communication should explain both revenue consequences and customer-risk consequences.

## Expected Outputs

- Packaging options memo.
- Product-led retention diagnosis.
- Upgrade or paywall flow review.
- Timing recommendation for monetization asks.
- Measurement plan for monetization changes.
- Guardrail list for rollout.

## Example Prompts

- Diagnose why users start trials but rarely upgrade.
- Design packaging for teams that begin small and expand into governance needs.
- Assess whether our retention drop reflects weak value loops or pricing friction.

## Decision Rules

- If customers do not reach a repeatable value moment, a pricing change will not fix the core problem.
- Packaging should reflect meaningful differences in use case, risk, or value, not arbitrary differentiation.
- A retention intervention belongs in product scope when the underlying break is inside the workflow or value loop.
- Guardrails for monetization changes should include trust, support load, and downgrade behavior.
- When a plan boundary creates manual workarounds, the packaging model may be fighting real product value.
- Do not call a monetization improvement healthy if it lifts short-term conversion while damaging trust or retention.

## Worked Example

- A team notices that smaller accounts start trials but rarely upgrade, while governed teams expand after trust and audit concerns are resolved.
- The product response may be to improve plan clarity, time the upgrade ask later, and package governance depth more clearly.
- At the same time, a packaging review might separate lightweight exploration from governed operational use without punishing the behavior that predicts retention.
- That kind of change should be measured through conversion, retention, and support trust signals together.
- A narrow but honest monetization artifact therefore recommends value-aligned packaging, not a louder paywall.

## What A Safe Monetization Recommendation Contains

- The specific value signal that makes payment, upgrade, or expansion feel earned.
- The segment-specific risk that could make a pricing or packaging change backfire.
- The guardrail signals that protect trust, support load, and long-term retention.
- The condition under which the team should reverse or redesign the monetization move.
