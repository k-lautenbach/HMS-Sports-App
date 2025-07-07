# HMS Sports Project Repository

This repo contains our semester project for CS3200: Intro to Databases. It includes our infrastructure setup (containers), project databases, and UI pages. 

## Description
An all-in-one database for a high school sport’s team that allows streamlined activity for it’s users. Because our app is focused on our specific user stories and personas, some aspects of the code are “hard coded” to display only results that pertain to them. 

## Features
This repo contains for archetypical users: Coach, Athlete, Recruiter, and Athletic Director. We use Role-Based Access Control to specify certain abilities and access. Here are tools created for their use:
- Coach Features: Schedule viewing (games and practices), Strategy viewing(all strategies registered with the team).
- Recruiter Features: Search for players that meet their recruitment requirements (has access to academic and athletic stats), 
- Athlete Features: Stats management(canview or update), Can view  chedule(games, practices, and recruitment events), recruitment profile(includes, highlight reels, and scholarship guidance)
- Athletic Director Tools- View All teams  the manage(with roster and coach info), Practice management(can view all practices and their info, and can add or delete practices)
- App Features- Clear buttons on how to access tools, navigation sidebar which lets the user logout and go back to the previous page.

## Built With: 
- werkzeug
- flask
- flask-login
- flask-mysql
- cryptography
- python-dotenv
- pandas
- streamlit
- equests
- validators

## Prerequisites
- A GitHub Account
- A terminal-based git client or GUI Git client such as GitHub Desktop or the Git plugin for VSCode.
- VSCode with the Python Plugin
- A distribution of Python running on your laptop. The distro supported by the course is Anaconda or Miniconda.

## Installation
Clone your forked version of this repository:
1. clone project: terminal
- in github: code>SSH>*copy*
- in terminal:
- git clone *paste
2. Set up the .env file in the api folder using .env.template. 
- enter a new passcode
3. Install dependencies from the requirements.txt files:
bash
- For API folder: pip install -r ./api/requirements.txt
- For app folder: pip install -r ./app/requirements.txt
4. Use Docker to start services:
- docker compose up -d
5. To Stop and restart containers when updating the backend:
- docker compose down
- docker compose up -d
6. Create new data source in data grip, and connect the database(used for testing queries and updating the database):
- create new project
- name it ‘project repo’
- change port to 3200
- user root
- put in .env password
- test connection


## Usage
Break-Free Athletics offers intuitive tools for team and individual management. Users can:
- Log in to access role-specific dashboards (e.g., coach tools, recruiter search).
- Create player profiles with academic and athletic achievements.
- Access highlights for top athletes.
- Manage schedules, track stats, and connect directly with colleges and recruiters.

## Contributions
The contributors of this project are Kate Lautenbach, Emily Wang, Sophia Guerra, Noah Burra, and Rishona Israel. All team members contributed equally to the database design and conceptual development. Once progressing to the building phase, Emily and Sophia worked on creating all the blueprints and routes needed. For the UI, Kate worked on the Athletic Director pages, Emily worked on the Recruiter pages, Noah worked on the Athlete pages, and Rishona worked on the coach pages. Sophia did the home and navigation bar UI. After ensuring both the back and front ends were up and running, Emily worked on the UI and made sure the website was aesthetically pleasing. All team members were involved in debugging and resolving any conflicts. 

## Further Steps
In the future, we would like to implement more tools for our users that would streamline activity. For example, we would add contact information for all users that would allow easy access and communication. Additionally, we could have a messaging tool that allows users to directly send and receive messages between users. 

## Presentation
We prepared a [presentation](https://www.dropbox.com/scl/fo/xvq8gjvm8a2n3lc9ml2gi/AP33HnSugcZutj0y65PSgg8?rlkey=8w2u382ak0v0r93ub030069x7&st=u8jkzieq&dl=0 
) that goes through the user pages and functions. 

