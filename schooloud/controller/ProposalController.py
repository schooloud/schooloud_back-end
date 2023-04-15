from schooloud.model.proposal import Proposal


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
            'createdAt': proposal.createdAt,
            'endAt': proposal.endAt,
            'author': proposal.author
        }
        return proposal_dict
