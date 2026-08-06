from memory.agent_memory import AgentMemory

def test_memory():

    memory = AgentMemory()

    saved = memory.remember(

        "security-agent",

        "Found unused permission risk",

        "security_lesson"

    )

    print("Memory System Test")

    print("------------------")

    print(saved)

    print(memory.recall("security-agent"))

if __name__ == "__main__":

    test_memory()