from sqlalchemy.exc import NoResultFound

from schooloud.model.proposal import Proposal
from schooloud.libs.database import db
from schooloud.model.user import User


class ProposalController:
    def __init__(self):
        pass

    def get_proposal(self, proposal_id):
        try:
            proposal = Proposal.query.filter(Proposal.proposal_id == proposal_id).one()
            return proposal.as_dict()
        except NoResultFound:
            return "there is no proposal matches"

    def set_proposal(self, purpose, project_name, instance_num, cpu, memory, storage, author_email, end_at):

        proposal = Proposal(purpose=purpose, project_name=project_name, instance_num=instance_num, cpu=cpu, memory=memory,
                            storage=storage, status="WAIT", author_email=author_email, end_at=end_at)
        db.session.add(proposal)
        db.session.commit()
        return str(proposal.proposal_id)

    def get_proposal_list(self, user_email):
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

    def update_proposal_state(self, proposal_id, is_approved):
        if is_approved:
            proposal = Proposal.query.filter(Proposal.proposal_id == proposal_id)
            proposal.update({"status": "APPROVED"})
            # 프로젝트 생성 함수 호출


        else:
            proposal = Proposal.query.filter(Proposal.proposal_id == proposal_id)
            proposal.update({"status": "REJECTED"})
        db.session.commit()
        return str(proposal_id)
