import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Player Recruitment Tool ⛹️‍♂️")

#------------------------------------------------------------------
# Finds basketball teams in a specific state
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
]

selected_state = st.selectbox("Find A Team By State ", states)

if st.button("Get Basketball Teams"):
    api_url = f"http://web-api:4000/r/recruiter/state_teams?state={selected_state}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data:
                df = pd.DataFrame(data)
                st.success(f"Found {len(df)} basketball teams in {selected_state}")
                st.dataframe(df)
            else:
                st.warning(f"No basketball teams found in {selected_state}.")
        else:
            st.error(f"Failed to fetch data from the API. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error connecting to server: {e}")


#------------------------------------------------------------------
# shows a full team roster of a given team

team_name = st.text_input("Enter Team Name")

if st.button("View Team Roster"):
    if not team_name:
        st.warning("Please enter a team name.")
    else:
        # Need to encode the team name for URL
        encoded_team_name = requests.utils.quote(team_name)
        api_url = f"http://web-api:4000/r/recruiter/roster?team={encoded_team_name}"
        
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    df = pd.DataFrame(data)
                    
                    column_order = ['PlayerID', 'FirstName', 'LastName', 'Gender', 'GradeLevel', 
                                   'GPA', 'Height', 'Position', 'RecruitmentStatus', 'ContactID']
                    
                    df = df[[col for col in column_order if col in df.columns]]
                    
                    st.success(f"Found {len(df)} players on team '{team_name}'")
                    st.dataframe(df)
                else:
                    st.warning(f"Team '{team_name}' not found in the database. Please check the spelling or try another team name.")
            else:
                st.error(f"Failed to fetch data from the API. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to server: {e}")


#------------------------------------------------------------------
# shows player statistics of a given player 
st.title("Player Stats 🏀")

# ask for first and last name
col1, col2 = st.columns(2)
with col1:
    first_name = st.text_input("First Name")
with col2:
    last_name = st.text_input("Last Name")

if st.button("Get Player Stats"):
    if not first_name or not last_name:
        st.warning("Please enter both first and last name.")
    else:
        encoded_first_name = requests.utils.quote(first_name)
        encoded_last_name = requests.utils.quote(last_name)
        
        api_url = f"http://web-api:4000/r/recruiter/player_stats?first_name={encoded_first_name}&last_name={encoded_last_name}"
        
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    df = pd.DataFrame(data)
                    
                    st.success(f"Found stats for {first_name} {last_name}")
                    
                    player_info = data[0] if data else {}
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Player Information")
                        st.write(f"**Name:** {player_info.get('FirstName', '')} {player_info.get('LastName', '')}")
                        st.write(f"**Team:** {player_info.get('TeamName', '')}")
                        st.write(f"**Position:** {player_info.get('Position', '')}")
                        st.write(f"**Grade:** {player_info.get('GradeLevel', '')}")
                        st.write(f"**Height:** {player_info.get('Height', '')} inches")
                    
                    with col2:
                        st.subheader("Performance Stats")
                        st.write(f"**Points Per Game:** {player_info.get('PointsPerGame', '')}")
                        st.write(f"**Total Points:** {player_info.get('TotalPoints', '')}")
                        st.write(f"**Games Played:** {player_info.get('GamesPlayed', '')}")
                        st.write(f"**Assists Per Game:** {player_info.get('AssistsPerGame', '')}")
                        st.write(f"**Rebounds:** {player_info.get('Rebounds', '')}")
                        st.write(f"**Free Throw %:** {player_info.get('FreeThrowPercentage', '')}%")
                    
                        st.subheader("Player Highlights")
                        st.markdown(f"[Watch Highlights]({player_info['HighlightsURL']})")
      
                else:
                    st.warning(f"No stats found for player '{first_name} {last_name}'. Please check the spelling or try another player.")
            else:
                st.error(f"Failed to fetch data from the API. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to server: {e}")