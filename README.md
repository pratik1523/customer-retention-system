# 📉 Customer Retention System (End-to-End ML Project)

An end-to-end customer churn prediction system built using real-world telecom data.  
This project demonstrates how machine learning models can be taken from raw data to a **production-ready system** with APIs and a business-facing UI.

---

## 🔍 Business Context

In the telecom industry, acquiring new customers is significantly more expensive than retaining existing ones.  
Identifying customers who are likely to churn enables business teams to take **proactive retention actions** such as targeted offers, pricing interventions, or customer outreach.

This project focuses on:
- Understanding customer usage behavior
- Segmenting customers based on usage patterns
- Predicting churn risk at an individual level
- Making predictions accessible to non-technical users

---

## 🎯 Business Objectives

- Segment customers based on usage behavior  
- Define a churn proxy in the absence of explicit churn labels  
- Build a robust churn prediction model  
- Expose predictions via an API  
- Provide a simple UI for business decision-making  

---

## 🧠 Solution Overview

The system follows a **production-grade machine learning pipeline**:

1. Data understanding and cleaning  
2. Feature selection and missing value treatment  
3. Customer segmentation using KMeans clustering  
4. Segment profiling and statistical interpretation  
5. Churn proxy definition and labeling  
6. Supervised churn prediction model training  
7. Model persistence using Joblib  
8. FastAPI-based inference service  
9. Streamlit UI for business users  

---

## 🏗️ System Architecture

The system is designed as a modular, API-driven architecture:

- **Frontend Layer**:  
  Streamlit-based UI that allows business users to input customer details and view churn predictions.

- **Inference Layer**:  
  FastAPI service that receives requests from the UI, processes inputs, and returns predictions.

- **Model Layer**:  
  A trained churn prediction model persisted using Joblib and loaded during inference.

This separation ensures scalability, maintainability, and clear responsibility across components.

## 📁 Project Structure

- `src/` – Backend source code  
  - `app.py` – FastAPI application entry point  
  - `inference/` – Model inference logic  
    - `predict.py`

- `models/` – Persisted machine learning models  
  - `churn_model.joblib`

- `ui/` – Streamlit frontend  
  - `app.py`

- `Data/` – Dataset storage  
  - `raw/` – Original data  
  - `processed/` – Cleaned and feature-engineered data  

- `requirements.txt` – Project dependencies  
- `README.md` – Project documentation


---

## 🤖 Modeling Approach

- Customer segmentation was performed using **KMeans clustering** based on usage behavior.
- Since explicit churn labels were unavailable, a **churn proxy** was defined using prolonged inactivity and low usage patterns.
- A supervised classification model was trained to predict **churn probability**.
- Model performance was evaluated using **Accuracy** and **ROC-AUC** metrics.

---

## 🚀 How to Run the Project Locally

### 1️⃣ Start FastAPI Backend

```bash
uvicorn src.app:app --reload

FastAPI will run at:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

###2️⃣ Start Streamlit Frontend

Run the Streamlit application to access the user interface:
streamlit run ui/app.py

The Streamlit UI will open at:
http://localhost:8501

Output

The system provides the following outputs to the user:

Churn probability score (between 0 and 1)

Binary churn prediction (Yes / No)

Real-time predictions through the Streamlit UI


Key Learnings

Designing end-to-end ML systems beyond notebooks

Translating business problems into machine learning formulations

Handling the absence of explicit labels using business-driven proxies

Deploying models using APIs and integrating them with a frontend UI

Maintaining clean and logical Git commit history




