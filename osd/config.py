import os
from builtins import object

class Config(object):
    PROJECT = "osd"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SECRET_KEY = "s3cr3t_lol"

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
