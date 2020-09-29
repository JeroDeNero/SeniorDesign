import functools
import mysql.connector
import json
import shapefile

from data_management.db import getDb
from data_management.get import getOldest, getRun, getTag, getVideo
from data_management.delete import garbageCollector

from flask import(
    Blueprint, request, jsonify, send_file
)

bp = Blueprint('export', __name__, url_prefix='/export')


@bp.route('/locationExport', methods=(['POST']))
def exportTag():

    db = getDb() # access the DB
    runID = getRun() # obtain the run ID i.e. PipeID
    tagData = getTag(db, runID) # get coords
    video = getVideo(db, runID) # get the video info i.e. date

    theDate = video.get("DateTaken") # retrieve the date
    longitude = tagData.get("Longi") # retrieve the x coordinate
    latitude = tagData.get("Lat") # retrieve the y coordinate

    sfw = shapefile.Writer('TEMP/tmp_coord.shp', shapeType = shapefile.POINT) # writing a new shapefile
    sfw.autobalance = True # alternatively can be set to 1 for true

    # setting up the fields for writing the data to the shapefile
    sfw.field('xcord', 'N') # xcoordinate
    sfw.field('ycord', 'N') # ycoordinate
    sfw.field('Date', 'D') # input the date

    # write the shapefile
    sfw.point(longitude, latitude)
    sfw.record(longitude, latitude, theDate)

    sfw.close()
    db.close()

    return send_file('/TEMP/tmp_coord.shp', attachment_filename = 'coord.shp')
