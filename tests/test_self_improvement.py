from intelligence.self_improvement.improvement_engine import SelfImprovementEngine

def test_self_improvement():

    engine = SelfImprovementEngine()

    proposal = engine.create_proposal(

        "Agents need better testing",

        "Create a dedicated QA Agent"

    )

    print("Self Improvement Test")

    print("---------------------")

    print(proposal)

if __name__ == "__main__":

    test_self_improvement()