# pylint: disable=bare-except
"""to stop pylint from complainign about any excepts"""

import shapefile
import shutil
import glob
import os

from datetime import datetime
from flask_cors import CORS
from flask import(
    Blueprint, send_from_directory, send_file, request
)

from data_management.get import getOldest, getRun, getTag, getVideo
from data_management.delete import garbageCollector
from data_management.tempFileManger import remove

bp = Blueprint('export', __name__, url_prefix='/export')

CORS(bp)

TMPLOC = "data_management/temp/"


@bp.route('/tag/<target>')
def exportTag(target):
    global TMPLOC

    try:
        os.remove(TMPLOC + "coord.shp")
    except:
        print("new previous file.")

    # have to use "get" so I have ended up with magic numbers sorry.
    # [0] = date [1] = long [2] = lat
    parsedTarget = target.split('b')

    theDate = datetime.strptime(parsedTarget[0], '%Y-%m-%d_%H:%M:%S')
    longitude = float(parsedTarget[1])
    latitude = float(parsedTarget[2])

    # writing a new shapefile
    sfw = shapefile.Writer(TMPLOC + "coord.shp", shapeType=shapefile.POINT)
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

    try:
        return send_from_directory("temp/", filename="coord.shp", as_attachment=True)
    except:
        print("unable to send file")
        return ("unable to send file")

    return""


@ bp.route('/folder/<path>')
def exportFolder(path):
    global TMPLOC

    remove(glob.glob('data_management/temp/*.zip'))

    # [0] = pipe ID, [1] = date/time taken
    parsedTarget = path.split('!')

    pipeID = parsedTarget[0]
    date = parsedTarget[1]
    print(path)
    print(parsedTarget)

    fileName = "{}_{}_Data".format(pipeID, date)
    directory = "data_management/../../frontend/dist/site/assets/Data/{}/".format(
        pipeID)

    shutil.make_archive("data_management/temp/{}".format(fileName), 'zip',
                        directory, date)

    try:
        return send_from_directory("temp/", filename='{}.zip'.format(fileName), as_attachment=True)
    except:
        print("failed")
        return ("unable to send file")
