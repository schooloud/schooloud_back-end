import openstack
from schooloud.model.user import User
from schooloud.model.project import Project
from schooloud.model.studentInProject import StudentInProject


class OpenStackController:
    def __init__(self):
        pass

    def create_admin_connection(self):
        return openstack.connect(
            auth_url="http://211.37.146.151/identity",
            username="admin",
            password="vp2smsehsRktmfh!!",
            project_id="008f771ca9564acaae66fc110e964f75",
            project_name="admin",
            user_domain_name="Default",
            project_domain_name="default",
            region_name="RegionOne",
            interface="public",
            identity_api_version=3
        )

    def create_connection(self, email):
        # Find user and project for connection
        user = User.query.filter(User.email == email).one()
        project = Project.query.filter(Project.project_id == StudentInProject.query.filter(
            StudentInProject.student_email == email).one().project_id).all()[0]
        # return connection
        return openstack.connect(
            auth_url="http://211.37.146.151/identity",
            username=user.email,
            password=user.password,
            project_id=project.project_id,
            project_name=project.project_name,
            user_domain_name="Default",
            project_domain_name="default",
            region_name="RegionOne",
            interface="public",
            identity_api_version=3
        )

    def create_connection_with_project_id(self, email, project_id):
        user = User.query.filter(User.email == email).one()
        project = Project.query.filter(Project.project_id == project_id).one()
        return openstack.connect(
            auth_url="http://211.37.146.151/identity",
            username=user.email,
            password=user.password,
            project_id=project.project_id,
            project_name=project.project_name,
            user_domain_name="Default",
            project_domain_name="default",
            region_name="RegionOne",
            interface="public",
            identity_api_version=3
        )

    def create_connection_with_project_id_lower_version(self, email, project_id):
        user = User.query.filter(User.email == email).one()
        project = Project.query.filter(Project.project_id == project_id).one()
        return openstack.connect(
            auth_url="http://211.37.146.151/identity",
            username=user.email,
            password=user.password,
            project_id=project.project_id,
            project_name=project.project_name,
            user_domain_name="Default",
            project_domain_name="default",
            region_name="RegionOne",
            interface="public",
            identity_api_version=3,
            compute_api_version=2.27
        )