# athletic director page
import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks



# set up page
logger = logging.getLogger(__name__)
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

SideBarLinks()

st.title("Welcome, Athletic Director!")