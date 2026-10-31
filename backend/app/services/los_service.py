import logging
import math
import time
from datetime import datetime, timezone
from typing import Any, Dict

from fastapi import HTTPException

from app.implementations.los_implementation import LengthOfStayImplementation

from app.schemas.request_schema import LengthOfStayPredictionRequest
from app.schemas.response_schema import PredictionResponse

from app.config.settings import settings
logger = settings.get_logger()


class LengthOfStayService:
    """Service layer for hospital length-of-stay inference."""

    def __init__(self) -> None:
        self.impl = LengthOfStayImplementation()

    @staticmethod
    def _track_error_safely(
        request_data: Dict[str, Any],
        error_message: str,
    ) -> None:
        """Track an inference error without masking the original error."""
        try:
            track_prediction_error(
                request_data=request_data,
                error_message=error_message,
            )
        except Exception:
            logger.exception("MLflow error tracking failed")

    @staticmethod
    def _track_prediction_safely(
        request_data: Dict[str, Any],
        prediction_result: Dict[str, Any],
        execution_time: float,
    ) -> None:
        """Track a successful prediction without failing the API if MLflow is down."""
        try:
            track_prediction_request(
                request_data=request_data,
                prediction_result=prediction_result,
                execution_time=execution_time,
            )
        except Exception:
            logger.exception(
                "MLflow inference tracking failed; returning the prediction anyway"
            )

    def predict_length_of_stay(
        self,
        request: LengthOfStayPredictionRequest,
    ) -> PredictionResponse:
        start_time = time.perf_counter()
        request_data = request.model_dump()

        try:
            result = self.impl.predict(request_data)
            execution_time = time.perf_counter() - start_time

            if not isinstance(result, dict):
                raise RuntimeError(
                    "Length-of-stay implementation returned an invalid response; "
                    f"expected dict, received {type(result).__name__}"
                )

            if not result.get("success", False):
                reason = result.get("message") or "Unknown inference error"
                self._track_error_safely(request_data, str(reason))
                raise HTTPException(
                    status_code=500,
                    detail={
                        "message": "Length-of-stay prediction failed",
                        "reason": str(reason),
                    },
                )

            raw_prediction = result.get("predicted_length_of_stay_days")
            if raw_prediction is None:
                reason = "Implementation returned no predicted length-of-stay value"
                self._track_error_safely(request_data, reason)
                raise HTTPException(
                    status_code=500,
                    detail={"message": "Length-of-stay prediction failed", "reason": reason},
                )

            try:
                predicted_days = float(raw_prediction)
            except (TypeError, ValueError) as exc:
                reason = "Prediction value is not numeric"
                self._track_error_safely(request_data, f"{reason}: {raw_prediction!r}")
                raise HTTPException(
                    status_code=500,
                    detail={"message": "Length-of-stay prediction failed", "reason": reason},
                ) from exc

            if not math.isfinite(predicted_days):
                reason = "Prediction value must be finite"
                self._track_error_safely(request_data, f"{reason}: {raw_prediction!r}")
                raise HTTPException(
                    status_code=500,
                    detail={"message": "Length-of-stay prediction failed", "reason": reason},
                )

            # Use the validated numeric value in both tracking and API response.
            normalized_result = {
                **result,
                "success": True,
                "predicted_length_of_stay_days": predicted_days,
            }
            self._track_prediction_safely(
                request_data=request_data,
                prediction_result=normalized_result,
                execution_time=execution_time,
            )

            logger.info(
                "LOS prediction completed in %.4fs; model=%s",
                execution_time,
                result.get("model_name", "unknown"),
            )

            return PredictionResponse(
                success=True,
                predicted_length_of_stay_days=predicted_days,
                model_name=str(result.get("model_name") or "unknown"),
                prediction_timestamp=datetime.now(timezone.utc),
                message=str(result.get("message") or "Prediction generated successfully"),
            )

        except HTTPException:
            # Preserve intentional HTTP status codes and structured details.
            raise
        except Exception as exc:
            execution_time = time.perf_counter() - start_time
            logger.exception("LOS prediction failed after %.4fs", execution_time)
            self._track_error_safely(request_data, str(exc))
            raise HTTPException(
                status_code=500,
                detail={
                    "message": "Length-of-stay prediction failed",
                    "reason": str(exc),
                },
            ) from exc
