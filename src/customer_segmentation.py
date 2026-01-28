import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Paths
SEGMENTATION_DATA_PATH = Path("Data/processed/segmentation_data.csv")
OUTPUT_PATH = Path("Data/processed/customer_segments.csv")

def load_data():
    df = pd.read_csv(SEGMENTATION_DATA_PATH)
    print("Segmentation data loaded")
    print(df.head())
    return df

def scale_features(df):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)
    return scaled

def run_kmeans(scaled_data, n_clusters=4):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(scaled_data)
    return labels

def save_results(df, labels):
    df_out = df.copy()
    df_out["segment"] = labels
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(OUTPUT_PATH, index=False)
    print("Customer segments saved successfully")

if __name__ == "__main__":
    df = load_data()
    scaled_data = scale_features(df)
    labels = run_kmeans(scaled_data, n_clusters=4)
    save_results(df, labels)
