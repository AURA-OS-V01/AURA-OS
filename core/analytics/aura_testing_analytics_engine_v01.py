from uuid import uuid4

from datetime import datetime

class AURATestingAnalyticsEngine:

    """

    Tracks AURA alpha testing performance.

    """

    def __init__(self):

        self.metrics = []

    def record_metric(

        self,

        user,

        metric,

        value

    ):

        entry = {

            "id": str(uuid4()),

            "user": user,

            "metric": metric,

            "value": value,

            "created":

                datetime.utcnow().isoformat()

        }

        self.metrics.append(entry)

        return entry

    def get_metrics(self):

        return self.metrics