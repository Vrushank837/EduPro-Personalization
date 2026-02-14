import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def run_clustering():
    df = pd.read_csv('data/processed_learners.csv')
    features = df[['total_courses', 'diversity_score', 'depth_index']]
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Using 3 clusters for EduPro segments
    model = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = model.fit_predict(scaled_features)
    
    df.to_csv('data/clustered_learners.csv', index=False)
    print("✅ Step 3: K-Means Clustering complete.")

if __name__ == "__main__":
    run_clustering()