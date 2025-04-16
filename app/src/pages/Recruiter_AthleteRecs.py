import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Recommended Athletes ⛹️‍♂️")

# -----------------------------------------------
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

positions = ["Point Guard", "Guard", "Center", "Shooting Guard", 'Forward']

# -----------------------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    selected_position = st.multiselect("What position are you looking for?", positions)
with col2:
    selected_state = st.multiselect("Where do you want your player to be from?", states)
with col3:
    gpa = st.number_input("What should be their minimum GPA?", min_value=0.0, max_value=4.0, step=0.1)

# -----------------------------------------------
if st.button("Get Players"):
    if not selected_state or not selected_position or gpa is None:
        st.warning("Please select at least one state, one position, and enter a minimum GPA.")
    else:
        api_url = "http://web-api:4000/r/recruiter/player_criteria"

        params = []
        for state in selected_state:
            params.append(("State", state))
        for pos in selected_position:
            params.append(("Position", pos))
        params.append(("GPA", gpa))

        try:
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                data = response.json()
                if data:
                    df = pd.DataFrame(data)
                    st.success(f"Found {len(df)} players matching your criteria.")
                    column_order = ['PlayerID', 'FirstName', 'LastName', 'GradeLevel', 
                                    'GPA', 'Position', 'RecruitmentStatus']
                    
                    df = df[[col for col in column_order if col in df.columns]]
                    st.dataframe(df)
                else:
                    st.warning("No players matched your criteria.")
            else:
                st.error(f"API error. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to API: {e}")
