from __future__ import annotations

from .reference_data import BLOOD_TESTS


def analyze_reference_ranges(test_results: dict, gender: str) -> dict:
    analysis = {}

    for test_key, raw_value in test_results.items():
        test_info = BLOOD_TESTS.get(test_key)
        if test_info is None or raw_value is None:
            continue

        value = float(raw_value)
        ranges = test_info["ranges"]
        reference_range = ranges.get(gender, ranges) if isinstance(ranges, dict) else ranges

        if not isinstance(reference_range, dict) or "min" not in reference_range or "max" not in reference_range:
            continue

        status = "normal"
        context = None
        symptoms = None

        if value < reference_range["min"]:
            status = "low"
            context = test_info.get("low", {}).get("condition")
            symptoms = test_info.get("low", {}).get("symptoms")
        elif value > reference_range["max"]:
            status = "high"
            context = test_info.get("high", {}).get("condition")
            symptoms = test_info.get("high", {}).get("symptoms")

        analysis[test_key] = {
            "name": test_info["name"],
            "value": value,
            "status": status,
            "units": test_info["units"],
            "reference_range": f'{reference_range["min"]}-{reference_range["max"]}',
            "context": context,
            "symptoms": symptoms,
        }

    return analysis


def build_model_input(age: int, gender: str, test_results: dict, training_columns: list[str] | None) -> dict:
    model_input = {"Age": age, "Sex": gender}
    if not training_columns:
        return model_input

    for column in training_columns:
        if column in test_results:
            model_input[column] = test_results[column]
    return model_input


def summarize_analysis(analysis: dict) -> str:
    flagged = [result for result in analysis.values() if result["status"] != "normal"]
    if not flagged:
        return "All entered values fall within the reference ranges used by this demo."

    return f"{len(flagged)} entered value(s) fall outside the reference ranges used by this demo."
