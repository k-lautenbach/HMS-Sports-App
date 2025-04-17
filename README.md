# HMS Sports Project Repository

This repo contains our semester project for CS320: Intro to Databases. It includes our infrastructure setup (containers), project databases, and UI pages. 

## Prerequisites

- A GitHub Account
- A terminal-based git client or GUI Git client such as GitHub Desktop or the Git plugin for VSCode.
- VSCode with the Python Plugin
- A distribution of Python running on your laptop. The distro supported by the course is Anaconda or Miniconda.

## Major Project Components

There are three major components that each run in their own Docker Containers:

- Streamlit App in the `./app` directory
- Flask REST api in the `./api` directory
- MySQL Database that will be initialized with SQL script files from the `./database-files` directory

## Project Description:
We implemented an athletics app to help high-school student athletes through their college recruitment process. We were aiming to bridge the gap between these young athletes and their future schools. We wanted to create a place where students could connect with recruiters, coaches, and athletic directors in an accesible and streamlined environment. 

We used Docker Desktop to create and run the database. These containers were built and createdin the docker-compose.yml file. We then used the Python Flask library to build blueprints for the relavant user persons and corresponding routes for each of these blueprints that help users execute their goals. The core database was cerated in DataGrip as a MySQL file. The current version of the app contains sample data generated through ChatGPT, though edits to the data could be made to better match an actual school system.

We hope that this project can continue to be used to aid students in their recruitment process. In the future, we would love to expandt this program to include some aspects of a social network, by opening up local communication lines between users. 

