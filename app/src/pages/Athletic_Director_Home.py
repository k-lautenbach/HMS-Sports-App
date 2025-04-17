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

if st.button('test api',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/TEST_API.py')

st.markdown("---")
st.header("Your Profile")
st.subheader('Ethan Wilson')

prof_layout = st.columns([2, 2, 1])

with prof_layout[0]:
    st.markdown("Athletic Director for East High")

with prof_layout[0]:
    st.image("assets/athletic_director.jpeg", width=250)

mid = st.columns(3)
<<<<<<< HEAD
# TEST API
import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks
import pandas as pd
SideBarLinks()
=======
school_name = 'East High'
api_url = 'http://api:4000/d/athletic_director/teams'
params = {'high_school': school_name}
response = requests.get(base_url, params=params)
>>>>>>> e013d9381d4c572e369c27c30ebad8ac63631b0f

st.write('test api connection')
api_url = 'http://web-api:4000/d/athletic_director/teams'

try:
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            st.success(f"Found {len(df)} events!")
            
            st.dataframe(df)
        else:
            st.warning("No players matched your criteria.")
    else:
        st.error(f"API error. Status code: {response.status_code}")
except Exception as e:
    st.error(f"Error connecting to API: {e}")

with prof_layout[1]:
    st.markdown("Your Contact Info")
    st.text("Email: ethanwilson@easthigh.edu")
    st.text("Phone: 317-891-0001")

with prof_layout[1]:
    st.markdown(" ")


with prof_layout[1]:
    st.markdown("You Direct:")
    st.text("Total Teams: {number_manged}}")





