import os
import asyncio

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO

from data_management import robotSetup

socketio = SocketIO(cors_allowed_origins="*")
roboto = robotSetup.Robot()


def create_app(test_config=None):
    # create and configure the app

    load_dotenv("data_management/../.env")

    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={r"/foo": {"origins": "*"}})
    socketio.init_app(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if __name__ == "__main__":
        app.run(host='0.0.0.0')
        socketio.run(app, host='0.0.0.0', cors_allowed_origins="*")

    from . import db
    from . import save
    from . import delete
    from . import get
    from . import streams
    from . import commands
    from . import export
    from . import robotSetup

    app.register_blueprint(save.bp)
    app.register_blueprint(delete.bp)
    app.register_blueprint(get.bp)
    app.register_blueprint(export.bp)

    @app.route('/')
    def index():
        # rendering webpage
        return render_template('index.html')

    return app
