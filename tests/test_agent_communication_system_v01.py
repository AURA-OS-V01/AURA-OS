from core.agents.agent_communication_system_v01 import (

    AgentCommunicationSystem

)

def test_agent_communication():

    system = AgentCommunicationSystem()

    result = system.send_message(

        "Architect Agent",

        "Backend Agent",

        "Create authentication service"

    )

    print("Agent Communication Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_agent_communication()