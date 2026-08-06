from agents.memory.memory_store import MemoryStore

def test_memory():

    memory = MemoryStore(

        "test_memory.json"

    )

    saved = memory.store(

        "Research Agent",

        {

            "knowledge":

            "AI automation market growing"

        }

    )

    recalled = memory.recall(

        "Research Agent"

    )

    print("Memory Store Test")

    print("-----------------")

    print(saved)

    print(recalled)

if __name__ == "__main__":

    test_memory()