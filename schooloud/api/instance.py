from schooloud.blueprints import instance
from schooloud.controller.InstanceController import InstanceController
from schooloud.libs.decorator import session_authenticate
from flask import request

instanceController = InstanceController()


@instance.route('/create', methods=['POST'])
@session_authenticate
def create_instance(**kwargs):
    params = request.get_json()
    response = instanceController.create_instance(params, kwargs['email'])
    return response


@instance.route('/unpause', methods=['POST'])
@session_authenticate
def unpause_instance(**kwargs):
    params = request.get_json()
    response = instanceController.unpause_instance(params, kwargs['email'])
    return response


@instance.route('/pause', methods=['POST'])
@session_authenticate
def pause_instance(**kwargs):
    params = request.get_json()
    response = instanceController.pause_instance(params, kwargs['email'])
    return response


@instance.route('/delete', methods=['POST'])
@session_authenticate
def delete_instance(**kwargs):
    params = request.get_json()
    response = instanceController.delete_instance(params, kwargs['email'])
    return response


@instance.route('/reboot', methods=['POST'])
@session_authenticate
def reboot_instance(**kwargs):
    params = request.get_json()
    response = instanceController.reboot_instance(params, kwargs['email'])
    return response


@instance.route('/list')
@session_authenticate
def get_instance_list(**kwargs):
    params = request.get_json()
    response = instanceController.get_instance_list(params, kwargs['email'])
    return response


@instance.route('/detail')
@session_authenticate
def get_instance_detail(**kwargs):
    params = request.get_json()
    response = instanceController.get_instance_detail(params, kwargs['email'])
    return response
