import streamlit as st
import requests
import pandas as pd
import logging
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
logger = logging.getLogger(__name__)

SideBarLinks()

st.title("🗒️ Strategies/Plays")

try:
    api_url = "http://web-api:4000/c/coach/strategies"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)                    
            st.dataframe(df)
        else:
            st.warning("No players matched your criteria.")
    else:
        st.error(f"API error. Status code: {response.status_code}")
except Exception as e:
    st.error(f"Error connecting to API: {e}")