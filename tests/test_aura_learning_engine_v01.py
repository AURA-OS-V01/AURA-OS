from core.memory.aura_memory_store_v01 import (

    AURAMemoryStore

)

from core.learning.aura_learning_engine_v01 import (

    AURALearningEngine

)

def test_learning_engine():

    memory = AURAMemoryStore()

    memory.store(

        "performance",

        "Agent improved task completion"

    )

    engine = AURALearningEngine(

        memory

    )

    analysis = engine.analyze_memory(

        "performance"

    )

    engine.create_improvement(

        "Research Agent",

        "Improve information retrieval"

    )

    proposed = engine.learning_cycles[0].copy()

    applied = engine.apply_learning(

        proposed["id"]

    )

    state = engine.get_state()

    assert analysis["patterns_found"] is True

    assert proposed["status"] == "proposed"

    assert applied["status"] == "applied"

    assert state["total"] == 1

if __name__ == "__main__":

    test_learning_engine()