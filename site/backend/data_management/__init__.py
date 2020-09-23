import os
import asyncio

from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*")


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
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
        socketio.run(app)

    from . import db
    from . import save
    from . import delete
    from . import get
    from . import streams

    app.register_blueprint(save.bp)
    app.register_blueprint(delete.bp)
    app.register_blueprint(get.bp)

    @app.route('/')
    def index():
        # rendering webpage
        return render_template('index.html')

    return app
