from uuid import uuid4

class StrategyOptimizer:

    """

    Learns successful workflows.

    """

    def __init__(self):

        self.strategies = []

    def evaluate(

        self,

        workflow,

        score

    ):

        strategy = {

            "id": str(uuid4()),

            "workflow": workflow,

            "score": score

        }

        self.strategies.append(

            strategy

        )

        return strategy

    def recommend(self):

        if not self.strategies:

            return None

        return max(

            self.strategies,

            key=lambda x: x["score"]

        )