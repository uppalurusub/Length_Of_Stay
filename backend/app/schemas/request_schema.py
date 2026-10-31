from typing import Optional

from pydantic import AliasChoices, BaseModel, ConfigDict, Field


class LengthOfStayPredictionRequest(BaseModel):
    """Validated request fields for hospital length-of-stay prediction.

    `department` is the canonical training feature. The legacy API field
    `hospital_department` is accepted as an input alias for compatibility.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        extra="forbid",
        json_schema_extra={
            "examples": [
                {
                    "age": 45,
                    "gender": "Male",
                    "admission_type": "Emergency",
                    "primary_diagnosis": "Pneumonia",
                    "comorbidity_count": 2,
                    "previous_admissions": 1,
                    "severity_score": 7.5,
                    "insurance_type": "Private",
                    "smoker": "No",
                    "bmi": 27.4,
                    "department": "Cardiology",
                    "admission_source": "Referral",
                    "discharge_disposition": "Home",
                    "marital_status": "Married",
                    "heart_rate": 82.0,
                    "blood_pressure": 120.0,
                    "temperature": 37.0,
                    "oxygen_saturation": 98.0,
                    "glucose": 105.0,
                    "creatinine": 1.0,
                    "hemoglobin": 13.5,
                }
            ]
        },
    )

    age: int = Field(gt=0, le=120, examples=[45])
    gender: str = Field(min_length=1, examples=["Male"])
    admission_type: str = Field(min_length=1, examples=["Emergency"])
    primary_diagnosis: str = Field(min_length=1, examples=["Pneumonia"])
    comorbidity_count: int = Field(ge=0, examples=[2])
    previous_admissions: int = Field(ge=0, examples=[1])
    severity_score: float = Field(ge=0, examples=[7.5])
    insurance_type: str = Field(min_length=1, examples=["Private"])
    smoker: str = Field(min_length=1, examples=["No"])
    bmi: float = Field(gt=0, examples=[27.4])

    department: Optional[str] = Field(
        ...,
        validation_alias=AliasChoices("department", "hospital_department"),
        examples=["Cardiology"],
    )
    admission_source: Optional[str] = Field(..., examples=["Referral"])
    discharge_disposition: Optional[str] = Field(default="Unknown")
    marital_status: str = Field(min_length=1)

    heart_rate: float
    blood_pressure: float
    temperature: float
    oxygen_saturation: float
    glucose: float
    creatinine: float
    hemoglobin: float
