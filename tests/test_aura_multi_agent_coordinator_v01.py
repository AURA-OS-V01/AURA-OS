from core.agents.orchestration.aura_multi_agent_coordinator_v01 import (

    AURAMultiAgentCoordinator

)

def test_multi_agent_coordinator():

    coordinator = AURAMultiAgentCoordinator()

    sales_agent = coordinator.register_agent(

        "Sales Agent",

        "sales"

    )

    research_agent = coordinator.register_agent(

        "Research Agent",

        "market research"

    )

    team = coordinator.create_team(

        "Growth Team",

        [

            sales_agent["id"],

            research_agent["id"]

        ]

    )

    assignment = coordinator.delegate_task(

        team["id"],

        "Find new customer opportunities"

    )

    members = coordinator.get_team_agents(

        team["id"]

    )

    print(

        "AURA Multi-Agent Coordinator Test"

    )

    print(

        "----------------------------------"

    )

    print(team)

    print(assignment)

    print(members)

    assert len(members) == 2

    assert assignment["status"] == (

        "assigned"

    )

if __name__ == "__main__":

    test_multi_agent_coordinator()