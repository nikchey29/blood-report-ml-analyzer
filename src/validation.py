from __future__ import annotations


def validate_payload(data: dict | None) -> tuple[dict | None, str | None]:
    if not isinstance(data, dict):
        return None, "Request body must be JSON."

    required = {"gender", "age", "testResults"}
    if not required.issubset(data):
        return None, "Missing required fields."

    gender = str(data["gender"]).lower().strip()
    if gender not in {"male", "female"}:
        return None, "Gender must be 'male' or 'female'."

    try:
        age = int(data["age"])
    except (TypeError, ValueError):
        return None, "Age must be a whole number."

    if not 18 <= age <= 120:
        return None, "Age must be between 18 and 120."

    test_results = data["testResults"]
    if not isinstance(test_results, dict) or not test_results:
        return None, "Enter at least one test result."

    cleaned_results = {}
    for key, value in test_results.items():
        if value in (None, ""):
            continue
        try:
            cleaned_results[key] = float(value)
        except (TypeError, ValueError):
            return None, f"Invalid numeric value for {key}."

    if not cleaned_results:
        return None, "Enter at least one numeric test result."

    return {"gender": gender, "age": age, "testResults": cleaned_results}, None
