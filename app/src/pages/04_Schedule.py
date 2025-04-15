import streamlit as st
import requests
from datetime import datetime

st.set_page_config(layout="wide")
st.title("My Schedule")

practices = requests.get("http://api:4000/sch/practices").json()
games = requests.get("http://api:4000/sch/games").json()
events = requests.get("http://api:4000/sch/recruitingevents").json()

schedule = []

for practice in practices:
    schedule.append({
        "Type": "Practice",
        "Date": practice["Date"],
        "Time": practice.get("Time", "08:00"),
        "Location": practice.get("Location", "TBD")
    })

for game in games:
    schedule.append({
        "Type": "Game",
        "Date": game["Date"],
        "Time": game.get("Time", "18:00"),
        "Opponent": game.get("Opponent", "TBD"),
        "Location": game.get("Location", "TBD")
    })

for event in events:
    schedule.append({
        "Type": "Recruiting Event",
        "Date": event["Date"],
        "Time": event.get("Time", "12:00"),
        "College": event.get("CollegeName", "TBD"),
        "Location": event.get("Location", "TBD")
    })

schedule.sort(key=lambda x: datetime.strptime(x["Date"], "%Y-%m-%d"))
st.subheader("🗓️ Upcoming Events (Table View)")
st.dataframe(schedule)
