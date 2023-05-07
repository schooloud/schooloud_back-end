from schooloud.libs.database import db


class Session(db.Model):
    __tablename__ = 'session'
    session_key = db.Column(db.String(32), primary_key=True)
    expired_at = db.Column(db.DateTime(), nullable=False)
    user_email = db.Column(db.String(50), db.ForeignKey("user.email"))

    __table_args__ = {'extend_existing': True}