from flask import Blueprint, jsonify, request

from data_management.db import getDb
from data_management.get import getVideo
from data_management.tempFileManger import moveFiles

bp = Blueprint('save', __name__, url_prefix='/save')


@bp.route('/newRun', methods=(['POST']))
def newRun():
    """Inserts a new run"""

    db = getDb()

    userInput = request.json

    name = userInput['Name']
    driverName = userInput['DriverName']
    tagged = userInput['Tagged']
    pipeID = userInput['PipeID']
    direction = userInput['Direction']
    lat = userInput['Lat']
    longi = userInput['Longi']
    tags = userInput['Tags']
    error = None

    if not pipeID:
        error = 'PipeID is required.'
    elif not direction:
        error = 'Direction is required.'

    if error is None:

        checker = db.cursor(dictionary=True, buffered=True)
        query = ("SELECT * "
                 "FROM Pipe "
                 "WHERE Id = '{}'".format(pipeID))

        checker.execute(query)

        if(not checker.fetchall()):
            query = ("INSERT INTO Pipe (Id, Lat, Longi)"
                     "VALUES ('{}', {}, {})".format(
                         pipeID, lat, longi))
            sendCommand(db, query)

        checker.close()

        query = ("INSERT INTO Video (Name, PipeID, DriverName, DateTaken, Tagged, Direction) VALUES"
                 "('{}', '{}', '{}', NOW(), {}, {})".format(
                     name, pipeID, driverName, tagged, direction))
        videoID = sendCommand(db, query)
        print(videoID)
        videoData = getVideo(db, videoID)

        moveFiles(videoData.get('PipeID'), str(videoData.get('DateTaken')).replace(' ', '_'))

        #add tags now

    return jsonify({})


@bp.route('/editRun', methods=(['POST']))
def editRun():
    """edits a runs information"""
    db = getDb()
    userInput = request.json

    updateVideo(db, userInput["Id"], userInput["Name"],
                userInput["DriverName"], userInput["Tagged"])
    return jsonify({})


def updateVideo(db, targ, name, driverName, tagged):
    """updates information in the Video table"""
    query = ("UPDATE Video SET "
             "Name = '{}', DriverName = '{}', Tagged = {} "
             "WHERE Id = {} ".format(name, driverName, tagged, targ))

    sendCommand(db, query)


def updatePipe(db, targ, newName, lat, long, dir):
    """updates the information in the pipe table"""
    query = (" UPDATE Pipe SET "
             "Id = '{}', Lat = {}, Longi = {}, Direction = '{}' "
             "WHERE Id = '{}' ".format(newName, lat, long, dir, targ))

    sendCommand(db, query)


def updateRoughLoc(db, targ, name, lat, long, rad):
    """updates rough location"""
    query = ("UPDATE RoughLocation "
             "Name = {}, Lat = {}, Longi = {}, Raduis = {} "
             "WHERE Id = {} ".format(name, lat, long, rad, targ))

    sendCommand(db, query)


# To be moved into a new files, and move it into a file

def sendCommand(db, query):
    """takes a query and then runs it. and commits the update.  also updates the most recently updated row"""
    update = db.cursor(dictionary=True, buffered=True)
    update.execute(query)
    value = update.lastrowid
    db.commit()
    update.close()

    #value is the value of the most recent created ID
    return value