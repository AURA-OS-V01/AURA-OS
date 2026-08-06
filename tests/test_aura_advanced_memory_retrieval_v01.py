from core.memory.aura_advanced_memory_retrieval_v01 import (

    AURAAdvancedMemoryRetrieval

)

def test_advanced_memory():

    system = AURAAdvancedMemoryRetrieval()

    system.store_memory(

        "Test User",

        "Building AURA platform",

        "project",

        10

    )

    result = system.retrieve_relevant(

        "Test User",

        "project"

    )

    print("AURA Advanced Memory Retrieval Test")

    print("-----------------------------------")

    print(result)

if __name__ == "__main__":

    test_advanced_memory()