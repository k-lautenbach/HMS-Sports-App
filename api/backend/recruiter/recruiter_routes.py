########################################################
# Routes for Recruiter Blueprint
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db


recruiter = Blueprint('recruiter', __name__)
#------------------------------------------------------------------
# fetch all of recruiters events
@recruiter.route('/recruiter/events', methods=['GET'])
def view_events():
    cursor = db.get_db().cursor()
    query = '''
        SELECT re.DateTime, re.Location, re.EventID
        FROM RecruitingEvents re
        WHERE re.RecruiterID = 301
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    return jsonify(theData), 200

#----------------------------------------------------------
# adds a recruiting event
@recruiter.route('/recruiter/event', methods=['POST'])
def add_events():
    cursor = db.get_db().cursor()
    data = request.get_json()
    query = '''
        INSERT INTO RecruitingEvents (
            DateTime, Location, RecruiterID
        ) 
        VALUES (%s, %s, %s)
    '''
    values = (data.get('DateTime'), data.get('Location'), 301)
    cursor.execute(query, values)
    db.get_db().commit()
    return jsonify({'message':'Event added successfully'}), 200

#------------------------------------------------------------------
#removes a recruiting event 
@recruiter.route('/recruiter/event', methods=['DELETE'])
def delete_event():
    cursor = db.get_db().cursor()
    event_id = request.args.get('EventID')

    if not event_id:
        return jsonify({'error': 'Missing event_id'}), 400

    query = '''
        DELETE FROM RecruitingEvents
        WHERE RecruiterID = 301 AND EventID = %s;
    '''

    cursor.execute(query, (event_id,))
    db.get_db().commit()

    return jsonify({'message': f'Successfully cancelled event {event_id}!'}), 200

#------------------------------------------------------------------
# gets player stats based on their first and last name
@recruiter.route('/recruiter/player_stats', methods=['GET'])
def get_player_stats():
    cursor = db.get_db().cursor()
    query = '''
        SELECT a.FirstName, a.LastName, a.Position, a.GradeLevel, a.Height,
               s.TotalPoints, s.GamesPlayed, s.AssistsPerGame, s.Rebounds,
               s.PointsPerGame, s.FreeThrowPercentage, s.HighlightsURL,
               t.TeamName
        FROM Athlete a 
        JOIN AthleteStats s ON a.PlayerID = s.PlayerID
        JOIN Team t ON a.TeamID = t.TeamID
        WHERE a.FirstName = %s AND a.LastName = %s
    '''
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    
    cursor.execute(query, (first_name, last_name))
    theData = cursor.fetchall()
    return jsonify(theData), 200
#------------------------------------------------------------------
# gets all teams in a certain state
@recruiter.route('/recruiter/state_teams', methods=['GET'])
def get_hs_teams_in_area():
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM Team
        WHERE State = %s and Sport = 'Basketball'
    '''
    state = request.args.get('state')
    cursor.execute(query, (state,))
    theData = cursor.fetchall()
    return jsonify(theData), 200

#------------------------------------------------------------------
@recruiter.route('/recruiter/roster', methods=['GET'])
def get_roster():
    cursor = db.get_db().cursor()
    query = '''
        SELECT a.PlayerID, a.FirstName, a.LastName, a.Gender, a.Height, a.GradeLevel, a.Position, a.RecruitmentStatus, a.GPA
        FROM Team t JOIN Athlete a
        ON t.TeamID = a.TeamID
        WHERE t.TeamName = %s
    '''
    team = request.args.get('team')
    cursor.execute(query, (team,))
    theData = cursor.fetchall()
    return jsonify(theData), 200

#------------------------------------------------------------------
# shows athletes who match given criteria of gpa, state, and position
@recruiter.route('/recruiter/player_criteria', methods=['GET'])
def player_criteria():
    cursor = db.get_db().cursor()
    
    # Get values from query parameters
    states = request.args.getlist('State')     
    gpa = request.args.get('GPA')    
    positions = request.args.getlist('Position') 
    
    state_str = ', '.join([f"'{state_item}'" for state_item in states])
    position_str = ', '.join([f"'{pos_item}'" for pos_item in positions])

    query = '''
            SELECT a.FirstName, a.LastName, a.Position, a.GradeLevel, a.Height,
                   t.TeamName, t.State, a.GPA, a.RecruitmentStatus
            FROM Athlete a 
            JOIN Team t ON a.TeamID = t.TeamID
            WHERE a.Gender = 'Male' AND t.State IN %s AND a.GPA > %s AND a.Position IN %s
        '''

    # Ensure states and positions are passed as tuples of values in the correct format for SQL
    cursor.execute(query, (tuple(states), gpa, tuple(positions)))
    data = cursor.fetchall()

    return jsonify(data), 200
