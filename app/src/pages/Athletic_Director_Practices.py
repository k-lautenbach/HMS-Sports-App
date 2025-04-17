import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

SideBarLinks()

st.title("East High Practices Manager⚽🎾🏀")
st.header("Complete Practice Schedule")
# athletic directors view all practices 
api_url = "http://web-api:4000/d/athletic_director/practices"

if st.button("Show Practices"):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data:
                df = pd.DataFrame(data)
                st.success(f"There are {len(df)} practices scheduled!")
                st.dataframe(df)
            else:
                st.warning("No events found.")
        else:
            st.error(f"API error. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")

# -----------------------------------------
# add practice to schedule 

st.header("📅 Schedule a Practice")

with st.form("add_practice"):
    datetime_input = st.text_input("DateTime (YYYY-MM-DD HH:MM:SS)", placeholder="e.g., 2025-04-20 15:30:00")
    location = st.text_input("Location", placeholder="e.g., East High Main Gym")
    teamname = st.text_input("TeamName", placeholder="e.g., Wildcats")

    submitted = st.form_submit_button("Add Practice")

    if submitted:
        payload = {
            "DateTime": datetime_input,
            "Location": location,
            "TeamName": teamname
        }

        try:
            response = requests.post(api_url, json=payload)

            if response.status_code == 200:
                st.success("✅ Practice added successfully!")

            elif response.status_code == 404:
                st.error("❌ Team not found!")

            elif response.status_code == 409:
                st.error("❌ Court is already booked!")

            else:
                st.error(f"❌ {response.text}")

        except Exception as e:
            st.error(f"❗ Error connecting to API: {e}")


#-------------------------------------------------
# delete a practice 
st.subheader("🗑️ Cancel Practice")
with st.form("delete_practice"):
    practice_id = st.text_input("PracticeID", placeholder="e.g., 1, 2, 3")

    submitted = st.form_submit_button("Cancel Practice")

    if submitted:
        payload = {
            "PracticeID": practice_id,
        }
        try:
            response = requests.delete(api_url, params=payload)  
            if response.status_code == 200:
                st.success("✅ Practice canceled successfully!")
            else:
                try:
                    error_msg = response.json().get('error', 'Unknown server error.')
                except ValueError:
                    error_msg = response.text or 'No response body.'
                st.error(f"❌ {error_msg}")
        except Exception as e:
            st.error(f"❗ Error connecting to API: {e}")
