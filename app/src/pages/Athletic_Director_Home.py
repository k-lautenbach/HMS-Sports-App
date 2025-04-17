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
st.write('')
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
st.header("Your Profile")
st.subheader('Ethan Wilson')

prof_layout = st.columns([2, 2, 1])

with prof_layout[0]:
    st.markdown("Athletic Director for East High")

with prof_layout[0]:
    st.image("assets/athletic_director.jpeg", width=250)

mid = st.columns(3)


with prof_layout[1]:
    st.markdown("Your Contact Info")
    st.text("Email: ethanwilson@easthigh.edu")
    st.text("Phone: 317-891-0001")

with prof_layout[1]:
    st.markdown(" ")

try:
    api_url = 'http://web-api:4000/d/athletic_director/teams'
    number_managed = 0
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            st.success(f"Found {len(df)} events!")
            number_managed = len(df)
        else:
            st.warning("No players matched your criteria.")
    else:
        st.error(f"API error. Status code: {response.status_code}")
except Exception as e:
    st.error(f"Error connecting to API: {e}")

with prof_layout[1]:
    st.markdown("You Direct:")
    st.text(f"Total Teams: {number_managed}")





