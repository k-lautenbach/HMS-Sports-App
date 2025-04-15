########################################################
# Team BluePrint
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Create a new Blueprint object
teams = Blueprint('teams', __name__)

#------------------------------------------------------------
# Get all teams
@teams.route('/teams', methods=['GET'])
def get_all_teams():
    cursor = db.get_db().cursor()
    query = '''
        SELECT TeamID, TeamName, HighSchoolName
        FROM Team
    '''
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get a specific team by TeamID
@teams.route('/teams/<TeamID>', methods=['GET'])  # Use int for type safety
def get_team(TeamID):
    current_app.logger.info(f'GET /teams/{TeamID} route')

    cursor = db.get_db().cursor()
    
    query = '''
        SELECT TeamID, TeamName, HighSchoolName
        FROM Team
        WHERE TeamID = %s
    '''
    cursor.execute(query, (TeamID,))
    data = cursor.fetchone()  

    response = make_response(jsonify(data))
    response.status_code = 200
    return response
#------------------------------------------------------------
# Get all coaches 

@teams.route('/coaches', methods=['GET'])
def get_all_teams():
    cursor = db.get_db().cursor()
    query = '''
        SELECT CoachID, FirstName, LastName
        FROM Coach
    '''
    cursor.execute(query)
    data = cursor.fetchall()

    response = make_response(jsonify(data))
    response.status_code = 200
    return response
#------------------------------------------------------------
# Get a specific coach by TeamID
@teams.route('/coaches/<TeamID>', methods=['GET'])  # Use int for type safety
def get_coach(TeamID):
    current_app.logger.info(f'GET /teams/{TeamID} route')

    cursor = db.get_db().cursor()
    
    query = '''
        SELECT CoachID, FirstName, LastName
        FROM Coach
        WHERE TeamID = %s
    '''
    cursor.execute(query, (TeamID,))
    data = cursor.fetchone()  

    response = make_response(jsonify(data))
    response.status_code = 200
    return response
#------------------------------------------------------------
# Get all players on a specific team
@teams.route('/players/<TeamID>', methods=['GET'])
def get_customer(TeamID):
    current_app.logger.info('GET /Teams/<TeamID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Athlete WHERE TeamID = {0}'.format(TeamID))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
