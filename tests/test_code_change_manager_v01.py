from core.self_builder.code_change_manager_v01 import (

    CodeChangeManager

)

def test_code_change_manager():

    manager = CodeChangeManager()

    change = manager.create_change_request(

        "Add AURA client dashboard"

    )

    result = manager.update_status(

        change["id"],

        "approved"

    )

    print("Code Change Manager Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_code_change_manager()