import streamlit as st

# ------------------------ Navigation Configurations ------------------------

NAV_CONFIG = {
    "athletic_director": [
        ("pages/Athletic_Director_Home.py", "Athletic Director Home", "🧍‍♂️")
    ],
    "coach": [
        ("pages/Coach_Home.py", "Coach Home", "👨‍💼")
    ],
    "athlete": [
        ("pages/Athlete_Home.py", "Athlete Home", "🏃‍♂️")
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
    # Add logo to sidebar
    st.sidebar.image("assets/bfa.logo.png", width=150)

    # Ensure session_state has default values
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.switch_page("Home.py")

    # Optional: Welcome message if logged in
    if st.session_state["authenticated"] and "first_name" in st.session_state:
        st.sidebar.markdown(f"👋 Welcome, **{st.session_state['first_name']}**!")

    # Show Home nav link if specified
    if show_home:
        HomeNav()

    # Show role-based links if authenticated
    if st.session_state["authenticated"] and "role" in st.session_state:
        role = st.session_state["role"]

        if role in NAV_CONFIG:
            for path, label, icon in NAV_CONFIG[role]:
                st.sidebar.page_link(path, label=label, icon=icon)
        else:
            st.sidebar.warning("⚠️ Unknown role. Please return to Home.")
    elif st.session_state["authenticated"]:
        st.sidebar.warning("⚠️ Missing user role. Please return to Home.")

    # Always show the About page
    AboutPageNav()

    # Logout button if logged in
    if st.session_state["authenticated"]:
        if st.sidebar.button("Logout"):
            for key in ["role", "authenticated", "first_name"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.switch_page("Home.py")
