from core.memory.decision_history_system_v01 import (

    DecisionHistorySystem

)

def test_decision_history():

    system = DecisionHistorySystem()

    result = system.record(

        "Create education mode",

        "Different age groups need adaptive explanations"

    )

    print("Decision History Test")

    print("--------------------")

    print(result)

if __name__ == "__main__":

    test_decision_history()