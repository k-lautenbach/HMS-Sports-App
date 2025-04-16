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

#------------------------------------------------------------------
#gets all of the schools a player has saved (for recruitment)
players = Blueprint('players', __name__)
@players.route('/players/schoolsofinterest', methods=['GET'])
def get_schools_interest():
    cursor = db.get_db().cursor()
    query = '''
        SELECT SchoolsOfInterest.Name, SchoolsOfInterest.RecruitmentProgress, SchoolsOfInterest.Location
        FROM SchoolsOfInterest
        JOIN Athlete ON SchoolsOfInterest.PlayerID = Athlete.PlayerID
        WHERE Athlete.PlayerID = %s;
    '''
    player_id = request.args.get('player_id')
    cursor.execute(query, (player_id,))
    theData = cursor.fetchall()
    return jsonify(theData), 200


#------------------------------------------------------------------
#gets all players
@players.route('/players', methods=['GET'])
def get_all_players():
    cursor = db.get_db().cursor()
    query = '''
        SELECT Athlete.PlayerID, Athlete.FirstName, Athlete.LastName, Athlete.Gender, Athlete.GPA, Athlete.GradeLevel, Athlete.Height, Athlete.Position, Athlete.RecruitmentStatus, Athlete.ContactID, Athlete.TeamID
        FROM Athlete;
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    return jsonify(theData), 200
#------------------------------------------------------------------
@players.route('/players/<int:player_id>', methods=['GET'])
def get_player_info(player_id):
    try:
        cursor = db.get_db().cursor()

        query = '''
            SELECT PlayerID, FirstName, LastName, Gender,
                   GPA, GradeLevel, Height, Position,
                   RecruitmentStatus, ContactID, TeamID
            FROM Athlete
            WHERE PlayerID = %s;
        '''
        cursor.execute(query, (player_id,))
        
        row = cursor.fetchone()  # ✅ first fetch the row

        if row:
            colnames = [desc[0] for desc in cursor.description]  # ✅ then get column names
            result = dict(zip(colnames, row))
            print("→ Returning player data:", result)
            return jsonify(result), 200
        else:
            return jsonify({'error': 'Player not found'}), 404

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'Something went wrong', 'details': str(e)}), 500

#------------------------------------------------------------------
#gets all practices (for specific player)
@players.route('/players/practices', methods=['GET'])
def get_practices():
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM Practice
        WHERE TeamID = %s
        ORDER BY Date ASC;
    '''
    team_id = request.args.get('team_id')
    cursor.execute(query, (team_id,))
    theData = cursor.fetchall()
    return jsonify(theData), 200

#------------------------------------------------------------------
#gets all college teams with the average gpa is less than inputted 
@players.route('/players/gpa_match', methods=['GET'])
def get_potential_schools_gpa():
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM CollegeTeam
        WHERE Avg_GPA < %s
    '''
    gpa_limit = request.args.get('gpa_limit')
    cursor.execute(query, (gpa_limit,))
    theData = cursor.fetchall()
    return jsonify(theData), 200

#------------------------------------------------------------------
#gets all college teams with the matching division
@players.route('/players/div_match', methods=['GET'])
def get_div_match():
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM CollegeTeam
        WHERE Division = %s;
    '''
    division = request.args.get('division')
    cursor.execute(query, (division,))
    theData = cursor.fetchall()
    return jsonify(theData), 200

#------------------------------------------------------------------
#removes a school for a player's school of interest
@players.route('/players/schoolsofinterest', methods=['DELETE'])
def delete_school_of_interst():
    cursor = db.get_db().cursor()
    player_id = request.args.get('player_id')
    school_name = request.args.get('school_name')
    if not player_id or not school_name:
        return jsonify({'error': 'Missing player_id or school_name'}), 400
    query = '''
        DELETE FROM SchoolsOfInterest
        WHERE PlayerID = %s AND Name = %s;
    '''
    cursor.execute(query, (player_id, school_name))
    db.get_db().commit()
    return jsonify({'message': f'Successfully removed {school_name} from player {player_id}\'s interests'}), 200