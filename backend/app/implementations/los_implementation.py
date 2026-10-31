"""Inference implementation for hospital length-of-stay prediction."""

import logging
import time
from typing import Any, Dict

import numpy as np
import pandas as pd

from app.config.settings import settings
logger = settings.get_logger()

from ml.data.model_loader import ModelLoader
from ml.data.preprocessing import DataPreprocessor

class LengthOfStayImplementation:
    """Prepare request features and run the fitted LOS model."""

    def __init__(self) -> None:
        self.loader = ModelLoader()
        self.model = self.loader.get_model()
        self.preprocessor = self.loader.get_preprocessor()

        # The persisted artifact is a fitted ColumnTransformer, not the
        # DataPreprocessor wrapper. Feature engineering must happen first.
        self.feature_engineer = DataPreprocessor()

    def predict(self, patient_data: Dict[str, Any]) -> Dict[str, Any]:
        started = time.perf_counter()

        try:
            input_df = pd.DataFrame([patient_data])

            # Accept both API and training column names.
            if (
                "hospital_department" in input_df.columns
                and "department" not in input_df.columns
            ):
                input_df = input_df.rename(
                    columns={"hospital_department": "department"}
                )

            # These features were created before fitting the saved transformer.
            input_df = self.feature_engineer.feature_engineering(input_df)

            expected_columns = getattr(
                self.preprocessor, "feature_names_in_", None
            )
            if expected_columns is not None:
                expected_columns = list(expected_columns)
                missing = [
                    column for column in expected_columns
                    if column not in input_df.columns
                ]
                if missing:
                    raise ValueError(
                        "Input is missing model features after feature engineering: "
                        f"{missing}. Check request-to-training feature mapping."
                    )

                # Ignore API fields that were not model features and preserve
                # the exact column order used to fit the transformer.
                input_df = input_df.loc[:, expected_columns]

            logger.debug("LOS model artifact: %s", self.loader.model_path)
            logger.debug("LOS preprocessor artifact: %s", self.loader.preprocessor_path)
            logger.debug("LOS features sent to preprocessor: %s", input_df.columns.tolist())

            transformed = self.preprocessor.transform(input_df)

            # Some estimators were fitted on a DataFrame carrying generated
            # feature names. Restore those names when the fitted model exposes
            # them, avoiding feature-name warnings and detecting mismatches.
            model_feature_names = getattr(self.model, "feature_names_in_", None)
            if model_feature_names is not None:
                model_feature_names = list(model_feature_names)
                if len(model_feature_names) != transformed.shape[1]:
                    raise ValueError(
                        "Transformed feature count does not match the model: "
                        f"{transformed.shape[1]} transformed vs "
                        f"{len(model_feature_names)} expected."
                    )
                transformed = pd.DataFrame(
                    transformed,
                    columns=model_feature_names,
                    index=input_df.index,
                )

            prediction = float(self.model.predict(transformed)[0])

            if not np.isfinite(prediction):
                raise ValueError(f"Model returned a non-finite prediction: {prediction}")

            return {
                "success": True,
                "predicted_length_of_stay_days": round(max(0.0, prediction), 2),
                "model_name": type(self.model).__name__,
                "execution_time_seconds": round(time.perf_counter() - started, 4),
                "message": "Prediction generated successfully",
            }

        except Exception as exc:
            logger.exception("Length-of-stay inference failed")
            return {
                "success": False,
                "predicted_length_of_stay_days": None,
                "model_name": type(self.model).__name__,
                "execution_time_seconds": round(time.perf_counter() - started, 4),
                "message": str(exc),
            }
