from core.runtime.aura_agent_management_bridge_v01 import (

    AURAAgentManagementBridge

)

from core.runtime.aura_module_registry_v01 import (

    AURAModuleRegistry

)

from core.agents.aura_agent_lifecycle_manager_v01 import (

    AURAAgentLifecycleManager

)

def test_agent_management_bridge():

    registry = AURAModuleRegistry()

    lifecycle = AURAAgentLifecycleManager()

    bridge = AURAAgentManagementBridge(

        registry,

        lifecycle

    )

    result = bridge.add_agent(

        "Research Agent",

        "Knowledge discovery"

    )

    active = bridge.activate_agent(

        "Research Agent"

    )

    status = bridge.get_agent_status(

        "Research Agent"

    )

    assert result["module"]["name"] == "Research Agent"

    assert result["agent"]["name"] == "Research Agent"

    assert active["state"] == "active"

    assert status["agent"]["state"] == "active"

    assert status["module"]["status"] == "registered"

if __name__ == "__main__":

    test_agent_management_bridge()