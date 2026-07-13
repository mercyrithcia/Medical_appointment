import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load model and preprocessor
no_show_model = joblib.load(
    BASE_DIR / "notebooks" / "models" / "no_show_model.pkl"
)

preprocessor = joblib.load(
    BASE_DIR / "notebooks" / "models" / "preprocessor.pkl"
)


def show_no_show_page():

    st.title("🩺 Patient No-Show Prediction")

    st.markdown("### Enter Patient Details")

    col1, col2 = st.columns(2)

    with col1:

        specialty = st.selectbox(
            "Specialty",
            [
                "psychotherapy",
                "speech therapy",
                "physiotherapy",
                "occupational therapy",
                "pedagogo",
                "enf",
                "assist",
                "sem especialidade",
                "Unknown"
            ]
        )

        gender = st.selectbox(
            "Gender",
            ["F", "M", "I"]
        )

        disability = st.selectbox(
            "Disability",
            [" ", "Unknown"]
        )

        place = st.selectbox(
            "Place",
            [
                "ITAJAÍ",
                "B. CAMBORIU",
                "CAMBORIU",
                "NAVEGANTES",
                "ITAPEMA",
                "BOMBINHAS",
                "PENHA",
                "PORTO BELO",
                "ILHOTA",
                "LUIZ ALVES",
                "Unknown"
            ]
        )

        appointment_shift = st.selectbox(
            "Appointment Shift",
            ["morning", "afternoon"]
        )

        age = st.number_input(
            "Age",
            min_value=0,
            max_value=100,
            value=35
        )

        appointment_time = st.slider(
            "Appointment Hour",
            7,
            18,
            10
        )

    with col2:

        average_temp_day = st.number_input(
            "Average Temperature",
            value=20.0
        )

        average_rain_day = st.number_input(
            "Average Rain",
            value=0.0
        )

        max_temp_day = st.number_input(
            "Maximum Temperature",
            value=25.0
        )

        max_rain_day = st.number_input(
            "Maximum Rain",
            value=0.0
        )

        rain_intensity = st.selectbox(
            "Rain Intensity",
            ["no_rain", "weak", "moderate", "heavy"]
        )

        heat_intensity = st.selectbox(
            "Heat Intensity",
            ["heavy_cold", "cold", "mild", "warm", "heavy_warm"]
        )

    st.markdown("---")

    st.subheader("Medical Information")

    col3, col4 = st.columns(2)

    with col3:

        Hipertension = st.selectbox("Hypertension", [0, 1])
        Diabetes = st.selectbox("Diabetes", [0, 1])
        Alcoholism = st.selectbox("Alcoholism", [0, 1])
        Handcap = st.selectbox("Handicap", [0, 1])

    with col4:

        Scholarship = st.selectbox("Scholarship", [0, 1])
        SMS_received = st.selectbox("SMS Received", [0, 1])

        rainy_day_before = st.selectbox(
            "Rainy Day Before",
            [0, 1]
        )

        storm_day_before = st.selectbox(
            "Storm Day Before",
            [0, 1]
        )

    st.markdown("---")

    if st.button("Predict No-Show"):

        input_data = pd.DataFrame({

            "specialty":[specialty],
            "appointment_time":[appointment_time],
            "gender":[gender],
            "disability":[disability],
            "place":[place],
            "appointment_shift":[appointment_shift],
            "age":[age],
            "under_12_years_old":[1 if age < 12 else 0],
            "over_60_years_old":[1 if age >= 60 else 0],
            "patient_needs_companion":[1 if age < 12 or age >= 60 else 0],
            "average_temp_day":[average_temp_day],
            "average_rain_day":[average_rain_day],
            "max_temp_day":[max_temp_day],
            "max_rain_day":[max_rain_day],
            "rainy_day_before":[rainy_day_before],
            "storm_day_before":[storm_day_before],
            "rain_intensity":[rain_intensity],
            "heat_intensity":[heat_intensity],
            "Hipertension":[Hipertension],
            "Diabetes":[Diabetes],
            "Alcoholism":[Alcoholism],
            "Handcap":[Handcap],
            "Scholarship":[Scholarship],
            "SMS_received":[SMS_received],
            "Year":[2021],
            "Month":[6],
            "Day":[15],
            "DayOfWeek":[2],
            "Quarter":[2]

        })

        # Preprocess input
        input_processed = preprocessor.transform(input_data)

        # Predict
        prediction = no_show_model.predict(input_processed)[0]

        probability = no_show_model.predict_proba(input_processed)[0][1]

        st.markdown("---")

        st.subheader("📊 Prediction Result")

        if prediction == 1:

            st.error("⚠️ High Risk of Patient No-Show")

            st.progress(float(probability))

            st.metric(
                "No-Show Probability",
                f"{probability*100:.2f}%"
            )

            st.warning("""
### 📋 Recommendation

• 📞 Call the patient one day before the appointment

• 📱 Send an SMS reminder

• 📅 Confirm appointment timing

• 👨‍⚕️ Keep a backup slot ready
""")

        else:

            st.success("✅ Patient is Likely to Attend")

            st.progress(float(1 - probability))

            st.metric(
                "Attendance Probability",
                f"{(1-probability)*100:.2f}%"
            )

            st.info("""
### 👍 Recommendation

• Appointment is likely to proceed normally

• Standard reminder is sufficient

• No additional follow-up required
""")