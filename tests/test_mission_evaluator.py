from core.evaluation.mission_evaluator import MissionEvaluator

def test_evaluator():

    evaluator = MissionEvaluator()

    result = evaluator.evaluate(

        "AI Business Discovery",

        True,

        [

            "Research Agent found opportunities",

            "Finance Agent ranked risks"

        ]

    )

    print("Mission Evaluation Test")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_evaluator()