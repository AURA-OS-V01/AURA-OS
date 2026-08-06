from core.memory.aura_context_memory_engine_v01 import (

    AURAContextMemoryEngine

)

def test_context_memory():

    memory = AURAContextMemoryEngine()

    result = memory.store_memory(

        "User wants enterprise automation platform",

        "project"

    )

    found = memory.retrieve_memory(

        "enterprise"

    )

    state = memory.get_state()

    assert result["category"] == "project"

    assert len(found) == 1

    assert len(state["memory"]) == 1

if __name__ == "__main__":

    test_context_memory()