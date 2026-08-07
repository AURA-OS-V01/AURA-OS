
from datetime import datetime, UTC

from uuid import uuid4

class AURAAgentExecutor:

    def __init__(self):

        self.results = []

    def execute(

        self,

        agent,

        task

    ):

        result = {

            "id": str(uuid4()),

            "agent": agent["name"] if agent else None,

            "task": task["task"],

            "status": "completed",

            "output": f"{agent['name']} completed: {task['task']}" if agent else "No agent found",

            "created": datetime.now(UTC).isoformat()

        }

        self.results.append(result)

        return result

    def history(self):

        return self.results

