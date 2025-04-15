import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title(f"Troy Bolton")
st.write('')
st.write("### Select Below")

if st.button('Stats', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/02_Athlete_Stats.py')

if st.button('Compare Colleges',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/03_Compare_Colleges.py')

if st.button('Manage Schedule',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/04_Schedule_And_Events.py')

st.markdown("---")
st.subheader("My Profile")

top = st.columns([2, 2, 1])

with top[0]:
    st.markdown("### Troy Bolton")
    st.text("Team: East High Wildcats")
    st.text("Age: 17")

with top[1]:
    st.image("assets/troyboltonpfp.webp", width=130)

with top[2]:
    st.markdown("### Athlete")
    st.text("Contact: troybolton@easthigh.edu")
    
mid = st.columns(3)

with mid[0]:
    st.subheader("Schedule")
    st.markdown("- Practice: Monday 4PM\n- Game: Fri 7PM\n- Recruiting Fair: Sat 2PM")

with mid[1]:
    st.subheader("Current Stats")
    st.markdown("""
    - **My Ranking**: #9  
    - **PPG**: 23.1  
    - **Team Record**: 20W - 5L
    """)

with mid[2]:
    st.subheader("Highlights")
    st.markdown("https://maxpreps.com/highlights/troybolton")

# Athlete
import requests
PLAYER_ID = 1

response = requests.get(f"http://api:4000/a/athlete/{PLAYER_ID}")
response.raise_for_status()
info = response.json()

st.subheader("Information")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"**GPA:** {info['GPA']}")
    st.markdown(f"**Grade Level:** {info['GradeLevel']}")
    st.markdown(f"**Height:** {info['Height']}")

with col2:
    st.markdown(f"**Position:** {info['Position']}")
    st.markdown(f"**Recruitment Status:** {info['RecruitmentStatus']}")