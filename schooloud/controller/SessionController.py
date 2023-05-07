from datetime import datetime
from schooloud.model.session import Session
from schooloud.libs.database import db


class SessionController:
    def __init__(self):
        pass

    def create_session_key(self, user_email, response):
        session = Session(user_email=user_email)
        db.session.add(session)
        db.session.commit()
        response.set_cookie('session_key', session.session_key)
        response.set_cookie('expired_at', datetime.strftime(session.expired_at, "%Y-%m-%d"))
        return response
