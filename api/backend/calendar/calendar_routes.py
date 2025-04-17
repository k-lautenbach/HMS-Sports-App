from flask import Blueprint, request, jsonify
from backend.db_connection import db

calendar = Blueprint('calendar', __name__)

@calendar.route('/calendar/practices', methods=['GET'])
def get_team_practices():
    try:
        team_id = request.args.get('team_id')
        if not team_id:
            return jsonify({'error': 'Missing team_id'}), 400

        cursor = db.get_db().cursor()
        query = '''
            SELECT PracticeID, Date, Time, Location
            FROM Practice
            WHERE TeamID = %s
            ORDER BY Date ASC;
        '''
        cursor.execute(query, (team_id,))
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
        return jsonify([dict(zip(colnames, row)) for row in rows]), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'Failed to fetch practices', 'details': str(e)}), 500

@calendar.route('/calendar/games', methods=['GET'])
def get_team_games():
    try:
        team_id = request.args.get('team_id')
        if not team_id:
            return jsonify({'error': 'Missing team_id'}), 400

        cursor = db.get_db().cursor()
        query = '''
            SELECT GameID, Date, Time, Location
            FROM Game
            WHERE HomeTeamID = %s OR AwayTeamID = %s
            ORDER BY Date ASC;
        '''
        cursor.execute(query, (team_id, team_id))
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
        return jsonify([dict(zip(colnames, row)) for row in rows]), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'Failed to fetch games', 'details': str(e)}), 500

@calendar.route('/calendar/recruitingevents', methods=['GET'])
def get_player_recruiting_events():
    try:
        player_id = request.args.get('player_id')
        if not player_id:
            return jsonify({'error': 'Missing player_id'}), 400

        cursor = db.get_db().cursor()
        query = '''
            SELECT re.EventID, re.DateTime AS Date, re.Location
            FROM RecruitingEvents re
            JOIN AthleteEvent ae ON re.EventID = ae.EventID
            WHERE ae.PlayerID = %s
            ORDER BY re.DateTime ASC;
        '''
        cursor.execute(query, (player_id,))
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
        return jsonify([dict(zip(colnames, row)) for row in rows]), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'Failed to fetch recruiting events', 'details': str(e)}), 500
