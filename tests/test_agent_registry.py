from agents.factory.registry import AgentRegistry

def test_registry():

    registry = AgentRegistry()

    agent = registry.register(

        "AURA Legal Agent",

        "legal_specialist",

        "Developer Agent"

    )

    print("Agent Registry Test")

    print("-------------------")

    print(agent)

    print(registry.get_agents())

if __name__ == "__main__":

    test_registry()