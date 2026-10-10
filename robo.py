"""
Robotics Demand Dashboard  |  run with:  streamlit run robotics_demand_app.py
pip install streamlit pandas plotly

IMPORTANT: The numbers below are PLACEHOLDER / ILLUSTRATIVE values.
Before posting on LinkedIn, replace them with real figures from sources such as
IFR World Robotics report, Statista, LinkedIn Economic Graph, Naukri/Indeed job counts,
and fill in the SOURCE strings. Credibility = your sources.
"""
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Robotics Demand Today", page_icon="🤖", layout="wide")

# ---------- DATA (edit these) ----------
market = pd.DataFrame({
    "Year": [2020, 2021, 2022, 2023, 2024, 2025, 2026],
    "Market Size (USD B)": [27, 31, 36, 42, 49, 57, 66],      # PLACEHOLDER
})
industry = pd.DataFrame({
    "Industry": ["Automotive", "Electronics", "Healthcare", "Logistics & Warehousing",
                 "Agriculture", "Education", "Manufacturing (General)"],
    "Demand Index": [85, 80, 70, 90, 55, 50, 78],              # PLACEHOLDER
})
skills = pd.DataFrame({
    "Skill": ["Python", "ROS", "Embedded / Arduino", "Computer Vision",
              "AI / ML", "PLC & Automation", "CAD / Mechanical", "IoT"],
    "Job Postings Share (%)": [78, 52, 45, 48, 66, 40, 35, 42],  # PLACEHOLDER
})
SOURCE = "Source: add your sources here (IFR, Statista, job portals)"

# ---------- HEADER ----------
st.title("🤖 Why Robotics Skills Are in Demand Today")
st.caption("An interactive look at the market, industries and skills driving robotics careers")

c1, c2, c3 = st.columns(3)
c1.metric("Market size 2026 (USD B)", int(market["Market Size (USD B)"].iloc[-1]),
          f"{market['Market Size (USD B)'].pct_change().iloc[-1]*100:.0f}% YoY")
c2.metric("Top demand industry", industry.sort_values("Demand Index").iloc[-1]["Industry"])
c3.metric("Most asked skill", skills.sort_values("Job Postings Share (%)").iloc[-1]["Skill"])

st.divider()

# ---------- CHARTS ----------
left, right = st.columns(2)
with left:
    st.subheader("📈 Market growth")
    fig = px.area(market, x="Year", y="Market Size (USD B)", markers=True)
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("🏭 Demand by industry")
    fig = px.bar(industry.sort_values("Demand Index"), x="Demand Index", y="Industry",
                 orientation="h", color="Demand Index", color_continuous_scale="Blues")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("🛠️ Skills employers look for")
fig = px.bar(skills.sort_values("Job Postings Share (%)", ascending=False),
             x="Skill", y="Job Postings Share (%)", color="Job Postings Share (%)")
st.plotly_chart(fig, use_container_width=True)

# ---------- INTERACTIVE: skill roadmap ----------
st.subheader("🎯 Build your robotics roadmap")
level = st.selectbox("Your level", ["Beginner", "Intermediate", "Advanced"])
roadmap = {
    "Beginner": ["Electronics basics", "Arduino Uno projects", "Python basics", "Sensors & motors"],
    "Intermediate": ["Raspberry Pi", "Computer vision (OpenCV)", "IoT with ESP32", "Python + data"],
    "Advanced": ["ROS 2", "SLAM & navigation", "ML for robotics", "Industrial automation"],
}
for i, step in enumerate(roadmap[level], 1):
    st.write(f"**{i}.** {step}")

# ---------- UPLOAD YOUR OWN DATA ----------
with st.expander("📂 Upload your own job-demand CSV (columns: Skill, Job Postings Share (%))"):
    f = st.file_uploader("CSV file", type="csv")
    if f:
        df = pd.read_csv(f)
        st.plotly_chart(px.bar(df, x=df.columns[0], y=df.columns[1]), use_container_width=True)

st.divider()
st.caption(SOURCE)
st.caption("Built with Python & Streamlit by Fathima TH Zuhra C — Data Science & Robotics Trainer")