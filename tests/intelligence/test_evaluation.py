from intelligence.evaluation.engine import EvaluationEngine

def test_evaluation():

    engine = EvaluationEngine()

    result = engine.evaluate(

        "Grow user base",

        "Users increased by 20%",

        "Users increase by 50%"

    )

    print("Evaluation Engine Test")

    print("---------------------")

    print(result)

if __name__ == "__main__":

    test_evaluation()