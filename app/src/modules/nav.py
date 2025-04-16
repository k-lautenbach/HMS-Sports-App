# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/About.py", label="About", icon="❓")


#### ------------------------ Role of Athletic Director ------------------------
def AthleticDirectorHomeNav():
    st.sidebar.page_link(
        "pages/Athletic_Director_Home.py", label="Athletic Director Home", icon="🧍‍♂️"
    )


## ------------------------ Role of Coach ------------------------
def CoachHomeNav():
    st.sidebar.page_link(
        "pages/Coach_Home.py", label="Coach Home", icon="👨‍💼"
    )


#### ------------------------ Role of Player ------------------------
def AthletesHomeNav():
     st.sidebar.page_link(
        "pages/Athlete_Home.py", label="Athlete Home", icon="🏃‍♂️"
    )

#### ------------------------ Role of Recruiter ------------------------
def RecruiterHomeNav():
     st.sidebar.page_link(
        "pages/Recruiter_Home.py", label="Recruiter Home", icon="🧑‍💻"
    )
     st.sidebar.page_link(
         "pages/Recruiter_AthleteRecs.py", label="Recommended Athletes", icon = "🏃‍♂️"
     )
     st.sidebar.page_link(
        "pages/Recruitment_Tool.py", label="Recruitment Tool", icon = "🛠️"
     )
     st.sidebar.page_link(
        "pages/Recruitment_Events.py", label="Recruitment Events", icon = "📅"
     )

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):

    # add a logo to the sidebar always
    st.sidebar.image("assets/bfa.logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")    

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # if the user role is an athletic director, give them acces to the AD page
        if st.session_state["role"] == "athletic_director":
            AthleticDirectorHomeNav()

        # If the user role is coach, give them access to the coach page
        if st.session_state["role"] == "coach":
            CoachHomeNav()

        # If the user is an player, give them access to the athlete pages
        if st.session_state["role"] == "athlete":
            AthletesHomeNav()

         # If the user is a recruiter, give them access to the recruiter pages
        if st.session_state["role"] == "recruiter":
            RecruiterHomeNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
