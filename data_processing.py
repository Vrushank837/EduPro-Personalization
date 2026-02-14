import pandas as pd
import os

def process_data():
    users = pd.read_csv('data/users.csv')
    courses = pd.read_csv('data/courses.csv')
    tx = pd.read_csv('data/transactions.csv')

    df = tx.merge(users, on='UserID').merge(courses, on='CourseID')

    # Aggregating features
    features = df.groupby('UserID').agg(
        total_courses=('CourseID', 'count'),
        diversity_score=('CourseCategory', 'nunique'),
        avg_spend=('Amount', 'mean')
    )

    # Depth Index: Mapping Level to Numbers
    level_map = {'Beginner': 1, 'Intermediate': 2, 'Advanced': 3}
    df['level_val'] = df['CourseLevel'].map(level_map)
    features['depth_index'] = df.groupby('UserID')['level_val'].mean()

    features.to_csv('data/processed_learners.csv')
    print("✅ Step 2: Feature Engineering complete.")

if __name__ == "__main__":
    process_data()