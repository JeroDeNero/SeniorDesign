import functools
import datetime
import mysql.connector

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

    for row in Videos:

        video = db.cursor(buffered=True)
        query = ("SELECT TagID FROM VideoToTags "
                 "WHERE VideoID = {}".format(row.get('Id')))

        video.execute(query)
        vidTags = []

        for tagID in video:

            tags = db.cursor(dictionary=True, buffered=True)
            query = ("SELECT * FROM TaggedLocs "
                     "WHERE Id = {}".format(tagID[0]))

            tags.execute(query)
            vidTags.append(tags.fetchone())
            tags.close

        row.update({'tag': vidTags})
        video.close()

        if (row.get('PipeID') != None):
            pipe = db.cursor(dictionary=True, buffered=True)
            query = ("SELECT * FROM Pipe "
                     "WHERE Id = '{}'".format(row.get('PipeID')))

            pipe.execute(query)
            value = pipe.fetchone()

            row.update({'direction': value.get('Direction')})
            row.update({'lat': value.get('Lat')})
            row.update({'long': value.get('Longi')})

            pipe.close()
        else:
            row.update({'direction': None})
            row.update({'lat': None})
            row.update({'long': None})

        if (row.get('Tagged') != None):
            tagVids.append(row)
        elif (row.get('Tagged') == None and row.get('Name') != 'None'):
            namVids.append(row)
        else:
            noNamVids.append(row)

    Videos.close()
    db.close()

    allVideos = [tagVids, namVids, noNamVids, {'videoID': -1}]

    return jsonify(allVideos)


@ bp.route('/deleteRun', methods=(['GET']))
def deleteRun():
    id = request.form['id']

    print(id)

    db = getDb()
    tagCursor = db.cursor(dictionary=True, buffered=True)

    requestTags = ("SELECT TagID FROM VideoToTags"
                   "WHERE VideoID = {}".format(id))

    tagCursor.execute(requestTags)

    for tag in tagCursor:

        highlightedZones = db.cursor(dictionary=True, buffered=True)

        requestHL = ("SELECT HighlightID FROM TagToHighlights"
                     "WHERE LocationID = {}".format(tag.get('TagID')))

        highlightedZones.execute(requestHL)

        for HL in highlightedZones:

            db.execute('DELETE FROM HighlightedZones WHERE Id = {}'.format(
                HL.get('HighlightID')))
            db.commit()

        highlightedZones.close()

        db.execute('DELETE FROM TaggedLocs WHERE Id = {}'.format(
            tag.get('TagID')))
        db.commit()

    tagCursor.close()

    db.execute('DELETE FROM Video WHERE Id = {}'.format(id))
    db.commit()
    db.close

    return 'TODO Callum'
