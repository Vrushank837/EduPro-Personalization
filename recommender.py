import pandas as pd

def get_cluster_recommendations(user_id, clustered_data, transactions, courses):
    user_row = clustered_data[clustered_data['UserID'] == user_id]
    if user_row.empty: return pd.DataFrame()
    
    user_cluster = user_row['Cluster'].values[0]
    user_taken = transactions[transactions['UserID'] == user_id]['CourseID'].unique()
    
    peers = clustered_data[clustered_data['Cluster'] == user_cluster]['UserID']
    peer_tx = transactions[transactions['UserID'].isin(peers)]
    
    recommendations = (
        peer_tx[~peer_tx['CourseID'].isin(user_taken)]
        .groupby('CourseID').size().reset_index(name='popularity')
        .sort_values('popularity', ascending=False)
    )
    
    return recommendations.merge(courses, on='CourseID').head(3)