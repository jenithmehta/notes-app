"""Create flask app and register blueprints"""
from flask import Flask
from website.config import Config, DevelopmentConfig
from .views import views
from .auth import auth

def create_app(debug: bool=True):
    """
    Creates flask application instance object

    :param debug: Set to true for development, defaults to True
    :type debug: bool, optional
    :return: flask app instance
    :rtype: _type_
    """
    app = Flask(__name__)
    app.config.update(
        DEBUG=debug,
        SECRET_KEY=Config.SECRET_KEY,
    )
    app.register_blueprint(views)
    app.register_blueprint(auth,url_prefix="/auth")

    return app
