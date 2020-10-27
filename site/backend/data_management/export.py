# pylint: disable=bare-except
"""to stop pylint from complainign about any excepts"""

import shapefile
import os

from flask_cors import CORS
from flask import(
    Blueprint, send_from_directory, request
)

from data_management.db import getDb
from data_management.get import getOldest, getRun, getTag, getVideo
from data_management.delete import garbageCollector

bp = Blueprint('export', __name__, url_prefix='/export')

CORS(bp)

SHPFILE = "data_management/temp/"


@bp.route('/tag/', methods=(['GET']))
def exportTag():
    global SHPFILE

    db = getDb()

    try:
        os.remove(SHPFILE + "coord.shp")
    except:
        print("new previous file.")

    target = request.args

    theDate = target.get["date"]
    longitude = target["long"]  # retrieve the x coordinate
    latitude = target["lat"]  # retrieve the y coordinate

    # writing a new shapefile
    sfw = shapefile.Writer(SHPFILE + "coord.shp", shapeType=shapefile.POINT)
    sfw.autobalance = True  # alternatively can be set to 1 for true

    # setting up the fields for writing the data to the shapefile
    sfw.field('xcord', 'N')  # xcoordinate
    sfw.field('ycord', 'N')  # ycoordinate
    sfw.field('Date', 'D')  # input the date

    sfw.point(longitude, latitude)  # write to shapefile
    # recording and saving the the shapefile
    sfw.record(longitude, latitude, theDate)

    sfw.close()
    db.close()

    try:
        return send_from_directory(SHPFILE, filename='coord.shp', as_attachment=True)
    except:
        return ({"unable to send file"})


@bp.route('/folder/<path>', methods=(['POST']))
def exportFolder():
    target = request.json

    print(target)

    try:
        return send_from_directory("data_management/../../frontend/src/assets/Data/", filename=target["dir"], as_attachment=True)
    except:
        print("failed")
        return ({"unable to send file"})
