import functools
import datetime
import mysql.connector
import json

from backend.db import getDb

from flask import(
    Blueprint, jsonify, request
)

bp = Blueprint('run', __name__, url_prefix='/run')


@bp.route('/newRun', methods=(['GET']))
def newRun():
    return 'TODO Jero'


@bp.route('/editRun', methods=(['GET']))
def editRun():
    return 'TODO Callum'


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

        if (run.get('Tagged') != None):
            tagVids.append(run)
        elif (run.get('Tagged') == None and run.get('Name') != 'None'):
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
