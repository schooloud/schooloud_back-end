from schooloud.blueprints import proposal
from schooloud.controller.ProposalController import ProposalController
from flask import request

proposalController = ProposalController()


@proposal.route('/detail/<proposalId>')
def get_proposal_detail(proposalId):
    return proposalController.get_proposal(proposalId)


@proposal.route('/create', methods=['POST'])
def create_proposal():
    params = request.get_json()
    return proposalController.set_proposal(params['purpose'], params['name'], params['instanceNum'], params['cpu'],
                                           params['memory'], params['storage'], params['author_email'], params['endAt'])


@proposal.route('/list')
def get_proposal_list():
    params = request.get_json()
    return proposalController.get_proposal_list(params['user_email'])


@proposal.route('/approve', methods=['POST'])
def approve_proposal():
    params = request.get_json()
    return proposalController.update_proposal_state(params['proposalId'], params['isApproved'])
