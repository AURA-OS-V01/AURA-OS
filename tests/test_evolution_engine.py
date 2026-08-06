from core.evolution.evolution_engine import (

    EvolutionEngine

)

def test_evolution_engine():

    engine = EvolutionEngine()

    proposal = engine.create_proposal(

        "AURA Runtime",

        "Improve decision speed"

    )

    approved = engine.approve_proposal(

        proposal["id"]

    )

    experiment = engine.run_experiment(

        proposal["id"]

    )

    change = engine.apply_change(

        proposal["id"]

    )

    state = engine.get_state()

    assert approved["status"] == "approved"

    assert experiment["status"] == "completed"

    assert experiment["result"] == "successful"

    assert change["status"] == "applied"

    assert len(state["proposals"]) == 1

if __name__ == "__main__":

    test_evolution_engine()