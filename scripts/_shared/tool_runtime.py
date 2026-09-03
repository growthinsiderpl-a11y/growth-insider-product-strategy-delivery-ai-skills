#!/usr/bin/env python3
"""Shared deterministic runtime for Growth Insider product tools."""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any


class InputError(ValueError):
    """Raised when supplied data violates an explicit contract."""


def obj(required: list[str], properties: dict[str, Any]) -> dict[str, Any]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": required,
        "additionalProperties": True,
        "properties": properties,
    }


def record(required: list[str], properties: dict[str, Any]) -> dict[str, Any]:
    return {"type": "object", "required": required, "additionalProperties": True, "properties": properties}


TEXT = {"type": "string", "minLength": 1}
NON_NEGATIVE = {"type": "number", "minimum": 0}
BOOLEAN = {"type": "boolean"}

SPECS: dict[str, dict[str, Any]] = {
    "calculate_experiment_sample_size": {
        "description": "Estimate per-variant sample size for a two-variant product experiment.",
        "schema": obj(
            ["baseline_rate", "expected_variant_rate", "confidence_level", "power"],
            {
                "baseline_rate": {"type": "number", "minimum": 0, "maximum": 1},
                "expected_variant_rate": {"type": "number", "minimum": 0, "maximum": 1},
                "confidence_level": {"type": "number", "minimum": 0.8, "maximum": 0.999},
                "power": {"type": "number", "minimum": 0.5, "maximum": 0.999},
                "daily_exposed_users": NON_NEGATIVE,
            },
        ),
        "formulas": [
            "delta = abs(expected_variant_rate - baseline_rate)",
            "pooled = (baseline_rate + expected_variant_rate) / 2",
            "n_per_variant = ((z_alpha * sqrt(2 * pooled * (1 - pooled)) + z_beta * sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2) / delta ** 2",
        ],
    },
    "calculate_product_metrics": {
        "description": "Calculate explicit activation, engagement, retention, and monetization metrics from supplied counts.",
        "schema": obj(
            ["period"],
            {
                "period": record(
                    ["signups", "activated_users", "monthly_active_users", "weekly_active_users", "retained_users", "paying_accounts", "revenue"],
                    {
                        "signups": NON_NEGATIVE,
                        "activated_users": NON_NEGATIVE,
                        "monthly_active_users": NON_NEGATIVE,
                        "weekly_active_users": NON_NEGATIVE,
                        "retained_users": NON_NEGATIVE,
                        "paying_accounts": NON_NEGATIVE,
                        "revenue": NON_NEGATIVE,
                        "starting_accounts": NON_NEGATIVE,
                        "churned_accounts": NON_NEGATIVE,
                    },
                )
            },
        ),
        "formulas": [
            "activation_rate = activated_users / signups",
            "wau_mau_ratio = weekly_active_users / monthly_active_users",
            "retention_rate = retained_users / activated_users",
            "arpa = revenue / paying_accounts",
        ],
    },
    "calculate_retention_cohorts": {
        "description": "Calculate cohort retention tables from retained counts by period.",
        "schema": obj(
            ["cohorts"],
            {
                "cohorts": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(
                        ["cohort", "start_users", "retained_counts"],
                        {
                            "cohort": TEXT,
                            "start_users": NON_NEGATIVE,
                            "retained_counts": {"type": "array", "minItems": 1, "items": NON_NEGATIVE},
                        },
                    ),
                }
            },
        ),
        "formulas": [
            "retention_rate[period] = retained_counts[period] / start_users",
            "average_retention[period] = mean(retention_rate[period] across cohorts)",
        ],
    },
    "evaluate_evidence_rubric": {
        "description": "Check completeness and balance of evidence used in a product decision.",
        "schema": obj(
            ["decision_name", "evidence_items"],
            {
                "decision_name": TEXT,
                "required_classes": {"type": "array", "items": TEXT},
                "evidence_items": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(
                        ["title", "evidence_class", "source_type", "segment", "decision_relevance"],
                        {
                            "title": TEXT,
                            "evidence_class": TEXT,
                            "source_type": TEXT,
                            "segment": TEXT,
                            "decision_relevance": TEXT,
                            "timeframe": TEXT,
                            "metric": TEXT,
                            "limitations": TEXT,
                            "observed_behavior": TEXT,
                        },
                    ),
                },
            },
        ),
        "formulas": [
            "missing_required_class = required_class not represented in evidence_items",
            "item_missing_fields = count of key optional quality fields missing",
            "segment_count = number of unique segments represented",
        ],
    },
    "compare_prioritization_options": {
        "description": "Compare prioritization options using only user-supplied criteria and weights.",
        "schema": obj(
            ["criteria", "options"],
            {
                "criteria": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(["name", "weight"], {"name": TEXT, "weight": NON_NEGATIVE}),
                },
                "options": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(
                        ["name", "scores"],
                        {
                            "name": TEXT,
                            "scores": {"type": "object", "additionalProperties": {"type": "number", "minimum": 0, "maximum": 5}},
                            "notes": TEXT,
                        },
                    ),
                },
            },
        ),
        "formulas": [
            "weighted_score = sum(score[criterion] * weight[criterion])",
            "normalized_score = weighted_score / sum(weights)",
        ],
    },
    "validate_user_story": {
        "description": "Validate whether a user story is outcome-linked, bounded, and refinement-ready.",
        "schema": obj(
            ["story"],
            {
                "story": record(
                    ["actor", "need", "outcome"],
                    {
                        "actor": TEXT,
                        "need": TEXT,
                        "outcome": TEXT,
                        "context": TEXT,
                        "dependencies": {"type": "array", "items": TEXT},
                        "non_goals": {"type": "array", "items": TEXT},
                    },
                )
            },
        ),
        "formulas": [
            "well_formed = actor and need and outcome are non-empty",
            "scope_warning when need includes many conjunctions or step bundles",
            "dependency_count = len(dependencies)",
        ],
    },
    "validate_acceptance_criteria": {
        "description": "Validate whether acceptance criteria are observable, categorized, and complete enough for discussion.",
        "schema": obj(
            ["criteria"],
            {
                "criteria": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(["text", "category"], {"text": TEXT, "category": TEXT}),
                }
            },
        ),
        "formulas": [
            "ambiguous_count = count(criteria containing vague language)",
            "category_coverage = unique categories present",
            "observable_count = count(criteria with checkable action verbs)",
        ],
    },
    "validate_roadmap_consistency": {
        "description": "Check roadmap items for objective alignment, metric coverage, dependencies, and sequencing gaps.",
        "schema": obj(
            ["items"],
            {
                "items": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(
                        ["id", "theme", "quarter", "objective", "metric", "owner"],
                        {
                            "id": TEXT,
                            "theme": TEXT,
                            "quarter": TEXT,
                            "objective": TEXT,
                            "metric": TEXT,
                            "owner": TEXT,
                            "dependencies": {"type": "array", "items": TEXT},
                            "confidence": TEXT,
                        },
                    ),
                }
            },
        ),
        "formulas": [
            "orphan_item when objective missing or blank",
            "missing_metric when metric missing or blank",
            "unknown_dependency when dependency id not found among items",
        ],
    },
    "validate_okr_cascade": {
        "description": "Check whether objectives, key results, and initiatives form a coherent cascade.",
        "schema": obj(
            ["objectives", "key_results", "initiatives"],
            {
                "objectives": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(["id", "name", "owner"], {"id": TEXT, "name": TEXT, "owner": TEXT}),
                },
                "key_results": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(["id", "objective_id", "metric", "target"], {"id": TEXT, "objective_id": TEXT, "metric": TEXT, "target": TEXT, "baseline": TEXT}),
                },
                "initiatives": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(["id", "key_result_id", "name", "owner"], {"id": TEXT, "key_result_id": TEXT, "name": TEXT, "owner": TEXT}),
                },
            },
        ),
        "formulas": [
            "orphan_key_result when objective_id missing from objectives",
            "orphan_initiative when key_result_id missing from key_results",
            "unowned_count = count(items with blank owner)",
        ],
    },
}


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def _validate(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    expected = schema.get("type")
    if expected == "object":
        if not isinstance(value, dict):
            return [f"{path} must be an object"]
        for field in schema.get("required", []):
            if field not in value:
                errors.append(f"{path}.{field} is required")
        for key, subschema in schema.get("properties", {}).items():
            if key in value:
                errors.extend(_validate(value[key], subschema, f"{path}.{key}"))
        additional_schema = schema.get("additionalProperties")
        if isinstance(additional_schema, dict):
            known = set(schema.get("properties", {}).keys())
            for key, item in value.items():
                if key not in known:
                    errors.extend(_validate(item, additional_schema, f"{path}.{key}"))
    elif expected == "array":
        if not isinstance(value, list):
            return [f"{path} must be an array"]
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path} must contain at least {schema.get('minItems', 0)} items")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                errors.extend(_validate(item, item_schema, f"{path}[{index}]"))
    elif expected == "string":
        if not isinstance(value, str) or len(value) < schema.get("minLength", 0):
            return [f"{path} must be a non-empty string"]
    elif expected == "number":
        if not _is_number(value):
            return [f"{path} must be a finite number"]
        numeric = float(value)
        if "minimum" in schema and numeric < schema["minimum"]:
            errors.append(f"{path} must be >= {schema['minimum']}")
        if "maximum" in schema and numeric > schema["maximum"]:
            errors.append(f"{path} must be <= {schema['maximum']}")
    elif expected == "boolean":
        if not isinstance(value, bool):
            return [f"{path} must be a boolean"]
    return errors


def finite(value: Any, name: str, minimum: float | None = None, maximum: float | None = None) -> float:
    if not _is_number(value):
        raise InputError(f"{name} must be a finite number")
    number = float(value)
    if minimum is not None and number < minimum:
        raise InputError(f"{name} must be >= {minimum}")
    if maximum is not None and number > maximum:
        raise InputError(f"{name} must be <= {maximum}")
    return number


def _z_for_probability(probability: float) -> float:
    table = {
        0.80: 0.841621,
        0.85: 1.036433,
        0.90: 1.281552,
        0.95: 1.644854,
        0.975: 1.959964,
        0.99: 2.326348,
        0.995: 2.575829,
    }
    rounded = round(probability, 3)
    if rounded in table:
        return table[rounded]
    raise InputError("supported probability levels: 0.80, 0.85, 0.90, 0.95, 0.975, 0.99, 0.995")


def _ratio(numerator: float, denominator: float) -> float | None:
    return None if denominator <= 0 else numerator / denominator


def calculate(tool_id: str, data: dict[str, Any]) -> dict[str, Any]:
    if tool_id == "calculate_experiment_sample_size":
        p1 = finite(data["baseline_rate"], "baseline_rate", 0, 1)
        p2 = finite(data["expected_variant_rate"], "expected_variant_rate", 0, 1)
        confidence = finite(data["confidence_level"], "confidence_level", 0.8, 0.999)
        power = finite(data["power"], "power", 0.5, 0.999)
        delta = abs(p2 - p1)
        if delta == 0:
            raise InputError("expected_variant_rate must differ from baseline_rate")
        alpha_tail = 1 - ((1 + confidence) / 2)
        z_alpha = _z_for_probability(round(1 - alpha_tail, 3))
        z_beta = _z_for_probability(round(power, 3))
        pooled = (p1 + p2) / 2
        numerator = (z_alpha * math.sqrt(2 * pooled * (1 - pooled)) + z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        n = math.ceil(numerator / (delta ** 2))
        daily_exposed = finite(data.get("daily_exposed_users", 0), "daily_exposed_users", 0)
        estimated_days = None if daily_exposed <= 0 else math.ceil((n * 2) / daily_exposed)
        return {
            "baseline_rate": p1,
            "expected_variant_rate": p2,
            "absolute_lift": delta,
            "sample_size_per_variant": n,
            "total_sample_size": n * 2,
            "estimated_runtime_days": estimated_days,
        }

    if tool_id == "calculate_product_metrics":
        period = data["period"]
        signups = finite(period["signups"], "signups", 0)
        activated = finite(period["activated_users"], "activated_users", 0)
        mau = finite(period["monthly_active_users"], "monthly_active_users", 0)
        wau = finite(period["weekly_active_users"], "weekly_active_users", 0)
        retained = finite(period["retained_users"], "retained_users", 0)
        paying = finite(period["paying_accounts"], "paying_accounts", 0)
        revenue = finite(period["revenue"], "revenue", 0)
        starting = finite(period.get("starting_accounts", 0), "starting_accounts", 0)
        churned = finite(period.get("churned_accounts", 0), "churned_accounts", 0)
        return {
            "activation_rate": _ratio(activated, signups),
            "wau_mau_ratio": _ratio(wau, mau),
            "retention_rate": _ratio(retained, activated),
            "trial_to_paid_rate": _ratio(paying, activated),
            "arpa": _ratio(revenue, paying),
            "logo_churn_rate": _ratio(churned, starting),
        }

    if tool_id == "calculate_retention_cohorts":
        rows = []
        rates_by_period = []
        for cohort in data["cohorts"]:
            start = finite(cohort["start_users"], f"{cohort['cohort']}.start_users", 0)
            retained_counts = [finite(value, f"{cohort['cohort']}.retained_counts[{index}]", 0) for index, value in enumerate(cohort["retained_counts"])]
            rates = [_ratio(value, start) for value in retained_counts]
            rows.append({"cohort": cohort["cohort"], "start_users": start, "retained_counts": retained_counts, "retention_rates": rates})
            rates_by_period.append(rates)
        max_len = max(len(row) for row in rates_by_period)
        average_retention = []
        for index in range(max_len):
            values = [row[index] for row in rates_by_period if index < len(row) and row[index] is not None]
            average_retention.append(None if not values else statistics.mean(values))
        return {"cohorts": rows, "average_retention_by_period": average_retention}

    if tool_id == "evaluate_evidence_rubric":
        required_classes = list(data.get("required_classes") or ["FACT_USER", "FACT_TOOL", "ASSUMPTION"])
        represented = Counter()
        missing_field_items = []
        segments = set()
        for item in data["evidence_items"]:
            represented[item["evidence_class"]] += 1
            segments.add(item["segment"])
            missing = []
            for field in ["timeframe", "metric", "limitations", "observed_behavior"]:
                if not str(item.get(field, "")).strip():
                    missing.append(field)
            if missing:
                missing_field_items.append({"title": item["title"], "missing_fields": missing})
        missing_classes = [item for item in required_classes if represented[item] == 0]
        return {
            "decision_name": data["decision_name"],
            "represented_classes": dict(represented),
            "missing_required_classes": missing_classes,
            "segment_count": len(segments),
            "items_with_missing_quality_fields": missing_field_items,
        }

    if tool_id == "compare_prioritization_options":
        criteria = data["criteria"]
        total_weight = sum(finite(item["weight"], f"criteria[{index}].weight", 0) for index, item in enumerate(criteria))
        if total_weight <= 0:
            raise InputError("sum of weights must be greater than zero")
        criterion_names = [item["name"] for item in criteria]
        results = []
        for option in data["options"]:
            weighted = 0.0
            missing = []
            details = []
            for criterion in criteria:
                name = criterion["name"]
                weight = finite(criterion["weight"], f"criterion weight {name}", 0)
                if name not in option["scores"]:
                    missing.append(name)
                    continue
                score = finite(option["scores"][name], f"{option['name']}.{name}", 0, 5)
                weighted += score * weight
                details.append({"criterion": name, "weight": weight, "score": score, "weighted": score * weight})
            results.append({"name": option["name"], "weighted_score": weighted, "normalized_score": weighted / total_weight, "missing_scores": missing, "details": details})
        results.sort(key=lambda item: item["normalized_score"], reverse=True)
        return {"criteria": criterion_names, "total_weight": total_weight, "ranked_options": results}

    if tool_id == "validate_user_story":
        story = data["story"]
        actor = story["actor"].strip()
        need = story["need"].strip()
        outcome = story["outcome"].strip()
        warnings = []
        if need.lower().count(" and ") >= 2:
            warnings.append("need may bundle multiple behaviors")
        if len(story.get("dependencies", [])) > 3:
            warnings.append("story has many dependencies and may need splitting")
        if len(need.split()) > 35:
            warnings.append("need text is unusually long and may hide scope")
        return {
            "well_formed": bool(actor and need and outcome),
            "story_sentence": f"As {actor}, I need {need}, so that {outcome}.",
            "dependency_count": len(story.get("dependencies", [])),
            "non_goal_count": len(story.get("non_goals", [])),
            "warnings": warnings,
        }

    if tool_id == "validate_acceptance_criteria":
        ambiguous_terms = {"works", "easy", "intuitive", "fast", "appropriate", "properly", "correctly"}
        observable_verbs = {"shows", "displays", "stores", "records", "prevents", "sends", "creates", "updates", "blocks", "allows"}
        categories = Counter()
        ambiguous = []
        observable = 0
        for item in data["criteria"]:
            text = item["text"].strip().lower()
            categories[item["category"]] += 1
            if any(word in text for word in ambiguous_terms):
                ambiguous.append(item["text"])
            if any(word in text for word in observable_verbs):
                observable += 1
        return {"criteria_count": len(data["criteria"]), "observable_count": observable, "category_coverage": dict(categories), "ambiguous_items": ambiguous}

    if tool_id == "validate_roadmap_consistency":
        items = data["items"]
        ids = {item["id"] for item in items}
        orphan_items = []
        missing_metrics = []
        unknown_dependencies = []
        releases = Counter()
        for item in items:
            if not item["objective"].strip():
                orphan_items.append(item["id"])
            if not item["metric"].strip():
                missing_metrics.append(item["id"])
            releases[item["quarter"]] += 1
            for dependency in item.get("dependencies", []):
                if dependency not in ids:
                    unknown_dependencies.append({"item": item["id"], "dependency": dependency})
        overloaded_periods = [{"quarter": quarter, "item_count": count} for quarter, count in releases.items() if count > 4]
        return {"item_count": len(items), "orphan_items": orphan_items, "missing_metrics": missing_metrics, "unknown_dependencies": unknown_dependencies, "overloaded_periods": overloaded_periods}

    if tool_id == "validate_okr_cascade":
        objectives = {item["id"]: item for item in data["objectives"]}
        key_results = {item["id"]: item for item in data["key_results"]}
        orphan_key_results = [item["id"] for item in data["key_results"] if item["objective_id"] not in objectives]
        orphan_initiatives = [item["id"] for item in data["initiatives"] if item["key_result_id"] not in key_results]
        objective_to_kr = Counter(item["objective_id"] for item in data["key_results"])
        initiative_to_kr = Counter(item["key_result_id"] for item in data["initiatives"])
        objectives_without_key_results = [objective_id for objective_id in objectives if objective_to_kr[objective_id] == 0]
        key_results_without_initiatives = [key_result_id for key_result_id in key_results if initiative_to_kr[key_result_id] == 0]
        unowned = [item["id"] for item in data["objectives"] + data["initiatives"] if not item["owner"].strip()]
        return {
            "objective_count": len(objectives),
            "key_result_count": len(key_results),
            "initiative_count": len(data["initiatives"]),
            "objectives_without_key_results": objectives_without_key_results,
            "key_results_without_initiatives": key_results_without_initiatives,
            "orphan_key_results": orphan_key_results,
            "orphan_initiatives": orphan_initiatives,
            "unowned_items": unowned,
        }

    raise InputError(f"Unknown tool: {tool_id}")


def run_tool(tool_id: str) -> int:
    spec = SPECS[tool_id]
    parser = argparse.ArgumentParser(description=spec["description"])
    parser.add_argument("--input", type=Path, help="Path to UTF-8 JSON input")
    parser.add_argument("--json", help="Inline JSON object")
    parser.add_argument("--schema", action="store_true", help="Print JSON Schema and exit")
    args = parser.parse_args()

    if args.schema:
        print(json.dumps(spec["schema"], ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    try:
        if args.input:
            payload = json.loads(args.input.read_text(encoding="utf-8"))
        elif args.json:
            payload = json.loads(args.json)
        elif not sys.stdin.isatty():
            payload = json.load(sys.stdin)
        else:
            raise InputError("provide --input, --json, or JSON on stdin")
        if not isinstance(payload, dict):
            raise InputError("input must be a JSON object")
        errors = _validate(payload, spec["schema"])
        if errors:
            raise InputError(" | ".join(errors))
        result = calculate(tool_id, payload)
        print(json.dumps({"status": "OK", "tool_id": tool_id, "formulas": spec["formulas"], "benchmarks_injected": False, "result": result}, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (InputError, OSError, json.JSONDecodeError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "ERROR", "tool_id": tool_id, "errors": [str(exc)]}, ensure_ascii=False), file=sys.stderr)
        return 2


def entrypoint(tool_id: str) -> None:
    raise SystemExit(run_tool(tool_id))
