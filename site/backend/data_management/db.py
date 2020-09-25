import mysql.connector

import click
from flask import current_app, g
from flask.cli import with_appcontext


def getDb():
    if 'db' not in g:
        g.db = mysql.connector.connect(user='roboto',
                                       password='password',
                                       host='127.0.0.1',
                                       database='SewerBot'
                                       )
    return g.db


def closeDb():
    db = g.pop('db', None)

    if db is not None:
        db.close()


def initApp(app):
    app.teardown_appcontext(closeDb())
