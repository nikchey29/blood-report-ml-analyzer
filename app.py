import logging

from flask import Flask, jsonify, render_template, request

from src.analysis import analyze_reference_ranges, build_model_input, summarize_analysis
from src.model import ModelBundle
from src.recommendations import build_educational_notes
from src.reference_data import BLOOD_TESTS
from src.validation import validate_payload

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
model_bundle = ModelBundle()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/enter-report")
def enter_report():
    return render_template("enter_report.html", tests=BLOOD_TESTS)


@app.route("/results")
def results():
    return render_template("results.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():
    payload, error = validate_payload(request.get_json(silent=True))
    if error:
        return jsonify({"error": error}), 400

    gender = payload["gender"]
    age = payload["age"]
    test_results = payload["testResults"]

    reference_analysis = analyze_reference_ranges(test_results, gender)
    model_input = build_model_input(age, gender, test_results, model_bundle.training_columns)
    predictions = model_bundle.predict(model_input)

    response = {
        "gender": gender,
        "age": age,
        "analysis": reference_analysis,
        "ml_predictions": predictions,
        "notes": build_educational_notes(predictions),
        "summary": summarize_analysis(reference_analysis),
        "model_available": model_bundle.available,
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run()
