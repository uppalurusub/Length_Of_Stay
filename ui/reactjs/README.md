# 🏥 Hospital Length of Stay Prediction - React Frontend

A modern **React + TypeScript** web application that provides an intuitive user interface for predicting a patient's **Hospital Length of Stay (LOS)** using a Machine Learning model exposed through a FastAPI REST API.

The application collects patient demographics, admission details, clinical measurements, and laboratory values, sends them to the prediction service, and displays the predicted hospital stay along with model information.

---

# Features

- Modern React + TypeScript architecture
- Material UI (MUI) responsive user interface
- Patient information entry form
- Admission information capture
- Clinical measurements
- Laboratory values
- REST API integration using Axios
- Beautiful prediction result dashboard
- Responsive design for desktop and mobile
- Clean component-based architecture
- Easy API endpoint configuration

---

# Technology Stack

| Technology | Version |
|------------|----------|
| React | 18+ |
| TypeScript | 5+ |
| Material UI | 7+ |
| Axios | Latest |
| Vite | Latest |
| CSS3 | Yes |

---

# Project Structure

```

src/
│
├── api/
│ └── losApi.ts
│
├── components/
│ ├── LOSForm.tsx
│ ├── PredictionResult.tsx
│ └── FormField.tsx
│
├── config/
│ └── losFormConfig.ts
│
├── models/
│ └── LengthOfStayRequest.ts
│
├── pages/
│ └── PredictionPage.tsx
│
├── styles/
│ ├── global.css
│ ├── LOSForm.css
│ └── PredictionResult.css
│
├── App.tsx
└── main.tsx

```

---

# Application Workflow

```

User
│
▼

Enter Patient Details

│

▼

LOS Form

│

▼

Axios API Call

│

▼

FastAPI Backend

│

▼

Machine Learning Model

│

▼

Prediction Response

│

▼

Prediction Dashboard

```

---

# Input Parameters

## Patient Information

- Age
- Gender
- Marital Status
- BMI
- Smoker
- Comorbidity Count

---

## Admission Information

- Admission Type
- Admission Source
- Hospital Department
- Insurance Type
- Primary Diagnosis
- Discharge Disposition
- Previous Admissions

---

## Clinical Measurements

- Severity Score
- Blood Pressure
- Temperature
- Heart Rate
- Oxygen Saturation

---

## Laboratory Values

- Glucose
- Hemoglobin
- Creatinine

---

# Prediction API

## Endpoint

```

POST /los/predict

```

Base URL

```

http://localhost:8000

```

Configured inside

```

src/api/losApi.ts

```

---

# Sample Request

```json
{
  "admission_source": "Referral",
  "admission_type": "Emergency",
  "age": 45,
  "bmi": 27.4,
  "comorbidity_count": 2,
  "discharge_disposition": "Home",
  "gender": "Male",
  "hospital_department": "Cardiology",
  "insurance_type": "Private",
  "previous_admissions": 1,
  "primary_diagnosis": "Pneumonia",
  "severity_score": 7.5,
  "smoker": "No",
  "glucose": 190,
  "marital_status": "Married",
  "oxygen_saturation": 96,
  "hemoglobin": 12.7,
  "creatinine": 2.86,
  "blood_pressure": 160,
  "temperature": 98,
  "heart_rate": 99
}
```

---

# Sample Response

```json
{
  "message": "Prediction completed successfully.",
  "predicted_length_of_stay_days": 6.8,
  "model_name": "XGBoost Regressor",
  "prediction_timestamp": "2026-07-16T10:20:55"
}
```

---

# User Interface

The application consists of two major sections.

## Patient Input Form

Collects

- Demographics
- Admission Details
- Clinical Information
- Laboratory Results

---

## Prediction Result

Displays

- Predicted Length of Stay
- Model Name
- Prediction Timestamp
- Prediction Status
- Success Message

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
```

---

## Install Dependencies

```bash
npm install
```

---

## Start Development Server

```bash
npm run dev
```

---

## Build Production

```bash
npm run build
```

---

## Preview Production Build

```bash
npm run preview
```

---

# Required Backend

The frontend expects a FastAPI backend running on

```
http://localhost:8000
```

Example endpoint

```
POST /los/predict
```

If the backend runs on another server, update

```
src/api/losApi.ts
```

Example

```typescript
const api = axios.create({
    baseURL: "http://localhost:8000"
});
```

---

# Main Components

## LOSForm

Responsible for

- Rendering the prediction form
- Collecting user input
- Validation
- Calling REST API

---

## PredictionResult

Responsible for

- Displaying prediction response
- Showing model details
- Displaying prediction timestamp
- Showing predicted LOS

---

## losApi

Responsible for

- HTTP communication
- REST API requests
- Response handling

---

## PredictionPage

Acts as the container page.

Responsibilities

- Maintains prediction state
- Renders form
- Displays prediction results

---

# Styling

Custom styling includes

- Responsive Grid Layout
- Material UI Theme
- Card-based Design
- Mobile Friendly Layout
- CSS Modules
- Typography Improvements

Files

```
global.css
LOSForm.css
PredictionResult.css
```

---

# Future Enhancements

- Form validation using React Hook Form
- Yup validation
- Loading spinner
- Error notifications
- Prediction history
- Export prediction as PDF
- Download prediction report
- Dark mode
- Authentication
- Environment-based API configuration
- Docker deployment
- Unit testing
- Integration testing
- CI/CD pipeline

---

# Recommended Improvements

- Replace hardcoded API URL with environment variables.
- Add centralized Axios interceptors.
- Introduce reusable form components driven by configuration.
- Add request validation before API submission.
- Improve error handling with toast notifications.
- Add loading indicators during prediction.
- Implement API timeout and retry mechanisms.
- Add authentication if deployed in production.

---

# Dependencies

Major libraries

- React
- TypeScript
- Material UI
- Axios
- Vite

---

# Author

Hospital Length of Stay Prediction Frontend

Built using

- React
- TypeScript
- Material UI
- Axios
- FastAPI Backend
- Machine Learning Prediction API

---

# License

This project is intended for educational, research, and healthcare analytics purposes. Modify and extend it according to your organizational requirements.