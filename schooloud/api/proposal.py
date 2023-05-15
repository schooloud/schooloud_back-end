from sqlalchemy.exc import NoResultFound

from schooloud.blueprints import proposal
from schooloud.controller.ProposalController import ProposalController
from flask import request

from schooloud.libs.decorator import session_authenticate

proposalController = ProposalController()


@proposal.route('/detail/<proposal_id>')
@session_authenticate
def get_proposal_detail(proposal_id):
    response = ''
    response_code = 200
    try:
        response = proposalController.get_proposal(proposal_id)
    except NoResultFound:
        response_code = 400
        return {"status": response_code, "message": "there is no proposal matches"}
    return response


@proposal.route('/create', methods=['POST'])
@session_authenticate
def create_proposal():
    params = request.get_json()
    response = ''
    response_code = 200
    try:
        proposal_id = proposalController.set_proposal(params)
        response = str(proposal_id)
    except Exception:
        pass

    return response


@proposal.route('/delete', methods=['POST'])
@session_authenticate
def delete_proposal():
    params = request.get_json()
    response = ''
    try:
        response = proposalController.delete_proposal(params, request.cookies.get('email'))
    except Exception:
        pass

    return response


@proposal.route('/list')
@session_authenticate
def get_proposal_list():
    params = request.get_json()
    response = ''
    response_code = 200
    try:
        proposal_list = proposalController.get_proposal_list(params, request.cookies.get('email'))
        response = {"proposals": proposal_list}
    except Exception:
        pass

    return response


@proposal.route('/approve', methods=['POST'])
@session_authenticate
def approve_proposal():
    params = request.get_json()
    response = ''
    response_code = 200
    try:
        response = proposalController.update_proposal_state(params)
    except Exception:
        pass
    return response
