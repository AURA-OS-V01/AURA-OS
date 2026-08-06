from core.evolution.continuous_improvement_loop_v01 import (

    ContinuousImprovementLoop

)

def test_loop():

    loop = ContinuousImprovementLoop()

    cycle = loop.start_cycle(

        "Improve memory retrieval"

    )

    result = loop.complete_cycle(

        cycle["id"]

    )

    print("Continuous Improvement Loop Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_loop()