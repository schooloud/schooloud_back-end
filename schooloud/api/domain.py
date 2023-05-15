from schooloud.blueprints import domain
from schooloud.controller.DomainController import DomainController
from flask import request

domainController = DomainController()


@domain.route('/assign', methods=['POST'])
def assign_domain():
    params = request.get_json()
    response = domainController.assign_domain(params, request.cookies.get('email'))
    return response


@domain.route('/list')
def get_domain_list():
    response = domainController.get_domain_list(request.cookies.get('email'))
    return response

