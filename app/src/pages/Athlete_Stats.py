import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()

st.title("📈 Troy Bolton's Stats")

TROY_STATS_ID = 1
API_URL = f"http://api:4000/s/athletestats/{TROY_STATS_ID}"

# Get current stats
response = requests.get(API_URL)
response.raise_for_status()
stats = response.json()

# Current
if stats:
    st.subheader("Current Stats")
    st.dataframe([stats])

# Update
st.subheader("Update Stats")
with st.form("update_stats"):
    points = st.number_input("Total Points", value=stats.get("TotalPoints", 0))
    games = st.number_input("Games Played", value=stats.get("GamesPlayed", 0))
    assists = st.number_input("Assists Per Game", value=stats.get("AssistsPerGame", 0.0))
    rebounds = st.number_input("Rebounds", value=stats.get("Rebounds", 0))
    ppg = st.number_input("Points Per Game", value=stats.get("PointsPerGame", 0.0))
    ft = st.number_input("Free Throw %", value=stats.get("FreeThrowPercentage", 0.0))
    highlights = st.text_input("Highlights URL", value=stats.get("HighlightsURL", ""))

    updated = st.form_submit_button("Update Stats")
    if updated:
        payload = {
            "TotalPoints": points,
            "GamesPlayed": games,
            "AssistsPerGame": assists,
            "Rebounds": rebounds,
            "PointsPerGame": ppg,
            "FreeThrowPercentage": ft,
            "HighlightsURL": highlights
        }

        res = requests.put(API_URL, json=payload)
        res.raise_for_status()
        st.success("Stats Updated")

