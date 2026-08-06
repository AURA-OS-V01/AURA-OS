from core.business.contracts.aura_proposal_contract_intelligence_v01 import (

    AURAProposalContractIntelligence

)

def test_proposal_contract_intelligence():

    intelligence = AURAProposalContractIntelligence()

    proposal = intelligence.create_proposal(

        "Technology Company",

        "AI Automation Platform",

        50000

    )

    submitted = intelligence.submit_proposal(

        proposal["id"]

    )

    contract = intelligence.create_contract(

        proposal["id"],

        "Technology Company"

    )

    completed = intelligence.complete_contract(

        contract["id"]

    )

    pipeline = intelligence.get_deal_pipeline()

    print(

        "AURA Proposal Contract Intelligence Test"

    )

    print(

        "---------------------------------------"

    )

    print(pipeline)

    assert submitted["status"] == (

        "submitted"

    )

    assert completed["status"] == (

        "completed"

    )

    assert len(

        pipeline["contracts"]

    ) == 1

if __name__ == "__main__":

    test_proposal_contract_intelligence()