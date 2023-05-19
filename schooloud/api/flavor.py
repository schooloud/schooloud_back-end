from schooloud.blueprints import flavor
from schooloud.controller.FlavorController import FlavorController
from schooloud.libs.decorator import session_authenticate
from flask import request

flavorController = FlavorController()


@flavor.route('/list')
@session_authenticate
def get_flavor_list(**kwargs):
    response = flavorController.get_flavor_list(kwargs['email'])
    return response
