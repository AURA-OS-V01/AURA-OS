from intelligence.decision.engine import DecisionEngine

def test_decision():

    engine = DecisionEngine()

    result = engine.make_decision(

        "Choose business growth strategy",

        [

            "Build audience first",

            "Build product first",

            "Seek investment"

        ]

    )

    print("Decision Engine Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_decision()