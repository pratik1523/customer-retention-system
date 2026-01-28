import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn Predictor",
    layout="centered"
)

st.title("📉 Customer Churn Prediction System")
st.write("Predict whether a telecom customer is likely to churn")

st.divider()

# Input fields
aon = st.number_input(
    "Account Age (days)",
    min_value=0,
    value=300
)

total_mou = st.number_input(
    "Total Minutes of Usage",
    min_value=0.0,
    value=2.0
)

total_data_usage = st.number_input(
    "Total Data Usage (GB)",
    min_value=0.0,
    value=1.0
)

segment = st.selectbox(
    "Customer Segment",
    options=[0, 1, 2],
    help="Customer usage-based segment"
)

# Predict button
if st.button("🔮 Predict Churn"):
    payload = {
        "aon": aon,
        "total_mou": total_mou,
        "total_data_usage": total_data_usage,
        "segment": segment
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.success(f"Churn Probability: {result['churn_probability']}")
            st.info(
                "Churn Prediction: "
                + ("Yes 🚨" if result["churn_prediction"] == 1 else "No ✅")
            )
        else:
            st.error("API returned an error")

    except Exception as e:
        st.error(f"Could not connect to API: {e}")

