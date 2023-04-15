from schooloud import db


class QuataRequest(db.Model):
    __tablename__ = 'quataRequest'
    quataRequestId = db.Column(db.Integer, primary_key=True)

    author = db.relationship('User', backref=db.backref('quataRequests'))
    author_email = db.Column(db.String(50), db.ForeignKey('user.email', ondelete='CASCADE'))

    purpose = db.Column(db.Text(200), nullable=False)
    memory = db.Column(db.Integer, nullable=False)
    cpu = db.Column(db.Integer, nullable=False)
    storage = db.Column(db.Integer, nullable=False)
    createAt = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    projectId = db.Column(db.String(32), db.ForeignKey("project.projectId"))
    project = db.relationship("Project", back_populates="quataRequests")  # many-to-one 관계의 참조 변수

