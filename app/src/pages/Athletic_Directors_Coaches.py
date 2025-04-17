# Athletic Directors contact list
import streamlit as st
import requests
from modules.nav import SideBarLinks
import pandas as pd

st.title(f"Your Teams:")
SideBarLinks()

team_url = 'http://web-api:4000/d/athletic_director/teams'
try:
    response = requests.get(team_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            st.success(f"Found {len(df)} coaches!")
            st.dataframe(df)
        else:
            st.warning("No coaches matched your criteria.")
    else:
        st.error(f"API error. Status code: {response.status_code}")
except Exception as e:
    st.error(f"Error connecting to API: {e}")

#------------------------------------
# coach and player info

st.markdown("----")

st.title("👨‍🏫 Get Coach Info")

team_id = st.text_input("Enter Team ID:", placeholder="e.g., 1")

if st.button("Get Coach Info"):
    if not team_id:
        st.warning("Please enter a Team ID.")
    else:
        # Encode and build request
        encoded_id = requests.utils.quote(team_id)
        api_url = f"http://web-api:4000/d/athletic_director/coaches?team_id={encoded_id}"

        try:
            with st.spinner("Fetching coach data..."):
                response = requests.get(api_url)

            if response.status_code == 200:
                data = response.json()

                if data:
                    df = pd.DataFrame(data)
                    st.success(f"Found {len(df)} coach(es) for Team ID {team_id}")
                    st.dataframe(df)
                else:
                    st.info("No coach data found for this team.")
            else:
                st.error(f"❌ {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Could not contact API: {e}")

# shows a full team roster of a given team
st.title("Get Roster")
team_id = st.text_input("Enter Team ID", placeholder = "e.g. 1, 2")

if st.button("View Team Roster"):
    if not team_id:
        st.warning("Please enter a TeamID.")
    else:
        # Need to encode the team name for URL
        encoded_teamid = requests.utils.quote(team_id)
        api_url = f"http://web-api:4000/d/athletic_director/players?team_id={encoded_teamid}"
        
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    df = pd.DataFrame(data)
                    
                    column_order = ['PlayerID', 'FirstName', 'LastName', 'Gender', 'GradeLevel', 
                                   'GPA', 'Height', 'Position', 'RecruitmentStatus']
                    
                    df = df[[col for col in column_order if col in df.columns]]
                    
                    st.success(f"Found {len(df)} players on team '{team_id}'")
                    st.dataframe(df)
                else:
                    st.warning(f"Team '{team_id}' not found in the database. Please check the spelling or try another team name.")
            else:
                st.error(f"Failed to fetch data from the API. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to server: {e}")

