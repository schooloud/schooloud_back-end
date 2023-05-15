from schooloud.libs.database import db


class QuotaRequest(db.Model):
    __tablename__ = 'quotaRequest'
    quota_request_id = db.Column(db.Integer, primary_key=True)

    # author = db.relationship('User', backref=db.backref('quotaRequests'))
    # author_email = db.Column(db.String(50), db.ForeignKey('user.email', ondelete='CASCADE'))

    purpose = db.Column(db.Text(200), nullable=False)
    memory = db.Column(db.Integer, nullable=False)
    cpu = db.Column(db.Integer, nullable=False)
    storage = db.Column(db.Integer, nullable=False)
    create_at = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    # projectId = db.Column(db.String(32), db.ForeignKey("project.projectId"))
    # project = db.relationship("Project", back_populates="quotaRequests")  # many-to-one 관계의 참조 변수

    __table_args__ = {'extend_existing': True}