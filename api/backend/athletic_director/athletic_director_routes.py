########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
athletic_director = Blueprint('athletic_director', __name__)
#------------------------------------------------------------------
#gets teams in the athletic program at their school
@athletic_director.route('/teams', methods=['GET'])
def get_teams():
    try:
        cursor = db.get_db().cursor()
        high_school = request.args.get('high_school')
        query = '''
            SELECT * 
            FROM Team t
            WHERE t.DirectorID = 131
        '''
        cursor.execute(query,)
        theData = cursor.fetchall()
        return jsonify(theData), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'details': str(e)}), 500
#------------------------------------------------------------------
#gets coaches and their contacts in the athletic program at their school
@athletic_director.route('/athletic_director/coaches', methods=['GET'])
def get_players():
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM Coach c
        JOIN Team t on c.CoachID=t.CoachID
        WHERE t.TeamID = %s
    '''
    team_id = request.args.get('team_id')
    cursor.execute(query, (team_id,))
    theData = cursor.fetchall()
    return jsonify(theData), 200
#------------------------------------------------------------------
#gets coaches and their contacts in the athletic program at their school
@athletic_director.route('/athletic_director/players', methods=['GET'])
def get_players():
    cursor = db.get_db().cursor()
    query = '''
        SELECT Athlete.FirstName, Athlete.LastName
        FROM Athlete
        WHERE Athlete.TeamID = %s
    '''
    team_id = request.args.get('team_id')
    cursor.execute(query, (team_id,))
    theData = cursor.fetchall()
    return jsonify(theData), 200
#--------------------------------------------------------------
# #gets all of the schools a player has saved (for recruitment)
# @athletic_director.route('/athletic_director/coaches', methods=['GET'])
# def get_coaches():
#     cursor = db.get_db().cursor()
#     query = '''
#         SELECT Coach.FirstName, Coach.Last, Contact.Phone, Contact.Email
#         FROM Coach
#         JOIN Contact ON Coach.ContactID = Contact.ContactID
#         WHERE Coach.CoachID IN (
#             SELECT CoachID FROM Team WHERE HighSchoolName = %s);
#         )
#     '''
#     high_school_team = request.args.get('team_id')
#     cursor.execute(query, (high_school_team),)
#     theData = cursor.fetchall()
#     return jsonify(theData), 200
#------------------------------------------------------------------
#gets all practices where team id from team equals athletic director's id
@athletic_director.route('/athletic_director/practices', methods=['GET'])
def get_practices():
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM Practice p 
        JOIN Team t ON t.TeamID = p.PracticeID 
        WHERE TeamID = 131
    '''
    cursor.execute(query,)
    theData = cursor.fetchall()
    return jsonify(theData), 200

#------------------------------------------------------------------
#gets all games

@athletic_director.route('/games', methods=['GET'])
def get_games():
    try:
        team_id = request.args.get('team_id')
        cursor = db.get_db().cursor()
        query = '''
            SELECT GameID, Date, Time, Location, HomeTeamID, AwayTeamID
            FROM Game
            WHERE HomeTeamID = %s OR AwayTeamID = %s
            ORDER BY Date ASC;
        '''
        cursor.execute(query, (team_id, team_id))
        rows = cursor.fetchall()

        # If empty, just return empty list
        if not rows:
            return jsonify([]), 200

        colnames = [desc[0] for desc in cursor.description]

        # Only return actual data rows (skip if column names got inserted somehow)
        valid_rows = [row for row in rows if row[0] != colnames[0]]
        return jsonify([dict(zip(colnames, row)) for row in valid_rows]), 200

    except Exception as e:
        return jsonify({'error': 'Failed to fetch games', 'details': str(e)}), 500
#------------------------------------------------------------------
# adds a player
@athletic_director.route('/athletic_director/addplayer', methods=['POST'])
def add_player():
    cursor = db.get_db().cursor()
    data = request.get_json()
    query = '''
        INSERT INTO Athlete (
            FirstName, LastName, Gender, GPA, GradeLevel, Height, Position, RecruitmentStatus, ContactID, TeamID
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    values = (data.get('FirstName'), data.get('LastName'), data.get('Gender'), data.get('GPA'), data.get('GradeLevel'), data.get('Height'), data.get('Position'), data.get('RecruitmentStatus'), data.get('ContactID'), data.get('TeamID'))
    cursor.execute(query, values)
    db.get_db().commit()
    return jsonify({'message':'Player added successfully'}), 200
#------------------------------------------------------------------
# deletes a player
@athletic_director.route('/athletic_director/deleteplayer', methods=['DELETE'])
def delete_player():
    cursor = db.get_db().cursor()
    player_id = request.args.get('player_id')
    if not player_id:
        return jsonify({'error': 'Missing player_id'}), 400
    query = '''
        DELETE FROM Athlete
        WHERE PlayerID = %s;
    '''
    cursor.execute(query, (player_id),)
    db.get_db().commit()
    return jsonify({'message':f'Player {player_id} deleted successfully'}), 200

#------------------------------------------------------------------
# adds a coach
@athletic_director.route('/athletic_director/addcoach', methods=['POST'])
def add_coach():
    cursor = db.get_db().cursor()
    data = request.get_json()
    query = '''
        INSERT INTO Coach (
            CoachID, FirstName, LastName
        ) 
        VALUES (%s, %s, %s)
    '''
    values = (data.get('CoachID'), data.get('FirstName'), data.get('LastName'))
    cursor.execute(query, values)
    db.get_db().commit()
    return jsonify({'message':'Coach added successfully'}), 200

#------------------------------------------------------------------
# deletes a coach
@athletic_director.route('/athletic_director/deletecoach', methods=['DELETE'])
def delete_coach():
    cursor = db.get_db().cursor()
    coach_id = request.args.get('coach_id')
    if not coach_id:
        return jsonify({'error': 'Missing coach_id'}), 400
    query = '''
        DELETE FROM Coach
        WHERE CoachID = %s;
    '''
    cursor.execute(query, (coach_id),)
    db.get_db().commit()
    return jsonify({'message':f'Player {coach_id} deleted successfully'}), 200

#------------------------------------------------------------------
# adds a game
@athletic_director.route('/athletic_director/addgame', methods=['POST'])
def add_game():
    cursor = db.get_db().cursor()
    data = request.get_json()
    query = '''
        INSERT INTO Game (
            GameID, Data, Time, Location, HomeTeamID, AwayTeamID, DirectorID
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    values = (data.get('GameID'), data.get('Date'), data.get('Time'), data.get('Location'), data.get('HomeTeamID'), data.get('AwayTeamID'), data.get('DirectorID'))
    cursor.execute(query, values)
    db.get_db().commit()
    return jsonify({'message':'Game added successfully'}), 200

#------------------------------------------------------------------
# deletes a game
@athletic_director.route('/athletic_director/deletegame', methods=['DELETE'])
def delete_game():
    cursor = db.get_db().cursor()
    game_id = request.args.get('game_id')
    if not game_id:
        return jsonify({'error': 'Missing game_id'}), 400
    query = '''
        DELETE FROM Game
        WHERE GameID = %s;
    '''
    cursor.execute(query, (game_id),)
    db.get_db().commit()
    return jsonify({'message':f'Player {game_id} deleted successfully'}), 200