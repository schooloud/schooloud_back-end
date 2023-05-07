from functools import wraps
from flask import request
from schooloud.libs.database import db
from datetime import datetime
from schooloud.model.session import Session
from sqlalchemy.exc import NoResultFound


def session_authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            session_key = request.cookies.get('session_key')
            session = Session.query.filter(Session.session_key == session_key).one()
            if datetime.now() > session.expired_at:
                return {"message": "session expired"}, 401
        except NoResultFound:
            return {"message": "invalid session"}, 401
        return f(*args, **kwargs)

    return decorated_function
