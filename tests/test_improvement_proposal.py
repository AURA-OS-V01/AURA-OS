from core.evolution.proposals.proposal_system import (

    ImprovementProposalSystem

)

def test_proposal():

    system = ImprovementProposalSystem()

    proposal = system.create(

        "agent",

        "Finance Agent",

        "Improve forecasting workflow",

        "Low prediction accuracy",

        "medium"

    )

    pending = system.list_pending()

    print("Improvement Proposal Test")

    print("------------------------")

    print(proposal)

    print(pending)

if __name__ == "__main__":

    test_proposal()