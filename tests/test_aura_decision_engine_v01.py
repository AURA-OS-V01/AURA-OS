from core.decision.aura_decision_engine_v01 import (

    AURADecisionEngine

)

def test_decision_engine():

    engine = AURADecisionEngine()

    decision = engine.evaluate(

        "Choose next task",

        [

            "Research",

            "Analyze"

        ]

    )

    improved = engine.improve_decision(

        decision["id"],

        0.9

    )

    outcome = engine.record_outcome(

        decision["id"],

        "Successful execution"

    )

    state = engine.get_state()

    assert decision["selected"] == "Research"

    assert improved["confidence"] == 0.9

    assert outcome["outcome"] == "Successful execution"

    assert state["total_decisions"] == 1

if __name__ == "__main__":

    test_decision_engine()