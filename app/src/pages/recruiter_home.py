import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title(f"Hi Cal!")
st.write('')
st.write("### What would you like to do today?")

if st.button('Player Recruitment Tool', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/Recruitement_Tool.py')

if st.button('Recommended Athletes',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/03_Compare_Colleges.py')

if st.button('Manage Event Schedules',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/04_Schedule_And_Events.py')

st.markdown("---")
st.subheader("Cal Goldstein")

top = st.columns([2, 2, 1])

with top[0]:
    st.markdown("*Golden Bears D1 Basketball*")


with top[0]:
    st.image("assets/recruiterpfp.jpeg", width=250)


with top[1]:
    st.markdown("### Contact")
    st.text("Email: calgold@ucb.edu")
    st.text("Phone: 718-214-9182")
    
mid = st.columns(3)

with mid[0]:
    st.subheader("Events")
    st.markdown("""
    - **East High**: March 1st, 2025 @ 5:30pm
    
    """)

with top[1]:
    st.subheader("Recruitment Criteria")
    st.markdown("""
    - **Grade**: High School Seniors and Juniors
    - **Positions**: Point Guard, Shooting Guard 
    - **States**: Utah, California, Colorado
    - **GPA Requirement**: 3.5
    """)

