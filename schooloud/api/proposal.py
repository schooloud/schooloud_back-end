from schooloud.blueprints import proposal
from schooloud.controller.ProposalController import ProposalController


proposalController = ProposalController()

@proposal.route('/detail/<proposalId>')
### 없는 proposalId를 요청한 경우 에러 처리 필요
def get_proposal_detail(proposalId):
    return proposalController.get_proposal(proposalId)

@proposal.route('/create')
### 데이터베이스에 값 추가될때마다 자동으로 id값 업데이트 필요
def create_proposal():
    proposalController.set_proposal("test", "projecttt", 2, 3, 4, 4, "WAIT", "asdf")
