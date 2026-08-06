from core.agents.aura_agent_communication_bus_v01 import (

    AURAAgentCommunicationBus

)

def test_agent_communication_bus():

    bus = AURAAgentCommunicationBus()

    message = bus.send_message(

        "sales_agent",

        "research_agent",

        "Find new market opportunities"

    )

    inbox = bus.get_messages_for_agent(

        "research_agent"

    )

    print(

        "AURA Agent Communication Bus Test"

    )

    print(

        "----------------------------------"

    )

    print(message)

    print(inbox)

    assert message["status"] == (

        "delivered"

    )

    assert len(inbox) == 1

if __name__ == "__main__":

    test_agent_communication_bus()