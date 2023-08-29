from flask import Flask
from website.config import Config, DevelopmentConfig

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
    return app