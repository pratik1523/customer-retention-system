import pandas as pd
from pathlib import Path

# Paths
SEGMENTS_PATH = Path("Data/processed/customer_segments.csv")
SUMMARY_PATH = Path("Data/processed/segment_summary.csv")

def load_data():
    df = pd.read_csv(SEGMENTS_PATH)
    print("Customer segments data loaded")
    return df

def segment_summary(df):
    summary = df.groupby("segment").agg({
        "aon": "mean",
        "total_mou": "mean",
        "total_data_usage": "mean"
    }).reset_index()

    summary.rename(columns={
        "aon": "avg_aon",
        "total_mou": "avg_total_mou",
        "total_data_usage": "avg_total_data_usage"
    }, inplace=True)

    print("\nSegment Summary:")
    print(summary)
    return summary

def save_summary(summary):
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(SUMMARY_PATH, index=False)
    print("\nSegment summary saved successfully")

if __name__ == "__main__":
    df = load_data()
    summary = segment_summary(df)
    save_summary(summary)
