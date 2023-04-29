from schooloud.model.proposal import Proposal
from datetime import datetime
from schooloud.libs.database import db
from schooloud.model.user import User


class ProposalController:
    def __init__(self):
        pass

    def get_proposal(self, proposalId):
        proposal = Proposal.query.filter(Proposal.proposalId == proposalId).one()
        return proposal.as_dict()


    def set_proposal(self, purpose, projectName, instanceNum, cpu, memory, storage, author_email, endAt):
        proposal = Proposal(purpose=purpose, projectName=projectName, instanceNum=instanceNum, cpu=cpu, memory=memory,
                            storage=storage, status="WAIT", author_email=author_email, endAt=endAt)
        db.session.add(proposal)
        db.session.commit()
        return str(proposal.proposalId)


    def get_proposal_list(self, user_email):
        proposal_list = []
        user = User.query.filter(User.email == user_email).one()
        if user.role == 'ADMIN':
            proposals = Proposal.query.all()
        elif user.role == 'STUDENT':
            proposals = Proposal.query.filter(Proposal.author_email == user_email).all()
        elif user.role == 'PROFESSOR':   # for professor
            proposals = Proposal.query.all()
        for proposal in proposals:
            proposal_list.append(proposal.as_dict())
        return proposal_list

    def update_proposal_state(self, proposalId, isApproved):
        if isApproved:
            proposal = Proposal.query.filter(Proposal.proposalId == proposalId)
            proposal.update({"status": "APPROVED"})
            # 프로젝트 생성 함수 호출


        else:
            proposal = Proposal.query.filter(Proposal.proposalId == proposalId)
            proposal.update({"status": "REJECTED"})
        db.session.commit()
        return str(proposalId)