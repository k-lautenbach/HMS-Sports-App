import streamlit as st
import requests

st.title("📊 Troy Bolton's Stats")

TROY_STATS_ID = 1
API_URL = f"http://api:4000/s/athletestats/{TROY_STATS_ID}"

response = requests.get(API_URL)
response.raise_for_status()
stats = response.json()

# Current
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

# Create New Stats
st.subheader("Add New Stats")

with st.form("create_stats"):
    player_id = st.number_input("Player ID", value=1)
    points_new = st.number_input("Total Points", value=0)
    games_new = st.number_input("Games Played", value=0)
    assists_new = st.number_input("Assists Per Game", value=0.0)
    rebounds_new = st.number_input("Rebounds", value=0)
    ppg_new = st.number_input("Points Per Game", value=0.0)
    ft_new = st.number_input("Free Throw %", value=0.0)
    highlights_new = st.text_input("Highlights URL")

    created = st.form_submit_button("Add New Stats Entry")
    if created:
        payload = {
            "PlayerID": player_id,
            "TotalPoints": points_new,
            "GamesPlayed": games_new,
            "AssistsPerGame": assists_new,
            "Rebounds": rebounds_new,
            "PointsPerGame": ppg_new,
            "FreeThrowPercentage": ft_new,
            "HighlightsURL": highlights_new
        }

        res = requests.post("http://api:4000/s/athletestats", json=payload)
        res.raise_for_status()
        st.success("✅ Stats Added Successfully!")
