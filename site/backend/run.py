import functools
import datetime
import mysql.connector
import json

from backend.db import getDb
from flask import Blueprint, jsonify, request

bp = Blueprint('run', __name__, url_prefix='/run')


@bp.route('/newRun', methods=(['POST']))
def newRun():

    db = getDb()
    
    PipeID = request.form['PipeID']
    Direction = request.form['Direction']
    Lat = request.form['Lat']
    Longi = request.form['Longi']
    error = None

    def deleteIt(db, query):
        delCursor = db.cursor(dictionary = True, buffered = True)
        delCursor.execute(query)
        db.commit()
        delCursor.close()

    if PipeID:
        error = 'PipeID is required.'
    elif not Direction:
        error = 'Direction is required.'

    if error is None:
        query = "INSERT INTO pipe (PipeID, Direction, Lat, Longi) VALUES {}, {}, {}, {}".format(PipeID, Direction, Lat, Longi)
        deleteIt(db, query)

        query = "INSERT INTO Videos (RunName, PipeID, DriverName, DateTaken) VALUES {}, {}, {}, {}".format(Name, PipeID, DriverName, DateTaken)
        deleteIt(db, query)

    return jsonify({})


@bp.route('/editRun', methods=(['POST']))
def editRun():
    db = getDb()
    input = request.json

    updateVideo(db, input["Id"], input["Name"],
                input["DriverName"], input["Tagged"])
    return jsonify({})


def updateVideo(db, targ, name, driverName, tagged):
    query = ("UPDATE Video SET "
             "Name = '{}', DriverName = '{}', Tagged = {} "
             "WHERE Id = {} ".format(name, driverName, tagged, targ))

    sendCommand(db, query)


def updatePipe(db, targ, newName, lat, long, dir):
    query = (" UPDATE Pipe SET "
             "Id = '{}', Lat = {}, Longi = {}, Direction = '{}' "
             "WHERE Id = '{}' ".format(newName, lat, long, dir, targ))

    sendCommand(db, query)


def updateRoughLoc(db, targ, name, lat, long, rad):
    query = ("UPDATE RoughLocation "
             "Name = {}, Lat = {}, Longi = {}, Raduis = {} "
             "WHERE Id = {} ".format(name, lat, long, rad, targ))

    sendCommand(db, query)


# To be moved into a new files, and move it into a file
@bp.route('/getRuns', methods=(['GET']))
def getRuns():

    db = getDb()
    Videos = db.cursor(dictionary=True, buffered=True)

    Videos.execute("SELECT * FROM Video")

    tagVids = []
    namVids = []
    noNamVids = []

    for run in Videos:

        tags = getTagIDs(db, run.get('Id'))
        vidTags = []

        for tag in tags:
            vidTags.append(getTag(db, tag[0]))

        run.update({'tag': vidTags})

        if run.get("PipeID"):
            pipe = getPipe(db, run.get("PipeID"))
            run.update({'direction': pipe.get('Direction')})
            run.update({'lat': pipe.get('Lat')})
            run.update({'long': pipe.get('Longi')})
        else:
            run.update({'direction': None})
            run.update({'lat': None})
            run.update({'long': None})

        run.update({'ShowRun': True})
        run.update({'ShowTag': False})

        if (run.get('Tagged') != None and run.get('Tagged') > 0):
            tagVids.append(run)
        elif ((run.get('Tagged') == None or run.get('Tagged') == 0) and run.get('Name') != None and run.get('Name') != ''):
            namVids.append(run)
        else:
            noNamVids.append(run)

    Videos.close()
    db.close()

    allVideos = [tagVids, namVids, noNamVids, {'videoID': -1}]

    return jsonify(allVideos)

# could also be called getVideo, as a run is equivialant the the video and all its info


@bp.route('/getRun', methods=(['POST']))
def getRun():

    target = request.json
    return jsonify(buildRun(target["id"]))


def buildRun(target):

    db = getDb()

    run = getVideo(db, target)
    tags = getTagIDs(db, run.get('Id'))
    vidTags = []

    for tag in tags:
        vidTags.append(getTag(db, tag[0]))

    run.update({'tag': vidTags})

    if run.get("PipeID"):
        pipe = getPipe(db, run.get("PipeID"))
        run.update({'direction': pipe.get('Direction')})
        run.update({'lat': pipe.get('Lat')})
        run.update({'long': pipe.get('Longi')})
    else:
        run.update({'direction': None})
        run.update({'lat': None})
        run.update({'long': None})

        run.update({'ShowRun': True})
        run.update({'ShowTag': False})

    return run


def getVideo(db, vidID):
    getter = db.cursor(dictionary=True, buffered=True)

    query = ("SELECT * FROM Video "
             "WHERE Id = {}".format(vidID))

    getter.execute(query)

    results = getter.fetchone()
    getter.close
    return results


def getTagIDs(db, vidID):
    tags = db.cursor(buffered=True)
    query = ("SELECT TagID FROM VideoToTags "
             "WHERE VideoID = {}".format(vidID))

    tags.execute(query)
    results = tags.fetchall()
    tags.close
    return results


def getTag(db, tagID):
    tag = db.cursor(dictionary=True, buffered=True)
    query = ("SELECT * FROM TaggedLocs "
             "WHERE Id = {}".format(tagID))

    tag.execute(query)

    results = tag.fetchone()
    tag.close
    return results


def getPipe(db, pipeID):
    pipe = db.cursor(dictionary=True, buffered=True)
    query = ("SELECT * FROM Pipe "
             "WHERE Id = '{}'".format(pipeID))

    pipe.execute(query)

    results = pipe.fetchone()
    pipe.close
    return results


def sendCommand(db, query):
    update = db.cursor(dictionary=True, buffered=True)
    update.execute(query)
    db.commit()
    update.close()
