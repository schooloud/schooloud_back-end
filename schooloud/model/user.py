from schooloud import db


class User(db.Model):
    __tablename__ = 'user'
    email = db.Column(db.String(50), primary_key=True)
    studentId = db.Column(db.String(20))
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    major = db.Column(db.String(30))
    role = db.Column(db.String(20), nullable=False)

    proposals = db.relationship("Proposal", back_populates="author")
    session = db.relationship("Session", back_populates="user", uselist=False)
    quataRequests = db.relationship("QuataRequest", back_populates="author")
    projects = db.relationship("StudentInProject", back_populates="students")
