from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config.dev.lsi import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from .model import proposal, student

    # blueprint
    from schooloud.api import hello, student
    app.register_blueprint(hello.bp)
    app.register_blueprint(student.bp)

    return app
