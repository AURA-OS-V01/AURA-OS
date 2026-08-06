from core.testing.personal_assistant_mode_validation_v01 import (

    PersonalAssistantModeValidation

)

def test_personal_assistant():

    system = PersonalAssistantModeValidation()

    result = system.run_validation(

        "Test User",

        "Help me plan my week",

        [

            "Identity",

            "Memory",

            "Preferences",

            "Planning"

        ]

    )

    print("Personal Assistant Validation")

    print("----------------------------")

    print(result)

if __name__ == "__main__":

    test_personal_assistant()