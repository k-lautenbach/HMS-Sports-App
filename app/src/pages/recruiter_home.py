import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title(f"Cal Goldstein")
st.write('')
st.write("### Select Below")

if st.button('Stats', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/02_Athlete_Stats.py')

if st.button('Find Athletes',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/03_Compare_Colleges.py')

if st.button('Manage Event Schedule',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/04_Schedule_And_Events.py')

st.markdown("---")
st.subheader("My Profile")

top = st.columns([2, 2, 1])

with top[0]:
    st.image("assets/recruiterpfp.jpeg", width=250)

with top[1]:
    st.markdown("### Cal Goldstein")
    st.text("Recruiter For Cal State Men's D1 Basketball")


with top[2]:
    st.markdown("### Recruiter")
    st.text("Contact: calgold@ucb.edu")
    st.text("718-214-9182")
    
mid = st.columns(3)

with mid[0]:
    st.subheader("Events")
    st.markdown("- East High: Tuesday 3PM")

with mid[1]:
    st.subheader("Looking For")
    st.markdown("""
    - **Grade**: High School Seniors 
    - **Positions**: Point Guard, Shooting Guard 
    - **GPA Requirement**: 3.5
    """)

