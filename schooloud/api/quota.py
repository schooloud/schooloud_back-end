from schooloud.blueprints import quota
from schooloud.controller.QuotaController import QuotaController
from flask import request, Response, abort

quotaController = QuotaController()

@quota.route('/usage')
def get_usage():
    return

@quota.route('/request')
def modify_request():
    return

@quota.route('/approval')
def approve_request():
    return

@quota.route('/usage')
def get_usage():
    return