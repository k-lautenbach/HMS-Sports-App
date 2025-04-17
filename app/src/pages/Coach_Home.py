import streamlit as st
import requests
import pandas as pd
import logging
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
logger = logging.getLogger(__name__)

SideBarLinks()

st.title("Jack Bolton")

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Jack Bolton")
    st.markdown("**Head Coach, East High Basketball**")

with col2:
    st.image("assets/jackboltonpfp.jpeg", width=175)

st.markdown("---")

st.subheader("Practices")

# link to practice schedule page
if st.button("Practice Schedule", use_container_width=True):
    st.switch_page("pages/Practice_Schedule.py")

st.markdown("---")
st.subheader("Strategies/Plays")


if st.button("View Team Strategies"):
        try:
            api_url = "http://web-api:4000/c/coach/strategies"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    df = pd.DataFrame(data)
                    st.success(f"Found {len(df)} Strategies!")
                    
                    st.dataframe(df)
                else:
                    st.warning("No players matched your criteria.")
            else:
                st.error(f"API error. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to API: {e}")


# Add user input new player
with st.expander("Player"):
    st.text_input("First Name")
    st.text_input("Last Name")
    st.text_input("Gender")
    st.text_input("GPA")
    st.text_input("Grade Level")
    st.text_input("Height")
    st.text_input("Position")
    st.text_input("Recruitment Status")

# Remove player using PlayerID
with st.expander("Remove Player"):
    st.text_input("Enter Player ID")
