from core.business.orchestrator.aura_enterprise_automation_orchestrator_v01 import (

    AURAEnterpriseAutomationOrchestrator

)

def test_enterprise_orchestrator():

    orchestrator = AURAEnterpriseAutomationOrchestrator()

    agent = orchestrator.register_agent(

        "Sales Intelligence Agent",

        "sales"

    )

    task = orchestrator.create_task(

        "Analyze new customer opportunity",

        agent["category"]

    )

    execution = orchestrator.execute_task(

        task["id"]

    )

    state = orchestrator.get_system_state()

    print(

        "AURA Enterprise Automation Orchestrator Test"

    )

    print(

        "-------------------------------------------"

    )

    print(state)

    assert agent["status"] == (

        "available"

    )

    assert task["status"] == (

        "completed"

    )

    assert execution["result"] == (

        "success"

    )

if __name__ == "__main__":

    test_enterprise_orchestrator()