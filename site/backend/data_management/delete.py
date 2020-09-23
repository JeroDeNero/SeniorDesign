import functools
import mysql.connector
import json

from data_management.db import getDb

from flask import(
    Blueprint, request, jsonify
)

bp = Blueprint('delete', __name__, url_prefix='/delete')


@bp.route('/run', methods=(['POST']))
def run():
    db = getDb()
    deleteRunTask(db, request.json["Id"])
    db.close

    return jsonify({})


@bp.route('/tag', methods=(['POST']))
def deleteTag():
    db = getDb()
    deleteTagTask(db, request.json["Id"])
    db.close()

    return jsonify({})


def deleteRunTask(db, id):

    tagCursor = db.cursor(dictionary=True, buffered=True)
    print(id)
    requestTags = ("SELECT TagID FROM VideoToTags "
                   "WHERE VideoID = {}".format(id))

    tagCursor.execute(requestTags)

    for tag in tagCursor:
        deleteTagTask(db, tag.get('TagID'))

    tagCursor.close()

    deleteIt(db, 'DELETE FROM Video WHERE Id = {}'.format(id))


def deleteTagTask(db, id):

    highlightedZones = db.cursor(dictionary=True, buffered=True)
    requestHL = ("SELECT HighlightID FROM TagToHighlights "
                 "WHERE LocationID = {}".format(id))
    highlightedZones.execute(requestHL)

    for HL in highlightedZones:

        deleteHighlightTask(db, HL.get["HighlightID"])

    highlightedZones.close()

    deleteIt(db, 'DELETE FROM TaggedLocs WHERE Id = {}'.format(id))


def deleteHighlightTask(db, id):
    deleteIt(db, 'DELETE FROM HighlightedZones WHERE Id = {}'.format(id))


def deletePipeTask(db, id):
    deleteIt(db, 'DELETE FROM Pipe WHERE Id = {}'.format(id))


def deleteRoughLocTask(db, id):
    deleteIt(db, 'DELETE FROM PipeToRoughLoc WHERE RoughLocID = {}'.format(id))
    deleteIt(db, 'DELETE FROM RoughLocation WHERE Id = {}'.format(id))


def deleteIt(db, queury):
    delCursor = db.cursor(dictionary=True, buffered=True)
    delCursor.execute(queury)
    db.commit()
    delCursor.close()


def garbageCollector():
    # Jero here
    # TODO
    # Get available space
    # while space is less that 20% delete oldest unamed file
    # get oldest takes db, and
    return
