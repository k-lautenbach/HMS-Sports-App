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
def get_all_coaches():
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
def get_all_players(TeamID):
    current_app.logger.info('GET /Teams/<TeamID> route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Athlete WHERE TeamID = {0}'.format(TeamID))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Add a player to a specific team
@teams.route('/teams/<int:TeamID>/players', methods=['POST'])
def add_player_to_team(TeamID):
    the_data = request.json
    current_app.logger.info(the_data)

    first_name = the_data['FirstName']
    last_name = the_data['LastName']
    gender = the_data.get('Gender')
    gpa = the_data.get('GPA')
    grade_level = the_data.get('GradeLevel')
    height = the_data.get('Height')
    position = the_data.get('Position')
    recruitment_status = the_data.get('RecruitmentStatus')
    contact_id = the_data.get('ContactID')  # assuming this is required or passed

    query = '''
        INSERT INTO Athlete (
            FirstName, LastName, Gender, GPA, GradeLevel,
            Height, Position, RecruitmentStatus, ContactID, TeamID
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (
        first_name, last_name, gender, gpa, grade_level,
        height, position, recruitment_status, contact_id, TeamID
    ))
    db.get_db().commit()

    response = make_response(jsonify({"message": "Player added successfully"}))
    response.status_code = 201
    return response

#------------------------------------------------------------
# Remove a player from a specific team
@teams.route('/teams/<int:TeamID>/players/<int:PlayerID>', methods=['DELETE'])
def delete_player_from_team(TeamID, PlayerID):
    current_app.logger.info(f'DELETE /teams/{TeamID}/players/{PlayerID} route')

    cursor = db.get_db().cursor()

    query = '''
        DELETE FROM Athlete
        WHERE PlayerID = %s AND TeamID = %s
    '''
    cursor.execute(query, (PlayerID, TeamID))
    db.get_db().commit()


