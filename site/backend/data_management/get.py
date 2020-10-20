from data_management.db import getDb
from flask import Blueprint, jsonify, request

bp = Blueprint('get', __name__, url_prefix='/get')


@bp.route('/runs', methods=(['GET']))
def getRuns():
    """gets all Runs in the database"""

    db = getDb()
    videos = db.cursor(dictionary=True, buffered=True)

    videos.execute("SELECT * FROM Video ORDER BY Name ASC, DateTaken ASC")

    tagVids = []
    namVids = []
    noNamVids = []

    for run in videos:

        tags = getTagIDs(db, run.get('Id'))
        vidTags = []

        for tag in tags:
            vidTags.append(getTag(db, tag[0]))

        run.update({'tag': vidTags})

        if run.get("PipeID"):
            pipe = getPipe(db, run.get("PipeID"))
            run.update({'Lat': pipe.get('Lat')})
            run.update({'Longi': pipe.get('Longi')})
        else:
            run.update({'Lat': None})
            run.update({'Longi': None})

        run.update({'ShowRun': True})
        run.update({'ShowTag': False})

        if (run.get('Tagged') and run.get('Tagged') > 0):
            tagVids.append(run)
        elif ((run.get('Tagged') == None or run.get('Tagged') == 0) and run.get('Name') != None and run.get('Name') != ''):
            namVids.append(run)
        else:
            noNamVids.append(run)

    videos.close()
    db.close()

    allVideos = [tagVids, namVids, noNamVids]

    return jsonify(allVideos)

# could also be called getVideo, as a run is equivialant the the video and all its info


@bp.route('/run', methods=(['POST']))
def getRun():
    """Get a single run"""

    target = request.json
    return jsonify(buildRun(target["id"]))


def buildRun(target):
    """Builds a single run"""

    db = getDb()

    run = getVideo(db, target)
    tags = getTagIDs(db, run.get('Id'))
    vidTags = []

    for tag in tags:
        vidTags.append(getTag(db, tag[0]))

    run.update({'tag': vidTags})

    if run.get("PipeID"):
        pipe = getPipe(db, run.get("PipeID"))
        run.update({'Lat': pipe.get('Lat')})
        run.update({'Longi': pipe.get('Longi')})
    else:
        run.update({'Lat': None})
        run.update({'Longi': None})

        run.update({'ShowRun': True})
        run.update({'ShowTag': False})

    return run


def getVideo(db, vidID):
    """Get gets the video information for a run"""
    getter = db.cursor(dictionary=True, buffered=True)

    query = ("SELECT * FROM Video "
             "WHERE Id = {}".format(vidID))

    getter.execute(query)

    results = getter.fetchone()
    getter.close()
    return results


def getTagIDs(db, vidID):
    """Get gets the tags involved in a run"""
    tags = db.cursor(buffered=True)
    query = ("SELECT TagID FROM VideoToTags "
             "WHERE VideoID = {}"
             "ORDER BY VideoTime ASC").format(vidID)

    tags.execute(query)
    results = tags.fetchall()
    tags.close()
    return results


def getTag(db, tagID):
    """Get gets the tag information for a tagID"""
    tag = db.cursor(dictionary=True, buffered=True)
    query = ("SELECT * FROM TaggedLocs "
             "WHERE Id = {}".format(tagID))

    tag.execute(query)

    results = tag.fetchone()
    tag.close()
    return results.update()


def getPipe(db, pipeID):
    """Get gets the video information for a run"""
    pipe = db.cursor(dictionary=True, buffered=True)
    query = ("SELECT * FROM Pipe "
             "WHERE Id = '{}'".format(pipeID))

    pipe.execute(query)

    results = pipe.fetchone()
    pipe.close()
    return results


def getOldest(db):
    # Jero here
    # TODO
    # gets oldest untagged unamed file
    # if none exist, go to named and unpinned
    # else go to pinned
    # code exist above for how to find out, try to do all comparisons in mySQL
    return
