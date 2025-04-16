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
api_url = 'http://api:4000/d/athletic_director/teams'
params = {'high_school': school_name}
response = requests.get(base_url, params=params)

def get_teams():
 try:
        response = requests.get(base_url, params=params)
        st.write(f"Response status: {response.status_code}")
        if response.status_code == 404:
            st.error("API endpoint not found. Please check if the backend server is running and the endpoint exists.")
            return []
        if response.ok:
            return response.json()
        else:
            st.error(f"API returned error: {response.status_code}")
            st.error(f"Response text: {response.text}")
            return []
 except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to API: {str(e)}")
        return []

teams = get_teams()
number_managed = len(teams) if teams else 0



with prof_layout[1]:
    st.markdown("Your Contact Info")
    st.text("Email: ethanwilson@easthigh.edu")
    st.text("Phone: 317-891-0001")

with prof_layout[1]:
    st.markdown(" ")


with prof_layout[1]:
    st.markdown("You Direct:")
    st.text("Total Teams: {number_manged}}")





