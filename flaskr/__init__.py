import os

from flask import Flask
from flaskr.dummy import dummy_backend
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

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

    app.json_encoder = LazyJSONEncoder

    # a simple page that says hello
    app.register_blueprint(dummy_backend)

    return app