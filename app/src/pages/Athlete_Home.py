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


st.subheader("Profile")

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

# Compare Schools
st.header("Compare Schools")
st.markdown("Find your best fit")
if st.button("Compare Now"):
    st.switch_page("pages/Compare_Collges.py")
