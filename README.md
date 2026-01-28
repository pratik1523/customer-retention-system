# 📉 Customer Retention System (End-to-End ML Project)

An end-to-end customer churn prediction system built using real-world telecom data.
The project demonstrates how machine learning models are taken from raw data
to a production-ready system with APIs and a business-facing UI.

---

## 🔍 Business Context

In the telecom industry, acquiring new customers is significantly more expensive
than retaining existing ones. Identifying customers who are likely to churn allows
business teams to take proactive retention actions such as personalized offers,
pricing interventions, or customer outreach.

This project focuses on:
- Understanding customer usage behavior
- Segmenting customers based on patterns
- Predicting churn risk at an individual level
- Making predictions accessible to non-technical users

---

## 🎯 Business Objectives

- Segment customers based on usage behavior
- Define a churn proxy in absence of explicit churn labels
- Build a robust churn prediction model
- Expose predictions via an API
- Provide a simple UI for business decision-making

---

## 🧠 Solution Overview

The system follows a **production-grade ML pipeline**:

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

User (Browser)
↓
Streamlit UI (Frontend)
↓
FastAPI Inference API
↓
Trained ML Model (Joblib)

## 📁 Project Structure

Customer Retention System/
│
├── src/
│ ├── app.py
│ └── inference/
│ └── predict.py
│
├── models/
│ └── churn_model.joblib
│
├── ui/
│ └── app.py
│
├── Data/
│ ├── raw/
│ └── processed/
│
├── requirements.txt
└── README.md

## 🤖 Modeling Approach

- Customer segmentation was performed using KMeans clustering based on usage behavior.
- Since explicit churn labels were unavailable, a churn proxy was defined using prolonged inactivity.
- A supervised classification model was trained to predict churn probability.
- Model performance was evaluated using accuracy and ROC-AUC.


## 🚀 How to Run the Project Locally
### Start FastAPI Backend

```bash
uvicorn src.app:app --reload

FastAPI will run at:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

## 6️⃣ Start Streamlit Frontend

Run the Streamlit application to access the user interface:

```bash
streamlit run ui/app.py

http://localhost:8501


📌 **Important fixes vs what you wrote**
- `http://localhost:8501` must be **outside** the bash block
- No nested ```markdown inside README
- Clean and professional

---

## 🔹 7️⃣ Output

👉 Paste **exactly this** below it:

```markdown
## 📊 Output

The system provides the following outputs to the user:

- Churn probability score (between 0 and 1)
- Binary churn prediction (Yes / No)
- Real-time prediction through the Streamlit UI



## 💡 Key Learnings

- Building end-to-end ML systems beyond notebooks
- Defining churn labels using business logic
- Deploying models via APIs
- Integrating backend and frontend systems
- Maintaining clean Git commit history


## 👤 Author

Pratik Raj  
Master’s in Analytics, TISS Mumbai

Project completed as part of end-to-end ML system design.

