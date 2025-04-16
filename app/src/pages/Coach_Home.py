import streamlit as st
import requests
import logging

st.set_page_config(layout='wide')
logger = logging.getLogger(__name__)

st.title("Jack Bolton")

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Jack Bolton")
    st.markdown("**Head Coach, East High Basketball**")

with col2:
    st.image("assets/jackboltonpfp.jpeg", width=175)

st.markdown("---")

st.subheader("Practices")

# link to practice schedule page
if st.button("Practice Schedule", use_container_width=True):
    st.switch_page("pages/Practice_Schedule.py")

st.markdown("---")
st.subheader("Strategies/Plays")

if "strategies" not in st.session_state:
    st.session_state.strategies = [
        "Man-to-Man Defense",
        "Zone Defense",
        "Full Court Press"
    ]

# add/delete strategies with user input
action = st.radio("Select", ["Add", "Delete"], horizontal=True)
user_input = st.text_input("Strategy")

if st.button("Submit"):
    strategies = st.session_state.strategies

    if action == "Add" and user_input:
        strategies.append(user_input)
    elif action == "Delete" and user_input in strategies:
        strategies.remove(user_input)
    st.session_state.strategies = strategies

st.markdown("### Current Plays")
with st.container():
    for strat in st.session_state.strategies:
        st.markdown(f"- {strat}")
