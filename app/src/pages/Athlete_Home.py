import logging
import streamlit as st
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout='wide')
SideBarLinks()

# Constants
PLAYER_ID = 1

st.title("Troy Bolton")

info = {
    "FirstName": "Troy",
    "LastName": "Bolton",
    "Gender": "Male",
    "GPA": 3.9,
    "GradeLevel": "11",
    "Height": "5'8\"",
    "Position": "Point Guard",
    "RecruitmentStatus": "Actice"
}

col1, col2 = st.columns(2)

with col1:
    st.header("Stats")
    st.markdown("Track and update your on-court performance.")
    if st.button("View / Update Stats"):
        st.switch_page("pages/02_Athlete_Stats.py")

with col2:
    st.header("Schedule")
    st.markdown("Keep up with games, practices, and recruiting events.")
    if st.button("View Schedule"):
        st.switch_page("pages/04_Schedule.py")

st.markdown("---")

st.subheader("Profile")
