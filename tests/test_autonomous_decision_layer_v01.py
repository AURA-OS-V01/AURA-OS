from core.operations.autonomous_decision_layer_v01 import (

    AutonomousDecisionLayer

)

def test_decision_layer():

    layer = AutonomousDecisionLayer()

    result = layer.evaluate(

        "Testing complete"

    )

    print("Autonomous Decision Layer Test")

    print("-----------------------------")

    print(result)

if __name__ == "__main__":

    test_decision_layer()