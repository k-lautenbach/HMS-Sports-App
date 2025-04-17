# 04_Schedule.py

import streamlit as st
import requests
import pandas as pd

# Streamlit page setup
st.set_page_config(layout="wide")
st.title("📅 My Schedule")

# Constants (could be dynamically set by login/session later)
TEAM_ID = 1
PLAYER_ID = 1
API_BASE = "http://api:4000/cal/calendar"

# -------------------------------
# 🔄 Safe fetch helper function
# -------------------------------
def fetch_schedule_data(endpoint, params):
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch from {endpoint}: {e}")
        return []

# -------------------------------
# 🏀 Team Practices Section
# -------------------------------
st.subheader("🏀 Team Practices")

practices = fetch_schedule_data(f"{API_BASE}/practices", {"team_id": TEAM_ID})
if practices:
    df_practices = pd.DataFrame(practices)
    st.dataframe(df_practices)
else:
    st.info("No upcoming practices scheduled.")

# -------------------------------
# 🎯 Upcoming Games Section
# -------------------------------
st.subheader("🎯 Upcoming Games")

games = fetch_schedule_data(f"{API_BASE}/games", {"team_id": TEAM_ID})
if games:
    df_games = pd.DataFrame(games)
    st.dataframe(df_games)
else:
    st.info("No upcoming games scheduled.")

# -------------------------------
# 🧲 Recruiting Events Section
# -------------------------------
st.subheader("🧲 Recruiting Events")

events = fetch_schedule_data(f"{API_BASE}/recruitingevents", {"player_id": PLAYER_ID})
if events:
    df_events = pd.DataFrame(events)
    st.dataframe(df_events)
else:
    st.info("No recruiting events scheduled.")
