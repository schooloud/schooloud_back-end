from schooloud.blueprints import proposal
from schooloud.controller.ProposalController import ProposalController
from flask import request

proposalController = ProposalController()


@proposal.route('/detail/<proposalId>')
### 없는 proposalId를 요청한 경우 에러 처리 필요
def get_proposal_detail(proposalId):
    return proposalController.get_proposal(proposalId)


@proposal.route('/create', methods=['POST'])
def create_proposal():
    params = request.get_json()
    return proposalController.set_proposal(params['purpose'], params['name'], params['instanceNum'], params['cpu'],
                                           params['memory'], params['storage'], params['author_email'], params['endAt'])


@proposal.route('/approve')
def approve_proposal():
    params = request.get_json()


@proposal.route('/list')
def get_proposal_list():
    params = request.get_json()
    return proposalController.get_proposal_list(params['user_email'])


@proposal.route('/approve')
def approve_proposal():
    params = request.get_json()
    return proposalController.get_proposal_list(params['user_email'])
