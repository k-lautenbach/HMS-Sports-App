##################################################
# Home Page 
##################################################

import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')
st.session_state['authenticated'] = False
SideBarLinks(show_home=True)


logger.info("Loading the Home page of the app")
st.title('👤 Break Free Athletics User Portal')
st.write('\n\n')
st.write('### Welcome! Which user would you like to act as today?')


if st.button('Act as Jack Bolton, the Head Coach of the East High Basketball Team', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'coach'
    st.session_state['first_name'] = 'Jack'
    logger.info("Logging in as Coach Persona")
    st.switch_page('pages/Coach_Home.py')

if st.button('Act as Troy, an East High Athlete', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'athlete'
    st.session_state['first_name'] = 'Troy'
    logger.info("Logging in as Athlete Persona")
    st.switch_page('pages/Athlete_Home.py')

if st.button('Act as Calvin Goldstein, UCB Recruiter', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'recruiter'
    st.session_state['first_name'] = 'Cal'
    st.switch_page('pages/Recruiter_Home.py')

if st.button("Act as Ethan Wilson, East High's Athletic Director", 
            type = 'primary', 
            use_container_width=True):
    # when user clicks the button, they are now considered authenticated
    st.session_state['authenticated'] = True
    # we set the role of the current user
    st.session_state['role'] = 'athletic_director'
    # we add the first name of the user (so it can be displayed on 
    # subsequent pages). 
    st.session_state['first_name'] = 'Ethan'
    # finally, we ask streamlit to switch to another page, in this case, the 
    # landing page for this particular user type
    logger.info("Logging in as Athletic Director Persona")
    st.switch_page('pages/Athletic_Director_Home.py')



