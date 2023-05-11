import datetime

from sqlalchemy.exc import NoResultFound
from schooloud.libs.database import db

from schooloud.model.project import Project

from schooloud.controller.OpenStackController import OpenStackController
from schooloud.model.proposal import Proposal
from schooloud.model.studentInProject import StudentInProject
from flask import jsonify, abort
from schooloud.model.user import User

openstack_controller = OpenStackController()


class ProjectController:
    def __init__(self):
        pass

    def get_project(self, project_id):
        project = Project.query.filter(Project.project_id == project_id).one()
        project_dict = {
            'is_deleted': project.is_deleted,
            'name': project.project_name,
            'cpu': project.cpu,
            'memory': project.memory,
            'storage': project.storage,
            'create_at': project.create_at,
            'end_at': project.end_at,
        }
        return project_dict

    # 제안서 승인 시 호출
    def create_project(self, params, email):
        # Get a proposal from relevant proposal
        proposal = Proposal.query.filter(Proposal.proposal_id == params['proposal_id']).one()
        # Create project on openstack
        conn = openstack_controller.create_admin_connection()
        created_project = conn.create_project(name=proposal.project_name, domain_id="default")
        # Get role and Add current user to created project
        user_id = conn.get_user(name_or_id=email).id
        role_id = conn.get_role(name_or_id="member").id
        conn.identity.assign_project_role_to_user(project=created_project.id, user=user_id, role=role_id)

        # Create project on backend server
        project = Project(
            project_id=created_project.id,
            project_name=proposal.project_name,
            is_deleted=False,
            cpu=proposal.cpu,
            memory=proposal.memory,
            storage=proposal.storage,
            create_at=datetime.datetime.now(),
            end_at=proposal.end_at
        )
        db.session.add(project)
        student_in_project = StudentInProject(
            student_email=email,
            project_id=project.project_id
        )
        db.session.add(student_in_project)
        db.session.commit()

        conn = openstack_controller.create_connection_with_project_id(email=email, project_id=project.project_id)

        # Create private network (with admin auth)
        private_net = conn.create_network(
            name="private"
        )

        # Update Security group Rule
        security_group = conn.get_security_group(name_or_id="default").id
        conn.create_security_group_rule(
            secgroup_name_or_id=security_group
        )

        # Create subnet for private network
        subnet = conn.create_subnet(
            network_name_or_id=private_net.id,
            subnet_name='private-subnet',
            use_default_subnetpool=True,
        )

        # Create router to connect between public and private
        public_net = conn.get_network(
            name_or_id="public"
        )

        router = conn.create_router(
            name="public-private-router",
            ext_gateway_net_id=public_net.id
        )

        conn.add_router_interface(
            router=router.id,
            subnet_id=subnet.id
        )

        return project.project_id


    def add_member_to_project(self, params):
        project = params['project_id']
        member = params['email']

        # Get role, userid and Add member
        conn = openstack_controller.create_admin_connection()
        user_id = conn.get_user(name_or_id=member).id
        role = conn.get_role(name_or_id='member').id
        conn.identity.assign_project_role_to_user(project=project, user=user_id, role=role)

        # add member to student in project
        student_in_project = StudentInProject(
            student_email=member,
            project_id=project
        )
        db.session.add(student_in_project)
        db.session.commit()
        return student_in_project

    def project_list(self, email):
        user_projects = (
            StudentInProject.query.join(Project, StudentInProject.project_id == Project.project_id)
            .add_columns(Project.project_name)
            .filter(StudentInProject.student_email == email)
            .all()
        )
        projects = []
        for project in user_projects:
            projects.append(
                {
                    "project_id": project[0].project_id,
                    "project_name": project.project_name
                }
            )
        return jsonify({"projects": projects})

    def project_detail(self, project_id, email, role):
        # project에 연결된 email 이거나, role이 admin인 경우에만 동작
        try:
            # Get Project
            if role == "ADMIN":
                project = (
                    StudentInProject.query.filter(StudentInProject.project_id == project_id)
                    .join(Project, StudentInProject.project_id == Project.project_id)
                    .add_columns(Project.project_name, Project.create_at, Project.cpu, Project.memory, Project.storage,
                                 Project.end_at)
                    .one()
                )
            else:
                project = (
                    StudentInProject.query.filter(StudentInProject.student_email == email)
                    .filter(StudentInProject.project_id == project_id)
                    .join(Project, StudentInProject.project_id == Project.project_id)
                    .add_columns(Project.project_name, Project.create_at, Project.cpu, Project.memory, Project.storage,
                                 Project.end_at)
                    .one()
                )
            # Get current instance number on openstack
            conn = openstack_controller.create_connection_with_project_id(email, project_id)
            instance_num = len(conn.list_servers())
            # Get members
            students = (
                StudentInProject.query.filter(StudentInProject.project_id == project_id)
                .join(User, StudentInProject.student_email == User.email)
                .add_columns(User.name)
                .all()
            )
            members = []

            for student in students:
                members.append(
                    {
                        "name": student.name,
                        "email": student[0].student_email
                    }
                )
        except NoResultFound:
            return abort(400)

        return jsonify({
            "name": project.project_name,
            "create_at": project.create_at,
            "instance_num": instance_num,
            "cpu": project.cpu,
            "memory": project.memory,
            "storage": project.storage,
            "end_at": project.end_at,
            "members": members
        })
