import streamlit as st


def apply_theme():

    # Create the dark_mode variable the first time the app runs
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    # If dark mode is turned on
    if st.session_state.dark_mode:

        st.markdown(
            """
            <style>
            .stApp {
                background-color: #0E1117;
                color: white;
            }

            h1, h2, h3, p, label {
                color: white !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Otherwise use light mode
    else:

        st.markdown(
            """
            <style>
            .stApp {
                background-color: white;
                color: black;
            }

            h1, h2, h3, p, label {
                color: black !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )