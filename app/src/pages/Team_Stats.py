# 05_Team_Stats.py

import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")
SideBarLinks()

# Streamlit page setup
st.title("📊 Team Stats")

# Constants
TEAM_ID = 1
API_BASE = "http://api:4000"
PLAYER_API = f"{API_BASE}/a/players"
STATS_API = f"{API_BASE}/s/athletestats"
TEAM_API = f"{API_BASE}/t/teams/{TEAM_ID}"

# -------------------------------
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch from {url}: {e}")
        return []

def fetch_stats_by_player(player_id):
    try:
        url = f"{API_BASE}/s/athletestats/player/{player_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Could not fetch stats for player {player_id}: {e}")
        return None

# -------------------------------
# 🏀 Team Info

team_info = fetch_data(TEAM_API)
if team_info:
    st.subheader(f"{team_info['TeamName']} - {team_info['HighSchoolName']}")

# -------------------------------
# 📋 All Player Stats

players = fetch_data(PLAYER_API)
stats = fetch_data(STATS_API)

if players and stats:
    # Combine player data with their stats
    rows = []
    for player in players:
        stat = next((s for s in stats if s['PlayerID'] == player['PlayerID']), None)
        if stat:
            rows.append({
                "Name": f"{player['FirstName']} {player['LastName']}",
                "PlayerID": player['PlayerID'],
                "Position": player['Position'],
                "Grade": player['GradeLevel'],
                "Height": player['Height'],
                "GPA": player['GPA'],
                "Recruitment Status": player['RecruitmentStatus'],
                "Games Played": stat['GamesPlayed'],
                "Total Points": stat['TotalPoints'],
                "Points Per Game": stat['PointsPerGame'],
                "Assists Per Game": stat['AssistsPerGame'],
                "Rebounds": stat['Rebounds'],
                "Free Throw %": stat['FreeThrowPercentage'],
                "Highlights": stat['HighlightsURL']
            })

    df = pd.DataFrame(rows)

    st.subheader("📋 Team Table")
    st.dataframe(df)

    st.subheader("📊 Summary Stats")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Avg PPG", round(df["Points Per Game"].mean(), 1))
        st.metric("Avg Assists", round(df["Assists Per Game"].mean(), 1))
    with col2:
        st.metric("Avg Rebounds", round(df["Rebounds"].mean(), 1))
        st.metric("Avg GPA", round(df["GPA"].mean(), 2))
    with col3:
        st.metric("Avg FT %", f"{round(df['Free Throw %'].mean(), 1)}%")
        st.metric("Total Players", len(df))

# -------------------------------
# 👤 Individual Player Lookup

    st.subheader("🔍 View Individual Player Stats")

    player_options = {f"{p['FirstName']} {p['LastName']}": p['PlayerID'] for p in players}
    selected_name = st.selectbox("Choose a Player", list(player_options.keys()))
    selected_id = player_options[selected_name]

    player_stat = fetch_stats_by_player(selected_id)
    if player_stat:
        st.markdown(f"### 📈 Stats for {selected_name}")
        st.write({
            "Total Points": player_stat['TotalPoints'],
            "Games Played": player_stat['GamesPlayed'],
            "Points/Game": player_stat['PointsPerGame'],
            "Assists/Game": player_stat['AssistsPerGame'],
            "Rebounds": player_stat['Rebounds'],
            "Free Throw %": player_stat['FreeThrowPercentage'],
            "Highlights URL": player_stat['HighlightsURL'] or "N/A"
        })

        if player_stat['HighlightsURL']:
            st.markdown(f"[🎥 Watch Highlights]({player_stat['HighlightsURL']})", unsafe_allow_html=True)

else:
    st.warning("No player or stats data available.")
