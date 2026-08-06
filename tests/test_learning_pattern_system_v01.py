from core.memory.learning_pattern_system_v01 import (

    LearningPatternSystem

)

def test_learning_patterns():

    system = LearningPatternSystem()

    result = system.record(

        "Examples improve learning",

        "Education"

    )

    print("Learning Pattern System Test")

    print("---------------------------")

    print(result)

if __name__ == "__main__":

    test_learning_patterns()