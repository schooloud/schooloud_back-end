from schooloud.model.quotaRequest import QuotaRequest
from schooloud.controller.OpenStackController import OpenStackController

openstackController = OpenStackController()

class QuotaController:
    def __init__(self):
        pass

    def get_quotaRequest(self, quota_request_id):
        quota_request = QuotaRequest.query.filter(QuotaRequest.quota_request_id == quota_request_id).one()
        proposal_dict = {
            'author': quota_request.author,
            'purpose': quota_request.purpose,
            'memory': quota_request.memory,
            'vCPU': quota_request.vCPU,
            'storage': quota_request.storage,
            'createdAt': quota_request.createdAt,
            'status': quota_request.status,
            'projectId': quota_request.projectId
        }
        return proposal_dict

    def current_usage(self):
        conn = openstackController.create_admin_connection()
        compute = conn.get_compute_quotas()
        return
