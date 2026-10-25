# Run: python3 -m streamlit run frontend/src/Dashboard.py
import streamlit as st
from theme import apply_theme

apply_theme()

# Sets up the dashboard page
st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

# ---------------- DASHBOARD HEADER ----------------

st.title("Dashboard")
st.write("Welcome back 👋")


# ---------------- ACTIVE GOALS ----------------

st.subheader("Active Goals")

# Temporary goal 1
st.write("School")
st.progress(40)
st.caption("40% complete")

# Temporary goal 2
st.write("Personal Goals")
st.progress(25)
st.caption("25% complete")


st.divider()


# ---------------- ACTIVITY TRACKER ----------------

st.subheader("Your Progress")
st.write("Your activity over the last few weeks")

# Temporary activity data
# Each row represents one week
# 1 = activity that day
# 0 = no activity that day
activity = [
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0]
]

# Go through every week
for week in activity:

    # Make 7 columns for the 7 days of the week
    columns = st.columns(7)

    # Go through every day in the week
    for i, day in enumerate(week):

        with columns[i]:

            # Activity happened
            if day == 1:
                st.write("🟩")

            # No activity
            else:
                st.write("⬜")