// src/models/LengthOfStayRequest.ts

export interface LengthOfStayRequest {
  admission_source: string;
  admission_type: string;

  age: number;
  bmi: number;
  comorbidity_count: number;

  discharge_disposition: string;
  gender: string;
  hospital_department: string;
  insurance_type: string;

  previous_admissions: number;
  primary_diagnosis: string;

  severity_score: number;
  smoker: string;

  glucose: number;
  marital_status: string;
  oxygen_saturation: number;

  hemoglobin: number;
  creatinine: number;
  blood_pressure: number;

  temperature: number;
  heart_rate: number;
}