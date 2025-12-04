import streamlit as st
import random

st.set_page_config(page_title="51 - Add an explainable evaluation dashboard ...", page_icon="📊")

st.title("📊 Add an explainable evaluation dashboard ...")
st.write("""Add an explainable evaluation dashboard with error examples and root causes.""")

# Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Requests", random.randint(1000, 5000), delta=random.randint(-50, 100))
with col2:
    st.metric("Avg Latency", f"{random.randint(100, 500)}ms", delta=f"{random.randint(-20, 20)}ms")
with col3:
    st.metric("Success Rate", f"{random.uniform(95, 99.9):.1f}%")
with col4:
    st.metric("Active Users", random.randint(50, 200))

# Chart placeholder
st.subheader("Trends")
import pandas as pd
chart_data = pd.DataFrame({
    "Time": list(range(10)),
    "Value": [random.randint(50, 100) for _ in range(10)]
})
st.line_chart(chart_data, x="Time", y="Value")

# Table
st.subheader("Recent Activity")
st.dataframe({
    "Timestamp": ["10:00", "10:05", "10:10", "10:15", "10:20"],
    "Event": ["Request", "Response", "Error", "Request", "Response"],
    "Status": ["Success", "Success", "Failed", "Success", "Success"]
})
