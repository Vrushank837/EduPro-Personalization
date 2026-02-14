# EduPro-Personalization
# 🚀 [Live Demo: EduPro Personalization Engine](https://edupro-personalization-crplrawdqif9ntxn6yjm4m.streamlit.app/)
# EduPro: Learner Personalization Engine 🎓

A data-driven personalization system that uses **Unsupervised Machine Learning** to segment online learners and provide cluster-aware course recommendations.

## 📌 Project Overview
Online learning platforms often struggle with "one-size-fits-all" recommendations, leading to low completion rates. This project introduces a **Learner-Level Aggregation** framework to understand behavioral patterns and personalize the educational journey.

### Key Objectives:
- **Segment Learners:** Categorize users based on engagement, diversity, and depth.
- **Personalize Discovery:** Recommend courses based on what similar learners in the same cluster are successfully completing.
- **Actionable Insights:** Provide a Streamlit dashboard for stakeholders to visualize market segments.

## 🛠️ Tech Stack
- **Language:** Python 3.14
- **ML Libraries:** Scikit-Learn (K-Means Clustering, StandardScaler)
- **Data Handling:** Pandas, NumPy
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Deployment:** Streamlit

## 🧬 Feature Engineering
To move beyond basic demographics, I engineered three primary features to define a "Learner Persona":
1. **Diversity Score:** Measures how many different course categories a learner explores.
2. **Learning Depth Index:** A weighted average of course levels (Beginner=1, Intermediate=2, Advanced=3).
3. **Engagement Score:** Total number of enrollments and average frequency.



## 🤖 Machine Learning Methodology
### 1. Clustering (K-Means)
The model identifies three distinct clusters:
- **Cluster 0: The Explorers** (High diversity, lower depth).
- **Cluster 1: The Career Specialists** (High depth, focused categories).
- **Cluster 2: The Beginner Enthusiasts** (New users with introductory interests).

### 2. Evaluation
- **Elbow Method:** Used to determine the optimal $K=3$.
- **Silhouette Score:** Utilized to validate the consistency and separation of clusters.



## 🚀 How to Run the Project
1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   python data_generator.py
python data_processing.py
python clustering_model.py
python -m streamlit run app.py
