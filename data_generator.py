import pandas as pd
import numpy as np
import os

os.makedirs('data', exist_ok=True)

# 1. Users
users = pd.DataFrame({
    'UserID': range(1, 101),
    'Age': np.random.randint(18, 60, 100),
    'Gender': np.random.choice(['M', 'F'], 100)
})

# 2. Courses
categories = ['Data Science', 'Programming', 'Business', 'Design']
levels = ['Beginner', 'Intermediate', 'Advanced']
courses = pd.DataFrame({
    'CourseID': range(101, 121),
    'CourseCategory': np.random.choice(categories, 20),
    'CourseLevel': np.random.choice(levels, 20),
    'CourseRating': np.random.uniform(3.5, 5.0, 20).round(1)
})

# 3. Transactions
transactions = pd.DataFrame({
    'UserID': np.random.choice(range(1, 101), 400),
    'CourseID': np.random.choice(range(101, 121), 400),
    'Amount': np.random.uniform(10, 150, 400).round(2)
})

users.to_csv('data/users.csv', index=False)
courses.to_csv('data/courses.csv', index=False)
transactions.to_csv('data/transactions.csv', index=False)
print("✅ Step 1: Raw data created in /data folder")