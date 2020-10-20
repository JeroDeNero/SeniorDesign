import mysql.connector
from flask import g


def getDb():
    """Gets a database"""
    if 'db' not in g:
        g.db = mysql.connector.connect(user='roboto',
                                       password='password',
                                       host='127.0.0.1',
                                       database='SewerBot'
                                       )
    return g.db


def closeDb():
    """Closing a database"""
    db = g.pop('db', None)

    if db is not None:
        db.close()


def initApp(app):
    app.teardown_appcontext(closeDb())
