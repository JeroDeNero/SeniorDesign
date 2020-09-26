import functools
import mysql.connector
import json

from data_management.db import getDb
from data_management.get import getOldest, getRun, getTag, getVideo
from data_management.delete import garbageCollector

from flask import(
    Blueprint, request, jsonify
)

bp = Blueprint('export', __name__, url_prefix='/export')


@bp.route('/tag', methods=(['POST']))
def exportTag():

    db = getDB()
    tag = getTag(db, tagID)
    video = getVideo()

    query = ("SELECT * FROM Video "
         "WHERE Id = {}".format(video))
    date = query.DateTaken

    db.close()

    return jsonify({})
