export interface FormFieldConfig {
  name: string;
  label: string;
  type: "text" | "number" | "select";
  options?: string[];
}

export interface FormSectionConfig {
  title: string;
  fields: FormFieldConfig[];
}

export const losFormConfig: FormSectionConfig[] = [
  {
    title: "Patient Information",
    fields: [
      { name: "age", label: "Age", type: "number" },
      {
        name: "gender",
        label: "Gender",
        type: "select",
        options: ["Male", "Female"],
      },
      {
        name: "marital_status",
        label: "Marital Status",
        type: "select",
        options: ["Single", "Married"],
      },
      { name: "bmi", label: "BMI", type: "number" },
      {
        name: "smoker",
        label: "Smoker",
        type: "select",
        options: ["Yes", "No"],
      },
      {
        name: "comorbidity_count",
        label: "Comorbidity Count",
        type: "number",
      },
    ],
  },

  {
    title: "Admission Information",
    fields: [
      {
        name: "admission_type",
        label: "Admission Type",
        type: "select",
        options: ["Emergency", "Elective", "Urgent"],
      },

      {
        name: "admission_source",
        label: "Admission Source",
        type: "select",
        options: ["Referral", "Transfer", "Walk-In"],
      },

      {
        name: "hospital_department",
        label: "Department",
        type: "select",
        options: [
          "Cardiology",
          "Neurology",
          "ICU",
          "Orthopedics",
        ],
      },

      {
        name: "insurance_type",
        label: "Insurance",
        type: "select",
        options: [
          "Private",
          "Government",
          "Self Pay",
        ],
      },

      {
        name: "primary_diagnosis",
        label: "Diagnosis",
        type: "text",
      },

      {
        name: "discharge_disposition",
        label: "Discharge",
        type: "select",
        options: [
          "Home",
          "Transferred",
          "Expired",
        ],
      },

      {
        name: "previous_admissions",
        label: "Previous Admissions",
        type: "number",
      },
    ],
  },

  {
    title: "Clinical Measurements",
    fields: [
      {
        name: "severity_score",
        label: "Severity Score",
        type: "number",
      },
      {
        name: "blood_pressure",
        label: "Blood Pressure",
        type: "number",
      },
      {
        name: "temperature",
        label: "Temperature",
        type: "number",
      },
      {
        name: "heart_rate",
        label: "Heart Rate",
        type: "number",
      },
      {
        name: "oxygen_saturation",
        label: "Oxygen Saturation",
        type: "number",
      },
    ],
  },

  {
    title: "Laboratory Values",
    fields: [
      {
        name: "glucose",
        label: "Glucose",
        type: "number",
      },

      {
        name: "hemoglobin",
        label: "Hemoglobin",
        type: "number",
      },

      {
        name: "creatinine",
        label: "Creatinine",
        type: "number",
      },
    ],
  },
];