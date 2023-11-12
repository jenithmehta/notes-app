"""Create flask app and register blueprints"""
from flask import Flask
from website import config
from website.models import db
from website.auth import auth
from website.views import views


def create_app():
    """
    Creates flask application instance object

    :param debug: Set to true for development, defaults to True
    :type debug: bool, optional
    :return: flask app instance
    :rtype: _type_
    """
    app = Flask(__name__)
    if app.config["DEBUG"]:
        app.config.from_object(config.DevelopmentConfig)
    else:
        app.config.from_object(config.MainConfig)
    db.init_app(
        app
    )  # initialising, provides db related config associated with flask app to db extension.
    with app.app_context():
        db.create_all()
    app.register_blueprint(views)
    app.register_blueprint(auth, url_prefix="/auth")
    return app
