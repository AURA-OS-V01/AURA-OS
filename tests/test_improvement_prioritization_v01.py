from core.evolution.improvement_prioritization_v01 import (

    ImprovementPrioritizationEngine

)

def test_priority():

    engine = ImprovementPrioritizationEngine()

    engine.evaluate(

        "Improve memory retrieval",

        10,

        9,

        3

    )

    engine.evaluate(

        "Improve documentation",

        3,

        2,

        1

    )

    result = engine.prioritize()

    print("Improvement Prioritization Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_priority()