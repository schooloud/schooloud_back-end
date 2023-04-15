from schooloud import db


class Proposal(db.Model):
    __tablename__ = 'proposal'
    proposalId = db.Column(db.Integer, primary_key=True)
    purpose = db.Column(db.Text(200), nullable=False)
    projectName = db.Column(db.String(30), nullable=False)
    createAt = db.Column(db.DateTime(), nullable=False)
    instanceNum = db.Column(db.Integer, nullable=False)
    cpu = db.Column(db.Integer, nullable=False)
    memory = db.Column(db.Integer, nullable=False)
    storage = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    endAt = db.Column(db.DateTime(), nullable=False)

    author = db.relationship('User', backref=db.backref('proposals'))
    author_email = db.Column(db.String(50), db.ForeignKey('user.email', ondelete='CASCADE'))

