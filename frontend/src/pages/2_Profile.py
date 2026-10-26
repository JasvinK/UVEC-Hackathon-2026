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

# get list of completed goals
done_goals = [key for key in st.session_state.goals if key["done"] >= key["total"]]

with col1:
    # Number of goals the user has completed
    st.metric("Goals Achieved", len(done_goals))

with col2:
    # Total number of goals the user has created
    st.metric("Total Goals", len(st.session_state.goals))

with col3:
    # Points earned from completing tasks/goals
    st.metric("Points", len(done_goals) * 100)


st.divider()


# ---------------- OVERALL PROGRESS ----------------

st.subheader("Overall Weekly Goal Progress")

total_done = sum(g["done"] for g in st.session_state.goals)
total_total = sum(g["total"] for g in st.session_state.goals)

if total_total > 0:
    progress = total_done / total_total
    st.progress(progress, text=f"{total_done}/{total_total} completed ({progress:.0%}) (Keep going!)")
else:
    st.info("Add a goal to start tracking progress.")


st.divider()


# ---------------- ACHIEVEMENTS ----------------

st.subheader("Achievements")

# Temporary achievements for now
st.write("First Goal: Completed your first goal")
st.write("Small Wins: Completed 5 tasks")
st.write("Back On Track: Returned to a paused goal")


st.divider()

# ---------------- Raw Json ----------------
st.write("raw json")
st.write(st.session_state.goals)

# ---------------- SETTINGS ----------------

st.subheader("Appearance")

st.toggle(
    "Dark mode",
    key="dark_mode"
)