import functools
import mysql.connector
import json

from data_management.db import getDb
from data_management.get import getOldest, getRun, getTag
from data_management.delete import garbageCollector

from flask import(
    Blueprint, request, jsonify
)

bp = Blueprint('export', __name__, url_prefix='/export')


@bp.route('/tag', methods=(['POST']))
def exportTag():
    # Jero Here
    return jsonify({})
