import functools
import mysql.connector
import json

from backend.db import getDb
from backend.get import getOldest, getRun, getTag
from backend.delete import garbageCollector

from flask import(
    Blueprint, request, jsonify
)

bp = Blueprint('export', __name__, url_prefix='/export')


@bp.route('/tag', methods=(['POST']))
def exportTag():
    # Jero Here
    return jsonify({})
