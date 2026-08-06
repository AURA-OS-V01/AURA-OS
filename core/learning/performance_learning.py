from uuid import uuid4

from datetime import datetime

class PerformanceLearningSystem:

    """

    Tracks performance of AURA decisions.

    """

    def __init__(self):

        self.metrics = []

    def record(

        self,

        system,

        result,

        score

    ):

        metric = {

            "id": str(uuid4()),

            "system": system,

            "result": result,

            "score": score,

            "timestamp":

                datetime.utcnow().isoformat()

        }

        self.metrics.append(

            metric

        )

        return metric

    def analyze(self):

        if not self.metrics:

            return {

                "average_score": 0

            }

        total = sum(

            item["score"]

            for item in self.metrics

        )

        return {

            "average_score":

                total / len(self.metrics),

            "samples":

                len(self.metrics)

        }