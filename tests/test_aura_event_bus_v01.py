from core.runtime.aura_event_bus_v01 import (

    AURAEventBus

)

def test_event_bus():

    bus = AURAEventBus()

    received = []

    def handler(event):

        received.append(

            event

        )

    bus.subscribe(

        "agent_started",

        handler

    )

    event = bus.publish(

        "agent_started",

        {

            "agent": "Research Agent"

        }

    )

    state = bus.get_state()

    assert event["event"] == "agent_started"

    assert len(received) == 1

    assert received[0]["payload"]["agent"] == "Research Agent"

    assert len(state["events"]) == 1

if __name__ == "__main__":

    test_event_bus()