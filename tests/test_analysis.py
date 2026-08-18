from src.analysis import analyze_reference_ranges, summarize_analysis


def test_hemoglobin_in_range_for_male():
    result = analyze_reference_ranges({"Hemoglobin": 15.0}, "male")
    assert result["Hemoglobin"]["status"] == "normal"


def test_low_hemoglobin_is_flagged():
    result = analyze_reference_ranges({"Hemoglobin": 10.5}, "female")
    assert result["Hemoglobin"]["status"] == "low"


def test_summary_counts_flagged_values():
    analysis = analyze_reference_ranges({"Hemoglobin": 10.5, "WBC": 7.0}, "female")
    assert summarize_analysis(analysis).startswith("1 entered value")
