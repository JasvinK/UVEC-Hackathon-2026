# python -m streamlit run frontend/src/App.py
import streamlit as st
import pandas as pd
import numpy as np

import sys
sys.path.append("backend/main.py")
from main import Node, make_sample_goals, COMMON_GOALS

import json
from pathlib import Path



# streamlit overhead 
st.set_page_config(
    page_title="Task",
    layout="wide"
)



# '''
# What each entry needs:
# - name (given by user)
# - category (selected by user)
# - context (user)
# - timeframe ()
# - todays_goal () 

# # '''

# title of page
st.subheader("UVEC Hackathon 2026")
goals_file = Path("goals.json")

# times = pd.DataFrame({
#   'first column': ["daily", "weekly", "monthly", "other"],
# })


# # # these will be the goal names
# # common_goals = ["Get on top of School", "Improve Fitness", "Get Organized", "Learn a New Hobby"]

# we have a json file that loads the goals
def load_goals():
    if goals_file.exists():
        return json.loads(goals_file.read_text())
    return []

# save to the json
def save_goals():
    goals_file.write_text(json.dumps(st.session_state.goals, indent=2))


# session state
if "goals" not in st.session_state:
    st.session_state.goals = load_goals()
if "mode" not in st.session_state:
    st.session_state.mode = None

st.write("Welcome! Our goal is to help you align and work on your goals.")

# # categories = pd.DataFrame({'first column': [1, 2, 3, 4]})

# st.write("Think of goals (Big Goals) of things you need to do or want to accomplish. Our site will keep track of them for you and allow you to see your improvement")

# # look_at_catalog
# # mental health is about self imrpovement
# if st.button("Choose from common goals"):
#     st.session_state.show_premade_goals_list = True
#     st.session_state.show_time_options = False

# if st.button("Add your own goals"):
#     st.session_state.show_time_options = True
#     st.session_state.show_premade_goals_list = False

#     goal = st.text_input("Name a goal you would like to accomplish or choose from a list of common goals")


# two buttons for preloading or making new
c1, c2 = st.columns(2)
if c1.button("Choose from common goals"):
    st.session_state.mode = "common"
if c2.button("Add your own goal"):
    st.session_state.mode = "custom"

# if either button is pressed 
if st.session_state.mode:
    # add the goal after filling out form
    with st.form("add_goal", clear_on_submit=True):
        if st.session_state.mode == "common":
            name = st.selectbox("Choose a common goal", COMMON_GOALS)
        else:
            name = st.text_input("Name your goal")

        # include addional extra info
        category = st.selectbox("Category", ["School", "Fitness", "Organization", "Hobby", "Other"])
        timeframe = st.selectbox("How often?", ["daily", "weekly", "monthly", "other"])
        context = st.text_area("Context (optional)")

        if st.form_submit_button("Save goal"):
            if name.strip():
                st.session_state.goals.append({
                    "name": name.strip(),
                    "category": category,
                    "timeframe": timeframe,
                    "context": context,
                    "done": 0,
                    "total": 20,
                })
                save_goals()
                st.success("Goal saved!")
            else:
                st.warning("Please enter a goal name.")


# done, total = 13, 20
# st.progress(done / total, text=f"{done}/{total} days completed")


# st.metric("Current streak", "7 days", "+2")

# neither button pressed
if not st.session_state.goals:
    st.info("No goals yet. Add one above.")

# go through the list of goals and print
for i, g in enumerate(st.session_state.goals):
    with st.container(border=True):
        left, right = st.columns([5, 1])
        # markdown format printing (this we used Claude to generate because we ain't doing that)
        left.markdown(f"**{g['name']}**  ·  {g['category']}  ·  {g['timeframe']}")
        if g["context"]:
            left.caption(g["context"])
        left.progress(g["done"] / g["total"], text=f"{g['done']}/{g['total']} completed")

        if right.button("Mark done", key=f"done_{i}"):
            g["done"] = min(g["done"] + 1, g["total"])
            save_goals()
            st.rerun()
        if right.button("Delete", key=f"del_{i}"):
            st.session_state.goals.pop(i)
            save_goals()
            st.rerun()



# st.divider()

# st.sidebar.title("Profile")
# st.sidebar.title("Settings")

