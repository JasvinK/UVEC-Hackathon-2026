
import streamlit as st

st.set_page_config(
    page_title="My Goals",
    page_icon="🎯",
    layout="wide"
)

st.title("My Goals")
st.subheader("UVEC Hackathon 2026")

st.write("Welcome! Your Streamlit frontend is working.")

name = st.text_input("Enter your name:")

if st.button("Click Me"):
    st.success(f"Hello, {name or 'World'}!")

st.divider()

st.sidebar.title("Navigation")
st.sidebar.write("Home")
st.sidebar.write("Settings")
