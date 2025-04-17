########################################################
# Routes for Coach Blueprint
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db


coach = Blueprint('coach', __name__)
#------------------------------------------------------------------
# fetch all of coach's strategies
@coach.route('/coach/strategies', methods=['GET'])
def view_strategies():
    cursor = db.get_db().cursor()
    query = '''
        SELECT Strategies.Name, Strategies.Type, Strategies.Description
        FROM Strategies
        WHERE Strategies.TeamID = 1
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    return jsonify(theData), 200