from intelligence.reasoning.engine import ReasoningEngine

def test_reasoning_engine():

    engine = ReasoningEngine()

    result = engine.analyze(

        "How can AURA improve itself?"

    )

    print("Reasoning Engine Test")

    print("--------------------")

    print(result)

if __name__ == "__main__":

    test_reasoning_engine()