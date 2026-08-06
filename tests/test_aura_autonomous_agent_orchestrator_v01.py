from core.agents.orchestration.aura_autonomous_agent_orchestrator_v01 import (

    AURAAnonymousAgentOrchestrator

)

def test_autonomous_agent_orchestrator():

    orchestrator = AURAAnonymousAgentOrchestrator()

    agent = orchestrator.register_agent(

        "sales_agent",

        [

            "research",

            "outreach"

        ]

    )

    operation = orchestrator.start_operation(

        "Acquire new business customers",

        [

            agent["agent_id"]

        ]

    )

    orchestrator.update_operation(

        operation["id"],

        "executing"

    )

    result = orchestrator.complete_operation(

        operation["id"]

    )

    print(

        "AURA Autonomous Agent Orchestrator Test"

    )

    print(

        "---------------------------------------"

    )

    print(agent)

    print(result)

    assert result["status"] == (

        "completed"

    )

    assert result["stage"] == (

        "completed"

    )

if __name__ == "__main__":

    test_autonomous_agent_orchestrator()
    