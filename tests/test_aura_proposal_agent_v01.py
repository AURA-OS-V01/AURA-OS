from core.growth.proposal_agent_v01 import (

    AURAProposalAgent

)

def test_proposal_agent():

    agent = AURAProposalAgent()

    result = agent.create_proposal(

        "Example Logistics",

        "Slow customer response times",

        "AI customer support automation",

        "Business Automation Package"

    )

    print("AURA Proposal Agent Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_proposal_agent()