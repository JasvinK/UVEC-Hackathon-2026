#python3 -m streamlit run frontend/src/pages/1_Goals.py

import streamlit as st
import pandas as pd


# ---------------- GOALS PAGE ----------------

st.title("Goals")

st.write(
    "Welcome! Our goal is to help you organize and work toward your goals."
)

st.write(
    "Think of big goals you need to complete or want to accomplish. "
    "The app will help you track your progress."
)


# ---------------- COMMON GOALS ----------------

# Example goals the user can choose from
common_goals = [
    "Get on top of School",
    "Improve Fitness",
    "Get Organized",
    "Learn a New Hobby"
]


# ---------------- SESSION STATE ----------------

# Controls whether the common goals list is displayed
if "show_premade_goals_list" not in st.session_state:
    st.session_state.show_premade_goals_list = False

# Controls whether options for creating your own goal are displayed
if "show_time_options" not in st.session_state:
    st.session_state.show_time_options = False


# ---------------- GOAL INPUT ----------------

# User can type a custom goal
goal = st.text_input(
    "Name a goal you would like to accomplish"
)


# Button to show premade goals
if st.button("Choose from common goals"):
    st.session_state.show_premade_goals_list = True
    st.session_state.show_time_options = False


# Button to create your own goal
if st.button("Add your own goal"):
    st.session_state.show_time_options = True
    st.session_state.show_premade_goals_list = False


# Show the common goals dropdown
if st.session_state.show_premade_goals_list:
    goal_name = st.selectbox(
        "Choose from a list of common goals",
        common_goals
    )