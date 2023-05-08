from schooloud.blueprints import flavor
from schooloud.controller.FlavorController import FlavorController
from flask import request

flavorController = FlavorController()


@flavor.route('/list')
def get_flavor_list():
    response = flavorController.get_flavor_list(request.cookies.get('email'))
    return response
