from schooloud.blueprints import quota
from schooloud.controller.QuotaController import QuotaController
from flask import request, Response, abort

quotaController = QuotaController()


@quota.route('/usage')
def get_usage():
    return quotaController.current_usage()


@quota.route('/request', methods=['POST'])
def modify_request():
    return quotaController.create_request(request.get_json(), request.cookies.get('email'))


@quota.route('/approval', methods=['POST'])
def approve_request():
    return quotaController.update_quota_request_state(request.get_json())


@quota.route('/list')
def get_quota_request_list():
    return quotaController.get_quota_request_list(request.cookies.get('role'), request.cookies.get('email'))

@quota.route('/detail/<quota_request_id>')
def get_quota_request_detail(quota_request_id):
    return quotaController.get_quota_request(quota_request_id)
