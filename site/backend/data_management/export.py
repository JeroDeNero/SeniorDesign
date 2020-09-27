import functools
import mysql.connector
import json
import shapefile

from data_management.db import getDb
from data_management.get import getOldest, getRun, getTag, getVideo
from data_management.delete import garbageCollector

from flask import(
    Blueprint, request, jsonify
)

bp = Blueprint('export', __name__, url_prefix='/export')


@bp.route('/tag', methods=(['POST']))
def exportTag():

    db = getDB() # access the DB
    tag = getTag(db, tagID) # get the coordinates
    video = getVideo() # get the Date
    
    path = #what is the path?

    sfw = shapefile.Writer(path, shapeType = shapefile.POINT) #writing a new shapefile
    sfw.autobalance = True #alternatively can be set to 1 for true

    #setting up the fields for writing the data to the shapefile
    sfw.field('Date', 'D') #input the date
    sfw.field('xcord', 'N') #xcoordinate
    sfw.field('ycord', 'N') #ycoordinate


    sfw.close()
    db.close()

    return jsonify({})
