########################################################
# Athlete Stats Blueprint of Endpoints
########################################################
from flask import Blueprint, request, jsonify
from backend.db_connection import db

athlete_stats_bp = Blueprint('athlete_stats', __name__)

#------------------------------------------------------------------
# GET single player's stats
@athlete_stats_bp.route('/s/athletestats/<int:player_id>', methods=['GET'])
def get_athlete_stats(player_id):
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT *
            FROM AthleteStats
            WHERE PlayerID = %s;
        '''
        cursor.execute(query, (player_id,))
        row = cursor.fetchone()

        if row:
            colnames = [desc[0] for desc in cursor.description]
            result = dict(zip(colnames, row))
            return jsonify(result), 200
        else:
            return jsonify({'message': 'No stats found for this player'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#------------------------------------------------------------------
# PUT update stats for a player
@athlete_stats_bp.route('/s/athletestats/<int:player_id>', methods=['PUT'])
def update_athlete_stats(player_id):
    try:
        cursor = db.get_db().cursor()
        data = request.get_json()

        query = '''
            UPDATE AthleteStats 
            SET TotalPoints = %s,
                GamesPlayed = %s,
                AssistsPerGame = %s,
                Rebounds = %s,
                PointsPerGame = %s,
                FreeThrowPercentage = %s,
                HighlightsURL = %s
            WHERE PlayerID = %s;
        '''
        cursor.execute(query, (
            data.get('TotalPoints'),
            data.get('GamesPlayed'),
            data.get('AssistsPerGame'),
            data.get('Rebounds'),
            data.get('PointsPerGame'),
            data.get('FreeThrowPercentage'),
            data.get('HighlightsURL'),
            player_id
        ))

        if cursor.rowcount == 0:
            return jsonify({'message': 'No stats found for this player'}), 404

        db.get_db().commit()
        return jsonify({'message': 'Stats updated successfully'}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({'error': str(e)}), 500

#------------------------------------------------------------------
# POST create new stats
@athlete_stats_bp.route('/s/athletestats', methods=['POST'])
def create_athlete_stats():
    try:
        cursor = db.get_db().cursor()
        data = request.get_json()

        query = '''
            INSERT INTO AthleteStats 
            (PlayerID, TotalPoints, GamesPlayed, AssistsPerGame, Rebounds, 
             PointsPerGame, FreeThrowPercentage, HighlightsURL)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
        cursor.execute(query, (
            data.get('PlayerID'),
            data.get('TotalPoints'),
            data.get('GamesPlayed'),
            data.get('AssistsPerGame'),
            data.get('Rebounds'),
            data.get('PointsPerGame'),
            data.get('FreeThrowPercentage'),
            data.get('HighlightsURL')
        ))

        db.get_db().commit()
        return jsonify({'message': 'Stats created successfully'}), 201
    except Exception as e:
        db.get_db().rollback()
        return jsonify({'error': str(e)}), 500

#------------------------------------------------------------------
# DELETE stats for a player
@athlete_stats_bp.route('/s/athletestats/<int:player_id>', methods=['DELETE'])
def delete_athlete_stats(player_id):
    try:
        cursor = db.get_db().cursor()

        query = '''
            DELETE FROM AthleteStats
            WHERE PlayerID = %s;
        '''
        cursor.execute(query, (player_id,))

        if cursor.rowcount == 0:
            return jsonify({'message': 'No stats found for this player'}), 404

        db.get_db().commit()
        return jsonify({'message': 'Stats deleted successfully'}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({'error': str(e)}), 500
