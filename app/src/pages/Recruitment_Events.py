import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Manage Recruitment Schedule")


# -----------------------------------------------
if st.button("View Upcoming Events"):
        api_url = "http://web-api:4000/r/recruiter/events"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    df = pd.DataFrame(data)
                    st.success(f"Found {len(df)} events!")
                    
                    st.dataframe(df)
                else:
                    st.warning("No players matched your criteria.")
            else:
                st.error(f"API error. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to API: {e}")



api_url = "http://web-api:4000/r/recruiter/event"

st.subheader("Add Recruiting Event")

with st.form("add_events"):
    datetime = st.text_input("DateTime (YYYY-MM-DD HH:MM:SS)", placeholder="e.g., 2025-04-20 15:30:00")
    location = st.text_input("Location", placeholder="e.g., Boston, MA")

    submitted = st.form_submit_button("Add Event")

    if submitted:
        payload = {
            "DateTime": datetime,
            "Location": location,
        }

        try:
            response = requests.post(api_url, json=payload)

            if response.status_code == 200:
                st.success("✅ Event added successfully!")
            else:
                try:
                    error_msg = response.json().get('error', 'Unknown server error.')
                except ValueError:
                    error_msg = response.text or 'No response body.'
                st.error(f"❌ Failed to add event. Status {response.status_code}: {error_msg}")
        except Exception as e:
            st.error(f"❗ Error connecting to API: {e}")


st.subheader("Delete Recruiting Event")
with st.form("delete_event"):
    eventid = st.text_input("EventID", placeholder="e.g., 1, 2, 3")

    submitted = st.form_submit_button("Cancel Event")

    if submitted:
        payload = {
            "EventID": eventid,
        }
        try:
            response = requests.delete(api_url, params=payload)  
            if response.status_code == 200:
                st.success("✅ Event canceled successfully!")
            else:
                try:
                    error_msg = response.json().get('error', 'Unknown server error.')
                except ValueError:
                    error_msg = response.text or 'No response body.'
                st.error(f"❌ Failed to cancel event. Status {response.status_code}: {error_msg}")
        except Exception as e:
            st.error(f"❗ Error connecting to API: {e}")
