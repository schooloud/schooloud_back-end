from schooloud.blueprints import quota
from schooloud.controller.QuotaController import QuotaController
from flask import request, Response, abort

from schooloud.libs.decorator import session_authenticate

quotaController = QuotaController()


@quota.route('/usage')
@session_authenticate
def get_usage(**kwargs):
    return quotaController.current_usage(request.get_json(), kwargs['email'], kwargs['role'])


@quota.route('/request', methods=['POST'])
def modify_request(**kwargs):
    return quotaController.create_request(request.get_json(), kwargs['email'])


@quota.route('/approval', methods=['POST'])
def approve_request(**kwargs):
    return quotaController.update_quota_request_state(request.get_json())


@quota.route('/list')
def get_quota_request_list(**kwargs):
    return quotaController.get_quota_request_list(kwargs['role'], kwargs['email'])


@quota.route('/detail/<quota_request_id>')
def get_quota_request_detail(quota_request_id, **kwargs):
    return quotaController.get_quota_request(quota_request_id)
