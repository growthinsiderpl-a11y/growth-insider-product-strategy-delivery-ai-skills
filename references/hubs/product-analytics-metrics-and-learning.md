# Product Analytics, Metrics, and Learning

Use this hub to define product metrics, interpret behavior trends, expose instrumentation gaps, and build learning loops from evidence.

## Purpose

This hub keeps product measurement tied to decisions. It helps the team define metrics cleanly, interpret behavior with the right segmentation and confidence, and turn data into the next question rather than into dashboard theater.

## What This Hub Owns

- Metric definitions and guardrails.
- Activation, engagement, and retention analysis.
- Cohort interpretation and segmentation logic.
- Learning agendas and review windows.
- Instrumentation gap framing at the product-decision level.
- Data-quality caution in product choices.

## Route Away When

- The request is martech attribution or campaign analytics.
- The main problem is infrastructure observability owned by engineering.
- The work is finance reporting detached from product behavior.
- The team wants a dashboard instead of an interpretation.
- The analysis depends on benchmarks that hide weak instrumentation.

## Related Playbooks

- `references/playbooks/retention-diagnosis.md`.
- `references/playbooks/product-experiment-design.md`.
- `references/playbooks/board-update-narrative.md`.

## Core Questions

- Which metric is actually tied to the current decision?
- What user behavior defines value rather than raw activity?
- Is the trend trustworthy or distorted by data-quality issues?
- Which segment or cohort split changes the interpretation?
- Which leading signal can inform the next review before lagging outcomes move?
- What should the team stop measuring because it does not guide action?

## Evidence To Gather

- Event definitions, owners, and known caveats.
- Cohort tables by signup, activation, or first value date.
- Feature adoption by role, segment, or use case.
- Retention differences by behavior milestone.
- Qualitative context for anomalies or unexplained shifts.
- Instrumentation gaps, logging drift, and broken joins that affect interpretation.

## Decision Procedure

### Define Metrics Clearly

- Write the numerator, denominator, window, and segmentation for every important metric.
- Link each metric to a product question or decision.
- Mark whether the metric is primary, leading, or guardrail.
- Avoid vanity metrics with no behavioral interpretation.
- Assign a data owner and note known reuse caveats.

### Analyze Behavior

- Start from the expected user journey or value loop.
- Locate the drop, stall, or acceleration point.
- Check role, segment, cohort, or tenure splits before trusting the aggregate.
- Compare behavior before and after a product change only when measurement semantics remain stable.
- Capture competing explanations instead of pretending one chart proves causality.

### Run Learning Loops

- Turn anomalies into explicit hypotheses.
- Define the next question before asking for more instrumentation or more dashboards.
- Use cohorts to judge durability, not only short-term activation or usage spikes.
- Document what the team learned and what remains unknown.
- Schedule the next review to match the decision horizon.

### Protect Interpretation Quality

- State confidence limits when samples are small or segments are sparse.
- Surface missing events, inconsistent naming, and unreliable joins.
- Avoid causal claims when several releases or campaigns changed at the same time.
- Separate product outcome metrics from engineering telemetry and operational metrics.
- Keep formulas transparent and reproducible.

## Failure Modes

- Treating every number as equally important.
- Tracking a headline metric with no definition discipline.
- Comparing periods with broken or changed instrumentation.
- Using averages that hide a failing cohort.
- Confusing dashboard freshness with product relevance.
- Treating tool output as a substitute for product interpretation.

## Cross-Skill Handoffs

- Hand acquisition attribution, SEO measurement, and campaign analytics to marketing.
- Hand pipeline implementation, logging mechanics, and data-quality fixes to engineering or data teams.
- Keep product behavior interpretation, metric design, and decision framing here.
- Pull stakeholder communication in only after the product meaning of the data is clear.

## Expected Outputs

- Metric definition sheet.
- Cohort analysis summary.
- Learning memo.
- Instrumentation gap backlog.
- Decision-oriented dashboard specification.
- Review note with explicit limitations.

## Example Prompts

- Define the minimum metric system for onboarding and first value.
- Interpret our drop in weekly active teams after a permissions change.
- Turn our dashboard into a learning plan with clear next questions.

## Decision Rules

- A metric is only useful if someone can act differently because of it.
- Do not use WAU or MAU as a proxy for value unless the product value event really is recurring weekly or monthly activity.
- If instrumentation changed during the review window, label the result as directional unless the break is clearly corrected.
- A cohort or segment split is mandatory whenever the average could hide strategically different behavior.
- When a leading indicator moves before revenue, treat it as an early decision signal, not as proof of business impact.
- If a dashboard needs long verbal explanation every week, the metric set is probably poorly designed.

## Worked Example

- A team sees weekly active teams hold steady while expansion slows and support complaints rise.
- A product analytics review should split activity by segment, role, and workflow depth rather than relying on the stable average.
- That often reveals that broad activity is intact while high-value governed teams are encountering trust or admin friction.
- The right response is then a product learning agenda tied to those segments, not a superficial engagement campaign.
- The final artifact should connect the cohort evidence to a specific roadmap or discovery decision.

## What To Quantify Next

- The first value event that predicts later retention or expansion.
- The instrumentation gap that most distorts interpretation today.
- The cohort or segment split most likely to reveal whether the product is helping the right users.
- The review cadence that matches how quickly the team can actually learn and respond.
