from schooloud.libs.database import db


class Session(db.Model):
    __tablename__ = 'session'
    sessionKey = db.Column(db.String(32), primary_key=True)
    expiredAt = db.Column(db.DateTime(),nullable=False)

    userEmail = db.Column(db.String(50), db.ForeignKey("user.email"))
    user = db.relationship("Session", back_populates="user")  # many-to-one 관계의 참조 변수