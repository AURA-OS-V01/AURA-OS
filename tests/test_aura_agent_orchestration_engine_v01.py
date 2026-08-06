from core.agents.aura_agent_orchestration_engine_v01 import (

    AURAAgentOrchestrationEngine

)

def test_agent_orchestration():

    system = AURAAgentOrchestrationEngine()

    result = system.assign_task(

        "Create startup launch plan",

        [

            "Research Agent",

            "Analysis Agent",

            "Writing Agent"

        ]

    )

    assert result["goal"] == "Create startup launch plan"

    assert len(result["assigned_agents"]) == 3

    print("AURA Agent Orchestration Engine Test")

    print("----------------------------------")

    print(result)

if __name__ == "__main__":

    test_agent_orchestration()