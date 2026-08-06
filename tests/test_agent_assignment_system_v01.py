from core.self_builder.agent_assignment_system_v01 import (

    AgentAssignmentSystem

)

def test_agent_assignment_system():

    system = AgentAssignmentSystem()

    result = system.assign(

        "AURA Client Dashboard Architecture"

    )

    print("Agent Assignment System Test")

    print("----------------------------")

    print(result)

if __name__ == "__main__":

    test_agent_assignment_system()