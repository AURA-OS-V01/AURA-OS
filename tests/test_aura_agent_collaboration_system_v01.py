from core.agents.aura_agent_collaboration_system_v01 import (

    AURAAgentCollaborationSystem

)

def test_agent_collaboration():

    system = AURAAgentCollaborationSystem()

    lead_agent = system.register_agent(

        "Lead Intelligence Agent",

        "growth"

    )

    sales_agent = system.register_agent(

        "Sales Agent",

        "sales"

    )

    message = system.send_message(

        lead_agent["name"],

        sales_agent["name"],

        "Found a high-value logistics opportunity."

    )

    request = system.create_agent_request(

        sales_agent["name"],

        "Outreach Agent",

        "Prepare client introduction message."

    )

    updated = system.update_request_status(

        request["id"],

        "completed"

    )

    print(

        "AURA Agent Collaboration System Test"

    )

    print(

        "-----------------------------------"

    )

    print(message)

    print(updated)

    assert message["sender"] == (

        "Lead Intelligence Agent"

    )

    assert updated["status"] == (

        "completed"

    )

if __name__ == "__main__":

    test_agent_collaboration()