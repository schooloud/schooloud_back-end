from schooloud.blueprints import flavor
from schooloud.controller.FlavorController import FlavorController
from schooloud.libs.decorator import session_authenticate
from flask import request

flavorController = FlavorController()


@flavor.route('/list')
@session_authenticate
def get_flavor_list():
    response = flavorController.get_flavor_list(request.cookies.get('email'))
    return response
