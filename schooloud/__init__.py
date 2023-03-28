import os

from logging.config import fileConfig
from flask import Flask

app = Flask(__name__)
phase = ''


def init_app(app):
    global phase

    phase = os.getenv('SCHOOLOUD_ENV', 'DEV').lower()
    # export SCHOOLOUD_ENV=suin
    app.config.from_pyfile(f'../config/{phase}/config.cfg')
    logfile = app.config['LOG_CONFIG_PATH']
    with open(logfile % phase) as f:
        fileConfig(f)
