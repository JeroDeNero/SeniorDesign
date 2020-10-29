# pylint: disable=bare-except
"""to stop pylint from complainign about any excepts"""

import shapefile
import os

from datetime import datetime
from flask_cors import CORS
from flask import(
    Blueprint, send_from_directory, send_file, request
)

from data_management.db import getDb
from data_management.get import getOldest, getRun, getTag, getVideo
from data_management.delete import garbageCollector

bp = Blueprint('export', __name__, url_prefix='/export')

CORS(bp)

SHPFILE = "data_management/temp/"


@bp.route('/tag/<target>')
def exportTag(target):
    global SHPFILE

    db = getDb()

    try:
        os.remove(SHPFILE + "coord.shp")
    except:
        print("new previous file.")

    print(target)

    # have to use get so I have ended up with magic numbers sorry.
    # [1] = date [2] = long [3] = lat
    parsedTarget = str(request).split('b')

    print(parsedTarget)

    theDate = datetime.strptime(parsedTarget[1], '%Y-%m-%d_%H:%M:%S')
    longitude = float(parsedTarget[2])
    latitude = float(parsedTarget[3])

    # writing a new shapefile
    sfw = shapefile.Writer(SHPFILE + "coord.shp", shapeType=shapefile.POINT)
    sfw.autobalance = True  # alternatively can be set to 1 for true

    # setting up the fields for writing the data to the shapefile
    sfw.field('xcord', 'N')  # xcoordinate
    sfw.field('ycord', 'N')  # ycoordinate
    sfw.field('Date', 'D')  # input the date

    print("{} {} {}".format(theDate, longitude, latitude))

    sfw.point(longitude, latitude)  # write to shapefile
    # recording and saving the the shapefile
    sfw.record(longitude, latitude, theDate)

    sfw.close()
    db.close()

    return send_from_directory("temp/", filename="coord.shp", as_attachment=True)

    try:
        return send_file("temp/coord.shp", as_attachment=True)
    except:
        print("unable to send file")
        return ("unable to send file")

    return""


@ bp.route('/folder/<path>', methods=(['POST']))
def exportFolder():
    target = request.json

    print(target)

    try:
        return send_from_directory("data_management/../../frontend/src/assets/Data/", filename=target["dir"], as_attachment=True)
    except:
        print("failed")
        return ({"unable to send file"})
