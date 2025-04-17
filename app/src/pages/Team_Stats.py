import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Streamlit page setup
st.set_page_config(layout="wide")
st.title("🏀 Team Statistics")

# Add navigation
SideBarLinks()

# Constants
API_BASE = "http://api:4000"

# -------------------------------
# 🔄 Helper Functions
# -------------------------------
def fetch_team_info(team_id):
    try:
        response = requests.get(f"{API_BASE}/t/teams/{team_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch team information: {e}")
        return None

def fetch_team_players(team_id):
    try:
        response = requests.get(f"{API_BASE}/a/players/{team_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch team players: {e}")
        return []

def fetch_player_stats_by_id(player_id):
    try:
        response = requests.get(f"{API_BASE}/s/athletestats/player/{player_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch player stats: {e}")
        return None

def fetch_all_player_stats():
    try:
        response = requests.get(f"{API_BASE}/s/athletestats")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch all player stats: {e}")
        return []

# -------------------------------
# 🏀 Team Selection
# -------------------------------
st.subheader("Select Team")
team_id = st.number_input("Team ID", min_value=1, value=1, step=1)

team_data = fetch_team_info(team_id)
if team_data:
    st.write(f"### {team_data['TeamName']} - {team_data['HighSchoolName']}")

# -------------------------------
# 📊 Player Statistics Table
# -------------------------------
st.subheader("All Player Statistics")

players = fetch_team_players(team_id)

if not players:
    st.info("No players found for this team.")
else:
    all_stats = fetch_all_player_stats()
    player_stats_data = []

    for player in players:
        stats = [s for s in all_stats if s['PlayerID'] == player['PlayerID']]
        if stats:
            stat = stats[0]
            player_stats_data.append({
                'Player ID': player['PlayerID'],
                'Name': f"{player['FirstName']} {player['LastName']}",
                'Position': player['Position'],
                'Grade': player['GradeLevel'],
                'Height': player['Height'],
                'GPA': player['GPA'],
                'Gender': player['Gender'],
                'Recruitment Status': player['RecruitmentStatus'],
                'Games Played': stat['GamesPlayed'],
                'Total Points': stat['TotalPoints'],
                'Points Per Game': stat['PointsPerGame'],
                'Assists Per Game': stat['AssistsPerGame'],
                'Rebounds': stat['Rebounds'],
                'Free Throw %': stat['FreeThrowPercentage'],
                'Highlights': stat['HighlightsURL']
            })

    if player_stats_data:
        df = pd.DataFrame(player_stats_data)

        # Filters
        st.subheader("Filter Players")
        col1, col2, col3 = st.columns(3)
        with col1:
            position_filter = st.multiselect("Position", df['Position'].unique(), df['Position'].unique())
        with col2:
            grade_filter = st.multiselect("Grade", df['Grade'].unique(), df['Grade'].unique())
        with col3:
            recruit_filter = st.multiselect("Recruitment Status", df['Recruitment Status'].unique(), df['Recruitment Status'].unique())

        filtered_df = df[
            (df['Position'].isin(position_filter)) &
            (df['Grade'].isin(grade_filter)) &
            (df['Recruitment Status'].isin(recruit_filter))
        ]

        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Player ID": st.column_config.NumberColumn(format="%d"),
                "GPA": st.column_config.NumberColumn(format="%.2f"),
                "Points Per Game": st.column_config.NumberColumn(format="%.1f"),
                "Assists Per Game": st.column_config.NumberColumn(format="%.1f"),
                "Free Throw %": st.column_config.NumberColumn(format="%.1f%%"),
                "Highlights": st.column_config.LinkColumn("Watch Highlights")
            }
        )

        # Team Summary
        st.subheader("Team Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Players", len(player_stats_data))
            st.metric("Avg Points/Game", round(df['Points Per Game'].mean(), 1))
        with col2:
            st.metric("Avg Assists/Game", round(df['Assists Per Game'].mean(), 1))
            st.metric("Avg Rebounds", round(df['Rebounds'].mean(), 1))
        with col3:
            st.metric("Avg Free Throw %", f"{round(df['Free Throw %'].mean(), 1)}%")
            st.metric("Avg GPA", round(df['GPA'].mean(), 2))

        # Player Cards
        st.subheader("📋 Individual Player Cards")
        for _, row in filtered_df.iterrows():
            with st.expander(f"{row['Name']} — {row['Position']} | Grade: {row['Grade']}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"**GPA:** {row['GPA']}")
                    st.markdown(f"**Height:** {row['Height']}")
                    st.markdown(f"**Gender:** {row['Gender']}")
                    st.markdown(f"**Recruitment Status:** {row['Recruitment Status']}")
                with col2:
                    st.markdown(f"**Games Played:** {row['Games Played']}")
                    st.markdown(f"**Total Points:** {row['Total Points']}")
                    st.markdown(f"**Points/Game:** {row['Points Per Game']}")
                    st.markdown(f"**Assists/Game:** {row['Assists Per Game']}")
                with col3:
                    st.markdown(f"**Rebounds:** {row['Rebounds']}")
                    st.markdown(f"**Free Throw %:** {row['Free Throw %']}%")
                    if row['Highlights']:
                        st.markdown(f"[🎥 Watch Highlights]({row['Highlights']})", unsafe_allow_html=True)
                    else:
                        st.markdown("_No highlights link available_")

# -------------------------------
# 🔍 View Stats for Specific Player
# -------------------------------
st.subheader("🔍 View Stats for a Specific Player")

if players:
    player_names = {f"{p['FirstName']} {p['LastName']}": p['PlayerID'] for p in players}
    selected_name = st.selectbox("Choose a Player", list(player_names.keys()))
    selected_id = player_names[selected_name]

    stat = fetch_player_stats_by_id(selected_id)
    if stat:
        st.markdown(f"### 📊 Stats for {selected_name}")
        st.write({
            "Total Points": stat['TotalPoints'],
            "Games Played": stat['GamesPlayed'],
            "Assists/Game": stat['AssistsPerGame'],
            "Rebounds": stat['Rebounds'],
            "Points/Game": stat['PointsPerGame'],
            "Free Throw %": stat['FreeThrowPercentage'],
            "Highlights URL": stat['HighlightsURL'] or "N/A"
        })

        if stat['HighlightsURL']:
            st.markdown(f"[🎥 Watch Highlights]({stat['HighlightsURL']})", unsafe_allow_html=True)
    else:
        st.warning("No stats available for selected player.")
