from core.self_builder.change_application_system_v01 import (

    ChangeApplicationSystem

)

def test_change_application():

    system = ChangeApplicationSystem()

    result = system.apply(

        "Add AURA user dashboard"

    )

    print("Change Application System Test")

    print("------------------------------")

    print(result)

if __name__ == "__main__":

    test_change_application()