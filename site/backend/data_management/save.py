import os

from flask import Blueprint, jsonify, request
from flask_cors import CORS

from data_management.db import getDb
from data_management.get import getVideo
from data_management.streams import rebootStream
from data_management.tempFileManger import moveFiles

bp = Blueprint('save', __name__, url_prefix='/save')

CORS(bp)


@bp.route('/settings', methods=(['POST']))
def settings():
    """updates the settings in both the file and backend"""
    data = request.json

    wheelRadius = data['wheelRad']
    mainCam = data['mainCamFPS']
    secondaryCam = data['backCamFPS']

    if 'WHEEL_RADIUS' not in os.environ is None:
        os.environ['WHEEL_RADIUS'] = '6'
    elif (wheelRadius and wheelRadius != os.environ.get('WHEEL_RADIUS')):
        os.environ.pop('WHEEL_RADIUS')
        os.environ['WHEEL_RADIUS'] = str(wheelRadius)

    if 'MAIN_FPS' not in os.environ:
        os.environ['MAIN_FPS'] = '20'
    elif (mainCam and mainCam != os.environ.get('MAIN_FPS')):
        os.environ.pop('MAIN_FPS')
        os.environ['MAIN_FPS'] = str(mainCam)

    if "SECONDARY_FPS" not in os.environ:
        os.environ['SECONDARY_FPS'] = '20'
    elif (secondaryCam and secondaryCam != os.environ.get('SECONDARY_FPS')):
        os.environ.pop('SECONDARY_FPS')
        os.environ['SECONDARY_FPS'] = str(secondaryCam)

    with open("data_management/../.env", "w") as f:
        f.write("MAIN_FPS={}\n".format(os.environ['MAIN_FPS']))
        f.write("SECONDARY_FPS={}\n".format(os.environ['SECONDARY_FPS']))
        f.write("WHEEL_RADIUS={}\n".format(os.environ['WHEEL_RADIUS']))

    rebootStream()

    return jsonify({})


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