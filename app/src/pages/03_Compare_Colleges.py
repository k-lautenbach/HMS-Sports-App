import streamlit as st
import requests

st.title("Compare Colleges")

colleges = requests.get("http://api:4000/ct/collegeteams").json()
name = [c['Name'] for c in colleges]

# Compare drop-down
selected = st.multiselect("Choose schools to compare side-by-side", name)

if selected:
    comparison = [c for c in colleges if c['Name'] in selected]
    st.dataframe(comparison)