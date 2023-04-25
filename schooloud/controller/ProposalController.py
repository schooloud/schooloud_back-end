from schooloud.model.proposal import Proposal
from datetime import datetime
from schooloud.libs.database import db

class ProposalController:
    def __init__(self):
        pass

    def get_proposal(self, proposalId):
        proposal = Proposal.query.filter(Proposal.proposalId == proposalId).one()
        proposal_dict = {
            'purpose': proposal.purpose,
            'projectName': proposal.projectName,
            'instanceNum': proposal.instanceNum,
            'cpu': proposal.cpu,
            'memory': proposal.memory,
            'storage': proposal.storage,
            'status': proposal.status,
            'createdAt': proposal.createAt.strftime('%Y-%m-%d %H:%M:%S'),
            'endAt': proposal.endAt.strftime('%Y-%m-%d %H:%M:%S'),
            'author_email': proposal.author_email
        }
        return proposal_dict

    def set_proposal(self, purpose, projectName, instanceNum, cpu, memory, storage, author_email, endAt):
        proposal = Proposal(purpose=purpose, projectName=projectName, instanceNum=instanceNum, cpu=cpu, memory=memory,
                            storage=storage, status="WAIT", author_email=author_email, endAt=endAt)
        db.session.add(proposal)
        db.session.commit()
        return str(proposal.proposalId)