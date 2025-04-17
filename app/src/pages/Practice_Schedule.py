import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

st.title("Team Schedule")

TEAM_ID = 1
PLAYER_ID = 1
API_URL = "http://api:4000/cal/calendar"

# -------------------------------
def get_data(endpoint, params):
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()

# -------------------------------
st.subheader("Practices")
practices = get_data(f"{API_URL}/practices", {"team_id": TEAM_ID})
df_practices = pd.DataFrame(practices)
st.dataframe(df_practices)

# -------------------------------
st.subheader("Upcoming Games")
games = get_data(f"{API_URL}/games", {"team_id": TEAM_ID})
df_games = pd.DataFrame(games)
st.dataframe(df_games)
