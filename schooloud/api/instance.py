from schooloud.blueprints import instance
from schooloud.controller.InstanceController import InstanceController
from flask import request

instanceController = InstanceController()


@instance.route('/create', methods=['POST'])
def create_instance():
    params = request.get_json()
    response = instanceController.create_instance(params, request.cookies.get('email'))
    return response


@instance.route('/unpause', methods=['POST'])
def unpause_instance():
    params = request.get_json()
    response = instanceController.unpause_instance(params, request.cookies.get('email'))
    return response


@instance.route('/pause', methods=['POST'])
def pause_instance():
    params = request.get_json()
    response = instanceController.pause_instance(params, request.cookies.get('email'))
    return response


@instance.route('/delete', methods=['POST'])
def delete_instance():
    params = request.get_json()
    response = instanceController.delete_instance(params, request.cookies.get('email'))
    return response


@instance.route('/reboot', methods=['POST'])
def reboot_instance():
    params = request.get_json()
    response = instanceController.reboot_instance(params, request.cookies.get('email'))
    return response


@instance.route('/list')
def get_instance_list():

    return


@instance.route('/detail')
def get_instance_detail():

    return
