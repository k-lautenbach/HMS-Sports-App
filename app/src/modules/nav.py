import streamlit as st

# ------------------------ Navigation Configurations ------------------------

NAV_CONFIG = {
    "athletic_director": [
        ("pages/Athletic_Director_Home.py", "Athletic Director Home", "🧑‍💻"),
        ("pages/Athletic_Directors_Coaches.py", "View Staff & Teams", "🧍‍♂️"),
        ("pages/Athletic_Director_Practices.py", "Practices", "📅"),



    ],
    "coach": [
        ("pages/Coach_Home.py", "Coach Home", "🧑‍💻"),
        ("pages/Coach_Practices.py", "Practices", "📅"),
        ("pages/Coach_Games.py", "Games", "🏆"),
        ("pages/Coach_Strategies.py", "Strategies", "🗒️")
    ],
    "athlete": [
        ("pages/Athlete_Home.py", "Athlete Home", "🧑‍💻"),
        ("pages/Athlete_Schedule.py", "Schedule", "📅"),
        ("pages/Athlete_Stats.py", "My Stats", "🏃‍♂️"),
    ],
    "recruiter": [
        ("pages/Recruiter_Home.py", "Recruiter Home", "🧑‍💻"),
        ("pages/Recruiter_AthleteRecs.py", "Recommended Athletes", "🏃‍♂️"),
        ("pages/Recruitment_Tool.py", "Recruitment Tool", "🛠️"),
        ("pages/Recruitment_Events.py", "Recruitment Events", "📅")
    ]
}

# ------------------------ Individual Page Navs ------------------------

def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")

def AboutPageNav():
    st.sidebar.page_link("pages/About.py", label="About", icon="❓")

# ------------------------ Main Navigation Sidebar ------------------------

def SideBarLinks(show_home=False):
    # Logo for sidebar
    st.sidebar.image("assets/bfa.logo.png", width=150)

    # Ensures session_state has default values
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.switch_page("Home.py")

    # Welcome message (if logged in)
    if st.session_state["authenticated"] and "first_name" in st.session_state:
        st.sidebar.markdown(f"👋 Welcome, **{st.session_state['first_name']}**!")

    # Show Home link at top if show_home is requested
    if show_home:
        HomeNav()

    # Role-based nav links
    if st.session_state["authenticated"] and "role" in st.session_state:
        role = st.session_state["role"]

        if role in NAV_CONFIG:
            for path, label, icon in NAV_CONFIG[role]:
                st.sidebar.page_link(path, label=label, icon=icon)
        else:
            st.sidebar.warning("⚠️ Unknown role. Please return to Home.")
    elif st.session_state["authenticated"]:
        st.sidebar.warning("⚠️ Missing user role. Please return to Home.")

 
    # About page
    AboutPageNav()

    # Logout button
    if st.session_state["authenticated"]:
        if st.sidebar.button("Logout"):
            for key in ["role", "authenticated", "first_name"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.switch_page("Home.py")
