import { useState } from "react";
import {
  Box,
  Button,
  Card,
  CardContent,
  Divider,
  MenuItem,
  TextField,
  Typography,
} from "@mui/material";

import "../styles/LOSForm.css";
import type { LengthOfStayRequest } from "../models/LengthOfStayRequest";
import { predictLOS } from "../api/losApi";

interface LOSFormProps {
  onResult: (response: any) => void;
}

const initialForm: LengthOfStayRequest = {
  admission_source: "Referral",
  admission_type: "Emergency",
  age: 45,
  bmi: 27.4,
  comorbidity_count: 2,
  discharge_disposition: "Home",
  gender: "Male",
  hospital_department: "Cardiology",
  insurance_type: "Private",
  previous_admissions: 1,
  primary_diagnosis: "Pneumonia",
  severity_score: 7.5,
  smoker: "No",
  glucose: 190,
  marital_status: "Married",
  oxygen_saturation: 96,
  hemoglobin: 12.7,
  creatinine: 2.86,
  blood_pressure: 160,
  temperature: 98,
  heart_rate: 99,
};

const LOSForm: React.FC<LOSFormProps> = ({ onResult }) => {

  const [form, setForm] = useState(initialForm);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const { name, value } = e.target;

    setForm(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async () => {

        try {

            const response = await predictLOS(form);

            console.log(response);

            onResult(response);

        } catch (err) {

            console.error(err);

        }

    };

  return (

<Card className="los-card">

    <CardContent>

        <Typography variant="h5" className="page-title">
            Hospital Length Of Stay Prediction
        </Typography>

        <Divider sx={{ mb: 3 }} />

        {/* Patient Information */}

        <Typography className="section-title">
            Patient Information
        </Typography>

        <div className="form-grid">

            <TextField
                label="Age"
                name="age"
                type="number"
                value={form.age}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                select
                label="Gender"
                name="gender"
                value={form.gender}
                onChange={handleChange}
                fullWidth
            >
                <MenuItem value="Male">Male</MenuItem>
                <MenuItem value="Female">Female</MenuItem>
            </TextField>

            <TextField
                select
                label="Marital Status"
                name="marital_status"
                value={form.marital_status}
                onChange={handleChange}
                fullWidth
            >
                <MenuItem value="Single">Single</MenuItem>
                <MenuItem value="Married">Married</MenuItem>
            </TextField>

            <TextField
                label="BMI"
                name="bmi"
                type="number"
                value={form.bmi}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                select
                label="Smoker"
                name="smoker"
                value={form.smoker}
                onChange={handleChange}
                fullWidth
            >
                <MenuItem value="Yes">Yes</MenuItem>
                <MenuItem value="No">No</MenuItem>
            </TextField>

        </div>

        <Divider className="divider" />

        <Typography className="section-title">
            Admission Information
        </Typography>

        <div className="form-grid">

            <TextField
                select
                label="Admission Type"
                name="admission_type"
                value={form.admission_type}
                onChange={handleChange}
                fullWidth
            >
                <MenuItem value="Emergency">Emergency</MenuItem>
                <MenuItem value="Elective">Elective</MenuItem>
                <MenuItem value="Urgent">Urgent</MenuItem>
            </TextField>

            <TextField
                select
                label="Admission Source"
                name="admission_source"
                value={form.admission_source}
                onChange={handleChange}
                fullWidth
            >
                <MenuItem value="Referral">Referral</MenuItem>
                <MenuItem value="Walk-In">Walk-In</MenuItem>
                <MenuItem value="Transfer">Transfer</MenuItem>
            </TextField>

            <TextField
                label="Department"
                name="hospital_department"
                value={form.hospital_department}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                label="Insurance"
                name="insurance_type"
                value={form.insurance_type}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                label="Primary Diagnosis"
                name="primary_diagnosis"
                value={form.primary_diagnosis}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                label="Discharge"
                name="discharge_disposition"
                value={form.discharge_disposition}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                label="Previous Admissions"
                name="previous_admissions"
                type="number"
                value={form.previous_admissions}
                onChange={handleChange}
                fullWidth
            />

        </div>

        <Divider className="divider" />

        <Typography className="section-title">
            Clinical Measurements
        </Typography>

        <div className="form-grid">

            <TextField
                label="Severity Score"
                name="severity_score"
                type="number"
                value={form.severity_score}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                label="Blood Pressure"
                name="blood_pressure"
                type="number"
                value={form.blood_pressure}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                label="Temperature"
                name="temperature"
                type="number"
                value={form.temperature}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                label="Heart Rate"
                name="heart_rate"
                type="number"
                value={form.heart_rate}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                label="Oxygen Saturation"
                name="oxygen_saturation"
                type="number"
                value={form.oxygen_saturation}
                onChange={handleChange}
                fullWidth
            />

        </div>

        <Divider className="divider" />

        <Typography className="section-title">
            Laboratory Values
        </Typography>

        <div className="form-grid">

            <TextField
                label="Glucose"
                name="glucose"
                type="number"
                value={form.glucose}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                label="Hemoglobin"
                name="hemoglobin"
                type="number"
                value={form.hemoglobin}
                onChange={handleChange}
                fullWidth
            />

            <TextField
                label="Creatinine"
                name="creatinine"
                type="number"
                value={form.creatinine}
                onChange={handleChange}
                fullWidth
            />

        </div>

        <Box className="button-area">

            <Button
                variant="contained"
                size="large"
                onClick={handleSubmit}
            >
                Predict Length Of Stay
            </Button>

        </Box>

    </CardContent>

</Card>

)
};

export default LOSForm;