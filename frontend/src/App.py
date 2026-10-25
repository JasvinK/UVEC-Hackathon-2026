# python -m streamlit run frontend/src/App.py
import streamlit as st
import pandas as pd
import numpy as np

import sys
sys.path.append("../../../backend/main.py")

# streamlit overhead 
st.set_page_config(
    page_title="Task",
    layout="wide"
)

# '''
# What each entry needs:
# - id (surogate key made elsewhere)
# - name (given by user)
# - category (selected by user)
# - context (user)
# - timeframe ()
# - todays_goal () 

# '''

# title of page
# st.subheader("UVEC Hackathon 2026")

times = pd.DataFrame({
  'first column': ["daily", "weekly", "monthly", "other"],
})


# these will be the goal names
common_goals = ["Get on top of School", "Improve Fitness", "Get Organized", "Learn a New Hobby"]

if "show_options" not in st.session_state:
    st.session_state.show_options = False

if "show_premade_goals_list" not in st.session_state:
    st.session_state.show_premade_goals_list = False

st.write("Welcome to the __, our goal is to help you align and work on your goals. ")


# categories = pd.DataFrame({'first column': [1, 2, 3, 4]})

st.write("Think of goals (Big Goals) fo things you need to do or want to accomplish. Ou site will keep track of them for you and allow you to see your improvement")
goal = st.text_input("Name a goal you would like to accomplish or choose from a list of common goals")

# look_at_catalog
# mental health is about self imrpovement
if st.button("Choose from common goals"):
    st.session_state.show_premade_goals_list = True
    st.session_state.show_time_options = False

if st.button("Add your own goals"):
    st.session_state.show_time_options = True
    st.session_state.show_premade_goals_list = False


if st.session_state.show_premade_goals_list:
    goal_name = st.selectbox("Choose from a list of common goals", common_goals)



# if st.session_state.show_options:
#     st.write("goal: " + goal)
#     goal_type = st.radio("Goal type", ["Single time goal", "Recurring goal"])

#     if goal_type == "Recurring goal":
#         frequency = st.selectbox("How frequent?", common_goals)


done, total = 13, 20
st.progress(done / total, text=f"{done}/{total} days completed")


st.metric("Current streak", "7 days", "+2")



st.divider()

st.sidebar.title("Profile")
st.sidebar.title("Settings")