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
# gets all players of a certain position
@recruiter.route('/recruiter/playerposition', methods=['GET'])
def get_all_players(Position):
    cursor = db.get_db().cursor()
    query = '''
        SELECT Athlete.PlayerID, Athlete.FirstName, Athlete.LastName, Athlete.Gender, Athlete.GPA, Athlete.GradeLevel, Athlete.Height, Athlete.Position, Athlete.RecruitmentStatus, Athlete.ContactID, Athlete.TeamID
        FROM Athlete
        WHERE Position = %s;
    '''
    cursor.execute(query)
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
        WHERE State = %s
    '''
    state = request.args.get('state')
    cursor.execute(query, (state,))
    theData = cursor.fetchall()
    return jsonify(theData), 200
