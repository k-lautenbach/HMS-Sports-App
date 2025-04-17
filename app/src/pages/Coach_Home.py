import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title(f"Hi Jack!")
st.write('')
st.write("### What would you like to do today?")

if st.button('View Practices', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/Coach_Practices.py')

if st.button('View Games',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Coach_Games.py')

if st.button('View Strategies',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Coach_Strategies.py')

st.markdown("---")
st.subheader("🏀 Jack Bolton")

top = st.columns([2, 2, 1])

with top[0]:
    st.markdown("*East High Wildcats Boy's Varsity*")

with top[0]:
    st.image("assets/jackboltonpfp.jpeg", width=250)

with top[1]:
    st.markdown("### Contact")
    st.markdown("**Email**: jackbolton@easthigh.edu")
    st.markdown("**Phone**: 218-514-9123")
    
with top[1]:
    st.subheader("Info")
    st.markdown("""
    - **Years Coaching**: 5
    - **Season Record**: 20-5
    - **Recent Titles**: Regional Champs, State Champs
    """)

