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
        print("unable to send .shp file")
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

    try:
        shutil.make_archive("data_management/temp/{}".format(fileName), 'zip',
                            directory, date)
    except:
        print("Failed to make zip")
        return ("unable to make file")

    try:
        return send_from_directory("temp/", filename='{}.zip'.format(fileName), as_attachment=True)
    except:
        print("Failed to send zip")
        return ("unable to send file")


@ bp.route('/image/<path>')
def exportImage(path):
    global TMPLOC

    # [0] = pipe ID, [1] = date/time taken, [2] tag position
    parsedTarget = path.split('!')

    pipeID = parsedTarget[0]
    date = parsedTarget[1]
    tagNum = parsedTarget[2]

    directory = "../../frontend/dist/site/assets/Data/{}/{}/tags/".format(
        pipeID, date)
    target = 'tag' + tagNum + '.jpg'

    print(directory)
    print(target)

    try:
        return send_from_directory(directory, filename=target, as_attachment=True)
    except:
        print("failed to send Image")
        return ("unable to send file")

def exportAllTag(db, runID):
    
    tagCursor = db.cursor(dictionary = True, buffered = True)
    requestTags = ("SELECT * FROM TaggedLocs "
                   "WHERE Id = {}".format(runID))
    
    tagCursor.execute(requestTags)

    # writing a new shapefile
    sfw = shapefile.Writer(TMPLOC + "coord.shp", shapeType=shapefile.POINT)
    sfw.autobalance = True  # alternatively can be set to 1 for true

    sfw.field('xcord', 'N')  # xcoordinate
    sfw.field('ycord', 'N')  # ycoordinate

    i = 0
    for tag in tagCursor:
        longitude = float(tag[2])
        latitude = float(tag[3])

        print("{} {}".format(longitude, latitude))
        sfw.point(longitude, latitude)  # write to shapefile
        sfw.record('point' + i)
        i += 1

    sfw.close()

    try:
        return send_from_directory("temp/", filename="completeRun.shp", as_attachment=True)
    except:
        print("unable to send .shp file")
        return ("unable to send file")

    return""