from src.validation import validate_payload


def test_valid_payload():
    payload, error = validate_payload({
        "gender": "female",
        "age": 30,
        "testResults": {"Hemoglobin": 13.2},
    })
    assert error is None
    assert payload["age"] == 30


def test_rejects_empty_results():
    payload, error = validate_payload({"gender": "male", "age": 40, "testResults": {}})
    assert payload is None
    assert error == "Enter at least one test result."
