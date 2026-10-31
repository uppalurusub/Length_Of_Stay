import streamlit as st


def render_form():

    with st.form("los_prediction_form"):

        st.subheader("Patient Information")

        col1, col2, col3 = st.columns(3)

        with col1:

            admission_source = st.selectbox(
                "Admission Source",
                [
                    "Direct",
                    "Referral",
                    "Transfer",
                    "Emergency Room"
                ],
                index=1
            )

            admission_type = st.selectbox(
                "Admission Type",
                [
                    "Emergency",
                    "Urgent",
                    "Elective"
                ]
            )

            age = st.number_input(
                "Age",
                min_value=0,
                max_value=120,
                value=45
            )

            gender = st.selectbox(
                "Gender",
                [
                    "Male",
                    "Female"
                ]
            )

            marital_status = st.selectbox(
                "Marital Status",
                [
                    "Single",
                    "Married",
                    "Divorced",
                    "Widowed"
                ],
                index=1
            )

        with col2:

            bmi = st.number_input(
                "BMI",
                min_value=10.0,
                max_value=80.0,
                value=27.4
            )

            comorbidity_count = st.number_input(
                "Comorbidity Count",
                min_value=0,
                max_value=20,
                value=2
            )

            previous_admissions = st.number_input(
                "Previous Admissions",
                min_value=0,
                max_value=50,
                value=1
            )

            severity_score = st.number_input(
                "Severity Score",
                min_value=0.0,
                max_value=10.0,
                value=7.5
            )

            smoker = st.selectbox(
                "Smoker",
                [
                    "No",
                    "Yes"
                ]
            )

        with col3:

            hospital_department = st.selectbox(
                "Hospital Department",
                [
                    "Cardiology",
                    "Neurology",
                    "Orthopedics",
                    "Oncology",
                    "Pulmonology",
                    "General Medicine",
                    "ICU"
                ]
            )

            insurance_type = st.selectbox(
                "Insurance Type",
                [
                    "Private",
                    "Government",
                    "Self-Pay",
                    "Corporate"
                ]
            )

            discharge_disposition = st.selectbox(
                "Discharge Disposition",
                [
                    "Home",
                    "Transferred",
                    "Expired",
                    "Rehabilitation",
                    "Other"
                ]
            )

            primary_diagnosis = st.text_input(
                "Primary Diagnosis",
                value="Pneumonia"
            )

        st.divider()

        st.subheader("Clinical Measurements")

        col4, col5, col6 = st.columns(3)

        with col4:

            glucose = st.number_input(
                "Glucose",
                min_value=0.0,
                value=190.0
            )

            oxygen_saturation = st.number_input(
                "Oxygen Saturation",
                min_value=0.0,
                max_value=100.0,
                value=96.0
            )

            hemoglobin = st.number_input(
                "Hemoglobin",
                min_value=0.0,
                value=12.7
            )

        with col5:

            creatinine = st.number_input(
                "Creatinine",
                min_value=0.0,
                value=2.86
            )

            blood_pressure = st.number_input(
                "Blood Pressure",
                min_value=0,
                max_value=300,
                value=160
            )

            temperature = st.number_input(
                "Temperature",
                min_value=80.0,
                max_value=110.0,
                value=98.0
            )

        with col6:

            heart_rate = st.number_input(
                "Heart Rate",
                min_value=20,
                max_value=250,
                value=99
            )

        submitted = st.form_submit_button(
            "Predict Length of Stay",
            use_container_width=True
        )

    payload = {

        "admission_source": admission_source,
        "admission_type": admission_type,
        "age": age,
        "bmi": bmi,
        "comorbidity_count": comorbidity_count,
        "discharge_disposition": discharge_disposition,
        "gender": gender,
        "hospital_department": hospital_department,
        "insurance_type": insurance_type,
        "previous_admissions": previous_admissions,
        "primary_diagnosis": primary_diagnosis,
        "severity_score": severity_score,
        "smoker": smoker,
        "glucose": glucose,
        "marital_status": marital_status,
        "oxygen_saturation": oxygen_saturation,
        "hemoglobin": hemoglobin,
        "creatinine": creatinine,
        "blood_pressure": blood_pressure,
        "temperature": temperature,
        "heart_rate": heart_rate
    }

    return submitted, payload