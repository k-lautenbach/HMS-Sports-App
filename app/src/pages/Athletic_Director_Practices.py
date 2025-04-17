import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks
# athletic directors view all practices 
if st.button("View Upcoming Events 📅"):
        api_url = "http://web-api:4000/d/recruiter/events"
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
