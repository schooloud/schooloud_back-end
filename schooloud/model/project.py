from schooloud.libs.database import db


class Project(db.Model):
    __tablename__ = 'project'
    projectId = db.Column(db.String(32), primary_key=True)
    isDeleted = db.Column(db.Boolean, nullable=False)
    projectName = db.Column(db.String(30), nullable=False)
    cpu = db.Column(db.Integer, nullable=False)
    memory = db.Column(db.Integer, nullable=False)
    storage = db.Column(db.Integer, nullable=False)
    createAt = db.Column(db.DateTime(), nullable=False)
    endAt = db.Column(db.DateTime(), nullable=False)

    # instances = db.relationship("Instance", back_populates="project")
    # quataRequests = db.relationship("QuataRequest", back_populates="project")
    # students = db.relationship("StudentInProject", back_populates="projects")

    __table_args__ = {'extend_existing': True}