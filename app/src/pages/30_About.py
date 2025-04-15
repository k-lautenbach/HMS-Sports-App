import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About BFA")

st.markdown (
    """
    Break Free Athletics is an all-in-one database that makes high school sports easy. 

    Whether you’re a player, coach, athletic director,  or recruiter, Break Free Athletics puts practice schedules, 
    athlete statistics, and college recruitments right at your fingertips. Now, better than ever, coaches can manage their roster, 
    schedule games/practices, and connect with recruiters, who can in turn, scout the top talent. 
    
    Most importantly, BFA also allows student-athletes to present their best selves to potential recruiters, 
    displaying highlight reels, academic information, and athletic statistics to college teams.
    BFA is here to guide students on contract negotiations, scholarships, college life, and more. 
    We work to help athletes make the transition from high school to the college game, by optimizing their player profile 
    and organizing all of their relevant recruiting information. 
   
    With Break-Free Athletics, student-athletes will never forget a practice or play, and can focus on getting their head in the game!

    """
        )
