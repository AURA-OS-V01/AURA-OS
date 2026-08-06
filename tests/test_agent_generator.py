from agents.factory.generator import AgentGenerator

def test_generator():

    generator = AgentGenerator()

    blueprint = generator.create_blueprint(

        "AURA Legal Agent",

        "legal_specialist",

        "Help with compliance and legal analysis"

    )

    print("Agent Generator Test")

    print("--------------------")

    print(blueprint)

if __name__ == "__main__":

    test_generator()