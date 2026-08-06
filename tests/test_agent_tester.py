from agents.factory.generator import AgentGenerator

from agents.factory.tester import AgentTester

def test_agent_tester():

    generator = AgentGenerator()

    blueprint = generator.create_blueprint(

        "AURA Legal Agent",

        "legal_specialist",

        "Compliance assistance"

    )

    tester = AgentTester()

    result = tester.test_blueprint(

        blueprint

    )

    print("Agent Testing System Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_agent_tester()
    