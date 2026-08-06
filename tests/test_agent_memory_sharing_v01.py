from core.agents.agent_memory_sharing_v01 import (

    AgentMemorySharing

)

def test_agent_memory():

    memory = AgentMemorySharing()

    memory.store_memory(

        "Architect Agent",

        "Use caching for performance"

    )

    result = memory.retrieve_memories()

    print("Agent Memory Sharing Test")

    print("-------------------------")

    print(result)

if __name__ == "__main__":

    test_agent_memory()