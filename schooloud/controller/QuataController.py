from schooloud.model.quataRequest import QuataRequest


class QuataController:
    def __init__(self):
        pass

    def get_quataRequest(self, quataRequestId):
        quataRequest = QuataRequest.query.filter(QuataRequest.quataRequestId == quataRequestId).one()
        proposal_dict = {
            'author': quataRequest.author,
            'purpose': quataRequest.purpose,
            'memory': quataRequest.memory,
            'vCPU': quataRequest.vCPU,
            'storage': quataRequest.storage,
            'createdAt': quataRequest.createdAt,
            'status': quataRequest.status,
            'projectId': quataRequest.projectId
        }
        return proposal_dict
