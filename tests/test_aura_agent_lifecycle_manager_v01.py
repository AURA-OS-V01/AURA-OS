from core.agents.aura_agent_lifecycle_manager_v01 import (

    AURAAgentLifecycleManager

)

def test_agent_lifecycle_manager():

    manager = AURAAgentLifecycleManager()

    manager.register_agent(

        "Research Agent",

        "Information gathering"

    )

    registered = manager.get_agent(

        "Research Agent"

    ).copy()

    manager.activate_agent(

        "Research Agent"

    )

    active = manager.get_agent(

        "Research Agent"

    ).copy()

    manager.pause_agent(

        "Research Agent"

    )

    paused = manager.get_agent(

        "Research Agent"

    ).copy()

    manager.retire_agent(

        "Research Agent"

    )

    retired = manager.get_agent(

        "Research Agent"

    ).copy()

    state = manager.get_state()

    assert registered["state"] == "registered"

    assert active["state"] == "active"

    assert paused["state"] == "paused"

    assert retired["state"] == "retired"

    assert state["total_agents"] == 1

if __name__ == "__main__":

    test_agent_lifecycle_manager()