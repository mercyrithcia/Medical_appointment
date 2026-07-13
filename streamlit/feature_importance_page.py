import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


def show_feature_importance_page():

    st.title("📊 Feature Importance")

    st.write(
        "This chart shows which features had the greatest influence on the LightGBM No-Show Prediction model."
    )

    BASE_DIR = Path(__file__).resolve().parent.parent

    feature_file = (
        BASE_DIR /
        "notebooks" /
        "models" /
        "feature_importance.csv"
    )

    feature_df = pd.read_csv(feature_file)

    feature_df = feature_df.sort_values(
        by="Importance",
        ascending=False
    )

    top_n = st.slider(
        "Select Top Features",
        min_value=5,
        max_value=50,
        value=20
    )

    top_features = feature_df.head(top_n)

    fig = px.bar(
        top_features,
        x="Importance",
        y="Feature",
        orientation="h",
        title=f"Top {top_n} Important Features",
        height=700
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Feature Importance Table")

    st.dataframe(
        top_features,
        use_container_width=True
    )