from __future__ import annotations

import logging
import os
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

LOGGER = logging.getLogger(__name__)
ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "models"
DEFAULT_THRESHOLD = 0.90


class ModelBundle:
    def __init__(self, model_dir: Path = MODEL_DIR) -> None:
        self.model = None
        self.label_binarizer = None
        self.imputer = None
        self.training_columns = None
        self.load_error = None
        self._load(model_dir)

    @property
    def available(self) -> bool:
        return all(
            item is not None
            for item in (
                self.model,
                self.label_binarizer,
                self.imputer,
                self.training_columns,
            )
        )

    def _load(self, model_dir: Path) -> None:
        try:
            self.model = joblib.load(model_dir / "blood_report_model.pkl")
            self.label_binarizer = joblib.load(model_dir / "label_binarizer.pkl")
            self.imputer = joblib.load(model_dir / "imputer.pkl")
            self.training_columns = joblib.load(model_dir / "training_columns.pkl")
        except Exception as exc:
            self.load_error = str(exc)
            LOGGER.warning("Model artifacts could not be loaded: %s", exc)

    def predict(self, patient_data: dict, threshold: float | None = None) -> dict:
        if not self.available:
            return {"Unavailable": 0.0}

        threshold = threshold if threshold is not None else _prediction_threshold()
        numeric_columns = [
            column for column in self.training_columns if not column.startswith("Sex_")
        ]

        numeric_values = {
            column: patient_data.get(column, np.nan) for column in numeric_columns
        }
        patient_df = pd.DataFrame([numeric_values], columns=numeric_columns)
        patient_df[numeric_columns] = self.imputer.transform(patient_df[numeric_columns])

        sex = str(patient_data.get("Sex", "")).lower()
        patient_df["Sex_female"] = int(sex == "female")
        patient_df["Sex_male"] = int(sex == "male")

        for column in self.training_columns:
            if column not in patient_df.columns:
                patient_df[column] = 0
        patient_df = patient_df[self.training_columns]

        probabilities = self.model.predict_proba(patient_df)
        predictions = {}
        for index, label in enumerate(self.label_binarizer.classes_):
            probability = probabilities[index][0][1]
            if probability >= threshold:
                predictions[label] = round(float(probability) * 100, 2)

        return predictions or {"Normal": 100.0}


def _prediction_threshold() -> float:
    raw_value = os.getenv("ML_PREDICTION_THRESHOLD", str(DEFAULT_THRESHOLD))
    try:
        value = float(raw_value)
    except ValueError:
        return DEFAULT_THRESHOLD
    return value if 0 <= value <= 1 else DEFAULT_THRESHOLD
