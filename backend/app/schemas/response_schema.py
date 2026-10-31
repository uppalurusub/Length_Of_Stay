from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PredictionResponse(
    BaseModel
):
    success: bool

    predicted_length_of_stay_days: float

    model_name: str

    prediction_timestamp: datetime

    message: str