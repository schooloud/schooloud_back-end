import os
from glob import glob
from importlib import import_module
from importlib.util import find_spec as importlib_find

from flask import Flask
from flask_migrate import Migrate

from schooloud.blueprints import all_blueprints
from schooloud.libs.database import db


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    phase = os.getenv('SCHOOLOUD_ENV', 'dev/dev').lower()
    app.config.from_pyfile('../config/%s/config.cfg' % phase)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprint
    for bp in all_blueprints:
        path_name = importlib_find(bp.import_name)
        import_module(path_name.name)
        app.register_blueprint(bp, url_prefix=bp.url_prefix)

    return app
