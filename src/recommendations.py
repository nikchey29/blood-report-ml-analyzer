from __future__ import annotations

from .recommendation_data import CONDITION_DESCRIPTIONS


def build_educational_notes(predictions: dict) -> list[dict]:
    if predictions == {"Unavailable": 0.0}:
        return [{
            "title": "Model unavailable",
            "items": [
                "The reference-range checks are available, but the serialized model could not be loaded.",
                "Install the pinned dependencies and restart the app before using the model output.",
            ],
        }]

    if not predictions or "Normal" in predictions:
        return [{
            "title": "General note",
            "items": [
                "Use the result as an educational demonstration only.",
                "Reference intervals can differ by laboratory, age, history, and other factors.",
            ],
        }]

    notes = []
    for label, confidence in predictions.items():
        if label in {"Normal", "Unavailable"}:
            continue

        description = CONDITION_DESCRIPTIONS.get(label)
        notes.append({
            "title": label,
            "confidence": confidence,
            "description": description,
            "items": [
                "Treat this label as a model output, not as a diagnosis.",
                "If this were real clinical data, interpretation should be done by a qualified healthcare professional.",
            ],
        })

    return notes or [{
        "title": "Model output",
        "items": ["No high-confidence label from the demo model was returned."],
    }]
