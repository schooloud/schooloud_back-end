from schooloud.libs.database import db


class Instance(db.Model):
    __tablename__ = 'instance'
    instanceId = db.Column(db.String(32), primary_key=True)
    domain = db.Column(db.Text(100))
    port = db.Column(db.Integer)

    projectId = db.Column(db.String(32), db.ForeignKey("project.projectId"))
    project = db.relationship("Project", back_populates="instances")  # many-to-one 관계의 참조 변수

