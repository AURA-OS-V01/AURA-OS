from core.memory.aura_memory_connection_layer_v01 import (

    AURAMemoryConnectionLayer

)

def test_memory_connection():

    system = AURAMemoryConnectionLayer()

    system.store_memory(

        "Test User",

        "Prefers detailed explanations",

        "preference"

    )

    result = system.retrieve_memory(

        "Test User"

    )

    print("AURA Memory Connection Test")

    print("---------------------------")

    print(result)

if __name__ == "__main__":

    test_memory_connection()