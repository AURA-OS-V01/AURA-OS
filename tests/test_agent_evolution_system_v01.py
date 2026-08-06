from core.learning.agent_evolution_system_v01 import (

    AgentEvolutionSystem

)

def test_agent_evolution():

    system = AgentEvolutionSystem()

    result = system.record_evolution(

        "Backend Agent",

        "v1.0",

        "v1.1",

        "Improved database optimization"

    )

    print("Agent Evolution Test")

    print("--------------------")

    print(result)

if __name__ == "__main__":

    test_agent_evolution()