from uuid import uuid4

from datetime import datetime

class ContinuousImprovementLoop:

    """

    Coordinates repeating improvement cycles.

    """

    def __init__(self):

        self.cycles = []

    def start_cycle(

        self,

        objective

    ):

        cycle = {

            "id": str(uuid4()),

            "objective": objective,

            "steps": [

                "research",

                "prioritize",

                "experiment",

                "evaluate",

                "learn"

            ],

            "status": "running",

            "created":

                datetime.utcnow().isoformat()

        }

        self.cycles.append(

            cycle

        )

        return cycle

    def complete_cycle(

        self,

        cycle_id

    ):

        for cycle in self.cycles:

            if cycle["id"] == cycle_id:

                cycle["status"] = "completed"

                return cycle

        return None