from core.testing.learning_mode_validation_v01 import (

    LearningModeValidation

)

def test_learning_mode():

    system = LearningModeValidation()

    result = system.run_validation(

        "Test User",

        "Learn Python programming",

        [

            "Level Detection",

            "Adaptive Explanation",

            "Practice Tasks",

            "Feedback Adjustment"

        ]

    )

    print("Learning Mode Validation")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_learning_mode()