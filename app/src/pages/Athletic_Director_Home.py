# athletic director page
import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks
import pandas as pd



# set up page
logger = logging.getLogger(__name__)
st.set_page_config(
    layout="wide")

SideBarLinks()

st.title(f"Hi Director Ethan!")
st.subheader("How can we help you today?")
Ath_Dir_id = 101

if st.button('View Coaches and Players', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/Athletic_Directors_Coaches.py')

if st.button('See and Manage East High Practices',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Athletic_Director_Practices.py')

st.markdown("---")
st.subheader("Ethan Wilson")

top = st.columns([2, 2, 1])

with top[0]:
    st.markdown("*East High Athletics*")

with top[0]:
    st.image("assets/athletic_director.jpeg", width=250)

with top[1]:
    st.markdown("### Contact")
    st.markdown('''**Email**: ethanwilson@easthigh.edu''')
    st.markdown('''**Phone**: 412-912-0182''')
    
with top[1]:
    st.subheader("Info")
    st.markdown("""
    - **Years of Experience**: 12
    - **Number of teams**: 5
    - **Favorite Sport**: Basketball
    """)

