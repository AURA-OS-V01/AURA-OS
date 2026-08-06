from core.agents.aura_dynamic_agent_routing_engine_v01 import (

    AURADynamicAgentRoutingEngine

)

def test_dynamic_routing():

    system = AURADynamicAgentRoutingEngine()

    result = system.analyze_request(

        "Research AI trends and create a coding prototype"

    )

    print("AURA Dynamic Agent Routing Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_dynamic_routing()