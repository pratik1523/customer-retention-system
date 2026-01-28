from fastapi import FastAPI
from pydantic import BaseModel

from src.inference.predict import predict_churn

app = FastAPI(title="Customer Churn Prediction API")


class ChurnRequest(BaseModel):
    aon: float
    total_mou: float
    total_data_usage: float
    segment: int


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/predict")
def predict(request: ChurnRequest):
    result = predict_churn(
        aon=request.aon,
        total_mou=request.total_mou,
        total_data_usage=request.total_data_usage,
        segment=request.segment
    )
    return result


