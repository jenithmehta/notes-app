""" This module is for importing config from .env file """
from os import environ
from dotenv import load_dotenv

load_dotenv()


class MainConfig:
    """Main Config"""

    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    DEBUG = False
    PORT = environ.get("PORT")


class DevelopmentConfig(MainConfig):
    """Development Config"""

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    DEBUG = True
