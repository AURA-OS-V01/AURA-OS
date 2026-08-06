from datetime import datetime

from uuid import uuid4

class ResultExchange:

    """

    Handles agent task handoffs and results.

    """

    def __init__(self):

        self.results = []

    def submit_result(

        self,

        agent: str,

        task: str,

        result: dict,

        confidence: float

    ):

        entry = {

            "id": str(uuid4()),

            "agent": agent,

            "task": task,

            "result": result,

            "confidence": confidence,

            "timestamp": datetime.utcnow().isoformat()

        }

        self.results.append(entry)

        return entry

    def get_results(self):

        return self.results

    def get_agent_results(

        self,

        agent: str

    ):

        return [

            result

            for result in self.results

            if result["agent"] == agent

        ]