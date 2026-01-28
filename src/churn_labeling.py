import pandas as pd
from pathlib import Path

# Paths
SEGMENTS_PATH = Path("Data/processed/customer_segments.csv")
CHURN_DATA_PATH = Path("Data/processed/churn_labeled_data.csv")

def load_data():
    df = pd.read_csv(SEGMENTS_PATH)
    print("Customer segment data loaded")
    return df

def define_churn(df):
    df["churn"] = ((df["total_mou"] < 5) & (df["total_data_usage"] < 5)).astype(int)
    print("\nChurn distribution:")
    print(df["churn"].value_counts())
    return df

def save_churn_data(df):
    CHURN_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CHURN_DATA_PATH, index=False)
    print("\nChurn-labeled data saved successfully")

if __name__ == "__main__":
    df = load_data()
    df = define_churn(df)
    save_churn_data(df)
