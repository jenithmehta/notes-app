""" This module is for importing config from .env file """
from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Main Config
    """
    SECRET_KEY = environ.get("SECRET_KEY")
    DEBUG = False

class DevelopmentConfig:
    """Development Config
    """
    DEBUG = True
    