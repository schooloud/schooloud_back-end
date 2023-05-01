from sqlalchemy.exc import NoResultFound

from schooloud.model.proposal import Proposal
from schooloud.libs.database import db
from schooloud.model.user import User


class ProposalController:
    def __init__(self):
        pass

    def get_proposal(self, proposal_id):
        proposal = Proposal.query.filter(Proposal.proposal_id == proposal_id).one()
        return proposal.as_dict()


    def set_proposal(self, request_data):
        purpose = request_data['purpose']
        project_name = request_data['name']
        instance_num = request_data['instance_num']
        cpu = request_data['cpu']
        memory = request_data['memory']
        storage = request_data['storage']
        author_email = request_data['author_email']
        end_at = request_data['end_at']

        proposal = Proposal(purpose=purpose, project_name=project_name, instance_num=instance_num, cpu=cpu,
                            memory=memory, storage=storage, status="WAIT", author_email=author_email, end_at=end_at)
        db.session.add(proposal)
        db.session.commit()
        return proposal.proposal_id

    def get_proposal_list(self, request_data):
        user_email = request_data['user_email']
        proposal_list = []

        user = User.query.filter(User.email == user_email).one()
        if user.role == 'ADMIN':
            proposals = Proposal.query.all()
        elif user.role == 'STUDENT':
            proposals = Proposal.query.filter(Proposal.author_email == user_email).all()
        elif user.role == 'PROFESSOR':  # for professor
            proposals = Proposal.query.all()
        for proposal in proposals:
            proposal_list.append(proposal.as_dict())
        return proposal_list

    def update_proposal_state(self, request_data):
        proposal_id = request_data['proposal_id']
        is_approved = request_data['is_approved']

        if is_approved:
            proposal = Proposal.query.filter(Proposal.proposal_id == proposal_id)
            proposal.update({"status": "APPROVED"})
            # 프로젝트 생성 함수 호출


        else:
            proposal = Proposal.query.filter(Proposal.proposal_id == proposal_id)
            proposal.update({"status": "REJECTED"})
        db.session.commit()
        return proposal_id
