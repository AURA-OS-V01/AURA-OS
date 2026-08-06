from core.memory.aura_memory_store_v01 import (

    AURAMemoryStore

)

def test_memory_store():

    memory = AURAMemoryStore()

    saved = memory.store(

        "agent_performance",

        "Research Agent completed task successfully",

        {

            "score": 100

        }

    )

    retrieved = memory.retrieve(

        "agent_performance"

    )

    results = memory.search(

        "successfully"

    )

    state = memory.get_state()

    assert saved["category"] == "agent_performance"

    assert len(retrieved) == 1

    assert len(results) == 1

    assert state["total_memories"] == 1

if __name__ == "__main__":

    test_memory_store()