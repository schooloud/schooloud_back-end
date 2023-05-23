from schooloud.blueprints import project
from schooloud.controller.ProjectController import ProjectController
from flask import request, abort, Response

from schooloud.libs.decorator import session_authenticate

projectController = ProjectController()


@project.route('/create', methods=['POST'])
@session_authenticate
def create_project(**kwargs):
    try:
        project = projectController.create_project(request.get_json(), kwargs['email'])
        return Response("", status=200, mimetype="application/json")
    except:
        return abort(404)


@project.route('/add-member', methods=['POST'])
@session_authenticate
def add_member_to_project(**kwargs):
    try:
        student_in_project = projectController.add_member_to_project(request.get_json())
        return Response("", status=200)
    except:
        return abort(404)


@project.route('/list')
@session_authenticate
def project_list(**kwargs):
    # try:
    return projectController.project_list(kwargs['email'], kwargs['role'])
    # except:
    #     return abort(404)


@project.route('/detail/<project_id>')
@session_authenticate
def project_detail(project_id, **kwargs):
    try:
        return projectController.project_detail(project_id, kwargs['email'], kwargs['role'])
    except:
        return abort(404)
