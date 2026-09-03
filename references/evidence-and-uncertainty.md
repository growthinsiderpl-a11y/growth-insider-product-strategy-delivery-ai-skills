# Evidence and Uncertainty

## Evidence classes

- `FACT_USER`: information stated by the user
- `FACT_FILE`: information observed in a local file or artifact
- `FACT_TOOL`: information produced by a deterministic local script
- `FACT_EXTERNAL`: information sourced from an external system or document and labeled as such
- `CALCULATION`: arithmetic derived from explicit inputs
- `ASSUMPTION`: unstated condition adopted to move forward
- `HYPOTHESIS`: testable explanation that still needs evidence
- `UNKNOWN`: material gap that remains unresolved

## Working rules

- prefer narrower truthful claims over broad confident claims
- name evidence limitations next to the recommendation, not in a footnote
- do not upgrade heuristics into facts
- keep benchmarks clearly labeled and optional
- when data quality is weak, state what decision can still be made safely
- use uncertainty to narrow the next step, not to avoid all action
