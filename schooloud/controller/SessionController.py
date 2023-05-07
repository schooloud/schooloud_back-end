import random

from sqlalchemy.exc import NoResultFound

from schooloud.model.session import Session
from schooloud.libs.database import db
from schooloud.model.user import User


class SessionController:
    def __init__(self):
        pass

    def create_session_key(self, user_email, response):
        session = Session(user_email=user_email)
        db.session.add(session)
        db.session.commit()
        response.set_cookie('session_key', session.session_key)
        return response
