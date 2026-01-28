import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, roc_auc_score


# ===============================
# Paths
# ===============================
DATA_PATH = Path("Data/processed/churn_labeled_data.csv")


def load_data():
    df = pd.read_csv(DATA_PATH)
    print("Churn labeled data loaded")
    return df


def prepare_features(df):
    X = df[["aon", "total_mou", "total_data_usage", "segment"]]
    y = df["churn"]
    return X, y


def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    y_prob = pipeline.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)

    print(f"Accuracy : {acc:.4f}")
    print(f"ROC-AUC  : {auc:.4f}")


if __name__ == "__main__":
    df = load_data()
    X, y = prepare_features(df)
    train_and_evaluate(X, y)

