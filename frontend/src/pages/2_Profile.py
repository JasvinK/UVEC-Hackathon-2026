# python3 -m streamlit run frontend/src/pages/2_Profile.py

import streamlit as st
from theme import apply_theme

apply_theme()

# Page title
st.title("Account")


# ---------------- PROFILE INFO ----------------

# Simple placeholder profile icon
st.write("👤")

# Placeholder name for now
st.subheader("Your Name")


st.divider()


# ---------------- ACCOUNT STATS ----------------

# Create 3 columns so the stats appear side by side
col1, col2, col3 = st.columns(3)

with col1:
    # Number of goals the user has completed
    st.metric("Goals Achieved", "3")

with col2:
    # Total number of goals the user has created
    st.metric("Total Goals", "10")

with col3:
    # Points earned from completing tasks/goals
    st.metric("Points", "300")


st.divider()


# ---------------- OVERALL PROGRESS ----------------

st.subheader("Overall Goal Progress")

# Temporary progress value
# 30 means 30%
st.progress(30)

st.caption("30% of your goals completed")


st.divider()


# ---------------- ACHIEVEMENTS ----------------

st.subheader("Achievements")

# Temporary achievements for now
st.write("🏆 First Goal — Completed your first goal")
st.write("⭐ Small Wins — Completed 5 tasks")
st.write("🌱 Back On Track — Returned to a paused goal")


st.divider()


# ---------------- SETTINGS ----------------

st.subheader("Appearance")

st.toggle(
    "Dark mode",
    key="dark_mode"
)