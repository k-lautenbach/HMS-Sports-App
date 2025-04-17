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
    st.switch_page('pages/Recruiter_Tool.py')

if st.button('Recommended Athletes',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Recruiter_AthleteRecs.py')

if st.button('Manage Event Schedules',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Recruiter_Events.py')

st.markdown("---")
st.subheader("🐻 Cal Goldstein")

top = st.columns([2, 2, 1])

with top[0]:
    st.markdown("*Golden Bears D1 Basketball*")

with top[0]:
    st.image("assets/recruiterpfp.jpeg", width=250)

with top[1]:
    st.markdown("### Contact")
    st.markdown('''**Email**: calgold@ucb.edu''')
    st.markdown('''**Phone**: 718-214-9182''')
    
with top[1]:
    st.subheader("Recruitment Criteria")
    st.markdown("""
    - **Grade**: High School Seniors and Juniors
    - **Positions**: Point Guard, Shooting Guard 
    - **States**: Utah, California, Colorado
    - **GPA Requirement**: 3.5
    """)

