import logging
import streamlit as st
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout='wide')
SideBarLinks()

PLAYER_ID = 1

st.title("Hi Troy,")
st.header("Getcha' Head in the Game! 🏀")

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
    st.header("📊 Stats")
    st.markdown("Track and update your on-court performance.")
    if st.button("View / Update Stats"):
        st.switch_page("pages/Athlete_Stats.py")

with col2:
    st.header("📅 Schedule")
    st.markdown("Keep up with games, practices, and recruiting events.")
    if st.button("View Schedule"):
        st.switch_page("pages/Athlete_Schedule.py")

st.markdown("---")

st.subheader("🏀 Profile")

profile_col1, profile_col2 = st.columns([3, 1])

with profile_col1:
    st.markdown(f"**Name:** {info['FirstName']} {info['LastName']}")
    st.markdown(f"**Gender:** {info['Gender']}")
    st.markdown(f"**GPA:** {info['GPA']}")
    st.markdown(f"**Grade Level:** {info['GradeLevel']}")
    st.markdown(f"**Height:** {info['Height']} ft")
    st.markdown(f"**Position:** {info['Position']}")
    st.markdown(f"**Recruitment Status:** {info['RecruitmentStatus']}")

with profile_col2:
    st.image("assets/troyboltonpfp.jpeg", width=500)

st.markdown("---")


