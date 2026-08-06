from uuid import uuid4

class ImprovementPrioritizationEngine:

    """

    Ranks improvement opportunities.

    """

    def __init__(self):

        self.improvements = []

    def evaluate(

        self,

        name,

        impact,

        urgency,

        difficulty

    ):

        score = (

            impact +

            urgency -

            difficulty

        )

        improvement = {

            "id": str(uuid4()),

            "name": name,

            "impact": impact,

            "urgency": urgency,

            "difficulty": difficulty,

            "score": score

        }

        self.improvements.append(

            improvement

        )

        return improvement

    def prioritize(self):

        return sorted(

            self.improvements,

            key=lambda x: x["score"],

            reverse=True

        )