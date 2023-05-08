from schooloud.blueprints import instance
from schooloud.controller.InstanceController import InstanceController
from flask import request

instanceController = InstanceController()


@instance.route('/create', methods=['POST'])
def create_instance():
    params = request.get_json()
    response = instanceController.create_instance(params, request.cookies.get('email'))
    return response


@instance.route('/unpause')
def unpause_instance():

    return


@instance.route('/pause')
def pause_instance():

    return


@instance.route('/delete')
def delete_instance():

    return


@instance.route('/reboot')
def reboot_instance():

    return


@instance.route('/list')
def get_instance_list():

    return


@instance.route('/detail')
def get_instance_detail():

    return
