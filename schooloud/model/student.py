from schooloud import db


class Student(db.Model):

    sid = db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    major = db.Column(db.String(30), nullable=False)
