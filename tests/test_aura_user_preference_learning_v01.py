from core.learning.aura_user_preference_learning_v01 import (

    AURAUserPreferenceLearning

)

def test_preference_learning():

    system = AURAUserPreferenceLearning()

    system.learn_preference(

        "Test User",

        "response_style",

        "detailed"

    )

    result = system.get_preferences(

        "Test User"

    )

    print("AURA User Preference Learning Test")

    print("----------------------------------")

    print(result)

if __name__ == "__main__":

    test_preference_learning()