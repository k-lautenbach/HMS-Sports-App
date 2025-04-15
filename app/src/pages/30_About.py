import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About BFA")

st.markdown (
    """
    Break Free Athletics is an all-in-one database that makes high school sports easy. 

    Whether you’re a player, coach, athletic director,  or recruiter, Break Free Athletics puts practice schedules, 
    athlete performance, and college recruitment right at your fingertips. Now, better than ever, coaches can manage their roster, 
    schedule games/practices, and connect with recruiters. Recruiters can actively search for top players at each school 
    while players learn about new opportunities that await them. 
    
    Most importantly, BFA also allows students to 
    present their best selves to potential recruiters, displaying highlight reels, academics, and stats to college teams.
    BFA is there to guide students on contract negotiations, scholarships, college life, and more. 
    Athletes will be able to personalize their journey from high school sports to beyond and optimize their player profile. 
   
    With Break-Free Athletics, student-athletes will never forget a practice or play, and focus on getting their head in the game!

    """
        )
