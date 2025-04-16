from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

athletestats = Blueprint('athletestats', __name__)

# ------------------------------------------------------------
# get all stats of athlete
@athletestats.route('/athletestats', methods=['GET'])
def get_all_stats():
    query = '''
        SELECT StatsID, PlayerID, TotalPoints, GamesPlayed,
               AssistsPerGame, Rebounds, PointsPerGame,
               FreeThrowPercentage, HighlightsURL
        FROM AthleteStats
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    return make_response(jsonify(theData), 200)

# ------------------------------------------------------------
# get specific athlete stats
@athletestats.route('/athletestats/<int:stats_id>', methods=['GET'])
def get_specific_stats(stats_id):
    query = '''
        SELECT StatsID, PlayerID, TotalPoints, GamesPlayed,
               AssistsPerGame, Rebounds, PointsPerGame,
               FreeThrowPercentage, HighlightsURL
        FROM AthleteStats
        WHERE StatsID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (stats_id,))
    theData = cursor.fetchone()

    if theData:
        return make_response(jsonify(theData), 200)
# ------------------------------------------------------------
# Updating specific athlete stats
@athletestats.route('/athletestats/<int:stats_id>', methods=['PUT'])
def update_athlete_stats(stats_id):
    theData = request.json
    query = '''
        UPDATE AthleteStats
        SET TotalPoints = %s,
            GamesPlayed = %s,
            AssistsPerGame = %s,
            Rebounds = %s,
            PointsPerGame = %s,
            FreeThrowPercentage = %s,
            HighlightsURL = %s
        WHERE StatsID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (
        theData['TotalPoints'],
        theData['GamesPlayed'],
        theData['AssistsPerGame'],
        theData['Rebounds'],
        theData['PointsPerGame'],
        theData['FreeThrowPercentage'],
        theData['HighlightsURL'],
        stats_id
    ))
    db.get_db().commit()
    return make_response("Updated", 200)

# ------------------------------------------------------------
# Add new stats to athlete
@athletestats.route('/athletestats', methods=['POST'])
def add_new_athlete_stats():
    try:
        theData = request.json
        query = '''
            INSERT INTO AthleteStats 
            (PlayerID, TotalPoints, GamesPlayed, AssistsPerGame,
             Rebounds, PointsPerGame, FreeThrowPercentage, HighlightsURL)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query, (
            theData['PlayerID'],
            theData['TotalPoints'],
            theData['GamesPlayed'],
            theData['AssistsPerGame'],
            theData['Rebounds'],
            theData['PointsPerGame'],
            theData['FreeThrowPercentage'],
            theData['HighlightsURL']
        ))
        db.get_db().commit()
        return make_response("Added New stats", 200)

    except Exception as e:
        current_app.logger.error(f"POST /athletestats error: {e}")
        return jsonify({"error": str(e)}), 500
