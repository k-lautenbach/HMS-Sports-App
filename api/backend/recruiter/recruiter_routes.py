########################################################
# Routes for Recruiter Blueprint
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db


#----------------------------------------------------------
# adds a recruiting event
recruiter = Blueprint('recruiter', __name__)
@recruiter.route('/recruiter/event', methods=['POST'])
def add_game():
    cursor = db.get_db().cursor()
    data = request.get_json()
    query = '''
        INSERT INTO RecrutingEvents (
            DateTime, Location, RecruiterID, EventID
        ) 
        VALUES (%s, %s, %s, %s)
    '''
    values = (data.get('DateTime'), data.get('Location'), data.get('RecruiterID'), data.get('EventID'), data.get('HomeTeamID'), data.get('AwayTeamID'), data.get('DirectorID'))
    cursor.execute(query, values)
    db.get_db().commit()
    return jsonify({'message':'Event added successfully'}), 200

#------------------------------------------------------------------
#removes a recruiting event 
@recruiter.route('/recruiter/event', methods=['DELETE'])
def delete_recruiter_event():
    cursor = db.get_db().cursor()
    recruiter_id = request.args.get('RecruiterID')
    event_id = request.args.get('EventID')
    if not recruiter_id or not event_id:
        return jsonify({'error': 'Missing recruiter_id or event_id'}), 400
    query = '''
        DELETE FROM RecruitingEvents
        WHERE RecruiterID = %s AND EventID = %s;
    '''
    cursor.execute(query, (recruiter_id, event_id))
    db.get_db().commit()
    return jsonify({'message': f'Successfully removed {event_id} from recruiter {recruiter_id}\'s events'}), 200


#------------------------------------------------------------------
# gets a player's stats given first and last name
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
        SELECT a.PlayerID, a.FirstName, a.LastName, a.Gender, a.Height, a.GradeLevel, a.Position, a.RecruitmentStatus, a.ContactID, a.GPA
        FROM Team t JOIN Athlete a
        ON t.TeamID = a.TeamID
        WHERE t.TeamName = %s
    '''
    team = request.args.get('team')
    cursor.execute(query, (team,))
    theData = cursor.fetchall()
    return jsonify(theData), 200

#------------------------------------------------------------------
# gets athlete contact info
@recruiter.route('/athlete/contact', methods=['GET'])
def get_athlete_contact():
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM Athlete a JOIN Contact c
        ON a.ContactID = c.ContactID
        WHERE a.PlayerID = %s
    '''
    playerid = request.args.get('PlayerID')
    cursor.execute(query,(playerid,) )
    theData = cursor.fetchall()
    return jsonify(theData), 200
