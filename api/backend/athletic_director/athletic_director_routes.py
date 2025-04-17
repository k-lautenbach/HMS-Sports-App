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
def get_coach():
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM Coach c
        JOIN Team t on c.CoachID=t.CoachID
        WHERE t.TeamID = 1
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
        SELECT a.FirstName, a.LastName, a.TeamID
        FROM Athlete a
        WHERE t.TeamID = 1
    '''
    team_id = request.args.get('team_id')
    cursor.execute(query, (team_id,))
    theData = cursor.fetchall()
    return jsonify(theData), 200
#------------------------------------------------------------------
#gets all practices where director id from team equals athletic director's id
@athletic_director.route('/athletic_director/practices', methods=['GET'])
def get_practices():
    cursor = db.get_db().cursor()

    query = '''
        SELECT p.PracticeID, p.DateTime, p.Location, t.TeamName, t.Sport
        FROM Practice p 
        JOIN Team t ON t.TeamID = p.TeamID 
        WHERE t.DirectorID = 131
        ORDER BY p.DateTime ASC
    '''
    cursor.execute(query)
    theData = cursor.fetchall()

    return jsonify(theData), 200

#----------------------------------------------------------
# schedule a practice 
@athletic_director.route('/athletic_director/practices', methods=['POST'])
def add_practice():
    cursor = db.get_db().cursor()

    data = request.get_json()

    team_name = data.get('TeamName')
    date_time = data.get('DateTime')
    location = data.get('Location')

    team_query = 'SELECT TeamID FROM Team WHERE TeamName = %s'
    cursor.execute(team_query, (team_name,))
    result = cursor.fetchone()

    if not team_name or not date_time or not location:
            return jsonify({'error': 'Please fill all fields!'}), 400

    if not result:
        return jsonify({'error': 'Team not found'}), 404

    team_id = result['TeamID']

    # checks if a practice already exists at the same time and location
    conflict_query = '''
        SELECT * FROM Practice
        WHERE DateTime = %s AND Location = %s
    '''
    cursor.execute(conflict_query, (date_time, location))
    conflict = cursor.fetchone()

    if conflict:
        return jsonify({
            'error': 'A practice is already scheduled at this time and location.'
        }), 409  


    insert_query = '''
        INSERT INTO Practice (DateTime, Location, TeamID, DirectorID)
        VALUES (%s, %s, %s, %s)
    '''
    cursor.execute(insert_query, (date_time, location, team_id, 131))
    db.get_db().commit()

    return jsonify({'message': 'Practice added successfully'}), 200

#------------------------------------------------------------------
#removes a practice  
@athletic_director.route('/athletic_director/practices', methods=['DELETE'])
def delete_practice():
    cursor = db.get_db().cursor()
    practice_id = request.args.get('PracticeID')

    if not practice_id:
        return jsonify({'error': 'Please input practice_id!'}), 400

# checks and makes sure that the practice exists 
    check_query = '''
        SELECT * FROM Practice
        WHERE PracticeID = %s AND DirectorID = 131;
    '''
    cursor.execute(check_query, (practice_id,))
    result = cursor.fetchone()

    if not result:
        return jsonify({'error': f'Practice {practice_id} not found.'}), 404

    delete_query = '''
        DELETE FROM Practice
        WHERE PracticeID = %s AND DirectorID = 131;
    '''
    cursor.execute(delete_query, (practice_id,))
    db.get_db().commit()

    return jsonify({'message': f'Successfully cancelled practice {practice_id}!'}), 200

#------------------------------------------------------------------
#gets all games

