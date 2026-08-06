from core.business.agents_marketplace.aura_enterprise_agent_marketplace_v01 import (

    AURAEnterpriseAgentMarketplace

)

def test_agent_marketplace():

    marketplace = AURAEnterpriseAgentMarketplace()

    agent = marketplace.create_agent_template(

        "Sales Intelligence Agent",

        "sales",

        [

            "lead_analysis",

            "outreach",

            "forecasting"

        ]

    )

    found = marketplace.find_agents(

        "sales"

    )

    deployment = marketplace.deploy_agent(

        agent["id"],

        "aura_demo_company"

    )

    data = marketplace.get_marketplace()

    print(

        "AURA Enterprise Agent Marketplace Test"

    )

    print(

        "--------------------------------------"

    )

    print(data)

    assert len(found) == 1

    assert deployment["status"] == (

        "active"

    )

if __name__ == "__main__":

    test_agent_marketplace()