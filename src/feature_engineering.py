import pandas as pd
from pathlib import Path

# Paths
PROCESSED_DATA_PATH = Path("Data/processed/telecom_churn_cleaned.csv")
SEGMENTATION_DATA_PATH = Path("Data/processed/segmentation_data.csv")

def load_data():
    df = pd.read_csv(PROCESSED_DATA_PATH)
    print("Processed data loaded")
    print("Shape:", df.shape)
    return df

def drop_identifier_columns(df):
    id_cols = [col for col in df.columns if "mobile" in col.lower()]
    print(f"Dropping identifier columns: {id_cols}")
    return df.drop(columns=id_cols, errors="ignore")

def create_usage_features(df):
    mou_cols = [col for col in df.columns if "mou" in col.lower()]
    df["total_mou"] = df[mou_cols].sum(axis=1)

    data_cols = [col for col in df.columns if "2g" in col.lower() or "3g" in col.lower()]
    df["total_data_usage"] = df[data_cols].sum(axis=1)

    return df

def prepare_segmentation_data(df):
    seg_cols = ["aon", "total_mou", "total_data_usage"]
    seg_df = df[seg_cols].fillna(0)
    return seg_df

def save_segmentation_data(seg_df):
    SEGMENTATION_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    seg_df.to_csv(SEGMENTATION_DATA_PATH, index=False)
    print("Segmentation data saved successfully")

if __name__ == "__main__":
    df = load_data()
    df = drop_identifier_columns(df)
    df = create_usage_features(df)
    seg_df = prepare_segmentation_data(df)
    save_segmentation_data(seg_df)


