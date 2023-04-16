from schooloud.libs.database import db


class StudentInProject(db.Model):
    __tablename__ = 'studentInProject'
    id = db.Column(db.Integer, primary_key=True)
    # studentEmail = db.Column(db.String(50), db.ForeignKey("user.email"))
    # students = db.relationship("User", back_populates="projects")
    #
    # projectId = db.Column(db.String(32), db.ForeignKey("project.projectId"))
    # projects = db.relationship("Project", back_populates="students")  # many-to-one 관계의 참조 변수

    __table_args__ = {'extend_existing': True}