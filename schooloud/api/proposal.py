from sqlalchemy.exc import NoResultFound

from schooloud.blueprints import proposal
from schooloud.controller.ProposalController import ProposalController
from flask import request, abort, Response, jsonify

from schooloud.libs.decorator import session_authenticate

proposalController = ProposalController()


@proposal.route('/detail/<proposal_id>')
@session_authenticate
def get_proposal_detail(proposal_id, **kwargs):
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
def create_proposal(**kwargs):
    params = request.get_json()
    try:
        proposal_id = proposalController.set_proposal(params)
        return str(proposal_id)
    except Exception:
        return abort(404)


@proposal.route('/delete', methods=['POST'])
@session_authenticate
def delete_proposal(**kwargs):
    params = request.get_json()
    response = ''
    try:
        response = proposalController.delete_proposal(params, kwargs['email'])
    except Exception:
        pass

    return response


@proposal.route('/list')
@session_authenticate
def get_proposal_list(**kwargs):
    params = request.get_json()
    response = ''
    response_code = 200
    try:
        proposal_list = proposalController.get_proposal_list(params, kwargs['email'])
        response = {"proposals": proposal_list}
    except Exception:
        pass

    return response


@proposal.route('/approve', methods=['POST'])
@session_authenticate
def approve_proposal(**kwargs):
    params = request.get_json()
    response = ''
    response_code = 200
    try:
        response = proposalController.update_proposal_state(params)
    except Exception:
        pass
    return response
