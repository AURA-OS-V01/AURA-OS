from core.agents.memory.aura_agent_memory_system_v01 import (

    AURAAgentMemorySystem

)

def test_agent_memory_system():

    memory = AURAAgentMemorySystem()

    stored = memory.store_memory(

        "sales_agent",

        "experience",

        "Customer prefers automated solutions"

    )

    recalled = memory.recall_memory(

        "sales_agent"

    )

    searched = memory.search_memory(

        "sales_agent",

        "automated"

    )

    print(

        "AURA Agent Memory System Test"

    )

    print(

        "-----------------------------"

    )

    print(stored)

    print(recalled)

    print(searched)

    assert len(recalled) == 1

    assert len(searched) == 1

if __name__ == "__main__":

    test_agent_memory_system()