import streamlit as st

from no_show_page import show_no_show_page
from demand_page import show_demand_page
from feature_importance_page import show_feature_importance_page

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Medical Appointment Prediction System",
    page_icon="🏥",
    layout="wide"
)

# =====================================================
# HOSPITAL BANNER
# =====================================================

st.image(
    "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=1200",
    use_container_width=True
)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🏥 Navigation")

st.sidebar.success("""
### Medical Appointment Prediction System

✅ Patient No-Show Prediction

✅ Appointment Demand Forecasting

✅ Feature Importance

Built Using

• Python
• Pandas
• NumPy
• Scikit-Learn
• LightGBM
• Random Forest
• Streamlit
""")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "🩺 No Show Prediction",
        "📈 Demand Forecasting",
        "📊 Feature Importance",
        "ℹ️ About Project"
    ]
)

# =====================================================
# HOME PAGE
# =====================================================

if page == "🏠 Home":

    st.markdown("""
# 🏥 Medical Appointment Prediction System

### AI Powered Hospital Decision Support Dashboard
""")

    st.write(
        "This application helps hospitals improve operational efficiency using Machine Learning."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
### 🩺 Patient No-Show Prediction

Predict whether a patient is likely to miss their appointment.

✔ LightGBM Classifier

✔ Accuracy : 73%

✔ ROC-AUC : 0.784
""")

    with col2:

        st.success("""
### 📈 Appointment Demand Forecasting

Forecast future hospital appointment demand.

✔ Random Forest Regressor

✔ R² Score : 0.327

✔ Daily Demand Prediction
""")

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    c1.metric("Classification Models", "4")
    c2.metric("Forecast Model", "1")
    c3.metric("Dataset Records", "109,593")

    c4, c5, c6 = st.columns(3)

    c4.metric("Classification Accuracy", "73%")
    c5.metric("ROC-AUC Score", "0.784")
    c6.metric("Forecast R² Score", "0.327")

    st.markdown("---")

    st.subheader("✨ Project Features")

    st.write("""
- 🩺 Predict Patient No-Shows
- 📈 Forecast Future Appointment Demand
- 📊 Feature Importance Visualization
- 🤖 Machine Learning Based Predictions
- 📊 Interactive Streamlit Dashboard
- ⚡ Real-Time Predictions
- 🏥 Hospital Decision Support System
""")

# =====================================================
# NO SHOW PAGE
# =====================================================

elif page == "🩺 No Show Prediction":

    show_no_show_page()

# =====================================================
# DEMAND PAGE
# =====================================================

elif page == "📈 Demand Forecasting":

    show_demand_page()

# =====================================================
# FEATURE IMPORTANCE PAGE
# =====================================================

elif page == "📊 Feature Importance":

    show_feature_importance_page()

# =====================================================
# ABOUT PAGE
# =====================================================

else:

    st.title("ℹ️ About Project")

    st.markdown("""
## Medical Appointment Prediction System

This project predicts whether a patient is likely to miss a scheduled appointment and forecasts future hospital appointment demand using Machine Learning.

---

### 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- LightGBM
- Random Forest
- Streamlit

---

### 🤖 Machine Learning Models

#### Classification

- Logistic Regression
- Random Forest
- XGBoost
- LightGBM

🏆 Best Model : LightGBM

Accuracy : 73%

ROC-AUC : 0.784

---

#### Forecasting

- Random Forest Regressor

🏆 Best Model : Random Forest

R² Score : 0.327

---

### 👩‍💻 Developed By

Mercy Rithcia
""")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "© 2026 Medical Appointment Prediction System | Developed by Mercy Rithcia"
)