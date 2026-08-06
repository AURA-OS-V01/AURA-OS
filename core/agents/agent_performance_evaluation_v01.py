from uuid import uuid4

from datetime import datetime

class AgentPerformanceEvaluation:

    """

    Tracks agent performance metrics.

    """

    def __init__(self):

        self.performance = []

    def record_performance(

        self,

        agent,

        tasks_completed,

        success_rate

    ):

        record = {

            "id": str(uuid4()),

            "agent": agent,

            "tasks_completed": tasks_completed,

            "success_rate": success_rate,

            "created":

                datetime.utcnow().isoformat()

        }

        self.performance.append(record)

        return record

    def get_performance(

        self,

        agent=None

    ):

        if agent:

            return [

                item

                for item in self.performance

                if item["agent"] == agent

            ]

        return self.performance