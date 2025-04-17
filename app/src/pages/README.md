# `pages` Folder

Our pages are set up so that the persona name is the prefix for their user pages. 
Ex. Athlete, Athletic_Director, Coach, Recruiter

## Page Structure

### Home Pages
Each persona has a home dashboard page:
- `Athlete_Home.py` - player profile 
- `Athletic_Director_Home.py` - director profile
- `Coach_Home.py` - coach profile
- `Recruiter_Home.py` - recruiter profile

### Feature Pages

#### Athlete Pages
- `Athlete_Stats.py` - Personal statistics and performance metrics
- `Athlete_Schedule.py` - Practice and game schedules

#### Coach Pages
- `Coach_Strategies.py` - Team plays and strategies
- `Coach_Practices.py` - Practice Schedule
- `Coach_Games.py` -Game Schedule

#### Athletic Director Pages
- `Athletic_Director_Coaches.py` - View teams and their rosters and coaches
- `Athletic_Director_Practices.py` - View practices 

#### Recruiter Pages
- `Recruiter_Tool.py` - Athlete and team search
- `Recruiter_AthleteRecs.py` - Get athlete reccomendations based on criteria
- `Recruiter_Events.py` - Recruitment events

## Navigation

- Each page has `SideBarLinks()` for quick navigation that depends on the logged in user

## API Integration

Pages connect to backend API using:
- Base URL: `http://web-api:4000`
