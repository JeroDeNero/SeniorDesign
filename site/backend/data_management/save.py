import functools
import datetime
import mysql.connector
import json

from data_management.db import getDb
from flask import Blueprint, jsonify, request

bp = Blueprint('save', __name__, url_prefix='/save')


@bp.route('/newRun', methods=(['POST']))
def newRun():

    db = getDb()

    input = request.json

    Name = input['Name']
    DriverName = input['DriverName']
    tagged = input['Tagged']
    PipeID = input['PipeID']
    Direction = input['Direction']
    Lat = input['Lat']
    Longi = input['Longi']
    error = None

    if not PipeID:
        error = 'PipeID is required.'
    elif not Direction:
        error = 'Direction is required.'

    if error is None:

        checker = db.cursor(dictionary=True, buffered=True)
        query = ("SELECT * "
                 "FROM Pipe "
                 "WHERE Id = '{}'".format(PipeID))

        checker.execute(query)

        if(not checker.fetchall()):
            query = ("INSERT INTO Pipe (Id, Direction, Lat, Longi)"
                     "VALUES ('{}', '{}', {}, {})".format(
                         PipeID, Direction, Lat, Longi))
            sendCommand(db, query)
            print(query)

        checker.close()

        query = ("INSERT INTO Video (Name, PipeID, DriverName, DateTaken, Tagged) VALUES"
                 "('{}', '{}', '{}', CURDATE(), {})".format(
                     Name, PipeID, DriverName, tagged))
        sendCommand(db, query)

        print(query)

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

def sendCommand(db, query):
    update = db.cursor(dictionary=True, buffered=True)
    update.execute(query)
    db.commit()
    update.close()
