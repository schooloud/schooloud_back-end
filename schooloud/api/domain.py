from schooloud.blueprints import domain
from schooloud.controller.DomainController import DomainController
from schooloud.libs.decorator import session_authenticate
from flask import request

domainController = DomainController()


@domain.route('/assign', methods=['POST'])
@session_authenticate
def assign_domain():
    params = request.get_json()
    response = domainController.assign_domain(params, request.cookies.get('email'))
    return response


@domain.route('/list')
@session_authenticate
def get_domain_list():
    response = domainController.get_domain_list(request.cookies.get('email'))
    return response

