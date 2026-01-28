import joblib
import pandas as pd


MODEL_PATH = "models/churn_model.joblib"


def load_model():
    return joblib.load(MODEL_PATH)


def predict_churn(aon, total_mou, total_data_usage, segment):
    model = load_model()

    input_df = pd.DataFrame([{
        "aon": aon,
        "total_mou": total_mou,
        "total_data_usage": total_data_usage,
        "segment": segment
    }])

    prob = model.predict_proba(input_df)[0][1]
    prediction = int(prob >= 0.5)

    return {
        "churn_probability": round(prob, 4),
        "churn_prediction": prediction
    }
