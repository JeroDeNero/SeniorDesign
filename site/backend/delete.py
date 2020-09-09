import functools
import mysql.connector
import json

from backend.db import getDb

from flask import(
    Blueprint, request
)

bp = Blueprint('delete', __name__, url_prefix='/delete')


@bp.route('/run', methods=(['POST']))
def deleteRun():
    db = getDb()
    deleteRunTask(db, request.json["Id"])
    db.close


@bp.route('/deleteTag', methods=(['POST']))
def deleteTag():
    db = getDb()
    deleteTagTask(db, request.json["Id"])
    db.close()


def deleteRunTask(db, id):

    tagCursor = db.cursor(dictionary=True, buffered=True)

    requestTags = ("SELECT TagID FROM VideoToTags"
                   "WHERE VideoID = {}".format(id))

    tagCursor.execute(requestTags)

    for tag in tagCursor:
        deleteTagTask(db, tag.get('TagID'))

    tagCursor.close()

    db.execute('DELETE FROM Video WHERE Id = {}'.format(id))
    db.commit()


def deleteTagTask(db, id):

    highlightedZones = db.cursor(dictionary=True, buffered=True)
    requestHL = ("SELECT HighlightID FROM TagToHighlights"
                 "WHERE LocationID = {}".format(id))
    highlightedZones.execute(requestHL)

    for HL in highlightedZones:

        deleteHighlightTask(db, HL.get["HighlightID"])

    highlightedZones.close()

    db.execute('DELETE FROM TaggedLocs WHERE Id = {}'.format(id))
    db.commit()


def deleteHighlightTask(db, id):
    db.execute('DELETE FROM HighlightedZones WHERE Id = {}'.format(id))
    db.commit()


def deletePipeTask(db, id):
    db.execute('DELETE FROM Pipe WHERE Id = {}'.format(id))
    db.commit()


def deleteRoughLocTask(db, id):
    db.execute('DELETE FROM PipeToRoughLoc WHERE RoughLocID = {}'.format(id))
    db.commit()
    db.execute('DELETE FROM RoughLocation WHERE Id = {}'.format(id))
    db.commit()
