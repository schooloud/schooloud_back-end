from datetime import datetime, timedelta

from sqlalchemy.exc import NoResultFound

from schooloud.model.session import Session
from schooloud.libs.database import db


class SessionController:
    def __init__(self):
        pass

    def create_session_key(self, user_email, response):
        # if session already exists, update expired time
        session = Session.query.filter(Session.user_email == user_email)
        if db.session.query(session.exists()).scalar():
            session = Session.query.filter(Session.user_email == user_email).one()
            session.expired_at = datetime.now() + timedelta(days=1)
        # if there is no valid session, create session
        else:
            session = Session(user_email=user_email)
            db.session.add(session)

        db.session.commit()
        response.set_cookie('session_key', session.session_key)
        response.set_cookie('expired_at', datetime.strftime(session.expired_at, "%Y-%m-%d"))
        return response

    def delete_session(self, session_key):
        Session.query.filter(Session.session_key == session_key).delete()
        db.session.commit()
        return
