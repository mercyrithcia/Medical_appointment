import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import plotly.graph_objects as go

# =====================================================
# LOAD MODEL
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

forecast_model = joblib.load(
    BASE_DIR / "notebooks" / "models" / "demand_forecast_model.pkl"
)

# =====================================================
# DEMAND PAGE
# =====================================================

def show_demand_page():

    st.title("📈 Appointment Demand Forecasting")

    st.write(
        "Predict the expected number of hospital appointments for a future day."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        lag_1 = st.number_input(
            "Appointments Yesterday",
            min_value=0,
            value=250
        )

        lag_7 = st.number_input(
            "Appointments 7 Days Ago",
            min_value=0,
            value=240
        )

        lag_30 = st.number_input(
            "Appointments 30 Days Ago",
            min_value=0,
            value=230
        )

        rolling_mean = st.number_input(
            "Rolling Mean (7 Days)",
            min_value=0.0,
            value=245.0
        )

        rolling_std = st.number_input(
            "Rolling Std (7 Days)",
            min_value=0.0,
            value=35.0
        )

    with col2:

        year = st.number_input(
            "Year",
            min_value=2020,
            max_value=2035,
            value=2021
        )

        month = st.number_input(
            "Month",
            min_value=1,
            max_value=12,
            value=5
        )

        day = st.number_input(
            "Day",
            min_value=1,
            max_value=31,
            value=13
        )

        dayofweek = st.selectbox(
            "Day of Week",
            [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"
            ]
        )

        day_map = {
            "Monday":0,
            "Tuesday":1,
            "Wednesday":2,
            "Thursday":3,
            "Friday":4,
            "Saturday":5,
            "Sunday":6
        }

        quarter = st.selectbox(
            "Quarter",
            [1,2,3,4]
        )

    st.markdown("---")

    if st.button("Forecast Demand"):

        input_data = pd.DataFrame({

            "Lag_1":[lag_1],
            "Lag_7":[lag_7],
            "Lag_30":[lag_30],
            "Rolling_Mean_7":[rolling_mean],
            "Rolling_STD_7":[rolling_std],
            "Year":[year],
            "Month":[month],
            "Day":[day],
            "DayOfWeek":[day_map[dayofweek]],
            "Quarter":[quarter]

        })

        prediction = forecast_model.predict(input_data)[0]

        st.success("Forecast Completed Successfully")

        st.metric(
            "Predicted Appointments",
            f"{prediction:.0f}"
        )

        if prediction < 150:

            st.success("🟢 Hospital Load : Low")

        elif prediction < 300:

            st.warning("🟡 Hospital Load : Moderate")

        else:

            st.error("🔴 Hospital Load : High")

        st.markdown("---")

        st.subheader("📈 Demand Visualization")

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=["Yesterday","7 Days Ago","30 Days Ago","Predicted"],
                y=[lag_1,lag_7,lag_30,prediction]
            )
        )

        fig.update_layout(
            title="Appointment Comparison",
            xaxis_title="Timeline",
            yaxis_title="Appointments",
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

        st.info("""
### 📋 Recommendation

🩺 Low Load
- Normal staffing

🟡 Moderate Load
- Keep additional consultation rooms ready

🔴 High Load
- Allocate additional doctors
- Increase nursing staff
- Prepare reception counters
- Keep emergency support ready
""")