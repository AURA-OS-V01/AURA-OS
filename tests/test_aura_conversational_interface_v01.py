from core.interface.aura_conversational_interface_v01 import (

    AURAConversationalInterface

)

def test_conversational_interface():

    interface = AURAConversationalInterface()

    message = interface.receive_message(

        "User",

        "Analyze a new business opportunity"

    )

    response = interface.generate_response(

        message["id"],

        "I will analyze the opportunity and create a plan."

    )

    history = interface.get_history()

    print(

        "AURA Conversational Interface Test"

    )

    print(history)

    assert response["response"] == (

        "I will analyze the opportunity and create a plan."

    )

    assert len(

        history["conversations"]

    ) == 1

if __name__ == "__main__":

    test_conversational_interface()