import streamlit as st
import pandas as pd
import plotly.express as px
import os
# MODIFIED IMPORT:
from recommender import get_cluster_recommendations

st.set_page_config(page_title="EduPro Personalization Engine", layout="wide")

st.title("🎓 EduPro: Learner Personalization Engine")

@st.cache_data
def load_data():
    if not os.path.exists('data/clustered_learners.csv'):
        st.error("❌ Data missing! Run generator, processing, and clustering scripts first.")
        return None, None, None
    df = pd.read_csv('data/clustered_learners.csv')
    tx = pd.read_csv('data/transactions.csv')
    courses = pd.read_csv('data/courses.csv')
    return df, tx, courses

df, tx, courses = load_data()

if df is not None:
    user_id = st.sidebar.selectbox("🔎 Select Learner ID", df['UserID'].unique())
    user_info = df[df['UserID'] == user_id].iloc[0]
    cluster_id = user_info['Cluster']

    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Segment", f"Cluster {cluster_id}")
    c2.metric("Courses", int(user_info['total_courses']))
    c3.metric("Depth", f"{user_info['depth_index']:.2f}")

    # Recommendations
    st.subheader("🎯 Recommended for You")
    recs = get_cluster_recommendations(user_id, df, tx, courses)
    if not recs.empty:
        st.table(recs[['CourseCategory', 'CourseLevel', 'CourseRating']])
    else:
        st.write("No new recommendations.")