import functools
import datetime
import mysql.connector
import json

from data_management.db import getDb
from flask import Blueprint, jsonify, request

bp = Blueprint('get', __name__, url_prefix='/get')


@bp.route('/runs', methods=(['GET']))
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

        print(run)
        print(run.get("PipeID"))

        if run.get("PipeID"):
            pipe = getPipe(db, run.get("PipeID"))
            run.update({'direction': pipe.get('Direction')})
            run.update({'Lat': pipe.get('Lat')})
            run.update({'Longi': pipe.get('Longi')})
        else:
            run.update({'direction': None})
            run.update({'Lat': None})
            run.update({'Longi': None})

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

    allVideos = [tagVids, namVids, noNamVids]

    return jsonify(allVideos)

# could also be called getVideo, as a run is equivialant the the video and all its info


@bp.route('/run', methods=(['POST']))
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
        run.update({'Lat': pipe.get('Lat')})
        run.update({'Longi': pipe.get('Longi')})
    else:
        run.update({'direction': None})
        run.update({'Lat': None})
        run.update({'Longi': None})

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


def getOldest(db):
    # Jero here
    # TODO
    # gets oldest untagged unamed file
    # if none exist, go to named and unpinned
    # else go to pinned
    # code exist above for how to find out, try to do all comparisons in mySQL
    return
