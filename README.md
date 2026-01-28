Customer Retention System (End-to-End ML Project)

An end-to-end customer churn prediction system built using real-world telecom data.
The project demonstrates how machine learning models can be taken from raw data to a production-ready system with APIs and a business-facing UI.

Business Context

In the telecom industry, acquiring new customers is significantly more expensive than retaining existing ones.
Identifying customers who are likely to churn enables business teams to take proactive retention actions such as targeted offers, pricing interventions, or customer outreach.

This project focuses on:

Understanding customer usage behavior

Segmenting customers based on usage patterns

Predicting churn risk at an individual customer level

Making predictions accessible to non-technical business users

Business Objectives

The key business objectives addressed in this project are:

Segment customers based on their usage behavior

Define a churn proxy in the absence of explicit churn labels

Build a robust and interpretable churn prediction model

Expose predictions via an API for real-time use

Provide a simple UI to support business decision-making

Solution Overview

The system follows a production-grade machine learning pipeline:

Data understanding and cleaning

Feature selection and missing value treatment

Customer segmentation using KMeans clustering

Segment profiling and statistical interpretation

Churn proxy definition and labeling

Supervised churn prediction model training

Model persistence using Joblib

FastAPI-based inference service

Streamlit UI for business users

System Architecture

The system is designed as a modular, API-driven architecture with clear separation of responsibilities:

Frontend Layer
A Streamlit-based UI that allows business users to input customer details and view churn predictions in real time.

Inference Layer
A FastAPI service that receives requests from the UI, processes inputs, and returns churn predictions.

Model Layer
A trained churn prediction model persisted using Joblib and loaded during inference.

This separation ensures scalability, maintainability, and ease of future enhancements.

Project Structure

Customer Retention System/
│
├── src/
│   ├── app.py                  # FastAPI application
│   ├── inference/
│   │   └── predict.py          # Prediction logic
│
├── models/
│   └── churn_model.joblib      # Trained ML model
│
├── ui/
│   └── app.py                  # Streamlit frontend
│
├── Data/
│   ├── raw/                    # Original dataset
│   └── processed/              # Cleaned & engineered data
│
├── requirements.txt
└── README.md

Modeling Approach

Customer segmentation was performed using KMeans clustering based on telecom usage behavior such as call minutes and data consumption.

Since explicit churn labels were unavailable, a business-driven churn proxy was defined using prolonged inactivity and low usage patterns.

A supervised classification model was then trained to predict churn probability.
Model performance was evaluated using:

Accuracy

ROC-AUC score

How to Run the Project Locally

1️⃣ Start FastAPI Backend

Run the following command from the project root:
uvicorn src.app:app --reload

The FastAPI server will start at:
👉 http://127.0.0.1:8000

Swagger API documentation (for testing predictions):
👉 http://127.0.0.1:8000/docs

2️⃣ Start Streamlit Frontend

In a new terminal, run:
streamlit run ui/app.py

The Streamlit UI will open at:
👉 http://localhost:8501

Business users can now input customer details and view churn predictions.

Output

The system provides the following outputs:

Churn probability score (between 0 and 1)

Binary churn prediction (Yes / No)

Real-time predictions through the Streamlit UI

Key Learnings

This project demonstrates:

Designing end-to-end ML systems beyond notebooks

Translating business problems into machine learning formulations

Handling the absence of explicit labels using business-driven proxies

Deploying models using APIs

Integrating backend services with a business-facing frontend

Maintaining clean and logical Git commit history

Author

Pratik Raj
Master’s in Analytics
Tata Institute of Social Sciences (TISS), Mumbai
