# athleticdirector schedule
# add events delete events
practices = requests.get("http://api:4000/sch/practices").json()
games = requests.get("http://api:4000/sch/games").json()