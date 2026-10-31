
"""Resolve and load the LOS model and its matching fitted preprocessor."""

import logging
from pathlib import Path
from typing import Any, Optional

import joblib

from app.config.settings import settings

logger = settings.get_logger()


class ModelLoader:
    """Load a model and its matching fitted preprocessor."""

    def __init__(
        self,
        model_path: Optional[str | Path] = None,
        preprocessor_path: Optional[str | Path] = None,
    ) -> None:

        self.artifact_dir = Path(settings.artifact_dir)

        # Resolve artifact paths
        self.model_path = (
            Path(model_path)
            if model_path
            else self.artifact_dir / "best_model.pkl"
        )

        self.preprocessor_path = (
            Path(preprocessor_path)
            if preprocessor_path
            else self.artifact_dir / "preprocessor.pkl"
        )

        self.model: Optional[Any] = None
        self.preprocessor: Optional[Any] = None

    def load(self) -> None:
        """Load model and preprocessor artifacts."""

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"LOS model not found: {self.model_path}"
            )

        if not self.preprocessor_path.exists():
            raise FileNotFoundError(
                f"LOS preprocessor not found: "
                f"{self.preprocessor_path}"
            )

        try:
            self.model = joblib.load(self.model_path)

            self.preprocessor = joblib.load(
                self.preprocessor_path
            )

            logger.info(
                "LOS model loaded successfully | model=%s",
                self.model_path
            )

            logger.info(
                "LOS preprocessor loaded successfully | path=%s",
                self.preprocessor_path
            )

        except Exception:
            logger.exception(
                "Failed to load LOS model artifacts"
            )
            raise

    def get_model(self) -> Any:
        """Return the loaded model."""

        if self.model is None:
            self.load()

        return self.model

    def get_preprocessor(self) -> Any:
        """Return the loaded preprocessor."""

        if self.preprocessor is None:
            self.load()

        return self.preprocessor

    def predict(self, data):
        """Transform input features and generate LOS prediction."""

        model = self.get_model()
        preprocessor = self.get_preprocessor()

        transformed = preprocessor.transform(data)

        return model.predict(transformed)
