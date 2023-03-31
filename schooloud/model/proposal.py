from schooloud import db


class Proposal(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    instanceNum = db.Column(db.Integer, nullable=False)
    cpu = db.Column(db.Integer, nullable=False)
    memory = db.Column(db.Integer, nullable=False)
    storage = db.Column(db.Integer, nullable=False)
    purpose = db.Column(db.Text(), nullable=False)
    endAt = db.Column(db.DateTime(), nullable=False)
    createAt = db.Column(db.DateTime(), nullable=False)
    author_id = db.Column(db.String(), db.ForeignKey('student.sid', ondelete='CASCADE'))
    author = db.relationship('Student', backref=db.backref('author'))

