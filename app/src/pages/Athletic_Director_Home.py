# athletic director page
import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks



# set up page
logger = logging.getLogger(__name__)
st.set_page_config(
    layout="wide")

SideBarLinks()

st.title(f"Hi Director Ethan!")
st.write('')
st.subheader("How can we help you today?")
Ath_Dir_id = 101

if st.button('Contact Your Coaches', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/Athletic_Directors_Coaches.py')

if st.button('Add a Coach or Athlete',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Athletic_Director_Input.py')

if st.button('See and Manage East Highs Schedule',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Athletic_Director_Sched.py')

st.markdown("---")
st.header("Your Profile")
st.subheader('Ethan Wilson')

prof_layout = st.columns([2, 2, 1])

with prof_layout[0]:
    st.markdown("Athletic Director for East High")

with prof_layout[0]:
    st.image("assets/athletic_director.jpeg", width=250)

mid = st.columns(3)
school_name = 'East High'
api_url = 'http://api:4000/d/teams/'
params = {'high_school': school_name}

response = requests.get(api_url, params=params)
response.raise_for_status()

teams_data = response.json()
number_managed = len(teams_data)



with prof_layout[1]:
    st.markdown("Your Contact Info")
    st.text("Email: ethanwilson@easthigh.edu")
    st.text("Phone: 317-891-0001")

with prof_layout[1]:
    st.markdown(" ")


with prof_layout[1]:
    st.markdown("You Direct:")
    st.text("Total Teams: {number_manged}}")





