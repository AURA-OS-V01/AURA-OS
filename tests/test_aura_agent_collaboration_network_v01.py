from core.intelligence.collaboration.aura_agent_collaboration_network_v01 import (

    AURAAgentCollaborationNetwork

)

def test_agent_collaboration_network():

    network = AURAAgentCollaborationNetwork()

    sales = network.register_agent(

        "Sales Agent",

        "sales"

    )

    research = network.register_agent(

        "Research Agent",

        "research"

    )

    message = network.communicate(

        sales["id"],

        research["id"],

        "Analyze enterprise opportunity"

    )

    task = network.assign_task(

        research["id"],

        "Research target market"

    )

    state = network.get_state()

    print(

        "AURA Agent Collaboration Network Test"

    )

    print(

        state

    )

    assert len(state["agents"]) == 2

    assert len(state["messages"]) == 1

    assert len(state["tasks"]) == 1

    assert task["status"] == "assigned"

if __name__ == "__main__":

    test_agent_collaboration_network()