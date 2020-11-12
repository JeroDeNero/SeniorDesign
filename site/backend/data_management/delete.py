from flask_cors import CORS
import shutil

from flask import(
    Blueprint, request, jsonify
)

from data_management.fileManager import removeRun, removeTag
from data_management.db import getDb

bp = Blueprint('delete', __name__, url_prefix='/delete')

CORS(bp)


@bp.route('/run', methods=(['POST']))
def run():
    """Recieves a remove run request"""

    data = request.json

    print(data)

    targetID = data.get("Id")
    pipe = data.get("pipeID")
    date = data.get("date")

    db = getDb()
    deleteRunTask(db, targetID)
    db.close()
    removeRun(pipe, date)

    return jsonify({})


@bp.route('/tag', methods=(['POST']))
def deleteTag():
    """Recieves a remove tag request"""

    data = request.json

    tagID = data.get("Id")

    db = getDb()
    deleteTagTask(db, tagID)
    db.close()

    return jsonify({})


def deleteRunTask(db, targetID):
    """Actually removes a run based upon an targetID, using the sent db"""

    tagCursor = db.cursor(dictionary=True, buffered=True)
    requestTags = ("SELECT TagID FROM VideoToTags "
                   "WHERE VideoID = {}".format(targetID))

    tagCursor.execute(requestTags)

    for tag in tagCursor:
        deleteTagTask(db, tag.get('TagID'))
        # don't need to worry about the middle table, as it has oncascade delete

    tagCursor.close()

    deleteVideoTask(db, targetID)


def deleteVideoTask(db, targetID):
    """makes/ and sends the deleteion query for a video using targetID"""
    deleteIt(db, 'DELETE FROM Video WHERE Id = {}'.format(targetID))


def deleteTagTask(db, targetID):
    """makes/ and sends the deleteion query for a Tag using targetID"""
    deleteIt(db, 'DELETE FROM TaggedLocs WHERE Id = {}'.format(targetID))


def deletePipeTask(db, targetID):
    """makes/ and sends the deleteion query for a Pipe using targetID"""
    deleteIt(db, 'DELETE FROM Pipe WHERE Id = {}'.format(targetID))


def deleteIt(db, queury):
    """Recieves a delete query then runs it"""
    print(queury)
    delCursor = db.cursor(dictionary=True, buffered=True)
    delCursor.execute(queury)
    db.commit()
    delCursor.close()


def garbageCollector():
    # Jero here
    db = getDb()

    # Get available space
    total, used, free = shutil.disk_usage("/")

    # while space is less that 20% delete oldest unamed file
    while(free/total < 0.2):
        # using shutil to calculate disk usage
        total, used, free = shutil.disk_usage("/")

        # get oldest takes db, and
        oldest = getOldest(db)
        vidID = oldest.get('Id')
        pipeID = oldest.get('PipeID')

        # Create and execute multiple queries to free up space
        runQuery = deleteRunTask(db, vidID)
        deleteIt(db, runQuery)

        vidQuery = deleteVideoTask(db, vidID)
        deleteIt(db, vidQuery)

        tagQuery = deleteTagTask(db, vidID)
        deleteIt(db, tagQuery)

    return
