import pandas as pd
from pathlib import Path

# Paths (match your folder structure EXACTLY)
RAW_DATA_PATH = Path("Data/raw/telecom_churn_data.csv")
PROCESSED_DATA_PATH = Path("Data/processed/telecom_churn_cleaned.csv")

def load_data():
    df = pd.read_csv(RAW_DATA_PATH)
    print("Data Loaded Successfully")

    print("Shape:", df.shape)
    return df

def basic_checks(df):
    print("\nColumn Info:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

def clean_data(df):
    print("\nChecking for churn column...")

    possible_churn_cols = ["churn", "Churn", "label", "churned"]
    churn_col = None

    for col in possible_churn_cols:
        if col in df.columns:
            churn_col = col
            break

    if churn_col:
        print(f"Churn column found: {churn_col}")
    else:
        print("No explicit churn column found yet")

    # Handle missing values (simple strategy for now)
    missing_pct = df.isnull().mean() * 100
    cols_to_drop = missing_pct[missing_pct > 30].index

    print(f"Dropping {len(cols_to_drop)} columns with >30% missing values")
    df = df.drop(columns=cols_to_drop)

    df = df.fillna(0)

    print("\nAfter Cleaning Shape:", df.shape)
    return df


def save_processed_data(df):
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print("\nProcessed data saved successfully")

if __name__ == "__main__":
    df = load_data()
    basic_checks(df)
    df_cleaned = clean_data(df)
    save_processed_data(df_cleaned)
