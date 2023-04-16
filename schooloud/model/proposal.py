from schooloud.libs.database import db
from datetime import datetime


class Proposal(db.Model):
    __tablename__ = 'proposal'
    proposalId = db.Column(db.Integer, primary_key=True)
    purpose = db.Column(db.Text(200), nullable=False)
    projectName = db.Column(db.String(30), nullable=False)
    createAt = db.Column(db.DateTime())
    instanceNum = db.Column(db.Integer, nullable=False)
    cpu = db.Column(db.Integer, nullable=False)
    memory = db.Column(db.Integer, nullable=False)
    storage = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    endAt = db.Column(db.DateTime())

    author = db.Column(db.String(50))
    # author = db.relationship('User', backref=db.backref('proposals'))
    # author_email = db.Column(db.String(50), db.ForeignKey('user.email', ondelete='CASCADE'))

    __table_args__ = {'extend_existing': True}

    def __init__(self, purpose, projectName, instanceNum, cpu, memory, storage, status, author):
        self.proposalId = 5 # 자동으로 +1 되도록 수정 필요
        self.purpose = purpose
        self.projectName = projectName
        self.instanceNum = instanceNum
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.status = status
        self.author = author
        self.createAt = datetime.now()
        self.endAt = datetime.now()
