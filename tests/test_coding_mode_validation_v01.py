from core.testing.coding_mode_validation_v01 import (

    CodingModeValidation

)

def test_coding_mode():

    system = CodingModeValidation()

    result = system.run_validation(

        "Test User",

        "Create a web application",

        [

            "Architecture Planning",

            "Code Generation",

            "Testing",

            "Debugging"

        ]

    )

    print("Coding Mode Validation")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_coding_mode()