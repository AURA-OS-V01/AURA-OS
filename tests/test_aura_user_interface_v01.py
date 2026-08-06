from core.interface.aura_user_interface_v01 import (

    AURAUserInterface

)

def test_user_interface():

    ui = AURAUserInterface()

    session = ui.create_user_session(

        "Test User"

    )

    result = ui.select_mode(

        session["id"],

        "Research"

    )

    print("AURA User Interface Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_user_interface()