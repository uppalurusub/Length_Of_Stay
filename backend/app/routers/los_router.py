"""FastAPI routes for LOS prediction."""

from fastapi import APIRouter, HTTPException, status

from app.schemas.request_schema import LengthOfStayPredictionRequest
from app.schemas.response_schema import PredictionResponse
from app.services.los_service import LengthOfStayService

router = APIRouter(
    prefix="/los",
    tags=["Length Of Stay Prediction"],
)

# Instantiate once so model artifacts are loaded during application startup.
service = LengthOfStayService()


@router.post(
    "/predict",
    response_model=PredictionResponse,
    status_code=status.HTTP_200_OK,
    summary="Predict Hospital Length Of Stay",
)
async def predict_length_of_stay(
    request: LengthOfStayPredictionRequest,
) -> PredictionResponse:
    try:
        return service.predict_length_of_stay(request)
    except HTTPException:
        # Do not turn the service's structured error into a string-wrapped 500.
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "Length-of-stay prediction failed",
                "reason": str(exc),
            },
        ) from exc
