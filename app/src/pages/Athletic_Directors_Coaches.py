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
            st.write(data[0])
            team_df = pd.DataFrame(data)
            st.success(f"Found {len(team_df)} coaches!")
            st.dataframe(team_df)
            st.write(team_df)
        else:
            st.warning("No coaches matched your criteria.")
    else:
        st.error(f"API error. Status code: {response.status_code}")
except Exception as e:
    st.error(f"Error connecting to API: {e}")


st.markdown("----")
st.subheader(f"Get Coach and Player Info")
team_id = st.text_input("Enter Team ID:")


if team_id:
    params = {'team_id': team_id}
    coach_url = f'http://web-api:4000/d/athletic_director/coaches'
    try:
        coach_response = requests.get(coach_url, params=params)
        if coach_response.status_code == 200:
            Cdata = coach_response.json()
            if Cdata:
                st.write(data[0])
                coach_df = pd.DataFrame(Cdata)
                st.success(f"Found {len(coach_df)} coaches!")
                st.dataframe(coach_df)
                coach_df['Email'] = coach_df['FirstName'].str.lower() + coach_df['LastName'].str.lower() + '@easthigh.edu'
                st.markdown("The Coach")
                top = st.columns([1,1])
                with top[0]:
                    st.write("Name", coach_df['FirstName'], coach_df['LastName'])
                with top[2]:
                    st.write("Contact At:", coach_df['Email'])
                st.markdown("----")
            else:
                st.warning("No coaches matched your criteria.")
        else:
            st.error(f"API error. Status code: {coach_response.status_code}")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")

    player_url = f'http://web-api:4000/d/athletic_director/players'
    try:
        player_response = requests.get(player_url, params=params)
        if player_response.status_code == 200:
            Pdata = player_response.json()
            if Pdata:
                st.write(data[0])
                player_df = pd.DataFrame(Pdata)
                st.success(f"Found {len(player_df)} players!")
                st.dataframe(player_df)
                st.markdown("The Players")
                top = st.columns([1,1])
                with top[0]:
                    st.write("Name", player_df['FirstName'], player_df['LastName'])
                with top[2]:
                    st.write("Contact At:", player_df['Email'])
            else:
                st.warning("No players matched your criteria.")
        else:
            st.error(f"API error. Status code: {player_response.status_code}")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")



