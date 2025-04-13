DROP DATABASE IF EXISTS project;
CREATE DATABASE project;
USE project;

CREATE TABLE Contact (
    ContactID INT PRIMARY KEY,
    Phone VARCHAR(20),
    Email VARCHAR(100),
    Address TEXT
);

CREATE TABLE Coach (
    CoachID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    ContactID INT,
    FOREIGN KEY (ContactID) REFERENCES Contact(ContactID)
);

CREATE TABLE Strategies (
    StrategyID INT PRIMARY KEY,
    Name VARCHAR(100),
    Type VARCHAR(50),
    Description TEXT
);

CREATE TABLE Team (
    TeamID INT PRIMARY KEY,
    TeamName VARCHAR(100),
    HighSchoolName VARCHAR(100),
    State VARCHAR(50),
    Sport VARCHAR(50),
    Record VARCHAR(20),
    CoachID INT,
    StrategyID INT,
    FOREIGN KEY (CoachID) REFERENCES Coach(CoachID),
    FOREIGN KEY (StrategyID) REFERENCES Strategies(StrategyID)
);

CREATE TABLE CollegeTeam (
    TeamID INT PRIMARY KEY,
    Name VARCHAR(100),
    TeamSize INT,
    Division VARCHAR(50)
);

CREATE TABLE Recruiter (
    RecruiterID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    University VARCHAR(100),
    TeamID INT,
    FOREIGN KEY (TeamID) REFERENCES CollegeTeam(TeamID)
);

CREATE TABLE RecruitingEvents (
    EventID INT PRIMARY KEY,
    DateTime DATETIME,
    Location VARCHAR(100),
    RecruiterID INT,
    FOREIGN KEY (RecruiterID) REFERENCES Recruiter(RecruiterID)
);

CREATE TABLE AthleticDirector (
    DirectorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    YearsExperience INT
);

CREATE TABLE Game (
    GameID INT PRIMARY KEY,
    Date DATE,
    Time TIME,
    Location VARCHAR(100),
    HomeTeamID INT,
    AwayTeamID INT,
    DirectorID INT,
    FOREIGN KEY (HomeTeamID) REFERENCES Team(TeamID),
    FOREIGN KEY (AwayTeamID) REFERENCES Team(TeamID),
    FOREIGN KEY (DirectorID) REFERENCES AthleticDirector(DirectorID)
);

CREATE TABLE Practice (
    PracticeID INT PRIMARY KEY,
    Date DATE,
    Time TIME,
    Location VARCHAR(100),
    TeamID INT,
    DirectorID INT,
    FOREIGN KEY (TeamID) REFERENCES Team(TeamID),
    FOREIGN KEY (DirectorID) REFERENCES AthleticDirector(DirectorID)
);

CREATE TABLE Athlete (
    PlayerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    GPA FLOAT,
    GradeLevel INT,
    Height FLOAT,
    Position VARCHAR(50),
    RecruitmentStatus VARCHAR(50),
    ContactID INT,
    TeamID INT,
    FOREIGN KEY (ContactID) REFERENCES Contact(ContactID),
    FOREIGN KEY (TeamID) REFERENCES Team(TeamID)
);

CREATE TABLE AthleteStats (
    StatsID INT PRIMARY KEY,
    PlayerID INT,
    TotalPoints INT,
    GamesPlayed INT,
    AssistsPerGame FLOAT,
    Rebounds INT,
    PointsPerGame FLOAT,
    FreeThrowPercentage FLOAT,
    HighlightsURL TEXT,
    FOREIGN KEY (PlayerID) REFERENCES Athlete(PlayerID)
);

CREATE TABLE SchoolsOfInterest (
    InterestID INT PRIMARY KEY,
    PlayerID INT,
    TeamID INT,
    Name VARCHAR(100),
    RecruitmentProgress VARCHAR(100),
    Location VARCHAR(100),
    FOREIGN KEY (PlayerID) REFERENCES Athlete(PlayerID),
    FOREIGN KEY (TeamID) REFERENCES CollegeTeam(TeamID)
);

CREATE TABLE Messages (
    MessageID INT PRIMARY KEY,
    SenderID INT,
    ReceiverID INT,
    CoachID INT,
    RecruiterID INT,
    DirectorID INT,
    MessageText TEXT,
    Timestamp DATETIME,
    FOREIGN KEY (SenderID) REFERENCES Athlete(PlayerID),
    FOREIGN KEY (ReceiverID) REFERENCES Athlete(PlayerID),
    FOREIGN KEY (CoachID) REFERENCES Coach(CoachID),
    FOREIGN KEY (RecruiterID) REFERENCES Recruiter(RecruiterID),
    FOREIGN KEY (DirectorID) REFERENCES AthleticDirector(DirectorID)
);

CREATE TABLE AthleteEvent (
    PlayerID INT,
    EventID INT,
    PRIMARY KEY (PlayerID, EventID),
    FOREIGN KEY (PlayerID) REFERENCES Athlete(PlayerID),
    FOREIGN KEY (EventID) REFERENCES RecruitingEvents(EventID)
);

CREATE TABLE AthleteRecruiter (
    PlayerID INT,
    RecruiterID INT,
    PRIMARY KEY (PlayerID, RecruiterID),
    FOREIGN KEY (PlayerID) REFERENCES Athlete(PlayerID),
    FOREIGN KEY (RecruiterID) REFERENCES Recruiter(RecruiterID)
);

CREATE TABLE AthleteInterestedSchools (
    PlayerID INT,
    InterestID INT,
    PRIMARY KEY (PlayerID, InterestID),
    FOREIGN KEY (PlayerID) REFERENCES Athlete(PlayerID),
    FOREIGN KEY (InterestID) REFERENCES SchoolsOfInterest(InterestID)
);

INSERT INTO Contact (ContactID, Phone, Email, Address) VALUES
(1, '8018320747', 'troybolton@easthigh.edu', '3642 Lang Avenue'),
(2, '8012925389', 'jackbolton@easthigh.edu', '3642 Lang Avenue'),
(3, '5306905699', 'calgoldstein@berkeley.edu', '1660 Providence Lane'),
(4, '8017487170', 'johnjames@easthigh.edu', '2516 Hickory Street');


INSERT INTO Coach (CoachID, FirstName, LastName, ContactID) VALUES
(1, 'Jack', 'Bolton', 2),
(2, 'John', 'James', 4);

INSERT INTO Strategies (StrategyID, Name, Type, Description) VALUES
(1, 'Pick and Roll', 'Offense', 'Set screen and rush basket'),
(2, 'Half-court Press', 'Defense', 'Guard in front of the half-court line');


INSERT INTO Team (TeamID, TeamName, HighSchoolName, State, Sport, Record, CoachID, StrategyID) VALUES
(1, 'Wildcats', 'East High', 'Utah', 'Basketball', '20-5', 1, 1),
(2, 'Tigers', 'North High', 'Utah', 'Basketball', '10-4', 2, 2);

INSERT INTO CollegeTeam (TeamID, Name, TeamSize, Division) VALUES
(123, 'UC Berkeley', 20, 'D1'),
(456, 'Duke', 19, 'D1');

INSERT INTO Recruiter (RecruiterID, FirstName, LastName, University, TeamID) VALUES
(1, 'Calvin', 'Goldstein', 'UC Berkeley', 123),
(2, 'Timothy', 'Barnes', 'Duke', 456);

INSERT INTO RecruitingEvents (EventID, DateTime, Location, RecruiterID) VALUES
(1, '2025-04-01 17:30:00', 'East High', 1),
(2, '2025-04-02 18:30:00', 'North High', 2);

INSERT INTO AthleticDirector (DirectorID, FirstName, LastName, YearsExperience) VALUES
(1, 'Ethan', 'Wilson', 20),
(2, 'Melanie', 'Black', 10);

INSERT INTO Game (GameID, Date, Time, Location, HomeTeamID, AwayTeamID, DirectorID) VALUES
(1, '2025-05-01', '19:45:00', 'East High', 1, 2, 1),
(2, '2025-05-02', '19:30:00', 'North High', 2, 1, 2);

INSERT INTO Practice (PracticeID, Date, Time, Location, TeamID, DirectorID) VALUES
(1, '2025-04-01', '14:00:00', 'South Court', 1, 1),
(2, '2025-04-02', '16:00:00', 'Court 1', 2, 2);

INSERT INTO Athlete (PlayerID, FirstName, LastName, Gender, GPA, GradeLevel, Height, Position, RecruitmentStatus, ContactID, TeamID) VALUES
(1, 'Troy', 'Bolton', 'Male', 3.9, 11, 68, 'Point Guard', 'Active', 1, 1),
(2, 'Chad', 'Danforth', 'Male', 3.6, 11, 69, 'Guard', 'Active', 1, 1),
(3, 'Zeke', 'Baylor', 'Male', 3.6, 11, 72, 'Forward', 'Active', 1, 1);

INSERT INTO AthleteStats (StatsID, PlayerID, TotalPoints, GamesPlayed, AssistsPerGame, Rebounds, PointsPerGame, FreeThrowPercentage, HighlightsURL) VALUES
(1, 1, 350, 21, 6.2, 75, 23.1, 0.67, 'https://maxpreps.com/highlights/troybolton'),
(2, 2, 267, 20, 4.3, 82, 18.7, 0.52, 'https://maxpreps.com/highlights/chaddanforth');

INSERT INTO SchoolsOfInterest (InterestID, PlayerID, TeamID, Name, RecruitmentProgress, Location) VALUES
(1, 1, 123, 'UC Berkeley', 'School visit', 'Berkeley, CA'),
(2, 2, 123, 'Purdue University', 'Contacted coach', 'West Lafayette, IN');

INSERT INTO Messages (MessageID, SenderID, ReceiverID, MessageText, Timestamp) VALUES
(1, 1, 2, 'Do you want to get food after practice?', '2025-04-01 12:01:00'),
(2, 2, 1, 'Yeah, do you want to eat Chipotle?', '2025-04-01 12:07:00');

INSERT INTO AthleteEvent (PlayerID, EventID) VALUES
(1, 1),
(2, 1),
(3, 2);

INSERT INTO AthleteRecruiter (PlayerID, RecruiterID) VALUES
(1, 1),
(1, 2),
(2, 2);

INSERT INTO AthleteInterestedSchools (PlayerID, InterestID) VALUES
(1, 1),
(1, 2),
(2, 2);