# 🏥 Medical Appointment Prediction System

An end-to-end Machine Learning project that predicts patient no-shows and forecasts future hospital appointment demand using historical appointment and weather data.

---

# 🚀 Project Overview

Healthcare providers lose significant time and resources due to missed appointments.

This project helps hospitals by:

- 🩺 Predicting whether a patient is likely to miss an appointment
- 📈 Forecasting future appointment demand
- 📊 Visualizing important prediction features
- 🏥 Supporting hospital resource planning

---

# 📂 Project Structure

```
Medical_appointment/
│
├── data/
│
├── notebooks/
│   ├── models/
│   │   ├── no_show_model.pkl
│   │   ├── demand_forecast_model.pkl
│   │   ├── preprocessor.pkl
│   │   ├── feature_importance.csv
│   │   └── demand_feature_importance.csv
│   │
│   └── notebooks
│
├── streamlit/
│   ├── app.py
│   ├── no_show_page.py
│   ├── demand_page.py
│   ├── feature_importance_page.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

- Total Records: **109,593**
- Hospital Appointment Records
- Weather Data
- Patient Medical History
- Appointment Information

---

# 🧹 Data Preprocessing

- Missing Value Handling
- Feature Engineering
- One-Hot Encoding
- Standard Scaling
- Pipeline using Scikit-Learn ColumnTransformer

---

# 🤖 Machine Learning Models

## Patient No-Show Prediction

Models Evaluated

- Logistic Regression
- Random Forest
- XGBoost
- LightGBM ✅ Best Model

Performance

- Accuracy: **73%**
- ROC-AUC: **0.784**

---

## Appointment Demand Forecasting

Model Used

- Random Forest Regressor

Performance

- MAE: **142.25**
- RMSE: **231.83**
- R² Score: **0.327**

---

# 📈 Features

- Patient No-Show Prediction
- Appointment Demand Forecasting
- Feature Importance Visualization
- Interactive Streamlit Dashboard
- Real-Time Predictions

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- LightGBM
- XGBoost
- Plotly
- Streamlit
- Joblib

---

# ▶️ Run the Project

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Medical_appointment.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run streamlit/app.py
```

---

# 👩‍💻 Developed By

**Mercy Rithcia**

Aspiring Data Analyst | Machine Learning Enthusiast

---