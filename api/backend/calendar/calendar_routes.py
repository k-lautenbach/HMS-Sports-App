########################################################
# Calendar Routes
########################################################

from flask import Blueprint, request, jsonify
from backend.db_connection import db

calendar = Blueprint('calendar', __name__)

@calendar.route('/calendar/practices', methods=['GET'])
def get_team_practices():
    try:
        
        cursor = db.get_db().cursor()       
        query = '''
            SELECT PracticeID, DateTime, Location
            FROM Practice
            WHERE TeamID = 1
            ORDER BY DateTime ASC;
        '''
        cursor.execute(query,)
        cursor.execute(query,)
        theData = cursor.fetchall()
        return jsonify(theData), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'details': str(e)}), 500
#------------------------------------------------------------------
# show athlete games 

@calendar.route('/calendar/games', methods=['GET'])
def get_team_games():
    try:

        cursor = db.get_db().cursor()
        query = '''
            SELECT GameID, DateTime, Location
            FROM Game
            WHERE HomeTeamID = 1 OR AwayTeamID = 1
            ORDER BY DateTime ASC;
        '''
        cursor.execute(query, )
        theData = cursor.fetchall()
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
        return jsonify(theData), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'details': str(e)}), 500
#------------------------------------------------------------------
# show athlete recruiting events
@calendar.route('/calendar/recruitingevents', methods=['GET'])
def get_player_recruiting_events():
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT re.EventID, re.DateTime AS Date, re.Location
            FROM RecruitingEvents re
            JOIN AthleteEvent ae ON re.EventID = ae.EventID
            WHERE ae.PlayerID = 1
            ORDER BY re.DateTime ASC;
        '''
        cursor.execute(query,)
        theData = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
        return jsonify(theData), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'details': str(e)}), 500