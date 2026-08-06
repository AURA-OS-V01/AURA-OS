from core.agents.aura_agent_runtime_core_v01 import (

    AURAAgentRuntimeCore

)

def test_agent_runtime_core():

    runtime = AURAAgentRuntimeCore()

    agent = runtime.create_agent(

        "Sales Agent",

        "business development"

    )

    activated = runtime.activate_agent(

        agent["id"]

    )

    task = runtime.assign_task(

        agent["id"],

        "Find new customer opportunities"

    )

    print(

        "AURA Agent Runtime Core Test"

    )

    print(

        "-----------------------------"

    )

    print(activated)

    print(task)

    assert activated["state"] == (

        "active"

    )

    assert task["status"] == (

        "assigned"

    )

if __name__ == "__main__":

    test_agent_runtime_core()