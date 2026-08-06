from aura_platform.interface.user_interface_foundation_v01 import (

    UserInterfaceFoundation

)

def test_user_interface():

    interface = UserInterfaceFoundation()

    result = interface.create_session(

        "Education"

    )

    print("User Interface Foundation Test")

    print("-----------------------------")

    print(result)

if __name__ == "__main__":

    test_user_interface()